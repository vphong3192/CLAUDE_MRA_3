# 04_appraisal.md — Critical appraisal (Phase 4): metformin efficacy and safety in adults with T2D

**Author:** critical-appraiser · **Date:** 2026-10-27 · **Branch:** `review/regression-2026-10-27`
**Scope anchor:** `00_scope.md` (clinical decision support · internists · ~1500 words · 2015–present ·
Vietnamese output · effort `normal`). **Gate status:** Research Map CLEARED (`03a_gate_approval.md`,
"Duyệt, tiếp tục"). **Appraised set:** exactly the 33 approved sources (16 HIGH / 17 MEDIUM) of the
final list in `03_research_map.md`. MET-M02, M13, M17 are DROPPED and are not appraised or used.
**Lessons applied:** L-005, L-006, L-010, L-039, L-043 (L-018, L-034 not applicable to this topic).

Companion artifacts: `04a_numbers.md` (deterministic store extraction) · `04b_cards.jsonl` (104 evidence
cards, 31 studies) · `04c_quote_locks.md` (verify_quotes: **104 accepted / 0 rejected**) ·
`source/metformin-t2d/` (machine-fetched NCBI text + `_fetch_manifest.json` + `_PROVENANCE.md`).

---

## 0. What changed at Phase 4, and what the quote locks prove (read first)

1. **Text on disk now exists, fetched by machine — not by me.** `source/` was empty. Direct HTTPS to NCBI
   E-utilities works through the session proxy (the Phase-2 failures were MCP empty bodies and WebFetch
   DNS). A deterministic script fetched, byte-for-byte, the PubMed XML record for all 33 approved studies
   (35 PMIDs incl. linked publications) and the PMC XML where a PMCID exists → 56 files in
   `source/metformin-t2d/`, SHA-256 per file in `_fetch_manifest.json`. No model transcribed any of it.
   This completes the user's own Gate 2b instruction ("Tải PMC + thử web"); **no new study was added.**
2. **Full-text depth after the fetch.** PMC served a full-text body for 16 records: HIGH H04, H05, H08,
   H10, H12, H13, S02 (the 7 already read by the retriever) and MEDIUM M04, M07, M08, M09, M10, M11, M12,
   M14, M19. PMC served front matter only for H02, H06, H14, S01, S03. **HIGH abstract-only remains 9/16:
   H01, H02, H03, H06, H07, H11, H14, M03, S01** (judgements on these are provisional, L-005/L-043).
3. **Guideline text.** ADA SOC 2026 s9 (H02), ADA/EASD 2026 (H01) and KDIGO 2022 (H03) recommendation
   text is still **NOT on disk** and is not filled from memory. **New:** the full text of the
   **ADA/KDIGO 2022 consensus (M12, MEDIUM)** is on disk; its prose states the metformin eGFR thresholds and contraindication; its Table 1 also reproduces KDIGO
   Recommendation 4.1.1 / Practice Point 4.1.3, but that is table text and was **not carded** (prose-only rule).
   These statements may be cited **to M12** (as M12 reporting ADA 2022/KDIGO 2022), never to H03 directly.
4. **What a green lock proves here.** All 104 cards quote NCBI-served text (`text_provenance` on each card).
   A green lock therefore proves: the quote is literally in text no model wrote; the file carries that
   study's PMID (IDENTITY); every number in the Vietnamese claim is in the quote (NUMBER); 34 `fulltext`
   cards quote body text outside the abstract (FULLTEXT). **It does not prove** (a) that the claim reads
   the quote correctly, (b) that the PMC rendering equals the publisher's version of record, or (c) anything
   beyond abstract depth for the 70 `abstract`-tier cards. Negative controls (wrong number, wrong PMID,
   abstract quote tagged fulltext) were run and all three were rejected — the locks are live.
5. **Provenance defects found in the Phase-2 record stream (not in the store).** In
   `02b_records.jsonl`/`02c_studies.jsonl`, the `abstract` field of MET-H13, M07, M08, M10, M11, M15, M16
   and S03 is an **agent-written summary** (93–269 chars, e.g. H13: "71 RCTs: abdominal pain RR 1.491…"),
   and M06 is empty; the real PubMed abstract of H13 contains **no numbers at all** (its numbers are in the
   full text). Nothing in this appraisal or the cards uses those summary fields. Lessons candidate (§11).
6. **`04a_numbers.md` limitation.** The extractor ran (exit 0) but its `confidence_intervals` bucket is
   empty for every record: the store writes CIs as "0.96 (0.84-1.09)" with no "CI" token, which the regex
   does not match, and some bare ratios are unbucketed. Every CI in this appraisal is therefore taken from
   a quote-locked card (stronger than the store), not hand-copied. One spurious token ("-26%", from
   "23-26%" in H05) is ignored.

---

## 1. Landmark scan (skill §0)

No approved source qualifies as a landmark (narrative review, last 5 years, high-impact journal, full text).
The only narrative review is Bin Hussain 2019 (M18; Diabetes Metab Syndr; 2019; abstract-only) — it fails
recency, venue and full-text criteria and is used **only as Level III framing of the first-line debate**.
I did not pull an unapproved review (that would need the gate re-opened). Orientation came instead from the
**ADA/KDIGO 2022 consensus full text (M12)** and the Research Map axes. Logged as AR-14; question Q3 in §12.

---

## 2. Evidence table (33 approved sources)

Design rank (Law 3): G = major-body guideline/consensus · SR/MA/NMA (of RCTs unless stated) · RCT-derived
post hoc · cohort/TTE · cross-sectional · Level III. Depth: **FT** = full text on disk and used ·
**ABS** = abstract only (provisional) · **FT\*** = full text on disk, abstract used for this appraisal.
RoB tools: SR → ROBIS-lite domains (D1 eligibility · D2 search/selection · D3 data/appraisal ·
D4 synthesis) — *the harness table has no SR tool; see Q4*; cohort/cross-sectional → Newcastle-Ottawa
(S selection · C comparability · O outcome); non-randomised intervention contrasts (TTE, within-trial
metformin-use comparisons) → ROBINS-I; guidelines → not appraisable (text not on disk) except M12.
Effect estimates are the values on the accepted cards listed in the last column.

