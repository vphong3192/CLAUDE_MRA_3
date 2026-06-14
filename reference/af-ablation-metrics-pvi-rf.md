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
> **Caveat for appraiser (L-005):** effect sizes/Ns are taken from Consensus-supplied **abstracts**
> UNLESS a record is marked "[FULL-TEXT CONFIRMED]". Treat any remaining abstract-derived value as
> **provisional**; extract final CIs/Ns from full text before grading.
>
> **Full-text upgrade — 2026-06-14 (L-005 applied):** Ten records were upgraded from user-supplied
> full-text HTML in `source/af-ablation-metrics/` (PDF→HTML conversions). Numbers below now taken from
> **results tables/text, not abstracts**, for: **[A001] Taghji, [A002] Phlips, [A007] Ioannou,
> [A009] Kanamori, [A016] Reddy/TOCCASTAR, [A017] Ullah, [A024] Solimene/CHARISMA, [A027] Lepillier,
> [A028] Lian/Lyan, [A033] Harada.** Each carries a "Full-text data" block + provenance line. Records
> NOT in that list (A003–A006, A008, A010–A015, A018–A023, A025–A026, A029, A030–A032, A034–A035)
> remain **abstract-derived — still provisional**, flag for full-text re-fetch before grading.

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
- **Notes:** Full-text re-verified against `source/af-ablation-metrics/29600792` HTML 2026-06-14 — all figures confirmed verbatim: overall KM 92.3%, off-ADT 91.3% (n=104), on-ADT 96.2% (n=26), both-free 73.1%; first-pass 98%; Table 2 procedure numbers (155±28 min; right RF 16±4, left 18±6 min; first-pass right 130/130=100%, left 126/130=97%; adeno-proof 128/130=99% each side). Median achieved values from text (AI 456, ILD 4.1 mm, D-Imp 12.7 Ω, CF 15.0 g, FTI 375 g·s, ALCI 163). 105/260 circles (40%) did not reach posterior AI 400 (chest pain/esophageal T° rise). Now full-text confirmed.

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
- **Notes:** Non-randomized (historical control); authors flag learning-curve confounder and call for an RCT. Full-text re-verified against `source/af-ablation-metrics/29315411` HTML 2026-06-14 — Table 2 confirms procedure time 192±42 (CONV-CF) vs 149±33 (CLOSE) min P<0.001; total RF time 56±11 vs 36±7 min P<0.001; RF/circle right 29±8 vs 17±3, left 26±6 vs 19±4 (all P<0.001); first-pass right 25/50=50% vs 50/50=100%, left 29/50=58% vs 48/50=96% (P<0.001); waiting/adeno-proof right 41/50=82% vs 49/50=98% (P=0.008), left 41/50=82% vs 48/50=96% (P=0.025); overall adeno-proof 82% vs 97% (P<0.001); 12-mo KM 80% vs 94% (P<0.05); CLOSE = independent predictor SR (OR 3.917, 95% CI 1.008–15.220); 1 tamponade (transseptal) in CONV-CF, 0 symptomatic in CLOSE; intermittent contact 1% vs 2% P=0.67. Now full-text confirmed.

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
- **Source:** PubMed | PMID: 32862230 | DOI: 10.1093/europace/euaa224 (Europace 2020)
- **Design:** Systematic review & meta-analysis (11 studies; PubMed/EMBASE/Cochrane/ESC to 1 July 2019; random-effects Mantel-Haenszel; Newcastle-Ottawa quality)
- **N / Follow-up:** [CONFIRMED from full text] 2306 patients (AI 1046 [45.4%] vs non-AI/control 1260 [54.5%]) / median 12 mo (IQR 12.0–16.5; max 24). Type known for 2096: 1215 (58.0%) paroxysmal. **No RCTs — 4 retrospective + 7 prospective cohorts.**
- **Key finding:** [FULL-TEXT CONFIRMED] AI vs non-AI: shorter procedural time 141.0 vs 152.8 min (P=0.01; I²=90%), ablation time 21.8 vs 32.0 min (P<0.00001; I²=0%), fluoroscopy 10.2 vs 12.0 min (P=0.009; I²=75%); higher first-pass PVI 93.4% vs 62.9% (OR 0.09 for *non-event/failure*, 95% CI 0.04–0.21; P<0.001; I²=58%); less acute PVR 18.0% vs 35.0% (OR 0.37, 95% CI 0.18–0.75; P=0.006; I²=0%); lower post-blanking relapse 11.8% vs 24.9% (OR 0.41, 95% CI 0.25–0.66; P=0.0003; I²=35%; NNT=7.6); cardiac tamponade 1.6% vs 2.4% (OR 0.69, 95% CI 0.30–1.60; P=0.39; I²=0%) — NS; no atrio-oesophageal fistulas/strokes/deaths in either arm.
- **Full-text data:**
  - Primary endpoint (AT/AF relapse post-blanking, 6 studies): OR 0.41 (95% CI 0.25–0.66), 11.8% vs 24.9%, P=0.0003, I²=35%, NNT 7.6
  - First-pass isolation: OR 0.09 (95% CI 0.04–0.21) for failure → 93.4% vs 62.9%, P<0.001, I²=58% (Figure 3; Hussein, Phlips, Dhillon)
  - Acute PVR: OR 0.37 (95% CI 0.18–0.75), 18.0% vs 35.0%, P=0.006, I²=0%
  - Procedure time: 141.0 vs 152.8 min (MD −11.81, 95% CI −20.89 to −2.74, P=0.01, I²=90%, funnel-plot publication-bias signal); ablation time 21.8 vs 32.0 min (P<0.00001, I²=0%); fluoroscopy 10.2 vs 12.0 min (P=0.009)
  - Complications: tamponade AI 7 events vs non-AI 17 → 1.6% vs 2.4% (OR 0.69, P=0.39); all pericardial complications 1.5% vs 2.5% (P=0.28); 0 fistula/stroke/death
  - Metric thresholds (pooled settings, Table 2): most common energy 35 W anterior/roof, 30 W posterior/inferior; commonest AI target 500–550 anterior, 400–450 roof/posterior/inferior; max ILD ≤6 mm (6/8 studies); Phlips up-to-50 W AI 550 ant/400 post shown safe
  - Key tables: Tables 1–4, Figures 1–4 (forest/funnel plots)
