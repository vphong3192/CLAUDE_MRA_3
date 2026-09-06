#!/usr/bin/env python3
"""
Deterministic number extraction (P2) — take the hand-copying of numbers away from the LLM.

The appraiser used to retype every N / CI / effect size / p-value from the store into the
evidence table by hand — exactly where a decimal breaks or a Methods number gets pasted as a
result (Law 1 risk). This script pulls those numbers VERBATIM from reference/<topic>.md into
typed buckets, so the appraiser LOADS them instead of copying them.

WHAT THIS DOES: regex-extract, per store record, five typed buckets of verbatim numbers —
  sample_sizes · percentages · p_values · confidence_intervals · ratios (OR/RR/HR/aHR/MD/SMD/β/coef)

WHAT THIS DOES NOT DO: it types numbers by SURFACE PATTERN, not meaning. It does not know which
number is the primary outcome, does not do RoB / GRADE / interpretation, and cannot tell a
baseline figure from a result. Those stay with the appraiser, who must confirm each loaded number
belongs to the outcome being tabled. An empty bucket means "no match" — never a placeholder, never
an invented number. No LLM, no network; identical output for identical input.
"""

import argparse
import re
import sys

# A number: optional sign (ASCII or Unicode minus), digits with comma/period decimals, optional
# leading dot (".210"). Thousands separators are kept inside the verbatim token.
NUM = r'[−-]?\d*[.,]?\d+'
RECORD_HEADER_RE = re.compile(r'^#{2,4}\s')
# Metadata SPANS (identifiers, links, ISO dates) are scrubbed out so a PMID/DOI/year cannot
# masquerade as data — but only the span is removed, not the whole line, so a findings sentence
# that ends with "(Source: …DOI…)" keeps its numbers.
SCRUB_RE = re.compile(
    r'PMID[:\s]*\d{5,9}'           # PMID 40201666
    r'|\bPMC\d+'                   # PMC11973668
    r'|10\.\d{4,9}/[^\s)\]\|]+'    # DOI
    r'|NCT\d{8}'                   # trial id
    r'|https?://\S+'              # URLs
    r'|\[\d{6,9}\]'               # bracketed identifier links [40201666]
    r'|\b\d{4}-\d{2}-\d{2}\b',     # ISO date 2026-06-15
    re.IGNORECASE,
)

# Patterns, built as strings first to keep the regexes readable.
SEP = r'(?:–|—|-|to|;|,)'
CI_PATTERN = (r'(?:95\s*%\s*)?\bCI\b[^\d−-]{0,6}' + NUM + r'\s*' + SEP + r'\s*' + NUM  # 95% CI 0.76–1.22
              + r'|\[\s*' + NUM + r'\s*' + SEP + r'\s*' + NUM + r'\s*\]')           # [1.2–2.3]
# Effect estimates. Two failures this shape is built to avoid, found by an integration run:
#   * "hazard ratio, 0.48" — how NEJM/JAMA/Lancet actually write it in prose — was missed, so the
#     single most important number in a trial never reached a bucket and the appraiser had to
#     hand-copy it, which is the exact hazard P2 exists to remove.
#   * `\bOR\b` under IGNORECASE matched the English word "or", turning "cryoballoon or 12
#     patients" into a ratio of 12. A fabricated number in front of the appraiser is worse than a
#     missing one, so the ABBREVIATIONS are matched case-sensitively — they are always uppercase
#     in medical prose — while only the spelled-out names are case-insensitive.
RATIO_ABBREV = r'aHR|aOR|aRR|HR|OR|RR|IRR|SMD|MD|β'
RATIO_SPELLED = (r'(?i:(?:adjusted|unadjusted|pooled)\s+)?'
                 r'(?i:(?:hazard|odds|risk|rate|incidence\s+rate)\s+ratios?'
                 r'|relative\s+risk'
                 r'|(?:standardi[sz]ed\s+)?mean\s+difference'
                 r'|coefficients?|coef\.?'
                 r'|tỷ\s+số\s+nguy\s+cơ|tỷ\s+suất\s+nguy\s+cơ|tỷ\s+số\s+chênh'
                 r'|nguy\s+cơ\s+tương\s+đối|khác\s+biệt\s+trung\s+bình)')
# The separator is optional and forgiving: "HR 0.48", "HR, 0.48", "HR=0.48", "ratio of 0.91".
RATIO_SEP = r'\s*(?:[=:,]|\bof\b|\bwas\b|\blà\b)?\s*'
RATIO_PATTERN = r'\b(?:' + RATIO_SPELLED + r'|' + RATIO_ABBREV + r')\b' + RATIO_SEP + NUM
PVALUE_PATTERN = r'\bp\s*[<>=]\s*' + NUM
SAMPLE_PATTERN = (
    r'\b[nN]\s*=\s*' + NUM +                                              # n=762 / N=132
    r'|\b\d[\d.,]*(?:\s+[A-Za-zÀ-ỹ][\wÀ-ỹ-]*){0,2}\s+'                    # 353 (persistent-AF) pts
    r'(?:randomized|randomised|patients|pts|participants|subjects|enrolled'
    r'|controls|cases|bệnh nhân|đối tượng|người)\b')