| ID | Study | Design · depth | N / scope | Population | Key effect (95% CI) | Risk of bias (domain judgements) | Cards |
|---|---|---|---|---|---|---|---|
| H01 | Davies 2026 ADA/EASD | G · ABS | consensus | non-pregnant adults T2D (US/EU) | — (no metformin statement in abstract) | not appraisable (AGREE II impossible without text) | H01-c1,c2 |
| H02 | Bajaj 2026 ADA SOC s9 | G · ABS (PMC front matter only) | guideline | T2D | — nothing metformin-specific on disk | not appraisable | none (do not cite for metformin) |
| H03 | KDIGO 2022 | G · no abstract | guideline | diabetes + CKD | — (exec summary H03/36272755 abstract: GRADE-based, ch. 4 updated) | not appraisable; recs reachable only via M12 | none |
| H04 | Griffin 2017 | SR/MA RCT · FT | 13 trials; 2079 on metformin; only 4 placebo trials with CV outcomes | T2D, mainly white, ≤65 y, overweight, poorly controlled | ACM RR 0.96 (0.84–1.09); CV death 0.97 (0.80–1.16); MI 0.89 (0.75–1.06); stroke 1.04 (0.73–1.48); PVD 0.81 (0.50–1.31) | D1 low · D2 some (3 DBs) · D3 low · D4 low → **some concerns**; primary trials: none low RoB; UKPDS 52.3–70.5% weight | H04-c1…c6 |
| H05 | Li 2021 | SR/MA RCT · FT | 29 studies (18 articles); 371 deaths | T2D | Mono vs control: ACM 0.98 (0.69–1.38); CV death 1.13 (0.60–2.15); macrovascular 0.87 (0.70–1.07); HF 1.02 (0.61–1.71). Add-on combination: ACM 1.49 (1.02–2.16); CV death 2.21 (1.22–4.00) | D1 low (PROSPERO) · D2 **high** (PubMed+Embase only) · D3 some (4 low / 14 moderate RoB) · D4 **high** for combination analysis (mixes insulin/SU/dapagliflozin backgrounds; UKPDSb 23.22%/25.76%) → **high** | H05-c1…c6 |
| H06 | Gnesin 2020 Cochrane | SR/MA RCT · ABS | 18 RCTs, N=10,680, ≥1 y | T2D monotherapy | vs SU: deaths 31/1454 vs 31/1441 (very low); vs TZD ACM RR 0.88 (0.55–1.39); no placebo/behaviour trial | D1–D4 low (Cochrane methods, GRADE) → **low** (provisional) | H06-c1…c4 |
| H07 | Maruthur 2016 AHRQ | SR RCT+obs · ABS | 179 RCTs + 25 obs; search to 2015 | T2D | CV mortality lower vs SU; HbA1c similar across monotherapies; weight ↓/stable vs ↑ with SU/TZD/insulin (≤5 kg); GI AEs highest with metformin/GLP-1 RA | D1–D4 low (paired review, SoE grading) → **low** (provisional); funding AHRQ | H07-c1…c6 |
| H08 | Shi 2023 BMJ | NMA RCT · FT | 816 RCTs, 471,038 pts | T2D, add-on to standard care | Metformin: ACM OR 0.84 (0.67–1.04, low); non-fatal MI 0.86 (0.68–1.09, low); CV death / HF admission little/no or uncertain (low/very low). SGLT2i/GLP-1 RA ACM 0.88 (high). SU severe hypo 5.22 (3.88–7.01) | D1 low · D2 some (non-English excluded) · D3 low · D4 low (GRADE) → **low** | H08-c1…c5 |
| H09 | Nong 2025 BMJ living NMA | NMA RCT · ABS | 869 RCTs, 493,168 | T2D | No metformin estimate in abstract; SGLT2i/GLP-1 RA/finerenone CV-kidney benefit moderate–high | **low** (provisional) | H09-c1 |
| H10 | Silverii 2026 | pairwise+NMA RCT (adjudicated, ≥40 wk) · FT | 93 trials; **only 4 metformin studies** | T2D, mostly CVOT populations | MACE vs placebo: **abstract OR 0.69 (0.53–0.89); main text OR 0.68 (0.51–0.92)**; ACM: no effect for metformin; certainty "low for metformin" (abstract) vs "low to high, mostly moderate" (text) | D1 low · D2 some (restriction leaves 4 old metformin trials) · D3 low (RoB2, CINeMA; "some concerns" concentrated in metformin contrasts) · D4 some (abstract/text numeric drift; class level; HbA1c confounding) → **some concerns** | H10-c1…c8 |
| H11 | Patiño-Cardona 2026 | SR/MA of 12 obs · ABS | 12 observational studies | T2D + CKD | ACM HR 0.76 (0.64–0.90); ESRD 0.61 (0.49–0.76); MACE NS; stage-4 lactic acidosis HR 1.93 (0.95–3.87) | D3 some · D4 high (inconsistent, very low certainty per authors; confounding by indication) → **high** (provisional) | H11-c1…c3 |
| H12 | Lambourg 2024 | TTE (cohort) · FT | 4,278 of 371,742; median age 77 | T2D, incident CKD stage 4 (eGFR<30) on metformin, Scotland | Stop vs continue: **text** survival 63.4% vs 70.3%, HR 1.23 (1.08–1.41); **abstract** 63.7% vs 70.5%, HR 1.26 (1.10–1.44); MSM ACM 1.34 (1.08–1.67); MACE 1.05 (0.88–1.26) | ROBINS-I: confounding **serious** (residual, e.g. frailty/terminal decline prompting stopping) · selection moderate (prevalent users) · classification moderate (dose assumed, adherence unknown) · deviations moderate · missing low · measurement low · reporting moderate (abstract/text drift) → **serious** | H12-c1…c7 |
| H13 | Nabrdalik 2022 | SR/MA/meta-regression RCT · FT | 71 RCTs, 55,042 randomised | T2D (one paediatric study; exclusion did not change results) | Diarrhoea RR 2.445 (1.656–3.609); abdominal pain 1.491 (1.211–1.836); incidence diarrhoea 12.94%; IR > XR diarrhoea (coef −0.344, p=0.0437); AE discontinuation 1.080 (0.949–1.228) | D1 low (PROSPERO) · D2 some (English, 4 DBs) · D3 some (AE definitions unreported; 71% arms industry) · D4 some (study-level meta-regression) → **some concerns** | H13-c1…c6 |
| H14 | El-Damanawi 2024 Cochrane | SR/MA RCT · ABS | 11 RCTs, 8,449 (4 ADPKD, 7 diabetes) | CKD ± diabetes | vs placebo: eGFR decline MD 1.92 (0.33–3.51, low); death RR 1.00 (0.76–1.32, moderate); intolerance withdrawal RR 2.19 (1.46–3.27, moderate) | **low** methods (provisional); **indirectness** for T2D-CKD | H14-c1…c4 |
| M01 | Tsapas 2020 | NMA RCT · ABS | 453 RCTs; 296 on metformin background | T2D | Low CV risk on metformin background: no meaningful differences; increased CV risk: several SGLT2i/GLP-1 RA ↓ ACM | **low** (provisional); funding: EFSD with unrestricted AstraZeneca grant (COI note) | M01-c1,c2 |
| M03 | Palmer 2016 JAMA | NMA RCT · ABS | 301 RCTs | T2D | vs metformin, higher HbA1c with SU (SMD 0.18), TZD 0.16, DPP-4i 0.33, AGI 0.35; no class differences in CV/ACM; hypoglycaemia SU OR 3.13, basal insulin 17.9 | **low** (provisional) | M03-c1…c3 |
| M04 | Hu 2020 | SR/MA mixed (9 cohorts, 3 RCT post hoc, 1 NCC) · FT for advanced CKD | 13 studies, 303,540 | T2D + CKD | G1–3: ACM RR 0.71 (0.61–0.84; I² 79%); CV 0.76 (0.60–0.97; I² 87%); advanced CKD ACM 0.80 (0.49–1.31; I² 86.7%) | D2 low · D3 some · D4 **high** (pooling designs; extreme heterogeneity) → **high** | M04-c1,c2 |
| M05 | Zhang 2020 | SR/MA mainly obs · ABS | 16 studies, 1,160,254 | T2D | CV risk OR 0.57 (0.48–0.68); CV mortality 0.44 (0.34–0.57); incidence 0.73 (0.59–0.90) | D2 some · D4 **high** (observational, heterogeneity acknowledged) → **high** | M05-c1…c3 |
| M06 | Lalau 2018 | 3 prospective PK/dose studies · ABS | N not reported | T2D, CKD 3A/3B/4 | 1500/1000/500 mg by stage; metformin never >5.0 mg/L; no lactate >5 mmol/L (1 MI case) | uncontrolled → **high** for safety inference; mechanistic value only | M06-c1,c2 |
| M07 | Atkinson 2024 | mini-SR (no pooling) · FT\* | 21 articles from 2015 | T2D on metformin | 17/21 studies: association with lower B12; dose/duration risk factors | D2 high (3 DBs, English, excluded no-full-text) · D4 some (vote counting) → **high** | M07-c1…c3 |
| M08 | Jung 2025 | retrospective cohort (Korean NHIS) · FT\* | 11,200 PS-matched | new metformin users ≥4 mo | Metformin+PPI vs metformin: B12 deficiency aHR 1.18 (1.02–1.35) | NOS S 4/4 · C 2/2 · O 1/3 (outcome = code or B12 prescription) → **7/9** (provisional) | M08-c1 |
| M09 | Huynh 2024 (VN) | cross-sectional · FT\* | single centre (Vinmec) | Vietnamese T2D on metformin | B12 deficiency 18.6%; dose > median aOR 4.10 (1.62–10.36) | NOS-adapted: S 2/5 (convenience, single centre) · C 1/2 · O 2/3 → **moderate** | M09-c1…c3 |
| M10 | Nabrdalik 2024 | SR/MA of 21 obs · FT\* | 21 observational | T2D on metformin | Diarrhoea 6.9%, bloating 6.2%, pain 5.3%, vomiting 2.4%, constipation 1.1%; XR lower except diarrhoea (p=0.0951, NS) | D4 some (prevalence pooling, wide CIs) → **some concerns** | M10-c1,c2 |
| M11 | Tan 2021 | SR (5 RCT + 1 obs, GRADE) · FT\* | 1,662 RCT pts + 10,909 obs | T2D | XR vs IR: HbA1c MD 0.04% (−0.05 to 0.13); any GI AE RR 1.09 (0.93–1.29); better compliance with XR | D4 some (few small RCTs, imprecision) → **some concerns** | M11-c1…c3 |
| M12 | de Boer 2022 ADA/KDIGO | G (joint consensus) · **FT** | consensus | diabetes + CKD | Metformin if eGFR ≥30; 1,000 mg/d at eGFR 30–44 (and some at 45–59); contraindicated eGFR<30/dialysis; SGLT2i without metformin reasonable in some (B12 monitoring >4 y appears only in Table 3 — not carded) | AGREE II not formally scored; explicit link to ADA 2022 SOC and KDIGO 2022 GRADE recs; 2022 → currency assumption (AR-3) | M12-c1, c2, c4, c5, c7, c8 |
| M14 | Phan 2025 (VN) | cross-sectional · FT\* | 145 (Chợ Rẫy) | Vietnamese T2D on metformin, mean age 61.5 | B12 deficiency 22.1%; median dose 1700 mg, median use 10 y | NOS-adapted → **moderate** (single tertiary centre) | M14-c1 |
| M15 | Clegg 2021 | RCT-derived post hoc (EXSCEL, SAVOR-TIMI 53), PS-matched · ABS | 1,745 matched users | T2D, eGFR 15–59 | MACE HR 0.91 (0.76–1.08); ACM 0.86 (0.70–1.07) | ROBINS-I: confounding **serious** (metformin not randomised) · others moderate → **serious** | M15-c1,c2 |
| M16 | Charytan 2019 | RCT-derived post hoc (TREAT) · ABS | 591 users vs 3,447 non-users | T2D + CKD (anaemia trial) | ACM HR 0.49 (0.36–0.69); CV death 0.49 (0.32–0.74); CV composite 0.67 (0.51–0.88); 2 lactic acidosis cases | ROBINS-I: confounding **serious**; implausibly large effect → **serious** | M16-c1,c2 |
| M18 | Bin Hussain 2019 | Level III narrative · ABS | — | — | framing of first-line debate only | expert opinion; no RoB tool | M18-c1 |
| M19 | Dang 2024 (VN) | descriptive hospital study · FT\* | not used numerically | T2D with kidney failure, Cần Thơ | insulin mono predominant; metformin most-prescribed oral drug | descriptive; no comparison → context only | M19-c1 |
| S01 | Lazarus 2018 | 2 retrospective cohorts · ABS (PMC front matter only) | 75,413 + replication | diabetes, community (Geisinger; US claims) | Acidosis hospitalisation: overall aHR 0.98 (0.89–1.08); eGFR 45–59 1.16 (0.95–1.41); 30–44 1.09 (0.83–1.44); **<30 2.07 (1.33–3.22)** | NOS S 4/4 · C 2/2 (time-dependent, active comparator, PS) · O 2/3 (ICD 276.2, not adjudicated lactic acidosis) → **8/9** (provisional) | S01-c1…c4 |
| S02 | Yen 2021 | nationwide PS-matched cohort (Taiwan NHIRD 2000–09) · FT | 8,612 + 4,333 matched pairs | T2D + compensated / decompensated cirrhosis | Compensated: ACM aHR 1.13 (1.01–1.25); decompensation 1.15 (1.04–1.27); >1000 mg/d ACM aHR 1.42 | NOS S 3/4 · C 1/2 (no alcohol/BMI/smoking; no Child-Pugh/MELD) · O 2/3 → **6/9** | S02-c1…c4 |
| S03 | Sakellariou 2023 | SR/MA RCT+obs · ABS | 9 studies, 2,235 (1,076 on metformin) | PCI patients, mostly eGFR >30 (not T2D-restricted) | No lactic acidosis cases; CIN SMD 0.0007 (−0.1007 to 0.1022) | D2 low (4 sources) · D4 some (mixed designs) → **some concerns**; indirect | S03-c1 |

