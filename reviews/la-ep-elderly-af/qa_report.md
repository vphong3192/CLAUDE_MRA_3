# QA Verification Report — LA EP Elderly AF Review
**Verifier:** citation-verifier agent
**Draft file:** `_workspace/la-ep-elderly-af-review-draft.md`
**Reference store:** `reference/la-electrophysiology-elderly-af.md`
**Date:** 2026-06-16
**Constitution laws binding:** Law 1 (auto-fail on fabricated citation), Law 2 (language strength), Law 3 (evidence hierarchy), Law 4 (consensus/controversy), Law 5 (limitations), Law 6 (numbers must match source)

---

## 1. Citation Map — Draft [#] → Store REF-XXX

| Draft # | Draft author/year | Store REF | Store PMID | Draft PMID | PMID match | Title match | Citable? |
|---|---|---|---|---|---|---|---|
| [1] | Joglar 2023 ACC/AHA/ACCP/HRS | REF-030 | 38033089 | 38033089 | YES | YES | YES |
| [2] | Hindricks 2020 ESC | REF-029 | 32860505 | 32860505 | YES | YES | YES |
| [3] | Howie 2025 | REF-023 | 40651587 | 40651587 | YES | YES | YES |
| [4] | Wang 2024 | REF-028 | 39135295 | 39135295 | YES | YES | YES |
| [5] | Lin K-B 2021 | REF-002 | 33634168 | 33634168 | YES | YES | YES |
| [6] | Mesquita 2020 | REF-004 | 32068183 | 32068183 | YES | YES | YES |
| [7] | Marzak 2024 | REF-001 | 40201666 | 40201666 | YES | YES | YES |
| [8] | van der Does 2021 | REF-003 | 33650738 | 33650738 | YES | YES | YES |
| [9] | Magnani 2011 | REF-037 | 21255761 | 21255761 | YES | YES | YES |
| [10] | Bayés de Luna 2017 | REF-038 | 28707575 | 28707575 | YES | YES | YES |
| [11] | Huang 2020 | REF-040 | PMID pending | DOI only listed in draft | PARTIAL — no PMID in draft; DOI matches | YES | YES (PMID pending per store) |
| [12] | [Author pending] 2023 | REF-039 | 36413611 | 36413611 | YES | Partial (title TBC) | CONDITIONAL — see note |
| [13] | Nademanee 2004 | REF-009 | 15172410 | 15172410 | YES | YES | YES |
| [14] | Verma 2015 (STAR AF II) | REF-010 | 25946280 | 25946280 | YES | YES | YES |
| [15] | Marrouche 2014 (DECAAF I) | REF-011 | 24496537 | 24496537 | YES | YES | YES |
| [16] | Marrouche 2022 (DECAAF II) | REF-012 | 35727277 | 35727277 | YES | YES | YES |
| [17] | Lin C-H 2021 | REF-022 | 34449092 | 34449092 | YES | YES | YES |
| [18] | Frontera 2025 | REF-035 | 39278611 | 39278611 | YES | YES | YES |
| [19] | Narayan 2024 | REF-036 | 41104347 | 41104347 | YES | YES | YES |
| [20] | Dittrich 2024 | REF-033 | 37227537 | 37227537 | YES | YES | YES |
| [21] | Butcher 2023 | REF-034 | 37204357 | 37204357 | YES | YES | YES |
| [22] | Bahnson 2021 (CABANA age) | REF-018 | 34933570 | 34933570 | YES | YES | YES |
| [23] | Hirata 2026 (REHEALTH AF) | REF-019 | 41288543 | 41288543 | YES | YES | YES |
| [24] | Boehmer 2024 | REF-013 | 39127258 | 39127258 | YES | YES | YES |
| [25] | Prasitlumkum 2022 | REF-015 | 35589557 | 35589557 | YES | YES | YES |
| [26] | Inoue 2025 | REF-020 | 39243122 | 39243122 | YES | YES | YES |
| [27] | Pajareya 2026 | REF-032 | 41784048 | 41784048 | YES | YES | YES |
| [28] | Yang 2021 | REF-026 | 33731545 | 33731545 | YES | YES | YES |
| [29] | Parks 2024 | REF-027 | 39288952 | 39288952 | YES | YES | YES |

**Notes on [11] and [12]:**
- **[11] Huang 2020 (PTFV1 meta-analysis, REF-040):** Draft lists DOI 10.1111/anec.12739 and PMC7358887 (no PMID in reference list). Store confirms DOI and PMC are correct but notes "PMID pending" (get_article_metadata approval needed). The DOI and PMC match; the paper is the correct record. This is NOT a fabricated citation — it is a verified real paper with confirmed DOI and PMC. PMID pending is a store-level administrative gap, not a Law 1 violation. **Verdict: PASS with note** (PMID should be confirmed before final submission).
- **[12] PMID 36413611 (REF-039):** Draft correctly flags this as unverified (full citation pending) and appropriately downgrades the claim to qualitative only. The PMID itself is confirmed as real in the store. **Verdict: Flagged appropriately by the writer; conditional.**

---

## 2. Data Verification — Claim-by-Claim Check

Each substantive claim is listed with its citation, the key data point, what the store records, and the verdict.

### Section 2.1 — Molecular mechanisms [4,5,6]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-01 | Mitochondrial dysfunction strongest mechanism; ROS prolongs APD; cellular senescence increases p16/p21 in human AF LA tissue; TGF-β/MMP axis | [4] Wang 2024 | ROS, p16/p21, SASP TGF-β/MMP, telomere attrition, autophagy | REF-028 full text confirms hierarchy: mitochondrial strongest; p16/p21 elevated in human AF LA; SASP drives TGF-β/MMP; telomere conflicting; autophagy preclinical; gut dysbiosis weakest | PASS |
| D-02 | Draft notes Wang 2024 is a narrative review; directs quantitative data to primary studies | [4] | Appropriate framing | Store explicitly says "cite primary studies for individual data points, not Wang 2024 as data source" | PASS |
| D-03 | Aged mice had higher LA fibrosis and longer P-wave | [5] Lin K-B | Mouse/aged data | REF-002 confirms: "Aged mice showed more LA fibrosis and longer P-wave" | PASS |
| D-04 | HFpEF aged rat model: LA enlargement, fibrosis, slowed conduction, increased inflammasome | [6] Mesquita | Mechanism | REF-004: "aging + HFpEF associated with LA enlargement, fibrosis, slowed conduction, nodal dysfunction and enhanced inflammasome signaling" | PASS |

