#!/usr/bin/env python3
"""
Verbatim quote & number locks for evidence cards (P8).

THE GAP THIS CLOSES
  citation_audit.py (P1) proves a citation is TRACEABLE to the closed pool. Its own docstring
  states the limit: "it cannot prove it is TRUE." A record can carry a real PMID, resolve
  correctly, and still be attached to a number the paper never reported.

  This layer narrows that gap by one honest step: it proves a QUOTE IS REALLY IN THE SOURCE FILE
  ON DISK, character for character, and that the numbers in the claim built on that quote are
  numbers the quote actually contains.

WHAT IT STILL DOES NOT DO
  It cannot prove the quote SUPPORTS the claim — that the authors meant what the claim says they
  meant. That is the LLM verifier's work and a human spot-check's. A card can pass all five locks
  and still misread its own quote. What it can no longer do is invent the quote or the number.

THE FIVE LOCKS (all HARD-FAIL; a card that trips any one is REJECTED and its claim is not citable)
  IDENTITY  the named source file exists AND carries this study's own identifier, so a real quote
            cannot be attached to the wrong citation. This is the failure the other locks cannot
            see: a quote lifted from the wrong paper matches its file perfectly.
  QUOTE     the quote is a literal substring of that file's text after whitespace/typographic
            normalisation ONLY (see NORMALISATION). No fuzzy matching, no "close enough".
  NUMBER    every number in the claim appears in that card's own quote. Not "somewhere in the
            record" — in the quote the claim rests on.
  LENGTH    the quote sits within bounds. Too short proves nothing specific; a whole page proves
            nothing either, because it always contains the number somewhere.
  FULLTEXT  a card tagged `tier: fulltext` must quote text that is NOT inside the record's
            abstract. Re-emitting the abstract while claiming full-text depth is the step-faking
            failure (R4), and nothing else here would catch it.

WHY THERE IS NO SIXTH LOCK
  The lineage this borrows from runs an ECHO lock: numbers from the abstract must reappear in a
  transcribed full-text dump, proving the dump really came from that paper. It exists there
  because the dump has no independent witness. Here the source file IS on disk, so IDENTITY and
  QUOTE check the same thing directly and better. Porting ECHO anyway would add a lock that
  cannot fail — six locks that look like five plus theatre. It is deliberately not ported.

NORMALISATION — the exact boundary of "verbatim"
  Applied to BOTH sides before matching, and to nothing else:
    * HTML tags stripped, entities unescaped (source corpora store converted HTML alongside PDFs)
    * Unicode NFKC (ligatures, non-breaking spaces)
    * curly quotes -> straight, en/em dash and minus -> hyphen, ellipsis -> three dots
    * all whitespace runs -> one space, then trimmed
  Case is NOT folded and characters are NOT dropped. Anything beyond this list would let a quote
  that is merely similar pass as verbatim, which is the whole thing being prevented.

PDFs are NOT read here: extracting PDF text needs a third-party library, and this layer is
stdlib-only by design so it can never fail to run. Convert to HTML/text first — the corpora
already store both side by side.

No LLM. No network. Pure function of (cards, source files) -> identical output every run.
Exit code: 0 if every card passes, 1 if any card is REJECTED.
"""

import argparse
import html
import json
import re
import sys
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

MIN_QUOTE_CHARS = 40      # below this a quote is too generic to prove anything specific
MAX_QUOTE_CHARS = 1500    # above this the quote contains everything and so evidences nothing
READABLE_SUFFIXES = {'.html', '.htm', '.txt', '.md', '.xml'}

TYPOGRAPHIC = {
    '‘': "'", '’': "'", '‚': "'", '‛': "'",
    '“': '"', '”': '"', '„': '"', '‟': '"',
    '‐': '-', '‑': '-', '‒': '-', '–': '-', '—': '-',
    '―': '-', '−': '-', '­': '',
    '…': '...', ' ': ' ', ' ': ' ', ' ': ' ',
}

# A number as it appears in prose: 74.6 · 0,76 · 1,234 · 12 . Percent/units are matched separately.
NUMBER_RE = re.compile(r'\d[\d.,]*\d|\d')
ID_RE = {
    'pmid': re.compile(r'\b(\d{7,9})\b'),
    'doi': re.compile(r'10\.\d{4,9}/[^\s"\'<>)\]]+', re.IGNORECASE),
    'nct': re.compile(r'\bNCT\d{8}\b', re.IGNORECASE),
}