### 2a. Per-study IMRAD context (study_context / study_limitations / author_suggestions)
Carried from `reference/metformin-t2d.md` for the writer; confirmed against the fetched full text where marked.
- **H04 Griffin** — context: 60th-anniversary series; prior SRs pooled short trials vs mixed comparators. Limitations: 3 DBs, heterogeneous CV definitions, UKPDS-dominated, all trials at risk/unclear (confirmed, H04-c4). Suggestions: pragmatic EHR trials, factorial add-on trials, CVOT in people without diabetes; placebo CVOT in T2D unlikely (H04-c6).
- **H05 Li** — context: conflicting reports of CV benefit/harm. Limitations: PubMed+Embase only, cohorts excluded, ≥50% weight UKPDS (H05-c5). Suggestions: large double-blind placebo-controlled CV trial; authors advise caution with combinations.
- **H08 Shi** — context: feeds BMJ Rapid Recommendations; risk-centred goals. Limitations: low/very low certainty for oldest drugs incl. metformin; no dose–response. Suggestions: living updates.
- **H10 Silverii** — context: earlier NMAs lacked tirzepatide CVOT. Limitations: metformin from few small old trials (H10-c7); class-level; HbA1c confounding. Suggestions: none listed.
- **H12 Lambourg** — context: NICE says neither start nor continue at eGFR<30 (H12-c7) without RCT evidence. Limitations: residual confounding, dose assumed, adherence unknown, 44.2% on SU (H12-c5). Suggestions: RCTs (H12-c6).
- **H13 Nabrdalik 2022** — context: ~20% affected, ~5% discontinue. Limitations: OCT1-inhibiting co-drugs not modelled; AE definitions unreported; 71% industry arms. Suggestion: consider IR→XR switch.
- **S02 Yen** — context: no trial in diabetes + cirrhosis; small cohorts suggested benefit. Limitations: no alcohol/BMI data, no Child-Pugh/MELD (S02-c3), 2000–2009 data. Suggestions: prospective RCT.
- **All abstract-only records** (H01, H02, H03, H06, H07, H11, H14, M03, S01 among HIGH): `not captured (abstract-only)` — **flagged for full-text upgrade** (Q1). The 9 MEDIUM records with full text now on disk (M04, M07–M12, M14, M19) were appraised from the abstract except M04 (advanced-CKD result) and M12 (whole consensus); their IMRAD fields can be upgraded on request.

