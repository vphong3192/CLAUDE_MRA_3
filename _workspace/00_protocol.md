# Review Protocol — Điện học & Điện sinh lý Nhĩ Trái ở Bệnh nhân Rung Nhĩ Cao Tuổi

**Version:** 1.0 · **Date:** 2026-06-29
**Strategist role; written pre-search — fixes the question and method before retrieval begins.**
**Output language of final review:** Vietnamese (user-confirmed, L-032 satisfied)
**Effort:** full · **Run mode:** reuse existing store + targeted new searches

---

## 1. Research Question (one sentence)

In elderly patients (≥65 years) with atrial fibrillation, what atrial electrical and
electrophysiological parameters — spanning conduction, refractoriness, electrogram substrate,
and P-wave morphology — characterize the left atrial substrate, and what reference values,
measurement methods, and units should a systematic data-collection instrument (CRF) capture
for each parameter?

### PECO decomposition

| Element | Specification |
|---|---|
| **P — Population** | Adults ≥65 years old with documented atrial fibrillation (paroxysmal, persistent, or permanent); clinical or EP-lab setting; human studies; sub-focus on ≥75y where data exist. Comparators admitted: non-AF controls (same age), younger AF patients (<65y). |
| **E — Exposure** | Aging (biological age as an exposure variable) AND the presence of AF as a substrate-modifying condition. For P-wave morphology studies: having AF or being at risk of AF. |
| **C — Comparator** | (a) Younger AF patients (<65y); (b) age-matched non-AF controls; (c) general-population elderly without AF (community cohort studies). |
| **O — Outcomes / parameters of interest** | The EP parameters themselves as descriptive endpoints: measured values, reference thresholds, normal ranges, and their association with AF burden, recurrence, or LA electropathology severity. The primary deliverable is a **proposed-variables table** (parameter → definition → measurement method → unit → reference threshold from literature → evidence level). |

**Adaptation note:** This is a descriptive/characterization question (not an intervention trial),
so the frame is PECO (Exposure = aging + AF) rather than PICO. The appraiser will apply
GRADE for observational/descriptive certainty, not just RCT grading.

---

## 2. Inclusion / Exclusion Criteria

