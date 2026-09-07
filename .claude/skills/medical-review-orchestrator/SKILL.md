---
name: medical-review-orchestrator
description: >
  Orchestrates a specialist agent team to produce high-quality, in-depth, systematic-style
  medical literature reviews from live, up-to-date sources (PubMed/PMC, bioRxiv/medRxiv
  preprints, ClinicalTrials.gov, Consensus). Use this skill WHENEVER the user asks to write,
  draft, build, update, expand, redo, or improve a medical/clinical/biomedical literature
  review, evidence review, systematic review, scoping review, narrative review, or
  "review the literature/evidence on <medical topic>". ALSO triggers on follow-ups:
  "update the review", "rerun", "redo the search", "expand section X", "improve the
  citations", "based on the previous review", "the appraisal was too shallow", "score this
  review", "run the audit". Do NOT use for a single factual medical question, a quick fact
  lookup, or non-medical reviews.
---

# Medical Literature Review Orchestrator

You are the lead AND writer. Default: four agents INCLUDING you, not four workers plus you.
Read the short shared constitution once. Load each phase skill only when entering that phase.
Do not load history, evaluation cases, all source files or the whole lesson archive by default.

## Roles and execution
| Role file | Responsibility | Context boundary |
|---|---|---|
| `review-lead` | Scope, protocol, Research Map, synthesis, revisions, lessons | current phase inputs |
| `evidence-retriever` | Search, source acquisition, store, screening pipeline | search-heavy context |
| `critical-appraiser` | RoB/GRADE, cards, contradictions, assumptions | evidence-heavy context |
| `citation-verifier` | Independent claim/source and methodology checks | fresh QA context |
| `quality-coach` | Optional targeted structural/clarity pass | only if a stated need |

Execute as lead with on-demand workers, not an always-running team or message mesh. A phase is
not a new agent. Reuse a worker for a related partial update; launch verifier without the writer's
conversation or persuasive handoff. Parallelize only independent source groups or study batches
when volume warrants it. Record each extra worker, assignment and actual model in `00a_run.json`.
Claude model defaults are in agent frontmatter; lead uses the session model. On other hosts choose
available models by role and measured performance, not by translating brand aliases blindly.
Retriever may use a cheaper model, escalating on failed coverage or difficult retrieval. Appraisal,
synthesis and semantic verification need capable reasoning; do not economize on QA by default.

## Context and handoffs
- Each worker reads constitution + its role file + its phase skill + relevant lesson slice only.
- Lead runs `scripts/select_lessons.py --roles <roles> --scopes <scopes> --out _workspace/00b_lessons.md`
  at phase entry; role aliases map writer/strategist/orchestrator to lead. Pass selected rule IDs/text,
  not the whole digest. Unknown lesson scope is universal (fail toward inclusion); filter only explicit tags.
- Handoff = artifact paths, changed IDs, decisions and blockers; target <=200 words, not copied evidence.
- Read metadata, then relevant source passages; expand to methods/results/supplement/full text whenever
  needed to interpret an outcome, denominator, subgroup or contradiction. A snippet is not full appraisal.
- Keep records, cards and links canonical; render repetitive tables/indexes with code. Do not summarize
  all source material repeatedly into each downstream artifact.

## Phase 0 — Scope gate A
Read existing scope/state for continuation. For a fresh topic use a separate study branch/workspace;
preserve previous runs. Confirm topic, purpose, audience, depth and date window from the user's explicit
request. **Already explicit answers count as approval: quote them in `_workspace/00_scope.md`; do not
ask them again.** Ask only missing/conflicting fields before retrieval. Vietnamese is the declared default;
an explicitly requested other language counts directly. Do not invent purpose or depth.
Inspect source folders; reuse the user-designated folder, ask only if ambiguous. Ask once about external
database exports if unanswered; record none/available/pending, never infer an unanswered question as no.
Tag tiny/normal/full/high-stakes to size depth, not truthfulness. Record actual model/settings per role.
Initialize `_workspace/00a_run.json` using `docs/run-state.md`: gate receipts, conditional decisions,
worker/model usage pointers and revisions. The state is a receipt, not independent proof of approval.

## Phase 1 — Protocol (lead)
Load `review-protocol/SKILL.md`. Write `_workspace/01_protocol.md`: PICO, criteria, source-specific queries,
outcomes/subgroups, date cutoff and >=1–2 applicable gap-directed searches. Write
`_workspace/01a_concepts.json` (surface synonyms for P4, not MeSH-only concepts). Freeze the question
before search; protocol changes require a reason and affected downstream work to be refreshed.

## Phase 2 — Retrieval (retriever)
Load `literature-retrieval/SKILL.md`. Search live sources, inspect supplied full texts and import author
exports with manifest. Preserve `02b_records.jsonl` before screening; concatenate external records before
dedupe. Run dedupe → prefilter → agent screening verdicts → PRISMA; validate the search ledger.
Write `_workspace/02_corpus.md` as a compact decision view linking to the store and `02j_prisma.md`,
not a second copy of every abstract. Expose deferred-unread records separately from excluded ones.
Try full-text upgrades for HIGH sources and screen retractions. Retry a failed source once, continue
independent searches, collect unresolved gaps for gate B. Do not silently lower coverage or claim completeness.
Paid tools require concrete parameters, usage/cost information and explicit authorization BEFORE execution;
this is a separate expenditure decision, not implied by accepting the corpus.