---

## 3. GRADE certainty per outcome (summary of findings)

Start: RCT/SR of RCTs = High; observational = Low. Downgrade reasons: RoB, Inconsistency, Indirectness,
Imprecision, Publication bias. "Strength summary" per axis uses: **Strong** = Moderate/High, concordant,
full-text HIGH sources · **Adequate** = Moderate from abstract-level SRs, or concordant Low evidence across
designs plus guideline consensus · **Thin** = Low/Very low, single-source or inconsistent · **Absent** = none
in the approved set.

| Axis | Outcome | Sources (cards) | Certainty | Reasons |
|---|---|---|---|---|
| A1 | HbA1c lowering vs other oral classes (metformin ≥ comparators) | M03-c1, H07-c1, M11-c1 | **Moderate** | −1 RoB/depth (both anchor NMAs abstract-only; old trials). Consistent, precise. |
| A1 | Durability / long-term glycaemic outcomes | H07-c6 | **Very low** | short trials; not addressed in corpus |
| A2 | All-cause mortality, metformin vs placebo/no drug | H04-c1, H05-c1, H08-c1, H10-c4, H06-c3 | **Low** | −1 RoB (no low-RoB trial; UKPDS open-label subgroup 52–70% weight); −1 imprecision (CI from ~16% ↓ to ~9% ↑); indirectness noted (1970s–90s, white, ≤65 y) |
| A2 | MACE / composite CV events | H10-c1/c2, H04-c1, H05-c1, H08-c2 | **Low** | −1 RoB; −1 inconsistency (Silverii significant vs Griffin/Li/Shi non-significant); Silverii rests on 4 old trials. Components (L-010): MI 0.89 (0.75–1.06) and 0.86 (0.68–1.09) — favour but NS; stroke 1.04 (0.73–1.48) — null/possible harm; CV death null. Any MACE benefit is not carried by stroke or CV death. |
| A2 | CV death | H04-c1, H05-c1, H08-c1 | **Low** | −1 RoB, −1 imprecision |
| A2 | HF hospitalisation | H05-c1, H08-c5 | **Very low** | −1 RoB, −2 imprecision (RR 1.02, 0.61–1.71) |
| A2 | CV mortality vs sulfonylureas | H07-c3, H06-c2 | **Low** | −1 inconsistency (AHRQ "lower" vs Cochrane very low, 4 vs 8 events); −1 depth (both abstract-only) |
| A2 | "Combination harm" (metformin added to other drugs ↑ mortality) | H05-c2…c5 vs M03-c2, M01-c1 | **Very low** | −1 RoB, −1 inconsistency with NMAs, −1 indirectness (mixed backgrounds; UKPDSb SU era), imprecision |
| A2 | Observational CV/mortality benefit | M05-c1…c3, M04-c1, M16-c2, H11-c1 | **Very low** | obs start Low; −1 RoB (confounding by indication, healthy-user/immortal-time risk); −1 inconsistency (I² 79–87%); effects implausibly large vs RCTs |
| A3 | Body weight (neutral/loss vs gain with SU/TZD/insulin) | H07-c2 | **Moderate** | −1 depth (abstract-only); consistent with Shi (intermediate weight effect) |
| A3 | Hypoglycaemia: low with metformin; high with SU/insulin | M03-c3, H08-c4, H07 | **Moderate** (SU/insulin excess: Moderate per Shi) | −1 depth/indirect (metformin is reference, not tested arm) |
| A4 | GI adverse events (diarrhoea, pain, nausea) | H13-c1…c3, H07-c4, H14-c3, M10-c1 | **Moderate** | −1 inconsistency/heterogeneity & undefined AE ascertainment; large consistent signal across RCT and observational data |
| A4 | Discontinuation due to AEs | H13-c5 vs H14-c3 | **Low** | −1 inconsistency (RR 1.080 NS vs all controls; RR 2.19 vs placebo in CKD); −1 indirectness |
| A4 | XR vs IR GI tolerability | M11-c1/c2, H13-c4, M10-c2 | **Low** | −1 inconsistency (RCT pooled null vs meta-regression/observational benefit); −1 imprecision (5 small RCTs) |
| A4 | Vitamin B12 deficiency (dose/duration-dependent) | M07-c1…c3, M09-c1…c3, M14-c1, M08-c1 | **Low** | obs Low; +1 dose–response (M09, M07); −1 RoB (mini-SR vote counting, cross-sectional) |
| A4 | Lactic acidosis at eGFR ≥30 (no excess) | S01-c1, S03-c1, M16-c2, M06-c2, M12-c5 | **Low** | obs Low; −1 indirectness (ICD acidosis code; PCI population); +1 consistency across 4 designs/large N |
| A5 | Lactic acidosis at eGFR <30 (excess) | S01-c2, H11-c2 | **Very low** | single cohort aHR 2.07; MA trend HR 1.93 NS; confounding |
| A5 | Death, metformin vs placebo in CKD (RCT) | H14-c2 | **Low** | authors: moderate; −1 indirectness here (4/11 ADPKD, not T2D-CKD) |
| A5 | eGFR decline vs placebo | H14-c1 | **Low** | per authors |
| A5 | Mortality/CV benefit in CKD G1–3 (obs) | M04-c1, H11-c1, M16-c2, M15-c1 | **Very low** | obs; inconsistency (M15 RCT-derived NS vs M16 HR 0.49); confounding |
| A5 | Continue vs stop at eGFR <30 (mortality) | H12-c1…c3, M04-c2 | **Very low** | single TTE (ROBINS-I serious); M04 advanced CKD NS (I² 86.7%) |
| A5 | Dose regimen by CKD stage | M06-c1/c2, M12-c1 | **Very low** (data) / guideline consensus on disk (M12) | uncontrolled PK; N not reported |
| A5 | Cirrhosis (compensated): ↑ mortality/decompensation | S02-c1…c4 | **Very low** | single cohort; unmeasured alcohol; IPCW mortality NS (within-study inconsistency) |
| A5 | Older adults (≥65) | — (H12-c4 indirect: median age 77, eGFR<30 only) | **Absent** | no dedicated record (3 supplementary queries) |
| A5 | Heart failure as a population | — | **Absent** | no record |
| A6 | SGLT2i/GLP-1 RA reduce mortality (added to standard care, mostly metformin) | H08-c3, M01-c2, H09-c1 | **High** | — |
| A6 | First-line SGLT2i/GLP-1 RA *instead of* metformin improves hard outcomes | H01-c1, M12-c7, M01-c1 | **Very low** | no head-to-head RCT in drug-naive patients in corpus; benefits shown on metformin background (indirectness −2) |
| A6 | Current (2026) guideline position of metformin | H01 (abstract), H02 (none) | **Absent on disk** | text not retrievable; only ADA/KDIGO 2022 (M12) on disk |

