# Deterministic Citation Audit (P1)

> Traceability check ONLY — it proves each citation maps to the closed reference
> pool; it does NOT read meaning, so it cannot prove a source supports a claim or
> that a number is correct. The LLM citation-verifier still owns semantics, and a
> human/LLM spot-check of ~10% of cited sentences is still required. No LLM, no network.

- draft: `_workspace/05_draft_review.md`
- store: `reference/la-electrophysiology-elderly-af.md`
- min-coverage-frac: 40%

## Counts
- store records: 76 · store PMIDs: 76
- draft reference entries: 72 · distinct inline citations: 54
- store records actually cited: 72 (95% coverage)

## HARD-FAIL findings (0)
- none

## WARN findings (6) — non-blocking, for human review
- _number_not_in_source_ (L75): number "0,002" not in any cited source text: "van der Does và cộng sự cho thấy vận tốc dẫn truyền thấp nhất giảm theo tuổi (hệ số −0,210; p=0,002) và tỷ lệ "
- _number_not_in_source_ (L75): number "0,210" not in any cited source text: "van der Does và cộng sự cho thấy vận tốc dẫn truyền thấp nhất giảm theo tuổi (hệ số −0,210; p=0,002) và tỷ lệ "
- _number_not_in_source_ (L113): number "78.000" not in any cited source text: "Phân tích gộp của Chattopadhyay và cộng sự (2022; N≈78.000) cho hiệu ứng gộp **2,12 (95% CI 1,49–3,01)** theo "
- _number_not_in_source_ (L115): number "0,04" not in any cited source text: "ngưỡng gốc của Morris là >0,03 mm·s [64], khác với >0,04 mm·s của Huang – nên nêu cả hai khi thiết kế biến số."
- _number_not_in_source_ (L131): number "0,63" not in any cited source text: "triệt đốt theo xơ hóa không hơn PVI, HR 0,95; 95% CI 0,77–1,17; P=0,63, kèm biến cố an toàn cao hơn) [12]:"
- _number_not_in_source_ (L143): number "95" not in any cited source text: "Trong CABANA, ở nhóm ≥75 tuổi, kết cục chính phức hợp có aHR 1,39 (95% CI 0,75–2,58) và tử vong do mọi nguyên "

## VERDICT: PASS
Traceability clean. Semantics and ~10% spot-check still required before delivery.