### Section 2.2 — Voltage and LVZ [5,7,8]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-05 | LVZ threshold < 0.5 mV; consistently used in key studies | [5,7,8] | Threshold value | REF-002 confirms EnSite NAVX, LVZ threshold <0.5 mV bipolar; REF-001 confirms <0.5 mV; REF-003 uses a different method (unipolar, 5th percentile 0.7339 mV) | PASS (threshold applies to bipolar; draft notes methodology-dependency) |
| D-06 | Marzak cohort: 353 persistent-AF patients; bipolar voltage ≥75y: 1.5 [1.2–2.3] mV vs <75y: 2.4 [1.7–2.8] mV; P<0.01; LVZ 67% vs 30%; P<0.01; age difference attenuated after propensity matching | [7] | 1.5 mV, 2.4 mV, 67%, 30% | REF-001 full text: "LA bipolar voltage lower in ≥75y vs <75y: 1.5 [1.2–2.3] mV vs 2.4 [1.7–2.8] mV (P<.01); low-voltage zones more frequent in elderly (45 [67%] vs 86 [30%], P<.01). Over 48.3-mo follow-up...no between-age difference" | PASS — all numbers exact |
| D-07 | Marzak: predictors of LVZ: female sex, age ≥75, renal function (eGFR), LAVI | [7] | Predictors | REF-001: "LVZ predictors: female sex (p<.001), age ≥75 (p=.042), renal function (p=.009), LA volume index (p<.001)" | PASS |
| D-08 | Lin K-B: EnSite NavX; AF groups: <65y 1.9±0.4 mV; 65–79y 1.2±0.4 mV; >80y 1.0±0.4 mV; LVA r=0.392; P<0.001; age β=−0.04 P<0.001; AF β=−1.26 P<0.001 | [5] | Six exact numbers | REF-002 full text (Table 2): AF <65y: 1.9±0.4 | 65–79y: 1.2±0.4 | >80y: 1.0±0.4; LVA% AF r=0.392 p<0.001; β(age)=−0.04 p<0.001; β(AF)=−1.26 p<0.001. Mapping system: EnSite NAVX | PASS — all numbers exact |
| D-09 | van der Does: 216 patients without AF history; CABG; conduction velocity coef −0.210 P=0.002; voltage fell most at RA and Bachmann's bundle (both P<0.0005) | [8] | CV coef; voltage; site; P values | REF-003 full text: n=216; CV "coef −.210, p=.002"; "median voltage fell with age most at the right atrium (coef −.291) and Bachmann's bundle (coef −.328), both p<.0005" | PASS — all numbers exact |

**NOTE on D-09:** Draft says "điện thế trung vị giảm mạnh nhất ở nhĩ phải và bó Bachmann (cả hai P<0.0005)" — this matches the store's statement that BOTH the RA (coef −.291) and Bachmann's bundle (coef −.328) have P<0.0005. PASS.

### Section 2.3 — P-wave markers [9,10,11,12]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-10 | Framingham cohort: N=1,550; ≥60 years; free of AF at baseline; each 10 ms PWD increment associated with increased long-term AF risk after multivariate adjustment | [9] Magnani 2011 | N=1,550; ≥60y; 10 ms per-increment | REF-037: "N=1,550 Framingham Heart Study participants aged ≥60 years (58% women); free of prevalent AF at baseline...Each 10-ms increment in PWD associated with significant increase in long-term AF risk after multivariate adjustment" | PASS — matches exactly |
| D-11 | GRADE label: Moderate ⊕⊕⊕○; prospective cohort large elderly; downgraded for 1960s–70s ECG technique | [9] | GRADE | Store GRADE: "Moderate (large prospective cohort; ECGs from 1960s–70s limit generalizability to modern ECG techniques)" | PASS |
| D-12 | Advanced IAB: PWD ≥120 ms + biphasic (±) in II, III, aVF; reflects block in Bachmann's bundle; Bayés syndrome = advanced IAB → paroxysmal AF → stroke; prevalence ~1% general population, 9–10% elderly/cardiac patients | [10] Bayés de Luna 2017 | Definition criteria; prevalence figures | REF-038: "Advanced IAB definition: P-wave duration ≥120 ms + biphasic (±) morphology in inferior leads (II, III, aVF); reflects total block in Bachmann's bundle region"; "Advanced IAB prevalence: ~1% in general population, up to 9–10% in elderly/cardiac patients" | PASS — all three data points match |
| D-13 | Huang PTFV1 meta-analysis: 12 studies; N=51,372; OR pooled 1.39 (95% CI 1.08–1.79; P=0.01); subgroups: hemodialysis OR 4.89; stroke OR 1.60; general population OR 1.15 | [11] Huang 2020 | 12 studies; N=51,372; OR 1.39; CI 1.08–1.79; P=0.01; three subgroup ORs | REF-040: "12 studies; N=51,372 participants"; "pooled OR 1.39 (95% CI 1.08–1.79; p=0.01)"; "hemodialysis OR 4.89; acute ischemic stroke OR 1.60; general population OR 1.15" | PASS — all six data points exact |
| D-14 | Draft [12]: states PWD prolonged before ablation associated with AF recurrence; explicitly flags "⚠️ ước lượng gộp định lượng chưa thẩm định toàn văn"; claims kept qualitative; PMID 36413611 confirmed real | [12] REF-039 | Qualitative claim only; explicit downgrade warning | Store REF-039: "Exact pooled estimate pending full-text verification"; "Full text retrieved: NOT YET RETRIEVED (PMC9935015 available)"; "Retrieve to confirm full citation and results before citing" | PASS — draft correctly follows store's constraint; qualitative framing is appropriate. The warning label in the text exactly mirrors the store's caution. |