### Per-axis strength summary
| Axis | Summary | One-line rationale |
|---|---|---|
| A1 Glycaemic | **Adequate** | Moderate; anchor NMAs abstract-only |
| A2 CV / mortality | **Thin** (contested) | Low/Very low; RCT null-to-uncertain, Silverii lone significant MACE signal, observational confounded |
| A3 Weight / hypoglycaemia | **Adequate** | Moderate, concordant across AHRQ/Palmer/Shi |
| A4 Safety | GI **Adequate** · B12 **Thin→Adequate (Low, concordant)** · lactic acidosis eGFR ≥30 **Adequate (Low, concordant + consensus)** · XR vs IR **Thin** | |
| A5 Special populations | CKD eGFR 30–59 **Adequate** (Low + consensus M12) · eGFR <30 **Thin** (contested) · cirrhosis **Thin** · older adults **Absent** · HF **Absent** | |
| A6 Place in therapy | **Thin** | add-on benefit of SGLT2i/GLP-1 RA High, but metformin-vs-newer first-line comparison Very low and 2026 guideline text Absent |

---

## 4. Contradictions & controversies (10) — with steelman

**C1 · RCT null/uncertain vs observational benefit (A2, A5).** RCT syntheses: ACM RR 0.96 (H04-c1), 0.98 (H05-c1),
OR 0.84 low certainty (H08-c1), Cochrane "no clear evidence" (H06-c4). Observational: CV mortality OR 0.44 (M05-c2),
CKD G1–3 ACM RR 0.71 (M04-c1), TREAT HR 0.49 (M16-c2), CKD ACM HR 0.76 (H11-c1). *Reason:* confounding by
indication (metformin withheld from frailer/sicker patients, eGFR-driven prescribing), healthy-adherer effects,
heterogeneity (I² 79–87%). *Resolvable by quality* → RCT evidence governs; observational effects are not
estimates of causal benefit. **Steelman for benefit:** every RCT point estimate for ACM/MI favours metformin, CIs
are compatible with a 16% mortality reduction (H04-c5), and the RCT-derived CKD cohort (M15) is directionally
consistent; absence of evidence ≠ evidence of absence. **Conclusion the writer may state:** a CV/mortality benefit
of metformin is *possible but unproven* [GRADE Low].

