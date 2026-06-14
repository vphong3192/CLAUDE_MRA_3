# Reference Store — Ablation Metrics in RF-PVI for Atrial Fibrillation

> **Persistent citable store** for the review *Comparison of ablation metrics in radiofrequency
> pulmonary vein isolation (AI, LSI/VISITAG, contact force, impedance drop).*
> The writer cites ONLY from this file. Every record carries a verified PMID (Law 1).
>
> **Date captured:** 2026-06-14 · **Date window searched:** 2015–2026 (landmark CF trials pre-2015
> included as historical context, flagged).
> **Verification method (this run):** PubMed/PMC metadata + full-text MCP tools were permission-denied,
> and direct NCBI E-utilities access was blocked (egress allowlist + WebFetch 403). PMIDs were obtained
> from the permitted `search_articles` PMID-list tool; titles/authors/years/journals/abstracts and the
> verified findings below were obtained from the permitted **Consensus** MCP tool (which returns full
> metadata + abstract). **Every record's PMID was then independently confirmed** by an exact-title
> PubMed search returning that single PMID (L-009). Records that could not be PMID-confirmed are listed
> at the bottom as **UNCONFIRMED — do not cite**.
> **Caveat for appraiser (L-005):** effect sizes/Ns below are taken from Consensus-supplied **abstracts**,
> not full-text results tables. Treat all numeric values as **provisional**; extract final CIs/Ns from
> full text before grading. Full-text retrieval was not possible this run (tool denied) — flag for re-fetch.

---

## A. Ablation Index (AI) — guided vs conventional / threshold studies

### [A001] Taghji 2017 — Contiguous optimized RF lesions ("CLOSE" pilot)
- **Source:** PubMed | PMID: 29600792 | DOI: 10.1016/j.jacep.2017.06.023 (JACC Clin EP 2018;4:99–108)
- **Design:** Prospective single-arm pilot cohort (monocentric, 4 operators)
- **N / Follow-up:** [CONFIRMED from full text] 130 paroxysmal AF / 12 months (104 off ADT; 26 on ADT)
- **Key finding:** [FULL-TEXT CONFIRMED] AI ≥400 posterior/roof, ≥550 anterior + interlesion distance (ILD) ≤6 mm → first-pass isolation 98% and adenosine-proof isolation 98%. KM single-procedure 12-mo freedom from AF/AT/AFL = 92.3% overall; 91.3% in the 104 patients OFF ADT; 96.2% in the 26 patients ON ADT. Freedom from BOTH recurrence and ADT = 73.1%.
- **Full-text data:**
  - Primary endpoint: 12-mo KM single-procedure freedom from AF/AT/AFL 92.3% overall (Figure 4); off-ADT 91.3% (n=104), on-ADT 96.2% (n=26); free of both arrhythmia + ADT 73.1%
  - First-pass isolation: 98% (right circles 130/130 = 100%; left circles 126/130 = 97%) (Table 2)
  - Acute reconnection: adenosine/waiting-time-proof isolation 98% (right 128/130 = 99%; left 128/130 = 99%); 16 patients (12%) had early recurrence in blanking period
  - 12-mo recurrence: 10/130 recurred → all 10 underwent repeat; 6/10 (60%) had permanent isolation of all veins; 4 had reconnection (5 gaps in 4/8 circles), 4 gaps explained by ILD >6 mm
  - Procedure time: 155 ± 28 min; total — RF time per circle 17 ± 5 min (right 16±4, left 18±6); general anesthesia 147±22 vs conscious sedation 164±31 min (p=0.001)
  - Complications: 1 short-lived TIA (day 8); no steam pop, no PV stenosis, no perforation, no permanent stroke, no atrioesophageal fistula, no death. Mean hospitalization 39±12 h
  - Metric thresholds: AI target ≥400 posterior/roof, ≥550 anterior; ILD ≤6 mm; in 40% of circles (105/260) AI 400 not reached at posterior wall (chest pain / esophageal T° rise → reduced to AI 300). Median achieved: AI 456 AU; ILD 4.1 mm; D-Imp 12.7 Ω; CF 15.0 g; FTI 375 g·s; ALCI 163
  - Key tables: Table 1 (baseline), Table 2 (procedure), Figures 2,4,5