- **Relevance:** HIGH (top-tier pooled evidence for AI; anchors the AI efficacy claim)
- **Notes:** Mostly non-randomized inputs (downgrades GRADE — authors: "low to moderate quality"). Tamponade rate is 2.4% in results text (abstract earlier cited ~2.5%) — use full-text 2.4%. Now full-text confirmed 2026-06-14 (`source/af-ablation-metrics/32862230`).

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
- **Source:** PubMed | PMID: 30176083 | DOI: 10.1111/jce.13727 (J Cardiovasc Electrophysiol; Kanamori/Kato et al.)
- **Design:** Prospective single-centre lesion-level analysis (TactiCath Quartz, EnSite Precision; LSI blinded to operator, FTI shown)
- **N / Follow-up:** [CONFIRMED from full text] 34 patients (18 paroxysmal [52.9%] + 16 persistent [47.1%]) / 3095 ablation points with valid LSI (avg 91.0±14.6/pt); acute endpoint (gaps/dormant conduction). Mean op time 112.8±33.0 min.
- **Key finding:** [FULL-TEXT CONFIRMED] LSI in gap/DC lesions significantly lower than gap-free (4.0±0.6 vs 4.7±0.9, P<0.0001; FTI 140.5±54.5 vs 232.4±121.4 g·s, P<0.0001). ROC optimal LSI threshold 4.05 (sens 63.4%, spec 76.3%); LSI <5.25 highly sensitive for gap/DC (sens 97.6%, spec 25.7%) → ≈5.2 proposed effective target. Posterior wall (37% thinner: 2.3±0.4 vs 3.6±1.3 mm, P<0.0001) acceptable at LSI <3.95 (sens 92.3%, spec 65.6%). 41 gaps, 0 dormant conduction observed.
- **Full-text data:**
  - Primary (gap prediction): LSI gap/DC 4.0±0.6 vs no-gap 4.7±0.9 (P<0.0001), Table 2; AUC LSI 0.724 (95% CI 0.659–0.790) vs FTI 0.774 (0.730–0.819), NS P=0.21
  - First-pass isolation: not reported (anatomical PVI, all 34 isolated)
  - Acute reconnection / dormant conduction: 41 gaps / 0 DC across 3095 points; gap-lesion max CF 29.8±12.3 vs 35.8±16.8 g (P=0.023), avg CF 13.0±4.9 vs 16.1±7.1 g (P=0.005), RF duration 11.3±4.6 vs 15.4±9.2 s (P=0.005); power not different (28.1±3.6 vs 28.2±3.0, P=0.818)
  - 12-mo recurrence: NOT assessed (acute surrogate study only)
  - Procedure time: mean operation (puncture→sheath removal) 112.8±33.0 min
  - Complications: none — no audible pop, perforation, tamponade, atrio-esophageal fistula, phrenic nerve injury, or stroke
  - Metric thresholds: optimal LSI 4.05 (sens 63.4/spec 76.3); LSI<5.25 sens 97.6/spec 25.7 → ~5.2 target; posterior LSI<3.95 sens 92.3/spec 65.6; AF-rhythm cutoff 4.05, SR cutoff 4.15. Power 25 W posterior, 35 W left lateral ridge, 30 W elsewhere; target CF 10–30 g; ILD 3–4 mm; FTI ≥200 g·s generally targeted
  - Key tables: Table 1 (baseline), Table 2 (CF/FTI/LSI by gap status), Figures 3–6 (ROC)
