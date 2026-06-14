---
name: citation-verification
description: >
  Quality-assurance protocol for an AI-written medical review — cross-checks every substantive
  claim against its cited source (anti-hallucination), confirms each citation resolves to a real
  record that genuinely supports the sentence, checks that language strength matches GRADE certainty,
  flags preprint claims, and verifies reference-list completeness and Vancouver formatting. Used by
  the citation-verifier (QA) agent before any review is finalized.
---

# Citation Verification (QA)

The most dangerous failure of an AI-written review is a confident claim attached to a citation that
doesn't say what's claimed — or doesn't exist. This protocol catches that. Produce
`_workspace/05_verification_report.md`, and when clean, `_workspace/06_final_review.md`.

## Boundary-crossing verification — the core check
"A reference exists" is not enough. For each inline `[n]`, read the **claim** and the **actual
source** side by side:
1. **Resolve the citation** — confirm the PMID/DOI/NCT points to a real record (re-fetch metadata
   via the PubMed/preprint/trials MCP if needed).
2. **Confirm support** — the source's findings genuinely support *this specific sentence*. A study
   that found the opposite, a different population, or a different endpoint is a mismatch.
3. **Check strength alignment** — a sentence stated as fact must rest on High/Moderate GRADE per the
   appraisal; flag over-claiming on Low/Very-Low evidence.
4. **Verdict:** `PASS` / `FIX` (correctable) / `BLOCK` (unverifiable → claim must be removed).

## Defect categories (tag every issue)
Tag each finding so the lessons-curator can build preventive rules:
- `fabricated-citation` — reference doesn't exist / 404s.
- `mismatched-citation` — exists but doesn't support the claim (wrong finding/population/endpoint).
- `overstated-certainty` — language stronger than GRADE allows.
- `missed-contradiction` — draft ignores conflicting evidence the appraiser flagged.
- `stale-source` — newer superseding evidence exists and was omitted.
- `preprint-unlabeled` — preprint-based claim not marked as not-peer-reviewed.
- `format-error` — numbering gap, missing reference entry, broken hyperlink, inconsistent Vancouver style.

## Completeness & format
- Every `[n]` has a reference entry; every entry is cited. Numbering contiguous and in order.
- Every reference hyperlinked to a working DOI/PMID/NCT URL.
- Vancouver format consistent across all entries.

## Run incrementally
Verify each section as the writer completes it, not only at the end. Late full-document-only
verification misses more and forces more rework. Re-verify after every writer revision until the
whole document is **PASS**.

## Then score and audit
Once claim-checking passes, run two more steps before delivery:
1. **Rubric** (`references/rubric.md`) — 6 weighted criteria, each scored with cited evidence from the
   output → total + band (EXCEEDED/MET/ADEQUATE/BELOW/FAIL). Any fabricated citation → AUTO-FAIL (Law 1).
2. **Audit** (`references/audit.md`) — process + law-compliance + scope integrity, including whether
   the **Research Map hard gate was cleared**. Emit the structured audit report.

## Output
A claim-by-claim table: `claim | citation | verdict | problem | required correction`, **then the
rubric score and audit report**, then an overall deliver / do-not-deliver decision. Send FIX/BLOCK
items to the writer; send the tagged defect list to the lessons-curator. Never pass an unverifiable
citation — if it can't be resolved after one re-fetch, it's BLOCK. Do not deliver on a fabricated
citation or an uncleared Research Map gate.