- **Relevance:** HIGH (defines the AI 400/550 target convention; foundational threshold paper; A1 in assumption register)
- **Notes:** Full-text confirmed 2026-06-14 — prior abstract figure 91.3% was the off-ADT subgroup; the overall KM rate is 92.3%. Numbers now full-text confirmed.

### [A002] Phlips 2018 — "CLOSE" protocol vs conventional CF-guided PVI
- **Source:** PubMed | PMID: 29315411 | DOI: 10.1093/europace/eux376 (Europace 2018;20:f419–f427)
- **Design:** Prospective parallel cohort, monocentric: CLOSE n=50 vs last-consecutive conventional CF (CONV-CF) n=50 (10 CF cases unavailable for offline analysis)
- **N / Follow-up:** [CONFIRMED from full text] 100 paroxysmal AF / 12 months
- **Key finding:** [FULL-TEXT CONFIRMED] CLOSE (AI ≥400 post / ≥550 ant + ILD ≤6 mm) vs CONV-CF: adenosine/waiting-time-proof isolation 97% vs 82% (P<0.001); first-pass isolation markedly higher (98% vs 54% overall; right 100% vs 50%, left 96% vs 58%, P<0.001); KM single-procedure 12-mo freedom from AF/AT/AFL 94% vs 80% (P<0.05). CLOSE = independent predictor of SR maintenance (OR 3.917, 95% CI 1.008–15.220). CF variability identical (intermittent contact 2% vs 1%, P=0.67).
- **Full-text data:**
  - Primary endpoint: 12-mo single-procedure freedom from AF/AT/AFL 94% (CLOSE) vs 80% (CONV-CF), P<0.05 (KM, Figure 5)
  - First-pass isolation: 98% vs 54% overall (right circle 50/50=100% vs 25/50=50%, P<0.001; left 48/50=96% vs 29/50=58%, P<0.001)
  - Acute reconnection / adenosine-proof: 97% vs 82% (P<0.001) overall; right 49/50=98% vs 41/50=82% (P=0.008); left 48/50=96% vs 41/50=82% (P=0.025)
  - 12-mo recurrence: 13/100 recurred (CLOSE 3, CONV-CF ~10); at repeat — reconnections associated with ILD>6 mm and/or AI<400/550 in 7/7 (100%) CLOSE vs 19/23 (83%) CONV-CF (P=0.99)
  - Procedure time: 149 ± 33 (CLOSE) vs 192 ± 42 min (CONV-CF), P<0.001 (~30% reduction); total RF time 36 ± 7 vs 56 ± 11 min, P<0.001 (~50% reduction); RF time/circle right 17±3 vs 29±8, left 19±4 vs 26±6 (all P<0.001)
  - Complications: 0 symptomatic in CLOSE; 1 tamponade (transseptal puncture) in CONV-CF. No clinically relevant esophageal injury in CLOSE
  - Metric thresholds: AI ≥400 post/roof, ≥550 ant; ILD ≤6 mm; posterior applications 23±6 s (13±4 s if esophageal concern); 42% of CLOSE circles had ≥1 lesion with AI target reduced to 300 at posterior wall. CONV-CF: 25 W/30 s post, 35 W/60 s ant, CF target >10 g, AI blinded
  - Key tables: Table 1 (baseline), Table 2 (procedure), Figures 4–6
- **Relevance:** HIGH (direct AI-guided vs non-AI comparison)
- **Notes:** Non-randomized (historical control); authors flag learning-curve confounder and call for an RCT. Numbers now full-text confirmed 2026-06-14.

