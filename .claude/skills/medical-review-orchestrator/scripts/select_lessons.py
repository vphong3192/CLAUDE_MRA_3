"""Select approved lesson text by explicit role and scope tags; no network or LLM."""
import argparse
import re
from pathlib import Path

ALIASES = {'lead': {'lead', 'orchestrator', 'strategist', 'writer', 'research-strategist', 'synthesis-writer'},
           'retriever': {'retriever', 'evidence-retriever'},
           'appraiser': {'appraiser', 'critical-appraiser'},
           'verifier': {'verifier', 'citation-verifier', 'qa'},
           'coach': {'coach', 'quality-coach'}}


def select(text, roles, scopes):
    expanded = set(roles)
    for role in roles:
        expanded.update(ALIASES.get(role, {role}))
    selected = []
    for block in re.split(r'(?=^### L-\d{3}:)', text, flags=re.M):
        if not block.startswith('### L-'):
            continue
        role_line = re.search(r'^- \*\*Role:\*\* (.*)$', block, re.M)
        scope_line = re.search(r'^- \*\*Scope:\*\* (.*)$', block, re.M)
        tags = set(re.findall(r'[a-z]+(?:-[a-z]+)*', role_line.group(1).lower())) if role_line else set()
        scope = set(re.findall(r'[a-z]+(?:-[a-z]+)*', scope_line.group(1).lower())) if scope_line else {'universal'}
        known = {'universal', 'vi-language', 'cardiology-ep'}
        if tags and not (tags & (expanded | {'all', 'universal'})):
            continue
        if scope <= known and 'universal' not in scope and not (scope & set(scopes)):
            continue
        # Historical origin is available on demand, not injected into every phase.
        selected.append(re.sub(r'^- \*\*Origin:\*\*.*\n?', '', block.strip(), flags=re.M).strip())
    return '# Selected lessons\n\n' + '\n\n'.join(selected) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--lessons', type=Path, default=Path(__file__).parents[2] / 'lessons-learned' / 'lessons.md')
    ap.add_argument('--roles', nargs='+', required=True, choices=sorted(ALIASES))
    ap.add_argument('--scopes', nargs='*', default=['universal'])
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    result = select(args.lessons.read_text(encoding='utf-8'), args.roles, args.scopes)
    args.out.write_text(result, encoding='utf-8')
    print(f'Selected {result.count("### L-")} lessons; {len(result)} characters; {args.out}')


if __name__ == '__main__':
    main()
