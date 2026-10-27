# Deterministic Deduplication (P4)

> One row per STUDY, not per record: a paper found as a preprint, a journal article
> and a trial registration counts once. Identifier match first, fuzzy title within the
> year guard second. Pairs outside the guard are REPORTED, never merged. Relevance and
> quality are not decided here. No LLM, no network; identical output every run.

- input: `_workspace/02b_records.jsonl`
- thresholds (hardcoded): fuzzy ≥ 0.92 · year guard ±1 · block prefix 12 chars

## Counts
- records in: **250**
  - consensus: 30
  - ctgov: 5
  - medrxiv: 1
  - pubmed: 214
- studies out: **219**
- duplicates removed: **31**

## Merges (60)
- `doi` (10.1016/s0140-6736(26)01865-9): [27] Cardiovascular safety of orforglipron versus insulin glargin… ⇔ [51]
- `doi` (10.4067/s0034-98872026000701070): [28] Chilean Multidisciplinary Consensus on the Use of GLP-1 Rece… ⇔ [52]
- `doi` (10.1007/s13300-026-01913-0): [32] The Role of SGLT2 Inhibitors in the Prevention of Type 2 Dia… ⇔ [56]
- `doi` (10.1007/s41999-026-01608-6): [55] Diabetes medication use in the last year of life in people l… ⇔ [59]
- `doi` (10.1177/1060028019889064): [0] Oral Semaglutide: First-in-Class Oral GLP-1 Receptor Agonist… ⇔ [65]
- `doi` (10.1136/bmj-2023-077097): [74] Comparative effectiveness of second line oral antidiabetic t… ⇔ [93]
- `doi` (10.7326/m20-0864): [22] Comparative Effectiveness of Glucose-Lowering Drugs for Type… ⇔ [133]
- `doi` (10.3310/hta21020): [68] Canagliflozin, dapagliflozin and empagliflozin monotherapy f… ⇔ [134]
- `doi` (10.7326/m15-2650): [70] Diabetes Medications as Monotherapy or Metformin-Based Combi… ⇔ [135]
- `doi` (10.1186/s12933-026-03346-2): [60] Disease-modifying anti-diabetic drugs (DMADDs): bridging the… ⇔ [146]
- `doi` (10.1007/s00125-026-06855-7): [58] Management of type 2 diabetes, 2026. A consensus report by t… ⇔ [151]
- `doi` (10.1007/s12020-015-0841-1): [141] Systematic review and meta-analysis of vildagliptin for trea… ⇔ [175]
- `doi` (10.2337/dc26-0298): [127] Estimating the True MACE Benefits From Tirzepatide in SURPAS… ⇔ [177]
- `doi` (10.1002/dmrr.3515): [138] Comparative efficacy and safety of antihyperglycemic drug cl… ⇔ [181]
- `doi` (10.1002/14651858.cd012906.pub2): [140] Metformin monotherapy for adults with type 2 diabetes mellit… ⇔ [186]
- `doi` (10.1186/s12933-020-01202-5): [137] Association of metformin monotherapy or combined therapy wit… ⇔ [193]
- `doi` (10.1111/dom.71128): [38] Effect of Medications for Type 2 Diabetes on Cardiovascular … ⇔ [214]
- `doi` (10.1007/s00125-017-4337-9): [185] Impact of metformin on cardiovascular disease: a meta-analys… ⇔ [215]
- `doi` (10.1016/j.diabres.2020.108001): [192] Cardiovascular risk following metformin treatment in patient… ⇔ [216]
- `doi` (10.1186/s12933-020-01202-5): [137] Association of metformin monotherapy or combined therapy wit… ⇔ [219]
- `doi` (10.1016/j.ejphar.2026.178560): [213] Safety of metformin in chronic kidney disease and type 2 dia… ⇔ [224]
- `doi` (10.2337/dc19-0936): [196] The Long-term Effects of Metformin on Patients With Type 2 D… ⇔ [226]
- `doi` (10.1111/dom.14313): [198] Cardiovascular and renal safety of metformin in patients wit… ⇔ [228]
- `doi` (10.1111/dom.13642): [200] Metformin use and cardiovascular events in patients with typ… ⇔ [229]
- `doi` (10.1186/s13098-025-02040-9): [209] Efficacy and safety of metformin versus empagliflozin on chr… ⇔ [232]
- `doi` (10.1002/14651858.cd013414.pub2): [169] Metformin for preventing the progression of chronic kidney d… ⇔ [233]
- `doi` (10.1371/journal.pone.0302500): [118] Vitamin B12 deficiency in diabetic patients treated with met… ⇔ [236]
- `doi` (10.17925/ee.2024.20.2.7): [201] Metformin Use and Vitamin B12 Deficiency in People with Type… ⇔ [240]
- `doi` (10.1111/jdi.70037): [202] Concomitant use of metformin and proton pump inhibitors incr… ⇔ [241]
- `pmid` (42815506): [27] Cardiovascular safety of orforglipron versus insulin glargin… ⇔ [51]
- `pmid` (42809786): [28] Chilean Multidisciplinary Consensus on the Use of GLP-1 Rece… ⇔ [52]
- `pmid` (42667546): [32] The Role of SGLT2 Inhibitors in the Prevention of Type 2 Dia… ⇔ [56]
- `pmid` (42802296): [55] Diabetes medication use in the last year of life in people l… ⇔ [59]
- `pmid` (31744308): [0] Oral Semaglutide: First-in-Class Oral GLP-1 Receptor Agonist… ⇔ [65]
- `pmid` (38719492): [74] Comparative effectiveness of second line oral antidiabetic t… ⇔ [93]
- `pmid` (32598218): [22] Comparative Effectiveness of Glucose-Lowering Drugs for Type… ⇔ [133]
- `pmid` (28105986): [68] Canagliflozin, dapagliflozin and empagliflozin monotherapy f… ⇔ [134]
- `pmid` (27088241): [70] Diabetes Medications as Monotherapy or Metformin-Based Combi… ⇔ [135]
- `pmid` (42649514): [60] Disease-modifying anti-diabetic drugs (DMADDs): bridging the… ⇔ [146]
- `pmid` (42825923): [58] Management of type 2 diabetes, 2026. A consensus report by t… ⇔ [151]
- `pmid` (26714458): [141] Systematic review and meta-analysis of vildagliptin for trea… ⇔ [175]
- `pmid` (41940793): [127] Estimating the True MACE Benefits From Tirzepatide in SURPAS… ⇔ [177]
- `pmid` (34951928): [138] Comparative efficacy and safety of antihyperglycemic drug cl… ⇔ [181]
- `pmid` (32501595): [140] Metformin monotherapy for adults with type 2 diabetes mellit… ⇔ [186]
- `pmid` (33516224): [137] Association of metformin monotherapy or combined therapy wit… ⇔ [193]
- `pmid` (42530338): [38] Effect of Medications for Type 2 Diabetes on Cardiovascular … ⇔ [214]
- `pmid` (28770324): [185] Impact of metformin on cardiovascular disease: a meta-analys… ⇔ [215]
- `pmid` (31904444): [192] Cardiovascular risk following metformin treatment in patient… ⇔ [216]
- `pmid` (33516224): [137] Association of metformin monotherapy or combined therapy wit… ⇔ [219]
- `pmid` (41548682): [213] Safety of metformin in chronic kidney disease and type 2 dia… ⇔ [224]
- `pmid` (32132005): [196] The Long-term Effects of Metformin on Patients With Type 2 D… ⇔ [226]
- `pmid` (33394543): [198] Cardiovascular and renal safety of metformin in patients wit… ⇔ [228]
- `pmid` (30672083): [200] Metformin use and cardiovascular events in patients with typ… ⇔ [229]
- `pmid` (41373013): [209] Efficacy and safety of metformin versus empagliflozin on chr… ⇔ [232]
- `pmid` (38837240): [169] Metformin for preventing the progression of chronic kidney d… ⇔ [233]
- `pmid` (38662670): [118] Vitamin B12 deficiency in diabetic patients treated with met… ⇔ [236]
- `pmid` (39526048): [201] Metformin Use and Vitamin B12 Deficiency in People with Type… ⇔ [240]
- `pmid` (40183554): [202] Concomitant use of metformin and proton pump inhibitors incr… ⇔ [241]
- `fuzzy_title` (ratio 1.000): [58] Management of type 2 diabetes, 2026. A consensus report by t… ⇔ [152]
- `fuzzy_title` (ratio 0.997): [154] Management of hyperglycaemia in type 2 diabetes, 2022. A con… ⇔ [155]