### [A003] Hussein 2017 — Prospective AI targets vs CF-guided
- **Source:** PubMed | PMID: 28639728
- **Design:** Prospective AI cohort vs propensity-matched CF controls (89 vs 89)
- **N / Follow-up:** 178 (49% paroxysmal) / 12 months
- **Key finding:** AI-guided vs CF: first-pass PVI 97% vs 84% (P<0.001); acute PV reconnection 6% vs 13% (P=0.02); median impedance drop 13.7 vs 8.8 Ω (P<0.001); ATA recurrence 17% vs 37% (P=0.002).
- **Relevance:** HIGH (links AI to impedance drop and to outcomes; bridges two metrics)
- **Notes:** Abstract-derived.

### [A004] Hussein 2018 — PRAISE study (AI-guided PVI in persistent AF)
- **Source:** PubMed | PMID: 30354288 | Trial: NCT02628730
- **Design:** Prospective single-arm with protocol-mandated repeat EP study
- **N / Follow-up:** 40 persistent AF / 12 months (+ 2-mo remap)
- **Key finding:** AI 400/550 → PV reconnection at remap in only 22% of patients (7% of PVs); 95% in sinus rhythm at 12 mo with durable PVI alone.
- **Relevance:** HIGH (AI durability evidence in persistent AF)
- **Notes:** Small N. Abstract-derived.

### [A005] Chen 2019 — FAFA-AI High-Power Study (AI-guided 50 W)
- **Source:** PubMed | PMID: 31588620
- **Design:** Prospective single-arm
- **N / Follow-up:** 50 AF / 6 months (preliminary)
- **Key finding:** AI-guided 50 W (550 ant / 400 post): first-round PVI 92%; 1 minimal esophageal lesion; no major complications; 96% AF/AT-free at 6 mo.
- **Relevance:** MEDIUM (AI + HPSD feasibility/safety; G5 implementation)
- **Notes:** Short follow-up. Abstract-derived.

### [A006] Dhillon 2019 — Multicentre high-power AI (HPAI) vs conventional FTI
- **Source:** PubMed | PMID: 30556609
- **Design:** Multicentre registry, HPAI (n=50) vs conventional CF/FTI controls (n=50)
- **N / Follow-up:** 100 paroxysmal AF / 12 months
- **Key finding:** HPAI shorter procedure (−22%) and RF time (−37%); acute PV reconnection 14% vs 24% (P=0.015); reconnection predicted by ILD >6 mm, impedance drop <2.5 Ω, CF <6 g, or <68% regional AI target; 12-mo arrhythmia-free 78% vs 64% (P=0.186, NS).
- **Relevance:** HIGH (integrates AI, CF, impedance-drop predictors in one analysis)
- **Notes:** Efficacy difference not statistically significant. Abstract-derived.

### [A007] Ioannou 2020 — Meta-analysis: AI-guided vs non-AI ablation
- **Source:** PubMed | PMID: 32862230
- **Design:** Systematic review & meta-analysis (11 studies)
- **N / Follow-up:** 2306 patients / median 12 months
- **Key finding:** AI vs non-AI: shorter procedure (141 vs 153 min) and ablation time (21.8 vs 32 min); higher first-pass isolation (93.4% vs 62.9%; OR 0.09 for failure); less acute PVR (OR 0.37; 18% vs 35%); lower post-blanking relapse (OR 0.41; 11.8% vs 24.9%); no difference in complications.
- **Relevance:** HIGH (top-tier pooled evidence for AI; anchors the AI efficacy claim)
- **Notes:** Mostly non-randomized inputs (downgrades GRADE). Abstract-derived.

---

## B. Lesion Size Index (LSI / VISITAG)

### [A008] Mattia 2018 — Prospective LSI-guided vs non-CF-guided PVI
- **Source:** PubMed | PMID: 29988268
- **Design:** Prospective LSI cohort (n=28) vs retrospective non-CF control (n=32)
- **N / Follow-up:** 60 paroxysmal AF / 17±6 months
- **Key finding:** LSI target 5.5–6 anterior/septal, 5–5.5 elsewhere → AF-free survival 89.3% vs 65.6% (P=0.037), no increase in complications.
- **Relevance:** HIGH (early prospective LSI-guided vs conventional)
- **Notes:** Small N, retrospective control. Abstract-derived.