- **Relevance:** HIGH (LSI threshold derivation; region-specific cutoffs; G3)
- **Notes:** Acute surrogate (gaps/DC), not clinical recurrence. Mixed paroxysmal + persistent (prior record omitted the 47% persistent share — now corrected). LSI was BLINDED to operators (authors flag as bias limiting LSI-vs-FTI comparison). High-sensitivity threshold is 5.25 (not 5.25 vs 5.2 — 5.2 is the rounded "suitable target"). Now full-text confirmed 2026-06-14 (`source/af-ablation-metrics/30176083`).

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
- **Source:** PubMed | PMID: 26260733 | DOI: 10.1161/CIRCULATIONAHA.114.014092 (Circulation 2015;132:907–915) | Trial: NCT01278953
- **Design:** Prospective multicentre RCT, 1:1, non-inferiority (NOT powered for superiority); TactiCath CF (EnSite NavX) vs ThermoCool Navistar control (CARTO); 17 sites, 47 operators; no protocol CF target specified
- **N / Follow-up:** [CONFIRMED from full text] 300 randomized paroxysmal AF (317 enrolled, 17 roll-in); safety population 295; effectiveness population 280 (CF 146, control 134) / 12 months
- **Key finding:** [FULL-TEXT CONFIRMED] Primary effectiveness (acute PVI + 12-mo freedom off AAD) 67.8% (CF) vs 69.4% (control); absolute diff −1.6%, lower limit one-sided 95% CI −10.7%, P=0.0073 for non-inferiority (margin −15%) — noninferior, NOT superior. Acute PVI 100% both arms. Within CF arm, optimal CF (≥90% lesions ≥10 g; achieved in 57.2%) 75.9% vs non-optimal 58.1% (P=0.018); clinically-relevant success 85.5% vs 67.7% (P=0.009). Primary device-related SAE 1.97% (CF) vs 1.40% (control), P=0.0004 non-inferiority (margin 9%).
- **Full-text data:**
  - Primary endpoint: 67.8% vs 69.4%, abs diff −1.6% (1-sided 95% CI lower −10.7%), P=0.0073 non-inferiority (Figure 2A); clinically-relevant success 78.1% vs 80.6% (P=0.659); "on-drug" analysis 72.6% vs 73.9%
  - First-pass isolation: not reported as such; acute PVI achieved in 100% of both arms
  - Acute reconnection: at 30-min wait 12.1% of lesion sets reconnected (CF 10.4% vs control 13.8%, P=0.206); CF-arm acute reconnection ~11% of PVs throughout trial vs control 18%→9% (learning effect)
  - 12-mo recurrence: 33 subjects (11.8%) repeat ablation post-blanking (16 CF, 17 control; 1 control needed 3rd); 12 repeats during blanking (6 each)
  - Procedure time: median fluoroscopy 27.0 (CF) vs 23.0 min (control) P=0.044; RF time 46.5 vs 53.0 min P=0.018
  - Complications: device+procedure-related SAE 7.24% (CF) vs 9.09% (control); primary device-related SAE 1.97% (3/152) vs 1.40% (2/143); cardiac tamponade/perforation 1 each arm (0.66% CF / 0.70% ctrl); PV stenosis 0 CF vs 1 control; pericarditis 2 CF vs 0; NO deaths, strokes, TIAs, or atrioesophageal fistulas either group (Table 2)
  - Subgroups: optimal vs non-optimal CF 75.9% vs 58.1% (P=0.018); operators with optimal CF in >80% of pts 79.1% vs 58.2% (P=0.008); CF 26.5 vs 19.2 g (P<0.001); EnSite experience effect — least-experienced operators 47.5% vs equivalent 75.7% (P=0.019) vs more-experienced 80.0% (P=0.004); excluding <25%-EnSite operators raised CF success 67.8%→76.0%
  - Metric thresholds: optimal CF defined post hoc as ≥90% of lesions with CF ≥10 g; manufacturer guidance ≤30 W / ≤30 g; CF target not protocol-specified
  - Key tables: Table 1 (baseline), Table 2 (SAEs), Figures 1–5
