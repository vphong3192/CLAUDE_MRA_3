# Verification Report — Ablation Metrics in RF-PVI for Atrial Fibrillation

> **Verifier (QA) output.** Date: 2026-06-14 · Inputs: `04_draft_review.md`, `reference/af-ablation-metrics-pvi-rf.md` (the ONLY authorised source store), `03_appraisal.md` (GRADE + §7 language guardrails).
> **Constitution binding:** Law 1 (no fabricated citation → auto-fail/BLOCK), Law 3, Law 4, Law 5. Lessons applied: L-001/002/003/006/007/009/010/011.
> **Verification method note (process limitation):** Independent PubMed re-fetch (`get_article_metadata`) was **permission-denied this run** — the same egress constraint the retriever documented in the store. Each PMID was title-confirmed by the retriever at capture, and **10 load-bearing records are full-text-confirmed** in `source/af-ablation-metrics/` (HTML+PDF). I directly re-verified the most consequential numbers against those full texts (see below). I could not independently re-resolve PMIDs; this is recorded in the audit, not treated as a fabrication.

---

## Citation map (draft [n] → store [Axxx] → PMID)

| Draft | Store | PMID | Draft | Store | PMID |
|---|---|---|---|---|---|
| [1] Taghji | A001 | 29600792 | [15] Lian/Lyan | A028 | 38995604 |
| [2] Phlips | A002 | 29315411 | [16] Natale/SMART-AF | A015 | 25125294 |
| [3] Ioannou | A007 | 32862230 | [17] Reddy/TOCCASTAR | A016 | 26260733 |
| [4] Hussein 2017 | A003 | 28639728 | [18] Ullah | A017 | 27173976 |
| [5] PRAISE | A004 | 30354288 | [19] Martin | A021 | 29858882 |
| [6] Chen/FAFA | A005 | 31588620 | [20] Masuda | A023 | 32671932 |
| [7] Dhillon | A006 | 30556609 | [21] Solimene/CHARISMA | A024 | 33851484 |
| [8] Kanamori | A009 | 30176083 | [22] Szegedi | A025 | 34529678 |
| [9] Mattia | A008 | 29988268 | [23] Fukaya | A026 | 36378816 |
| [10] Katić | A010 | 34453647 | [24] Lepillier | A027 | 37476572 |
| [11] Cai 2022 | A011 | 35463774 | [25] Perge | A029 | 39373571 |
| [12] Cai 2023 | A013 | 36640429 | [26] Harada | A033 | 41517933 |
| [13] Prasad | A012 | 36340486 | [27] Nair | A034 | 38204461 |
| [14] Kuo | A014 | 40599722 | [28] Arai | A035 | 39188036 |
| [29] Chinitz/SMART-SF | A018 | 29016769 | [32] 2024 ESC/EACTS | A030 | 39210723 |
| [30] Mansour/PRECEPT | A019 | 32819531 | [33] 2023 ACC/AHA | A031 | 38033089 |
| [31] Lo/TactiSense | A020 | 33812831 | [34] 2017 HRS consensus | A032 | 29021841 |

Every inline citation resolves to a real store record with a PMID. No citation points to an UNCONFIRMED record. **A022 (Segreti) is not cited; Pedersen is not cited.**

---

## Claim × Source cross-check (by section)

