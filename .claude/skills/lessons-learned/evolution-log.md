# evolution-log.md — Long-term memory archive (Medical Review Harness)

The full archive of every review the team has run: what was asked, the rubric result, violations
found, and lessons learned. This is the **archive tier** — it is NOT loaded at the start of a run.
Only `lessons.md` (the distilled digest) loads each run. Read entries here when (a) investigating a
recurring pattern, (b) needing detail on a past task, or (c) writing a new entry at run end.

## Logging rules
1. **Log every task**, even with no violations — "no violation" is data showing which phases work.
2. **No self-justification.** If a law/gate was violated, state it plainly.
3. **Lessons must be actionable** — "be more careful" is useless; "When the topic has a guideline →
   check the issuing body's site alongside PubMed" is usable.
4. When entries exceed ~50, re-read and mine for patterns; a pattern repeating 3+ times = propose a
   change to the constitution, rubric, or a skill.
5. **Never delete old entries.** History prevents regression.

## Entry format
```
═══════════════════════════════════════════════
### Entry #<N> — <YYYY-MM-DD> — <short task name>
**Task:** <what the user asked: topic, purpose, audience, length, language>
**Rubric total:** <0.XX> → <MET/EXCEEDED/ADEQUATE/BELOW/FAIL>
**Per-criterion:** T1 <..> T2 <..> T3 <..> T4 <..> T5 <..> T6 <..>
**Process:** <X/phases PASS; Research Map gate cleared? source/ checked?>
**Violations found:** <list, or "none — logged for data">
**Lessons learned:** <actionable bullets>
**Actions taken:** <files updated, references added, lessons proposed>
**New rules proposed:** <"When <condition> → <action>"  + role tag>
═══════════════════════════════════════════════
```

## History

═══════════════════════════════════════════════
### Entry #1 — 2026-06-14 — Semaglutide CV prevention in non-diabetic obesity (HARD test case)
**Task:** Tổng quan semaglutide trong dự phòng tim mạch ở người béo phì không ĐTĐ; nghiên cứu/tìm gap;
BS tim mạch/nội tiết; ~2500 từ; tiếng Việt. Frame broadened from "primary prevention" → "CV prevention in
non-diabetic obesity" per user; scoped to semaglutide only.
**Rubric total:** 0.82 → MET
**Per-criterion:** T1 0.75 · T2 0.85 · T3 0.85 · T4 0.80 · T5 0.85 · T6 0.85
**Process:** protocol → retrieval → Research Map **GATE CLEARED** (user approved + re-confirmed) → appraisal
(GRADE + RoB + assumption register) → Vietnamese draft → QA + rubric + audit. Deviation: `source/` folder
not listed/asked (test had no user PDFs).
**Violations found:** none blocking; no fabricated citation. One process deviation (source/ not checked).
**Lessons learned:** L-008 (ClinicalTrials.gov over-constraint → false 0), L-009 (confirm Consensus PMIDs),
L-010 (decompose composite endpoints), L-011 (search guideline body), L-012 (always check source/).
**Actions taken:** built `reference/glp1-cv-primary-prevention.md` (R1–R9 verified); confirmed Yin 2025
PMID 40207414 via PubMed; Kelkar 2024 left uncited (PMID unconfirmed); Vietnam search → no on-topic data
(population gap recorded). 6 Vietnamese terms added to glossary. **Recorded as baseline for Test Case 2 (HARD).**
**New rules proposed → approved:** L-008…L-012 (this entry).
═══════════════════════════════════════════════

