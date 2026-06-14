# 01_search_log.md — search log (PRISMA-ready)

**Run:** 2026-06-14

| # | Source | Query | Hits | Notes |
|---|---|---|---|---|
| 1 | PubMed | semaglutide cardiovascular outcomes obesity without diabetes (SELECT), 2023– | 81 (12 pulled) | SELECT cluster found |
| 2 | PubMed | GLP-1 RA[tiab] AND primary prevention[tiab] AND cardiovascular[tiab] AND non-diabetic | 6 | Stumpf review = key controversy anchor |
| 3 | ClinicalTrials.gov | intervention=semaglutide OR tirzepatide; condition=CV prevention obesity; phase 3–4 | **0** | ⚠️ returned 0 — see error note |
| 3-retry | ClinicalTrials.gov | intervention=tirzepatide; condition=cardiovascular; status=recruiting/active | 11 (8 pulled) | retry succeeded; NCT07619508 directly on-topic |
| 4 | Consensus | GLP-1 RA primary CV prevention without diabetes | 20 (3 shown) | 2 meta-analyses surfaced; PMIDs unconfirmed |
| 5 | bioRxiv/medRxiv | (keyword search unsupported by tool) | n/a | tool limitation logged; not a coverage claim |

## Error / coverage notes (honest accounting)
- **Search 3 returned 0** with the combined intervention+condition+phase filter. Per harness error rule,
  retried once with a simpler query → recovered 11 trials. The original 0 was a query-construction issue,
  not absence of trials. **Lesson candidate:** ClinicalTrials.gov over-constrained queries silently return 0 →
  start broad (intervention OR condition alone), then narrow.
- **Consensus** results (C1–C3) carry no confirmed PMIDs → flagged in the reference store as "confirm before citing."
- **Vietnam/local evidence not yet searched** → open population gap, not covered this run.
- bioRxiv/medRxiv tool has **no keyword search** → preprint coverage this run is incomplete; not claimed as covered.

## PRISMA numbers (provisional, pre-screening)
Identified ≈ 81 + 6 + 11 + 20 = 118 records · deduplicated to ~12 distinct on-topic studies/trials ·
core verified set = R1–R4 (PubMed) + T1–T3 (registry); C1–C3 pending PMID confirmation.