### Section 2.4 — CFAE and conduction [13,14,8]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-15 | Nademanee: N=121; age 63±12; AF terminated during ablation in 95% without external cardioversion; 110/121 (91%) free of arrhythmia at 1 year; 76% single-procedure | [13] | N=121; 63±12; 95%; 110/121; 91%; 76% | REF-009 full text: "N=121 (92 men, 29 women)...mean age 63±12y"; "AF termination during ablation: 95% without external cardioversion"; "1-year outcome: 110/121 (91%) free of arrhythmia at 1 year; 76% (92/121) single-procedure" | PASS — all six data points exact |
| D-16 | Draft mentions CFAE system CARTO; criteria: ≥2 deflections OR cycle length <120 ms | [13] | CARTO; criteria | REF-009: "Mapping system: CARTO"; "CFAE definition (2 criteria, either qualifying): (1) ≥2 deflections or continuous deflection over 10-s recording; (2) cycle length <120 ms averaged over 10s. Bipolar filtered 30–500 Hz" | PASS |
| D-17 | STAR AF II: N=589 randomized; EnSite Velocity; 18 months: 59% (PVI alone) vs 49% (PVI+CFAE) vs 46% (PVI+lines); P=0.15; procedure time ~1 hour longer P<0.001 | [14] | N=589; 59%; 49%; 46%; P=0.15; 1 hour | REF-010 full text: "N=589 randomised → 549 in outcome analysis"; "Primary outcome: PVI 59% (36/61) vs PVI+CFAE 49% (119/244) vs PVI+lines 46% (112/244); P=0.15"; "Procedure time ~1 hour longer for CFAE and lines arms vs PVI alone (P<0.001)"; "Mapping system: EnSite Velocity" | PASS — all data points exact |
| D-18 | Note: no CFAE age subgroup from STAR AF II in verified full text | [14] | No elderly data in main text | REF-010: "Age subgroup: Prespecified; no significant interaction found; results in Supplementary Fig. S7 — not in this HTML" | PASS — draft correctly notes this gap |

### Section 3 — LGE-MRI and DECAAF [15,16]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-19 | DECAAF I: 329 enrolled → 260 analyzed; mean age 59.1±10.7; Utah stages I<10%, II 10–<20%, III 20–<30%, IV≥30%; HR per 1% fibrosis 1.06 (95% CI 1.03–1.09; P<0.001); cumulative recurrence Utah I 15.3% vs IV 69.4% by day 475 | [15] | 329; 260; 59.1±10.7; 1.06; CI; 15.3%; 69.4%; day 475 | REF-011 full text: "329 enrolled → 260 in final analysis"; "mean age 59.1 (SD 10.7) y"; Utah definitions match exactly; "HR per 1% fibrosis increase: 1.06 (95% CI 1.03–1.09, P<.001)"; "Cumulative recurrence by day 475: Utah I: 15.3%; IV: 69.4% (95% CI 48.6–87.7%)" | PASS — all eight data points exact |
| D-20 | Draft: age not significant predictor (HR 1.05 [0.86–1.28] per 10 years; P=0.61); no elderly subgroup | [15] | HR 1.05; CI; P=0.61 | REF-011: "Age as predictor (univariable): HR 1.05 (0.86–1.28) per 10 y, P=.61 — NOT significant; age >75y (CHADS2 component): HR 1.19 (0.48–2.93), P=.71 — NOT significant. No elderly subgroup analysis." | PASS — exact match |
| D-21 | DECAAF II: N=843; mean age 62.7; recurrence 43.0% vs 46.1%; HR 0.95 [95% CI 0.77–1.17]; P=0.63; safety events 2.2% vs 0%; P=0.001; 6 ischemic strokes (1.5%) | [16] | N=843; 62.7; 43.0%; 46.1%; HR 0.95; CI; P=0.63; 2.2%; 0%; P=0.001; 6 strokes | REF-012: "843 randomized (mean age 62.7y)"; "fibrosis-guided+PVI 175/421 (43.0%) vs PVI-only 188/422 (46.1%)"; "HR 0.95 [95% CI 0.77–1.17], P=.63"; "9 [2.2%] vs 0, P=.001, including 6 ischemic strokes (1.5%)" | PASS — all numbers exact |
| D-22 | Draft notes DECAAF II data from abstract only; PMC full text empty | [16] | Provenance flag | REF-012: "Full text retrieved: ABSTRACT ONLY (PMC9214588 — get_full_text_article attempted twice...both returned empty full-text body. All numbers from verified structured abstract.)" | PASS — draft correctly flags this |

### Section 4 — Non-PV foci and functional substrate [17,18]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-23 | Lin C-H: N=1,585; age groups 20–40, 41–64, ≥65; non-PV foci: young 8.6% vs middle 3.6% vs old 3.3%; P<0.01; SVC: young 13.1% vs middle 7.8% vs old 6.5%; P=0.03 | [17] | N=1,585; three age groups; non-PV foci %; SVC %; P values | REF-022: "N=1,585 AF ablation pts; young 20–40 (n=175), middle 41–64 (n=1,134), old ≥65 (n=276)"; "Non-PV foci only (overall): young 8.6% vs middle 3.6% vs old 3.3%; P<0.01"; "SVC focus prevalence: young 13.1% vs middle 7.8% vs old 6.5%; P=0.03" | PASS — all data points exact |
| D-24 | Recurrence after multiple procedures (mean FU 5.6 years): young 12.1% vs middle 17.2% vs old 19.3%; P=0.2 | [17] | 12.1%; 17.2%; 19.3%; 5.6 years; P=0.2 | REF-022: "Recurrence after multiple procedures (mean follow-up 5.6±1.2y): young 12.1% vs middle 17.2% vs old 19.3%; P=0.2 — NS" | PASS — exact match |
| D-25 | Draft correctly notes direction of non-PV foci is HIGHER in young, not elderly (corrects initial protocol assumption) | [17] | Direction correction | REF-022 confirms same. Store also notes "Young pts had more non-PV foci (esp. SVC)" | PASS — draft aligned with source, Law 1 honored |
| D-26 | Frontera: 63 patients; 234 conduction abnormalities; 125 (53.4%) functional (rhythm-dependent); 88% of functional sites have normal bipolar voltage; residual functional phenomena post-PVI: HR 2.539 (95% CI 1.458–4.420; P=0.001); LVA only significant univariably | [18] | 63 patients; 234 total; 125; 53.4%; 88%; HR 2.539; CI 1.458–4.420; P=0.001 | REF-035 full text: "N=63"; "Total conduction abnormalities: 234"; "Functional (rhythm-dependent): 125 (53.4%)"; "Normal voltage at functional sites: 88%"; "Multivariable Cox — residual functional phenomena: HR 2.539 (1.458–4.420); P=0.001 — only independent predictor"; "LVA univariable: HR 1.547 (1.070–2.237); P=0.020; NOT significant in multivariable" | PASS — all seven data points exact |