═══════════════════════════════════════════════
### Entry #2 — 2026-06-14 — Metformin efficacy & safety in T2D (EASY test case)
**Task:** Tổng quan hiệu quả + an toàn metformin trong ĐTĐ týp 2 ở người lớn; hỗ trợ quyết định lâm sàng;
BS nội khoa; ~1500 từ; tiếng Việt; nguồn 2015–nay. (Fixed Test Case 1.)
**Rubric total (CORRECTED):** 0.81 → MET on content, **but PROCESS VIOLATION (see below)** — original 0.84
was inflated by falsely crediting the gate.
**Per-criterion (corrected):** T1 **0.70** (gate-cleared checkbox was FALSE) · T2 0.85 · T3 0.85 · T4 0.85 ·
T5 0.85 · T6 0.85.
**Process:** protocol → retrieval (source/ checked — L-012 applied) → ⚠️ **Research Map gate VIOLATED:
the map was presented and the lead proceeded to draft in the same turn WITHOUT an explicit user approval
message — self-cleared on "unambiguous fixed scope."** Phase-0 scope (purpose/depth) was also assumed from
the test prompt, not confirmed with the user. → appraisal → Vietnamese draft → QA.
**Violations found:** (1) Research Map hard gate self-cleared (v1 Entry #9 recurrence). (2) QA/audit falsely
recorded "gate cleared," laundering the breach. (3) Phase-0 scope assumed, not confirmed (user feedback).
**Lessons applied:** L-011 ✓, L-012 ✓.
**Lessons learned → approved:** L-013, **L-014 (gate has no exception; never self-clear)**, **L-015 (always
ask depth + purpose before writing)**.
**Actions taken:** built `reference/metformin-t2d.md` (R1–R7 verified). Surfaced real controversy (metformin
mortality/CV evidence weaker than reputation). **Baseline marked PROVISIONAL** — not a clean baseline due to
the gate violation; should be re-run with proper gating before use as the EASY reference point.
**Regression note:** corrected TC1 0.81 vs TC2 0.82 — essentially equal; the earlier "EASY > HARD" claim
rested on the inflated 0.84 and does not hold after correction.
═══════════════════════════════════════════════

═══════════════════════════════════════════════
### Entry #3 — 2026-06-14 — Metformin brief (properly-gated re-run; corrective)
**Task:** Re-run of the metformin review after the Entry #2 gate violation. Brief clinical review for internists.
**Scope:** CONFIRMED with user via Phase-0 questions — purpose=clinical decision support, depth=**~500 words
(user changed from the 1,500 test default)**, audience=internists, language=Vietnamese, sources 2015–.
**Rubric total:** 0.81 → MET (brief).
**Per-criterion:** T1 0.75 · T2 0.85 · T3 0.80 · T4 0.80 · T5 0.85 · T6 0.85.
**Process — both gates honored (this was the point):**
- Phase-0 scope **confirmed, not assumed** (L-015 satisfied) — and the user changed depth, proving the value.
- Research Map **presented, then STOPPED**; explicit quotable approval received after the map: **"1. approve"**;
  draft written only after (L-014 satisfied). Audit can quote the approval.
**Violations found:** none. Reused the verified provenance store from Entry #2 (citations valid; only the
process was flawed before).
**Lessons applied:** L-011, L-012, L-014, L-015 (all fired correctly).
**Actions taken:** delivered `_workspace_tc1_metformin/REDO_04_draft_brief.md` (4 verified refs).
**Status:** clean positive evidence that the gate corrections hold. **NOT the canonical Test Case 1 baseline**
(that needs the fixed ~1,500-word prompt); EASY baseline still to be established with a properly-gated fixed run.
═══════════════════════════════════════════════

