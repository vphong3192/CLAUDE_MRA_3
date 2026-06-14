# Critical Appraisal — Ablation Metrics in RF-PVI for Atrial Fibrillation

> **Appraiser output** for the review *Comparison of ablation metrics in RF-PVI (AI, LSI/VISITAG, Local
> Impedance Drop, Contact Force, AID/TactiFlex SE).*
> **Date:** 2026-06-14 · **Inputs:** `00_protocol.md`, `reference/af-ablation-metrics-pvi-rf.md` (35 records).
> **Tools applied:** Cochrane RoB 2 (RCTs), ROBINS-I (non-randomized), GRADE per outcome.
> **Constitution binding:** Law 3 (hierarchy), Law 4 (consensus vs controversy — Section 4), Law 5
> (limitations from Assumption Register — Sections 5–6).
> **Lessons applied:** L-002 (language ↔ GRADE, Section 7), L-005 (effect sizes from full-text tables —
> 10 records confirmed, rest flagged provisional), L-006 (contradictions preserved, Section 4),
> L-007 (associative language for observational data), L-010 (composite endpoints decomposed).

> **CARDINAL APPRAISAL MESSAGE (read first):** The entire field rests on a **single design pattern** —
> prospective and retrospective **cohorts** with **historical or propensity-matched controls**. There is
> **NO RCT of any lesion-quality index (AI, LSI, LID, AID) vs conventional ablation.** The only RCTs in
> the corpus (TOCCASTAR, Ullah) test **contact-force *availability***, not index-guided dosing, and both
> are **negative for 12-month clinical benefit.** Therefore the headline claim "metric-guided ablation
> improves outcomes" is supported almost entirely by **Low / Very-Low certainty** evidence. The writer
> must not let the volume of concordant cohort data masquerade as high certainty (this is the exact error
> the role exists to prevent).

---

## Section 1 — Evidence hierarchy overview

### 1.1 Classification of all 35 records by design

| Tier (Law 3) | Records | n |
|---|---|---|
| **Meta-analysis / systematic review** | A007 (Ioannou — but **all inputs non-randomized**: 4 retrospective + 7 prospective cohorts, **no RCT**) | 1 |
| **RCT** | A016 (TOCCASTAR — CF vs non-CF, non-inferiority), A017 (Ullah — CF-on vs CF-off) | 2 |
| **Prospective cohort / registry** (single-arm or parallel, incl. historical/propensity controls) | A001, A002, A003, A004, A005, A006, A012, A015, A018, A019, A020, A021, A022*, A023, A024, A027, A029, A033(Study 2), A034 | ~19 |
| **Retrospective cohort** | A008(control arm), A010, A011, A013, A014, A025, A026, A028, A035 | ~9 |
| **Society guideline / expert consensus** | A030 (2024 ESC/EACTS), A031 (2023 ACC/AHA/ACCP/HRS), A032 (2017 HRS/EHRA/ECAS consensus) | 3 |

\* A022 (Segreti CHARISMA pilot) PMID still UNCONFIRMED — **do not cite** until resolved (L-009).
Pedersen 2020 also UNCONFIRMED — **do not cite.**

> **Design caveats that bear on grading:**
> - A007 is nominally top-tier (meta-analysis) but **inherits the limitations of its non-randomized
>   inputs** — authors themselves rate the body "low to moderate quality." It cannot be graded above its
>   sources.
> - A002, A006, A008 use **historical / non-concurrent controls** → high confounding risk (learning
>   curve, secular technique improvement).
> - A033 is **two sub-studies**: Study 1 (lesion-level, acute) and Study 2 (single-arm clinical,
>   n=30, no control).

### 1.2 Which metrics have what tier of evidence

| Metric | Best available evidence | RCT vs conventional? | Notes |
|---|---|---|---|
| **AI (Ablation Index)** | Meta-analysis of cohorts (A007) + multiple prospective cohorts (A001–A006) | **NO** | Largest, most consistent cohort base; still no RCT of AI-guided vs conventional. |
| **LSI / VISITAG** | Prospective + retrospective cohorts (A008–A014); one head-to-head vs LID (A028) | **NO** | Smaller base than AI; threshold-derivation heavy; A028 confounded (see §4.3). |
| **LID / local impedance** | Prospective registries (A024, A027) + lesion-level pilots (A021–A029) | **NO** | Mostly **acute-surrogate** data; only A024/A028 report ≥12-mo clinical outcome. |
| **CF (contact force)** | **2 RCTs** (A016, A017) + cohorts (A015, A018–A020) | **YES (only metric with RCTs)** | RCTs show acute benefit but **NO 12-mo clinical benefit**; SMART-AF (cohort) is the positive outlier. |
| **AID (TactiFlex SE)** | One single-centre study, Study 2 single-arm n=30 (A033) + pivotal catheter trial (A034) | **NO** | Newest, thinnest; pilot-level only. TFSE has **no native AI/LSI** — AID is a surrogate. |

---

## Section 2 — Risk-of-bias assessment

### 2.1 RCTs — Cochrane RoB 2

