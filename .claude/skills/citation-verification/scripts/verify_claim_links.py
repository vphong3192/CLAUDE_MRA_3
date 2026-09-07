#!/usr/bin/env python3
"""Fail-closed draft -> evidence-card -> bibliography linkage checks, not semantics.

Supported draft: Markdown prose/pipe-table rows, bracketed Vancouver citations,
and a final References, Bibliography or Tài liệu tham khảo heading with one-line
numbered entries carrying PMID/DOI/NCT. Annotation immediately follows its unit:
    Result was lower [1]. <!-- claim:CLM-001 -->
JSONL links: claim_id, text (including citations), card_ids, citation_numbers,
study_ids. Whitespace alone is normalized. Arrays are unique, nonempty sets.
Fenced code, raw HTML, footnotes, numeric Markdown links, ambiguous numeric
brackets and citation-bearing headings/table headers are unsupported, not ignored.
Fulltext cards require an embedded abstract for the existing FULLTEXT lock.
Exit 0: mechanical checks pass; 1: invalid input/link/lock. No network or LLM.
"""

import argparse
import hashlib
import json
import re
import sys
import types
from pathlib import Path


def sibling(name):
    """Load current source without stale bytecode or a package dependency."""
    path = Path(__file__).with_name(name + '.py')
    module = types.ModuleType(name)
    module.__file__ = str(path)
    exec(compile(path.read_text(encoding='utf-8'), str(path), 'exec'), module.__dict__)
    return module


QUOTES = sibling('verify_quotes')
AUDIT = sibling('citation_audit')
ANNOTATION = re.compile(r'<!--\s*claim:(CLM-[A-Za-z0-9_-]+)\s*-->')
BIB_HEADING = re.compile(r'^#{1,6}\s+(?:References|Bibliography|Tài liệu tham khảo)\s*$', re.I)
LIMITS = ('PASS proves linkage, source identity and existing quote locks only; it does '
          'not prove semantic support. Uncited claims, completeness, methods and '
          'interpretation remain the independent verifier and human reviewer responsibility.')


def norm(text):
    return ' '.join(text.split())


def error(errors, code, detail):
    errors.append({'code': code, 'detail': detail})


def read_jsonl(path):
    records = []
    for line_number, line in enumerate(Path(path).read_text(encoding='utf-8-sig').splitlines(), 1):
        if not line.strip():
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f'{path}:{line_number}: invalid JSON: {exc.msg}') from exc
        if not isinstance(row, dict):
            raise ValueError(f'{path}:{line_number}: expected JSON object')
        records.append(row)
    return records


def canonical_id(value):
    if not isinstance(value, str):
        raise ValueError('study identifier must be a string')
    kind, sep, identifier = value.strip().partition(':')
    kind = kind.lower()
    patterns = {'pmid': r'\d{5,9}', 'doi': r'10\.\d{4,9}/\S+', 'nct': r'NCT\d{8}'}
    if not sep or kind not in patterns or not re.fullmatch(patterns[kind], identifier, re.I):
        raise ValueError(f'invalid study identifier: {value!r}')
    return kind + ':' + (identifier.upper() if kind == 'nct' else identifier.lower())


def ids_for_card(card):
    ids = {canonical_id(card['study_id'])}
    for kind in ('pmid', 'doi', 'nct'):
        if card.get(kind):
            ids.add(canonical_id(kind + ':' + str(card[kind])))
    for kind in ('pmid', 'doi', 'nct'):
        if len([x for x in ids if x.startswith(kind + ':')]) > 1:
            raise ValueError(f'conflicting {kind} identifiers')
    return ids