### Section 5 — EAM systems and omnipolar [19,20,21]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-27 | Narayan: three EAM systems (CARTO 3, EnSite X, Rhythmia); "less clear" they improve ablation outcomes for AF; no RCT; PVI success ~50–75% at 12–18 months; bipolar amplitude variation >50% from wavefront direction | [19] | Three systems named; "less clear"; >50% variation; 50–75% PVI success | REF-036: "Carto 3 (Biosense-Webster), EnSite X (Abbott), Rhythmia (Boston Scientific)"; "it is less clear that they have improved ablation outcomes particularly for AF"; "Propagation perpendicular to a bipole generates zero amplitude, and thus can result in >50% variations in electrogram amplitude"; "success of PVI remains ~50–75% over 12–18 months" | PASS — all claims exact |
| D-28 | Dittrich: 45 patients (own control); predominantly persistent AF; mean age 67.3±9.0; OT vs SD: point density 21,471±10,428 vs 6,682±3,009 (P<0.001); mean voltage OT 0.75±0.30 mV vs SD 0.61±0.24 mV (P<0.001); PV gaps OT 4 [3–5] vs SD 2 [2–3] per map (P=0.001) | [20] | 45 patients; 67.3±9.0; point density numbers; voltage numbers; PV gap numbers; P values | REF-033 full text: "45 patients (30 atrial, 15 ventricular); each patient as own control"; "mean age 67.3±9.0y" (atrial group); "OT 21,471±10,428 vs SD 6,682±3,009...P<0.001"; "atrial: OT 0.75±0.30 mV vs SD 0.61±0.24 mV...OT vs SD P<0.001"; "PV gap detection (atrial): OT 4 [3–5] gaps vs SD 2 [2–3] gaps per map; P=0.001" | PASS — all nine data points exact |
| D-29 | Draft says "EnSite X / HD Grid" for Dittrich | [20] | Mapping system | REF-033: "Mapping system: EnSite X (Abbott); Advisor HD Grid (16 electrodes, 4×4)" | PASS |
| D-30 | Butcher: 40 persistent AF patients; HD Grid on EnSite; OV 0.55±0.18 mV vs BV 0.38±0.12 mV (P=0.003); LVZ area: OV 42.4% vs BV 66.7% (P<0.001); 94.7% of BV-only LVZ = wavefront collision; OV vs BV SR difference 0.09±0.03 mV (P=0.24); AUC=0.89 (P<0.001) for gap detection | [21] | 40 patients; OV 0.55; BV 0.38; P=0.003; LVZ 42.4%; 66.7%; P<0.001; 94.7%; 0.09±0.03; P=0.24; AUC 0.89 | REF-034 full text: "N=40"; "Abbott EnSite + HD Grid catheter"; "OV 0.55±0.18 mV vs BV 0.38±0.12 mV; difference 0.20±0.07 mV; P=0.003"; "LVZ area %: OV 42.4%±12.8% vs BV 66.7%±12.7%; P<0.001"; "False LVZ: 94.7% corresponded to wavefront collision"; "0.09±0.03 mV difference; P=0.24 NS"; "OV AUC=0.89; P<0.001" | PASS — all ten data points exact |
| D-31 | Draft says ~24 percentage point overestimation by bipolar (66.7 − 42.4 = 24.3 pp); refers to as "~24 points" | [21] | Derived calculation | 66.7% − 42.4% = 24.3 percentage points. Store confirms both numbers. Arithmetic correct. | PASS |

### Section 6 — Ablation outcomes: CABANA and REHEALTH AF [22,23]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-32 | CABANA: N=2,204; ≥75y n=308 (14.0%); primary composite aHR by age: <65y 0.57; 65–74y 0.79; ≥75y 1.39 [0.75–2.58]; 4-year event rates ≥75y: 14.8% (ablation) vs 9.0% (drug); all-cause mortality ≥75y: 1.92 [0.88–4.17]; P interaction mortality = 0.031; AF recurrence consistent: aHR 0.47/0.58/0.49 | [22] | N=2,204; ≥75y=308 (14.0%); aHR 0.57; 0.79; 1.39 [0.75–2.58]; 14.8%; 9.0%; 1.92 [0.88–4.17]; P=0.031; 0.47/0.58/0.49 | REF-018 full text (Circulation PMC9003625): "N=2,204"; "<65y n=766 (34.8%); 65–74y n=1,130 (51.3%); ≥75y n=308 (14.0%)"; "primary composite aHR: <65y: 0.57 (0.30–1.09); 65–74y: 0.79 (0.54–1.16); ≥75y: 1.39 (0.75–2.58)"; "4-year primary event rates: ≥75y 14.8% vs 9.0%"; "total mortality aHR ≥75y: 1.92 (0.88–4.17); interaction p=0.031 (SIGNIFICANT)"; "AF recurrence (aHR): <65y: 0.47; 65–74y: 0.58; ≥75y: 0.49" | PASS — all twelve data points exact |
| D-33 | P-interaction for primary composite = 0.134 (not significant); only mortality interaction significant at 0.031 | [22] | P-interaction primary vs mortality | REF-018: "interaction p=0.134" for primary composite; "interaction p=0.031 (SIGNIFICANT)" for mortality | PASS — draft correctly distinguishes the two interaction P-values |
| D-34 | REHEALTH AF: Hirata; 47 Japanese hospitals; ≥80y; 193 matched pairs; median FU 504 days; aHR 0.44 (95% CI 0.21–0.92; P=0.029); unadjusted HR 0.65 (P=0.21); IPTW HR 0.97 (NS) | [23] | 47 hospitals; ≥80y; 193 pairs; 504 days; aHR 0.44; CI 0.21–0.92; P=0.029; HR 0.65; P=0.21; IPTW 0.97 | REF-019 full text: "47 Japanese hospitals (35 ablation + 12 non-ablation)"; "≥80y nonvalvular AF"; "193 matched pairs"; "median follow-up 504 days"; "aHR 0.44 (0.21–0.92); P=0.029"; "Unadjusted matched HR 0.65 (0.33–1.27); P=0.21"; "IPTW HR 0.97 NS" | PASS — all nine data points exact |
| D-35 | Draft notes CFS ≥7 excluded from REHEALTH AF | [23] | Exclusion criterion | REF-019: "CFS ≥7 excluded" | PASS |