class TextExtractor(HTMLParser):
    """Strip tags; drop script/style bodies, which are never quotable prose."""

    SKIP = {'script', 'style', 'noscript'}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip_depth += 1

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data):
        if not self._skip_depth:
            self.parts.append(data)

    def text(self):
        return ' '.join(self.parts)


def normalise(text):
    """The ONLY transformation applied before a verbatim comparison. See NORMALISATION above."""
    text = unicodedata.normalize('NFKC', text)
    text = ''.join(TYPOGRAPHIC.get(c, c) for c in text)
    return re.sub(r'\s+', ' ', text).strip()


def file_text(path):
    raw = path.read_text(encoding='utf-8', errors='replace')
    if path.suffix.lower() in {'.html', '.htm', '.xml'}:
        parser = TextExtractor()
        parser.feed(raw)
        raw = html.unescape(parser.text())
    return normalise(raw)


def canonical_number(tok):
    """'0,76' and '0.76' are the same number; '1,234' and '1234' are too.

    Vietnamese prose writes decimals with a comma while the English source writes a period, so a
    lock that compared the strings would reject every correctly-transcribed Vietnamese claim.
    """
    t = tok.strip().rstrip('.,')
    if not t:
        return None
    # a single separator followed by exactly 3 digits is a thousands group; otherwise it is decimal
    t = re.sub(r'(?<=\d)[.,](?=\d{3}(?!\d))', '', t)
    t = t.replace(',', '.')
    try:
        return f'{float(t):g}'
    except ValueError:
        return None


def numbers_in(text):
    out = []
    for m in NUMBER_RE.finditer(text):
        c = canonical_number(m.group(0))
        if c is not None and c not in out:
            out.append(c)
    return out


def study_ids(card):
    ids = []
    for kind, rx in ID_RE.items():
        val = card.get(kind)
        if val:
            ids.append((kind, str(val).strip()))
    sid = card.get('study_id') or ''
    if ':' in sid:
        kind, _, val = sid.partition(':')
        if kind in ID_RE and val:
            ids.append((kind, val.strip()))
    return ids


def check_card(card, source_dir, abstracts):
    """Return a list of (lock, detail) failures. Empty list = the card is accepted."""
    fails = []
    cid = card.get('card_id') or '(unnamed card)'
    quote = (card.get('quote') or '').strip()
    claim = (card.get('claim') or '').strip()
    fname = (card.get('source_file') or '').strip()

    if not quote or not claim:
        return [('SCHEMA', 'card needs a non-empty "claim" and "quote"')]
    if not fname:
        return [('SCHEMA', 'card needs "source_file" naming the file the quote came from')]

    path = Path(source_dir) / fname
    if not path.exists():
        return [('IDENTITY', f'source file not found: {path}')]
    if path.suffix.lower() not in READABLE_SUFFIXES:
        return [('IDENTITY',
                 f'{path.suffix} cannot be read by a stdlib-only layer — convert to HTML/text '
                 f'first (corpora already store both); PDF text extraction is deliberately '
                 f'outside this layer')]

    text = file_text(path)

    # --- IDENTITY -------------------------------------------------------------------
    ids = study_ids(card)
    if not ids:
        fails.append(('IDENTITY', 'card carries no pmid/doi/nct — cannot prove the file is this study'))
    else:
        found = [f'{k}:{v}' for k, v in ids
                 if re.search(re.escape(v), text, re.IGNORECASE)]
        if not found:
            shown = ', '.join(f'{k}:{v}' for k, v in ids)
            fails.append(('IDENTITY',
                          f'none of [{shown}] appears in {fname} — a real quote attached to the '
                          f'wrong paper is the one error the other locks cannot see'))

    # --- QUOTE ----------------------------------------------------------------------
    nq = normalise(quote)
    if nq not in text:
        fails.append(('QUOTE', f'not a literal substring of {fname}: "{nq[:90]}…"'))

    # --- LENGTH ---------------------------------------------------------------------
    if len(nq) < MIN_QUOTE_CHARS:
        fails.append(('LENGTH', f'{len(nq)} chars < {MIN_QUOTE_CHARS} — too generic to evidence a claim'))
    elif len(nq) > MAX_QUOTE_CHARS:
        fails.append(('LENGTH', f'{len(nq)} chars > {MAX_QUOTE_CHARS} — a passage this long '
                                f'contains the number by accident'))

    # --- NUMBER ---------------------------------------------------------------------
    in_quote = set(numbers_in(nq))
    missing = [n for n in numbers_in(normalise(claim)) if n not in in_quote]
    if missing:
        fails.append(('NUMBER', f'claim states {", ".join(missing)} — absent from its own quote'))

    # --- FULLTEXT -------------------------------------------------------------------
    if (card.get('tier') or '').lower() == 'fulltext':
        abstract = normalise(abstracts.get(card.get('study_id') or '', '') or card.get('abstract') or '')
        if abstract and nq in abstract:
            fails.append(('FULLTEXT',
                          'card claims full-text depth but its quote lies entirely inside the '
                          'abstract — re-emitting the abstract is not reading the paper (R4)'))
    return fails