| Dimension | Included | Excluded | Rationale |
|---|---|---|---|
| **Study design** | Prospective and retrospective cohorts, cross-sectional, observational registries, case-control, SR/MA, landmark RCT subgroups (age-stratified), community cohorts, animal/ex-vivo for mechanism only | Case reports (n<5), non-peer-reviewed conference abstracts (unless the only evidence for a parameter), non-systematic opinion pieces | Breadth needed for a CRF-framing review; case series of ≥5 admitted if the parameter is otherwise unsupported |
| **Population** | Human adults with AF; age ≥65y as primary focus; mixed-age studies admitted if ≥65y subgroup extractable or results stratified by age | Purely pediatric or congenital-heart-disease populations; AF secondary to acute reversible causes only (post-cardiac-surgery early phase, thyrotoxicosis without AF history) | Congenital/pediatric EP has different physiology; focus is acquired aging substrate |
| **Exposure/parameter** | Any measured atrial EP parameter: conduction velocity, conduction time, ERP/AERP, AF cycle length, SNRT/cSNRT, CFAE, P-wave indices, electrogram voltage/amplitude, activation mapping metrics | Ventricular EP parameters reported in isolation; LA anatomy without EP correlation | Scope is electrical/EP, not purely structural |
| **Comparators** | Age-matched non-AF controls; younger AF cohorts; general-population elderly (community cohorts) | No comparator required for purely descriptive/normative studies | A CRF table needs reference values from any reliable source, even single-arm normative studies |
| **Outcomes required** | Reported numerical value of at least one EP parameter with a defined measurement method and unit; reference range or threshold from the literature | Studies reporting outcomes only as composite endpoints without extractable EP parameter values | Values must be citable into a variable table |
| **Language** | English, Vietnamese; French, German, Japanese with available English abstract and extractable data | Languages with no English abstract and no available translation | Pragmatic; Japanese studies (Inoue 2024, Hirata 2026) are high priority — already in store |
| **Date window** | **No lower bound** — foundational works (e.g., Bayés de Luna 1988 original IAB, Bachmann's bundle anatomy, early ERP normative data) are essential; upper bound = current run date (2026-06-29) | Studies published after retrieval cutoff (2026-06-29) | Foundational works define parameters that CRF variables reference; newest evidence updates thresholds |
| **Publication type** | Peer-reviewed journals; SR/MA; society guidelines and consensus statements; preprints (bioRxiv/medRxiv — labeled not-peer-reviewed); trial registries (ClinicalTrials.gov — for ongoing or unpublished data) | Non-peer-reviewed blog posts, manufacturer white-papers without citation |  |
| **Thematic scope** | Electrical/EP parameters and P-wave morphology. **Brief background only:** pathophysiology, electrical remodeling mechanisms, elderly anatomy — included only as context for parameter interpretation | Reviews of AF pathophysiology without extractable EP parameter values; purely imaging structural studies (LA volume, fibrosis by MRI) without EP correlation | User-confirmed focus: parameters and P-wave morphology are primary |

---

## 3. Parameter Families: Coverage Status & Gap Map

Before the search strings, the protocol maps each parameter family against the existing 40-record store to identify which are **already-covered (AC)**, **partially-covered (PC)**, or **gap-needing-new-retrieval (GAP)**.

### 3.1 Already-covered (AC) — existing store satisfies the main question

| Parameter family | Key store records | What is covered |
|---|---|---|
| **LA bipolar/unipolar voltage & LVZ** | REF-001, REF-002, REF-003, REF-022, REF-033, REF-034 | Thresholds (<0.5 mV bipolar, ~0.73 mV unipolar); age gradient; omnipolar methodology; LA vs RA comparison |
| **LGE-MRI atrial fibrosis (Utah staging)** | REF-011, REF-012 | Utah I–IV definitions; fibrosis % thresholds; ablation outcome correlation |
| **Rotors / focal sources / CFAE** | REF-005, REF-007, REF-008, REF-009, REF-010 | FIRM, CFAE definitions, STAR AF II negative RCT |
| **Mapping technology (EnSite X, omnipolar, HD)** | REF-033, REF-034, REF-035, REF-036 | Omnipolar vs bipolar methodology; functional substrate |
| **LA strain (reservoir, contraction)** | REF-023, REF-024, REF-025 | Age-related LA strain decline; incident AF prediction |
| **Age-related conduction disturbances (non-AF baseline)** | REF-003 (van der Does 2021) | CV, conduction block, low-UV prevalence vs age in 216 CABG patients without AF history |
| **P-wave duration (PWD) + IAB** | REF-037 (Magnani 2011 Framingham), REF-038 (Bayés de Luna 2017), REF-039 (Intzes 2023 SR/MA) | PWD–AF risk (elderly ≥60y); advanced IAB / Bayés syndrome definition; PWD > ablation recurrence (OR 2.04–10.89) |
| **PTFV1** | REF-040 (Huang 2020 MA) | PTFV1 >0.04 mm·s → AF; pooled OR 1.39; N=51,372 |
| **Ablation outcomes in elderly (meta-analyses)** | REF-013, REF-014, REF-015, REF-016, REF-017, REF-018 | Recurrence, complications, CABANA age subgroup |
| **Frailty & elderly-specific considerations** | REF-026, REF-027 | Frailty scoring; implementation gaps |
| **ESC/AHA/HRS guidelines** | REF-029, REF-030, REF-031 | Ablation indications, rhythm control framework |

### 3.2 Partially-covered (PC) — present in store but evidence is thin or secondary-citation only

| Parameter family | Existing coverage | What is missing |
|---|---|---|
| **Conduction velocity (CV) — invasive EP** | REF-003 (intraoperative epicardial, non-AF CABG pts; CV 86.9 cm/s overall) | Intracardiac EP-lab CV in AF patients (endocardial, bipolar); age-stratified reference values from clinical EP studies |
| **Total atrial activation time (TAAT) / inter-/intra-atrial conduction time** | REF-022 (Lin 2021): "total atrial activation time similar among all 3 age groups" — qualitative | Quantitative TAAT (ms) by age; inter-atrial (P-wave–to–CS electrogram); intra-atrial (local activation time) from EP lab data |
| **P-wave area, P-wave axis, signal-averaged ECG** | Not in store (only PWD and PTFV1 covered) | SAECG filtered P-wave duration; P-wave area as predictor; morphological subtypes (positive/biphasic P) in AF-risk stratification; P-wave dispersion |
| **Non-PV trigger location by age** | REF-022 (Lin 2021: SVC higher in young) | Systematic evidence on age and trigger distribution; CRF variable for trigger location |

### 3.3 Gaps requiring new targeted retrieval

| Gap # | Parameter family | Specific gap | Priority |
|---|---|---|---|
| **G-1** | Atrial ERP / AERP (invasive) | Reference values (ms) by age; dispersion; AF vulnerability index in elderly | HIGH — core CRF variable |
| **G-2** | AF cycle length (AFCL) | AFCL as substrate marker; age effect on AFCL; measurement method (CS vs LA) | HIGH — EP lab parameter |
| **G-3** | Sinus node recovery time (SNRT / cSNRT) | Reference range in elderly AF; age-related sinus node dysfunction co-prevalence | HIGH — procedural safety variable |
| **G-4** | Conduction velocity (invasive EP, in AF) | CV during AF (not just SR mapping); endocardial bipolar; LA vs RA | HIGH — CRF variable |
| **G-5** | Local activation time / activation mapping | LAT maps; total atrial activation time quantification; elderly-specific data | MEDIUM |
| **G-6** | P-wave dispersion | Definition (max−min PWD across leads); threshold (≥40–50 ms); age-related increase | HIGH — CRF variable, simple 12-lead ECG |
| **G-7** | Signal-averaged ECG (SAECG) / filtered P-wave | Filtered P-wave duration >140 ms threshold; root-mean-square voltage; SAECG in elderly AF prediction | MEDIUM |
| **G-8** | P-wave area / P-wave morphology types | P-wave area in V1 vs PTFV1; P-wave positive/biphasic classification; P-wave axis | MEDIUM |
| **G-9** | Elderly-specific normative EP values | Age-stratified reference tables for AERP, CV, SNRT, AFCL from published EP studies | HIGH — anchors the CRF threshold column |
| **G-10** | Vietnamese / Asian EP normative data | Any published EP reference values in Vietnamese or Southeast Asian AF patients | LOW (evidence gap expected; still must probe) |

---

## 4. Per-Source Search Strategy

**Date window:** No lower bound → 2026-06-29 (current run date).
**Existing store status:** 40 records already in `reference/la-electrophysiology-elderly-af.md`.
The searches below are ADDITIVE — they target the gap families above and should not duplicate already-confirmed records. The retriever should deduplicate against the existing store by PMID.

**L-009 reminder:** Every new PMID must be cross-checked: first author + title + journal + year before entering the store.
**L-004 reminder:** Sweep bioRxiv/medRxiv and ClinicalTrials.gov every run.
**L-039 reminder:** After retrieval, run `validate_search_log.py` on the recall ledger.

---

### 4A. PubMed / PMC

#### Concept blocks (MeSH + free-text synonyms)

```
Block A (Population):
  "atrial fibrillation"[MeSH] OR "atrial fibrillation"[tiab]

Block B (Age):
  "aged"[MeSH] OR "elderly"[tiab] OR "older adults"[tiab] OR "age-related"[tiab]
  OR "aging"[MeSH] OR ">65"[tiab] OR "≥65"[tiab] OR "≥75"[tiab] OR ">75"[tiab]

Block C (Conduction — Gap G-1, G-4, G-5):
  "atrial conduction"[tiab] OR "conduction velocity"[tiab] OR "conduction delay"[tiab]
  OR "conduction block"[tiab] OR "interatrial conduction"[tiab]
  OR "intraatrial conduction"[tiab] OR "atrial activation"[tiab]
  OR "local activation time"[tiab] OR "total atrial activation time"[tiab]
  OR "Bachmann's bundle"[tiab] OR "inter-atrial conduction time"[tiab]

Block D (Refractoriness — Gap G-1, G-2, G-3):
  "atrial effective refractory period"[tiab] OR "AERP"[tiab] OR "ERP"[tiab]
  OR "refractory period"[MeSH] OR "atrial refractoriness"[tiab]
  OR "refractory dispersion"[tiab] OR "atrial vulnerability"[tiab]
  OR "AF cycle length"[tiab] OR "atrial cycle length"[tiab] OR "AFCL"[tiab]
  OR "sinus node recovery time"[tiab] OR "SNRT"[tiab] OR "corrected SNRT"[tiab]
  OR "sinoatrial node"[MeSH] OR "sick sinus syndrome"[MeSH]

Block E (P-wave morphology — Gaps G-6, G-7, G-8):
  "P-wave"[tiab] OR "P wave"[tiab] OR "P-wave duration"[tiab]
  OR "P-wave dispersion"[tiab] OR "interatrial block"[tiab]
  OR "advanced interatrial block"[tiab] OR "Bayés syndrome"[tiab]
  OR "Bayes syndrome"[tiab] OR "P-terminal force"[tiab] OR "PTFV1"[tiab]
  OR "P-wave area"[tiab] OR "P-wave axis"[tiab]
  OR "signal-averaged ECG"[tiab] OR "SAECG"[tiab]
  OR "filtered P-wave"[tiab] OR "signal averaged electrocardiogram"[MeSH]
  OR "P-wave morphology"[tiab]
```

#### Query strings to run (prioritized by gap)

**Search P-1 (AERP / refractoriness — Gap G-1, G-2, G-3):**
```
(Block A) AND (Block D) AND (Block B)
Filter: humans; no date limit
```
*Expected yield:* 30–80; deduplicate against store.

**Search P-2 (Conduction — Gaps G-4, G-5):**
```
(Block A) AND (Block C) AND (Block B)
Filter: humans; no date limit
```
*Expected yield:* 20–60.

**Search P-3 (P-wave morphology, SAECG — Gaps G-6, G-7, G-8):**
```
(Block A) AND (Block E)
Filter: humans; no date limit
```
*Note:* Age block intentionally omitted here to catch foundational normative studies (e.g., P-wave dispersion definitions that may not use the term "elderly" but report age-related data). The retriever will prioritize papers with elderly subgroups or age-stratified data.

**Search P-4 (Bayés syndrome / advanced IAB — targeted landmark):**
```
"interatrial block"[tiab] AND ("atrial fibrillation"[MeSH] OR "atrial fibrillation"[tiab])
Filter: humans; no date limit
```
*Note:* Bayés de Luna 2017 already in store (REF-038). This search targets Bayés de Luna 1988 original description, Lorbar 2004, Tse 2008, Baranchuk reviews, and the Bayes de Luna 2022 updated consensus.

**Search P-5 (Normative elderly EP values — Gap G-9):**
```
("electrophysiology study"[tiab] OR "electrophysiological study"[tiab]
  OR "invasive electrophysiology"[tiab])
AND (Block B)
AND ("atrial"[tiab] OR "atrioventricular"[tiab] OR "sinoatrial"[tiab])
Filter: humans; no date limit
```
*Goal:* Catch normative EP studies (AERP, CV, SNRT reference ranges in older adults) that may not specifically mention AF in the title.

**Search P-6 (P-wave dispersion — Gap G-6, targeted):**
```
"P-wave dispersion"[tiab] AND ("atrial fibrillation"[MeSH] OR "atrial fibrillation"[tiab])
Filter: humans; no date limit
```
*Landmark target:* Dilaveris 1998 (original P-wave dispersion definition); Dilaveris 2001 review; Okutucu 2010 review.

**Search P-7 (SAECG filtered P-wave — Gap G-7, targeted):**
```
("signal-averaged electrocardiogram"[tiab] OR "SAECG"[tiab] OR "filtered P-wave"[tiab])
AND ("atrial fibrillation"[MeSH])
Filter: humans; no date limit
```
*Target:* Fukunami 1991 (original filtered P-wave >140 ms threshold for paroxysmal AF prediction); Guidera & Steinberg 1993; Steinberg 1993 review.

**Search P-8 (Vietnam / Southeast Asian AF — Gap G-10, curiosity budget population gap):**
```
("atrial fibrillation"[tiab] OR "atrial fibrillation"[MeSH])
AND ("Vietnam"[tiab] OR "Vietnamese"[tiab] OR "Southeast Asia"[tiab]
     OR "Southeast Asian"[tiab] OR "Viet Nam"[tiab])
AND ("electrophysiology"[tiab] OR "ablation"[tiab] OR "P-wave"[tiab]
     OR "conduction"[tiab])
Filter: humans; no date limit
```
*Expected yield:* Likely small (<10). Even null results are informative (evidence gap).

**Search P-9 (Contradiction gap — elderly AF ERP paradox, curiosity budget):**
```
("atrial effective refractory period"[tiab] OR "AERP"[tiab])
AND ("shortening"[tiab] OR "prolonged"[tiab] OR "reverse remodeling"[tiab]
     OR "electrical remodeling"[tiab])
AND ("aged"[MeSH] OR "elderly"[tiab] OR "aging"[tiab])
Filter: humans and/or animal; no date limit
```
*Rationale:* There is a known contradiction in the literature: acute AF shortens AERP (standard tachycardia-induced remodeling), but some aging studies show paradoxical AERP prolongation with structural remodeling. This search deliberately probes that tension.

**MeSH terms to include in all PubMed searches where relevant:**
- `"atrial fibrillation"[MeSH]`
- `"aged"[MeSH]` / `"aged, 80 and over"[MeSH]`
- `"cardiac electrophysiology"[MeSH]`
- `"refractory period, electrophysiological"[MeSH]`
- `"heart conduction system"[MeSH]`
- `"electrocardiography"[MeSH]`
- `"signal averaged electrocardiogram"[MeSH]`

---

### 4B. Consensus (semantic search)

Consensus searches use natural-language queries; run ≤3 per batch (rate-limit rule). Do not apply year/study-type filters unless the user explicitly requests narrowing.

**Search C-1:** `atrial effective refractory period elderly atrial fibrillation`
**Search C-2:** `P-wave dispersion atrial fibrillation elderly risk`
**Search C-3:** `sinus node recovery time elderly atrial fibrillation electrophysiology`
**Search C-4:** `conduction velocity left atrium aging atrial fibrillation`
**Search C-5:** `signal-averaged ECG filtered P-wave atrial fibrillation prediction`
**Search C-6:** `advanced interatrial block Bayés syndrome atrial fibrillation elderly`

*Note:* Each Consensus result requires L-009 PMID confirmation before entering the store. Known Consensus false-positive risk: confirm first author + title via PubMed before storing.

---

### 4C. bioRxiv / medRxiv

Use `mcp__bioRxiv__search_preprints` by subject category + date range, and `mcp__bioRxiv__search_published_preprints` to check if preprints were subsequently peer-reviewed.

**Search B-1 (category: cardiovascular medicine; date: 2023-01-01 to 2026-06-29):**
Keywords: `atrial fibrillation electrophysiology elderly`
*Target:* Any recent preprint on atrial ERP, AFCL, P-wave morphology, or conduction in elderly AF patients.

**Search B-2 (category: cardiovascular medicine; date: 2023-01-01 to 2026-06-29):**
Keywords: `P-wave morphology interatrial block aging`
*Target:* Preprints on advanced IAB, SAECG, or P-wave dispersion in elderly or AF populations.

**Label all preprints:** "Preprint — không qua bình duyệt đồng nghiệp" in the reference store. Do NOT use as the sole evidence for a CRF threshold.

---

### 4D. ClinicalTrials.gov

Apply L-008: start broad, then narrow.

**Search T-1 (broad — atrial fibrillation elderly EP):**
`atrial fibrillation elderly electrophysiology`
*Filter:* Status = Completed or Active-not-recruiting; condition = AF
*Expected:* Identify any completed trials measuring EP parameters (ERP, AFCL, CV) in elderly cohorts that may have unpublished results or trial-registry-only data.

**Search T-2 (broad — P-wave interatrial block AF):**
`interatrial block atrial fibrillation`
*Filter:* No phase filter (L-008); condition = AF
*Target:* Registries or trials studying advanced IAB or P-wave dispersion as AF predictors.

**Search T-3 (broader — atrial electrophysiology aging):**
`atrial electrophysiology aging sinus node`
*Target:* Studies measuring sinus node function, ERP, or conduction parameters in elderly.

*Record every search, its result count, and at least one reproducible parameter (NCT search URL or query string) in the Recall & Reproducibility Ledger (required for `validate_search_log.py`).*

---

## 5. Pre-registered Outcomes of Interest and Subgroups

The following are the primary and secondary parameters the review must address. These are **fixed in advance** so the synthesis cannot be steered toward parameters where evidence happened to be abundant.

### 5.1 Primary parameter families (must address with definition, unit, method, threshold, evidence level)

| # | Parameter | Measurement method | Unit | Target threshold range (to be confirmed from literature) |
|---|---|---|---|---|
| 1 | **Atrial ERP / AERP** | Programmed stimulation (EP lab; S1–S2 extra-stimulus) | ms | 170–240 ms (general adult; age-adjusted range needed) |
| 2 | **ERP dispersion / refractory heterogeneity** | Max−min AERP across ≥3 sites | ms | <50 ms considered normal; >50 ms = increased dispersion |
| 3 | **AF cycle length (AFCL)** | Interval between successive fibrillatory waves; CS or LA measurement | ms | <150 ms = fine AF / high organization; >180 ms = coarser; age effect direction to confirm |
| 4 | **Sinus node recovery time (SNRT) and cSNRT** | Burst pacing × 30–60 s; longest return cycle; cSNRT = SNRT − mean sinus cycle length | ms | cSNRT normal <550 ms; SNRT normal <1500 ms; elderly thresholds to confirm |
| 5 | **Conduction velocity (LA, intraoperative or endocardial)** | Bipolar electrogram activation time / inter-electrode distance | cm/s or m/s | Normal LA CV ~70–90 cm/s; age-related decline to quantify |
| 6 | **Total atrial activation time (TAAT) / inter-atrial conduction time** | P-wave onset to distal CS electrogram (PA interval); or high-RA to distal CS | ms | PA ≤130 ms normal; >130 ms suggests conduction delay |
| 7 | **Local activation time (LAT)** | Activation time at each mapping point relative to reference | ms | Reported as maps / distribution; key: longest LAT (slowest activation region) |
| 8 | **Conduction delay and block** | Presence/absence and proportion of atrial wall | Qualitative/% area | Prevalence of conduction block; %-area slow-conduction zone |
| 9 | **P-wave duration (PWD)** | Max PWD across all 12 leads on surface 12-lead ECG | ms | Normal ≤110 ms; prolonged ≥120 ms (= partial IAB); advanced IAB ≥120 ms + biphasic inferior |
| 10 | **P-wave dispersion** | Difference: max − min PWD across leads | ms | Normal <40 ms; ≥40–50 ms = increased dispersion |
| 11 | **Advanced interatrial block (advanced IAB) / Bayés syndrome** | PWD ≥120 ms + biphasic (±) P in inferior leads (II, III, aVF) | Binary (present/absent) + PWD (ms) | Prevalence ~9–10% in elderly/cardiac; OR for AF development to cite |
| 12 | **PTFV1 (P-wave terminal force in V1)** | Depth (mm) × duration (ms) of negative terminal P-wave component in V1 | mm·s | Abnormal: >0.04 mm·s; OR 1.39 for AF (Huang 2020) |
| 13 | **P-wave area** | Area under the P-wave; total or negative component | mm·ms or μV·s | To be established from new search |
| 14 | **P-wave axis** | Mean P-wave axis on 12-lead ECG | degrees | Normal 0°–75°; leftward shift with LA enlargement / IAB |
| 15 | **Signal-averaged ECG (SAECG) — filtered P-wave duration** | High-pass filtered (40 Hz) P-wave duration; time-domain SAECG | ms | >140 ms = prolonged (Fukunami 1991); to confirm with age-specific data |

### 5.2 Secondary / contextual variables (needed for CRF completeness)

| # | Parameter | Notes |
|---|---|---|
| S-1 | **LA bipolar voltage / LVZ** | Already well-covered (AC); include for completeness in CRF (threshold <0.5 mV LVZ, <1.5 mV normal); note omnipolar differences |
| S-2 | **Unipolar voltage** | Already covered (AC); threshold ~0.73 mV (5th percentile van der Does); label separately from bipolar (L-018) |
| S-3 | **CFAE presence / distribution** | Covered (AC); include definition (CL <120 ms or ≥2 deflections per Nademanee 2004) and limitations (STAR AF II) |
| S-4 | **LA strain (reservoir)** | Covered (AC); non-invasive; LA reservoir strain <18–20% correlates with electropathology |
| S-5 | **LA diameter / volume index** | Background variable for CRF context (not primary EP parameter) |
| S-6 | **AF type (paroxysmal / persistent / permanent)** | CRF classification variable; affects AERP, AFCL, voltage interpretation |
| S-7 | **Atrial vulnerability index** | Ratio of AF inducibility rate by programmed stimulation (exploratory) |

### 5.3 Pre-registered subgroup analyses

The synthesis must address each of the following explicitly (per L-038):
1. **Age band:** ≥65y overall; ≥75y sub-focus; ≥80y where data exist.
2. **AF type:** Paroxysmal vs persistent vs permanent (parameters may differ systematically).
3. **Sex:** Where reported — women have shorter AERP, different P-wave indices; extract if available.
4. **Asian/Vietnamese populations:** Separate treatment where data exist (highest priority for G-10).
5. **Measurement modality:** Invasive (EP lab) vs non-invasive (surface ECG, SAECG) — clearly separate in CRF table.

---

## 6. Curiosity Budget (mandatory — ≥1 per gap type)

| Gap type | Search | Question being probed |
|---|---|---|
| **Evidence gap** | Search P-5 + P-8 | What EP normative data exist specifically for elderly patients (≥65y) in the EP lab? Are there any published Vietnamese or Southeast Asian reference ranges? Expected: near-zero for Vietnam; sparse for elderly. |
| **Contradiction gap** | Search P-9 (AERP paradox) | The tachycardia-induced remodeling model predicts AERP shortening in AF. But some aging studies show AERP prolongation due to structural remodeling (fibrosis). Does aging override or reverse tachycardia-induced AERP shortening in very elderly persistent-AF patients? Probe this tension explicitly. |
| **Methodological gap** | Search P-7 (SAECG) | SAECG was proposed in the 1990s as an AF predictor. Is it still used? Have modern HD mapping technologies replaced it? Does any study validate SAECG in elderly AF specifically? |
| **Population gap** | Search P-8 (Vietnam/Asia) + T-3 | Which populations are systematically excluded from EP normative data? Expected: elderly patients (>80y), women, Asian/Vietnamese patients, frail patients who cannot undergo invasive EP studies. Document this gap explicitly — it is itself a CRF design implication (proxy parameters needed for those who cannot undergo full EP study). |
| **Implementation gap** | ClinicalTrials.gov (T-1, T-2, T-3) + targeted PubMed | Which of the 15 primary parameters are routinely measurable in a real-world EP study CRF vs which require specialized equipment (e.g., SAECG machine, omnipolar catheter, intraoperative epicardial mapping)? Flag parameters as: (a) standard EP-lab feasible, (b) requires specialized equipment, (c) non-invasive (standard ECG), (d) research-only. This is the CRF's "feasibility" column. |

---

## 7. Planned Evidence-Grading Approach

The appraiser will use **GRADE** adapted for descriptive/characterization questions:

- **High certainty:** Large prospective cohort or SR/MA with consistent results across populations, low risk of bias, precise estimates, no known confounders — appropriate for CRF thresholds stated as "established."
- **Moderate certainty:** Moderate-sized prospective cohort or SR/MA with minor limitations (e.g., heterogeneity, single-center); downgrade for inconsistency or indirectness.
- **Low certainty:** Retrospective cohort, cross-sectional, or small studies; downgrade for risk of bias or imprecision.
- **Very low certainty:** Animal studies, single small series, no human data; label "exploratory" in the CRF.

**Design-specific tools:**
- Cohort/cross-sectional studies: Newcastle-Ottawa Scale (NOS)
- SR/MA: AMSTAR-2 (where feasible given the descriptive focus)
- Normative reference studies: assess sample representativeness, age range, measurement standardization

**Special rule for the CRF table:** For each parameter, the appraiser must assign:
1. GRADE certainty label for the threshold cited
2. Whether the threshold has been validated specifically in elderly (≥65y) vs extrapolated from younger adults
3. Feasibility flag (see Implementation gap above)

---

## 8. Coverage Assessment: Existing Store vs New Searches

| Parameter family | Existing store (40 records) | New searches needed |
|---|---|---|
| LA bipolar/unipolar voltage | AC — 6 records, HIGH evidence | None for primary review; monitor for 2025–2026 updates |
| LGE-MRI fibrosis | AC — 2 records (DECAAF I/II) | None |
| CFAE / rotor / substrate | AC — 5 records | None |
| Mapping technology | AC — 4 records | None |
| LA strain | AC — 3 records | None |
| Conduction (non-AF, intraoperative) | PC — 1 record (van der Does 2021) | P-2: endocardial EP-lab conduction in AF patients |
| **AERP / refractoriness** | **GAP** — 0 records | P-1, C-1, C-3, B-1, T-1, T-3 |
| **AF cycle length** | **GAP** — 0 records | P-1, C-1, C-4 |
| **SNRT / cSNRT** | **GAP** — 0 records | P-1, C-3, T-3 |
| **P-wave duration** | AC — 3 records (Magnani, Bayés de Luna, Intzes SR/MA) | P-3, P-4: add foundational Bayés 1988; Fukunami SAECG |
| **P-wave dispersion** | **GAP** — 0 records | P-6, C-2 |
| **PTFV1** | AC — 1 record (Huang 2020 MA) | None (core meta-analysis covered) |
| **Advanced IAB / Bayés syndrome** | PC — 1 record (Bayés de Luna 2017 review) | P-4: original 1988 paper + updated 2022 consensus |
| **SAECG / filtered P-wave** | **GAP** — 0 records | P-7, C-5 |
| **P-wave area / axis / morphology types** | **GAP** — 0 records | P-3 (broad P-wave search) |
| Elderly-specific normative EP values | **GAP** — indirect evidence only | P-5 |
| Vietnamese / Asian normative data | **GAP** — 0 records (Asian studies cover ablation outcomes, not EP parameters) | P-8 |
| Guideline EP definitions | PC — ESC/AHA/HRS on ablation (REF-029–031) | None; but check if 2023 ACC/AHA guideline has ERP/SNRT definitions |

**Summary:** Of 15 primary CRF parameter families, 6 are fully covered by the existing store, 3 are partially covered (need supplementation), and 6 are genuine gaps requiring new retrieval. The P-wave morphology family is partially covered (PWD + PTFV1 + IAB are in store; P-wave dispersion, SAECG, P-wave area/axis are not).

---

## 9. Recall & Reproducibility Ledger (template for retriever)

The evidence-retriever must fill the following table for every search executed, then pass it to `validate_search_log.py` (P3 deterministic layer):

| Source | Search ID | Query / Call parameters | Total count (probe) | Retrieved N | Pages pulled | Recall verdict | Note |
|---|---|---|---|---|---|---|---|
| PubMed | P-1 | [exact MeSH string] | [esearch retmax=0 count] | [actual N] | [page 1 of N] | Complete / Partial | [reason if partial] |
| PubMed | P-2 | ... | ... | ... | ... | ... | ... |
| ... | ... | ... | ... | ... | ... | ... | ... |
| Consensus | C-1 | [query] | N/A | [N results used] | 1 | Partial (Consensus API does not expose total) | Always partial |
| bioRxiv | B-1 | [category + date + keyword] | [countTotal] | [N retrieved] | [page 1 of N] | Complete / Partial | ... |
| ClinicalTrials.gov | T-1 | [query string + filters] | [totalCount] | [N retrieved] | 1 | Partial if >1 page | ... |

---

## 10. Constitution Compliance Checklist

Before the retriever begins:

- [x] Law 1: All new PMIDs to be cross-checked before entering store (L-009)
- [x] Law 2: Scope confirmed by user — CRF framing + in-depth review; no scope drift
- [x] Law 3: Evidence hierarchy specified in GRADE section above
- [x] Law 4: Synthesis writer must include explicit "Đồng thuận đã thiết lập" and "Tranh luận còn tồn tại" sections (L-026)
- [x] Law 5: Limitations section will document: no age-specific EP normative data for Vietnamese patients; foundational EP studies predate 1990s (ECG technology limitations); CRF thresholds extrapolated from non-elderly in several parameters
- [x] L-011 (guideline search): ESC/AHA/HRS already in store; check 2023 ACC/AHA for ERP/SNRT definitions in P-1/P-5
- [x] L-004 (preprints + registries): bioRxiv B-1/B-2 + ClinicalTrials T-1/T-2/T-3 planned
- [x] L-008 (ClinicalTrials broad first): T-1/T-2/T-3 start broad, no phase filter
- [x] L-032 (output language Vietnamese, fail-closed): confirmed
- [x] L-038 (PICO subgroups explicitly covered): age bands, AF type, sex, Asian population, measurement modality pre-specified
- [x] L-039 (deterministic layers): `validate_search_log.py` runs after retrieval; `extract_numbers.py` before appraisal tables; `citation_audit.py` after QA

---

*Protocol version 1.0 — fixed before any searching begins. Amendments require noting the change and reason.*