- **Relevance:** HIGH (key RCT showing CF availability alone ≠ better outcome; supports A3)
- **Notes:** Central to the "CF alone insufficient" controversy (Law 4). Confound: CF arm tied to EnSite, control to CARTO (not a pure CF vs no-CF comparison) — authors flag operator/mapping-experience bias. Now full-text confirmed 2026-06-14 (`source/af-ablation-metrics/26260733`).

### [A017] Ullah 2016 — SmartTouch CF-on vs CF-off RCT
- **Source:** PubMed | PMID: 27173976 | DOI: 10.1016/j.hrthm.2016.05.011 (Heart Rhythm 2016;13:1761–7) | Trial: NCT01730924
- **Design:** Prospective multicentre RCT, 7 UK centres; same SmartTouch catheter + Carto3 in both arms, CF data visible (CF-on) vs blinded (CF-off); target CF 5–40 g; intention-to-treat
- **N / Follow-up:** [CONFIRMED from full text] 117 paroxysmal AF randomized (59 CF-on, 58 CF-off; 3 withdrawn pre-procedure excluded → analysis 59 vs 56; 114/117 completed 12 mo) / 12 months (7-day Holter at 6 & 12 mo)
- **Key finding:** [FULL-TEXT CONFIRMED] Primary endpoint (time to isolate both vein sets) NOT different. CF-on vs CF-off: acute PV reconnection 22% vs 32% (P=0.03; 31% relative reduction) but NO difference in 12-mo single-procedure success off AAD (49% [29/59] vs 52% [29/56], P=0.9). Mean CF per application identical (13.4 [9.1–19.6] vs 13.4 [7.4–22.4] g, P=0.5) but more readings in 5–40 g target range with CF-on (80% vs 68%, P<0.0005). No difference in procedure/fluoroscopy times or major complications (3% vs 5%, P=0.7).
- **Full-text data:**
  - Primary endpoint: bilateral PVI time — total PVI time 70 [55–90] (CF-on) vs 73 [4–86] min (CF-off), P=0.82 (NS); total procedure time 194 vs 196 min, P=0.96 (Table 2)
  - First-pass isolation: not reported (WACA + 60-min wait + adenosine protocol)
  - Acute reconnection: of 392 analyzable PVs (76/468 excluded for protocol violations), 104/392 (27%) reconnected (68/104 spontaneous, 36/104 adenosine); CF-on 22% vs CF-off 32%, P=0.03 (Figure 2)
  - 12-mo recurrence: single-procedure success off AAD CF-on 29/59 (49%) vs CF-off 29/56 (52%) [or 29/58=50% if all dropouts=failures], P=0.9 (KM Figure 3)
  - Procedure time: 194 [171–220] vs 196 [165–217] min (P=0.96); fluoroscopy 648 vs 830 s (P=0.82); RF ablation time 2483 vs 2315 s (P=0.86) — all NS; individual RF application LONGER & higher FTI with CF-on (duration 52.3 vs 43.2 s P<0.0005; FTI 750 vs 639 g·s P<0.0005, Table 4)
  - Complications: major 2/59 (3%) CF-on (1 tamponade, 1 pseudoaneurysm) vs 3/58 (5%) CF-off (1 hematoma readmission, 1 pericarditis+effusion, 1 broken sheath), P=0.7; minor 4 vs 2 (P=0.7) (Table 3)
  - Subgroups / CF distribution: CF<5 g in 25% (CF-off) vs 17% (CF-on); CF>40 g in 6% vs 4%; 4,048,039 CF measurements analyzed (data available 81/117 cases)
  - Metric thresholds: target CF 5–40 g; ≥50 g visual safety alarm in BOTH arms (partial unblinding, a stated limitation); temperature-controlled 48°C/30 W; RF ≥20 s aiming >80% EGM reduction or <0.1 mV
  - Key tables: Table 1 (baseline), Table 2 (procedural), Table 3 (complications), Table 4 (RF application params), Figures 1–4