| § | Claim (abridged) | Cite | Store check | GRADE/language | Verdict |
|---|---|---|---|---|---|
| 1 Abstract | No RCT of any index (AI/LSI/LID/AID) vs conventional; only 2 RCTs test CF availability, both negative at 12 mo | — | Matches appraisal cardinal message + A016/A017 | Correct framing; LOW/VERY-LOW lead | PASS |
| 1 Abstract | AI/LSI "dường như liên quan đến" first-pass↑/recurrence↓ at LOW; LID "liên quan đến" durable acute lesions, clinical data VERY LOW | — | Matches GRADE O1/O2 | Associative, LOW/VL — correct | PASS |
| 3 | %AID ~%voltage-drop R²=0.785; ex-vivo volume R²=0.711 | [26] | A033 full-text confirmed | mechanism, attributed | PASS |
| 3 | FTI gap vs no-gap 140.5±54.5 vs 232.4±121.4 g·s, P<0.0001; AUC FTI 0.774 vs LSI 0.724, P=0.21 | [8] | A009 exact (full-text confirmed) | acute surrogate | PASS |
| 4.1 | CLOSE AI ≥400 post/≥550 ant + ILD ≤6 mm; pilot n=130; first-pass 98%, adenosine-proof 98%; 12-mo KM 92.3%; 40% (105/260) circles posterior AI400 not reached | [1] | A001 exact (full-text confirmed) | descriptive | PASS |
| 4.2 | Phlips CLOSE vs CONV-CF n=100: first-pass 98% vs 54%; adeno-proof 97% vs 82%; 12-mo 94% vs 80%; proc −30%, RF −50%; OR 3.917 (CI 1.008–15.220) | [2] | A002 exact (full-text confirmed); draft correctly flags CI lower bound barely >1 | LOW; historical control noted | PASS |
| 4.2 | Hussein AI vs PSM-CF (89 vs 89): first-pass 97% vs 84%; PVR 6% vs 13% (P=0.02); recurrence 17% vs 37% (P=0.002); impedance drop 13.7 vs 8.8 Ω | [4] | A003 exact | associative | PASS |
| 4.3 | Ioannou meta 11 studies n=2306; first-pass 93.4% vs 62.9% (OR fail 0.09, CI 0.04–0.21, I²=58%); PVR 18% vs 35% (OR 0.37, CI 0.18–0.75, I²=0); relapse 11.8% vs 24.9% (OR 0.41, CI 0.25–0.66, NNT 7.6); all inputs non-RCT, authors "low–moderate quality" | [3] | A007 exact (full-text confirmed) | LOW; "không thể vượt quá độ chắc chắn của đầu vào" — correct | PASS |
| 4.3 | PRAISE n=40: PVR at remap 22% pts (7% PVs); 95% SR at 12 mo | [5] | A004 exact | descriptive | PASS |
| 4.4 | No AI-vs-conventional RCT; A002/Dhillon use historical controls; Dhillon PVR 14% vs 24% P=0.015 but 12-mo 78% vs 64% P=0.186 NS; AI GRADE LOW; "dường như liên quan", NOT "làm giảm" | [2,7] | A006 exact; explicit null reported (L-006) | LOW; associative, contradiction surfaced | PASS |
| 5.1 | LSI thresholds dispersed: Kanamori 4.05 (sens 63.4/spec 76.3), ~5.2 target, <3.95 posterior; Mattia 5.5–6/5–5.5; Katić 6.5/5.2; Cai 4.35–4.7/3.95–4.3; Prasad regional EU4.4/JP4.5/US5.5 | [8,9,10,11,12,13] | A009/A008/A010/A011/A013/A012 — all match | heterogeneity (L-006/§4.5) | PASS |
| 5.2 | Mattia 89.3% vs 65.6% (P=0.037), n=60 retro control; Prasad n=143 95.7%/12mo; Kuo HP-LSI recurrence 14.9% vs 32.5% (HR 0.36, CI 0.16–0.83) | [9,13,14] | A008/A012/A014 — all match; draft flags small N / wide CI | LOW; associative | PASS |
| 5.3 | Lian LSI vs LID head-to-head: RF 25 vs 30 min (P=0.035); first-pass 87% vs 61% (P=0.002); gaps 42% vs 74% pts (P=0.016); recurrence KM 16.1% vs 34.3% (P=0.037) vs Table-2 P=0.09; **LID arm had NO CF sensing**; retrospective, persistent AF | [15] | A028 exact (full-text confirmed); confound + internal stat inconsistency both stated | VERY LOW; "không đủ để kết luận" — correct | PASS |
| 5.4 | No LSI RCT; no AI-vs-LSI head-to-head any design; GRADE LOW | — | Matches appraisal A7 | LOW; associative | PASS |
| 6.1–6.2 | CF only metric with RCTs; TOCCASTAR non-inferiority 67.8% vs 69.4% (NI not superior); optimal-CF subgroup post-hoc 75.9% vs 58.1% (P=0.018); Ullah PVR 22% vs 32% (P=0.03), 12-mo 49% vs 52% (P=0.9); CF/application equal; in-target 80% vs 68% | [17,18] | A016/A017 exact (both full-text confirmed; I re-read full text) | MODERATE (negative) | PASS |
| 6.3 | SMART-AF cohort: in-target CF ≥80% time → 4.25× success (P=0.0054); resolved as post-hoc stability subgroup in non-RCT vs RCT-negative availability; "chứng minh" used ONCE for the null/acute RCT result | [16,17,18] | A015 exact; uses the single permitted "demonstrates" per appraisal §7 | MODERATE for null; LOW for stability — correct | PASS |
| 6.4 | CF non-discriminative (Szegedi); weak CF↔LID r=0.14 (Lepillier); CF = necessary-but-insufficient input | [22,24] | A025/A027 exact | LOW; associative | PASS |
| 6.4 (added) | SMART-SF acute 96.2%/AE 2.5%; PRECEPT KM 61.7%/15mo; TactiSense 82.2%/12mo — single-arm benchmarks | [29,30,31] | A018/A019/A020 exact | descriptive benchmark; non-comparative noted | PASS (FIX applied) |
| 7.1 | LID via DirectSense/STABLEPOINT vs global impedance; Martin first-in-human LI drop 14.6 vs 6.8 Ω (P=0.049) | [19] | A021 exact | descriptive | PASS |
| 7.2 | Masuda gap LI half (12±7 vs 23±12 Ω, P<0.001), GID NS, cutoff 13.4 Ω (sens 0.78/spec 0.75); Szegedi 21.8/18.3 Ω; Fukaya 20.0 Ω/11.6%; Lepillier n=212 first-pass 93.3%/vein, 22.1±9 vs 14.4±5 Ω, >21/>18 Ω; Perge 161→150→141, <9 Ω@4s OR 3.82 | [20,22,23,24,25] | A023/A025/A026/A027/A029 — all match (A027 full-text confirmed) | LOW (acute) | PASS |
| 7.3 | Solimene CHARISMA n=153: acute 100%, 0 major, recurrence 11.8% → AF 6.5%/AT 4.6%/both 0.7% (L-010 decomposed); AUC LID 0.806 vs GID 0.582; OR 3.13/5Ω (CI 2.7–3.6) | [21] | A024 exact (I re-verified full text: 11.8/6.5/4.6/0.806/0.582/3.13 all confirmed) | VERY LOW clinical; composite decomposed | PASS |
| 7.4 | LID newest/least-standardized; thresholds 15–21.8 Ω; mostly acute surrogate; 12-mo VERY LOW; "không đủ để kết luận" | [21,22,23,24,15] | matches appraisal A4 | VERY LOW — correct | PASS |
| 8 | TactiFlex SE no native AI/LSI; AID surrogate; Harada gap %AID 7.2±1.7 vs 9.6±3.1 (P<0.0001); cutoff ≥9% (ROC 9.33%); AUC 0.761 vs unfiltered 0.627 (P<0.05); single-arm n=30 1-yr 82% (4/30); Nair pivotal n=334 72.9%, HP 76.4% vs LP 66.8%; Arai tamponade 1.1% vs 0.2% (OR 4.8) — catheter-specific, confounded | [26,27,28] | A033/A034/A035 — all match (A033 full-text confirmed) | VERY LOW; Arai correctly framed as platform-specific not metric | PASS |
| 8 | AutoMark Index: no peer-reviewed literature, not confirmed, future direction only | — | No store record → Law 1 "no source found" treatment | correct | PASS |
| 9 (HPSD) | Chen 50W 92% first-pass, 6-mo; Dhillon −22%/−37%; Cai 4.35 (2022)/87.1% 2-yr SP 1.6% (2023); Kuo HR 0.36; TactiFlex HP 76.4% vs 66.8% | [6,7,11,12,14,27] | A005/A006/A011/A013/A014/A034 — all match | LOW; associative | PASS |
| 10.1 | Consensus items anchored to 2024 ESC [32], 2023 ACC/AHA [33], 2017 HRS [34]; CLOSE targets reference convention | [1,2,3,17,18,20,21,22,24,6,11,12,32,33,34] | guideline records A030/A031/A032 exist | consensus stated plainly (safe per appraisal) | PASS (FIX applied) |
| 10.2 | Controversies: CF availability RCT-neg vs cohort-pos; LSI threshold range; LID-vs-LSI confounded; AID lacks long-term data | [17,18,16,9,10,11,13,15,26,27] | matches appraisal §4 | balanced, both sides | PASS |
| 11 Limitations | 2 RCTs both CF; no AI/LSI/LID RCT; 25/35 abstract-derived; Segreti & Pedersen UNCONFIRMED → not cited; threshold heterogeneity; no Vietnam data; preprint sweep incomplete; PFA not in corpus | [17,18] | matches appraisal §6; L-009 honoured | complete (Law 5) | PASS |
| 12 Conclusion | Composite metrics "dường như liên quan" LOW(AI/LSI)–VERY LOW(LID/AID); strongest conclusion is the MODERATE negative CF result; 5 research gaps | [17,18] | matches GRADE summary | correct certainty hedging | PASS |

