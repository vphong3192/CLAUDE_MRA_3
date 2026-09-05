#!/usr/bin/env python3
"""
Import bibliographic exports the author downloaded themselves (P7).

WHY THIS EXISTS
  The harness reaches PubMed, Elicit, preprint servers and trial registries through MCP. It has no
  Scopus, Web of Science, Embase or CENTRAL access, and it never will: those are subscription
  databases behind the author's institutional login. But the AUTHOR has that login. Exporting a
  result set and dropping the file on disk is the single largest recall gain available, and it
  costs the harness no credential at all.

  This script only ever READS FILES FROM DISK. It must never query those platforms — doing so
  would use someone's subscription through an automated agent, which their licence forbids.

WHAT IT DOES
  Parses RIS, NBIB/MEDLINE, BibTeX and CSV exports into the same record schema the rest of the
  pipeline uses, so step P4 dedupes and screens them alongside everything else with no special
  casing anywhere downstream.

THE MANIFEST IS NOT OPTIONAL
  An export file carries records but not the search that produced them. PRISMA-S requires the
  query string, the date searched, the database name, and the number of hits the platform
  reported — none of which survive an export. So every file needs a manifest entry declaring
  them, and a file without one is a HARD-FAIL rather than a silent import: an unrecorded search
  is an unreproducible one, and it would sit in the corpus looking exactly like a recorded one.

  `prisma_column` is declared per file, not guessed. A Scopus export belongs in PRISMA 2020's
  "databases and registers" column because it IS a database search; calling it "other methods"
  because it arrived by hand understates the systematic search. A file of references a colleague
  suggested genuinely is "other".

  `n_reported` (what the platform said it found) is compared against what parsed. A gap means
  the export was truncated — the commonest silent recall loss in a manual export, since most
  platforms cap a single download well below the result count.

No LLM. No network. Pure function of (files on disk) -> identical output every run.
Exit code: 0 if every file imported cleanly, 1 on any manifest or parse failure.
"""

import argparse
import csv
import json
import re
import sys
from pathlib import Path

REQUIRED_MANIFEST_FIELDS = ('file', 'label', 'database', 'query_string', 'date_searched',
                            'n_reported', 'prisma_column')
PRISMA_COLUMNS = ('database', 'other')
SUPPORTED = {'.ris': 'ris', '.nbib': 'nbib', '.txt': 'nbib', '.bib': 'bibtex', '.csv': 'csv'}

DOI_RE = re.compile(r'10\.\d{4,9}/[^\s"\'<>)\],;]+')
PMID_RE = re.compile(r'\b(\d{7,9})\b')
NCT_RE = re.compile(r'\bNCT\d{8}\b', re.IGNORECASE)
YEAR_RE = re.compile(r'\b(1[89]\d{2}|20\d{2}|21\d{2})\b')

# CSV headers differ per platform; map the ones that actually appear in Scopus/WoS/Embase exports.
CSV_ALIASES = {
    'title': ('title', 'document title', 'article title', 'ti'),
    'authors': ('authors', 'author full names', 'author(s) id', 'au'),
    'year': ('year', 'publication year', 'py'),
    'journal': ('source title', 'journal', 'publication title', 'so'),
    'doi': ('doi', 'di'),
    'pmid': ('pubmed id', 'pmid', 'pm'),
    'abstract': ('abstract', 'ab'),
    'publication_types': ('document type', 'publication type', 'dt'),
}


def blank_record():
    return {'pmid': None, 'doi': None, 'nct': None, 'title': None, 'authors': None,
            'year': None, 'journal': None, 'abstract': None, 'publication_types': [],
            'retracted': None}


def _clean(v):
    v = (v or '').strip()
    return v or None


def _year(v):
    m = YEAR_RE.search(str(v or ''))
    return int(m.group(1)) if m else None


def _ids_from(text, rec):
    """Identifiers hide in different tags per platform; sweep the record text for them."""
    if not rec.get('doi'):
        m = DOI_RE.search(text)
        if m:
            rec['doi'] = m.group(0).rstrip('.')
    if not rec.get('nct'):
        m = NCT_RE.search(text)
        if m:
            rec['nct'] = m.group(0).upper()