- **Relevance:** HIGH (RCT: CF improves acute metrics, not 12-mo recurrence; supports A3/A6)
- **Notes:** PMID confirmed by full text (NCT01730924; Heart Rhythm 2016;13:1761–7). Underpowered for complications; CF-off not fully blinded (>50 g alarm). Now full-text confirmed 2026-06-14 (`source/af-ablation-metrics/27173976`).

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
- **Source:** PubMed | PMID: 33851484 | DOI: 10.1111/jce.15041 (J Cardiovasc Electrophysiol 2021;32:1540–8) | Trial: NCT03793998
- **Design:** Prospective single-arm multicentre cohort (8 Italian centres); IntellaNav MiFi OI (DirectSense LI) + Rhythmia HDx; ablation guided by LI drop magnitude/time-course
- **N / Follow-up:** [CONFIRMED from full text] 153 patients (mean age 59±10, 70% men; 94 [61.4%] paroxysmal, 59 [38.6%] persistent; 96 [62.7%] de novo, 57 [37.3%] redo) / mean 366±130 days
- **Key finding:** [FULL-TEXT CONFIRMED] LI-guided PVI: 100% acute isolation, no steam pops, NO major complications (0% tamponade/fistula). 18 patients (11.8%) recurred after 90-day blanking (>88% AT/AF-free at 12 mo). Recurrence higher in persistent (11/59=18.6%) than paroxysmal (7/94=7.4%, P=0.0426). Absolute LI drop larger at successful (n=3122, 88%) than ineffective sites (n=434, 12%): 14±8 vs 6±4 Ω (P<0.0001); LI far outperformed generator impedance (GI drop 4.3±5 vs 3.1±5 Ω; AUC LI 0.806 vs GI 0.582). Every 5-Ω LI-drop increment → OR 3.13 (95% CI 2.7–3.6) for success; LI drop >15 Ω = effective.
- **Full-text data:**
  - Primary endpoint (acute LI predictors): successful sites baseline LI 105±15 → 92±12 Ω post (mean drop 13±8 Ω, %drop 12±7%) vs GI 90.1±11→85.9±9 (drop 4.2±5 Ω); LI drop at success 14±8 vs failure 6±4 Ω (P<0.0001)
  - First-pass isolation: not reported as %; all PVs isolated 100%
  - Acute reconnection: not separately reported (all isolated)
  - 12-mo recurrence: 18/153 (11.8%) post-blanking — AF only 10 (6.5%), AT only 7 (4.6%), both 1 (0.7%); persistent 18.6% vs paroxysmal 7.4% (P=0.0426); de novo 10.4% vs redo 14% (P=0.6052); de novo paroxysmal lowest (6.9%), redo persistent highest (23.8%)
  - Procedure time: 136±47 min; fluoroscopy 17.1±8 min; 7598 total RF applications (median 44 [27–66] spots, RF pulse 33 [24–48] s); mean power 35±4 W
  - Complications: 0 major (no tamponade/atrioesophageal fistula/steam pop); minor 9 (5.9%) — 5 vascular (3 groin hematoma, 1 pseudoaneurysm, 1 AV fistula), 4 pericarditis with mild effusion (all conservative)
  - Metric thresholds: LI-drop ROC — every 5-Ω increment OR 3.13 (95% CI 2.7–3.6); >15 Ω effective; LI drop/τ best cutoff 0.65 Ω/s (sens 56.4/spec 81.8, AUC 0.749) → OR 5.54 (95% CI 4.31–7.11); proposed max cutoff LI drop 30 Ω, effective predictor ~15 Ω; target ≥10 Ω within 30 s, stop at ≥40 Ω; ILD ≤6 mm; power 30–35 W. Analysis on 3556/7598 first-pass applications >10 s (105/153=69% had complete video)
  - Key tables: Table 1 (baseline/procedure), Figures 1–5
