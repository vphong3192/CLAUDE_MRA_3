#!/usr/bin/env python3
"""
Deterministic citation audit (P1) — the mechanical floor under the LLM citation-verifier.

WHAT THIS CHECKS (traceability only, NOT semantics):
  HARD-FAIL  fabricated_citation     a draft reference resolves to a PMID/DOI that is NOT in the store
             missing_in_store        a draft citation cannot be traced to any store record at all
             placeholder_leftover    [N] [?] CITATION_NEEDED TODO [@NEW:...] left in the body
             coverage_below_threshold too few of the approved store records are actually cited
  WARN       number_not_in_source    a stat number sits in a cited sentence but no cited source's
                                     verified text contains that digit sequence (heuristic)
             uncited_claim           a sentence carries %/p/CI/OR/RR/HR/n= but no inline [n]

WHAT THIS DOES NOT CHECK:
  Whether the source actually SUPPORTS the sentence (meaning), whether the number is the RIGHT
  number, GRADE/strength alignment, contradictions. Those stay with the LLM citation-verifier.
  This layer proves the citation is TRACEABLE to the closed pool; it cannot prove it is TRUE.
  A clean PASS still requires a human/LLM spot-check of ~10% of cited sentences.

No LLM. No network. Pure function of (draft file, store file, config) → identical output every run.
Exit code: 0 if no HARD-FAIL, 1 if any HARD-FAIL. WARNs never change the exit code.
"""

import argparse
import re
import sys

# --- regexes (module-level so they are compiled once and shared) ---
PMID_RE = re.compile(r'(?:PMID[:\s]*|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{5,9})', re.IGNORECASE)
DOI_RE = re.compile(r'10\.\d{4,9}/[^\s)\]\|]+')
NCT_RE = re.compile(r'NCT\d{8}')   # ClinicalTrials.gov — a first-class source in this harness
REF_LINE_RE = re.compile(r'^\s*(\d{1,3})\.\s')                       # "27. Author ..."
RECORD_HEADER_RE = re.compile(r'^#{2,4}\s')                          # "### [REF-001]" or "### CBA-01"
INLINE_CITE_RE = re.compile(r'\[([\d][\d,\s–\-]*)\](?!\()')     # [3] [5,7,8] [9–11,15]; skip md links
RANGE_RE = re.compile(r'^(\d+)\s*[–\-]\s*(\d+)$')
MAX_RANGE_SPAN = 20   # a citation range like [9–11] is small; [58,9–72,5] is a CI, not a citation
SINGLE_CITE_CAP = 500 # a lone bracketed integer up to this is treated as a citation (catches
                      # dangling [n] above the ref-list max); markdown PMID links are excluded
                      # separately by the (?!\() lookahead, so 8-digit PMIDs never reach here

PLACEHOLDERS = [
    (re.compile(r'\[N\]'), 'placeholder [N]'),
    (re.compile(r'\[\?\]'), 'placeholder [?]'),
    (re.compile(r'CITATION_NEEDED'), 'CITATION_NEEDED'),
    (re.compile(r'\bTODO\b'), 'TODO'),
    (re.compile(r'\[@NEW:[^\]]*\]'), '[@NEW:...] unresolved new-source tag'),
]

# A sentence is a "claim" worth a citation when it carries one of these statistical markers.
STAT_MARKER_RE = re.compile(
    r'(\d+(?:[.,]\d+)?\s*%'           # 34.6%
    r'|\bp\s*[<>=]\s*0?[.,]\d+'       # p<0.001
    r'|\b(?:95\s*%\s*)?CI\b'          # CI / 95% CI
    r'|\b(?:OR|RR|HR|MD|SMD)\b\s*[=:]?\s*\d'  # OR 0.96
    r'|\b[nN]\s*=\s*\d+)',            # n=762
    re.IGNORECASE,
)

# Draft-side "stat numbers" for the number_not_in_source heuristic: decimals, percentages,
# and explicit sample sizes (grouping separators kept, e.g. 17.642 / 17,642). Bare integers
# (years, section numbers) are skipped on the draft side to keep the heuristic quiet.
STAT_NUMBER_RE = re.compile(
    r'(\d+(?:[.,]\d+)+)\s*%?'         # decimals/grouped numbers (optionally a percentage)
    r'|(\d+)\s*%'                     # integer percentages
    r'|[nN]\s*=\s*(\d+(?:[.,]\d+)*)', # n=762 / N=17.642
)
# Store-side haystack: index EVERY number so a draft stat number can be found regardless of
# how the store wrote it (bare "762 randomized" must still match draft "N=762").
ANY_NUMBER_RE = re.compile(r'\d[\d.,]*\d|\d')
# Section / figure cross-references — not statistics; stripped before the draft number scan.
SECTION_REF_RE = re.compile(
    r'\b(?:Mục|Bảng|Hình|Phụ lục|Section|Fig\.?|Figure|Table|Axis)\s*[\dIVX]+(?:\.\d+)*',
    re.IGNORECASE,
)