### Section 6 — Meta-analyses [24,25]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-36 | Boehmer: 19 studies; 108,419 patients; 6,575 ≥75y; recurrence 39% vs 32%; RR 1.24 (95% CI 1.09–1.42; P=0.001); persistent AF RR 1.64 | [24] | 19 studies; 108,419; 6,575; 39%; 32%; RR 1.24; CI 1.09–1.42; P=0.001; persistent RR 1.64 | REF-013 full text: "19 studies"; "108,419 pts (101,844 <75y; 6,575 ≥75y)"; "Recurrence: elderly 39% vs young 32%; RR 1.24 (95% CI 1.09–1.42); P=0.001"; "Recurrence (persistent AF): RR 1.64 (1.18–2.28); P=0.003" | PASS — all data exact. NOTE: Draft says P=0.001 (PASS), CI 1.09–1.42 (PASS). Draft says "RR 1.24; 95% CI 1.09–1.42" — exact match. |
| D-37 | Prasitlumkum: 27 studies; 363,542 patients; ablation success OR 0.85 (95% CI 0.69–1.05; NS) | [25] | 27 studies; 363,542; OR 0.85; CI 0.69–1.05 | REF-015 full text: "27 observational studies"; "363,542 pts"; "Ablation success (overall): pooled OR 0.85 (0.69–1.05); P=0.131...NS" | PASS |
| D-38 | Prasitlumkum: cryoablation no higher complications (OR 0.97; NS) vs RF higher (OR 1.48) | [25] | Cryo OR 0.97; RF OR 1.48 | REF-015: "Complications by technique: RF: OR 1.48 (1.22–1.79); cryotherapy: OR 0.97 (0.56–1.67) NS" | PASS |

### Section 6.2 — Safety [26,27]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-39 | Inoue: 170,017 procedures; complication rates by age: ≤64y 2.27%, ≥85y 4.30%; Cochran-Armitage trend P<0.001; OR vs ≤64y at ≥85y: 1.94 [1.60–2.34]; age ≥80 multivariate OR 1.22 [1.11–1.34]; 1-year recurrence no difference (log-rank P=0.473) | [26] | 170,017; 2.27%; 4.30%; P<0.001; OR 1.94 [1.60–2.34]; OR 1.22 [1.11–1.34]; P=0.473 | REF-020 full text: "Safety cohort N=170,017"; "≤64y: 2.27%; ≥85y: 4.30%; Cochran-Armitage trend P<0.001"; "≥85y: 1.94 (1.60–2.34)"; "Age ≥80 multivariable 1.22 (1.11–1.34)"; "log-rank P=0.473 — NO significant difference by age" | PASS — all eight data points exact |
| D-40 | Pajareya (PFA): 10 studies; N=5,948; 900 elderly; arrhythmia-free survival OR 0.81 (CI 0.41–1.59; NS); overall complications OR 1.93 (CI 1.29–2.91; P=0.020) | [27] | 10 studies; 5,948; 900; OR 0.81 [0.41–1.59]; NS; OR 1.93 [1.29–2.91]; P=0.020 | REF-032 full text: "10 studies; N=5,948: 900 elderly ≥75y"; "Arrhythmia-free survival: OR 0.81 (0.41–1.59; I²=0%; P=0.315) — NOT significant"; "Overall complications (head-to-head): OR 1.93 (1.29–2.91; I²=0%; P=0.020) — SIGNIFICANT" | PASS — all six data points exact |

### Section 6.3 — Frailty [28,29]

| # | Claim in draft | Citation | Key data checked | Store says | Verdict |
|---|---|---|---|---|---|
| D-41 | Yang: Hospital Frailty Risk Score; ≥75y; non-frail: mortality HR 0.48 (P=0.004); composite HR 0.54 (P<0.001); frail: mortality HR 0.83 (P=0.506); composite HR 0.71 (P=0.076); interaction P=0.021 | [28] | HR 0.48; P=0.004; HR 0.54; P<0.001; HR 0.83; P=0.506; HR 0.71; P=0.076; P-interaction 0.021 | REF-026 full text: "NON-FRAIL: all-cause death HR 0.48 (0.30–0.79); P=0.004. Composite HR 0.54 (0.38–0.75); P<0.001. FRAIL: all-cause death: HR 0.83 (0.48–1.44); P=0.506 NS. Composite: HR 0.71 (0.48–1.04); P=0.076 NS. Frailty × ablation interaction: P interaction=0.021" | PASS — all nine data points exact |
| D-42 | Draft cautions: P-interaction should be interpreted cautiously (subgroup context) | [28] | Caution statement | REF-026: "P interaction=0.021 (reported in context of all-cause death subgroup; caution — may refer to specific EF≥80% subgroup context; main divergence confirmed by non-overlapping CIs)" | PASS — draft appropriately reproduces this caution |
| D-43 | Parks: CFS (9-point) and CGA; framework: fit/multimorbid/end-stage; most RCTs "age-agnostic" | [29] | CFS; CGA; framework | REF-027: "CFS (9-point) as practical means; CGA as most in-depth. Framework: (1) Fit and functional, (2) Multimorbid/frail, (3) End-stage/end of life"; "most AF RCTs/guidelines are 'age-agnostic'" | PASS |

---

## 3. Language Audit — Strength vs. GRADE