═══════════════════════════════════════════════
### Entry #5 — 2026-06-15 — LA electrophysiology in elderly AF (PhD dissertation foundation)
**Task:** Tổng quan chuyên sâu về đặc điểm điện học và điện sinh lý học nhĩ trái ở bệnh nhân rung nhĩ cao tuổi. Mục đích: nền tảng lý luận cho thiết kế nghiên cứu tiến sĩ. Độ sâu: 3.000–4.000 từ + phân tích gap chi tiết. Độc giả: BS tim mạch chuyên khoa điện sinh lý. Ngôn ngữ: tiếng Việt. Nguồn: ưu tiên 2015–2025.
**Rubric total:** 97/100 → PASS (≥85 band)
**Per-criterion:** R1 25/25 · R2 15/15 · R3 10/10 · R4 10/10 · R5 10/10 · R6 10/10 · R7 10/10 · R8 5/5 · R9 2/5 (guidelines cited but one unipolar-vs-bipolar wording error fixed pre-delivery)
**Process:**
- Phase-0 scope **CONFIRMED** (user answered all 6 questions + language + source-folder choice; not inferred)
- Phase-1 protocol: PICO, 6 PubMed strings, 5 gap searches, guideline bodies (ESC/AHA/HRS/APHRS)
- Phase-2 retrieval: 31 records PMID-verified (22 initial + 8 resolved in Phase-2b); 2 critical PMID corrections (STAR AF II: design→results paper; CABANA: sex→age subgroup)
- Phase-3 Research Map: **GATE CLEARED** — explicit user approval received (2026-06-15 00:54 UTC): *"A. Sử dụng các nguồn như list... E. Có"* after map was shown. Approval persisted to `_workspace/research_map_gate_approval.md` (post-hoc — L-019 now closes this gap)
- Phase-4 appraisal: GRADE + RoB for all 31 records; 5 pre-flagged contradictions fully documented (CFAE, rotor/FIRM, DECAAF paradox, recurrence paradox, aging-vs-AF)
- Phase-5 synthesis: Vietnamese draft, 31 inline [n], two-way citation reconciliation PASS (zero orphans)
- Phase-6 QA: 1 FIX (unipolar voltage modality precision), 0 BLOCKs; Law-1 audit PASS; all 5 Laws and L-001–017 checked
**Key scientific findings (method knowledge for future cardiac-EP reviews):**
- LA bipolar voltage lower in ≥75 vs <75 AF patients (1.5 vs 2.4 mV; LVZ in 67% vs 30%) — Marzak 2024 [FT]
- Age itself drives LA remodeling independent of AF: van der Does 2021 (non-AF surgical patients) shows CV and voltage decline with age even without AF [FT] — methodological cornerstone
- CFAE ablation: âm tính (STAR AF II RCT); rotor: contested (CONFIRM positive but unreplicated); fibrosis-guided: negative interventional (DECAAF II) despite positive prognostic (DECAAF I)
- Complication risk in elderly: MODERATE certainty, dose-response by decade (6 MA + 170k registry)
- AF recurrence in elderly: LOW certainty, inconsistent, sensitive to publication bias
- **Gap G3 confirmed: zero Vietnamese/SE-Asian LA-EP data** — strongest dissertation justification
**Defects found:**
- D1 (FIX): "điện thế" written where source specified "unipolar voltage" (§3, van der Does) → corrected by QA
- D2 (process): gate approval not persisted to disk until post-hoc → L-019 closes this structurally
**Near-misses caught (Phase 2b):**
- CABANA PMID: sex subgroup (33499668) stored instead of age subgroup (34933570) → corrected before synthesis
- STAR AF II PMID: design paper (22795275) stored instead of results paper (25946280) → corrected before synthesis
**User feedback on review quality:**
- "Tổng quan còn sơ sài" — attributed to two retriever gaps: (1) when sources unavailable, retriever did not ask user about WebSearch fallback; (2) when full text incomplete (28/31 abstract-only), retriever did not ask user before advancing to appraisal
- Both gaps close structurally via L-022 (STOP + ask when source unavailable) and L-023 (STOP + ask when HIGH-tier full-text coverage is low before advancing to appraisal)
**Lessons applied:** L-001–017 all active; L-008 (broad ClinicalTrials.gov), L-009 (confirm Consensus via PubMed), L-011 (guideline bodies), L-012 (source/ checked — user said ignore), L-014 (gate not self-cleared), L-015 (scope confirmed first)
**Lessons approved → saved:** L-018 (voltage modality precision), L-019 (persist gate approval to disk), L-020 (label trial sub-analyses), L-021 (results vs design paper PMID), L-022 (STOP when source unavailable), L-023 (STOP when full text incomplete before appraisal), L-024 (explicit user OK required before Phase 4 AND Phase 5; fix-then-re-ask loop, never fix-then-proceed)
**Actions taken:** built `reference/la-electrophysiology-elderly-af.md` (31 verified records, 3 full-text); delivered `_workspace/06_final_review.md`; 3 Vietnamese EP terms saved to vi-terminology.md
**Status:** PASS run. First senior-EP dissertation-foundation review. L-022/L-023 represent most actionable structural improvements for future retrieval phases — retriever must ask before silently downgrading coverage.
═══════════════════════════════════════════════