def citations(text, errors, location):
    if re.search(r'</?[A-Za-z][^>]*>|<!--|\[\^|\[\d[^\]]*\]\(', text):
        error(errors, 'UNSUPPORTED_FORMAT', f'{location}: HTML, footnote or numeric Markdown link')
    result = set()
    for bracket in re.finditer(r'\[([^\]]*)\]', text):
        inner = bracket.group(1)
        if not re.search(r'\d', inner):
            if inner in ('N', '?') or inner.startswith('@'):
                error(errors, 'UNRESOLVED_CITATION', f'{location}: [{inner}]')
            continue
        # Numeric-looking brackets are all interpreted; invalid ones must be rewritten.
        if not re.match(r'\s*\d', inner):
            continue
        nums = set()
        valid = True
        for part in inner.split(','):
            part = part.strip()
            if re.fullmatch(r'[1-9]\d{0,2}', part):
                nums.add(int(part))
            else:
                match = re.fullmatch(r'([1-9]\d{0,2})\s*[-–]\s*([1-9]\d{0,2})', part)
                if not match:
                    valid = False
                    break
                first, last = map(int, match.groups())
                if last <= first or last - first > 20:
                    valid = False
                    break
                nums.update(range(first, last + 1))
        if not valid or not nums:
            error(errors, 'AMBIGUOUS_CITATION', f'{location}: [{inner}]')
        else:
            result.update(nums)
    return result


def parse_draft(draft, errors):
    lines = draft.splitlines()
    starts = [i for i, line in enumerate(lines) if BIB_HEADING.fullmatch(line.strip())]
    if len(starts) != 1:
        error(errors, 'BIBLIOGRAPHY', 'Exactly one final bibliography heading is required')
        return {}, {}
    start = starts[0]
    refs = {}
    for i, line in enumerate(lines[start + 1:], start + 2):
        if not line.strip():
            continue
        match = AUDIT.REF_LINE_RE.match(line)
        if not match:
            error(errors, 'BIBLIOGRAPHY', f'line {i}: expected one-line numbered reference; no appendices after bibliography')
            continue
        number = int(match.group(1))
        if number in refs or number < 1:
            error(errors, 'BIBLIOGRAPHY', f'line {i}: duplicate/invalid reference number {number}')
        ref = AUDIT.parse_ref_list([(i, line)])[number]
        ids = {kind + ':' + value for kind, key in (('pmid', 'pmids'), ('doi', 'dois'), ('nct', 'ncts')) for value in ref[key]}
        if not ids:
            error(errors, 'BIBLIOGRAPHY', f'line {i}: reference {number} lacks PMID/DOI/NCT')
        refs[number] = ids
    if not refs:
        error(errors, 'BIBLIOGRAPHY', 'Empty bibliography')

    units = []
    buffer = []
    buffer_line = 0

    def flush():
        if buffer:
            units.append((buffer_line, ' '.join(buffer)))
            buffer.clear()

    for i, line in enumerate(lines[:start], 1):
        stripped = line.strip()
        if stripped.startswith(('```', '~~~')):
            error(errors, 'UNSUPPORTED_FORMAT', f'line {i}: fenced code unsupported')
        if not stripped:
            flush()
        elif stripped.startswith('|'):
            flush()
            units.append((i, stripped))
        elif ANNOTATION.fullmatch(stripped) and not buffer and units and units[-1][0] == i - 1:
            previous_line, previous_text = units[-1]
            units[-1] = (previous_line, previous_text + ' ' + stripped)
        elif stripped.startswith('#') or re.fullmatch(r'[-=*]{3,}', stripped):
            flush()
            units.append((i, stripped))
        else:
            if not buffer:
                buffer_line = i
            buffer.append(stripped)
            if ANNOTATION.search(stripped):
                flush()
    flush()
    claims = {}
    for index, (line_number, unit) in enumerate(units):
        annotations = list(ANNOTATION.finditer(unit))
        clean = ANNOTATION.sub('', unit).strip()
        numbers = citations(clean, errors, f'line {line_number}')
        is_table_header = clean.startswith('|') and index + 1 < len(units) and bool(re.fullmatch(r'[| :\-]+', units[index + 1][1]))
        if numbers and (clean.startswith('#') or is_table_header):
            error(errors, 'UNSUPPORTED_FORMAT', f'line {line_number}: citations in heading/table header')
        if not annotations:
            if numbers:
                error(errors, 'MISSING_ANNOTATION', f'line {line_number}: cited unit needs claim annotation')
            continue
        if len(annotations) != 1 or annotations[0].end() != len(unit):
            error(errors, 'ANNOTATION', f'line {line_number}: one annotation must end its paragraph/row')
            continue
        claim_id = annotations[0].group(1)
        if claim_id in claims:
            error(errors, 'DUPLICATE_CLAIM', claim_id)
        if not clean or not numbers:
            error(errors, 'ANNOTATION', f'{claim_id}: annotated unit requires text and citations')
        claims[claim_id] = {'text': norm(clean), 'citations': numbers}
    if not claims:
        error(errors, 'NO_CLAIMS', 'No annotated cited claims found')
    return claims, refs