def digits(token):
    """Locale-robust canonical form of a number: just its digit run.

    '1,5' -> '15', '1.5' -> '15', '17.000' -> '17000', '17,000' -> '17000'.
    Collapsing separators is deliberate: it errs toward MATCHING (fewer warnings),
    the safe direction for a non-blocking heuristic that must never falsely accuse.
    """
    return re.sub(r'\D', '', token)


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


# ----------------------------------------------------------------------------- store
def parse_store(text):
    """Return (pmids:set, dois:set, ncts:set, records:list[dict]).

    Format-agnostic: works for the '### [REF-001] ... PMID 12345' style and the
    '### CBA-01 ... | **PMID** | [12345](url) |' table style alike, because it keys on
    PMIDs/DOIs/NCTs and on '###' record headers — never on a specific citekey shape.
    """
    pmids, dois, ncts = set(), set(), set()
    records = []
    current = None
    for line in text.splitlines():
        if RECORD_HEADER_RE.match(line) and not line.lstrip('#').strip().lower().startswith(
            ('section', 'instructions', 'axis')
        ):
            current = {'header': line.strip(), 'pmids': set(), 'dois': set(),
                       'ncts': set(), 'text': []}
            records.append(current)
        if current is not None:
            current['text'].append(line)
        for m in PMID_RE.finditer(line):
            pmids.add(m.group(1))
            if current is not None:
                current['pmids'].add(m.group(1))
        for m in DOI_RE.finditer(line):
            doi = m.group(0).rstrip('.').lower()
            dois.add(doi)
            if current is not None:
                current['dois'].add(doi)
        for m in NCT_RE.finditer(line):
            ncts.add(m.group(0))
            if current is not None:
                current['ncts'].add(m.group(0))
    # collapse each record's text into a digit-set of ALL its numbers (the haystack)
    for r in records:
        body = '\n'.join(r['text'])
        r['number_digits'] = {digits(m.group(0)) for m in ANY_NUMBER_RE.finditer(body)}
        del r['text']
    return pmids, dois, ncts, records


# ----------------------------------------------------------------------------- draft
def split_draft(text):
    """Separate the reference-list lines from the body.

    Reference-list line = '<n>. ...' that carries a PMID or DOI. Everything else is body
    (incl. appendices, which legitimately carry inline [n] citations).
    """
    body_lines, ref_lines = [], []
    for i, line in enumerate(text.splitlines(), start=1):
        if REF_LINE_RE.match(line) and (PMID_RE.search(line) or DOI_RE.search(line)
                                        or NCT_RE.search(line)):
            ref_lines.append((i, line))
        else:
            body_lines.append((i, line))
    return body_lines, ref_lines


def parse_ref_list(ref_lines):
    """Map draft reference number -> {pmids, dois, line}."""
    refs = {}
    for ln, line in ref_lines:
        m = REF_LINE_RE.match(line)
        num = int(m.group(1))
        refs[num] = {
            'pmids': {x.group(1) for x in PMID_RE.finditer(line)},
            'dois': {x.group(0).rstrip('.').lower() for x in DOI_RE.finditer(line)},
            'ncts': {x.group(0) for x in NCT_RE.finditer(line)},
            'line': ln,
        }
    return refs


def paragraphs(body_lines):
    """Reconstruct hard-wrapped paragraphs so a sentence + its [n] are scanned together.

    Yields (start_line, joined_text). Headings, tables, rules and blank lines end a paragraph.
    """
    buf, start = [], None
    for ln, raw in body_lines:
        line = raw.rstrip()
        is_break = (not line.strip()) or line.lstrip().startswith(('#', '|', '---', '==='))
        if is_break:
            if buf:
                yield start, ' '.join(buf)
                buf, start = [], None
            continue
        if start is None:
            start = ln
        buf.append(line.strip())
    if buf:
        yield start, ' '.join(buf)


def split_sentences(paragraph):
    # Vietnamese decimals use commas, so '. ' / '.\n' reliably mark sentence ends.
    parts = re.split(r'(?<=[.!?:])\s+', paragraph)
    return [p for p in parts if p.strip()]


