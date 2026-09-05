#!/usr/bin/env python3
"""
Deterministic relevance prioritisation before LLM screening (P4).

WHAT THIS DOES
  Ranks deduplicated studies by how many of the protocol's CONCEPTS each one matches, so
  the LLM screens the most promising first when a pool is too large to read whole. It
  writes a screening worksheet the LLM fills in, and records exactly what it cut and why.

WHAT THIS DOES NOT DO
  It does NOT decide inclusion. A study it defers is not excluded — it is unread, and the
  PRISMA flow says so in those words. Ranking by concept hits is a crude proxy for
  relevance and is allowed to be wrong; that is why the two recall floors below exist.

THREE RULES, EACH GUARDING A KNOWN WAY THIS GOES WRONG
  1. The score only ever ADDS, and the scope bonus is worth LESS than one concept hit. An
     out-of-scope study sorts lower but is never penalised, and the bonus can never lift a
     less topical study above a more topical one.
  2. An EMPTY scope signal means UNKNOWN, not OUT. PubMed carries no field-of-study data;
     treating "no signal" as "wrong field" would push every biomedical record below every
     record from a source that happens to label its fields.
  3. Two recall floors override the percentage. A percentage is a relative quantity;
     losing a relevant study is an absolute loss.
       - min_candidates      : a pool at or below this is screened IN FULL, nothing cut.
       - full_coverage_floor : a study matching EVERY concept is never cut, at any rank.
                               Under the CURRENT scoring a full-coverage study almost always
                               ranks above the cut on its own, so this floor mostly guards two
                               narrower cases: a tie exactly at the cut line, and any future
                               scoring change (citation counts, recency weighting) that could
                               let a fully-matching study be outranked. Keep it — that is the
                               shape of the loss it is named after.

CALIBRATION — READ THIS BEFORE TRUSTING THE DEFAULTS
  These numbers are NOT measured on this harness's own corpora; no pre-screening record
  set existed to measure against when they were chosen. They are set deliberately
  cautious for the pool sizes this harness actually produces (tens of studies, where any
  cut is dangerous), so that the prefilter is inert on a normal run and only engages on
  the large pulls that wide-recall sources now make possible. Re-measure before tightening
  them, and record the measurement — do not tighten on intuition.

No LLM. No network. Pure function of (studies, concepts, config) -> identical output.
Exit code: 0 always; the report and the worksheet are the deliverable.
"""

import argparse
import json
import math
import re
import sys

CONCEPT_WEIGHT = 2       # each distinct concept matched
SCOPE_BONUS = 1          # deliberately LESS than one concept hit: it may break a tie between
                         # equally topical studies, but can never lift a less topical study
                         # above a more topical one. A bonus equal to a concept hit would do
                         # exactly that, which is the bug this asymmetry exists to prevent.
MIN_CANDIDATES = 150     # pool <= this is screened in full (see CALIBRATION above)
FULL_COVERAGE_FLOOR = True
TARGET_PERCENT = 25      # of the pool, when the pool exceeds MIN_CANDIDATES
MAX_CANDIDATES = 600     # cost ceiling on the PERCENTAGE rule only; floors may exceed it


def read_jsonl(path):
    out = []
    with open(path, encoding='utf-8') as fh:
        for n, line in enumerate(fh, start=1):
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as exc:
                sys.stderr.write(f'{path}:{n}: not valid JSON — {exc}\n')
                raise SystemExit(2)
    return out


def compile_concepts(spec):
    """spec: {"concepts": [{"name": ..., "terms": [...]}, ...], "scope_terms": [...]}"""
    concepts = []
    for c in spec.get('concepts', []):
        pats = [re.compile(r'\b' + re.escape(t.lower()) + r'\b' if ' ' not in t
                           else re.escape(t.lower()), re.IGNORECASE)
                for t in c.get('terms', []) if t]
        concepts.append((c.get('name') or '(unnamed)', pats))
    scope = [re.compile(re.escape(t.lower()), re.IGNORECASE) for t in spec.get('scope_terms', []) if t]
    return concepts, scope


def haystack(study):
    return ' '.join(str(study.get(f) or '') for f in ('title', 'abstract', 'journal'))


def score_study(study, concepts, scope_pats):
    text = haystack(study)
    hits = [name for name, pats in concepts if any(p.search(text) for p in pats)]
    if not scope_pats:
        scope = 'unknown'                       # no scope declared: nothing to judge against
    elif any(p.search(text) for p in scope_pats):
        scope = 'in'
    else:
        scope = 'unknown' if not study.get('abstract') else 'out'
    bonus = SCOPE_BONUS if scope == 'in' else 0   # rule 1: only ever added
    return {
        'concept_hits': hits,
        'n_concepts': len(hits),
        'scope': scope,
        'score': len(hits) * CONCEPT_WEIGHT + bonus,
        'full_coverage': len(concepts) > 0 and len(hits) == len(concepts),
    }