def parse_ris(text):
    """RIS: two-letter tag, two spaces, hyphen, space. Records end at ER.

    A wrapped field continues on indented lines with no tag. Those MUST be folded back in:
    abstracts routinely wrap, they feed concept matching and screening, and a silently truncated
    abstract loses recall without leaving a trace anywhere.
    """
    records, rec, buf = [], blank_record(), []
    tag_re = re.compile(r'^([A-Z][A-Z0-9])\s{2}-\s?(.*)$')
    authors, types = [], []
    last_tag, last_target = None, None

    def fold(text_):
        """Append a continuation line to whichever field the last tag wrote."""
        if last_target == 'author' and authors:
            authors[-1] += ' ' + text_
        elif last_target and rec.get(last_target):
            rec[last_target] += ' ' + text_

    for line in text.splitlines():
        m = tag_re.match(line)
        if not m:
            if last_tag and line.strip():          # continuation of the previous field
                buf.append(line.strip())
                fold(line.strip())
            continue
        tag, val = m.group(1), m.group(2).strip()
        last_tag = tag
        last_target = {'TI': 'title', 'T1': 'title', 'AB': 'abstract', 'N2': 'abstract',
                       'JO': 'journal', 'JF': 'journal', 'T2': 'journal', 'J2': 'journal',
                       'AU': 'author', 'A1': 'author'}.get(tag)
        buf.append(line)
        if tag == 'ER':
            _ids_from('\n'.join(buf), rec)
            rec['authors'] = '; '.join(authors) or None
            rec['publication_types'] = types
            records.append(rec)
            rec, buf, authors, types = blank_record(), [], [], []
            last_tag, last_target = None, None
            continue
        if tag in ('TI', 'T1') and not rec['title']:
            rec['title'] = val
        elif tag in ('AU', 'A1'):
            authors.append(val)
        elif tag in ('PY', 'Y1') and not rec['year']:
            rec['year'] = _year(val)
        elif tag in ('JO', 'JF', 'T2', 'J2') and not rec['journal']:
            rec['journal'] = val
        elif tag in ('AB', 'N2') and not rec['abstract']:
            rec['abstract'] = val
        elif tag == 'DO' and not rec['doi']:
            rec['doi'] = val
        elif tag in ('AN', 'ID') and not rec['pmid'] and re.fullmatch(r'\d{7,9}', val):
            rec['pmid'] = val
        elif tag == 'TY' and val:
            types.append(val)
    return records


def parse_nbib(text):
    """NBIB/MEDLINE: four-char tag, hyphen, space; continuations are indented six spaces."""
    records = []
    for block in re.split(r'\n\s*\n', text):
        if not block.strip():
            continue
        rec, authors, types = blank_record(), [], []
        fields = {}
        cur = None
        for line in block.splitlines():
            m = re.match(r'^([A-Z]{2,4})\s*-\s?(.*)$', line)
            if m:
                cur = m.group(1)
                fields.setdefault(cur, []).append(m.group(2).strip())
            elif cur and line.startswith('      '):
                fields[cur][-1] += ' ' + line.strip()
        if not fields:
            continue
        rec['pmid'] = _clean((fields.get('PMID') or [''])[0])
        rec['title'] = _clean((fields.get('TI') or [''])[0])
        rec['abstract'] = _clean((fields.get('AB') or [''])[0])
        rec['journal'] = _clean((fields.get('TA') or fields.get('JT') or [''])[0])
        rec['year'] = _year((fields.get('DP') or [''])[0])
        authors = fields.get('FAU') or fields.get('AU') or []
        types = [t for t in fields.get('PT', []) if t]
        for tag in ('LID', 'AID', 'SI'):
            for v in fields.get(tag, []):
                _ids_from(v, rec)
        rec['authors'] = '; '.join(authors) or None
        rec['publication_types'] = types
        rec['retracted'] = True if any('retract' in t.lower() for t in types) else None
        records.append(rec)
    return records


