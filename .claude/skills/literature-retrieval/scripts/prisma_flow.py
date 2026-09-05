#!/usr/bin/env python3
"""
Deterministic PRISMA 2020 flow (P4).

WHAT THIS DOES
  Counts the pipeline's own stage files and draws the flow from those numbers. Every box
  is a count of records on disk, so the diagram and the Methods section cannot drift from
  what actually ran.

THE RULE THAT MATTERS MOST — DRAW WHAT HAPPENED, NOT THE TEMPLATE
  Do not reproduce the full box set of a full-text systematic review and fill the gaps with
  "n/a". Boxes appear only when the corresponding step actually ran:
    * the full-text eligibility box appears ONLY with --fulltext-assessed;
    * the "other methods" column appears ONLY when a record carries a non-database source;
    * eligibility decided on title and abstract is LABELLED as such;
    * the prefilter cut is called "automated relevance prioritisation" and its records are
      counted as NOT SCREENED — never as excluded, because nobody read them.
  Mislabelling these tells a reader that studies were assessed and rejected when they were
  never opened, which is a false claim about the method.

  Records removed for retraction are shown as their own named removal, never folded into
  "duplicates" or into the exclusion reasons — they were never eligible in the first place.

No LLM. No network. Pure function of (stage files) -> identical output every run.
Exit code: 0 on a consistent flow, 1 when the counts contradict each other.
"""

import argparse
import json
import sys

# PRISMA 2020 splits identification into "databases and registers" and "other methods".
# A preprint server is a DATABASE you searched, not an other method — miscounting it there
# understates the systematic search and overstates the hand-found material. "Other methods"
# is for records that did not come from running a query: PDFs the author supplied, citation
# chasing, and supplementary web finds.
DATABASE_SOURCES = {'pubmed', 'pmc', 'europepmc', 'europe_pmc', 'elicit', 'consensus',
                    'embase', 'scopus', 'wos', 'openalex', 'semantic_scholar', 'cochrane',
                    'biorxiv', 'medrxiv', 'preprint'}
REGISTRY_SOURCES = {'ctgov', 'clinicaltrials', 'clinicaltrials.gov', 'ictrp', 'isrctn'}
OTHER_METHOD_SOURCES = {'source_folder', 'user_supplied', 'citation_chase', 'web',
                        'google_scholar', 'sciencedirect', 'hand_search'}
NO_REASON = '(no reason recorded)'


def read_jsonl(path):
    if not path:
        return None
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


def source_split(records):
    """Split identification by PRISMA column: databases/registers vs other methods."""
    db, other = 0, {}
    for r in records:
        src = (r.get('source') or '').lower()
        if src in DATABASE_SOURCES or src in REGISTRY_SOURCES:
            db += 1
        else:
            # An unrecognised source is reported by name rather than silently binned, so a
            # typo'd or new source shows up as itself instead of inflating "other methods".
            other[src or '(unlabelled)'] = other.get(src or '(unlabelled)', 0) + 1
    return db, other


