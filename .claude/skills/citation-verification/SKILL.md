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
`_workspace/06a_verification_report.md`, and when clean, `_workspace/06_final_review.md`.

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
Tag each finding so the lead can build preventive rules:
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

## Deterministic citation audit — the mechanical floor (run LAST, always)
Your semantic checks above can be *talked into* a pass by confident prose — the exact failure that
let an early test self-clear a gate. So after your LLM verification, run a script that cannot be
persuaded. It is a **traceability** check, not a meaning check; the two layers are complementary.

```
python3 .claude/skills/citation-verification/scripts/citation_audit.py \
  --draft _workspace/06_final_review.md \
  --store reference/<topic>.md \
  --min-coverage-frac 0.4 \
  --out _workspace/06b_citation_audit.md
```
- **HARD-FAIL → exit 1 → not deliverable** (Law 1): `fabricated_citation` (a draft reference's
  PMID/DOI/NCT is not in the store), `missing_in_store` (a citation traces to no record),
  `placeholder_leftover` (`[N] [?] CITATION_NEEDED TODO [@NEW:…]`), `coverage_below_threshold`.
- **WARN → for human/LLM review** (non-blocking): `number_not_in_source`, `uncited_claim`.
- **What it does NOT check:** whether a source *supports* the sentence, whether a number is the
  *right* one, GRADE alignment, contradictions. Those stay yours. A clean exit-0 still requires independent semantic QA of all substantive claims. Human sampling is recommended and recorded honestly as completed or pending. No LLM, no network; same input →
  identical output every run. Fold its verdict into the audit report (see `references/audit.md`).

## Then score and audit
Once claim-checking passes, run two more steps before delivery:
1. **Rubric** (`references/rubric.md`) — 6 weighted criteria, each scored with cited evidence from the
   output → total + band (EXCEEDED/MET/ADEQUATE/BELOW/FAIL). Any fabricated citation → AUTO-FAIL (Law 1).
2. **Audit** (`references/audit.md`) — process + law-compliance + scope integrity, including whether
   the **Research Map hard gate was cleared**. Emit the structured audit report.

## Output
A checked-claim ID list plus a defect table: `claim_id | citation | verdict | problem | required correction`, **then the
rubric score and audit report**, then an overall deliver / do-not-deliver decision. Send FIX/BLOCK
items to the writer; send the tagged defect list to the lead. Never pass an unverifiable
citation — if it can't be resolved after one re-fetch, it's BLOCK. Do not deliver on a fabricated
citation or an uncleared Research Map gate.


## Mandatory draft-to-card check
Use `docs/claim-links.md` and `verify_claim_links.py` before semantic QA and after final edits.
It verifies exact draft text mappings, card/study/citation sets, source locks and draft numbers against
linked quotes. Report `_workspace/06d_claim_audit.json`. Its successful inputs are SHA-256 bound;
editing text, cards, links or source bytes makes the report stale. Derived numbers need an explicitly
auditable derivation outside this supported verbatim contract; do not smuggle them in or loosen locks.
Changing prose updates links and triggers semantic re-verification, even when quote locks still pass.