## Phase 3 — Research Map + corpus gate B (required)
Lead writes `_workspace/03_research_map.md` BEFORE showing it. Include scope recap; world axes labelled
mature/emerging/contested; local/Vietnam applicability; evidenced gap types and next directions; source
approval list (IDs, relevance, source type, full-text/abstract status); PRISMA counts, deferred studies,
unavailable sources and HIGH full-text gaps. This replaces the separate post-retrieval gate.
STOP for explicit approval of this map AND source list after presentation. Record the reply and approved
map hash in `_workspace/03a_gate_approval.md` and state. A PDF-supply promise or unrelated answer is not
approval. If the user requests changes, revise and present again. Deep appraisal/writing cannot start
before approval; no tiny or fixed-case exception. A light landscape classification may precede approval.

## Phase 4 — Appraisal (appraiser)
Load `evidence-appraisal/SKILL.md`; use only approved sources. Run P2 number extraction, interpret each
number in context, build `_workspace/04b_cards.jsonl`, run P8 quote locks, repair/drop rejected claims.
Render `_workspace/04d_evidence_table.md` from cards via `scripts/render_artifacts.py evidence` (see
docs/run-state.md). Write `_workspace/04_appraisal.md` for RoB/GRADE by outcome with reasons,
contradictions, strongest counter-case, gaps and Assumption Register; link the generated evidence table.
Empty numeric buckets mean extraction found nothing: check the source before concluding not reported.

### Conditional appraisal decision (formerly unconditional Gate 4b)
Record a brief decision in state. Continue without another approval when evidence can be synthesized
honestly within approved scope, including ordinary uncertainty/expected disagreement. STOP for a user
decision if appraisal requires changing scope/source set, cannot answer a key outcome with available
evidence, uncovers a major unanticipated contradiction affecting the planned interpretation, needs a
consequential new extrapolation, or the user requested this checkpoint. Present certainty, contradictions,
assumptions, accepted/rejected card counts and options. Scope/source changes return to gate B with a revised
map; a material appraisal-only decision is recorded here. Requests for changes reopen the relevant decision.

## Phase 5 — Synthesis (lead)
Load `review-synthesis/SKILL.md`; for Vietnamese load only relevant terminology entries. Draft
`_workspace/05_draft_review.md` from the store + accepted cards + appraisal, preserving thematic depth,
subgroups, counter-evidence and calibrated conclusions. Each cited paragraph/table row carries an invisible
claim ID linked through `_workspace/05b_claim_links.jsonl`; exact schema: `docs/claim-links.md`.
No card → obtain appraisal support or remove the claim. A multi-study conclusion links all supporting cards;
its inference/semantic support still needs verifier judgment. Uncited process statements need audit receipts.

Optional coach: only for a requested publication-level editorial pass, long/complex structure, or a concrete
clarity/depth defect. Record not_needed with reason in state otherwise; no separate skip essay. Coach reads
only relevant sections/appraisal and recommends at most one improvement pass. It cannot widen scope or
clear citations. Do not spawn it merely because effort=full.

## Phase 6 — Independent QA and delivery
Verifier reads actual draft, sources, cards, appraisal and gate receipts, not the lead's defense of its work.
Run claim-link + quote checks before semantic QA to fix mechanical errors cheaply. Verify ALL substantive
claims including uncited factual prose, source support, population/endpoints, numeric context, RoB/GRADE
and neglected subgroups/counter-evidence. Use a compact issue list plus checked claim IDs; no prose essay
per passing claim. Score rubric with evidence, not just a total. Write `_workspace/06a_verification_report.md`.
Lead fixes affected claims/sections only. Recheck changed claims AND dependent conclusions/GRADE/summary;
keep prior semantic verdict only when its text, sources and appraisal are unchanged. After two unsuccessful
repair rounds, report the blocker and get a decision; never deliver unresolved BLOCK to meet a budget.

Copy the corrected draft to `_workspace/06_final_review.md`; keep invisible claim annotations. Against
this EXACT file rerun `verify_claim_links.py` → `_workspace/06d_claim_audit.json`, P8 quote locks and P1
`citation_audit.py` (coverage floor 0.4) → `_workspace/06b_citation_audit.md`. Re-run search/PRISMA checks
if their inputs changed. No fabricated citation, rejected linked card, unresolved substantive mismatch,
unapproved map, failed required check or stale QA may be delivered. Nonblocking limitations stay visible.
Run `scripts/render_artifacts.py manifest` to generate `_workspace/06c_manifest.md` with state, confidence
card index, assumptions link and artifact hashes. No edits after validation without refreshing affected QA
and regenerating manifest. Scripts attest their narrow checks; this prompt is not an enforced runtime gate.
Deliver Markdown + verification + audits + manifest. Human sampling of pivotal claims is recommended;
never pretend a person performed a check they did not perform.

## Phase 7 — Learning (lead, no worker)
Record outcome/defect categories in run state. If there is a NEW reusable lesson or important recurrence,
load `lessons-learned/SKILL.md` and write `_workspace/07_proposed_lessons.md`. Bundle approve/edit/reject
with delivery; persist cross-run knowledge only on approval. Otherwise record no_new_lesson and finish.

## Partial updates and failure behavior
Retain unchanged upstream artifacts. Mark affected downstream outputs stale in state, regenerate them or
their affected sections and rerun global checks; archive superseded receipts. If scope or source approval
changes, reopen gate B. A missing appraiser/verifier cannot be treated as an optional omission: retry once,
then surface the blocker. Routine reversible choices within scope are autonomous, recorded when material.

## Validation
Run the automated suite after edits. `references/test-cases.md` preserves benchmark prompts;
`docs/lean-harness-evaluation.md` defines controlled old/new trials. Cheap dry runs: vague topic → ask before
search; full scope → no duplicate scope questions; map awaiting approval → no appraisal; ordinary low
certainty → proceed with calibrated writing; material scope change → reopen map; unrelated reply → wait.
Unit-green proves mechanics, not clinical quality or token savings. Real A/B results remain required.
