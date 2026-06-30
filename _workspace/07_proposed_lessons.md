# Phase 7 — Proposed Lessons (pending user approval)

**Run:** LA electrophysiology in elderly AF (Đặc điểm điện học, điện sinh lý nhĩ trái ở bệnh nhân rung
nhĩ cao tuổi) · **Date:** 2026-06-30 · **Branch:** review/la-ep-elderly-af

**Verification basis:** Read `_workspace/06_verification_report.md`, `_workspace/05b_coach.md`,
`_workspace/gate4b_approval.md`, `_workspace/04b_crf_table_preview.md`, and `git log` over `_workspace/`
to confirm candidates against actual events (not the user's framing alone) before drafting.

---

## Evolution-log entry (draft — Entry #10)

**Topic:** LA electrophysiology in elderly AF — narrative review + CRF parameter table (dual Phase-0
deliverable). **Rubric:** 0.92 (EXCEEDED). **Bands:** T1 0.9 · T2 0.85 · T3 0.95 · T4 0.95 · T5 1.0 · T6
0.9. **Deterministic citation audit:** PASS, exit 0, 0 HARD-FAIL, 6 non-blocking WARN (5 formatting
heuristics + 1 genuine store-depth gap, both traced). **Gates:** Research Map (Phase 3) approved "ok";
Gate 4b approved "bắt đầu viết" in a distinct turn after a nested CRF structural sub-approval (3
yes/no decisions) was resolved. **Coach verdict:** SHIP-AS-IS, one pass, no improvement-pass triggered.
**Laws:** 6/6 PASS. **Strengths:** AFCL (G-2) gap discipline held throughout (never used REF-074 to
silently fill it); Chattopadhyay internal inconsistency reported transparently rather than resolved;
GRADE language calibrated both directions; L-038 PICO-subgroup-completeness check explicitly passed.
**Risk surfaced:** one store record (REF-003, van der Does) retrieved via Consensus-only with no
full-text pull, producing predictable but non-blocking `number_not_in_source` WARNs at audit time —
flagged by the verifier itself as a lesson candidate. **Process note:** the stop-hook fired multiple
times across the run because per-phase `_workspace/` artifacts were left uncommitted at turn
boundaries; each time resolved reactively rather than the artifact being committed proactively at
write-time.

---

## Candidate lessons

### L-040: Commit each phase artifact immediately after it is written and verified, not at turn end
- **Role:** orchestrator
- **Trigger:** any `_workspace/` artifact is written or finalized (appraisal, draft, coach report, QA
  output, table preview, gate-approval file)
- **Rule:** Run `git add` + commit for that artifact in the same tool-call batch that finishes writing
  it — before moving on to the next phase step or ending the turn. Do not wait for the stop-hook to
  flag uncommitted changes as the trigger to commit.
- **Why:** This run, the stop-hook (`~/.claude/stop-hook-git-check.sh`) fired roughly five times because
  newly-written artifacts (appraisal, CRF preview, draft, coach report, QA outputs) were left
  uncommitted at turn boundaries; each was resolved with an immediate add+commit+push cycle, but only
  reactively. The hook is a safety net for forgotten commits, not the intended commit trigger — relying
  on it costs an extra round-trip per phase and risks losing the per-phase audit trail (L-019/L-027's
  value: artifacts on disk are the audit's only evidence) if a session ends before the hook fires.
- **Origin:** Entry #10 — LA-EP elderly AF review, recurring stop-hook pattern (2026-06-30)

### L-041: Track gate status as explicit state across interleaved side-conversation turns
- **Role:** orchestrator
- **Trigger:** a human gate (Research Map, Gate 2b, Gate 4b) has been presented and is awaiting
  approval, AND the user's next messages are unrelated or semi-related questions before the actual
  approval/rejection arrives
- **Rule:** Answer side questions on their merits without treating them as gate approval and without
  re-litigating gate status mid-answer. Before launching the next phase's agent, re-confirm explicitly
  that the gate-closing question was asked again (if the side conversation introduced new decisions,
  e.g. a structural sub-approval) and that a distinct, quotable approval was received for the gate
  itself — not inferred from the side conversation's tone or from "the user seems satisfied."
- **Why:** This run, Gate 4b's presentation was followed by two side-conversation turns (a CRF table
  draft request, a CV data question) and a nested 3-question structural sub-approval on the CRF table,
  before the actual gate-closing approval ("bắt đầu viết") arrived in a separate, later turn. The
  orchestrator handled this correctly here (confirmed in `gate4b_approval.md`'s sequence-of-record), but
  the pattern is a plausible failure mode the existing L-024 doesn't explicitly name: L-024 covers
  "present, then stop and wait," not "present, then survive N interleaved unrelated turns before
  closing." Naming the multi-turn case makes the discipline explicit rather than incidentally correct.
- **Origin:** Entry #10 — LA-EP elderly AF review, Gate 4b interleaved side-conversation (2026-06-30)

### L-042: A second locked Phase-0 deliverable (e.g., a structured table) gets its own labeled sub-approval, nested inside but distinct from the phase gate
- **Role:** orchestrator
- **Trigger:** Phase 0 scope locks two deliverables (e.g., narrative review + CRF/structured table), and
  the second deliverable's structure (columns, highlighting, grouping) requires user decisions before
  it can be finalized
- **Rule:** When a phase gate (e.g., Gate 4b) also requires finalizing a second deliverable's structure,
  present the structural questions as an explicitly labeled sub-approval (e.g., numbered yes/no
  decisions) distinct from the gate-closing question. Resolve and record the sub-approval first: write
  the finalized structure to its own artifact (e.g., `04b_crf_table_preview.md`) and commit it. Only
  then re-ask the gate-closing question on its own. Do not let "user answered the structural questions"
  stand in for "user closed the gate" — they are different approvals even though they happen inside the
  same gate window.
- **Why:** This run, Gate 4b correctly nested a 3-question CRF structural sub-approval ("1.2. có 3.
  không") inside the gate window, finalized and committed the table (`d1e4ad0`) before re-asking the
  gate-closing question, and only then received "bắt đầu viết" as the distinct gate approval. This
  worked because the orchestrator treated them as separate approvals; documenting the pattern protects
  future dual-deliverable reviews (any review locking a narrative + a structured artifact at Phase 0)
  from collapsing the two into one ambiguous approval.
- **Origin:** Entry #10 — LA-EP elderly AF review, CRF table structural sub-approval (2026-06-30)

### L-043: Flag Consensus-only / abstract-only store entries at appraisal time so verifier WARNs on them are pre-triaged
- **Role:** appraiser, retriever
- **Trigger:** a store record was retrieved via Consensus (or any abstract-only path) without a
  full-text pull, and it anchors a quantitative claim (effect size, coefficient, p-value) used in the
  draft
- **Rule:** When building the evidence table (Phase 4), explicitly tag such records — e.g., "Consensus-
  only / abstract-depth: numbers unconfirmable by audit heuristic" — in the appraisal artifact (and
  propagate the tag into `03b_numbers.md` or the store entry itself). At QA time, the citation-verifier
  should treat a `number_not_in_source` WARN on a pre-tagged record as already triaged (known store-
  depth limitation) rather than re-investigating it as if newly discovered.
- **Why:** This run, REF-003 (van der Does) was a Consensus-only retrieval lacking full-text verbatim
  numbers; the deterministic citation_audit.py correctly WARN-flagged its cited coefficient/p-value as
  `number_not_in_source`, and the verifier had to manually re-derive that this was a store-completeness
  gap, not a draft error — taking real investigation effort that a Phase-4 tag would have pre-empted.
  This is the citation-verifier's own self-update proposal in `06_verification_report.md` §5/§6,
  confirmed here as a generalizable rule rather than a one-paper note. Complements L-009 (PMID
  verification) and L-005 (copy from results table, not abstract) by closing the loop when full text
  genuinely isn't available: tag the limitation instead of leaving it implicit.
- **Origin:** Entry #10 — LA-EP elderly AF review, REF-003 WARN triage (citation-verifier
  self-update proposal, 2026-06-30)

---

## Items considered and NOT proposed as new lessons

- **Citation_audit.py heuristic false positives** (comma-vs-period decimals, bare "95" inside "95% CI"):
  the verifier's own report (§5 SELF-UPDATE PROPOSALS) explicitly concludes these are already documented
  script-docstring limitations with no script change recommended — this is confirmation the existing
  L-039 deterministic-layer discipline is working as intended, not a new defect. No lesson drafted.
- No fabricated citation, no overstated certainty, no missed contradiction, no format error occurred
  this run (per `06_verification_report.md` §6) — nothing else in the two QA artifacts rises to a
  generalizable defect beyond the four drafted above.

---

## Awaiting user decision: approve / edit / reject each of L-040 through L-043, and the Entry #10 draft above.