**C2 · Silverii 2026 significant MACE reduction vs other syntheses; and Silverii's internal discrepancies (A2).**
Abstract OR 0.69 (0.53–0.89) (H10-c1) vs main-text Results OR 0.68 (0.51–0.92) (H10-c2); GLP-1 RA and tirzepatide
estimates also shift (0.87→0.88; 0.82→0.83, upper CI 0.93→0.96), suggesting the abstract reports a different model
run. Certainty: abstract "low for metformin" (H10-c3) vs text "from low … to high … most other comparisons rated as
moderate" (H10-c8). Against: Griffin/Li/Shi non-significant (H04-c1, H05-c1, H08-c2). *Reason:* Silverii's metformin
node = 4 old, small trials (H10-c2, H10-c7) with RoB concerns concentrated there (H10-c5) and the only significant
inconsistency is metformin vs SGLT2i (H10-c6). *Decision (L-005):* cite the **main-text** value OR 0.68 (0.51–0.92),
mention that the abstract reports 0.69 (0.53–0.89), and keep [GRADE Low]. **Steelman:** this is the only synthesis
restricted to adjudicated MACE in ≥40-week trials — the outcome definition most relevant to the question.

**C3 · Li 2021 "combination harm" vs NMAs (A2, A6).** Add-on metformin: ACM RR 1.49, CV death RR 2.21 (H05-c2) vs no
class differences in dual/triple therapy (M03-c2) and no meaningful differences on metformin background in low-risk
patients (M01-c1). *Reason:* the combination signal rests on 4 insulin-background + 1 SU + 1 dapagliflozin studies
(H05-c4) with UKPDSb (metformin added to SU, 1990s) carrying 23.22%/25.76% weight (H05-c3); Li's search was 2 DBs
(RoB high). Minor internal inconsistency: Li gives UKPDS weight in the main ACM analysis as 50.64% in Results and
50.63% in Limitations (H05-c5). *Resolvable by quality* → treat as a hypothesis-generating signal [GRADE Very low].
**Steelman:** UKPDS itself reported the SU+metformin excess and the signal survived pooling with insulin trials.

**C4 · Lambourg 2024 abstract vs main text (A5).** Abstract: 63.7% vs 70.5%, HR 1.26 (1.10–1.44) (H12-c1);
main-text Results (CCW, after confounding adjustment): 70.3% vs 63.4%, HR 1.23 (1.08–1.41) (H12-c3). Same direction
and significance; magnitude differs slightly. *Decision (L-005):* cite main-text HR 1.23 and note the abstract value.

**C5 · eGFR <30: guidelines vs target-trial emulation vs acidosis signal (A5) — decisive controversy.**
Guideline side (on disk): metformin "contraindicated with eGFR<30 … and with dialysis" (M12-c2); NICE (as reported by
Lambourg) "neither be initiated nor continued" below 30 (H12-c7); FDA label as summarised by M12 (M12-c5). Evidence
side: stopping associated with higher mortality, MACE unchanged (H12-c1…c3); advanced-CKD MA NS (M04-c2); but acidosis
aHR 2.07 at eGFR<30 (S01-c2) and a non-significant stage-4 lactic-acidosis trend (H11-c2). *Reason:* all patient-level
data are observational; Lambourg's cohort are *prevalent* users with assumed doses, 44.2% on SU (H12-c5), and stopping may
mark clinical decline (confounding). **Steelman (for continuation):** a nationwide TTE with MSM sensitivity analysis
found consistent excess mortality on stopping with no MACE explanation, and pharmacokinetic data support 500 mg/day at
stage 4 (M06-c1/c2). **Steelman (for stopping):** the only direct acidosis estimate at eGFR<30 doubles risk (S01-c2),
and no RCT exists. **Not resolvable** with current evidence → present both; the writer must not imply that continuing
below 30 is recommended. [GRADE Very low both ways.]

**C6 · XR vs IR GI tolerability (A4).** RCT synthesis: no difference (HbA1c MD 0.04%; any GI AE RR 1.09) (M11-c1/c2);
vs meta-regression (IR more diarrhoea, p=0.0437; H13-c4) and observational (XR lower for bloating/pain/constipation/
vomiting, diarrhoea NS p=0.0951; M10-c2). *Reason:* 5 small RCTs vs study-level ecological meta-regression. Both
agree XR is not worse and improves compliance (M11-c3). [GRADE Low]

**C7 · Discontinuation for adverse events (A4).** No excess vs all controls (RR 1.080; H13-c5) vs withdrawal for
intolerance RR 2.19 vs placebo in CKD (H14-c3). *Reason:* active comparators (DPP-4i, GLP-1 RA, SGLT2i) also cause
AEs; CKD population; different outcome definitions. [GRADE Low]

**C8 · Cirrhosis: harm signal vs benefit-suggesting literature; within-study inconsistency (A5).** Compensated
cirrhosis: ACM aHR 1.13, decompensation 1.15 (S02-c1), dose-dependent (>1000 mg/d aHR 1.42; S02-c2); but in the
IPCW model mortality was not significant (store; table value, not carded) while decompensation stayed elevated. The
authors themselves cite smaller cohorts suggesting benefit (not in the approved corpus). Unmeasured alcohol use and no
Child-Pugh/MELD (S02-c3). [GRADE Very low]

**C9 · Metformin vs sulfonylureas, CV mortality (A2).** AHRQ: lower CV mortality with metformin (H07-c3) vs Cochrane:
4 vs 8 CV deaths and 31 vs 31 deaths, very low certainty (H06-c2). *Reason:* AHRQ pools RCTs+observational; Cochrane
RCTs ≥1 y only. [GRADE Low]

