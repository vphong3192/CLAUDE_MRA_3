# 01_protocol.md — Metformin in adult type 2 diabetes: efficacy and safety

**Written by:** lead (Phase 1, `review-protocol` skill) · **Date:** 2026-10-27 · **Pre-registered before Phase 2.**
**Scope anchor:** `_workspace/00_scope.md` — clinical decision support · internists · ~1500 words ·
2015–present · **output language: Vietnamese** (from 00_scope.md; L-032) · effort `normal`.
**"Current" cutoff for this run:** 2026-10-27.

## 1. Research question
In adults with type 2 diabetes, what are the glycaemic, cardiovascular/mortality and other clinical
benefits of metformin, and what are its harms (including in CKD, older adults and other special
populations), compared with placebo/no treatment or other glucose-lowering drugs — and where does it sit
in current guideline-directed therapy?

| Element | Definition |
|---|---|
| **P** | Adults (≥18 y) with type 2 diabetes, any setting; special subgroups: CKD (eGFR strata), older adults (≥65), established CVD / heart failure, hepatic impairment |
| **I** | Metformin (immediate- or extended-release), monotherapy or as background/add-on |
| **C** | Placebo / diet-lifestyle / no metformin; other glucose-lowering drugs (sulfonylureas, DPP-4i, SGLT2i, GLP-1 RA, insulin); first-line SGLT2i/GLP-1 RA without metformin |
| **O** | Primary: HbA1c change; MACE / CV mortality; all-cause mortality. Secondary: body weight; hypoglycaemia; GI adverse events/discontinuation; lactic acidosis; vitamin B12 deficiency/neuropathy; heart failure outcomes; cancer/dementia (observational, flagged); safety in CKD by eGFR |

## 2. Inclusion / exclusion
| Criterion | Include | Exclude (why) |
|---|---|---|
| Design | SR/meta-analyses (priority), major guidelines/consensus (ADA, ADA/EASD, KDIGO, NICE, FDA safety communications), RCTs, large prospective cohorts / target-trial emulations for safety & special populations | Narrative reviews without method (except as Level III context), case reports/series (except lactic-acidosis signal context), animal/in vitro, editorials |
| Population | Adults with T2D | Type 1 diabetes, GDM/pregnancy, PCOS, prediabetes-only populations (prediabetes noted only as a controversy pointer), children/adolescents, non-diabetic indications (cancer, aging, COVID) |
| Intervention | Metformin | Metformin used solely as a comparator for another drug's question without metformin-specific outcomes |
| Outcomes | ≥1 pre-registered outcome | Pharmacokinetic-only / biomarker-only (except B12) |
| Date | Published 2015-01-01 → 2026-10-27 | Earlier work (UKPDS 34, 1998) cited only as historical anchor if a 2015+ source discusses it |
| Language | English, Vietnamese | Others (Limitations) |
| Publication type | Peer-reviewed; trial registry; preprints (downgraded, flagged) | Conference abstracts without full report |

## 3. Search strategy
**Concept blocks**
- B1 population: "Diabetes Mellitus, Type 2"[MeSH] OR "type 2 diabetes" OR T2D OR T2DM
- B2 intervention: "Metformin"[MeSH] OR metformin OR biguanide
- B3a design: "meta-analysis"[pt] OR "systematic review"[pt] OR "meta-analysis"[tiab] OR "systematic review"[tiab]
- B3b outcomes/safety: "cardiovascular" OR mortality OR "lactic acidosis" OR "vitamin B12" OR "renal insufficiency" OR "chronic kidney disease" OR eGFR OR "gastrointestinal"

**PubMed (filters: 2015/01/01–2026/10/27, humans, English/Vietnamese)**
- Q1 (core SR): B1 AND B2 AND B3a
- Q2 (CV/mortality): B1 AND metformin AND (cardiovascular OR mortality OR "major adverse cardiovascular") AND (meta-analysis OR "systematic review" OR randomized)
- Q3 (safety): B1 AND metformin AND ("lactic acidosis" OR "vitamin B12" OR "renal insufficiency" OR "chronic kidney disease" OR eGFR) 
- Q4 (guidelines, L-011): (metformin OR "glucose-lowering") AND ("type 2 diabetes") AND (guideline OR "consensus report" OR "Standards of Care") — target ADA Standards of Care (latest available, 2025/2026), ADA/EASD consensus 2018/2019/2022, KDIGO diabetes-in-CKD 2020/2022, NICE NG28 updates
- Q5 (first-line debate): metformin AND (SGLT2 OR "GLP-1") AND (first-line OR "without metformin" OR "background metformin") AND (cardiovascular OR meta-analysis)
- Q6 (older adults): metformin AND ("older adults" OR elderly OR aged) AND "type 2 diabetes" AND (safety OR mortality)

**Elicit `search_papers`** (free): "metformin efficacy cardiovascular outcomes type 2 diabetes meta-analysis"; "metformin safety lactic acidosis chronic kidney disease"; "metformin vitamin B12 deficiency type 2 diabetes". Credit-spending Elicit tools only if approved at Gate 2b.

**Consensus `search`:** "Does metformin reduce cardiovascular events and mortality in type 2 diabetes?"; "Is metformin safe in chronic kidney disease?"; "metformin vitamin B12 deficiency".

**medRxiv/bioRxiv:** date-range sweep 2024-01-01→2026-10-27 (no keyword search in the API) — record yield honestly; peer-reviewed literature expected to dominate.

**ClinicalTrials.gov:** condition "Type 2 Diabetes" × intervention "metformin", phase 3/4, status completed/active with results or recruiting — especially trials testing metformin vs. no metformin on CV outcomes or metformin in CKD/older adults.

## 4. Recency
Window 2015-01-01 → 2026-10-27. Preprint and trial-registry sweeps are planned (above). Most recent guideline edition available at run time must be identified.

## 5. Pre-registered outcomes & subgroups
**Outcomes (axes):** A1 glycaemic efficacy (HbA1c, durability, vs comparators) · A2 CV outcomes & mortality · A3 weight · A4 safety: GI tolerance/XR formulation, hypoglycaemia, lactic acidosis, B12 deficiency · A5 special populations: CKD by eGFR, older adults, heart failure, hepatic impairment · A6 place in therapy: guideline position, first-line vs SGLT2i/GLP-1 RA, combination.
**Subgroups:** eGFR strata (≥45, 30–44, <30); age ≥65; established ASCVD/HF vs not; monotherapy vs add-on; IR vs XR.
**Controversy candidates (pre-specified, not to be steered):** whether metformin has independent CV benefit (UKPDS-era vs modern meta-analyses); mandatory first-line status in the SGLT2i/GLP-1 RA era; dose limits and safety at eGFR 30–44 / <30; B12 screening policy; observational cancer/dementia signals.

## 6. Curiosity budget (2 targeted probes)
- **Evidence/contradiction gap:** "metformin cardiovascular outcomes trial" in CT.gov + PubMed (e.g., ongoing pragmatic trials of metformin vs no metformin in CV outcomes; VA-IMPACT type) — is there any adequately powered modern CVOT?
- **Population gap (local):** PubMed "metformin AND (Vietnam OR Vietnamese)" — any Vietnamese-population efficacy/safety data; Asian-population meta-analyses as proxy. Never fabricate.
- (implementation gap, if budget allows) adherence/GI discontinuation in real-world cohorts.

## 7. Machine-readable concepts
See `_workspace/01a_concepts.json`.

## 8. Language & change log
Output language: **Vietnamese** (00_scope.md: "Tiếng Việt (Recommended)").
Change log: (none yet — any post-hoc change must be logged here with reason.)