def parse_bibtex(text):
    """BibTeX: brace-balanced entries; values may be braced or quoted."""
    records = []
    for m in re.finditer(r'@(\w+)\s*\{', text):
        start = m.end() - 1
        depth, i = 0, start
        while i < len(text):
            if text[i] == '{':
                depth += 1
            elif text[i] == '}':
                depth -= 1
                if depth == 0:
                    break
            i += 1
        body = text[start + 1:i]
        rec = blank_record()
        fields = dict((k.lower(), v.strip().strip('{}"').strip())
                      for k, v in re.findall(r'(\w+)\s*=\s*[{"](.*?)[}"]\s*,?\s*(?=\w+\s*=|$)',
                                             body, re.DOTALL))
        rec['title'] = _clean(fields.get('title'))
        rec['authors'] = _clean(fields.get('author'))
        rec['year'] = _year(fields.get('year'))
        rec['journal'] = _clean(fields.get('journal') or fields.get('booktitle'))
        rec['abstract'] = _clean(fields.get('abstract'))
        rec['doi'] = _clean(fields.get('doi'))
        rec['publication_types'] = [m.group(1)] if m.group(1) else []
        _ids_from(body, rec)
        records.append(rec)
    return records


def parse_csv(text):
    records = []
    reader = csv.DictReader(text.splitlines())
    if not reader.fieldnames:
        return records
    lower = {(f or '').strip().lower(): f for f in reader.fieldnames}
    pick = {}
    for field, aliases in CSV_ALIASES.items():
        for a in aliases:
            if a in lower:
                pick[field] = lower[a]
                break
    for row in reader:
        rec = blank_record()
        for field, col in pick.items():
            val = _clean(row.get(col))
            if field == 'year':
                rec['year'] = _year(val)
            elif field == 'publication_types':
                rec['publication_types'] = [val] if val else []
            else:
                rec[field] = val
        _ids_from(' '.join(str(v) for v in row.values() if v), rec)
        if any((rec['title'], rec['doi'], rec['pmid'])):
            records.append(rec)
    return records


PARSERS = {'ris': parse_ris, 'nbib': parse_nbib, 'bibtex': parse_bibtex, 'csv': parse_csv}


def check_manifest(entries, present_files):
    """Return (by_filename, errors). Every file on disk needs an entry and every field."""
    errors, by_file = [], {}
    for i, e in enumerate(entries):
        missing = [f for f in REQUIRED_MANIFEST_FIELDS if e.get(f) in (None, '')]
        if missing:
            errors.append(f'manifest entry #{i + 1} ({e.get("file") or "unnamed"}) '
                          f'missing: {", ".join(missing)} — PRISMA-S requires each of these, and '
                          f'an export does not carry them')
            continue
        if e['prisma_column'] not in PRISMA_COLUMNS:
            errors.append(f'{e["file"]}: prisma_column must be one of {PRISMA_COLUMNS}, '
                          f'got "{e["prisma_column"]}"')
            continue
        if not isinstance(e['n_reported'], int):
            errors.append(f'{e["file"]}: n_reported must be an integer (what the platform said '
                          f'it found), got {e["n_reported"]!r}')
            continue
        by_file[e['file']] = e
    for name in sorted(present_files):
        if name not in by_file:
            errors.append(f'{name} is on disk with no manifest entry — an unrecorded search is an '
                          f'unreproducible one, and it would sit in the corpus looking recorded')
    return by_file, errors