def parse_citation_bracket(inner, max_ref):
    """Return the citation numbers in a bracket, or None if it is NOT a citation.

    The hard part: Vietnamese statistics look like citations. `[5,7,8]` is a citation;
    `[0,88–4,17]` (a confidence interval) and `[58,9–72,5]` (median [IQR], with comma
    decimals) are NOT. A bracket counts as a citation only if EVERY comma-separated part
    is a bare integer or an ASCENDING short range, and every integer falls in [1, max_ref].
    A CI/IQR fails this because it contains a 0, a value above max_ref, a descending pair,
    or an over-wide span.
    """
    # A lone integer is almost certainly a citation, even above the ref-list max — so a
    # dangling [99] still gets caught as missing_in_store. (CIs/IQRs always have a comma or
    # dash, so this never swallows a statistic.)
    solo = inner.strip()
    if solo.isdigit():
        v = int(solo)
        return {v} if 1 <= v <= SINGLE_CITE_CAP else None

    nums = set()
    for part in inner.split(','):
        part = part.strip()
        if not part:
            return None
        rng = RANGE_RE.match(part)
        if rng:
            a, b = int(rng.group(1)), int(rng.group(2))
            if a < 1 or b <= a or (b - a) > MAX_RANGE_SPAN or b > max_ref:
                return None
            nums.update(range(a, b + 1))
        elif part.isdigit():
            v = int(part)
            if v < 1 or v > max_ref:
                return None
            nums.add(v)
        else:
            return None
    return nums or None


def citation_spans(text, max_ref):
    """List of (match_obj, numbers) for brackets recognized as real citations."""
    spans = []
    for m in INLINE_CITE_RE.finditer(text):
        nums = parse_citation_bracket(m.group(1), max_ref)
        if nums is not None:
            spans.append((m, nums))
    return spans


def cited_numbers(text, max_ref):
    out = set()
    for _, nums in citation_spans(text, max_ref):
        out |= nums
    return out


def strip_citations(text, max_ref):
    """Remove recognized citation brackets so stat-number extraction never reads them."""
    spans = citation_spans(text, max_ref)
    for m, _ in reversed(spans):
        text = text[:m.start()] + ' ' + text[m.end():]
    return text


# ----------------------------------------------------------------------------- audit
def resolves(ref, store_pmids, store_dois, store_ncts):
    """Does a draft reference entry trace to the closed pool?"""
    if ref['pmids'] & store_pmids:
        return 'pmid'
    if ref['dois'] & store_dois:
        return 'doi'
    if ref['ncts'] & store_ncts:
        return 'nct'
    return None


def audit(draft_text, store_text, min_coverage_frac):
    store_pmids, store_dois, store_ncts, records = parse_store(store_text)
    body_lines, ref_lines = split_draft(draft_text)
    refs = parse_ref_list(ref_lines)
    max_ref = max(refs) if refs else 0

    hard, warn = [], []

    # --- placeholder_leftover (body only) ---
    for ln, line in body_lines:
        for rx, label in PLACEHOLDERS:
            if rx.search(line):
                hard.append((ln, 'placeholder_leftover', f'{label}: "{line.strip()[:90]}"'))

    # --- inline citations resolve to a reference-list entry ---
    body_text = '\n'.join(l for _, l in body_lines)
    inline = cited_numbers(body_text, max_ref)
    for n in sorted(inline):
        if n not in refs:
            hard.append((0, 'missing_in_store',
                         f'inline citation [{n}] has no entry in the draft reference list'))

    # --- each reference-list entry traces to the closed pool ---
    id_to_record = {}   # PMID/NCT -> record, for coverage counting
    for r in records:
        for key in list(r['pmids']) + list(r['ncts']):
            id_to_record.setdefault(key, r)
    pmid_to_record = id_to_record  # alias used by the number heuristic below
    cited_records = set()
    for n in sorted(refs):
        ref = refs[n]
        how = resolves(ref, store_pmids, store_dois, store_ncts)
        if how is None:
            if ref['pmids'] or ref['dois'] or ref['ncts']:
                ids = ', '.join(sorted(ref['pmids']) + sorted(ref['dois'])
                                + sorted(ref['ncts'])) or '—'
                hard.append((ref['line'], 'fabricated_citation',
                             f'ref [{n}] cites {ids} which is NOT in the store'))
            else:
                hard.append((ref['line'], 'missing_in_store',
                             f'ref [{n}] carries no PMID/DOI/NCT — cannot be traced to any record'))
        else:
            for key in list(ref['pmids']) + list(ref['ncts']):
                if key in id_to_record:
                    cited_records.add(id(id_to_record[key]))

    # --- coverage_below_threshold (denominator = citable records only) ---
    total = sum(1 for r in records if r['pmids'] or r['dois'] or r['ncts'])
    covered = len(cited_records)
    frac = (covered / total) if total else 0.0
    if min_coverage_frac > 0 and total and frac < min_coverage_frac:
        hard.append((0, 'coverage_below_threshold',
                     f'only {covered}/{total} store records cited '
                     f'({frac:.0%} < required {min_coverage_frac:.0%})'))

    # --- WARN: number_not_in_source & uncited_claim (heuristic, non-blocking) ---
    for start, para in paragraphs(body_lines):
        para_has_cite = bool(cited_numbers(para, max_ref))
        for sent in split_sentences(para):
            nums_here = cited_numbers(sent, max_ref)
            bare = SECTION_REF_RE.sub(' ', strip_citations(sent, max_ref))  # drop cites + section refs
            has_stat = STAT_MARKER_RE.search(bare) is not None
            # uncited_claim: only when the WHOLE paragraph carries no citation (low-noise)
            if has_stat and not para_has_cite:
                warn.append((start, 'uncited_claim',
                             f'stat sentence in an uncited paragraph: "{sent.strip()[:110]}"'))
            if nums_here:
                allowed = set()
                for n in nums_here:
                    ref = refs.get(n)
                    if not ref:
                        continue
                    for p in ref['pmids']:
                        rec = pmid_to_record.get(p)
                        if rec:
                            allowed |= rec['number_digits']
                if allowed:  # only check when we could load the cited source's numbers
                    for m in STAT_NUMBER_RE.finditer(bare):
                        tok = next(g for g in m.groups() if g)
                        d = digits(tok)
                        if d and d not in allowed:
                            warn.append((start, 'number_not_in_source',
                                         f'number "{tok}" not in any cited source text: '
                                         f'"{sent.strip()[:110]}"'))

    stats = {'store_records': total, 'store_pmids': len(store_pmids),
             'draft_refs': len(refs), 'inline_citations': len(inline),
             'cited_records': covered, 'coverage_frac': frac}
    return hard, warn, stats


