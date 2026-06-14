# 05_verification_report.md — QA: verification + rubric + audit

## A. Claim ↔ source verification (cross-checked against reference store)
| Claim | Cite | Source check | Verdict |
|---|---|---|---|
| SELECT MACE 8.0%→6.5%, HR 0.80 (0.72–0.90), n=17,604, established CVD, no DM | [1] | matches R1 (PMID 37952131) | PASS |
| Meta MACE RR 0.80 (0.72–0.89); MI 0.72 (0.61–0.85); all-cause 0.81 (0.71–0.93); CV death/stroke NS | [2] | matches R5 (PMID 40207414) | PASS |
| Primary prevention "scarce and controversial," extrapolated | [3] | matches R4 (PMID 37648659) | PASS |
| STEP 1 weight −14.9% vs −2.4%, n=1961, no DM | [4] | matches R8 (PMID 33567185) | PASS |
| SELECT weight −10.2% at 208 wk | [5] | matches R2 (PMID 38740993) | PASS |
| SELECT kidney HR 0.78 (0.63–0.96) | [6] | matches R3 (PMID 38796653) | PASS |
| Weight −8.77 kg, SBP −4.13, 15 trials | [7] | matches R6 (PMID 38029929) | PASS |
| MACE + all-cause mortality meta in non-DM | [8] | matches R7 (PMID 39345822) | PASS (advisory) |
| Obesity is a growing global CV risk factor | [9] | matches R9 (PMID 41092926) | PASS |
| Discontinuation 16.6% vs 8.2% | [1] | matches R1 | PASS |
| No Vietnamese-population data | (text) | matches search result; no figure invented | PASS |

**Strength alignment:** Moderate→MACE, Low→stroke/CV-death, Low(extrapolated)→primary prevention,
High→surrogates. All match the appraisal GRADE labels. ✔
**Fabricated citations:** none. **Naked claims:** none.

**Advisory (FIX-optional, not blocking):** [8] Stefanou pools GLP-1 RA **and tirzepatide**; in a
semaglutide-only review it supports the general MACE/mortality direction but is not semaglutide-specific —
already used as corroboration alongside [2], acceptable; a one-line note could be added.

## B. Rubric score
| Criterion | Score | Evidence |
|---|---|---|
| T1 Search comprehensiveness (25%) | 0.75 | ≥2 sources, MeSH listed, 3 meta-analyses, gap search, current to 2025–26, gate cleared; **no formal society guideline cited**; 9 core refs (<20) |
| T2 Source quality (20%) | 0.85 | NEJM/Nature/Lancet/Endocr Pract; >80% tier 1–3; GRADE assigned; no predatory |
| T3 Synthesis (20%) | 0.85 | thematic; cross-study comparison; MACE-decomposition insight; mechanism |
| T4 Critical appraisal (15%) | 0.80 | consensus/controversy split; RoB table; industry-funding COI; assumption register |
| T5 Citation accuracy (10%) | 0.85 | all verified PMIDs/DOIs; Vancouver; ref [2] missing vol/pages (Epub) |
| T6 Applicability (10%) | 0.85 | clinical implications; Asian/Vietnam applicability limit; next steps |

**Total = 0.25·0.75 + 0.20·0.85 + 0.20·0.85 + 0.15·0.80 + 0.10·0.85 + 0.10·0.85 = 0.82 → MET**
(no fabricated citation → no auto-fail).

## C. Audit
- **Process:** protocol ✓ · retrieval ✓ · curiosity budget ✓ (Vietnam + gap searches run) · Research Map
  **GATE CLEARED** (user approved + re-confirmed direction) ✓ · appraisal + assumption register ✓ · synthesis ✓.
  ⚠️ **Deviation:** `source/` folder not listed/asked this run (test had no user PDFs) — minor process gap, logged.
- **Laws:** L1 truth ✓ · L2 purpose/scope (broadened per user) ✓ · L3 hierarchy ✓ · L4 consensus/controversy ✓ ·
  L5 limitations ✓ · L6 learning (entry pending) ✓.
- **Scope integrity:** semaglutide-only ✓ · broadened frame ✓ · Vietnamese ✓ · ~1,900 words (target ~2,500 —
  slightly under; acceptable for focused semaglutide scope).

## D. Decision
**DELIVER — MET (0.82).** No fabricated citation; gate cleared. Advisories (guideline absent, [8] not
semaglutide-specific, length slightly under, `source/` not checked) noted for the lessons loop, none blocking.
