# Deterministic Citation Audit (P1)

> Traceability check ONLY — it proves each citation maps to the closed reference
> pool; it does NOT read meaning, so it cannot prove a source supports a claim or
> that a number is correct. The LLM citation-verifier still owns semantics, and a
> human/LLM spot-check of ~10% of cited sentences is still required. No LLM, no network.

- draft: `_workspace/05_draft_review.md`
- store: `reference/metformin-t2d.md`
- min-coverage-frac: 40%

## Counts
- store records: 39 · store PMIDs: 47
- draft reference entries: 33 · distinct inline citations: 33
- store records actually cited: 33 (85% coverage)

## HARD-FAIL findings (0)
- none

## WARN findings (4) — non-blocking, for human review
- _number_not_in_source_ (L47): number "1.000" not in any cited source text: "- *eGFR 30–44:* không tăng nhiễm toan [7]; tối đa 1.000 mg/ngày [22]."
- _number_not_in_source_ (L47): number "1.000" not in any cited source text: "- *eGFR ≥45:* không tăng nhiễm toan ở 45–59 [7]; nên giảm còn 1.000 mg/ngày ở một số bệnh nhân nguy cơ cao [22"
- _number_not_in_source_ (L80): number "44,2" not in any cited source text: "*Phản biện cho ngừng:* nhiễm toan ở tầng này tăng gấp đôi [7]; người ngừng thuốc có thể đang suy giảm, và 44,2"
- _number_not_in_source_ (L98): number "1.000" not in any cited source text: "**Liều (ADA/KDIGO 2022):** tối đa 1.000 mg/ngày khi eGFR 30–44 và ở một số bệnh nhân 45–59 nguy cơ cao; chống "

## VERDICT: PASS
Traceability clean. Semantics and ~10% spot-check still required before delivery.
