#!/usr/bin/env python3
"""
Deterministic deduplication for the retrieved record set (P4).

WHAT THIS DOES
  Clusters the raw records from every source into one row per STUDY, so a paper that
  surfaced as a preprint, a journal article and a trial registration counts once — the
  rule literature-retrieval/SKILL.md already states, moved out of the LLM's hands.

  Cluster keys, strongest first:
    1. DOI   (normalised: lowercased, https://doi.org/ prefix stripped)
    2. PMID
    3. NCT
    4. fuzzy title match within the year guard

WHAT THIS DOES NOT DO
  It does not decide relevance, quality or inclusion. It does not merge a pair whose
  years sit outside the guard: a preprint and its journal version usually differ by
  0-1 years and merge, but a wider gap is REPORTED as a suspected pair for a human to
  judge — silently picking one venue, one year and one DOI for a pair the script cannot
  tell apart is worse than reporting it.

  Thresholds are hardcoded on purpose. Loosening them dismantles the guarantee; a
  regression test pins each one.

No LLM. No network. Pure function of (input records) -> identical output every run.
Exit code: 0 always (dedup has no failure verdict; the report is the deliverable).
"""

import argparse
import json
import re
import sys
import unicodedata
from difflib import SequenceMatcher

# --- Hardcoded thresholds. Do not read these from config; do not loosen them. ---
FUZZY_THRESHOLD = 0.92   # title similarity required to merge two records
YEAR_GUARD = 1           # merge only when |year difference| <= this
BLOCK_PREFIX = 12        # compare only titles sharing this normalised prefix (keeps it linear)

DOI_PREFIX_RE = re.compile(r'^(?:https?://)?(?:dx\.)?doi\.org/', re.IGNORECASE)
# Cold Spring Harbor's prefix — every bioRxiv/medRxiv preprint DOI. A merged study takes its
# identity from the PUBLISHED version when it has one (Law 3 downgrades preprints), so a
# 10.1101 DOI is the last choice for study_id, never the first.
PREPRINT_DOI_PREFIX = '10.1101/'
NON_ALNUM_RE = re.compile(r'[^a-z0-9 ]+')
WS_RE = re.compile(r'\s+')


def norm_doi(value):
    if not value:
        return None
    v = DOI_PREFIX_RE.sub('', str(value).strip()).strip().lower()
    return v or None


def norm_id(value):
    if value is None:
        return None
    v = re.sub(r'[^0-9A-Za-z]', '', str(value)).upper()
    return v or None


def norm_title(value):
    """Lowercase, strip accents and punctuation, collapse whitespace."""
    if not value:
        return ''
    v = unicodedata.normalize('NFKD', str(value))
    v = ''.join(c for c in v if not unicodedata.combining(c)).lower()
    return WS_RE.sub(' ', NON_ALNUM_RE.sub(' ', v)).strip()


def year_of(rec):
    y = rec.get('year')
    try:
        return int(str(y)[:4])
    except (TypeError, ValueError):
        return None


def read_jsonl(path):
    records = []
    with open(path, encoding='utf-8') as fh:
        for n, line in enumerate(fh, start=1):
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as exc:
                sys.stderr.write(f'{path}:{n}: not valid JSON — {exc}\n')
                raise SystemExit(2)
    return records


class Clusters:
    """Union-find over record indices, so merge order cannot change the result."""

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, i):
        while self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
            i = self.parent[i]
        return i

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.parent[max(ra, rb)] = min(ra, rb)   # lowest index wins: deterministic


def dedupe(records):
    """Return (clusters, merge_log, suspected_pairs)."""
    cl = Clusters(len(records))
    merges = []          # (i, j, basis, detail)

    # --- 1-3: exact identifier match -------------------------------------------------
    for field, normaliser in (('doi', norm_doi), ('pmid', norm_id), ('nct', norm_id)):
        seen = {}
        for i, rec in enumerate(records):
            key = normaliser(rec.get(field))
            if not key:
                continue
            if key in seen:
                cl.union(seen[key], i)
                merges.append((seen[key], i, field, key))
            else:
                seen[key] = i

    # --- 4: fuzzy title within the year guard ---------------------------------------
    blocks = {}
    for i, rec in enumerate(records):
        t = norm_title(rec.get('title'))
        if len(t) < BLOCK_PREFIX:
            continue
        blocks.setdefault(t[:BLOCK_PREFIX], []).append(i)

    suspected = []
    for _, idxs in sorted(blocks.items()):
        for a in range(len(idxs)):
            for b in range(a + 1, len(idxs)):
                i, j = idxs[a], idxs[b]
                if cl.find(i) == cl.find(j):
                    continue
                ti, tj = norm_title(records[i].get('title')), norm_title(records[j].get('title'))
                ratio = SequenceMatcher(None, ti, tj).ratio()
                if ratio < FUZZY_THRESHOLD:
                    continue
                yi, yj = year_of(records[i]), year_of(records[j])
                if yi is not None and yj is not None and abs(yi - yj) > YEAR_GUARD:
                    # Outside the guard: report, never merge. Picking one venue/year/DOI
                    # for a pair the script cannot tell apart is a silent wrong answer.
                    suspected.append((i, j, round(ratio, 3), yi, yj))
                    continue
                cl.union(i, j)
                merges.append((i, j, 'fuzzy_title', f'ratio {ratio:.3f}'))

    groups = {}
    for i in range(len(records)):
        groups.setdefault(cl.find(i), []).append(i)
    return [groups[k] for k in sorted(groups)], merges, suspected