PCT_PATTERN = NUM + r'\s*%'

# Buckets, in priority order. The FIRST pattern to claim a span of text owns it, so "HR 0.96"
# is a ratio (not a bare percentage/sample size) and "95% CI 0.76–1.22" is one interval.
BUCKETS = [
    ('confidence_intervals', re.compile(CI_PATTERN, re.IGNORECASE)),
    ('ratios', re.compile(RATIO_PATTERN)),   # NOT IGNORECASE — see RATIO_ABBREV
    ('p_values', re.compile(PVALUE_PATTERN, re.IGNORECASE)),
    ('sample_sizes', re.compile(SAMPLE_PATTERN, re.IGNORECASE)),
    ('percentages', re.compile(PCT_PATTERN)),
]
BUCKET_ORDER = [name for name, _ in BUCKETS]


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def record_id(header):
    """Pull the stable citekey from a header: '### [REF-001] ...' or '### CBA-01 — ...'."""
    h = header.lstrip('#').strip()
    m = re.match(r'\[([^\]]+)\]', h)          # [REF-001]
    if m:
        return m.group(1)
    m = re.match(r'([A-Z][A-Z0-9]*-\d+|[A-Z]{2,}-\d+)', h)  # CBA-01 / H2H-01 / PFA-07
    if m:
        return m.group(1)
    return h.split('—')[0].split(' - ')[0].strip()[:40]


def split_records(text):
    """Yield (citekey, header, body_text) for each store record, format-agnostic."""
    records, current = [], None
    for line in text.splitlines():
        if RECORD_HEADER_RE.match(line) and not line.lstrip('#').strip().lower().startswith(
            ('section', 'instructions', 'axis')
        ):
            current = {'header': line.strip(), 'lines': []}
            records.append(current)
        elif current is not None:
            current['lines'].append(line)
    for r in records:
        body = SCRUB_RE.sub(' ', '\n'.join(r['lines']))
        yield record_id(r['header']), r['header'], body


def extract(body):
    """Return {bucket: [verbatim, ...]} with claimed spans not reused across buckets."""
    claimed = []  # list of (start, end) already taken by a higher-priority bucket
    found = {name: [] for name in BUCKET_ORDER}

    def overlaps(s, e):
        return any(s < ce and cs < e for cs, ce in claimed)

    for name, rx in BUCKETS:
        for m in rx.finditer(body):
            s, e = m.start(), m.end()
            if overlaps(s, e):
                continue
            claimed.append((s, e))
            tok = ' '.join(m.group(0).split())   # normalise internal whitespace, keep digits verbatim
            if tok not in found[name]:            # dedup, preserve first-seen order
                found[name].append(tok)
    return found


def render(records, store_path):
    out = []
    out.append('# Deterministic Number Extraction (P2)')
    out.append('')
    out.append('> Verbatim numbers pulled by regex from the reference store. The appraiser LOADS these')
    out.append('> into the evidence table instead of hand-copying them. Extraction is NOT')
    out.append('> interpretation: which number is the primary outcome, RoB, GRADE, and baseline-vs-result')
    out.append('> all stay with the appraiser, who must confirm each number belongs to the outcome being')
    out.append('> tabled. An empty bucket = no regex match (never a placeholder; never invent a number).')
    out.append('> No LLM, no network; identical output every run.')
    out.append('')
    out.append(f'- store: `{store_path}`')
    out.append('')
    for cid, header, found in records:
        out.append(f'## {header.lstrip("#").strip()}')
        for name in BUCKET_ORDER:
            vals = found[name]
            out.append(f'- {name}: ' + (' | '.join(vals) if vals else '(none)'))
        out.append('')
    return '\n'.join(out) + '\n'


def main(argv=None):
    ap = argparse.ArgumentParser(description='Deterministic verbatim number extraction (P2).')
    ap.add_argument('--store', required=True, help='reference/<topic>.md')
    ap.add_argument('--out', help='write the extraction to this path (also prints to stdout)')
    args = ap.parse_args(argv)

    records = [(cid, header, extract(body)) for cid, header, body in split_records(read(args.store))]
    report = render(records, args.store)
    if args.out:
        with open(args.out, 'w', encoding='utf-8') as fh:
            fh.write(report)
    sys.stdout.write(report)
    return 0


if __name__ == '__main__':
    sys.exit(main())
