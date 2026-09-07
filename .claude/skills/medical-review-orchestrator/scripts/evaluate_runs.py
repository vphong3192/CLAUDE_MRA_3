"""Compare paired baseline/candidate run measurements. Never invent usage or approve a harness."""
import argparse
import json
import math
import statistics
import sys
from pathlib import Path

METRICS = ('input_tokens_total', 'output_tokens_total', 'cost_usd', 'duration_seconds', 'gate_questions', 'repair_rounds')
QUALITY = ('critical_errors', 'unsupported_claims', 'numeric_errors', 'missing_key_studies',
           'certainty_errors', 'lost_nuance', 'gate_violations')


def number(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def compare(runs):
    if not isinstance(runs, list) or not runs:
        raise ValueError('runs must be a nonempty list')
    pairs = {}
    for r in runs:
        if not isinstance(r, dict) or r.get('variant') not in ('baseline', 'candidate'):
            raise ValueError('Every run needs baseline/candidate variant')
        if not isinstance(r.get('case_id'), str) or not r['case_id'] or r.get('mode') not in ('frozen', 'live') or type(r.get('repeat')) is not int or r['repeat'] < 1:
            raise ValueError('Each run needs case_id, mode=frozen/live, positive integer repeat')
        for field in ('settings_id', 'prompt_sha256', 'corpus_sha256'):
            if not isinstance(r.get(field), str) or not r[field]:
                raise ValueError(f'Missing comparability field {field}')
        for field in ('prompt_sha256', 'corpus_sha256'):
            if len(r[field]) != 64 or any(c not in '0123456789abcdef' for c in r[field]):
                raise ValueError(f'{field} must be lowercase SHA-256, not placeholder text')
        if not isinstance(r.get('usage'), dict) or not isinstance(r.get('quality'), dict):
            raise ValueError('usage and quality must be objects; unknown values are null')
        for field in METRICS:
            value = r['usage'].get(field)
            if value is not None and not number(value):
                raise ValueError(f'Invalid measurement {field}')
        for field in QUALITY:
            value = r['quality'].get(field)
            if value is not None and (type(value) is not int or value < 0):
                raise ValueError(f'Quality defect counts must be nonnegative integers: {field}')
        key = (r['case_id'], r['mode'], r['repeat'])
        pair = pairs.setdefault(key, {})
        if r['variant'] in pair:
            raise ValueError(f'Duplicate paired run: {key}, {r["variant"]}')
        pair[r['variant']] = r
    details, differences, issues = [], {m: [] for m in METRICS}, []
    for key, pair in sorted(pairs.items()):
        if len(pair) != 2:
            issues.append(f'{key}: missing baseline or candidate')
            continue
        a, b = pair['baseline'], pair['candidate']
        match_fields = ['settings_id', 'prompt_sha256'] + (['corpus_sha256'] if key[1] == 'frozen' else [])
        if any(a[f] != b[f] for f in match_fields):
            raise ValueError(f'{key}: incompatible settings/prompt/frozen corpus')
        row = {'case_id': key[0], 'mode': key[1], 'repeat': key[2], 'deltas': {}, 'quality_regressions': []}
        human = all(x['quality'].get('human_reviewed') is True for x in (a, b))
        if not human:
            issues.append(f'{key}: human review incomplete')
        for metric in METRICS:
            av, bv = a['usage'].get(metric), b['usage'].get(metric)
            if av is None or bv is None:
                row['deltas'][metric] = None
                issues.append(f'{key}: missing {metric}')
                continue
            delta = bv - av
            row['deltas'][metric] = {'absolute': delta, 'percent': 100 * delta / av if av > 0 else None}
            differences[metric].append(delta)
        for field in QUALITY:
            av, bv = a['quality'].get(field), b['quality'].get(field)
            if av is None or bv is None:
                issues.append(f'{key}: missing human score {field}')
            elif human and (bv > av or (field in ('critical_errors', 'gate_violations') and bv > 0)):
                row['quality_regressions'].append(field)
        details.append(row)
    regression = any(r['quality_regressions'] for r in details)
    status = 'REGRESSION' if regression else ('INCOMPLETE' if issues else 'COMPARISON_READY')
    # Never aggregate incomplete measurements across different subsets or mix live/frozen modes.
    modes = {r['mode'] for r in runs}
    aggregate = None
    if not issues and len(modes) == 1:
        aggregate = {m: {'median_paired_delta': statistics.median(ds), 'pairs': len(ds)}
                     for m, ds in differences.items() if ds}
    return {'status': status, 'pairs': details, 'issues': issues, 'aggregate': aggregate,
            'automatic_approval': False,
            'limits': 'Measurements are supplied by the runner/reviewer, not independently authenticated. '
                      'COMPARISON_READY is not proof of non-inferiority; inspect human judgments and repeated results. '
                      'Negative deltas mean candidate used less. Token input totals include cached tokens; output totals include reasoning only once.'}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--runs', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args(argv)
    try:
        data = json.loads(args.runs.read_text(encoding='utf-8-sig'))
        result = compare(data['runs'])
        args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'INVALID: {exc}', file=sys.stderr)
        return 2
    print(f'{result["status"]}: {len(result["pairs"])} pairs; report {args.out}; never automatic approval')
    return 0 if result['status'] == 'COMPARISON_READY' else 1


if __name__ == '__main__':
    sys.exit(main())