- **Relevance:** HIGH (LI-guided 1-year clinical outcome; the confirmed CHARISMA 1-yr study)
- **Notes:** Prior record was truncated/sparse — now fully extracted. Note: this is the *Solimene* CHARISMA 1-yr paper; it cites the *Segreti* CHARISMA pilot as ref 10 (Segreti L et al. J Cardiovasc Electrophysiol 2020;31:2319–27, DOI 10.1111/jce.14647) — that resolves the [A022] UNCONFIRMED Segreti PMID question (see UNCONFIRMED list). Now full-text confirmed 2026-06-14 (`source/af-ablation-metrics/33851484`).

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
- **Source:** PubMed | PMID: 37476572 | DOI: 10.3389/fcvm.2023.1169037 (Front Cardiovasc Med 2023;10:1169037) | Trial: NCT03793998
- **Design:** Prospective multicentre registry, 16 European centres; StablePoint catheter (combined CF + LI) + Rhythmia HDx; first PVI for paroxysmal & persistent AF (incl. 20 reanalyzed pilot cases)
- **N / Follow-up:** [CONFIRMED from full text] 212 patients (130 [61.3%] paroxysmal, 82 [38.7%] persistent; 68.9% male, age 61±10) / acute (13,891 RF applications ≥3 s analyzed of 15,599 delivered); no medium/long-term outcome reported
- **Key finding:** [FULL-TEXT CONFIRMED] First-pass PV isolation 93.3% per vein (180/212 patients = 84.9%); 80 PV gaps (63.7% at right PVs). At successful vs gap spots: baseline LI 161.4±19 vs 153.0±13 Ω (P<0.0001), LI drop 22.1±9 vs 14.4±5 Ω (P<0.0001), %LI drop 13.5±5% vs 9.4±3% (P<0.0001). ROC ideal LI drop overall >20 Ω (spec 93.2%); region-specific >21 Ω anterior (sens 60.2/spec 93.5), >18 Ω posterior (sens 55.9/spec 86.3). Every 5-Ω LI-drop increment OR 2.03 (95% CI 1.9–2.2). Non-linear weak CF↔LI-drop association (r=0.14); higher CF → higher likelihood of ideal LI drop; both CF & LI drop inversely related to delivery time.
- **Full-text data:**
  - Primary endpoint: first-pass PVI per vein 93.3% (84.9% of patients); ideal LI drop ROC AUC 0.784 overall
  - First-pass isolation: 93.3% per vein; 80 gaps (anterior 25 [31.3%], posterior 25 [31.3%], carina 16 [20%], superior 8 [10%], inferior 6 [7.5%])
  - Acute reconnection: not separately reported beyond first-pass gaps; all PVs ultimately isolated
  - 12-mo recurrence: NOT assessed (acute lesion-quality registry; explicit limitation)
  - Procedure time: 115±41 min; fluoroscopy 10.3±7 min; mean 68±23 ablation spots; mean RF duration time 9.2±4 s; mean power 48±2 W (45–50 W); total RF time 11±4 min (cf. CLOSE 35.2±11.1 in VISTAX)
  - Complications: 0 — no tamponade, stroke, esophageal fistula, or steam pops; minor 7 (3.3%): 4 vascular, 3 pericarditis (Table 1)
  - Subgroups (anterior vs posterior): baseline LI homogeneous (161.1 vs 161.3 Ω, P=0.847); LI drop 23.0±8 vs 20.4±9 Ω (P<0.0001); %LI drop 14.1 vs 12.5% (P<0.0001); RF delivery 9.7 vs 8.9 s (P<0.0001); CF 11.8 vs 13.0 g (P<0.0001)
  - Metric thresholds: ideal LI drop >21 Ω anterior / >18 Ω posterior (matches Szegedi 21.80/18.30); %LI-drop cutoff >12.5% overall (>14% ant, >12% post); protocol target LI drop ≥15 Ω within 15 s, max ≥40 Ω, general aim 20–30 Ω; CF 5–40 g; ILD ≤6 mm; CF >25 g had little extra impact on LI drop
  - Key tables: Table 1 (baseline), Table 2 (logistic regression), Figures 1–4
- **Relevance:** HIGH (links CF and LI drop; largest single CF-LI lesion dataset; G1)
- **Notes:** Acute only; non-randomized; no esophageal temperature monitoring (no complications observed). Now full-text confirmed 2026-06-14 (`source/af-ablation-metrics/37476572`).

