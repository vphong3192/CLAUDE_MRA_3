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