def prioritise(studies, concepts, scope_pats, cfg):
    scored = []
    for s in studies:
        sc = score_study(s, concepts, scope_pats)
        scored.append({**s, '_score': sc})

    retracted = [s for s in scored if s.get('retracted') is True]
    live = [s for s in scored if s.get('retracted') is not True]

    # Deterministic order: score desc, most recent, title, then study_id. The study_id tiebreak
    # is what makes the result independent of INPUT ORDER — without it a stable sort silently
    # falls back to the order the sources happened to return, so re-running the same search in a
    # different order would screen a different subset.
    live.sort(key=lambda s: (-s['_score']['score'], -(s.get('year') or 0),
                             str(s.get('title') or ''), str(s.get('study_id') or '')))

    n = len(live)
    reasons = {}
    if cfg['target_percent'] is None:                       # top_k mode: a human set the budget
        k = min(cfg['max_candidates'], n)
        rule = f'top_k (target_percent explicitly null) → k={k}'
    elif n <= cfg['min_candidates']:
        k = n
        rule = f'recall floor: pool {n} ≤ min_candidates {cfg["min_candidates"]} → screen in full'
    else:
        pct_k = math.ceil(n * cfg['target_percent'] / 100)
        # The ceiling caps the PERCENTAGE only. The recall floor then raises k and is allowed
        # to exceed the ceiling: a pool that large means the query needs tightening, which is a
        # human decision — capping the floor here would be exactly the silent cut it exists to stop.
        k = max(min(pct_k, cfg['max_candidates']), cfg['min_candidates'])
        k = min(k, n)
        rule = (f'{cfg["target_percent"]}% of {n} = {pct_k}, capped at max_candidates '
                f'{cfg["max_candidates"]}, then raised to min_candidates {cfg["min_candidates"]} '
                f'if lower → k={k}')

    keep_idx = set(range(k))
    for i, s in enumerate(live):
        if i in keep_idx:
            reasons[i] = 'rank'
        elif cfg['full_coverage_floor'] and s['_score']['full_coverage']:
            keep_idx.add(i)                                  # rule 3: never cut a full-concept match
            reasons[i] = 'full_coverage_floor'

    over_cap = len(keep_idx) > cfg['max_candidates']
    candidates = [live[i] for i in sorted(keep_idx)]
    deferred = [live[i] for i in range(n) if i not in keep_idx]
    stats = {
        'studies_in': len(studies),
        'retracted_excluded': len(retracted),
        'ranked': n,
        'rule': rule,
        'k_from_rule': k,
        'candidates': len(candidates),
        'deferred': len(deferred),
        'kept_by_full_coverage_floor': sum(1 for r in reasons.values() if r == 'full_coverage_floor'),
        'over_cap': over_cap,
        'scope_split': {
            'in': sum(1 for s in live if s['_score']['scope'] == 'in'),
            'out': sum(1 for s in live if s['_score']['scope'] == 'out'),
            'unknown': sum(1 for s in live if s['_score']['scope'] == 'unknown'),
        },
    }
    return candidates, deferred, retracted, stats