# ----------------------------------------------------------------------------- report
def render(hard, warn, stats, args):
    hard = sorted(set(hard))
    warn = sorted(set(warn))
    out = []
    out.append('# Deterministic Citation Audit (P1)')
    out.append('')
    out.append('> Traceability check ONLY — it proves each citation maps to the closed reference')
    out.append('> pool; it does NOT read meaning, so it cannot prove a source supports a claim or')
    out.append('> that a number is correct. The LLM citation-verifier still owns semantics, and a')
    out.append('> human/LLM spot-check of ~10% of cited sentences is still required. No LLM, no network.')
    out.append('')
    out.append(f'- draft: `{args.draft}`')
    out.append(f'- store: `{args.store}`')
    out.append(f'- min-coverage-frac: {args.min_coverage_frac:.0%}'
               + ('' if args.min_coverage_frac > 0 else ' (disabled)'))
    out.append('')
    out.append('## Counts')
    out.append(f'- store records: {stats["store_records"]} · store PMIDs: {stats["store_pmids"]}')
    out.append(f'- draft reference entries: {stats["draft_refs"]} · '
               f'distinct inline citations: {stats["inline_citations"]}')
    out.append(f'- store records actually cited: {stats["cited_records"]} '
               f'({stats["coverage_frac"]:.0%} coverage)')
    out.append('')
    out.append(f'## HARD-FAIL findings ({len(hard)})')
    if hard:
        for ln, cat, detail in hard:
            loc = f'L{ln}' if ln else '—'
            out.append(f'- **{cat}** ({loc}): {detail}')
    else:
        out.append('- none')
    out.append('')
    out.append(f'## WARN findings ({len(warn)}) — non-blocking, for human review')
    if warn:
        for ln, cat, detail in warn:
            out.append(f'- _{cat}_ (L{ln}): {detail}')
    else:
        out.append('- none')
    out.append('')
    verdict = 'FAIL' if hard else 'PASS'
    out.append(f'## VERDICT: {verdict}')
    if hard:
        out.append('Do NOT deliver until every HARD-FAIL is resolved (Law 1).')
    else:
        out.append('Traceability clean. Semantics and ~10% spot-check still required before delivery.')
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Deterministic citation traceability audit (P1).')
    ap.add_argument('--draft', required=True, help='final review markdown')
    ap.add_argument('--store', required=True, help='reference/<topic>.md closed pool')
    ap.add_argument('--min-coverage-frac', type=float, default=0.4,
                    help='HARD-FAIL if fewer than this fraction of store records are cited '
                         '(0 disables; default 0.4)')
    ap.add_argument('--out', help='write the report to this path (always also prints verdict)')
    args = ap.parse_args(argv)

    hard, warn, stats = audit(read(args.draft), read(args.store), args.min_coverage_frac)
    report = render(hard, warn, stats, args)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(report)
    sys.stdout.write(report)
    return 1 if hard else 0


if __name__ == '__main__':
    sys.exit(main())