**Total inline citations checked: all of [1]–[34]. Verdict: 0 BLOCK, 0 pending FIX (1 FIX applied), all PASS.**

---

## Special checks (from QA brief)

- **A022 (Segreti) NOT cited:** CONFIRMED — absent from text and reference list. PASS.
- **Pedersen NOT cited:** CONFIRMED — appears only in §11 Limitations, named as UNCONFIRMED and explicitly excluded (L-009). PASS.
- **Composite endpoints decomposed (L-010):** CONFIRMED — §7.3 decomposes Solimene 11.8% into AF 6.5%/AT 4.6%/both 0.7% with the explicit caveat not to imply AF-specific prevention. PASS.
- **Observational → associative language (L-007):** CONFIRMED — cohort findings use "liên quan đến / dường như liên quan đến"; causal/"làm giảm/chứng minh" used only for RCT-backed CF acute+null results, exactly as permitted by appraisal §7. PASS.
- **GRADE LOW → "may/suggests" not "demonstrates" (L-002):** CONFIRMED — AI/LSI (LOW) and LID/AID (VERY LOW) consistently hedged; the one "chứng minh" is the appraisal-sanctioned MODERATE negative CF conclusion, and the draft self-flags it. PASS.
- **Preprint honesty:** No preprint is cited as evidence; corpus is peer-reviewed PMIDs + guidelines. AutoMark explicitly flagged as not-yet-in-literature. PASS.