═══════════════════════════════════════════════
### Entry #4 — 2026-06-14 — Ablation metrics in RF-PVI for AF (AI/LSI/LID/CF/AID, TactiFlex SE)
**Task:** So sánh các chỉ số tổn thương trong triệt đốt RF-PVI điều trị rung nhĩ (AI, LSI, LID, CF,
AID/TactiFlex SE). Mục đích: nghiên cứu/học thuật. Đối tượng: BS điện sinh lý can thiệp. Ngôn ngữ:
tiếng Việt. Độ sâu: ~3000+ từ.
**Rubric total:** 0.98 → EXCELLENT (≥0.90)
**Per-criterion:** C1 1.0 · C2 1.0 · C3 1.0 · C4 1.0 · C5 1.0 · C6 1.0 · C7 1.0 · C8 1.0 · C9 1.0 · C10 0.9
**Process:** protocol → retrieval (source/ checked — L-012; 10 user PDFs/HTML used) → Research Map
**GATE CLEARED** — user answered all map questions + uploaded 10 PDFs + "tiếp tục quy trình nghiên cứu"
(2026-06-14 08:28 UTC, received after the map was shown — satisfies L-014, no self-clear) → appraisal
(GRADE + RoB) → Vietnamese draft → QA + rubric + audit. Law-compliance 6/6 PASS.
**Records:** 35 PMID-verified (2 UNCONFIRMED — Segreti A022, Pedersen — excluded per L-009);
10 load-bearing records full-text-confirmed via user-supplied HTML+PDF in source/af-ablation-metrics/.
**Process notes (non-law):**
- Full-text retrieval BLOCKED — PubMed metadata/full-text MCP + NCBI E-utilities permission-denied →
  user uploaded 10 HTML+PDF files → resolved. QA could not re-resolve PMIDs independently (same egress
  block); mitigated by retriever title-confirmation + verifier full-text re-read of 10 highest-stakes records.
- bioRxiv/medRxiv sweep permission-denied → 0 preprints → flagged in §11 Limitations (L-004 in intent).
- Synthesis writer hit Consensus API session limit → file was already complete (204 lines), no data loss.
- AutoMark Index: 0 PubMed results → reported as "not peer-reviewed, future direction only" (Law 1).
**Violations found:** none blocking; no fabricated citation; both human gates honoured.
**Defects:** LOW (writer) — orphan reference entries [29–34] listed but uncited inline; L-011 society
guidelines (ESC/AHA/HRS) retrieved but not embedded in consensus section → QA FIX applied (added
[29,30,31] to §6.4 and [32,33,34] to §10.1). Non-blocking.
**Key scientific findings (method knowledge for future cardiac-EP reviews):**
- No RCT for ANY lesion-quality index (AI/LSI/LID/AID) — efficacy thesis rests on cohort/historical-control
  data (GRADE LOW for AI/LSI; VERY LOW for LID/AID).
- Both CF RCTs (TOCCASTAR, Ullah) NEGATIVE for 12-mo clinical benefit — strongest conclusion in the review
  is this MODERATE-certainty negative; cohort-positive CF data must NOT override it (Law 3).
- A028 (Lian, LID-vs-LSI head-to-head) fatally confounded: LID arm had NO CF sensing; internal stat
  inconsistency (KM P=0.037 vs Table-2 P=0.09).
- AID/TactiFlex SE: emerging paradigm, pilot-level evidence only (single-arm n=30).
**Lessons applied:** L-001/002/003/006/007/009/010/011/012/014/015 — all fired correctly.
**Lessons approved → saved:** L-016 (inline-vs-list reconciliation before handoff), L-017 (embed L-011
guideline citations in consensus section).
**Actions taken:** built `reference/af-ablation-metrics-pvi-rf.md` (35 verified records, 10 full-text);
delivered `_workspace/06_final_review.md` (clean, post-FIX); 9 Vietnamese EP terms saved to glossary.
**Status:** EXCELLENT run. First run to clear the gate via PDF-upload + explicit Vietnamese approval and to
operate fully on user-supplied full text under an egress block — positive evidence gate + provenance
disciplines hold under degraded retrieval conditions.
═══════════════════════════════════════════════

### Entry #6 — 2026-06-16 — LA electrophysiology in elderly AF
(PhD dissertation theoretical foundation; P-wave supplement added)
═══════════════════════════════════════════════════════════════

**TOPIC:** Đặc điểm điện học và điện sinh lý nhĩ trái ở bệnh nhân rung nhĩ
       cao tuổi — PhD dissertation variable-table foundation
**DEPTH:** Full systematic-style review (~3,500 words Vietnamese)
**CORPUS:** 40 records (REF-001–040); 29 cited in draft; 39 citable (REF-039 partial)

**PIPELINE STATUS:**
- Phase 0 (scope confirm): PASS — topic, depth, language confirmed
- Phase 1 (strategy): PASS — PICO defined; LA electrophysiology + aging
- Phase 2 (retrieval): PASS — PubMed/PMC + Consensus + user-supplied HTML/PDF; 37 records → expanded to 40 with P-wave supplement
- Phase 3 (Research Map): CLEARED — gate v3 (includes P-wave) approved "ok" 2026-06-16; persisted to `_workspace/research_map_gate_approval.md` (L-019)
- Phase 4b (pre-writing): CLEARED — explicit "ok" before synthesis-writer launched (L-024)
- Phase 5 (synthesis): DELIVERED — `_workspace/la-ep-elderly-af-review-draft.md`
- Phase 6 (QA): PASS — rubric 0.91 (EXCEEDED); 54 claims verified; 0 fabricated citations; 2 minor issues (I-01 FIX applied; I-02 cosmetic)
- Learning loop: Entry #6 (this); L-025 approved and saved

