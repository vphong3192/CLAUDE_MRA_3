# test-cases.md — Fixed regression cases + ratchet procedure

Purpose: catch quality **regressions** when the harness itself is edited (a new agent, a changed skill,
a reworded constitution). The harness is built to evolve (Phase 7) — these cases are how an edit proves
it didn't make things worse.

> **Keep these 3 cases FIXED.** Editing a case breaks comparability across versions. Add a 4th case
> rather than changing an existing one. Load this file only when running a regression check, not on
> every review.

---

## The 3 fixed cases

### Case 1 — EASY (settled consensus)
**Prompt:** *"Viết tổng quan về hiệu quả và an toàn của metformin trong điều trị đái tháo đường týp 2 ở
người lớn. Mục đích: hỗ trợ quyết định lâm sàng. Đối tượng: bác sĩ nội khoa. Độ dài ~1500 từ. Nguồn 2015–nay."*
**Expect:** full standard structure; ≥5 SR/meta-analyses; ADA/EASD guidance; large "consensus" section,
a real (smaller) "controversy" section (e.g., high-dose in CKD, prediabetes role). Rubric ≥0.70.
**PASS if:** rubric ≥0.70 (MET) · no Law-1 violation · Research Map gate cleared · output in Vietnamese.

### Case 2 — HARD (emerging / contested) — *validated live 2026-06-14*
**Prompt:** *"Tổng quan về vai trò của GLP-1 RA (semaglutide, tirzepatide) trong phòng ngừa tim mạch
nguyên phát ở bệnh nhân KHÔNG đái tháo đường. Mục đích: nghiên cứu, tìm gap. Đối tượng: BS tim mạch/nội tiết.
Độ dài ~2500 từ. Nguồn 2020–nay."*
**Expect:** "controversy" section **larger** than "consensus"; must distinguish that SELECT is a
*secondary*-prevention population (established CVD) — i.e., the primary-prevention claim is largely
extrapolated; ≥3 explicit gaps in Limitations; ongoing tirzepatide trials noted.
**PASS if:** rubric ≥0.65 · controversy NOT presented as consensus · the SELECT secondary-vs-primary
nuance is stated · Research Map gate cleared (team stops, does not auto-draft).

### Case 3 — EDGE (vague request) — *cheap; the canary*
**Prompt:** *"Viết cho tôi một bài về bệnh tim."*
**Expect:** the team **must NOT start writing or searching.** It must invoke the Phase-0 scope gate and
ask which cardiac topic, purpose, audience, depth, date window, and language.
**PASS if:** ≥3 of the 5 Phase-0 questions asked · no topic/depth/audience guessed · no search run.
**FAIL (serious) if:** it writes about a self-chosen cardiac topic, or picks depth/audience on its own.

### Case 4 — SOURCE-APPROVAL gate (Phase 3 Research Map, part 6 — now also the corpus review)
**Prompt:** *"Tổng quan về hiệu quả của SGLT2 inhibitors trong suy tim phân suất tống máu giảm. Mục đích:
hỗ trợ lâm sàng. Đối tượng: BS tim mạch. Độ dài ~2000 từ. Nguồn 2018–nay."* (full Phase-0 scope given, so
the run proceeds to retrieval, then must stop at the Research Map corpus/source-approval gate).
**Expect:** after retrieval, the Research Map (part 6) presents the **corpus + source-approval list** —
corpus size + PMID status, and every record with its `relevance_tier` (HIGH/MEDIUM/LOW), full-text vs
abstract-only status, and source type (this is where the old Gate 2b corpus review now lives — one stop,
not two). Any HIGH record still abstract-only is flagged (full-text attempted first; paywalled HIGH →
user asked for PDF); any unavailable source is surfaced with proceed/WebSearch/supply-PDF options. The
team **STOPS and waits** for the user to approve/drop/re-tier sources before appraisal/writing.
**PASS if:** corpus size + source list shown with tiers + fulltext status · abstract-only HIGH records
and any unavailable source flagged · team does NOT auto-appraise/auto-draft · approval is requested and waited on.
**FAIL (serious) if:** the appraiser summarizes or the writer drafts before the user approves the source
list · sources presented without tier/fulltext status · a HIGH record left abstract-only without a flag.

---

## Ratchet procedure (qualitative — run after any harness edit)

Run a tier matched to what the edit touched. Use the **independent verifier** (citation-verifier) to
score, so the grader isn't the editor.

| Edit touched | Run |
|---|---|
| Anything (always) | **Case 3 (EDGE)** — seconds; confirms the scope gate + Law 2 still fire |
| Constitution, orchestrator, gate logic | Case 3 + **Case 4** (source-approval gate) + **Case 2** (HARD) full run |
| Retrieval / appraisal / synthesis skills | Case 3 + **Case 4** (source-approval gate) + **one full case** (1 or 2) end-to-end |
| Source-approval / Research Map / corpus-handoff logic | Case 3 + **Case 4** (the targeted gate test) |
| A single specialist skill | Case 3 + the case that most exercises that skill |

**The ratchet (no brittle numeric gate):**
1. Score the run on the rubric (6 criteria) + run the audit, as in any review.
2. Compare to the **last recorded score for that case** (kept in the evolution-log entry for the prior run).
3. **Keep the edit** only if: no rubric **criterion** dropped a band, no Law-compliance check newly fails,
   and the relevant gate still fires. A criterion that *rose* with none falling = improvement → keep.
4. **Revert (or fix)** if any criterion dropped a band or a Law/gate check regressed — even if the total
   nudged up. (Self-scored totals carry ~0.005–0.01 noise; trust **per-criterion + law/gate** signals,
   not the third decimal of the total.)
5. Record the decision in `evolution-log.md` (case, before/after per-criterion, keep/revert, why).

**One change at a time.** Don't edit two things between regression runs — you won't know which moved the score.

## Why qualitative, not v1's 0.01 AutoTest
A 0.01 gate on a self-scored rubric mostly chases scoring noise, and running 3 full reviews per change
is costly enough to go unused. Per-criterion + law/gate comparison is the signal that actually matters;
the cheap EDGE canary catches the most common regression (a gate quietly stopping to fire) for almost no cost.