**C10 · First-line position: metformin vs organ-protective agents from diagnosis (A6) — decisive controversy.**
AHRQ 2016 supports metformin first-line (H07-c5); Palmer 2016 "consistent with ADA recommendations" (M03); ADA/KDIGO
2022: metformin + SGLT2i early in CKD (M12-c8) but SGLT2i without metformin "may be reasonable" in defined cases
(M12-c7); ADA/EASD 2026 abstract advocates SGLT2i and/or GLP-1-based therapy "potentially from diagnosis" without
stating metformin's place (H01-c1). Evidence: SGLT2i/GLP-1 RA reduce ACM (High; H08-c3) — but largely on metformin
background (M01-c1/c2). Level III framing: M18-c1. **Steelman (against mandatory metformin-first):** metformin's own
hard-outcome evidence is Low (C1/C2) while newer classes have High-certainty organ protection; requiring metformin
first adds a step without proven outcome benefit. **Steelman (for metformin-first):** no trial shows SGLT2i/GLP-1 RA
*without* metformin beats metformin-first; cost/access matter in Vietnam (AR-2). The writer must not state what the
2026 ADA/EASD or ADA SOC documents say about metformin (Absent on disk).

---

## 5. Evidence gaps (for Discussion / Limitations)
1. **No adequately powered modern CVOT** of metformin vs placebo/no metformin in T2D (H04-c2, H04-c6; registry note in store: VA-IMPACT is prediabetes, completes 2029).
2. **Older adults (≥65): Absent.** Trials in H04 were mostly ≤65 y; only indirect data from Lambourg (median 77, eGFR<30; H12-c4).
3. **Heart failure population and hepatic impairment:** HF none; cirrhosis one Taiwanese cohort (S02).
4. **eGFR <30:** no RCT of continue vs stop (H12-c6, H14 conclusions).
5. **Head-to-head first-line metformin vs SGLT2i/GLP-1 RA on hard outcomes** in drug-naive patients: none in corpus.
6. **Lactic acidosis incidence** with adjudicated outcomes: none (S01 uses ICD acidosis code).
7. **Vietnamese/Asian efficacy and CV data:** none; local data only B12 prevalence (M09, M14) and prescribing (M19).
8. **B12 screening interval / when to start:** unknown (M07-c3).
9. **Current guideline text** (ADA SOC 2026 s9, ADA/EASD 2026, KDIGO 2022 primary) not on disk; NICE NG28 and FDA not in store.
10. **Long-term durability of glycaemic control** and microvascular outcomes: insufficient (H07-c3, H07-c6).

---

## 6. Assumption Register (→ Limitations, Law 5)
| # | Assumption / extrapolation | Where it bites |
|---|---|---|
| AR-1 | Trial and cohort results (mostly ≤65 y) apply to older adults; no dedicated ≥65 evidence. | A1–A5 |
| AR-2 | Effects estimated in mainly white Western / Scottish / Korean / Taiwanese populations apply to Vietnamese patients; local data cover only B12 and prescribing. | all axes |
| AR-3 | ADA/KDIGO 2022 (M12) eGFR thresholds are still current; the 2026 ADA SOC / ADA/EASD texts could not be read and may have changed them. | A5, A6 |
| AR-4 | KDIGO 2022 Rec 4.1.1, FDA label and NICE positions are taken second-hand (via M12 and Lambourg H12), not from the primary documents. | A5 |
| AR-5 | UKPDS-era trials (1970s–1990s) are informative for current practice (H04, H05, H10 metformin node). | A2 |
| AR-6 | Hospitalisation with ICD-9 276.2 acidosis is a valid proxy for metformin-associated lactic acidosis (S01). | A4/A5 |
| AR-7 | El-Damanawi (4/11 trials ADPKD) results generalise to T2D with CKD. | A5 |
| AR-8 | Nabrdalik 2022 GI estimates apply to adults (one paediatric study; exclusion did not change results, H13-c6). | A4 |
| AR-9 | Peri-PCI data (S03; not T2D-restricted, mostly eGFR >30) inform lactic-acidosis risk in T2D generally. | A4 |
| AR-10 | Abstract-only appraisals (9/16 HIGH) are representative of the full papers; values provisional (L-005, L-043). | all |
| AR-11 | NCBI PMC XML renders the version of record faithfully (locks prove presence in NCBI text only). | cards |
| AR-12 | Taiwanese 2000–2009 cirrhosis cohort reflects current practice and other populations (S02). | A5 |
| AR-13 | Silverii's class-level metformin node (4 trials) represents metformin's effect. | A2 |
| AR-14 | Landmark pre-reads: none qualifying in the approved set; orientation from ADA/KDIGO 2022 consensus full text (M12) and the Research Map; M18 cited as Level III only where a direct framing claim is drawn. | structure |
| AR-15 | Korean NHIS B12 outcome (diagnostic code or B12 prescription) approximates biochemical deficiency (M08). | A4 |
| AR-16 | Lalau's dose regimen (small PK studies, N not reported) generalises to routine care (M06). | A5 |

---