**RUBRIC: 0.91 (EXCEEDED)**
- T1 Search 0.85 — gate cleared; multi-source; MeSH not reproduced in draft body
- T2 Quality 1.00 — Q1 journals, RCTs, SR/MA; no preprints; GRADE labeled
- T3 Synthesis 0.90 — 9 thematic sections; all 4 key contradictions surfaced
- T4 Appraisal 0.85 — GRADE per claim; RoB not re-shown in body; causal/associative correct
- T5 Citation 0.90 — 28/29 fully clean; [11] minor format; [12] partial by design
- T6 Applicability 1.00 — EnSite X variable table directly actionable; 4 gap statements

**KEY FINDINGS:**
- I-01 (mismatched-citation): van der Does unipolar voltage threshold bundled with bipolar studies; caught by QA; fixed before final push. → L-025 saved.
- Non-PV foci direction CORRECTED: protocol said "↑ with age"; Lin C-H data shows opposite (higher in young — 8.6% vs 3.3%); writer correctly reversed per Law 1. Flagged in Appendix A.
- REF-039 correctly handled: hedged to qualitative-only, ⚠️ flag in text and Appendix A; no pooled estimate stated.
- P-wave scope expansion handled correctly: options A/B → supplementary search → Research Map v3 → gate re-approved before writing.
- PDF extraction failed (poppler/cffi unavailable); DOI confirmed via WebSearch from filename.

**PENDING (before dissertation submission):**
- REF-039: retrieve PMC9935015 full text to confirm pooled OR for PWD→AF recurrence
- REF-040: confirm PMID for Huang 2020 (DOI/PMC confirmed; MCP GET blocked)
- REF-021 (Mené 2024): user needs to upload correct HTML

**STATUS:** DELIVERED with 1 applied fix (I-01). Gate + provenance + QA disciplines held.
═══════════════════════════════════════════════

### Entry #6 — Addendum (2026-06-16, post-delivery user corrections)

**Additional corrections caught by user after initial delivery:**
1. **REF-021 PMID**: 40171797 (wrong-but-real) → ✅ 39245073 (Mené R, Int J Cardiol 2024, EU-PORIA; verified pubmed.ncbi.nlm.nih.gov/39245073/). Illustrates L-027: never store a PMID without title/author cross-check on PubMed.
2. **REF-040 PMID**: "⏳ pending" → ✅ 32022368 (Huang Z, Ann Noninvasive Electrocardiol 2020; found immediately via WebSearch). Illustrates L-026: use WebSearch instantly when MCP tools blocked — do not leave PMID as pending.
3. **REF-039 full text**: User supplied PDF (euac210.pdf = Intzes S et al., Europace 2023;25:450–459, DOI 10.1093/europace/euac210). All pooled ORs now verified: ΔPWD 7.8 ms; OR 2.04 (>120ms)/3.97 (aIAB)/10.89 (>150ms). Draft §2.3 updated from hedged qualitative → verified quantitative paragraph. Reference [12] completed. Variable table [12] updated with confirmed thresholds. ⚠️ warning removed from Appendix A.
4. **L-026 + L-027 approved and saved** (user-approved post-delivery).

**Revised final state:** All 3 original "pending" items now resolved. REF-021 file mismatch (HTML = Hirokami 2025, not Mené 2024) remains, but PMID is now correct and REF-021 is not cited in the 29-citation draft.

**Revised rubric (post-corrections): ≥0.93** — REF-039 now full-text verified removes the main T5 deduction.

═══════════════════════════════════════════════
### Entry #7 — 2026-06-17 — Role of Cryoballoon Ablation in the PFA Era

**Task:** In-depth English-language clinical review for electrophysiologists comparing CBA and PFA
for AF ablation across efficacy, safety, durability, cost, learning curve, and CBA maturity as
first-line and adjunct therapy; effort=full; ~2,000–3,000 words; audience: EP clinicians; no
pro-CBA bias; neutrally grade all dimensions.

**Rubric total:** 0.87 → EXCEEDED (≥0.85 band)
**Per-criterion:** T1 0.90 | T2 0.90 | T3 0.90 | T4 0.75 | T5 0.85 | T6 0.90