def merge_cluster(records, idxs):
    """Build one study row. Identifiers and sources are UNIONED; never pick one and drop the rest."""
    members = [records[i] for i in idxs]
    out = {'study_id': None, 'members': len(members)}

    for field in ('pmid', 'doi', 'nct', 'pmcid'):
        normalise = norm_doi if field == 'doi' else norm_id
        vals, seen = [], set()
        for m in members:
            v = m.get(field)
            if not v:
                continue
            key = normalise(v)                 # 'https://doi.org/10.X' and '10.X' are ONE value
            if key and key not in seen:
                seen.add(key)
                vals.append(str(v))
        if field == 'doi' and len(vals) > 1:
            # published DOI first, preprint DOI last — identity follows the peer-reviewed record
            vals.sort(key=lambda d: (norm_doi(d) or '').startswith(PREPRINT_DOI_PREFIX))
        out[field] = vals[0] if vals else None
        if len(vals) > 1:                      # a real disagreement, not a formatting difference
            out.setdefault('id_conflicts', {})[field] = vals

    # longest title wins (subtitles get truncated by some sources), first non-empty otherwise
    out['title'] = max((m.get('title') or '' for m in members), key=len) or None
    for field in ('authors', 'journal', 'abstract'):
        out[field] = next((m.get(field) for m in members if m.get(field)), None)
    years = [y for y in (year_of(m) for m in members) if y is not None]
    out['year'] = min(years) if years else None          # earliest = first public appearance

    out['sources'] = sorted({m.get('source') for m in members if m.get('source')})
    out['search_ids'] = sorted({m.get('search_id') for m in members if m.get('search_id')})
    out['record_ids'] = [m.get('record_id') for m in members]
    types = []
    for m in members:
        for t in m.get('publication_types') or []:
            if t not in types:
                types.append(t)
    out['publication_types'] = types
    flags = [m.get('retracted') for m in members if m.get('retracted') is not None]
    out['retracted'] = True if any(flags) else (False if flags else None)

    out['study_id'] = (out['doi'] and f"doi:{norm_doi(out['doi'])}") \
        or (out['pmid'] and f"pmid:{norm_id(out['pmid'])}") \
        or (out['nct'] and f"nct:{norm_id(out['nct'])}") \
        or f"title:{norm_title(out['title'])[:60]}"
    return out


def render(records, studies, merges, suspected, args):
    by_source = {}
    for r in records:
        by_source[r.get('source') or '(unknown)'] = by_source.get(r.get('source') or '(unknown)', 0) + 1
    out = []
    out.append('# Deterministic Deduplication (P4)')
    out.append('')
    out.append('> One row per STUDY, not per record: a paper found as a preprint, a journal article')
    out.append('> and a trial registration counts once. Identifier match first, fuzzy title within the')
    out.append('> year guard second. Pairs outside the guard are REPORTED, never merged. Relevance and')
    out.append('> quality are not decided here. No LLM, no network; identical output every run.')
    out.append('')
    out.append(f'- input: `{args.records}`')
    out.append(f'- thresholds (hardcoded): fuzzy ≥ {FUZZY_THRESHOLD} · year guard ±{YEAR_GUARD} '
               f'· block prefix {BLOCK_PREFIX} chars')
    out.append('')
    out.append('## Counts')
    out.append(f'- records in: **{len(records)}**')
    for src in sorted(by_source):
        out.append(f'  - {src}: {by_source[src]}')
    out.append(f'- studies out: **{len(studies)}**')
    out.append(f'- duplicates removed: **{len(records) - len(studies)}**')
    out.append('')
    out.append(f'## Merges ({len(merges)})')
    if merges:
        for i, j, basis, detail in merges:
            ti = (records[i].get('title') or '')[:60]
            out.append(f'- `{basis}` ({detail}): [{i}] {ti}… ⇔ [{j}]')
    else:
        out.append('- none')
    out.append('')
    out.append(f'## Suspected pairs — NOT merged, human decides ({len(suspected)})')
    if suspected:
        out.append('Same title, years further apart than the guard. Usually a preprint and its journal')
        out.append('version, sometimes two genuinely different studies. Confirm before treating as one.')
        for i, j, ratio, yi, yj in suspected:
            out.append(f'- similarity {ratio} · {yi} vs {yj}: '
                       f'[{i}] {(records[i].get("title") or "")[:60]}… ⇔ [{j}]')
    else:
        out.append('- none')
    out.append('')
    conflicts = [s for s in studies if s.get('id_conflicts')]
    out.append(f'## Identifier conflicts inside a cluster ({len(conflicts)})')
    if conflicts:
        out.append('Merged records that disagree on an identifier. All values are kept in the row.')
        for s in conflicts:
            out.append(f'- `{s["study_id"]}`: {json.dumps(s["id_conflicts"], ensure_ascii=False)}')
    else:
        out.append('- none')
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Deterministic record deduplication (P4).')
    ap.add_argument('--records', required=True, help='_workspace/02_records.jsonl')
    ap.add_argument('--out-studies', help='write deduplicated studies as JSONL to this path')
    ap.add_argument('--out', help='write the human-readable report to this path')
    args = ap.parse_args(argv)

    records = read_jsonl(args.records)
    clusters, merges, suspected = dedupe(records)
    studies = [merge_cluster(records, idxs) for idxs in clusters]

    if args.out_studies:
        with open(args.out_studies, 'w', encoding='utf-8') as fh:
            for s in studies:
                fh.write(json.dumps(s, ensure_ascii=False, sort_keys=True) + '\n')
    report = render(records, studies, merges, suspected, args)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(report)
    sys.stdout.write(report)
    return 0


if __name__ == '__main__':
    sys.exit(main())