def render(candidates, deferred, retracted, stats, concepts, args):
    out = []
    out.append('# Deterministic Relevance Prioritisation (P4)')
    out.append('')
    out.append('> Ranks studies by concept coverage so the LLM screens the most promising first.')
    out.append('> **A deferred study is UNREAD, not excluded** — the PRISMA flow must say so in those')
    out.append('> words. Scores only ever add; an empty scope signal means unknown, never out; a study')
    out.append('> matching every concept is never cut. No LLM, no network; identical output every run.')
    out.append('')
    out.append(f'- input: `{args.studies}` · concepts: `{args.concepts}`')
    out.append(f'- config: target_percent={args.target_percent} · min_candidates={args.min_candidates} '
               f'· max_candidates={args.max_candidates} · full_coverage_floor={not args.no_full_coverage_floor}')
    out.append(f'- concepts ({len(concepts)}): ' + ', '.join(f'`{n}`' for n, _ in concepts))
    out.append('')
    out.append('## Counts')
    out.append(f'- studies in: **{stats["studies_in"]}**')
    if stats['retracted_excluded']:
        out.append(f'- **retracted, excluded before ranking: {stats["retracted_excluded"]}** '
                   '(a retracted study cites cleanly — real PMID, real record, withdrawn science)')
    out.append(f'- ranked: **{stats["ranked"]}**')
    out.append(f'- selection rule: {stats["rule"]}')
    out.append(f'- candidates to screen: **{stats["candidates"]}** '
               f'(of which {stats["kept_by_full_coverage_floor"]} kept by the full-coverage floor)')
    out.append(f'- deferred (unread, NOT excluded): **{stats["deferred"]}**')
    out.append(f'- scope split: in {stats["scope_split"]["in"]} · out {stats["scope_split"]["out"]} '
               f'· unknown {stats["scope_split"]["unknown"]}')
    if stats['over_cap']:
        out.append('- ⚠ **over_cap**: the recall floors kept more than max_candidates. Nothing was cut '
                   'back — a pool this large means the query needs tightening, and that is a human '
                   'decision, not a silent trim.')
    out.append('')
    if retracted:
        out.append(f'## Retracted — excluded, never citable ({len(retracted)})')
        for s in retracted:
            out.append(f'- `{s.get("study_id")}` — {(s.get("title") or "")[:80]}')
        out.append('')
    out.append('## Screening worksheet — the LLM fills `verdict` and `reason`')
    out.append('')
    out.append('| study_id | year | concepts matched | scope | score | verdict | reason |')
    out.append('|---|---|---|---|---|---|---|')
    for s in candidates:
        sc = s['_score']
        out.append(f'| `{s.get("study_id")}` | {s.get("year") or "—"} | '
                   f'{len(sc["concept_hits"])}/{len(concepts)} '
                   f'({", ".join(sc["concept_hits"]) or "—"}) | {sc["scope"]} | {sc["score"]} |  |  |')
    out.append('')
    out.append(f'## Deferred — unread, available if the corpus proves thin ({len(deferred)})')
    if deferred:
        for s in deferred[:50]:
            sc = s['_score']
            out.append(f'- `{s.get("study_id")}` ({s.get("year") or "—"}) score {sc["score"]} — '
                       f'{(s.get("title") or "")[:70]}')
        if len(deferred) > 50:
            out.append(f'- … and {len(deferred) - 50} more (full list in the deferred JSONL)')
    else:
        out.append('- none — the whole pool is being screened')
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Deterministic relevance prioritisation (P4).')
    ap.add_argument('--studies', required=True, help='deduplicated studies JSONL (from dedupe_records.py)')
    ap.add_argument('--concepts', required=True, help='JSON: {"concepts":[{"name","terms"}],"scope_terms":[]}')
    ap.add_argument('--target-percent', type=lambda v: None if v.lower() == 'null' else int(v),
                    default=TARGET_PERCENT, help=f'percent of the pool to screen, or "null" for top_k '
                                                 f'(default {TARGET_PERCENT})')
    ap.add_argument('--min-candidates', type=int, default=MIN_CANDIDATES,
                    help=f'recall floor: a pool at or below this is screened in full (default {MIN_CANDIDATES})')
    ap.add_argument('--max-candidates', type=int, default=MAX_CANDIDATES,
                    help=f'cost ceiling on the percentage rule only (default {MAX_CANDIDATES})')
    ap.add_argument('--no-full-coverage-floor', action='store_true',
                    help='disable the "a study matching every concept is never cut" floor')
    ap.add_argument('--out-candidates', help='write candidates as JSONL to this path')
    ap.add_argument('--out-deferred', help='write deferred studies as JSONL to this path')
    ap.add_argument('--out', help='write the human-readable worksheet/report to this path')
    args = ap.parse_args(argv)

    studies = read_jsonl(args.studies)
    with open(args.concepts, encoding='utf-8') as fh:
        concepts, scope_pats = compile_concepts(json.load(fh))
    cfg = {
        'target_percent': args.target_percent,
        'min_candidates': args.min_candidates,
        'max_candidates': args.max_candidates,
        'full_coverage_floor': not args.no_full_coverage_floor,
    }
    candidates, deferred, retracted, stats = prioritise(studies, concepts, scope_pats, cfg)

    for path, rows in ((args.out_candidates, candidates), (args.out_deferred, deferred)):
        if path:
            with open(path, 'w', encoding='utf-8') as fh:
                for r in rows:
                    fh.write(json.dumps(r, ensure_ascii=False, sort_keys=True) + '\n')
    report = render(candidates, deferred, retracted, stats, concepts, args)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(report)
    sys.stdout.write(report)
    return 0


if __name__ == '__main__':
    sys.exit(main())