**Process:**
- Phase 0 (Scope): PASS — effort=full confirmed; English; EP audience; purpose and length confirmed.
- Phase 1 (Protocol): PASS — 00_protocol.md produced with PICO, MeSH blocks, inclusion/exclusion.
- Phase 2 (Retrieval): PASS — 02_corpus.md + search_log + fulltext_upgrade; 39 records in store;
  supplementary learning-curve and persistent-AF gap searches run.
- Phase 3 (Research Map / HARD GATE): CLEARED — quotable approval "Duyệt có chỉnh" documented in
  research_map_gate_approval.md. NOTE: conditional option selected twice without edit specification;
  lead correctly held and requested specifics before proceeding.
- Phase 4 (Appraisal): PASS — 03_appraisal.md with GRADE table per axis and RoB per study.
- Phase 4b gate: PASS — lead presented appraisal; user approved before drafting.
  NOTE: lead initially framed summary as "CBA advantage" dimensions; user corrected framing.
- Phase 5b (Coach): NOT PRESENT — 04b_coach.md absent, no declared skip reason. V-01 R4 violation.
- Phase 5 (Draft): PASS — 05_review_draft.md; 39 references; all inline; full structured review.
- Phase 6 (QA): PASS — 06_qa_report.md; 21 live PMID checks; 0 fabrications; 5 minor defects.
- Phase 8 (Manifest): NOT PRESENT — 08_manifest.md absent. V-02 process violation.
- source/ folder checked: PASS — user confirmed no PDFs to add.
- Research Map gate approval persisted to disk: PASS (L-019 compliant).

**Violations found:**
- V-01 [R4 — Faking the steps]: Phase 5b quality-coach pass absent; no declared skip reason for
  effort=full run.
- V-02 [PROCESS]: 08_manifest.md not produced before QA delivery.
- V-03 [LAW 4]: Law 4 structural labels ("Established consensus" / "Ongoing controversy") absent
  from draft body; content covered both but section headers missing.

**Defects found (QA):**
- D-01 MINOR format-error — P-value rounding (Urbanek §3: P=0.72/0.63 → P=0.724/0.629)
- D-02 MINOR mismatched-citation — Chéhirlian §5.1: "(N=64)" parenthetical wrong for 24%
  sub-cohort figure (correct N is 25)
- D-03 MINOR overstated-certainty — Abstract "Moderate certainty" vs §3 GRADE LOW inconsistency
  without explanation
- D-04 MINOR format-error — Ref [5] Xu: "2025;Nov" should be "2025;62:101845"
- D-05 MINOR format-error — Ref [21] preprint: author names absent from reference list entry
All 5 defects corrected before final delivery. CRITICAL/MAJOR defects: ZERO.

**Process observations:**
- (a) User selected conditional gate option ("Duyệt có chỉnh") twice without specifying edits; lead
  correctly held and asked for specifics rather than self-clearing. Gate behaviour was correct.
- (b) Lead framed Gate-4b appraisal as "CBA advantage" because user-requested investigation
  dimensions (cost, learning curve, maturity) favoured CBA; user corrected — dimensions are search
  axes, not conclusion steers.

**Lessons proposed (pending user approval):**
- L-025 (orchestrator): Silent absence of 04b_coach.md for effort=full = R4; must declare SKIP
- L-026 (writer): Law 4 explicit section labels required in draft body, not just implicit content
- L-027 (orchestrator): 08_manifest.md must be assembled before QA handoff, not after
- L-028 (writer): Sub-group statistics must cite sub-cohort N, not parent-study N
- L-029 (writer): Abstract GRADE labels must match body stamps; resolve dual-level certainty inline
- L-030 (orchestrator/lead): Conditional gate option = HOLD until specific edits specified
- L-031 (writer/coach/lead): User-specified investigation dimensions are evidence axes, not
  conclusion steers; steelman the weaker side before concluding

**Actions taken (pending approval):**
- _workspace/07_lessons_proposal.md produced (this file)
- No changes to lessons.md or evolution-log.md until user approves

**What changed / what this run validated:**
- First PFA-vs-CBA review in the harness; validated multi-technology comparative framing.
- Gate-hold behaviour on conditional approval worked correctly (process observation a).
- Anti-bias (steelman) principle caught a framing drift at Gate-4b (process observation b).
- V-01 and V-02 identify two recurring omissions (coach pass, manifest) that need procedural anchors.
- T4 deduction for absent Law 4 headers is a clean writer-discipline failure with a simple fix (L-026).
═══════════════════════════════════════════════