### [A028] Lian/Lyan 2024 — Local-impedance-drop-guided vs LSI-guided PVI
- **Source:** PubMed | PMID: 38995604 | DOI: 10.1007/s10840-024-01870-3 (J Interv Card Electrophysiol 2024;67:2051–2058)
- **Design:** Retrospective, non-randomized, double-arm comparison. LID-guided (IntellaNav MiFi, Rhythmia, **no CF monitoring**, stop at LI-drop plateau) n=35 vs LSI-guided (TactiCath, EnSite Precision, CF-based) n=31; both 40 W anterior/30 W posterior, ILD <6 mm
- **N / Follow-up:** [CONFIRMED from full text] 66 patients (LID 35, LSI 31; persistent AF 68.6% vs 74.2%, P=0.82); 264/264 PVs isolated / 11.5±2.9 months (Holter 3/6/12 mo)
- **Key finding:** [FULL-TEXT CONFIRMED] LSI vs LID: significantly shorter RF ablation time (25 [21–31] vs 30 [27–35] min, P=0.035); first-pass PVI in more circles (54/62=87% vs 43/70=61%, P=0.002); fewer patients with any PV gap (42% [13/31] vs 74% [26/35], P=0.016). Arrhythmia recurrence by KM higher with LID (34.3% vs 16.1%, log-rank P=0.037) — though raw Table-2 recurrence comparison P=0.09. Predefined LID targets met in only 22.4% (anterior) / 55.1% (posterior); LID <9.7 Ω predicted PV gap (sens 96.4/spec 67, AUC 0.85).
- **Full-text data:**
  - Primary comparison: RF ablation time LID 30 vs LSI 25 min (P=0.035); total procedure time 150 vs 156 min (P=0.31, NS); fluoroscopy 12 vs 11 min (P=0.25)
  - First-pass isolation: per circle LID 43/70 (61%) vs LSI 54/62 (87%), P=0.002
  - Acute reconnection (after 20-min wait): LID 9/70 (13%) vs LSI 5/62 (8%) circles, P=0.54 (NS); first-pass gaps 34 (LID, 20/35=57% pts) vs 7 (LSI, 7/31=23% pts), P=0.009
  - Overall PV gaps: 26/35 (74%) LID vs 13/31 (42%) LSI, P=0.016; paroxysmal subgroup 9/11 (81.8%) vs 2/8 (25%), P=0.045
  - 12-mo recurrence: 12/35 (34.3%) LID vs 5/31 (16.1%) LSI (Table 2 P=0.09; KM log-rank P=0.037); redo 10 (28.6%) vs 3 (9.7%); chronic PV reconnection at redo 7/10 (70%) vs 2/3 (67%)
  - Procedure time: see above; both groups off all AAD except beta-blockers at follow-up
  - Complications: NO major complications either arm
  - Metric thresholds: **internal discrepancy in paper** — Abstract states "target LID 12 Ω posterior, 16 Ω anterior"; Methods text states "LID target 16 Ω posterior, 12 Ω anterior." LSI target 5 anterior / 4 posterior (LSI in gap points 3.8±1.0 vs no-gap 4.9±1.1, P<0.0001). LID success vs gap sites: baseline LI 103.5±13.8 vs 96.9±10.7 Ω (P<0.0001), LI drop 13.8±9.1 vs 5.3±3.1 Ω (P<0.0001). Best gap predictor LID <9.7 Ω. LOCALIZE-derived targets cited: 16.1 Ω anterior / 12.3 Ω posterior
  - Key tables: Table 1 (baseline), Table 2 (procedural/gaps/follow-up), Figures 2–3, Supplementary Tables 1–2