---

## Completeness check

- **All 12 sections present:** YES (1 Abstract → 12 Conclusion + research gaps).
- **Abstract accurate:** YES — leads with the no-RCT cardinal message and correct LOW/VERY-LOW certainty; the single MODERATE cell (negative CF) is reflected.
- **Controversy section present & balanced (Law 4):** YES — §10.2 lists 4 controversies, each with both sides + methodological reason.
- **Limitations complete (Law 5):** YES — §11 covers search/evidence scope, no-RCT, abstract-derived provisional records, threshold heterogeneity, no-Vietnam-data, incomplete preprint sweep, PFA-as-inference.
- **Reference list PMID for every entry:** YES — all 34 entries carry a PMID; numbering contiguous 1–34; Vancouver style consistent.
- **Orphan references:** RESOLVED — refs 29–34 were listed but uncited in the draft; FIX applied (now cited in §6.4 and §10.1). No orphan or dangling citation remains.

---

## Rubric scores

| Criterion | Score | Justification |
|---|---|---|
| C1 Law 1 compliance (no fabricated citations) | **1.0** | Every [1]–[34] resolves to a real store record with PMID. UNCONFIRMED records (A022/Pedersen) not cited. Load-bearing numbers re-verified against full text. No fabrication. |
| C2 Citation accuracy (claim ↔ source) | **1.0** | All sampled numbers match the store (and full text where available) exactly — TOCCASTAR, Ullah, Ioannou, Solimene, Phlips, Hussein, Kuo, Harada all verbatim. |
| C3 GRADE language consistency (L-002) | **1.0** | Verb strength matches every GRADE cell; the sole "demonstrates" is the appraisal-permitted MODERATE negative. |
| C4 Evidence hierarchy respected (Law 3) | **1.0** | RCTs (CF) vs cohorts correctly tiered; meta-analysis explicitly capped at its non-RCT inputs; cohort-positive does not override RCT-negative. |
| C5 Consensus vs controversy separated (Law 4) | **1.0** | §10.1/§10.2 cleanly split; both sides of each controversy preserved with a methodological reason. |
| C6 Limitations complete (Law 5) | **1.0** | §11 thorough; ties to Assumption Register; honest about provisional records and the PFA gap. |
| C7 Research gate cleared | **1.0** | User reply quotable: **"tiếp tục quy trình nghiên cứu"**, answered all Research Map questions, and uploaded the 10 source PDFs (present in `source/af-ablation-metrics/`). Gate cleared after the map was shown. |
| C8 Provenance on disk | **1.0** | Writer cited ONLY from `reference/af-ablation-metrics-pvi-rf.md`; 10 records full-text-backed in `source/`. |
| C9 Scope served | **1.0** | Research/academic depth for interventional EP audience; Vietnamese with English terms in parentheses — matches confirmed scope. |
| C10 Completeness (all sections/metrics) | **0.9** | All 12 sections + all 5 metric families (AI/LSI/LID/CF/AID) + HPSD covered. Minor: guideline bodies were retrieved but were only thinly integrated until the FIX; even now they anchor consensus rather than being discussed substantively. |