| # | Claim phrasing (Vietnamese draft) | GRADE label in draft | GRADE in store | Language verdict | Issue? |
|---|---|---|---|---|---|
| L-01 | "cơ chế có chứng cứ mạnh nhất" (strongest mechanism) for mitochondria dysfunction | No GRADE for Wang narrative review | Store: N/A (review) | Appropriate — phrasing attributes hierarchy to the review's own framework, not as established causal fact | PASS |
| L-02 | "các loài oxy phản ứng (ROS) kéo dài thời gian điện thế hoạt động và làm tăng dòng natri muộn" | Mechanistic; in mechanism section | Very Low (animal/translational) | Appropriate — stated in mechanistic context, not clinical fact | PASS |
| L-03 | "điện thế lưỡng cực nhĩ trái toàn cục thấp hơn rõ ở nhóm ≥75 tuổi" (significantly lower voltage) | GRADE ⊕⊕○○ | Low (retrospective cohort) | Language matches Low GRADE; "lower" = observational association, not causal | PASS |
| L-04 | "Bằng chứng cho thấy điện thế nhĩ trái giảm và LVZ tăng theo tuổi tương đối thống nhất về hướng" (evidence consistent in direction) | Mixed GRADE ⊕○○○–⊕⊕○○ | Low/Very Low | "Consistent in direction" — appropriately hedged language for Low GRADE evidence | PASS |
| L-05 | "Bayés syndrome" definition stated as "mô tả mối liên hệ" (describes the association) not "chứng minh nhân quả" | Not GRADE labeled (consensus/definition) | N/A (review) | Draft explicitly notes "không phải mức nhân quả đã chứng minh" | PASS |
| L-06 | PTFV1: "liên quan có ý nghĩa với rung nhĩ" (significantly associated) with "ngôn ngữ liên quan, không nhân quả" | GRADE ⊕⊕⊕○ Moderate | Moderate (SR/MA observational) | PASS — association language used; draft explicitly flags "liên quan, không nhân quả" |
| L-07 | PWD [12]: kept qualitative "liên quan với tái phát" (associated with recurrence) | Flagged "chưa thẩm định" | GRADE not assigned | PASS — qualitative claim is appropriately conservative given unverified quantitative estimate |
| L-08 | CFAE Nademanee [13]: stated as "loạt quan sát mốc lịch sử" (historical observational series) at GRADE ⊕⊕○○ | GRADE ⊕⊕○○ | Store: Low (observational landmark) | PASS |
| L-09 | STAR AF II conclusion: "CFAE-guided ablation không nên coi là chiến lược cải thiện kết cục đã được chứng minh" (should not be regarded as proven) | GRADE ⊕⊕⊕○ | Moderate (RCT before downgrade) | PASS — "not proven" correctly avoids overclaiming the RCT negative result while also not dismissing it |
| L-10 | DECAAF II: "không cải thiện kết cục" (did not improve outcomes) | GRADE ⊕⊕⊕○ | Moderate (RCT) | PASS — correct framing of a negative RCT result; language matches evidence strength |
| L-11 | Frontera: "dự báo độc lập tái phát" (independently predicts recurrence) | GRADE ⊕⊕○○ | Low (prospective, n=63) | MINOR FLAG: "dự báo độc lập" (independent predictor) is technically accurate (multivariable Cox HR 2.539 with P=0.001) but the sample size is small (n=63). The GRADE label ⊕⊕○○ appropriately hedges. The phrase is supported by the statistics but should be read in context of the GRADE label. Acceptable given explicit GRADE annotation. | BORDERLINE — PASS with annotation |
| L-12 | "lợi ích của triệt đốt sau hiệu chỉnh đa biến" (benefit of ablation after multivariable adjustment) for REHEALTH AF | GRADE ⊕⊕○○ | Low (observational registry) | PASS — language explicitly notes the conditionality of adjustment; draft further notes IPTW non-significant |
| L-13 | CABANA ≥75y: "không xác định, có khuynh hướng bất lợi" (indeterminate, trend to harm) | GRADE ⊕⊕⊕○ | Moderate (RCT subgroup) | PASS — appropriate language for an imprecise subgroup estimate with wide CI |
| L-14 | Inoue: "gradient biến chứng tăng đều theo tuổi" (complication gradient rises steadily with age) | GRADE ⊕⊕○○ | Low (registry) | PASS — observational association language, consistent with Low GRADE |
| L-15 | Yang: "lợi ích mất ý nghĩa" (benefit loses significance) in frail patients | GRADE ⊕⊕○○ | Low (retrospective cohort) | PASS — "lose significance" is accurate for NS P-values in frail subgroup |

**Summary: No language violations requiring mandatory correction. One borderline case (L-11) is adequately covered by explicit GRADE annotation.**

---

## 4. Law Violations

### Law 1 (Fabricated citations)
- No fabricated citations found. All 29 draft references map to confirmed store records with matching PMIDs (except [11] where PMID is pending at store level but DOI and PMC are verified).
- **Citation [12] (PMID 36413611, REF-039):** The PMID is confirmed real by the store. The draft correctly handles its unverified status by (a) using qualitative language only, (b) attaching a prominent warning flag, (c) noting the limitation in Appendix A, and (d) noting it in the variable table with a warning symbol. This is exemplary Law 1 compliance.
- **Verdict: NO Law 1 violations. Auto-fail not triggered.**

### Law 2 (Evidence language must match GRADE strength)
- All claims reviewed: no causal language used for Low/Very-Low evidence. Association language is consistent throughout.
- One borderline case (L-11, Frontera "independent predictor" with n=63) is covered by explicit GRADE ⊕⊕○○ annotation.
- **Verdict: NO Law 2 violations.**

### Law 3 (Evidence hierarchy)
- STAR AF II (RCT) correctly cited as overriding Nademanee (observational) per Law 3. Draft explicitly states this.
- DECAAF II (RCT) correctly placed above DECAAF I (cohort) for the intervention vs. prognostic question.
- **Verdict: NO Law 3 violations.**

### Law 4 (Consensus vs. controversy)
- Appendix B explicitly lists established consensus and ongoing controversy.
- Within text: CFAE (§2.4), LGE-MRI targeting (§3), and ablation outcomes ≥75y (§6.1) all have marked controversy boxes with both sides cited.
- **Verdict: NO Law 4 violations.**

### Law 5 (Limitations transparency)
- Appendix A is comprehensive: lists source scope, evidence level, unverified records (REF-039), direction corrections, missing elderly data, unvalidated omnipolar thresholds, and absence of Vietnamese population data.
- **Verdict: NO Law 5 violations.**

### Law 6 (No invented numbers)
- All quantitative claims checked against the reference store. Zero discrepancies found in 50+ individual data points checked.
- **Verdict: NO Law 6 violations.**

---

## 5. Special Focus Areas

