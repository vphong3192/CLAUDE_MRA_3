# 02_corpus.md - metformin efficacy and safety in adult T2D (Phase 2 corpus, 2026-10-27)

> One row per logical study. Source of record details: `reference/metformin-t2d.md`. Machine layer: `_workspace/02b_records.jsonl`. Eligibility judged on TITLE+ABSTRACT only (no full-text eligibility box). Verdicts are the retriever's, pending the user at Gate 2b.

## A. Studies in the store (29) - tier and full-text status

| store id | stable_id | first author, year | design / source type | source | tier | fulltext | pipeline path | relevance note |
|---|---|---|---|---|---|---|---|---|
| MET-H01 | PMID 42825450 + PMID 42825923 | Davies MJ, 2026 | peer-reviewed (major-body consensus report, parallel publication in Di | PubMed | HIGH | unavailable (no PMCID; MCP abstract only) | screened: include | Current ADA/EASD algorithm (2026); metformin position not in abstract |
| MET-H02 | PMID 41358900 | Bajaj M, 2026 | peer-reviewed (major-body guideline: ADA Standards of Care 2026, secti | PubMed | HIGH | available (PMC12690185, open access) | DEFERRED by prefilter -> hand-added | Latest ADA Standards of Care (s9); recommendation text missing |
| MET-H03 | PMID 36272764 + PMID 36272755 | KDIGO Diabetes Work Group, 2022 | peer-reviewed (major-body guideline: KDIGO 2022 diabetes in CKD) + lin | PubMed | HIGH | unavailable (PubMed record has no abstract; no PMCID) | DEFERRED by prefilter -> hand-added | KDIGO diabetes-in-CKD guideline; no abstract |
| MET-H04 | PMID 28770324 | Griffin SJ, 2017 | peer-reviewed (SR/MA of RCTs) | PubMed | HIGH | retrieved (PMC5552849) | screened: include | RCTs isolating metformin: CV effect uncertain (UKPDS-dominated) |
| MET-H05 | PMID 33516224 | Li T, 2021 | peer-reviewed (SR/MA of RCTs | PubMed | HIGH | retrieved (PMC7847575) | screened: include | RCT MA: null on mortality/CV; "combination harm" signal |
| MET-H06 | PMID 32501595 | Gnesin F, 2020 | peer-reviewed (Cochrane SR/MA, GRADE) | PubMed | HIGH | available (PMC7386876) | screened: include | Cochrane: no clear evidence on patient-important outcomes |
| MET-H07 | PMID 27088241 | Maruthur NM, 2016 | peer-reviewed (AHRQ SR | PubMed | HIGH | unavailable (no PMCID; MCP abstract only) | screened: include | AHRQ: supports metformin first-line (CV mortality vs SU) |
| MET-H08 | PMID 37024129 | Shi Q, 2023 | peer-reviewed (SR + network MA, GRADE | PubMed | HIGH | retrieved (PMC10077111) | screened: include | NMA: metformin low-certainty effects; SGLT2i/GLP-1 RA high |
| MET-H09 | PMID 40813122 | Nong K, 2025 | peer-reviewed (living SR + NMA, GRADE | PubMed | HIGH | unavailable (no PMCID; MCP abstract only) | screened: include | Living NMA (2025); no metformin numbers in abstract |
| MET-H10 | PMID 42530338 | Silverii GA, 2026 | peer-reviewed (pairwise + network MA | PubMed | HIGH | retrieved (PMC13538750) | screened: include | 2026 NMA: metformin MACE OR ~0.69, low certainty |
| MET-H11 | PMID 41548682 | Patiño-Cardona S, 2026 | peer-reviewed (SR/MA of 12 observational studies | PubMed | HIGH | unavailable (no PMCID; MCP abstract only) | screened: include | Observational MA: metformin in CKD, stage 4 lactic acidosis trend |
| MET-H12 | PMID 39521399 | Lambourg EJ, 2024 | peer-reviewed (nationwide target-trial emulation, observational) | PubMed | HIGH | retrieved (PMC12101959) | screened: include | Stopping vs continuing metformin at eGFR<30 |
| MET-H13 | PMID 36187122 | Nabrdalik K, 2022 | peer-reviewed (SR/MA/meta-regression of 71 RCTs | PubMed | HIGH | retrieved (PMC9524196) | screened: include | GI AE meta-analysis of RCTs; IR vs XR |
| MET-H14 | PMID 38837240 | El-Damanawi R, 2024 | peer-reviewed (Cochrane SR/MA, GRADE | PubMed | HIGH | available (PMC11152183) | screened: include | Cochrane: metformin in CKD (mixed T2D/ADPKD) |
| MET-M01 | PMID 32598218 | Tsapas A, 2020 | peer-reviewed (SR/NMA, 453 RCTs) | PubMed | MEDIUM | abstract-only (provisional) | screened: include | Comparative effectiveness SR/NMA, metformin background |
| MET-M02 | PMID 38639546 | Qaseem A, 2024 | peer-reviewed (ACP clinical guideline | PubMed | MEDIUM | abstract-only (provisional) | screened: include | ACP guideline on newer agents; recs not captured |
| MET-M03 | PMID 27434443 | Palmer SC, 2016 | peer-reviewed (network MA, 301 RCTs) | PubMed | MEDIUM | abstract-only (provisional) | screened: include | JAMA NMA: no mortality difference between classes |
| MET-M04 | PMID 33117278 | Hu Y, 2020 | peer-reviewed (SR/MA, 13 studies: 9 cohorts, 3 RCT post hoc, 1 nested  | PubMed | MEDIUM | abstract-only (provisional) | screened: include | Metformin in T2D+CKD, mortality/CV MA |
| MET-M05 | PMID 31904444 | Zhang K, 2020 | peer-reviewed (SR/MA incl. observational | PubMed | MEDIUM | abstract-only (provisional) | screened: include | Observational pooled CV risk (contrast to RCTs) |
| MET-M06 | PMID 29305402 | Lalau JD, 2018 | peer-reviewed (three complementary prospective studies: dose-finding,  | PubMed | MEDIUM | abstract-only (provisional) | screened: include | CKD 3A-4 dose regimen; lactate safety |
| MET-M07 | PMID 39526048 | Atkinson M, 2024 | peer-reviewed (mini-systematic review | PubMed | MEDIUM | available (PMC11548349) | screened: include | B12 deficiency mini-SR (2015+) |
| MET-M08 | PMID 40183554 | Jung C, 2025 | peer-reviewed (Korean NHIS retrospective cohort | PubMed | MEDIUM | available (PMC12131923) | screened: include | Metformin+PPI and B12 deficiency (Korea) |
| MET-M09 | PMID 38662670 | Huynh DT, 2024 | peer-reviewed (cross-sectional | PubMed | MEDIUM | available (PMC11045118) | screened: include | Vietnam: B12 deficiency 18.6% |
| MET-M10 | PMID 39350158 | Nabrdalik K, 2024 | peer-reviewed (SR/MA of 21 observational studies | PubMed | MEDIUM | available (PMC11440709) | screened: include | GI AE prevalence, observational MA |
| MET-M11 | PMID 34079464 | Tan J, 2021 | peer-reviewed (SR | PubMed | MEDIUM | available (PMC8165304) | screened: include | XR vs IR formulation SR |
| MET-M12 | PMID 36189689 | de Boer IH, 2022 | peer-reviewed (ADA/KDIGO joint consensus report 2022) | PubMed | MEDIUM | abstract-only (provisional) | DEFERRED by prefilter -> hand-added | ADA/KDIGO consensus on metformin in CKD; deferred->hand-added |
| MET-M13 | PMID 36148880 + PMID 36151309 | Davies MJ, 2022 | peer-reviewed (ADA/EASD consensus 2022 | PubMed | MEDIUM | abstract-only (provisional) | DEFERRED by prefilter -> hand-added | Previous ADA/EASD (2022), superseded |
| MET-M14 | PMID 40374214 | Phan HH, 2025 | peer-reviewed (cross-sectional | PubMed | MEDIUM | abstract-only (provisional) | DEFERRED by prefilter -> hand-added | Vietnam: B12 deficiency 22.1% (Cho Ray) |
| MET-M15 | PMID 33394543 | Clegg LE, 2021 | peer-reviewed (post hoc analysis of EXSCEL and SAVOR-TIMI 53 RCT data, | PubMed | MEDIUM | abstract-only (provisional) | DEFERRED by prefilter -> hand-added | RCT-derived CKD 3-4 cohort; deferred->hand-added |

## B. Uncertain (11) - not included, listed for the user

| stable_id | year | title | source_type | why uncertain |
|---|---|---|---|---|
| PMID 42365335 | 2026 | Comparative cardiovascular efficacy of antidiabetic therapies in type 2 diabetes: a systematic revie | peer-reviewed | 2026 SR/NMA of CV efficacy incl. metformin; overlaps Silverii 2026; listed for user decision |
| PMID 41223492 | 2025 | Empagliflozin versus metformin for glucose variability and metabolic outcomes in drug-naïve type 2 d | peer-reviewed | Small RCT (n=46) drug-naive empagliflozin vs metformin, glycaemic-variability surrogate; listed for user decision |
| PMID 38719492 | 2024 | Comparative effectiveness of second line oral antidiabetic treatments among people with type 2 diabe | peer-reviewed | Target-trial emulation of second-line agents added to metformin (n=75,739); metformin is background; listed for user decision |
| PMID 39391521 | 2024 | Optimising antidiabetic medication management for type 2 diabetes and renal dysfunction in Can Tho C | peer-reviewed | Vietnamese hospital (Can Tho) antidiabetic use in kidney failure: local prescribing context, descriptive; listed for user decision |
| PMID 31235118 | 2019 | Should metformin still be the first-line of treatment in type 2 diabetes mellitus? A comprehensive r | peer-reviewed | Level III narrative review on whether metformin should stay first-line; useful for controversy framing; listed for user decision |
| PMID 41373013 | 2025 | Efficacy and safety of metformin versus empagliflozin on chronic kidney disease progression (MET-EMP | peer-reviewed | MET-EMPA-CKD RCT (n=120, mixed diabetic/non-diabetic CKD, retrospectively registered); population only partly T2D; listed for user decision |
| DOI 10.1101/2024.01.07.24300938 | 2024 | Metformin use is associated with lower risks of dementia, anxiety and depression: The Hong Kong Diab | preprint (NOT peer-reviewed) | medRxiv PREPRINT (not peer-reviewed): metformin vs sulphonylurea, dementia/psychiatric outcomes (HK cohort n=89,711); observational signal; listed for user decision (L-004) |
| PMID 36129996 | 2022 | Glycemia Reduction in Type 2 Diabetes - Glycemic Outcomes. | peer-reviewed | GRADE RCT: second-line agents added to metformin (n=5047); informs add-on sequencing, not metformin itself; listed for user decision |
| PMID 32132005 | 2020 | The Long-term Effects of Metformin on Patients With Type 2 Diabetic Kidney Disease. | peer-reviewed | Observational DKD cohort (n=10,426): mortality/ESRD/lactic acidosis; may overlap included CKD meta-analyses; listed for user decision |
| PMID 30672083 | 2019 | Metformin use and cardiovascular events in patients with type 2 diabetes and chronic kidney disease. | peer-reviewed | TREAT post hoc (NCT00093015) metformin in T2D+CKD: mortality HR 0.49; may overlap included CKD meta-analyses; listed for user decision |
| NCT NCT03627039 | 2018 | Metformin And Cardiovascular Effectiveness vs SGLT2 (MACES) | trial registry | Registered observational metformin-vs-SGLT2 CV effectiveness study (n=20000, status unknown); no publication found; listed for user decision |

## C. PRISMA numbers (from `02i_prisma.json`, script-derived)

identified 250 -> duplicates removed 31 -> retracted removed 1 -> eligible 218 -> **deferred by prefilter, UNREAD (not excluded): 68** / screened on title+abstract 150 -> excluded 116 / uncertain 11 / included 23.

**Disclosure for the Methods section:** six studies in section A (MET-H02, H03, M12, M13, M14, M15) were among the 68 deferred by the automated prefilter (thin PubMed metadata -> low concept score) and were added by hand after targeted known-item searches; they are therefore NOT in the PRISMA "included" count of 23. Screening was AI-assisted with a human at the gates; no second reviewer.

## D. Coverage by evidence tier (Law 3)

- Major-body guidelines / consensus: ADA/EASD 2026, ADA SOC 2026 s9, KDIGO 2022, ADA/KDIGO 2022, ACP 2024 (+ADA/EASD 2022 historical). NICE NG28 and FDA labelling NOT searched (gap).
- SR/MA/NMA: 17 (>=5 requirement met), incl. 2 Cochrane reviews on metformin (Gnesin 2020; El-Damanawi 2024).
- Large RCT evidence specific to metformin vs placebo with CV outcomes in T2D: none (UKPDS-era trials pooled in Griffin 2017 / Li 2021).
- Preprints: 1 (medRxiv HK cohort, uncertain list). Trial registry: 2 context records (VA-IMPACT prediabetes; MACES observational).
