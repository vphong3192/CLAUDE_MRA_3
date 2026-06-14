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