### Citation [12] (PMID 36413611, REF-039) — "Unverified" flag
- **Store status:** PMID confirmed real; full text NOT retrieved; PMC9935015 available but not yet pulled; exact pooled estimate unknown.
- **Draft handling:** Keeps claim qualitative ("liên quan với tái phát") with explicit ⚠️ warning; repeats in variable table with "⚠️ ước lượng gộp chưa thẩm định"; lists in Appendix A as unverified.
- **Verdict: APPROPRIATE. The flag is correctly placed and Law 1 is honored. Full quantitative use should await PMC9935015 retrieval.**

### Citation [11] (Huang 2020 PTFV1, REF-040) — PMID pending
- **Store status:** DOI 10.1111/anec.12739 confirmed; PMC7358887 confirmed; PMID pending (get_article_metadata needs approval).
- **Draft listing:** Lists DOI and PMC7358887 without a PMID. This is the correct and honest approach given the store's record.
- **Data verification:** All five key numbers verified exact (12 studies; N=51,372; OR 1.39; CI 1.08–1.79; P=0.01; three subgroup ORs).
- **Verdict: PASS. Not a fabricated citation. Note: PMID should be confirmed before final dissertation submission.**

### Dittrich [20] — Exact numbers
- All confirmed exact: 45 patients; age 67.3±9.0; OT 21,471±10,428 vs SD 6,682±3,009 points; OT voltage 0.75±0.30 vs SD 0.61±0.24 mV; PV gaps 4 [3–5] vs 2 [2–3].
- **Verdict: PASS.**

### Butcher [21] — Exact numbers
- All confirmed exact: N=40; OV 0.55±0.18 vs BV 0.38±0.12 mV (P=0.003); LVZ 42.4% vs 66.7% (P<0.001); 94.7% wavefront collision; OV-SR difference 0.09±0.03 mV (P=0.24 NS); AUC=0.89 (P<0.001).
- **Verdict: PASS.**

### REHEALTH AF [23] — Key numbers
- aHR 0.44 (0.21–0.92) P=0.029: CONFIRMED EXACT.
- Unadjusted matched HR 0.65 (P=0.21): CONFIRMED EXACT.
- IPTW HR 0.97 NS: CONFIRMED EXACT.
- **Verdict: PASS.**

### CABANA [22] — Age-group aHRs and p-interaction
- Primary composite: 0.57/0.79/1.39 [0.75–2.58]: CONFIRMED EXACT.
- P-interaction primary = 0.134 (NS): Draft notes "Tuy vậy" (however) for AF recurrence consistency — the P-interaction for the primary composite is 0.134. Draft does not cite this number explicitly, but it also does not claim interaction is significant for the primary composite. Only mortality interaction (P=0.031) is cited as significant. CONFIRMED ACCURATE.
- Mortality aHR ≥75y: 1.92 [0.88–4.17]; P-interaction = 0.031: CONFIRMED EXACT.
- AF recurrence aHR: 0.47/0.58/0.49: CONFIRMED EXACT.
- 4-year event rates: 14.8% vs 9.0%: CONFIRMED EXACT.
- **Verdict: PASS.**

### Frontera [18] — HR 2.539, 88%, 53.4%
- HR 2.539 (1.458–4.420; P=0.001): CONFIRMED EXACT (REF-035: "HR 2.539 (1.458–4.420); P=0.001").
- 88% normal bipolar voltage: CONFIRMED EXACT (REF-035: "Normal voltage at functional sites: 88%").
- 53.4% functional: CONFIRMED EXACT (REF-035: "Functional (rhythm-dependent): 125 (53.4%)").
- **Verdict: PASS — all three priority checks confirmed.**

### Non-PV foci direction — Lin C-H [17]
- Store confirms: "Non-PV foci only: young 8.6% vs middle 3.6% vs old 3.3%; P<0.01" — HIGHER in young, not elderly.
- Draft correctly presents this and includes a warning note that this contradicts the original protocol assumption.
- **Verdict: PASS — Law 1 honored; draft corrects the initial protocol direction.**

---

## 6. Reference List Completeness and Format Check

| Check | Result |
|---|---|
| All 29 citations in body have a reference-list entry | YES — entries 1–29 listed in Section 10 |
| All reference-list entries used in body (no orphan refs) | YES — all 29 are cited at least once |
| Numbering contiguous (1–29, no gaps) | YES |
| Vancouver format (Author et al. Journal. Year;volume:pages. PMID: [link].) | MOSTLY — see notes below |
| Every reference hyperlinked to PubMed URL | YES — all 29 have clickable PubMed URL except [11] (DOI only; no PubMed hyperlink because PMID pending) |
| Reference [11] missing PMID link | Note: draft lists DOI and PMC but no PMID URL; this is honest (PMID pending) but the reference entry is not fully Vancouver-complete |

**Format notes:**
- Reference [11] (Huang 2020): Draft lists "DOI: [10.1111/anec.12739]. PMC7358887." No PMID hyperlink. Acceptable given store's pending status, but flag for update once PMID confirmed.
- Reference [12]: Listed as "[Tác giả chờ xác minh toàn văn]" (author pending verification) with PMID 36413611 and PMC9935015. Honest but not a complete Vancouver citation. Appropriate given constraints.
- Reference [18] (Frontera): Draft lists year 2025; store confirms print year is 2025 (Vol.22); online accept 2024. Correct.
- Reference [26] (Inoue): Draft lists year 2025 for journal; store confirms "Journal year is 2025 (not 2024 as in PMID year)." Correct.
- All DOIs are correctly formatted and hyperlinked where present.
- Overall Vancouver formatting is consistent and acceptable.

---

## 7. Overall Verdict

**CONDITIONAL PASS**

All 29 citations map to confirmed, real records in the reference store. Zero fabricated citations. All 50+ quantitative data points checked match their source records exactly. Language strength is aligned with GRADE levels throughout. Law 4 (consensus/controversy) is explicitly addressed in Appendix B and in three embedded controversy boxes. Law 5 (limitations) is comprehensively covered in Appendix A.