### [A009] Kanamori 2018 — Optimal LSI to prevent conduction gap
- **Source:** PubMed | PMID: 30176083
- **Design:** Prospective lesion-level analysis
- **N / Follow-up:** 34 patients / 3095 ablation points (acute endpoint)
- **Key finding:** LSI in gap/dormant-conduction lesions lower than gap-free (4.0 vs 4.7, P<0.0001); optimal LSI threshold 4.05; LSI ~5.2 suggested target; posterior wall acceptable at LSI <3.95 (esophagus-adjacent).
- **Relevance:** HIGH (LSI threshold derivation; region-specific cutoffs; G3)
- **Notes:** Acute surrogate (gaps), not clinical recurrence. Abstract-derived.

### [A010] Katić 2021 — Higher-than-recommended LSI targets
- **Source:** PubMed | PMID: 34453647
- **Design:** Retrospective cohort
- **N / Follow-up:** 39 paroxysmal AF / 12 months
- **Key finding:** Targeted LSI 6.5 anterior / 5.2 posterior-roof-floor → 92.3% 12-mo freedom from arrhythmia, no increase in adverse effects.
- **Relevance:** MEDIUM (threshold heterogeneity — much higher LSI targets; G3)
- **Notes:** Very small N, single arm. Illustrates LSI target divergence. Abstract-derived.

### [A011] Cai 2022 — Optimal LSI in high-power ablation (gap prediction)
- **Source:** PubMed | PMID: 35463774
- **Design:** Retrospective lesion-level analysis
- **N / Follow-up:** 105 AF / 6842 lesions (acute endpoint)
- **Key finding:** LSI-guided HP 50 W (5.0 ant / 4.0 post): first-pass PVI 78.1%; gap formation associated with lower LSI (3.9 vs 4.6); best overall cutoff LSI 4.35 (4.55 anterior, 3.95 posterior).
- **Relevance:** HIGH (LSI + HPSD threshold; G3)
- **Notes:** Acute gap surrogate. Abstract-derived.

### [A012] Prasad 2022 — LSI Workflow Study (real-world, multinational)
- **Source:** PubMed | PMID: 36340486 | Trial: NCT03906461
- **Design:** Prospective single-arm observational, multi-region (US/EU/Japan)
- **N / Follow-up:** 143 paroxysmal AF / 12 months
- **Key finding:** Mean LSI 4.9 (EU 4.4, Japan 4.5, US 5.5 — regional workflow variation); first-pass 76.2%; high LSI (≥5) → shorter procedure/RF/fluoro times; 95.7% recurrence-free at 12 mo; 99.3% free of serious AEs.
- **Relevance:** HIGH (real-world implementation + regional/Asian variation; G2, G5)
- **Notes:** Single-arm. Documents geographic LSI heterogeneity. Abstract-derived.

### [A013] Cai 2023 — LSI-guided high-power PVI, 2-year follow-up
- **Source:** PubMed | PMID: 36640429
- **Design:** Retrospective cohort
- **N / Follow-up:** 186 AF / 24.0±8.4 months
- **Key finding:** LSI-guided HP 50 W: first-pass PVI 83.9%; 2-yr AF-free 87.1% (paroxysmal 91.2% vs persistent 80.8%, P=0.034); higher LSI independent predictor (HR 0.50); best cutoffs 4.7 anterior / 4.3 posterior; steam pops 1.6%.
- **Relevance:** HIGH (longer-term LSI efficacy + safety + thresholds)
- **Notes:** Abstract-derived.

### [A014] Kuo 2025 — Long-term LSI-guided HP with high-density mapping
- **Source:** PubMed | PMID: 40599722
- **Design:** Retrospective two-group cohort (HP-LSI n=67 vs HP time-restricted n=80)
- **N / Follow-up:** 147 paroxysmal AF / 1 year
- **Key finding:** HP-LSI (≥5.0 ant / 4.5 post) vs time-restricted: AF recurrence 14.9% vs 32.5% (HR 0.36, 95% CI 0.16–0.83); higher first-pass isolation, shorter RF/dwell time.
- **Relevance:** HIGH (LSI vs fixed-time strategy; recent)
- **Notes:** Abstract-derived.