def read_cards(path):
    cards = []
    with open(path, encoding='utf-8') as fh:
        for n, line in enumerate(fh, start=1):
            line = line.strip()
            if not line or line.startswith('//'):
                continue
            try:
                cards.append(json.loads(line))
            except json.JSONDecodeError as exc:
                sys.stderr.write(f'{path}:{n}: not valid JSON — {exc}\n')
                raise SystemExit(2)
    return cards


def read_abstracts(path):
    """Optional: {study_id: abstract} so the FULLTEXT lock has something to compare against."""
    if not path:
        return {}
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def render(results, args):
    rejected = [(c, f) for c, f in results if f]
    accepted = [c for c, f in results if not f]
    by_lock = {}
    for _, fails in rejected:
        for lock, _d in fails:
            by_lock[lock] = by_lock.get(lock, 0) + 1

    out = ['# Verbatim Quote & Number Locks (P8)', '']
    out.append('> Proves each quote is REALLY IN the source file on disk, character for character,')
    out.append('> and that the numbers in the claim are numbers that quote contains. It does NOT')
    out.append('> prove the quote supports the claim — a card can pass every lock and still misread')
    out.append('> itself. What it can no longer do is invent the quote or the number.')
    out.append('> No LLM, no network; identical output every run.')
    out.append('')
    out.append(f'- cards: `{args.cards}` · sources: `{args.source_dir}`')
    out.append(f'- bounds: quote {MIN_QUOTE_CHARS}–{MAX_QUOTE_CHARS} chars after normalisation')
    out.append('')
    out.append('## Counts')
    out.append(f'- cards checked: **{len(results)}**')
    out.append(f'- accepted: **{len(accepted)}**')
    out.append(f'- **REJECTED: {len(rejected)}**')
    if by_lock:
        out.append('- by lock: ' + ' · '.join(f'{k} {v}' for k, v in sorted(by_lock.items())))
    out.append('')
    out.append(f'## Rejected cards ({len(rejected)})')
    if rejected:
        out.append('A rejected card is NOT citable. Fix the quote or drop the claim — never widen a lock.')
        out.append('')
        for card, fails in rejected:
            out.append(f'### `{card.get("card_id") or "(unnamed)"}` — {card.get("study_id") or "—"}')
            out.append(f'- claim: {(card.get("claim") or "")[:160]}')
            for lock, detail in fails:
                out.append(f'- **{lock}**: {detail}')
            out.append('')
    else:
        out.append('- none')
        out.append('')
    out.append(f'## Accepted ({len(accepted)})')
    for card in accepted:
        out.append(f'- `{card.get("card_id")}` — {card.get("study_id")} '
                   f'({len(normalise(card.get("quote") or ""))} chars, '
                   f'{card.get("tier") or "unspecified"})')
    if not accepted:
        out.append('- none')
    out.append('')
    out.append('## Residual risk, stated not hidden')
    out.append('These locks cannot tell you the authors meant what the claim says they meant. The LLM')
    out.append('verifier and a ~10% human spot-check still own that. A green run here narrows the')
    out.append('question from "is any of this real?" to "is this reading correct?".')
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Verbatim quote & number locks for evidence cards (P8).')
    ap.add_argument('--cards', required=True, help='JSONL of evidence cards')
    ap.add_argument('--source-dir', required=True, help='source/<folder>/ holding the full texts')
    ap.add_argument('--abstracts', help='optional JSON {study_id: abstract} for the FULLTEXT lock')
    ap.add_argument('--out', help='write the report to this path (also prints to stdout)')
    args = ap.parse_args(argv)

    cards = read_cards(args.cards)
    abstracts = read_abstracts(args.abstracts)
    results = [(c, check_card(c, args.source_dir, abstracts)) for c in cards]

    report = render(results, args)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(report)
    sys.stdout.write(report)
    return 1 if any(f for _, f in results) else 0


if __name__ == '__main__':
    sys.exit(main())
