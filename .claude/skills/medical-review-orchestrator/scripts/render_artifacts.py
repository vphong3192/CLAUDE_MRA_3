"""Render evidence tables and a provenance index from existing data; no judgment or QA certification."""
import argparse
import hashlib
import json
import sys
from pathlib import Path


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def cell(value):
    return str(value if value is not None else 'not recorded').replace('|', '\\|').replace('\n', ' ')


def read_cards(path):
    cards = [json.loads(line) for line in path.read_text(encoding='utf-8-sig').splitlines() if line.strip()]
    if not cards or any(not isinstance(c, dict) or not all(isinstance(c.get(k), str) and c[k].strip()
            for k in ('card_id', 'study_id', 'claim', 'certainty', 'outcome')) for c in cards):
        raise ValueError('Nonempty cards with card_id, study_id, claim, certainty and outcome required')
    if len({c['card_id'] for c in cards}) != len(cards):
        raise ValueError('Duplicate card_id')
    if any(c['certainty'] not in ('High', 'Moderate', 'Low', 'Very Low', 'not_assessed') for c in cards):
        raise ValueError('Unknown certainty label')
    return cards


def evidence(cards):
    fields = ('card_id', 'study_id', 'outcome', 'claim', 'certainty', 'design', 'sample_size', 'effect', 'rob')
    lines = ['# Evidence card index', '', '> One row per card, not per unique study. Certainty is supplied by appraisal, not calculated here.', '',
             '| ' + ' | '.join(fields) + ' |', '| ' + ' | '.join('---' for _ in fields) + ' |']
    lines += ['| ' + ' | '.join(cell(c.get(f)) for f in fields) + ' |' for c in cards]
    return '\n'.join(lines) + '\n'


def manifest(workspace, store, source_dir, out):
    state = json.loads((workspace / '00a_run.json').read_text(encoding='utf-8-sig'))
    required = ('run_id', 'scope', 'research_map', 'appraisal_decision', 'coach', 'qa', 'learning')
    if not isinstance(state, dict) or any(k not in state for k in required):
        raise ValueError('State missing required receipt fields; see docs/run-state.md')
    for key in required[1:]:
        if not isinstance(state[key], dict):
            raise ValueError(f'{key} must be an object')
    minimum = ['00_scope.md', '01_protocol.md', '02_corpus.md', '02a_search_log.md', '02j_prisma.md',
               '03_research_map.md', '03a_gate_approval.md', '04_appraisal.md', '04b_cards.jsonl',
               '04c_quote_locks.md', '04d_evidence_table.md', '05b_claim_links.jsonl',
               '06_final_review.md', '06a_verification_report.md', '06b_citation_audit.md', '06d_claim_audit.json']
    missing = [p for p in minimum if not (workspace / p).is_file()]
    if missing or not store.is_file() or not source_dir.is_dir():
        raise ValueError(f'Missing inputs: {missing}; citation store and source directory must exist')
    if state['scope'].get('status') != 'approved' or not state['scope'].get('receipt'):
        raise ValueError('Scope receipt not approved')
    if state['research_map'].get('status') != 'approved' or not state['research_map'].get('receipt'):
        raise ValueError('Research Map receipt not approved')
    if state['research_map'].get('sha256') != digest(workspace / '03_research_map.md'):
        raise ValueError('Map changed since recorded approval')
    if state['appraisal_decision'].get('status') not in ('not_needed', 'approved') or not state['appraisal_decision'].get('reason'):
        raise ValueError('Appraisal decision pending or unexplained')
    if state['appraisal_decision']['status'] == 'approved' and not state['appraisal_decision'].get('receipt'):
        raise ValueError('Appraisal decision approval needs receipt')
    if state['coach'].get('status') not in ('not_needed', 'completed') or not state['coach'].get('reason'):
        raise ValueError('Coach status missing or unexplained')
    if state['coach']['status'] == 'completed' and not (workspace / '05a_coach.md').is_file():
        raise ValueError('Coach declared completed but report missing')
    if state['qa'].get('status') != 'PASS' or state['qa'].get('draft_sha256') != digest(workspace / '06_final_review.md'):
        raise ValueError('QA missing or final draft changed since QA receipt')
    audit = json.loads((workspace / '06d_claim_audit.json').read_text(encoding='utf-8'))
    if audit.get('status') != 'PASS':
        raise ValueError('Claim audit failed')
    cards = read_cards(workspace / '04b_cards.jsonl')
    expected = {'draft': digest(workspace / '06_final_review.md'),
                'cards': digest(workspace / '04b_cards.jsonl'),
                'links': digest(workspace / '05b_claim_links.jsonl'),
                'sources': {c['source_file']: digest(source_dir / c['source_file']) for c in cards}}
    if audit.get('inputs') != expected:
        raise ValueError('Claim audit stale: rerun on current draft, cards, links and sources')
    files = sorted(p for p in workspace.iterdir() if p.is_file() and p != out and p.name[:2].isdigit() and int(p.name[:2]) <= 6)
    files += [store] + sorted(p for p in source_dir.rglob('*') if p.is_file())
    lines = ['# Review manifest', '', '> Index of recorded receipts and current bytes, not a new semantic review or proof that a human approved.',
             '> QA and approval receipts are agent-authored. Verify them against the actual conversation and CLI runs.', '',
             f'Run: {cell(state["run_id"])}', '', '## Decisions', '']
    for key in required[1:]:
        lines.append(f'- {key}: {json.dumps(state[key], ensure_ascii=False, sort_keys=True)}')
    lines += ['', 'Scope: `00_scope.md`. Confidence/outcomes: `04_appraisal.md` + `04d_evidence_table.md`.',
              'Open assumptions: Assumption Register in `04_appraisal.md`; limitations in final review.', '',
              '## Confidence card index', '', '| Card | Source | Outcome | Certainty |', '|---|---|---|---|']
    lines += ['| ' + ' | '.join(cell(c[k]) for k in ('card_id', 'study_id', 'outcome', 'certainty')) + ' |' for c in cards]
    lines += ['', '## Current artifact SHA-256', '', '| File | SHA-256 |', '|---|---|']
    for p in files:
        # Paths relative to the study root retain identity across machines.
        label = p.relative_to(workspace.parent) if p.is_relative_to(workspace.parent) else p.name
        lines.append(f'| {cell(label)} | {digest(p)} |')
    return '\n'.join(lines) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    subs = ap.add_subparsers(dest='command', required=True)
    ev = subs.add_parser('evidence')
    ev.add_argument('--cards', type=Path, required=True)
    ev.add_argument('--out', type=Path, required=True)
    ma = subs.add_parser('manifest')
    for arg in ('workspace', 'store', 'source-dir', 'out'):
        ma.add_argument('--' + arg, type=Path, required=True)
    args = ap.parse_args(argv)
    try:
        text = evidence(read_cards(args.cards)) if args.command == 'evidence' else manifest(
            args.workspace.resolve(), args.store.resolve(), args.source_dir.resolve(), args.out.resolve())
        args.out.write_text(text, encoding='utf-8')
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        return 1
    print(f'RENDERED {args.command}: {args.out}; no semantic verdict generated')
    return 0


if __name__ == '__main__':
    sys.exit(main())