def import_dir(export_dir, manifest_path):
    export_dir = Path(export_dir)
    files = {p.name for p in sorted(export_dir.iterdir())
             if p.is_file() and p.suffix.lower() in SUPPORTED}
    with open(manifest_path, encoding='utf-8') as fh:
        manifest = json.load(fh)
    by_file, errors = check_manifest(manifest.get('exports', []), files)

    records, per_file = [], []
    for name in sorted(files):
        entry = by_file.get(name)
        if not entry:
            continue
        path = export_dir / name
        kind = SUPPORTED[path.suffix.lower()]
        try:
            parsed = PARSERS[kind](path.read_text(encoding='utf-8', errors='replace'))
        except Exception as exc:                       # a broken export must not pass as empty
            errors.append(f'{name}: {kind} parse failed — {exc}')
            continue
        label = entry['label']
        for n, rec in enumerate(parsed, start=1):
            rec.update({
                'record_id': f'EXT-{label}-{n:04d}',
                'source': f'external:{label}',
                'search_id': f'X-{label}',
                'provenance': 'user_export',
                'prisma_column': entry['prisma_column'],
            })
            records.append(rec)
        per_file.append({'file': name, 'kind': kind, 'label': label,
                         'n_reported': entry['n_reported'], 'n_parsed': len(parsed),
                         'prisma_column': entry['prisma_column'],
                         'query_string': entry['query_string'],
                         'date_searched': entry['date_searched'], 'database': entry['database']})
    return records, per_file, errors


def render(records, per_file, errors, args):
    out = ['# External Export Import (P7)', '']
    out.append('> Reads bibliographic exports the author downloaded from subscription databases.')
    out.append('> It only ever reads files from disk — it never queries those platforms, because an')
    out.append('> automated agent using someone\'s institutional subscription breaks their licence.')
    out.append('> Records land in the same schema as every other source, so P4 dedupes and screens')
    out.append('> them with no special casing. No LLM, no network; identical output every run.')
    out.append('')
    out.append(f'- exports: `{args.export_dir}` · manifest: `{args.manifest}`')
    out.append('')
    out.append('## Files')
    out.append('')
    if per_file:
        out.append('| file | format | database | reported | parsed | PRISMA column | date |')
        out.append('|---|---|---|---|---|---|---|')
        for f in per_file:
            gap = '' if f['n_parsed'] >= f['n_reported'] else '  ⚠'
            out.append(f'| `{f["file"]}` | {f["kind"]} | {f["database"]} | {f["n_reported"]} | '
                       f'{f["n_parsed"]}{gap} | {f["prisma_column"]} | {f["date_searched"]} |')
        out.append('')
        short = [f for f in per_file if f['n_parsed'] < f['n_reported']]
        if short:
            out.append('**⚠ Truncated exports — the commonest silent recall loss.** These files parsed')
            out.append('fewer records than the platform reported finding. Most platforms cap a single')
            out.append('download well below the result count, so re-export in batches before relying')
            out.append('on this corpus:')
            for f in short:
                out.append(f'- `{f["file"]}`: platform reported {f["n_reported"]}, '
                           f'file contains {f["n_parsed"]} — {f["n_reported"] - f["n_parsed"]} missing')
            out.append('')
    else:
        out.append('- none imported')
        out.append('')
    out.append('## Search strategies (for the Methods section)')
    out.append('')
    for f in per_file:
        out.append(f'- **{f["database"]}** ({f["date_searched"]}, {f["n_reported"]} hits reported): '
                   f'`{f["query_string"]}`')
    if not per_file:
        out.append('- none')
    out.append('')
    out.append(f'## Records imported: {len(records)}')
    out.append('')
    out.append(f'## Manifest / parse errors ({len(errors)})')
    if errors:
        for e in errors:
            out.append(f'- **{e}**')
        out.append('')
        out.append('Nothing from a failing file is imported. Fix the manifest and re-run.')
    else:
        out.append('- none')
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Import author-supplied bibliographic exports (P7).')
    ap.add_argument('--export-dir', required=True, help='source/<folder>/_exports/')
    ap.add_argument('--manifest', required=True, help='JSON declaring each file\'s search')
    ap.add_argument('--out-records', help='append/write records as JSONL to this path')
    ap.add_argument('--out', help='write the human-readable report to this path')
    args = ap.parse_args(argv)

    records, per_file, errors = import_dir(args.export_dir, args.manifest)
    if args.out_records:
        with open(args.out_records, 'w', encoding='utf-8') as fh:
            for r in records:
                fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n')
    report = render(records, per_file, errors, args)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(report)
    sys.stdout.write(report)
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