**Entry #7 — Addendum (2026-06-17, post-delivery language correction)**
- The review was delivered in English; `00_protocol.md` had set "Output language: English" with NO recorded, quotable user confirmation. Per CLAUDE.md the default is Vietnamese (user-selectable, confirm in Phase 0). User caught this and requested Vietnamese as the primary deliverable.
- Re-issued in Vietnamese (`06_final_review_vi.md`). First pass was a literal translation — user flagged it as unnatural/clunky (run-on sentences, calques). A full **native rewrite** followed; all numerics/CIs/P-values/GRADE/citations preserved verbatim, neutral stance intact.
- Process hardening: `00_protocol.md` annotated; orchestrator SKILL Phase 0 now gates output language (quotable confirm, else default Vietnamese, fail closed); review-synthesis SKILL now mandates native composition over literal translation.
- New lessons: **L-032** (language gated, quotable, fail-closed Vietnamese) and **L-033** (compose natively, never literal-translate). English version retained at `06_final_review.md` for record.
- Open follow-up: ablation-modality EP terms used in the VN version (cryoballoon, PFA, phrenic nerve palsy, PV isolation, electroporation, tamponade) are still **provisional** — pending user confirmation for append to `vi-terminology.md`.
- (2026-06-18) Terminology batch confirmed by user and appended to `vi-terminology.md` (Entry #7 section): triệt đốt (not triệt phá); bóng áp lạnh (CBA); trường xung (PFA); thiết bị theo dõi tim cấy ghép (ICM); so sánh đối đầu CBA và PFA. Applied across the VN review.
- (2026-06-18) **Factual correction (user-caught, domain expert):** §8/§9 framed "PFA single-use catheter vs CBA reusable console" — false contrast, since both modalities use single-use catheters and both have a reusable console/generator. Reframed cost driver to the higher PFA catheter price + anaesthesia; infrastructure differentiator narrowed to the anaesthesia profile. New lesson **L-034** (verify a feature actually differs between arms before contrasting). Targeted citation-verifier re-check of §8/§9 against [22].
═══════════════════════════════════════════════


### Entry #8 — 2026-06-23 — AF catheter ablation in the elderly: cryoballoon vs RF (+PFA) (PhD thesis chapter)
- **Task:** High-stakes "chuyên đề" for a PhD medicine thesis — efficacy & safety of catheter ablation for AF in elderly patients, cryoballoon (CB) vs radiofrequency (RF), with a short PFA-context section. Vietnamese, >7000 words (delivered ~10,690), audience = thesis committee + EP specialists.
- **Rubric:** 0.895 — band **EXCEEDED**. Per-criterion: T1 0.90 / T2 0.90 / T3 0.90 / T4 0.90 / T5 0.85 / T6 0.90.
- **Violations:** none. 0 BLOCK. 2 FIX (format-only, both applied): FIX-01 reference [2] CIRCA-DOSE title was a reconstruction → corrected to verbatim PubMed title; FIX-02 five references missing DOI → tagged "DOI: not yet indexed".
- **Gates:** all four human gates cleared. Phase-0 scope confirmed (purpose/depth/audience/language/date window, two AskUserQuestion rounds). Gate 2b cleared (corpus presented; user chose PMC pulls + uploaded 12 paywalled full texts to `source/elderly-rf-vs-cryo/`). Research Map HARD GATE cleared with quotable approval "duyệt hết" (persisted to `_workspace/research_map_gate_approval.md`, L-019). Gate 4b cleared with an added RF/CBA-generation directive.
- **Corpus:** 53 records (R001–R053) + 3 guidelines + 3 trials, 100% PMID-verified, 24 full-text on disk (8 PMC pulls + 12 user uploads + prior). New store `reference/af-ablation-elderly-rf-vs-cryo.md`.
- **Notable process facts:**
  - **Harness reconciled from `main` mid-run** (user point 5): pulled only the methodology files (constitution anti-hedging + steelman + named failure modes R2–R6 + effort tag; orchestrator per-agent model allocation; quality-coach agent; appraiser steelman; writer both-directions calibration + steelman; rubric/audit steelman/calibration/coach/manifest checks; unified vi-terminology; CLAUDE.md branch-per-study). Did NOT pull main's other-topic review data (would have clobbered this study). Removed legacy duplicate root glossary.
  - **Full-text discipline (L-005):** ingesting the 12 uploaded full texts corrected several abstract-stored values — França overall major-complication RR 1.30→1.33 (1.17–1.52); França cryo-complications subgroup was mislabeled (the stored 1.10 was the cryo *recurrence* RR; true cryo complications RR 1.26 [0.60–2.63]); Boehmer recurrence CI 1.09–1.41→1.09–1.42; confirmed Boehmer has NO energy-subgroup forest (L-034 — expected contrast not present; CB-vs-RF subgroup comes from Kawamura/Lee/França).
  - **User directive operationalized the Ioannou caveat:** every RF result labels its technology generation (CF / ablation-index / not-reported) and the CBA generation, with a dedicated technology-generation comparison sub-section — making the temporal/indirectness steelman (AR-6) systematic rather than a single caveat.
  - **Steelman + anti-hedging** applied throughout: "CB safer/faster" steelmanned against the RF-legacy artifact (edge narrows vs modern AI/CF-RF, but the AEF/stroke mechanism advantage survives); "ablation benefits the very old" left honestly unresolved (CABANA/Bahnson HR≈1 ~age 78). Boehmer⇄França contradiction carried with a methodological resolution (publication-bias handling), not false balance (L-006).
  - Coach pass = ONE-IMPROVEMENT-PASS → C1–C4 applied (+~810 words: monitoring-intensity second-bias depth, blanking-period direction, clinical "so what" conclusion head, Calkins-2017 currency caveat).
- **Lessons added:** **L-035** (verbatim reference titles from PubMed metadata, never reconstruct) and **L-036** (carry missing/pending DOI as an explicit tag, not an empty field). Both user-approved 2026-06-23.
- **Provisional VN terms surfaced (pending user confirmation before append to vi-terminology.md):** "đánh đổi đặc hiệu theo cơ chế" (mechanism-specific trade-off); "giai đoạn blanking" (blanking period); "cường độ theo dõi" (monitoring intensity); "liệt thần kinh hoành" (phrenic nerve palsy); "rò nhĩ-thực quản" (atrio-oesophageal fistula). NOT yet appended.

**Entry #8 — Addendum (2026-06-23, post-delivery Vietnamese fluency correction)**
- User (native domain expert) flagged the delivered review (which had passed QA at 0.895) for many word-by-word / calque sentences: "tạo tác" (artifact), "điểm cuối nhị phân" (binary endpoint), "câu chuyện an toàn" (the safety story), "tâng bốc" (flatter), plus 60–90-word run-on sentences.
- Fixes applied across the pipeline: term swaps (đánh đổi rủi ro theo cơ chế; catheter đốt tưới lạnh; tái phát tăng thêm) + a full native-fluency pass reworking ~83 paragraphs (06_final_review.md → 11,324 words), preserving all numerics/CIs/[n]/GRADE and the reference list verbatim. Glossary updated with Entry #8 confirmed terms + style notes (artifact, binary endpoint).
- New lesson **L-037** (native-fluency self-pass with a calque blacklist before handoff) — generalizes L-033 from "compose natively" to an explicit pre-handoff check with a banned-pattern list. User-requested.
- Process note: the calque leakage passed QA because the rubric/audit check correctness + structure + steelman + calibration, but not idiomatic fluency for a native reader. Consider whether the quality-coach (ceiling-raiser) should own a fluency check for non-English deliverables.

**Entry #8 — Addendum 2 (2026-06-23, AF-type / PICO-subgroup salience gap)**
- User (domain expert) flagged that the paroxysmal-vs-persistent distinction and elderly-specific efficacy features — esp. that ≥75 + persistent AF is the highest-recurrence, lowest-evidence group (Boehmer 57% vs ~39% overall elderly) — were present-but-scattered, not given an explicit labeled treatment.
- Self-assessment: a real, moderate-severity synthesis/salience defect (NOT Law-1, NOT retrieval — data were in corpus + appraisal). Root cause: Gate-4b emphasis on safety+QoL implicitly demoted an in-scope PICO subgroup; writer covered it in substance only; rubric/coach/audit lacked a PICO-subgroup-completeness check.
- Fixes: document — added §4.5 (efficacy & safety stratified by AF type) + an explicit ≥75-persistent clinical headline. Harness — new lesson **L-038** + patched `synthesis-writer.md` (PICO×outcome coverage matrix before handoff), `audit.md` (Synthesis check now requires explicit locatable treatment of each pre-registered subgroup), and `quality-coach.md` (completeness angle now asks about under-weighted population-critical effect modifiers).