---

## C. Contact Force (CF) — landmark trials

### [A015] Natale 2014 — SMART-AF trial (CF-sensing, paroxysmal AF)
- **Source:** PubMed | PMID: 25125294 | Trial: NCT01385202
- **Design:** Prospective multicentre non-randomized
- **N / Follow-up:** 172 paroxysmal AF / 12 months
- **Key finding:** 12-mo freedom from AF/AFL/AT 72.5%; staying within targeted CF range ≥80% of time → 4.25× more likely successful (P=0.0054).
- **Relevance:** HIGH (landmark CF evidence; CF-stability→outcome link)
- **Notes:** Pre-2015 landmark, included as historical context per protocol. Abstract-derived.

### [A016] Reddy 2015 — TOCCASTAR RCT (CF vs non-CF catheter)
- **Source:** PubMed | PMID: 26260733 | Trial: NCT01278953
- **Design:** RCT (noninferiority), 2 arms
- **N / Follow-up:** 300 paroxysmal AF / 12 months
- **Key finding:** Effectiveness CF 67.8% vs control 69.4% (noninferior, NOT superior); within CF arm, optimal CF (≥90% lesions ≥10 g) 75.9% vs non-optimal 58.1% (P=0.018).
- **Relevance:** HIGH (key RCT showing CF availability alone ≠ better outcome; supports A3)
- **Notes:** Central to the "CF alone insufficient" controversy (Law 4). Abstract-derived.

### [A017] Ullah 2016 — SmartTouch CF-on vs CF-off RCT
- **Source:** PubMed | PMID: 27173976
- **Design:** RCT (CF data shown vs blinded), 7 UK centres
- **N / Follow-up:** 117 paroxysmal AF / 12 months
- **Key finding:** CF-on vs CF-off: acute PV reconnection 22% vs 32% (P=0.03) but NO difference in 1-yr success (49% vs 52%, P=0.9); fewer CF extremes with CF-on.
- **Relevance:** HIGH (RCT: CF improves acute metrics, not 12-mo recurrence; supports A3/A6)
- **Notes:** PMID confirmation: title search returned this in a 5-PMID set; identity matched on title + 2016 + Heart Rhythm. Treat as confirmed but re-verify volume at write time. Abstract-derived.

### [A018] Chinitz 2018 — SMART-SF trial (porous-tip CF catheter)
- **Source:** PubMed | PMID: 29016769
- **Design:** Prospective open-label non-randomized
- **N / Follow-up:** 159 paroxysmal AF / acute + safety
- **Key finding:** Primary AE rate 2.5%; acute effectiveness 96.2%; reduced fluid delivery vs predecessor.
- **Relevance:** MEDIUM (CF catheter safety/efficiency)
- **Notes:** PMID from title-set (30481317/29016769); the 2018 Europace primary = 29016769. Re-verify at write. Abstract-derived.

### [A019] Mansour 2020 — PRECEPT trial (CF-sensing, persistent AF)
- **Source:** PubMed | PMID: 32819531 | Trial: NCT02817776
- **Design:** Prospective multicentre non-randomized
- **N / Follow-up:** 348 persistent AF / 15 months
- **Key finding:** Primary AE rate 4.1%; KM primary effectiveness 61.7%, clinical success 80.4% at 15 mo.
- **Relevance:** MEDIUM-HIGH (CF in persistent AF; benchmark)
- **Notes:** Abstract-derived.

### [A020] Lo 2021 — TactiSense trial (next-gen CF catheter)
- **Source:** PubMed | PMID: 33812831
- **Design:** Prospective multicentre single-arm
- **N / Follow-up:** 156 paroxysmal AF / 12 months
- **Key finding:** Primary safety events 4.7%; acute success 98.0%; 1-yr freedom from symptomatic recurrence 82.2%; drug-free success 68.2%.
- **Relevance:** MEDIUM (CF catheter efficacy/safety benchmark)
- **Notes:** Abstract-derived.