def build(records, studies, candidates, deferred, verdicts, fulltext_assessed, fulltext_excluded):
    flow = {'stages': {}, 'warnings': [], 'labels': {}}
    s = flow['stages']

    if records is not None:
        s['identified'] = len(records)
        db, other = source_split(records)
        s['identified_databases_registers'] = db
        s['identified_other_methods'] = sum(other.values())
        flow['identified_other_breakdown'] = other

    if studies is not None:
        s['after_deduplication'] = len(studies)
        if records is not None:
            s['duplicates_removed'] = len(records) - len(studies)
        retracted = [x for x in studies if x.get('retracted') is True]
        s['retracted_removed'] = len(retracted)
        flow['retracted_ids'] = [x.get('study_id') for x in retracted]
        s['eligible_for_screening'] = len(studies) - len(retracted)

    if candidates is not None:
        s['screened_title_abstract'] = len(candidates)
    if deferred is not None:
        s['deferred_not_screened'] = len(deferred)

    if verdicts is not None:
        by_verdict, reasons = {}, {}
        for v in verdicts:
            key = (v.get('verdict') or 'unlabelled').lower()
            by_verdict[key] = by_verdict.get(key, 0) + 1
            if key == 'exclude':
                r = (v.get('reason') or '').strip() or NO_REASON
                reasons[r] = reasons.get(r, 0) + 1
        s['verdicts_recorded'] = len(verdicts)
        s['excluded_title_abstract'] = by_verdict.get('exclude', 0)
        s['maybe_not_included'] = by_verdict.get('maybe', 0)
        s['included'] = by_verdict.get('include', 0)
        flow['exclusion_reasons'] = dict(sorted(reasons.items(), key=lambda kv: (-kv[1], kv[0])))
        # PRISMA 2020 requires a reason for EVERY exclusion, so count the ones that lack it
        # rather than only noticing when none of them has one — an unreasoned exclusion hides
        # inside a populated table exactly as easily as in an empty one.
        unreasoned = reasons.get(NO_REASON, 0)
        if unreasoned:
            flow['warnings'].append(
                f'{unreasoned} exclusion(s) carry no reason — PRISMA 2020 requires a reason '
                'for every excluded record')

    if fulltext_assessed is not None:
        s['fulltext_assessed'] = fulltext_assessed
        if fulltext_excluded is not None:
            s['fulltext_excluded'] = fulltext_excluded

    # --- internal consistency: the flow must add up ---------------------------------
    if candidates is not None and deferred is not None and 'eligible_for_screening' in s:
        total = s['screened_title_abstract'] + s['deferred_not_screened']
        if total != s['eligible_for_screening']:
            flow['warnings'].append(
                f'screened ({s["screened_title_abstract"]}) + deferred ({s["deferred_not_screened"]}) '
                f'= {total}, but {s["eligible_for_screening"]} were eligible for screening')
    if verdicts is not None and candidates is not None:
        if s['verdicts_recorded'] != s['screened_title_abstract']:
            flow['warnings'].append(
                f'{s["verdicts_recorded"]} verdicts recorded for {s["screened_title_abstract"]} '
                'screened studies — every screened study needs exactly one verdict')
        counted = s['excluded_title_abstract'] + s['maybe_not_included'] + s['included']
        if counted != s['verdicts_recorded']:
            flow['warnings'].append(
                f'verdicts do not partition: include+exclude+maybe = {counted}, '
                f'but {s["verdicts_recorded"]} verdicts exist (an unlabelled verdict?)')

    flow['labels'] = {
        'eligibility_basis': 'title and abstract',
        'prioritisation': 'automated relevance prioritisation (deferred studies were NOT read)',
        'fulltext_box_drawn': fulltext_assessed is not None,
    }
    return flow


def mermaid(flow):
    s = flow['stages']
    L = ['```mermaid', 'flowchart TD']
    if 'identified' in s:
        other = s.get('identified_other_methods', 0)
        L.append(f'  A["Records identified from databases and registers<br/>'
                 f'(n = {s.get("identified_databases_registers", s["identified"])})"]')
        if other:                                   # box appears only if such a record exists
            L.append(f'  A2["Records identified via other methods<br/>(n = {other})"]')
    if 'duplicates_removed' in s:
        L.append(f'  B["Duplicate records removed<br/>(n = {s["duplicates_removed"]})"]')
    if s.get('retracted_removed'):
        L.append(f'  R["Retracted records removed<br/>(n = {s["retracted_removed"]})"]')
    if 'eligible_for_screening' in s:
        L.append(f'  C["Studies eligible for screening<br/>(n = {s["eligible_for_screening"]})"]')
    if 'deferred_not_screened' in s:
        L.append(f'  D["Deferred by automated relevance prioritisation<br/>'
                 f'NOT screened, not excluded (n = {s["deferred_not_screened"]})"]')
    if 'screened_title_abstract' in s:
        L.append(f'  E["Studies screened on title and abstract<br/>'
                 f'(n = {s["screened_title_abstract"]})"]')
    if 'excluded_title_abstract' in s:
        L.append(f'  F["Excluded with reasons<br/>(n = {s["excluded_title_abstract"]})"]')
    if s.get('maybe_not_included'):
        L.append(f'  M["Uncertain — not included, listed for the author<br/>'
                 f'(n = {s["maybe_not_included"]})"]')
    if 'fulltext_assessed' in s:
        L.append(f'  G["Full text assessed for eligibility<br/>(n = {s["fulltext_assessed"]})"]')
        if 'fulltext_excluded' in s:
            L.append(f'  H["Excluded after full text<br/>(n = {s["fulltext_excluded"]})"]')
    if 'included' in s:
        L.append(f'  I["Studies included in the synthesis<br/>(n = {s["included"]})"]')

    edges = []
    if 'duplicates_removed' in s:
        edges.append('  A --> B')
        if s.get('identified_other_methods'):
            edges.append('  A2 --> B')
        edges.append('  B --> ' + ('R' if s.get('retracted_removed') else 'C'))
        if s.get('retracted_removed'):
            edges.append('  R --> C')
    if 'deferred_not_screened' in s:
        edges.append('  C --> D')
    if 'screened_title_abstract' in s:
        edges.append('  C --> E')
    if 'excluded_title_abstract' in s:
        edges.append('  E --> F')
    if s.get('maybe_not_included'):
        edges.append('  E --> M')
    if 'fulltext_assessed' in s:
        edges.append('  E --> G')
        if 'fulltext_excluded' in s:
            edges.append('  G --> H')
        if 'included' in s:
            edges.append('  G --> I')
    elif 'included' in s:
        edges.append('  E --> I')
    L += edges
    L.append('```')
    return '\n'.join(L)