def validate(draft, cards, links, source_dir):
    errors = []
    claims, refs = parse_draft(draft, errors)
    card_index = {}
    card_ids = {}
    for card in cards:
        try:
            if not isinstance(card, dict):
                raise ValueError('card must be an object')
            for key in ('card_id', 'study_id', 'claim', 'quote', 'source_file', 'tier'):
                if not isinstance(card.get(key), str) or not card[key].strip():
                    raise ValueError(f'card requires nonempty string {key}')
            if card['card_id'] in card_index:
                raise ValueError(f'duplicate card_id {card["card_id"]}')
            if card['tier'] not in ('abstract', 'fulltext'):
                raise ValueError('tier must be abstract or fulltext')
            if card.get('abstract') is not None and not isinstance(card['abstract'], str):
                raise ValueError('abstract must be a string')
            if card['tier'] == 'fulltext' and not card.get('abstract', '').strip():
                raise ValueError('fulltext card requires embedded abstract for FULLTEXT lock')
            for key in ('pmid', 'doi', 'nct'):
                if card.get(key) is not None and not isinstance(card[key], str):
                    raise ValueError(f'{key} must be a string')
            source = (Path(source_dir) / card['source_file']).resolve()
            if not source.is_relative_to(Path(source_dir).resolve()):
                raise ValueError('source_file must stay inside source-dir')
            card_ids[card['card_id']] = ids_for_card(card)
            card_index[card['card_id']] = card
        except (ValueError, TypeError) as exc:
            error(errors, 'CARD_SCHEMA', str(exc))
    link_index = {}
    checked_cards = set()
    for link in links:
        try:
            if not isinstance(link, dict):
                raise ValueError('link must be an object')
            if not isinstance(link.get('claim_id'), str) or not re.fullmatch(r'CLM-[A-Za-z0-9_-]+', link['claim_id']):
                raise ValueError('invalid claim_id')
            cid = link['claim_id']
            if cid in link_index:
                raise ValueError(f'duplicate link claim_id {cid}')
            link_index[cid] = link
            if not isinstance(link.get('text'), str) or not link['text'].strip():
                raise ValueError(f'{cid}: text must be a nonempty string')
            for key, cls in (('card_ids', str), ('study_ids', str), ('citation_numbers', int)):
                values = link.get(key)
                if not isinstance(values, list) or not values or any(type(v) is not cls or (cls is str and not v.strip()) for v in values):
                    raise ValueError(f'{cid}: {key} requires nonempty array of {cls.__name__}')
                if len(set(values)) != len(values):
                    raise ValueError(f'{cid}: duplicate {key}')
            studies = {canonical_id(sid) for sid in link['study_ids']}
            if len(studies) != len(link['study_ids']):
                raise ValueError(f'{cid}: duplicate canonical study_ids')
            if cid not in claims:
                error(errors, 'ORPHAN_LINK', cid)
                continue
            claim = claims[cid]
            if norm(link['text']) != claim['text']:
                error(errors, 'STALE_TEXT', cid)
            if set(link['citation_numbers']) != claim['citations']:
                error(errors, 'CITATION_SET', cid)
            missing = set(link['card_ids']) - card_index.keys()
            if missing:
                error(errors, 'DANGLING_CARD', f'{cid}: {sorted(missing)}')
                continue
            used_cards = [card_index[k] for k in link['card_ids']]
            # The writer's text can change numbers while the card claim stays intact.
            draft_prose = re.sub(r'\[[\d,\s–-]+\]', '', claim['text'])
            quote_numbers = {n for c in used_cards for n in QUOTES.numbers_in(QUOTES.normalise(c['quote']))}
            absent = set(QUOTES.numbers_in(QUOTES.normalise(draft_prose))) - quote_numbers
            if absent:
                error(errors, 'DRAFT_NUMBER', f'{cid}: {sorted(absent)} absent from linked quotes')
            if studies != {canonical_id(c['study_id']) for c in used_cards}:
                error(errors, 'STUDY_SET', cid)
            for card in used_cards:
                key = card['card_id']
                if key not in checked_cards:
                    checked_cards.add(key)
                    for lock, detail in QUOTES.check_card(card, source_dir, {}):
                        error(errors, 'CARD_' + lock, f'{key}: {detail}')
            matching = set()
            for number in claim['citations']:
                ids = refs.get(number, set())
                matches = {c['card_id'] for c in used_cards if ids & card_ids[c['card_id']]}
                if not matches:
                    error(errors, 'CITATION_IDENTITY', f'{cid}: reference [{number}] does not match linked cards')
                for key in matches:
                    for kind in ('pmid', 'doi', 'nct'):
                        left = {x for x in ids if x.startswith(kind + ':')}
                        right = {x for x in card_ids[key] if x.startswith(kind + ':')}
                        if left and right and left != right:
                            error(errors, 'IDENTITY_CONFLICT', f'{cid}: [{number}] vs {key}: {kind}')
                matching.update(matches)
            if matching != set(link['card_ids']):
                error(errors, 'UNCITED_CARD', f'{cid}: linked cards absent from paragraph citations')
        except (ValueError, TypeError, OSError, UnicodeError) as exc:
            error(errors, 'LINK_SCHEMA', str(exc))
    for cid in claims.keys() - link_index.keys():
        error(errors, 'MISSING_LINK', cid)
    return {'status': 'FAIL' if errors else 'PASS', 'claims_checked': len(claims),
            'cards_checked': len(checked_cards), 'errors': errors, 'limits': LIMITS}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    for arg in ('draft', 'cards', 'source-dir', 'links', 'out'):
        parser.add_argument('--' + arg, required=True)
    args = parser.parse_args(argv)
    try:
        result = validate(Path(args.draft).read_text(encoding='utf-8-sig'),
                          read_jsonl(args.cards), read_jsonl(args.links), args.source_dir)
        if result['status'] == 'PASS':
            sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
            result['inputs'] = {k: sha(getattr(args, k)) for k in ('draft', 'cards', 'links')}
            result['inputs']['sources'] = {c['source_file']: sha(Path(args.source_dir) / c['source_file'])
                                          for c in read_jsonl(args.cards)}
    except (OSError, UnicodeError, ValueError) as exc:
        result = {'status': 'FAIL', 'claims_checked': 0, 'cards_checked': 0,
                  'errors': [{'code': 'INPUT', 'detail': str(exc)}], 'limits': LIMITS}
    try:
        Path(args.out).write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    except OSError as exc:
        print(f'FAIL: cannot write report: {exc}', file=sys.stderr)
        return 1
    print(f'{result["status"]}: {result["claims_checked"]} claims, {result["cards_checked"]} cards, '
          f'{len(result["errors"])} errors; report: {args.out}')
    return int(result['status'] != 'PASS')


if __name__ == '__main__':
    sys.exit(main())