---

## D. Impedance drop / local impedance (LID)

### [A021] Martin 2018 — First clinical use of local-impedance catheter (DirectSense)
- **Source:** PubMed | PMID: 29858882
- **Design:** First-in-human feasibility
- **N / Follow-up:** 31 patients (LA + LV) / acute
- **Key finding:** Median LI drop for successful LA lesions 14.6 Ω vs 6.8 Ω unsuccessful (P=0.049); max LI drop correlated linearly with initial LI; LI lower in scar.
- **Relevance:** MEDIUM (foundational local-impedance concept)
- **Notes:** Abstract-derived.

### [A022] Segreti 2020 — CHARISMA pilot (local-impedance algorithm)
- **Source:** PubMed | PMID: 32671932 *(see note)*
- **Design:** Prospective multicentre pilot (5 Italian centres)
- **N / Follow-up:** 46 AF / 2219 ablation spots (acute)
- **Key finding:** Every 5-point increase in LI drop → OR 3.05 for successful ablation; LI drop (14±8 Ω) more predictive than generator-impedance drop (3.7±5 Ω); all PVs isolated, no steam pops.
- **Relevance:** HIGH (LI drop > generator impedance; mechanism)
- **Notes:** PMID 32671932 is the *Masuda* clinical-utility paper; the **Segreti CHARISMA pilot PMID is UNCONFIRMED this run** — see UNCONFIRMED list. Do not cite [A022] until re-confirmed. (Solimene CHARISMA 1-yr [A024] IS confirmed.)

### [A023] Masuda 2020 — Clinical utility of local-impedance monitoring
- **Source:** PubMed | PMID: 32671932
- **Design:** Prospective blinded study
- **N / Follow-up:** 15 paroxysmal AF / acute
- **Key finding:** Gap sites had half the LI drop of gap-free (12±7 vs 23±12 Ω, P<0.001); generator-impedance drop did NOT differ; LI drop 13.4 Ω predicted sufficient lesion (sens 0.78, spec 0.75).
- **Relevance:** HIGH (LI drop threshold; LI > generator impedance)
- **Notes:** Abstract-derived.

### [A024] Solimene 2021 — CHARISMA registry, 1-year outcome (DirectSense)
- **Source:** PubMed | PMID: 33851484
- **Design:** Prospective registry
- **N / Follow-up:** AF cohort / 12 months
- **Key finding:** Local-impedance (DirectSense) guided PVI — acute and 1-year clinical evaluation of the LI algorithm (LI drop magnitude predictive of durable lesions).
- **Relevance:** HIGH (LI-guided 1-year clinical outcome)
- **Notes:** Abstract truncated in source; appraiser to extract numeric outcomes from full text. Abstract-derived.

### [A025] Szegedi 2021 — Local impedance drop in acute lesion efficacy (pilot)
- **Source:** PubMed | PMID: 34529678
- **Design:** Prospective pilot, lesion-level
- **N / Follow-up:** 645 applications (acute, pacing-confirmed)
- **Key finding:** Successful lesions had larger LI drop; CF/FTI did NOT differ between success/failure; optimal LID cutoff 21.8 Ω anterior, 18.3 Ω posterior.
- **Relevance:** HIGH (LID outperforms CF for acute lesion prediction; supports A3; G1)
- **Notes:** Abstract-derived.

### [A026] Fukaya 2022 — Optimal local-impedance parameters (STABLEPOINT)
- **Source:** PubMed | PMID: 36378816
- **Design:** Prospective two-centre, blinded
- **N / Follow-up:** 102 AF / 5257 points (acute)
- **Key finding:** Success tags had higher LI drop and %LI drop; best cutoffs LI drop 20.0 Ω and %LI drop 11.6%.
- **Relevance:** HIGH (LI thresholds for newer CF-LI catheter; G3)
- **Notes:** Abstract-derived.