def render(flow, args):
    s = flow['stages']
    out = ['# PRISMA 2020 Flow (P4)', '']
    out.append('> Every number below is a count of records on disk, not a recollection. Boxes appear')
    out.append('> only for steps that actually ran: eligibility here was decided on **title and')
    out.append('> abstract**, and studies the prefilter deferred are counted as **not screened** —')
    out.append('> never as excluded, because nobody read them. No LLM, no network.')
    out.append('')
    out.append('## Flow')
    out.append('')
    out.append(mermaid(flow))
    out.append('')
    out.append('## Counts')
    out.append('')
    out.append('| Stage | n |')
    out.append('|---|---|')
    for k, v in s.items():
        if isinstance(v, int):
            out.append(f'| {k.replace("_", " ")} | {v} |')
    out.append('')
    if flow.get('identified_other_breakdown'):
        out.append('## Identified via other methods')
        for src, n in sorted(flow['identified_other_breakdown'].items()):
            out.append(f'- {src}: {n}')
        out.append('')
    if flow.get('retracted_ids'):
        out.append('## Retracted, removed before screening')
        out.append('Never eligible, and never folded into "duplicates" or the exclusion reasons.')
        for sid in flow['retracted_ids']:
            out.append(f'- `{sid}`')
        out.append('')
    if flow.get('exclusion_reasons'):
        out.append('## Exclusion reasons (title/abstract stage)')
        out.append('')
        out.append('| Reason | n |')
        out.append('|---|---|')
        for r, n in flow['exclusion_reasons'].items():
            out.append(f'| {r} | {n} |')
        out.append('')
    out.append(f'## Consistency check ({len(flow["warnings"])})')
    if flow['warnings']:
        for w in flow['warnings']:
            out.append(f'- ⚠ {w}')
        out.append('')
        out.append('**The flow does not add up.** Fix the stage files; do not hand-edit the diagram.')
    else:
        out.append('- the stages add up')
    out.append('')
    out.append('## What this does NOT claim')
    out.append(f'- Eligibility was judged on **{flow["labels"]["eligibility_basis"]}**'
               + ('' if flow['labels']['fulltext_box_drawn']
                  else ' — no full-text eligibility assessment was performed, so no such box is drawn.'))
    out.append(f'- Deferred studies were subject to {flow["labels"]["prioritisation"]}.')
    out.append('- Screening was AI-assisted against protocol criteria, with a human at the gates. '
               'Do NOT write "two reviewers independently screened" unless that literally happened.')
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Deterministic PRISMA 2020 flow (P4).')
    ap.add_argument('--records', help='raw records JSONL (pre-dedup) — the identification count')
    ap.add_argument('--studies', help='deduplicated studies JSONL')
    ap.add_argument('--candidates', help='prefiltered candidates JSONL (what was screened)')
    ap.add_argument('--deferred', help='deferred studies JSONL (not screened)')
    ap.add_argument('--verdicts', help='screening verdicts JSONL: {study_id, verdict, reason}')
    ap.add_argument('--fulltext-assessed', type=int,
                    help='draw the full-text eligibility box ONLY if this is given')
    ap.add_argument('--fulltext-excluded', type=int, help='excluded after full-text assessment')
    ap.add_argument('--out-json', help='write prisma.json to this path')
    ap.add_argument('--out', help='write the human-readable flow to this path')
    args = ap.parse_args(argv)

    flow = build(read_jsonl(args.records), read_jsonl(args.studies), read_jsonl(args.candidates),
                 read_jsonl(args.deferred), read_jsonl(args.verdicts),
                 args.fulltext_assessed, args.fulltext_excluded)
    if args.out_json:
        with open(args.out_json, 'w', encoding='utf-8') as fh:
            json.dump(flow, fh, ensure_ascii=False, indent=2, sort_keys=True)
    report = render(flow, args)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(report)
    sys.stdout.write(report)
    return 1 if flow['warnings'] else 0


if __name__ == '__main__':
    sys.exit(main())