**Two conditional items (not blocking):**
1. **Citation [11]** (Huang PTFV1): PMID pending confirmation at the store level. DOI and PMC confirmed. Claim data verified exact. Upgrade to FULL PASS when PMID is confirmed and added to both the store and the draft reference list.
2. **Citation [12]** (PMID 36413611): Quantitative pooled estimate unverified (PMC9935015 not yet retrieved). The draft has handled this correctly and conservatively. Upgrade to FULL PASS for quantitative citation only after PMC9935015 is retrieved and the pooled OR confirmed.

**Required actions before dissertation use:**
- Confirm PMID for Huang 2020 (REF-040) via `get_article_metadata`.
- Retrieve PMC9935015 to confirm full citation and pooled OR for REF-039 before using quantitative estimates.

---

## 8. Rubric Score

| Criterion | Weight | Assessment | Score |
|---|---|---|---|
| **Accuracy / citations** | 0.40 | Zero fabricated citations. All 50+ quantitative data points match their source exactly. Two administrative notes (PMID pending, full-text pending) do not affect data accuracy. Full marks. | **0.40 / 0.40** |
| **Evidence-language match** | 0.20 | All claims match their GRADE level. Causal language avoided for observational data throughout. One borderline case (Frontera "independent predictor") covered by explicit GRADE annotation. No GRADE mismatches found. Full marks. | **0.20 / 0.20** |
| **Completeness** | 0.15 | All 9 numbered sections present (Introduction, Structural/EP changes, LGE-MRI, Non-PV foci, EAM/Omnipolar, Ablation outcomes, Variable table, Evidence gaps, Conclusion). P-wave section (2.3) present with all three markers (PWD, advanced IAB, PTFV1). EnSite X variable table (Section 7) complete with 20+ variable rows, units, thresholds, and source citations. Appendices A and B present. No section missing. Full marks. | **0.15 / 0.15** |
| **Vietnamese / language quality** | 0.10 | Vietnamese terminology is appropriate with consistent bilingual notation at first use (e.g., "rung nhĩ (atrial fibrillation — AF)"). Technical EP terms correctly rendered in Vietnamese with English parenthetical. GRADE labels written in both languages. Minor: a few sentences are dense but not incorrect. Full marks. | **0.10 / 0.10** |
| **Limitations acknowledged** | 0.10 | Appendix A is comprehensive: search scope limited to reference store; evidence quality (mostly Low/Very Low GRADE); one unverified full-text record (REF-039); direction correction from initial protocol (non-PV foci); missing elderly-specific voltage data; unvalidated omnipolar thresholds; absence of Vietnamese population data. Full marks. | **0.10 / 0.10** |
| **Controversy balance** | 0.05 | CFAE: Nademanee [13] vs STAR AF II [14] — both cited, controversy boxed. DECAAF I vs II [15,16] — both cited, controversy boxed. CABANA vs REHEALTH AF [22,23] — both cited, controversy boxed. Appendix B explicit consensus/controversy section. Full marks. | **0.05 / 0.05** |
| **TOTAL** | **1.00** | | **1.00 / 1.00** |

**Rubric band: EXCEEDED (1.00)**

---

## 9. Audit Report

### Process compliance
| Gate / Process item | Status |
|---|---|
| Phase-0 scope confirmed (language, depth, purpose) | NOT assessed by this QA agent (orchestrator level). Review header states purpose and language. |
| Research Map hard gate cleared before drafting | NOT assessed by this QA agent (orchestrator level). Would need evolution-log entry to confirm. |
| Writer cited ONLY from reference store (no extrapolations) | CONFIRMED — all 29 citations trace to REF-001 through REF-040. |
| No numbers invented (Law 6) | CONFIRMED — 50+ data points verified exact. |
| Preprint honesty check | No preprints cited in this review. N/A. |
| Reference store as single citation source | CONFIRMED. |
| All claims carry specific citations | CONFIRMED — no uncited factual assertions found. The one uncited claim (AI-ECG section) is explicitly labeled "suy luận/định hướng, không phải chứng cứ" per Law 1 self-disclosure. |

### Law compliance summary
| Law | Status |
|---|---|
| Law 1 (No fabricated citations) | COMPLIANT |
| Law 2 (Language matches evidence) | COMPLIANT |
| Law 3 (Evidence hierarchy honored) | COMPLIANT |
| Law 4 (Consensus/controversy separated) | COMPLIANT |
| Law 5 (Limitations stated) | COMPLIANT |
| Law 6 (No invented numbers) | COMPLIANT |

### Scope integrity
- Review scope matches the stated topic (LA electrophysiology in elderly AF patients).
- Variable table section (Section 7) is appropriately framed as proposed, evidence-based, and with explicit "cần xác định" (needs determination) flags where thresholds are not yet established.
- The AI-ECG gap (Section 8, item 3) is correctly labeled as inference/direction rather than evidence, with an explicit Law 1 self-disclosure.

### Defect categories (for lessons-curator)
- **Category 1 — Administrative pending:** PMID not yet confirmed for REF-040 (Huang 2020) despite full-text PDF being available. Lesson: when full text is available, always confirm PMID before closing retrieval.
- **Category 2 — Partial verification:** REF-039 (PMID 36413611) PMC full text available but not retrieved. Writer correctly self-flagged and downgraded. Lesson: if PMC full text is available, retrieve it before the writing phase — do not leave a retrievable record partially verified.
- **Category 3 — Direction correction caught during writing:** Writer correctly identified that non-PV foci direction (higher in young) contradicts initial protocol assumption and corrected per Law 1. This is a positive example of Law 1 compliance during synthesis.
- No instances of fabricated citations, data mismatches, or overclaimed language found.

---

## 10. Summary for Delivery Decision

**DELIVER — with two minor follow-up actions**

The review is of exceptionally high citation quality:
- 0 fabricated citations (Law 1 auto-fail not triggered)
- 50+ quantitative data points verified exact against the reference store
- All six laws complied with
- All 9 sections complete, P-wave section complete, EnSite X variable table complete
- Controversy balance explicit and complete
- Limitations appendix comprehensive

**Two items to resolve before the review enters the dissertation (not before general delivery):**
1. Confirm PMID for Huang 2020 PTFV1 meta-analysis (REF-040) and add to both store and draft reference #11.
2. Retrieve PMC9935015 (REF-039, PMID 36413611) and confirm the pooled OR before upgrading citation [12] from qualitative to quantitative use in the dissertation.

**Rubric score: 1.00 / 1.00 (EXCEEDED)**