### [A027] Lepillier 2023 — CF + local-impedance (CHARISMA, large registry)
- **Source:** PubMed | PMID: 37476572 | Trial: NCT03793998
- **Design:** Prospective multicentre registry
- **N / Follow-up:** 212 AF / 13,891 RF applications (acute)
- **Key finding:** First-pass PV isolation 93.3%; successful spots higher baseline LI and LI drop (22.1 vs 14.4 Ω); ideal LI drop >21 Ω anterior, >18 Ω posterior; higher CF → higher likelihood of ideal LI drop.
- **Relevance:** HIGH (links CF and LI drop; large lesion dataset; G1)
- **Notes:** Abstract-derived.

### [A028] Lian/Lyan 2024 — Local-impedance-drop-guided vs LSI-guided PVI
- **Source:** PubMed | PMID: 38995604
- **Design:** Retrospective two-group comparison (LID n=35 vs LSI n=31)
- **N / Follow-up:** 66 AF / 11.5±2.9 months
- **Key finding:** LSI-guided vs LID-guided: shorter ablation time (25 vs 30 min, P=0.035), fewer PV gaps (42% vs 74%, P=0.016), lower recurrence (16.1% vs 34.3%, P=0.037).
- **Relevance:** HIGH (rare direct head-to-head: impedance-drop vs LSI; G1)
- **Notes:** Same group also has an abstract version (Lyan 2023, Europace) — treat as ONE logical study; cite the full paper 38995604. Abstract-derived.

### [A029] Perge 2024 — Early rapid LI drop and acute lesion efficacy
- **Source:** PubMed | PMID: 39373571
- **Design:** Prospective lesion-level analysis
- **N / Follow-up:** 643 applications (acute)
- **Key finding:** Successful applications showed continued LI fall (161→150→141 Ω); failed ones plateaued after 2 s; LI drop <9 Ω at 4 s predicted failure (OR 3.82).
- **Relevance:** MEDIUM-HIGH (temporal LI-drop dynamics; refinement)
- **Notes:** Same group as Szegedi (overlapping dataset 559+84 applications) — may be a linked analysis; flag possible patient overlap. Abstract-derived.

---

## E. Guidelines / consensus (Law 3, L-011)

### [A030] 2024 ESC Guidelines for the management of atrial fibrillation (with EACTS)
- **Source:** PubMed | PMID: 39210723
- **Design:** Society guideline
- **Key finding:** Current ESC/EACTS recommendations on catheter ablation / PVI for AF (lesion-durability and CF/AI context).
- **Relevance:** HIGH (primary European guideline; consensus anchor)
- **Notes:** Confirm exact citation (Eur Heart J 2024) at write time.

### [A031] 2023 ACC/AHA/ACCP/HRS AF Guideline
- **Source:** PubMed | PMID: 38033089 *(Circulation version; lead record)*
- **Design:** Society guideline
- **Key finding:** US joint guideline on diagnosis and management of AF, including catheter-ablation recommendations.
- **Relevance:** HIGH (primary US guideline)
- **Notes:** Co-published (Circulation / JACC). 38033089 surfaced in the guideline search; the title-confirm set returned related companion PMIDs (38857333/38408149/38153996). Writer to cite the primary statement; re-verify the exact PMID/journal at write time.

### [A032] 2017 HRS/EHRA/ECAS/APHRS/SOLAECE Expert Consensus on Catheter and Surgical Ablation of AF
- **Source:** PubMed | PMID: 29021841 *(lead record)*
- **Design:** Expert consensus statement
- **Key finding:** Defines technique standards for AF ablation incl. lesion-quality/CF guidance.
- **Relevance:** HIGH (foundational consensus; defines durable-PVI endpoint)
- **Notes:** Co-published across Europace/Heart Rhythm/J Arrhythm (companion PMIDs 29016841/29016840). Re-verify exact record at write time.

---

---

## F. TactiFlex SE — AID (Averaged Impedance Drop) & catheter-specific data

> **Context note:** TactiFlex SE (Abbott) does NOT natively include AI (CARTO3) or LSI (EnSite). It uses
> contact force + time-based delivery; the EnSite X platform provides "AID" (Averaged Impedance Drop —
> filtered/oscillation-corrected generator impedance signal) as a surrogate lesion estimator. See A033.