#### A016 — TOCCASTAR (Reddy 2015) — CF-sensing vs non-CF catheter, non-inferiority RCT

| RoB 2 domain | Judgment | Basis |
|---|---|---|
| Randomization process | **Low** | 1:1 randomized, multicentre (17 sites). |
| Deviations from intended intervention | **SOME CONCERNS** | **Confounded by platform**: CF arm = TactiCath/EnSite NavX; control = ThermoCool/CARTO. Not a pure CF-vs-no-CF contrast; mapping-system + operator-experience effects confound (authors flag; excluding <25%-EnSite operators raised CF success 67.8→76.0%). No protocol CF target. |
| Missing outcome data | **Low** | Effectiveness population 280/300 well accounted. |
| Measurement of outcome | **Low–Some concerns** | Standard arrhythmia monitoring; open-label (catheter type not blindable). |
| Selection of reported result | **Low** | Pre-registered (NCT01278953); primary endpoint reported. |
| **Overall** | **SOME CONCERNS** | Driven by intervention/platform confounding. Underpowered for superiority (non-inferiority design only). |

#### A017 — Ullah 2016 — CF-on vs CF-off RCT (same catheter)

| RoB 2 domain | Judgment | Basis |
|---|---|---|
| Randomization process | **Low** | Randomized, 7 UK centres, ITT analysis. |
| Deviations from intended intervention | **Low** | **Cleaner design** — same SmartTouch catheter both arms; only CF visibility differs. |
| Missing outcome data | **Low** | 114/117 completed 12 mo. |
| Measurement of outcome | **SOME CONCERNS** | CF-off **not fully blinded** — ≥50 g safety alarm visible in both arms (partial unblinding, authors' stated limitation). |
| Selection of reported result | **Low** | Pre-registered (NCT01730924). |
| **Overall** | **SOME CONCERNS** | Best internal validity in corpus for the CF question; underpowered for complications (3% vs 5%, NS). |

### 2.2 Non-randomized studies — ROBINS-I (key domains)

Common pattern flagged once, then per-study deviations noted.
**Domain key:** Conf = confounding · Sel = selection · Class = intervention classification · Miss =
missing data · Meas = outcome measurement · Rep = selective reporting.

| ID | Design | Conf | Sel | Class | Miss | Meas | Rep | Overall ROBINS-I | Dominant problem |
|---|---|---|---|---|---|---|---|---|---|
| A001 Taghji (CLOSE pilot) | Prosp single-arm | n/a (no control) | Mod | Low | Low | Low | Low | **MODERATE** | No comparator — threshold-defining, not comparative. |
| A002 Phlips (CLOSE vs CONV-CF) | Prosp parallel, **historical control** | **SERIOUS** | Serious | Low | Mod | Low | Low | **SERIOUS** | Historical control + learning curve (authors call for RCT). |
| A003 Hussein 2017 | Prosp AI vs **propensity-matched** CF | Mod | Mod | Low | Low | Low | Low | **MODERATE** | Propensity matching mitigates but residual confounding. *Abstract-derived — provisional.* |
| A004 PRAISE | Prosp single-arm | n/a | Mod | Low | Low | Low | Low | **MODERATE** | N=40, no comparator. *Abstract-derived.* |
| A005 FAFA-AI | Prosp single-arm | n/a | Serious | Low | Mod | Low | Some | **SERIOUS** | N=50, 6-mo only. *Abstract-derived.* |
| A006 Dhillon HPAI | Multicentre registry vs **historical FTI** | **SERIOUS** | Serious | Low | Mod | Low | Low | **SERIOUS** | Historical control; efficacy diff NS. *Abstract-derived.* |
| A008 Mattia | Prosp LSI vs **retrospective** non-CF | **SERIOUS** | Serious | Low | Mod | Low | Some | **SERIOUS** | N=60, retrospective control. *Abstract-derived.* |
| A010 Katić | Retrospective single-arm | Serious | Serious | Low | Mod | Mod | Some | **SERIOUS** | N=39, no comparator. *Abstract-derived.* |
| A011 Cai 2022 | Retrospective lesion-level | Mod | Mod | Low | Low | Low | Low | **MODERATE** | Acute gap surrogate. *Abstract-derived.* |
| A012 Prasad (LSI Workflow) | Prosp single-arm, multinational | n/a | Mod | Low | Low | Low | Low | **MODERATE** | Single-arm; documents regional heterogeneity. *Abstract-derived.* |
| A013 Cai 2023 | Retrospective | Mod | Mod | Low | Mod | Low | Low | **MODERATE** | 2-yr data; single-arm. *Abstract-derived.* |
| A014 Kuo 2025 | Retrospective two-group | **SERIOUS** | Serious | Low | Mod | Low | Low | **SERIOUS** | Retrospective allocation by strategy. *Abstract-derived.* |
| A015 SMART-AF | Prosp multicentre non-randomized | Serious | Mod | Low | Low | Low | Low | **MODERATE–SERIOUS** | The positive CF-stability outlier; post-hoc CF-stability subgroup. *Abstract-derived; pre-2015 historical.* |
| A018 SMART-SF | Prosp open-label non-rand | Mod | Mod | Low | Low | Low | Low | **MODERATE** | Acute/safety. *Abstract-derived; PMID re-verify.* |
| A019 PRECEPT | Prosp multicentre non-rand | Mod | Mod | Low | Low | Low | Low | **MODERATE** | Persistent AF benchmark, single-arm. *Abstract-derived.* |
| A020 TactiSense | Prosp single-arm | n/a | Mod | Low | Low | Low | Low | **MODERATE** | Benchmark. *Abstract-derived.* |
| A021 Martin | First-in-human feasibility | n/a | Serious | Low | Mod | Mod | Some | **SERIOUS** | N=31, feasibility. *Abstract-derived.* |
| A023 Masuda | Prosp blinded, lesion-level | Mod | Mod | Low | Low | Low | Low | **MODERATE** | N=15, acute surrogate. *Abstract-derived.* |
| A024 Solimene (CHARISMA 1-yr) | Prosp single-arm multicentre | n/a | Mod | Low | Low | Low | Low | **MODERATE** | Best LID clinical-outcome data; single-arm. **Full-text confirmed.** |
| A025 Szegedi | Prosp pilot, lesion-level | Mod | Mod | Low | Low | Low | Low | **MODERATE** | Acute; CF non-discriminative finding. *Abstract-derived.* |
| A026 Fukaya (STABLEPOINT) | Prosp two-centre blinded | Mod | Mod | Low | Low | Low | Low | **MODERATE** | Acute thresholds. *Abstract-derived.* |
| A027 Lepillier (CHARISMA reg) | Prosp multicentre registry | n/a | Mod | Low | Mod | Low | Low | **MODERATE** | Largest CF-LI lesion dataset; **acute only, no clinical outcome.** **Full-text confirmed.** |
| A028 Lian/Lyan | **Retrospective** double-arm LID vs LSI | **SERIOUS** | Serious | **SERIOUS** | Mod | Low | Some | **SERIOUS** | Retrospective; **LID arm had NO CF sensing** → intervention-classification confound (see §4.3); internal threshold inconsistency. **Full-text confirmed.** |
| A029 Perge | Prosp lesion-level | Mod | Mod | Low | Low | Low | Some | **MODERATE** | Possible patient overlap with A025 (same group). *Abstract-derived.* |
| A033 Harada (Study 2) | Single-arm n=30 | n/a (no control) | Serious | Low | Mod | Low | Some | **SERIOUS** | N=30, single-arm, 1-wk Holter only, single-centre. **Full-text confirmed.** |
| A034 Nair (TactiFlex pivotal) | Prosp non-rand multicentre IDE | Mod | Mod | Low | Low | Low | Low | **MODERATE** | No AI/LSI metric (CF+time). *Abstract-derived.* |
| A035 Arai | Retrospective registry (safety) | Serious | Mod | Low | Mod | Low | Low | **MODERATE–SERIOUS** | Platform safety comparison; confounded by catheter/centre. *Abstract-derived.* |

### 2.3 Meta-analysis (A007 Ioannou) — ROBINS-I of the body + structural note

- **Inputs:** 11 studies, **0 RCT** (4 retrospective + 7 prospective cohorts). The pooled estimate
  cannot exceed the certainty of its non-randomized inputs.
- **Heterogeneity:** procedure time I²=90% (very high), fluoroscopy I²=75% (high) — major inconsistency
  on efficiency outcomes; first-pass I²=58% (moderate); primary relapse I²=35% (low-moderate); acute
  PVR and tamponade I²=0%.
- **Publication-bias signal:** authors report a **funnel-plot asymmetry for procedure time** → reporting
  bias plausible.
- **Quality tool used by authors:** Newcastle-Ottawa; authors self-rate "low to moderate quality."
- **Overall:** treat as **MODERATE-to-SERIOUS ROBINS-I body**; a meta-analysis of confounded cohorts,
  not of RCTs.

---

## Section 3 — GRADE evidence table (per outcome)

> GRADE starts non-randomized evidence at **Low** and RCT evidence at **High**, then up/down-grades.
> Downgrade reasons: **RoB** (risk of bias), **Incons** (inconsistency), **Indir** (indirectness),
> **Imprec** (imprecision), **PubBias** (publication bias). Upgrade: **large effect**, **dose-response**.

### O1 — First-pass PVI rate (ACUTE SURROGATE)

| Metric | Key data (source) | Direction | GRADE |
|---|---|---|---|
| **AI** | 98% (A001); 98% vs 54% (A002); 97% vs 84% (A003); meta 93.4% vs 62.9%, OR 0.09 [0.04–0.21] (A007) | Strongly favours AI | **LOW** |
| **LSI** | 78.1% (A011); 76.2% (A012); 83.9% (A013); 87% vs (LID 61%) (A028) | Favourable, single-arm mostly | **LOW** |
| **LID** | 93.3%/vein (A027); 90% (A033 Study 2); 61% in head-to-head (A028) | Mixed (A028 lower) | **LOW** |
| **CF** | Acute PVI ~100% both arms (A016); first-pass not reported in CF RCTs | No discriminating first-pass data | **VERY LOW** |
| **AID** | 90%/90% (A033 Study 2, n=30, vs 70% conventional P=0.074 NS) | Favourable but NS, tiny N | **VERY LOW** |

**Overall O1 grade: LOW.**
- Start Low (non-randomized). **Large, consistent effect for AI** (OR 0.09; 93.4 vs 62.9%) would justify
  an *upgrade*, but it is offset by **serious RoB** (historical controls A002/A006) and **indirectness**
  (first-pass is an acute surrogate, not a clinical endpoint) → net **LOW**, not Moderate.
- LID head-to-head (A028) **contradicts** registry first-pass (61% vs 93%) — but A028's LID arm lacked
  CF sensing (confound). AID/CF graded **Very Low** (single tiny study / not reported).

### O2 — 12-month freedom from ATA recurrence (PRIMARY CLINICAL OUTCOME)

| Metric | Key data (source) | GRADE |
|---|---|---|
| **AI** | 92.3% (A001); 94% vs 80% P<0.05 (A002); recurrence 17% vs 37% (A003); 78% vs 64% **NS** (A006); meta relapse 11.8% vs 24.9%, OR 0.41 [0.25–0.66], NNT 7.6 (A007) | **LOW** |
| **LSI** | 89.3% vs 65.6% (A008); 95.7% (A012); 87.1% @2yr (A013); recurrence 14.9% vs 32.5%, HR 0.36 [0.16–0.83] (A014) | **LOW** |
| **LID** | 11.8% recurrence (A024); 16.1% vs 34.3% LSI-better, KM P=0.037 / Table-2 P=0.09 (A028) | **VERY LOW** |
| **CF** | 72.5% (A015, cohort, +stability subgroup); **67.8% vs 69.4% non-inferior NOT superior** (A016 RCT); **49% vs 52% NS** (A017 RCT); 61.7% (A019) | **MODERATE (for "no superiority of CF availability")** |

**Overall O2 grade: LOW** for AI and LSI; **VERY LOW** for LID; **MODERATE for the specific CF
conclusion that CF *availability* does not improve 12-mo outcome.**

Reasoning (the most important grading judgment in this review):
- **AI & LSI (LOW):** Start Low (cohorts). Consistent direction, but downgrade for **serious RoB**
  (A002/A006/A008/A014 historical or retrospective controls) and **imprecision** (wide CIs, e.g. A014
  HR 0.36 [0.16–0.83]; A002 OR 3.917 [1.008–15.220] — lower bound barely excludes 1). The **A006 null
  result (78% vs 64%, NS)** is a critical inconsistency within the AI evidence and must be reported
  (L-006). Net: **LOW** — "may reduce / appears to reduce," not "reduces."
- **LID (VERY LOW):** Only A024 (single-arm) and A028 (retrospective, confounded, internally
  inconsistent KM vs Table-2 p-values) provide ≥12-mo data → downgrade for RoB + imprecision +
  indirectness. **Insufficient to conclude.**
- **CF (MODERATE, in a specific direction):** This is the one place we have **two RCTs**. TOCCASTAR
  (non-inferior, not superior) + Ullah (acute benefit, **no 12-mo benefit**) are **concordant** that
  **CF *availability* alone does not improve 12-month freedom**. Start High (RCT), downgrade once for
  **Some Concerns RoB** (platform confound A016; partial unblinding A017) and **imprecision** (both
  underpowered) → **MODERATE.** Note: this is a conclusion of *absence of benefit from CF availability*,
  **not** a conclusion about index-guided dosing. SMART-AF's positive CF-stability finding is a
  lower-tier post-hoc cohort subgroup and does not overturn the RCTs (Law 3).

> **Composite-endpoint decomposition (L-010):** Most "freedom from ATA" endpoints bundle AF + AT + AFL.
> Where decomposable: A024 recurrences were AF 6.5% / AT 4.6% / both 0.7% — i.e. the LID "11.8%
> recurrence" is **not** all AF. The writer should not imply a metric prevents *AF specifically* when the
> endpoint is a composite.

### O3 — Procedural efficiency (procedure time, RF time)

| Metric | Key data (source) | GRADE |
|---|---|---|
| **AI vs CF** | Procedure −30%, RF −50% (A002); meta AI 141 vs 152.8 min, MD −11.81 [−20.89 to −2.74] (A007) | **LOW** |
| **LSI + HPSD** | Higher LSI → shorter times (A012, A013, A014) | **LOW** |
| **LID vs LSI** | RF 30 vs 25 min, LSI shorter P=0.035; procedure time NS (A028) | **VERY LOW** |

**Overall O3 grade: LOW.**
- Start Low (cohorts). **Severe inconsistency** in the meta-analysis (procedure-time **I²=90%**,
  fluoroscopy I²=75%) + **funnel-plot publication-bias signal** (A007) → these would justify a further
  downgrade, but the effect is directionally consistent (AI/LSI faster). Net **LOW**. A028's RF-time
  result is confounded (LID arm no CF) → **Very Low** for the LID-vs-LSI efficiency contrast.

### O4 — Safety (composite: tamponade, PV stenosis, esophageal injury, steam pops, stroke)

| Source | Safety signal |
|---|---|
| A016 TOCCASTAR (RCT) | Primary device-related SAE **1.97% (CF) vs 1.40% (control)**; tamponade 1 each arm; 0 deaths/strokes/fistulas |
| A017 Ullah (RCT) | Major AE **3% vs 5%, NS**; underpowered |
| A007 Ioannou (meta) | Tamponade **1.6% vs 2.4%, OR 0.69 [0.30–1.60], NS**; 0 fistula/stroke/death either arm |
| A035 Arai (registry) | **TactiFlex tamponade 1.1% vs CARTO-platform 0.2%, P=0.008** (multivariate OR 4.8 for TF/TC platforms) |
| A013 Cai | Steam pops 1.6% (LSI-HPSD) |
| A001/A002/A024/A027/A033 | Essentially **0 major complications** (no tamponade/fistula/steam pop) in metric-guided cohorts |

**Overall O4 grade: VERY LOW (for any between-metric safety *difference*); LOW (for the general
statement that metric-guided RF-PVI has low absolute complication rates).**
- **All studies are underpowered for rare safety events** (A8 confirmed). The RCT and meta-analysis
  safety comparisons are **all NS**. The only statistically significant safety signal is **A035
  (TactiFlex/EnSite higher tamponade)** — but it is a **retrospective registry confounded by
  catheter/platform/centre**, and it reflects catheter design, **not** a lesion-index comparison.
- **Inconsistent reporting** of esophageal injury and steam pops across studies (A8) precludes pooling.

### O5 — Acute reconnection / dormant conduction (INTERMEDIATE SURROGATE)

| Metric | Key data (source) | GRADE |
|---|---|---|
| **AI** | Adenosine-proof 97% vs 82% P<0.001 (A002); acute PVR 6% vs 13% P=0.02 (A003); meta PVR 18% vs 35%, OR 0.37 [0.18–0.75], I²=0% (A007) | **LOW** |
| **CF** | Acute reconnection 22% vs 32% P=0.03 (A017 RCT — CF-on better acutely) | **MODERATE** |
| **LID** | LI drop 23 vs 12 Ω at gap sites (A023); CF AUC non-discriminative (A025); LI-drop AUC 0.761–0.806 (A033, A024); gap predictor LID <9.7 Ω (A028) | **LOW** |

**Overall O5 grade: LOW**, except **MODERATE for "CF-on reduces acute reconnection vs CF-off"** (A017
RCT, consistent with A002 AI data; downgrade once from High for partial unblinding + single trial).
- Surrogate outcome → inherent **indirectness** for clinical decisions.
- **Consistent mechanistic signal across metrics:** larger impedance drop / better contact → fewer
  acute gaps. The LID-vs-CF discrimination data (A025 CF non-discriminative; A023/A024 LI superior to
  generator impedance) are mechanistically coherent but **acute-surrogate only**.

### GRADE summary table (writer's quick reference)

| Outcome | AI | LSI | LID | CF | AID |
|---|---|---|---|---|---|
| O1 First-pass PVI | LOW | LOW | LOW | VERY LOW | VERY LOW |
| O2 12-mo freedom | LOW | LOW | VERY LOW | **MOD (no benefit of CF availability)** | VERY LOW |
| O3 Efficiency | LOW | LOW | VERY LOW | — | — |
| O4 Safety (between-metric diff) | VERY LOW | VERY LOW | VERY LOW | VERY LOW | VERY LOW |
| O5 Acute reconnection | LOW | LOW | LOW | **MOD (CF-on vs CF-off)** | LOW (acute) |

---

## Section 4 — Key contradictions (Law 4 — separate consensus from controversy)

> Per L-006, both sides are reported with citations AND a methodological reason for the discrepancy.

### 4.1 Contact-force availability → outcome (RCT-negative vs cohort-positive)

- **No clinical benefit side:** **TOCCASTAR (A016, RCT)** — CF non-inferior, **not superior** (67.8% vs
  69.4%). **Ullah (A017, RCT)** — CF-on improved *acute* reconnection (22% vs 32%) but **NO 12-mo
  difference** (49% vs 52%, NS).
- **Benefit side:** **SMART-AF (A015, cohort)** — staying within target CF range ≥80% of time → **4.25×**
  more likely success.
- **Methodological resolution:** The benefit signal is a **post-hoc CF-*stability* subgroup within a
  non-randomized cohort**; the RCTs (higher tier, Law 3) test CF *availability* and are negative. Within
  TOCCASTAR itself, the **optimal-CF subgroup did better** (75.9% vs 58.1%) — consistent with SMART-AF —
  but this is post-hoc. **Consensus: CF availability alone does not guarantee benefit; CF *quality/
  stability* may matter, but only at low certainty.** This directly supports assumption **A3**.

### 4.2 AI vs CF superiority (cohort-suggested, no RCT)

- **AI-superior side:** CLOSE-protocol cohort data — **A002** (94% vs 80%), **A003** (recurrence 17% vs
  37%), pooled **A007** (relapse OR 0.41).
- **Caveat side:** **No RCT** of AI-guided vs CF-guided/conventional exists; **A002/A006 use historical
  controls** (learning-curve confound; A002 authors explicitly call for an RCT); **A006 efficacy
  difference was NS** (78% vs 64%, P=0.186).
- **Resolution:** AI **appears** superior to CF-only guidance, but the claim rests on **confounded
  cohorts** → **LOW certainty**. Cannot be stated as established. Supports the **A7 gap** (no head-to-head
  RCT).

### 4.3 LID vs LSI (the head-to-head is confounded)

- **LSI-better finding:** **A028 (Lian/Lyan 2024)** — LSI shorter RF time (25 vs 30 min), higher
  first-pass (87% vs 61%), fewer gaps (42% vs 74%), lower recurrence (16.1% vs 34.3%, KM P=0.037).
- **Major caveat (intervention-classification confound):** the **LID arm used NO contact-force
  sensing**, while the LSI arm (TactiCath) did. So the apparent LSI superiority **may reflect the
  benefit of CF monitoring**, not LSI-vs-LID per se — **the authors' own stated limitation.** Also
  retrospective, mostly persistent AF, and **KM P=0.037 conflicts with raw Table-2 P=0.09** (statistical
  inconsistency within the same paper).
- **Resolution:** This is **the only head-to-head LID-vs-LSI study and it cannot support a clean
  comparison** → **VERY LOW certainty.** Writer must state the CF confound explicitly. Supports the
  **A4 gap** (LID least standardized, least RCT support).

### 4.4 LID threshold direction inconsistency (internal contradiction)

- **A028 internal discrepancy:** Abstract states "target LID 12 Ω **posterior**, 16 Ω **anterior**";
  Methods text states "16 Ω **posterior**, 12 Ω **anterior**" — a **direction flip** within one paper.
  LOCALIZE-derived targets cited as 16.1 Ω anterior / 12.3 Ω posterior (anterior > posterior, the
  physiologically expected direction given thicker anterior wall).
- **Resolution:** The thresholds themselves are **unsettled**; this internal inconsistency is concrete
  evidence that **LID targets are not standardized** (A4). Writer should cite the LOCALIZE direction
  (anterior > posterior) as the likely intended one but flag the discrepancy.

### 4.5 LSI threshold heterogeneity (no single agreed target)

- **Range across studies:** LSI anterior targets span **~3.95 to 6.5**: A009 ~4.05–5.2 (region-specific),
  A011 best cutoff 4.35 (4.55 ant / 3.95 post), A013 4.7 ant / 4.3 post, A008 5.5–6 ant, **A010 6.5
  anterior**, A012 mean LSI varied **by region** (EU 4.4, Japan 4.5, US 5.5), A014 ≥5.0 ant / 4.5 post.
- **Resolution:** **No consensus LSI target** — heterogeneity is partly **regional/workflow-driven**
  (A012) and partly tissue-thickness-driven (posterior lower). This **precludes pooling** and is a core
  methodological gap (A2, G3). Same heterogeneity, less severe, applies to AI (400–550 range) and LID.

### 4.6 (Bonus) CF as a lesion-quality discriminator — contradicted by impedance studies

- **CF non-discriminative:** **A025 (Szegedi)** and **A009 (Kanamori — for the LSI/gap question CF/FTI
  did differ, but A025 found CF/FTI did NOT differ between success/failure)** report **CF/FTI did not
  separate successful from failed lesions**, whereas **local-impedance drop did** (A023, A025). A027
  found only a **weak non-linear CF↔LI-drop association (r=0.14).**
- **Resolution:** Supports **A3** — instantaneous CF is **necessary but insufficient**; integrated/
  impedance metrics discriminate lesion quality better. Acute-surrogate evidence, **LOW** certainty.

---

## Section 5 — Assumption Register (status of A1–A10)

| # | Assumption | Status | Evidence |
|---|---|---|---|
| **A1** | AI anterior ≥500–550 / posterior ≥400 (CLOSE) is most-studied cutoff | **CONFIRMED** | A001 defines it; A002, A007 (pooled commonest 500–550 ant / 400–450 post) adopt it; it is the field's reference convention. |
| **A2** | LSI ≈5.0 ant / 4.0 post most-cited; LSI base smaller than AI | **PARTIALLY CONFIRMED** | LSI base **is** smaller than AI (confirmed). But "5.0/4.0" is **not** a settled single target — actual range 3.95–6.5 (A008–A014); regional variation (A012). The *direction* (anterior > posterior) holds. |
| **A3** | CF necessary but insufficient; integrated indices predict better | **CONFIRMED** | A016/A017 (CF availability ≠ 12-mo benefit); A025 (CF non-discriminative for lesion success); A023/A024 (LI drop > generator impedance); A027 (weak CF↔LI r=0.14). Strongest-supported assumption. |
| **A4** | LID newest, least-standardized, least RCT support | **CONFIRMED** | Thresholds vary widely (A024 ~15 Ω; A025 21.8/18.3; A026 20.0; A027 21/18; A028 internal flip); **no RCT**; mostly acute surrogates. |
| **A5** | Data mostly paroxysmal, Western/Japanese; Asian/Vietnamese validation thin | **PARTIALLY CONFIRMED / mostly CONFIRMED** | Asian cohorts exist (A009 Japan, A011/A013 Cai, A014 Kuo, A033 Harada Japan, A012 Japan subset) — so **not purely Western**. But **NO Vietnamese-specific data**; persistent-AF data thinner than paroxysmal. Vietnamese gap **CONFIRMED**. |
| **A6** | Metric guidance improves first-pass/reduces acute reconnection; weaker/less-consistent 12-mo effect | **CONFIRMED** | Acute benefit consistent (O1, O5); 12-mo benefit weaker — A006 NS, A016/A017 RCTs NS for CF. Exactly the predicted pattern. |
| **A7** | Direct AI-vs-LSI head-to-head RCTs scarce; comparisons indirect/registry | **CONFIRMED (stronger than stated)** | **NO AI-vs-LSI RCT at all**; the only head-to-head is LID-vs-LSI (A028, retrospective, confounded). All AI-vs-LSI comparison is **indirect**. |
| **A8** | Safety differences under-powered; steam-pop/esophageal rates reported inconsistently | **CONFIRMED** | All safety comparisons NS (A007, A016, A017); reporting inconsistent; only A035 significant (and confounded). |
| **A9** | Rise of PFA reframes RF-metric relevance | **STILL UNRESOLVED** | No corpus record directly evaluates PFA-vs-RF-metric relevance; this remains an **inference / context point**, not evidenced. Flag per Law 1 ("no direct evidence found; this is context/inference"). |
| **A10** | Abstract effect sizes incomplete → extract from full text | **CONFIRMED (process)** | 10 records full-text confirmed (A001/2/7/9/16/17/24/27/28/33); **25 remain abstract-derived = provisional** (L-005). |

> **New assumption surfaced during appraisal (log for Limitations):**
> **A11 — AID/TactiFlex SE evidence is pilot-level only.** TFSE has no native AI/LSI; AID surrogate is
> validated in a **single-centre, single-arm n=30 study with 1-week Holter** (A033) → cannot be compared
> on equal footing with AI/LSI/CF. **CONFIRMED as a gap.**

---

## Section 6 — Gaps that feed the Limitations section (Law 5)

1. **No RCT of any lesion-index (AI/LSI/LID/AID) vs conventional ablation.** The only RCTs (A016, A017)
   test CF *availability* and are negative for 12-mo benefit. The entire "metric-guided is better"
   thesis is **cohort-grade** (Low/Very-Low).
2. **No head-to-head AI-vs-LSI study of any design** (A7). The single LID-vs-LSI head-to-head (A028) is
   retrospective and **confounded by absent CF sensing in the LID arm** (§4.3).
3. **Threshold non-standardization** across all metrics (AI 400–550; LSI 3.95–6.5; LID 9.7–21.8 Ω;
   AID ~9%) — driven by region, tissue thickness, and catheter — **precludes meta-analytic pooling** (G3).
4. **LID/AID evidence is predominantly acute-surrogate** (first-pass, gap prediction); only A024/A028
   give ≥12-mo clinical outcomes, both at Very-Low certainty.
5. **No Vietnamese-specific and limited persistent-AF / elderly data** (A5); thresholds validated mostly
   in paroxysmal AF; applicability to a Vietnamese persistent-AF population is an **assumption**, not
   evidence.
6. **Safety underpowered and inconsistently reported** (A8); the one significant safety signal (A035)
   is confounded and catheter-specific, not metric-specific.
7. **Short follow-up** in several pivotal records (A005 6 mo; A027/A009/A033-Study1 acute only;
   A033-Study2 1-week Holter) → recurrence rates likely **underestimated**.
8. **Historical / non-concurrent controls** in the foundational AI comparative studies (A002, A006,
   A008) → learning-curve and secular-trend confounding.
9. **25 of 35 records remain abstract-derived (provisional, L-005)** — CIs/Ns for these should be
   re-extracted from full text before final pooling; several PMIDs need re-confirmation (A018);
   **A022 Segreti and Pedersen 2020 are UNCONFIRMED — do not cite.**
10. **PFA disruption (A9) unaddressed by the corpus** — the clinical relevance of RF lesion metrics in a
    PFA era is context/inference, not evidence (Law 1).
11. **Meta-analysis (A007) has high heterogeneity (I² up to 90%) and a publication-bias signal** for
    efficiency outcomes → pooled efficiency estimates are unstable.

---

## Section 7 — Recommendations for the writer (Law 2 + L-002)

> **Binding rule (L-002):** match verb strength to the GRADE cell in §3. Use **associative, not causal**
> language for all cohort data (L-007): "associated with," "linked to," not "causes/reduces" — EXCEPT
> the two RCT-backed CF conclusions.

### Permitted language by outcome × metric

| Claim | GRADE | Required phrasing |
|---|---|---|
| **AI improves first-pass PVI** | LOW | "**appears to be associated with** higher first-pass isolation" — cite A001/A002/A007; note A002/A006 historical controls. |
| **AI reduces acute reconnection** | LOW | "**may reduce / is associated with less** acute reconnection" (A002, A003, A007 OR 0.37, I²=0). |
| **AI improves 12-mo freedom** | LOW | "**may improve / is associated with** higher 12-mo freedom (NNT≈7.6, A007), **though no RCT exists and one cohort (A006) found no significant difference**." Do NOT write "AI reduces recurrence" as fact. |
| **LSI improves first-pass / 12-mo** | LOW | "**appears to be associated with**…"; always note threshold heterogeneity (3.95–6.5) and smaller evidence base. |
| **LSI superior to LID** | VERY LOW | "**evidence is insufficient to conclude**; the single head-to-head (A028) is confounded by absent contact-force sensing in the LID arm — **requires confirmation**." |
| **LID/local-impedance drop predicts durable lesions** | LOW (acute) | "**is associated with** durable acute lesions; local-impedance drop **outperforms generator impedance** (A023/A024)"; for clinical outcome → "**evidence is insufficient** beyond acute surrogates." |
| **LID improves 12-mo freedom** | VERY LOW | "**evidence is insufficient to conclude**; based on one single-arm registry (A024) and one confounded retrospective comparison (A028) — **requires confirmation**." |
| **CF availability improves 12-mo outcome** | MODERATE (negative) | State as a **moderate-certainty negative**: "Two RCTs (A016, A017) **demonstrate that contact-force *availability* alone does not improve** 12-month freedom, though it **reduces acute reconnection** (A017)." This is the one place "demonstrates" is allowed — for the *null/acute* result. |
| **CF stability/quality matters** | LOW | "**may be associated with** better outcomes (SMART-AF 4.25×; TOCCASTAR optimal-CF subgroup) — **post-hoc, requires confirmation**." |
| **CF necessary but insufficient (A3)** | LOW–MOD | "Contact force **appears necessary but insufficient**; integrated/impedance indices discriminate lesion quality better (A025, A023, A027)." |
| **AID/TactiFlex SE is effective** | VERY LOW | "**evidence is insufficient to conclude**; a single single-arm study (A033, n=30, 1-week Holter) **requires confirmation**. TactiFlex SE lacks a native AI/LSI index — AID is a surrogate." |
| **Any between-metric SAFETY difference** | VERY LOW | "**evidence is insufficient** to establish safety differences between metrics; all comparisons are underpowered (A007/A016/A017 all NS). The TactiFlex tamponade signal (A035) is **catheter/platform-specific and confounded**, not a metric comparison." |
| **Procedural efficiency (AI/LSI faster)** | LOW | "**is associated with** shorter procedure/RF times, **though pooled estimates are highly heterogeneous (I²=90%) with a publication-bias signal** (A007)." |

### Must-mention controversies (hand to writer for the Law-4 "Ongoing controversy" section)
1. CF availability: RCT-negative (A016/A017) vs cohort-positive (A015) — §4.1.
2. AI vs CF superiority — no RCT, historical-control confound — §4.2.
3. LID vs LSI head-to-head confounded by absent CF sensing — §4.3.
4. LID threshold direction flip within A028; LSI target range 3.95–6.5 — §4.4–4.5.

### Established-consensus items (safe to state plainly)
- CLOSE protocol AI targets (≥400 post / ≥550 ant, ILD ≤6 mm) are the field's **reference convention**
  (A1 CONFIRMED).
- Larger impedance drop / adequate contact **acutely** produces more durable lesions (mechanistic
  consensus across A001, A002, A023, A024, A027 — but acute surrogate).
- Metric guidance's benefit is **strongest on acute surrogates and weaker/inconsistent on 12-month
  clinical recurrence** (A6 CONFIRMED).

---

## Handoff note to synthesis-writer

- **Cite ONLY from `reference/af-ablation-metrics-pvi-rf.md`.** Do not cite A022 (Segreti) or Pedersen
  2020 (UNCONFIRMED). Re-verify A018 PMID at write.
- **The headline must not overstate.** No metric has RCT evidence of clinical superiority vs conventional
  ablation. Lead with the **Low/Very-Low** certainty framing; the single Moderate cell is a *negative*
  CF conclusion.
- **Carry the §7 phrasing verbatim** — language strength is graded, not stylistic (L-002).
- **25 records are provisional** (abstract-derived); if the writer needs a CI/N not in a full-text block,
  flag it rather than invent it (Law 1). Request retriever full-text re-fetch if a provisional number
  becomes load-bearing.
- **Limitations section** is pre-built in §6; the Assumption Register (§5, incl. new A11) feeds it (Law 5).