## Suspected pairs — NOT merged, human decides (7)
Same title, years further apart than the guard. Usually a preprint and its journal
version, sometimes two genuinely different studies. Confirm before treating as one.
- similarity 0.936 · 2021 vs 2019: [156] Cardiovascular, mortality, and kidney outcomes with GLP-1 re… ⇔ [157]
- similarity 0.939 · 2026 vs 2022: [58] Management of type 2 diabetes, 2026. A consensus report by t… ⇔ [154]
- similarity 0.942 · 2026 vs 2022: [58] Management of type 2 diabetes, 2026. A consensus report by t… ⇔ [155]
- similarity 0.939 · 2026 vs 2022: [151] Management of type 2 diabetes, 2026. A consensus report by t… ⇔ [154]
- similarity 0.942 · 2026 vs 2022: [151] Management of type 2 diabetes, 2026. A consensus report by t… ⇔ [155]
- similarity 0.939 · 2026 vs 2022: [152] Management of Type 2 Diabetes, 2026. A Consensus Report by t… ⇔ [154]
- similarity 0.942 · 2026 vs 2022: [152] Management of Type 2 Diabetes, 2026. A Consensus Report by t… ⇔ [155]

## Identifier conflicts inside a cluster (2)
Merged records that disagree on an identifier. All values are kept in the row.
- `doi:10.1007/s00125-026-06855-7`: {"pmid": ["42825923", "42825450"], "doi": ["10.1007/s00125-026-06855-7", "10.2337/dci26-0141"]}
- `doi:10.1007/s00125-022-05787-2`: {"pmid": ["36151309", "36148880"], "doi": ["10.1007/s00125-022-05787-2", "10.2337/dci22-0034"]}