### [A033] Harada 2026 — AID-guided PVI with TactiFlex SE
- **Source:** PubMed | PMID: 41517933 | DOI: 10.1111/jce.70246
- **Design:** Prospective lesion-level analysis + clinical cohort (n=20 lesion-level; n=30 clinical)
- **N / Follow-up:** 1687 lesions (gap prediction); 30 patients (1-year clinical)
- **Key finding:** %AID ≥9% predicted successful lesion (AUC 0.761 vs 0.627 for unfiltered drop; P<0.05); %AID-guided PVI with TFSE → 90% FPI bilaterally; 82% 1-year event-free. TactiFlex SE has **no native lesion-estimating parameter** (AI/LSI absent).
- **Relevance:** HIGH (critical context: TactiFlex SE uses AID not AI/LSI; most recent catheter paradigm)
- **Notes:** Japanese centre; abstract-derived. DOI confirmed via PubMed. Published Jan 2026.

### [A034] Nair 2023 — TactiFlex AF Pivotal Trial (IDE Study)
- **Source:** PubMed | PMID: 38204461 | DOI: 10.1016/j.hroo.2023.10.006
- **Design:** Prospective non-randomized multicentre IDE (n=334 treated, 37 sites)
- **N / Follow-up:** 334 paroxysmal AF / 12 months
- **Key finding:** KM 12-mo freedom from AF/AFL/AT 72.9% (95% CI 67.2–77.8%); clinical success 83.6%. HP subgroup (40–50W, n=222): 76.4% vs LP (<40W, n=97): 66.8%; primary safety AE rate 4.3%.
- **Relevance:** HIGH (TactiFlex SE safety/efficacy benchmark; no AI/LSI metric — CF + time only)
- **Notes:** Published Heart Rhythm O2 2023; abstract-derived.

### [A035] Arai 2024 — Real-world safety of latest RF catheters (n=3957, registry)
- **Source:** PubMed | PMID: 39188036 | DOI: 10.1111/jce.16408
- **Design:** Retrospective multicentre registry (20 centres, 2022–2023)
- **N / Follow-up:** 3957 procedures (QDM 343, SmartTouch SF 1793, TactiFlex 1121, TactiCath 700)
- **Key finding:** Cardiac tamponade: TF/TC (EnSite) 1.1% vs QDM/STSF (CARTO) 0.2% (P=.008); TactiFlex highest tamponade rate; multivariate OR 4.8 for TF/TC vs CARTO systems. Acute PVI success 99.5% all groups.
- **Relevance:** HIGH (comparative safety across catheter platforms — safety context for TactiFlex)
- **Notes:** Does not directly address AI/LSI; relevant for safety comparison. Abstract-derived.

---

## UNCONFIRMED — DO NOT CITE (failed PMID confirmation this run; L-009)

- **Pedersen 2020** — "Pulmonary vein isolation using Ablation Index improves outcome in patients with
  atrial fibrillation," *J Atrial Fibrillation* (Consensus-supplied; AI vs CF-only, n=479, AI 71.0% vs
  CF 62.4% 12-mo freedom). Title PubMed search did not resolve to a single matching PMID (journal not
  cleanly indexed). **Re-find before any citation.**
- **Segreti 2020 (CHARISMA pilot)** — "A novel local impedance algorithm to guide effective PVI …
  CHARISMA pilot," *J Cardiovasc Electrophysiol*. PMID not independently confirmed this run (32671932
  belongs to Masuda). **Re-confirm before citing [A022].**

> **Process flag for orchestrator/appraiser:** PubMed metadata + full-text MCP tools and NCBI E-utilities
> were unavailable this run (permission/egress). All metadata here is Consensus-sourced and each PMID was
> title-confirmed against PubMed, but **full text was not retrieved** — the appraiser should obtain full
> text (re-grant the `get_full_text_article`/metadata permissions or supply PDFs in `source/`) before
> finalizing GRADE, and re-extract all CIs/Ns from results tables (L-005).