- **Relevance:** HIGH (rare direct head-to-head: impedance-drop vs LSI; G1)
- **Notes:** First author "Evgeny Lian" (=Lyan); same group's abstract version (Lyan 2023, Europace) is the SAME logical study — cite full paper 38995604. KEY CAVEAT: LID arm used NO contact-force sensing, so superiority of LSI may reflect CF-monitoring benefit rather than LSI-vs-LID per se (authors' own limitation). Mostly persistent AF. Internal LID-target wording discrepancy flagged above. Now full-text confirmed 2026-06-14 (`source/af-ablation-metrics/38995604`).

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
- **Source:** PubMed | PMID: 41517933 | DOI: 10.1111/jce.70246 (J Cardiovasc Electrophysiol 2026;37:501–509)
- **Design:** Two-protocol single-centre study (Fujita Health Univ, Japan). Study 1: lesion-level AID-vs-gap analysis, n=20 patients / 1687 RF points + ex-vivo swine (n=444 lesions). Study 2: single-arm %AID-guided PVI clinical validation, n=30 patients. TactiFlex SE (TFSE) catheter + EnSite X AID module
- **N / Follow-up:** [CONFIRMED from full text] Study 1: 20 patients (55% persistent), 1687 lesion points (CG+ 45, CG− 1642); Study 2: 30 patients (67% persistent) / 1-year (event-free analysis, 1-week Holter)
- **Key finding:** [FULL-TEXT CONFIRMED] Conduction-gap lesions had lower %AID than gap-free (7.2±1.7% vs 9.6±3.1%, P<0.0001; absolute AID 7.0±2.3 vs 9.4±3.7 Ω, P<0.0001). ROC %AID cutoff for predicting CG = 9.33% (absolute AID 8.01 Ω; unfiltered generator-impedance drop 11.0 Ω); %AID AUC 0.761 significantly > unfiltered GI-drop AUC 0.627 (P<0.05). %AID correlated with %voltage-amplitude decrease (R²=0.785) and with ex-vivo lesion volume (R²=0.711). In %AID (≥9%)-guided PVI (Study 2): first-pass isolation 90% LPV / 90% RPV (vs 70%/70% conventional in Study 1, P=0.074); 1-year atrial-tachyarrhythmia event-free 82% (4/30 recurred); NO adverse events, NO steam pops. **TFSE has NO native lesion-estimating parameter (AI/LSI absent)** — AID is the surrogate.
- **Full-text data:**
  - Primary endpoint (Study 1, gap prediction): %AID CG+ 7.2±1.7 vs CG− 9.6±3.1% (P<0.0001), Table 2; ROC %AID cutoff 9.33%, AUC 0.761 vs unfiltered GI-drop AUC 0.627 (P<0.05, DeLong)
  - First-pass isolation: Study 1 (conventional HPSD/SPLD) 70% LPV / 70% RPV; Study 2 (%AID-guided) 90% LPV / 90% RPV (P=0.074 vs Study 1)
  - Acute reconnection / gaps: Study 1 — 45/1687 CG+ points; lower RF energy (600±163 vs 696±172 J), shorter duration (13.4±4.5 vs 16.6±5.3 s), no CF or ILD difference. Study 2 — 20/2452 CG+ points
  - 12-mo recurrence: Study 2 — 4/30 recurred → 1-year event-free 82% (Figure 4)
  - Procedure time: not separately tabulated (HPSD 50 W/10–12 s/CF 5–10 g or SPLD 25–30 W/30 s/CF 10–20 g in Study 1; Study 2 modified HPSD ≥40 W/15–20 s/CF 5–20 g)
  - Complications: NO adverse events in either protocol; NO steam pops in Study 2 (14 SPs in ex-vivo only). Context: Arai 2024 [A035] found TFSE higher tamponade — attributed to absence of lesion-index, motivating this AID work
  - Metric thresholds: %AID ≥9% target (cutoff 9.33%) for durable lesion; absolute AID cutoff 8.01 Ω; %AID >14% (ex-vivo) predicts steam pops (stop RF); SP AUC %AID 0.907. Esophageal T° limit 41°C. Caveat: 7/45 CG+ points still had %AID ≥9% (anterior ridge/roof LPV, posterior RPV — thicker/curved wall), and 756/1642 gap-free points had %AID <9% → fixed 9% not universally sufficient/necessary
  - Comparison anchors cited: Matsumoto TFSE 50 W first-pass 87%/82% (GI-drop cutoff 13.5/14.5 Ω, AUC 0.612/0.586); Nair TactiFlex pivotal [A034]; Dello Russo HPSD-TFSE vs SPLD-TC
  - Key tables: Table 1–2 (Study 1), Table 3–4 (Study 2), Figures 1–4 + Supporting ex-vivo
- **Relevance:** HIGH (critical context: TactiFlex SE uses AID not AI/LSI; most recent catheter paradigm)
- **Notes:** Single-centre, small N, Study 2 single-arm (no control — stated limitation); 1-week Holter only. OCR table shows CG− n=1682 vs text 1642 for Study 1 (minor extraction inconsistency; both ≈ total 1687 − 45 CG+); use 45 CG+ / ~1642 CG−. Now full-text confirmed 2026-06-14 (`source/af-ablation-metrics/41517933`).

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
  CHARISMA pilot," *J Cardiovasc Electrophysiol* 2020;31(9):2319–2327, **DOI 10.1111/jce.14647**.
  *Citation lead obtained from full text:* the Solimene 2021 CHARISMA paper [A024] cites this as its
  ref 10 with the exact volume/pages/DOI above (and Lepillier 2023 [A027] ref 6 corroborates:
  "J Cardiovasc Electrophysiol 2020;31(9):2319–27, doi:10.1111/jce.14647"). The PMID still needs a
  direct PubMed confirmation, but the DOI is now corroborated by two independent full-text reference
  lists — **resolve the PMID via the DOI before citing [A022]; no longer treat as fabrication-risk.**

> **Process flag for orchestrator/appraiser:** PubMed metadata + full-text MCP tools and NCBI E-utilities
> were unavailable this run (permission/egress). All metadata here is Consensus-sourced and each PMID was
> title-confirmed against PubMed, but **full text was not retrieved** — the appraiser should obtain full
> text (re-grant the `get_full_text_article`/metadata permissions or supply PDFs in `source/`) before
> finalizing GRADE, and re-extract all CIs/Ns from results tables (L-005).