## 7. Per-claim strength labels for the writer
Carry the label into the draft; cite only claims backed by an accepted card (IDs shown).
| # | Claim (short) | Label | Cards |
|---|---|---|---|
| 1 | Metformin lowers HbA1c at least as much as other oral classes | **[GRADE: Moderate]** | M03-c1, H07-c1 |
| 2 | Weight neutral/modest loss vs gain with SU/TZD/insulin | **[GRADE: Moderate]** | H07-c2 |
| 3 | Low hypoglycaemia; SU and insulin carry the excess | **[GRADE: Moderate]** | M03-c3, H08-c4 |
| 4 | No proven reduction in all-cause mortality vs placebo/no drug | **[GRADE: Low]** | H04-c1, H05-c1, H08-c1, H06-c4 |
| 5 | Possible MACE reduction (Silverii OR 0.68, main text) — 4 old trials | **[GRADE: Low]** | H10-c2, H10-c3, H10-c7 |
| 6 | No effect on CV death / HF admission shown | **[GRADE: Low / Very low]** | H04-c1, H05-c1, H08-c5 |
| 7 | Observational CV/mortality benefits likely confounded | **[GRADE: Very low]** | M05-c2, M05-c3, M04-c1 |
| 8 | "Combination harm" signal driven by UKPDSb | **[GRADE: Very low]** | H05-c2…c5 |
| 9 | GI AEs common (diarrhoea RR ~2.4; incidence ~13% in RCTs) | **[GRADE: Moderate]** | H13-c1, H13-c2 |
| 10 | XR at least as well tolerated as IR, better adherence | **[GRADE: Low]** | M11-c1…c3, H13-c4, M10-c2 |
| 11 | B12 deficiency dose/duration-dependent; VN prevalence 18.6–22.1% | **[GRADE: Low]** | M07-c2, M09-c1/c2, M14-c1 |
| 12 | PPI co-use raises B12 deficiency risk | **[GRADE: Low]** | M08-c1 |
| 13 | No excess acidosis at eGFR ≥30 | **[GRADE: Low]** | S01-c1, S03-c1, M12-c5 |
| 14 | Acidosis signal at eGFR <30 | **[GRADE: Very low]** | S01-c2, H11-c2 |
| 15 | Guideline/consensus: use if eGFR ≥30, 1,000 mg/d at 30–44, contraindicated <30 (ADA/KDIGO 2022) | consensus statement — cite **M12**, not graded | M12-c1, M12-c2 |
| 16 | Stopping at eGFR <30 associated with higher mortality (HR 1.23, main text) | **[GRADE: Very low]** | H12-c3, H12-c2 |
| 17 | Death vs placebo in CKD RCTs: little/no difference | **[GRADE: Low]** | H14-c2 |
| 18 | Compensated cirrhosis: harm signal, dose-dependent | **[GRADE: Very low]** | S02-c1, S02-c2 |
| 19 | Older adults: no direct evidence | **Absent** — write "No direct evidence found; this is inference." | (H12-c4 indirect) |
| 20 | SGLT2i/GLP-1 RA reduce mortality on top of standard care | **[GRADE: High]** | H08-c3, M01-c2 |
| 21 | Replacing metformin first-line with SGLT2i/GLP-1 RA improves outcomes | **[GRADE: Very low]** (indirect) | M01-c1, M12-c7, H01-c1 |
| 22 | ADA/EASD 2026 advocates earlier SGLT2i/GLP-1 "potentially from diagnosis" | report verbatim as consensus framing; metformin's 2026 position **not on disk** | H01-c1, H01-c2 |

**Do not cite:** H02 and H03 for any metformin-specific statement (no text on disk); M02, M13, M17 (dropped);
any number not on an accepted card (e.g., Lambourg respiratory death HR, Yen IPCW mortality) unless the lead asks for
an extra card; the `abstract` fields of `02b_records.jsonl` (agent summaries for 8 records).

---

## 8. Must-mention for the synthesis-writer (handoff)
- Controversies to put under "Ongoing controversy": **C1/C2 (CV benefit), C5 (eGFR <30), C10 (first-line)**; also C3.
- Report Silverii and Lambourg with the **main-text** values and name the abstract discrepancy (L-005).
- Decompose MACE (L-010): MI favourable but NS; stroke null; CV death null.
- Older adults and HF populations: explicit "no direct evidence" statements.
- Guideline section: only ADA/KDIGO 2022 (M12) text is on disk; ADA/EASD 2026 only its abstract framing.

---

## 9. Provenance & tooling notes (for the verifier and the lead)
- Store PMIDs/DOIs were cross-checked implicitly: every fetched XML carries the same PMID as the store entry
  (IDENTITY lock passed for all 33 studies represented on cards; H02 and H03 have no cards).
- `extract_numbers.py` CI bucket empty (store CI format) — candidate harness fix (§11).
- `verify_quotes.py` exit 0; 104/104 accepted (two drafted M12 cards quoting Table 1/Table 3 cells were withdrawn before the final run to respect the prose-only rule, not because a lock failed); negative controls rejected (FULLTEXT, IDENTITY, NUMBER).

## 10. Re-invocation note
If the corpus changes (e.g., full text of H01/H02/H03 supplied), re-appraise only the affected axes (A5, A6) and
regenerate 04a–04c; everything numbered above 04 becomes stale.

## 11. Lesson candidates (for the lessons-curator; not applied)
1. The retriever must store the **verbatim** MCP/PubMed abstract in `02b_records.jsonl`, never a summary; 8 records
   held agent-written text in the `abstract` field.
2. When MCP returns empty PMC bodies, try direct NCBI E-utilities (`efetch db=pmc`) via a script before declaring
   full text unavailable — machine text on disk makes the quote locks meaningful.
3. `extract_numbers.py` misses CIs written "x (a-b)" without a "CI" token; either the store format or the regex should change.
4. The evidence-appraisal skill names no RoB tool for systematic reviews (ROBIS/AMSTAR 2); one should be specified.

## 12. Questions for the lead / user (Gate 4b)
- **Q1.** Accept the 56 machine-fetched NCBI files placed in `source/metformin-t2d/` (the directory contract calls
  `source/` user-supplied), or move them to `_workspace/`? The quote locks depend on them.
- **Q2.** Supply PDFs/text for ADA SOC 2026 s9 (H02), ADA/EASD 2026 (H01) and KDIGO 2022 (H03)? Without them the 2026
  guideline position of metformin stays "not on disk" and A6 stays Thin.
- **Q3.** No qualifying landmark review exists in the approved set; proceed without one (current plan), or re-open the
  gate to add one?
- **Q4.** Confirm ROBIS-lite as the SR risk-of-bias approach (the skill's tool table has no SR tool).

---

## 13. Gate 4b — user decisions (2026-10-27, lead-recorded verbatim; asked before and separately from the gate question, L-044)
- Q1 machine-fetched NCBI files: **"Giữ ở source/ kèm nhãn (Recommended)"** → keep `source/metformin-t2d/` with `_PROVENANCE.md`; directory-contract tension goes to Phase 7 lesson proposals.
- Q2 guideline PDFs: **"Không, dùng ADA/KDIGO 2022 (Recommended)"** → guideline section uses M12 full text + H01 abstract framing; declared in Limitations.
- Q3 landmark review: **"Không cần (Recommended)"**.
- Q4 SR risk-of-bias tool: **"Đồng ý ROBIS rút gọn (Recommended)"**.
Gate 4b approval: pending (asked separately).
- **Gate 4b — CLEARED.** Gate-closing question asked alone: "Gate 4b: Có muốn điều chỉnh gì trước khi viết bài không? Anh có duyệt kết quả thẩm định … để tôi chuyển sang Phase 5 viết bài không?" User's answer (verbatim): **"Duyệt, tiếp tục"**.