**Weighted mean (equal weights): 9.8 / 10 = 0.98.**
**Band: EXCELLENT (≥0.90).**
No AUTO-FAIL trigger (no fabricated citation; gate cleared).

---

## Audit checklist

- [x] **Law 1 — no fabricated citation.** All inline cites resolve; UNCONFIRMED records excluded. PASS.
- [x] **Law 2 — scope confirmed before writing.** Phase-0 purpose/depth/audience/language confirmed; quotable user approval exists. PASS.
- [x] **Law 3 — hierarchy used correctly.** RCT > cohort enforced; meta-analysis capped at inputs. PASS.
- [x] **Law 4 — controversy present & balanced.** §10.2. PASS.
- [x] **Law 5 — limitations complete.** §11. PASS.
- [x] **Research Map gate — cleared with quotable approval.** User: "tiếp tục quy trình nghiên cứu" + answered all map questions + uploaded PDFs, received after the map was shown (satisfies L-014; no self-clear). PASS.
- [x] **Provenance — cited only from store.** PASS.
- [x] **source/ folder listed & checked.** Exists with 10 HTML+PDF pairs (+ converter + .gitkeep); used for the 10 full-text-confirmed records (L-012). PASS.
- [x] **UNCONFIRMED records — A022/Pedersen not cited.** PASS.
- [~] **PROCESS NOTE (not a law breach):** Independent PubMed PMID re-resolution was permission-denied this run. Mitigation: retriever title-confirmed every PMID at capture; verifier re-read full text for the 10 highest-stakes records and confirmed all load-bearing numbers verbatim. Recommend re-granting PubMed metadata permission for future runs so QA can re-resolve PMIDs end-to-end.

**Law-compliance: 6/6 PASS. Gate: cleared. Scope integrity: intact.**

---

## Fix list

| # | § | Type | Issue | Correction | Status |
|---|---|---|---|---|---|
| F1 | Refs 29–34 | FIX (format/completeness, Vancouver + L-011) | Six reference-list entries (3 CF-catheter benchmarks + 3 society guidelines) were present in the list but never cited inline — orphan references; also the guideline bodies (ESC/AHA/HRS) retrieved per L-011 went unused in the text. | Added [29,30,31] to §6.4 (CF-catheter efficacy/safety benchmarks, numbers verified vs A018/A019/A020) and [32,33,34] to §10.1 (anchor the established-consensus statements to the society guidelines). | **APPLIED** |

No BLOCK items. No other FIX items.

---

## Mistake-capture (defect categories → lessons-curator)

- **Format/completeness — orphan reference entries (refs 29–34 listed but uncited).** Category: *citation-list completeness*. Recurrence-prevention candidate: writer should run an inline-vs-list reconciliation before handoff, and explicitly place the L-011 guideline citations in the consensus section (they are easy to retrieve and then forget to cite). Low severity (no fabrication; non-blocking), but the guideline omission slightly weakened L-011 coverage — worth a lesson.

(No Law-1, GRADE-language, hierarchy, contradiction, or stale-source defects found.)

---

## Final verdict

**PASS — DELIVER.**
- Overall rubric score: **0.98 — EXCELLENT.**
- BLOCK items: **none.**
- FIX items: **1, applied** (orphan references / L-011 guideline anchoring).
- `06_final_review.md` **produced** (clean final deliverable, copied after the FIX).
