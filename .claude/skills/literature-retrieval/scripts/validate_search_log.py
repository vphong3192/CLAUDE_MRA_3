#!/usr/bin/env python3
"""
Deterministic search-log validator (P3) — make recall + reproducibility checkable, not trust-me.

Retrieval is LLM/MCP-driven, so it can't be made deterministic itself. What CAN be made mechanical
is the *receipt* it leaves: a search log that proves recall (every source paginated to exhaustion or
explicitly capped) and reproducibility (the actual call/params, not just a human-readable query).
This script checks that receipt's FORMAT — it does not run any search and needs no network.

It validates ONE block: the "Recall & reproducibility ledger" table, whose required columns are
  id | source | query | call | total_count | retrieved | recall
Per row it checks:
  - every column present and non-empty
  - total_count / retrieved are integers (clean numbers, not "10/20")
  - call is reproducible — carries params/URL (an '=' or 'http'), not a copy of the human query
  - recall is a known verdict AND consistent with the numbers:
        complete (✓)  -> retrieved >= total_count
        capped  (⚠)   -> retrieved <  total_count
HARD-FAIL (exit 1) on any missing ledger, missing column, malformed row, or inconsistent verdict.

WHAT THIS DOES NOT CHECK: whether the counts are TRUE, whether the query was well-designed, or
whether the right sources were searched. It checks the log is COMPLETE and SELF-CONSISTENT — the
mechanical floor under the retriever's recall claims. No LLM, no network; identical output each run.
"""

import argparse
import re
import sys

LEDGER_HEADER_RE = re.compile(r'recall\s*&?\s*reproducibility\s*ledger', re.IGNORECASE)
REQUIRED = ['id', 'source', 'query', 'call', 'total_count', 'retrieved', 'recall']


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def find_ledger_table(lines):
    """Return (header_cells, [(line_no, row_cells), ...]) for the ledger table, or (None, [])."""
    in_section = False
    header = None
    rows = []
    for i, raw in enumerate(lines, start=1):
        if raw.lstrip().startswith('#'):
            in_section = bool(LEDGER_HEADER_RE.search(raw))
            header = None
            continue
        if not in_section:
            continue
        if '|' not in raw:
            if header is not None and raw.strip() == '':
                break          # blank line ends the table
            continue
        cells = [c.strip() for c in raw.strip().strip('|').split('|')]
        if re.fullmatch(r'[\s|:\-]+', raw.strip()):
            continue           # markdown separator row (---|---)
        if header is None:
            header = [c.lower().replace(' ', '_') for c in cells]
        else:
            rows.append((i, cells))
    return header, rows


def to_int(tok):
    """Parse a CLEAN integer cell (grouping , or . allowed). '10/20' or '~70' -> None."""
    tok = (tok or '').strip()
    if not re.fullmatch(r'\d[\d.,]*', tok):
        return None
    return int(re.sub(r'[.,]', '', tok))


def classify_recall(tok):
    t = (tok or '').lower()
    if '✓' in tok or 'complete' in t or 'retrieved==total' in t.replace(' ', '') or '==total' in t.replace(' ', ''):
        return 'complete'
    if '⚠' in tok or 'capped' in t or 'partial' in t:
        return 'capped'
    return None


def validate(text):
    lines = text.splitlines()
    header, rows = find_ledger_table(lines)
    findings = []

    if header is None:
        return [(0, 'no_ledger', 'no "Recall & reproducibility ledger" table found')], 0

    missing_cols = [c for c in REQUIRED if c not in header]
    if missing_cols:
        findings.append((0, 'missing_columns',
                         f'ledger header missing columns: {", ".join(missing_cols)}'))
        return findings, len(rows)            # can't check rows without the columns

    idx = {c: header.index(c) for c in REQUIRED}
    if not rows:
        findings.append((0, 'empty_ledger', 'ledger table has a header but no data rows'))

    for ln, cells in rows:
        if len(cells) < len(header):
            findings.append((ln, 'malformed_row',
                             f'row has {len(cells)} cells, header has {len(header)}'))
            continue
        get = lambda c: cells[idx[c]]
        for c in REQUIRED:
            if not get(c):
                findings.append((ln, 'empty_cell', f'empty "{c}"'))

        total, retr = to_int(get('total_count')), to_int(get('retrieved'))
        if total is None:
            findings.append((ln, 'bad_number', f'total_count not an integer: "{get("total_count")}"'))
        if retr is None:
            findings.append((ln, 'bad_number', f'retrieved not an integer: "{get("retrieved")}"'))

        call, query = get('call'), get('query')
        if call and not ('=' in call or 'http' in call.lower()):
            findings.append((ln, 'call_not_reproducible',
                             f'call carries no params/URL: "{call[:60]}"'))
        elif call and query and call.strip() == query.strip():
            findings.append((ln, 'call_not_reproducible',
                             'call is just a copy of the human query'))

        verdict = classify_recall(get('recall'))
        if verdict is None:
            findings.append((ln, 'unknown_recall_verdict',
                             f'recall not "✓ complete" or "⚠ capped": "{get("recall")}"'))
        elif total is not None and retr is not None:
            if verdict == 'complete' and retr < total:
                findings.append((ln, 'inconsistent_recall',
                                 f'marked complete but retrieved {retr} < total {total}'))
            if verdict == 'capped' and retr >= total:
                findings.append((ln, 'inconsistent_recall',
                                 f'marked capped but retrieved {retr} >= total {total}'))
    return findings, len(rows)


def render(findings, n_rows, path):
    findings = sorted(set(findings))
    out = []
    out.append('# Deterministic Search-Log Validation (P3)')
    out.append('')
    out.append('> Checks the recall/reproducibility receipt FORMAT only — not whether the counts are')
    out.append('> true or the search was well-designed. It proves the log is complete and self-')
    out.append('> consistent (every source paginated-to-total or explicitly capped; every call')
    out.append('> reproducible). No LLM, no network; identical output every run.')
    out.append('')
    out.append(f'- log: `{path}`')
    out.append(f'- ledger rows checked: {n_rows}')
    out.append('')
    out.append(f'## Findings ({len(findings)})')
    if findings:
        for ln, cat, detail in findings:
            loc = f'L{ln}' if ln else '—'
            out.append(f'- **{cat}** ({loc}): {detail}')
    else:
        out.append('- none')
    out.append('')
    verdict = 'FAIL' if findings else 'PASS'
    out.append(f'## VERDICT: {verdict}')
    if findings:
        out.append('Search log is incomplete or self-inconsistent — fix before relying on its recall claims.')
    else:
        out.append('Ledger is complete and self-consistent. (Format only — counts still trust the retriever.)')
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Deterministic search-log format validator (P3).')
    ap.add_argument('--log', required=True, help='_workspace/02a_search_log.md')
    ap.add_argument('--out', help='write the report to this path (also prints to stdout)')
    args = ap.parse_args(argv)

    findings, n_rows = validate(read(args.log))
    report = render(findings, n_rows, args.log)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(report)
    sys.stdout.write(report)
    return 1 if findings else 0


if __name__ == '__main__':
    sys.exit(main())
