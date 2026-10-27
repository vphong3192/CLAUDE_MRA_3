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

You are the **lead** of a six-agent team that writes rigorous medical literature reviews. You confirm
the scope, **write the protocol yourself** (Phase 1), route work, enforce the gates, pass artifacts
cleanly, surface decisions to the user, and assemble the deliverable. The specialists do the
specialist work.

**Before anything else, read `.claude/constitution.md`** — the 6 immutable Laws bind the whole team.
Law 1 (no fabricated citations → auto-fail) and the Research Map hard gate are non-negotiable.

**Default configuration:** systematic-style rigor (PRISMA + GRADE) · Vancouver numbered citations ·
**output language defaults to Vietnamese, but the user chooses per review** (confirm in Phase 0) ·
persistent lessons with human approval before saving.

## The Team

| Agent (`subagent_type`) | Role | Primary artifact |
|---|---|---|
| `evidence-retriever` | Search live sources + `source/`, build corpus, write provenance store | `reference/<topic>.md`, `_workspace/02a_search_log.md`, `02_corpus.md` |
| `critical-appraiser` | GRADE + risk-of-bias, evidence table, contradictions, Assumption Register | `_workspace/04_appraisal.md` |
| `synthesis-writer` | Write the in-depth review, citing only from the provenance store | `_workspace/05_draft_review.md` |
| `quality-coach` | Read-only "best-self" pass — raises the ceiling; **runs on `full`/`high-stakes` only** (Phase 5b) | `_workspace/05a_coach.md` |
| `citation-verifier` (QA) | Cross-check claims↔sources; score rubric; run audit | `_workspace/06a_verification_report.md`, `06_final_review.md` |
| `lessons-curator` | Phase 7: propose new lessons + evolution-log entry (start-of-run injection is a script) | `_workspace/07_proposed_lessons.md` |

**Model, effort, preloaded skill and tool limits are set in each agent's own frontmatter — do NOT
override them on spawn.** Current allocation: `opus` for `critical-appraiser`, `synthesis-writer`, and
`quality-coach` (deep reasoning / ceiling-raising); `sonnet` for
`evidence-retriever`, `citation-verifier`, and `lessons-curator`. `effort: medium` for the retriever and
curator (tool-heavy, mechanical), `high` for the rest. Each agent preloads its own skill via `skills:`,
so its procedure is in context from the first turn instead of depending on the agent choosing to open
it. `disallowedTools` removes web/MCP search from the writer, coach and curator — provenance-on-disk and
the coach's read-only boundary are enforced by the harness, not by prompt. The lead runs as the
orchestrator session's own model. Change any of these in the agent's frontmatter, not here.

## Directory contract
- `reference/<topic>.md` — **persistent verified-citation store** (PMID/DOI/NCT + date). The writer
  cites ONLY from here, never from memory or a context summary (Law: provenance on disk). One topic =
  one file; check for a near-match before creating a new one.
- `source/<folder>/` — **user-supplied full-text PDFs** (paywalled papers, guidelines). Checked every run.
- `_workspace/` — per-run artifacts, named by the CLAUDE.md contract (`NN` = producing phase). Preserved after the run.
  Includes `06c_manifest.md` — the one-page proof package assembled at delivery (see Phase 6).
- `.claude/skills/lessons-learned/lessons.md` — distilled digest; each agent loads only its role's slice via
  `scripts/lessons_digest.py --role <agent>` (Trigger + Rule, no incident narrative).
- `.claude/skills/lessons-learned/evolution-log.md` — full archive, NOT auto-loaded.

## Phase 0 — Context Check & Scope (always first)
1. Read `.claude/constitution.md` and load your lessons:
   `python3 .claude/skills/lessons-learned/scripts/lessons_digest.py --role orchestrator`.
2. Determine run mode from `_workspace/`:
   - none → fresh review · exists + new topic → move to `_workspace_prev/`, start fresh · exists +
     partial-refine request → re-invoke only the affected agent(s), reuse upstream artifacts.
3. **Confirm the scope and STOP for the user — always, even for a clear topic or a fixed test case.**
   Explicitly ask for and wait on: **purpose** (clinical/research/education), **depth/length**, audience,
   date window, and **output language** (default Vietnamese — confirm or switch). Do NOT infer these from
   the request or a test-case prompt — depth and purpose change the whole review, and guessing them
   violates Law 2. Proceed only after the user answers. (See L-015.)
   - **Ask whether the author has database access beyond the MCP sources** (Scopus, Web of Science,
     Embase, CENTRAL). Ask HERE, not at retrieval: the answer changes the whole search plan, and by
     Phase 2 it is too late to rebuild the strategy around a source you did not know existed. If yes,
     they export the result set to `source/<folder>/_exports/` with a manifest and the retriever
     imports it (P7). Record the answer in `00_scope.md` either way — an unasked question and an
     answered "no" look identical at Gate 2b.
   - **Persist the answer to `_workspace/00_scope.md` the moment it arrives**, quoting the user's own
     words for purpose, depth, audience, date window and language. Phase 0 previously left no artifact
     at all, so "the user confirmed the scope" was a claim with no receipt behind it — exactly R4.
     Every later phase anchors to this file, and the audit quotes it.
   - **Output language is gated like the scope:** it defaults to Vietnamese. Any non-default language
     (e.g. English) requires a **quotable user confirmation** recorded in the protocol/scope file. The
     protocol must NOT set a non-default language on its own in `01_protocol.md`. Absent a quotable
     record, the language **is Vietnamese** — fail closed. (See L-032.)
4. **Tag the effort** `tiny | normal | full | high-stakes` to right-size the *depth of work* (search
   breadth, corpus size, RoB tools, target length, curiosity-budget probes) and decides whether the
   quality-coach runs (Phase 5b: `full`/`high-stakes` only). **The tag never skips a
   gate** — all four human gates run on every level, including `tiny` (constitution: Effort tag). When
   unsure, choose the more careful level.

## Execution Mode: sequential subagents (default)
The pipeline is a chain broken by four human gates, and every hand-off is already a file on disk — so
run each phase as **one foreground `Agent` call** with `subagent_type` set to the specialist. A fresh
subagent per phase starts clean, reads exactly the artifacts it needs, writes its artifact, and exits;
nothing idles while the user is deciding at a gate. The writer⇄verifier loop is the lead re-invoking
the writer with the verifier's FIX/BLOCK list, then re-invoking the verifier on the revised draft.

**Spawn prompt = pointers, not content.** Pass the phase, the topic, the paths of the input artifacts,
the confirmed scope line from `00_scope.md`, and any user decision from the last gate. Do NOT paste
artifact text into the prompt — the subagent reads the file, which is both cheaper and the only way it
sees the real artifact (R5).

**Return contract — append it to every spawn prompt:** *"End with ≤150 words: artifact paths written,
key counts, blocking issues, and anything the user must decide. Do not repeat artifact content."* The
lead's context grows with every subagent report over a long review; the artifacts on disk are the
record, the report is only a pointer. Read an artifact yourself when you need to present it at a gate.

**Subagents cannot ask the user** — `AskUserQuestion` is removed from every subagent. Wherever an
agent's instructions say "ask the user" (which `source/` folders to read, an unavailable source, a
paywalled HIGH record, an Elicit credit spend), the agent puts the question in its report and stops;
the lead asks, records the answer in the relevant artifact, and re-invokes the agent with it. This
also keeps every gate with the lead, the only party that can quote the user's approval.

**Agent Team mode (optional).** If `TeamCreate` is available and the user prefers it, the same six
agents can run as a team (`TaskCreate` with dependencies, `SendMessage` between members). It buys
direct writer⇄verifier messaging at the cost of six persistent contexts that stay open across every
gate wait; the gates and artifacts are identical either way.

**Four stops** where the lead waits for the user: Phase 0 scope, Gate 2b (post-retrieval), Phase 3
Research Map (hard gate), and Gate 4b (post-appraisal).
At every gate: if the user requests changes → fix → ask again. Never fix-then-proceed silently. (L-024)

```
[lead]
  ├── read constitution + lessons_digest.py --role orchestrator (each agent loads its own slice)
  ├── Phase 0  scope confirm ......................... STOP, await user  (L-015)
  ├── Phase 1  protocol — written by the lead (review-protocol skill) → 01_protocol.md + 01a_concepts.json
  ├── Phase 2  retrieval: live sources + source/ folder → reference/<topic>.md
  │            └── Gate 2b: present corpus + full-text status + source gaps .. STOP, await user OK  ← L-022/L-024
  ├── Phase 3  RESEARCH MAP ......................... STOP, await user approval  ← HARD GATE (L-014)
  │            └── persist map to 03_research_map.md, then approval to 03a_gate_approval.md  (L-019)
  ├── Phase 4  appraisal (GRADE/RoB + Assumption Register)
  │            └── Gate 4b: present GRADE summary + contradictions + assumptions . STOP, await user OK  ← L-024
  ├── Phase 5  synthesis (writer cites only from reference store)
  │            └── Phase 5b: full/high-stakes → quality-coach → ≤1 improvement pass · tiny/normal → writer self-check, SKIPPED declared
  ├── Phase 6  verification: claims↔sources + rubric score + audit  (writer⇄verifier loop)
  ├── assemble 06_final_review.md + 06c_manifest.md → deliver with audit report + manifest
  └── Phase 7  lessons-curator proposes lessons + evolution-log entry → user approves → persist (+ TeamDelete in team mode)
```

### Phase detail

**1 · Protocol — written by the lead, no agent spawned.** You already hold the scope conversation
verbatim; a separate agent would have to rebuild it from `00_scope.md` to write a 2–3 page file. Invoke
the `review-protocol` skill and follow it → `01_protocol.md` (research question, PICO, inclusion/
exclusion, per-source search strings, pre-registered outcomes/subgroups, **curiosity budget** of ≥1–2
searches aimed at the 5 gap types) **and** `01a_concepts.json` (the P4 prefilter cannot run without it).
Pre-specification comes from the file being on disk **before** Phase 2 starts — so write both files,
then spawn the retriever; never revise the protocol after seeing results without logging the change
and the reason in `01_protocol.md`. Do not hand protocol-writing to the retriever: an agent that sets
its own strategy and then runs it can quietly bend the strategy toward what was easy to find.

**2 · Retrieval** — `evidence-retriever`: run the strategy across PubMed/PMC + **Elicit** + preprints +
ClinicalTrials.gov + Consensus (+ ChEMBL/Open Targets for drug topics). Elicit's `search_papers` is free to run and widens recall; its `create_systematic_review`/`create_report` **spend user credits and are gated at 2b**. **Then list `source/` subfolders and ask the user
which to read** — do this whether or not files exist (never silent). Write every verified record into
`reference/<topic>.md` with a stable ID; produce `02a_search_log.md` (PRISMA numbers) + `02_corpus.md`,
and the machine-readable `02b_records.jsonl` that the P4 screening pipeline consumes. Then run
`dedupe_records.py` → `prefilter_records.py`, screen the worksheet into `02h_verdicts.jsonl`, and draw
the flow with `prisma_flow.py` (exit 1 when the counts contradict each other).

**Gate 2b (post-retrieval) — STOP, await user OK before Phase 4.** Present: (a) corpus size and PMID status,
(a2) the **PRISMA flow** from `02j_prisma.md` — identified → deduplicated → retracted removed → screened →
excluded with reasons → included — plus how many studies the prefilter **deferred unread**, so the user
can ask for them if the corpus looks thin,
(b) full-text coverage — count HIGH records still abstract-only; if ≥3, list them and ask user to supplement
before proceeding (L-022); (c) source availability gaps — any planned source that was unavailable must be
surfaced here with options: proceed / try WebSearch / user supplies PDFs (L-022). Wait for explicit user OK.
If user requests changes: fix → present update → ask again. Do NOT launch appraisal until OK received. (L-024)

**3 · Research Map — HARD GATE.** The lead, using the corpus + a light landscape pass from the appraiser,
writes the map to `_workspace/03_research_map.md`, presents it, and STOPS for the user. **Write the file
before presenting it** — a map that lives only in a chat turn cannot be re-read by the appraiser, cannot be
diffed when the user asks for changes, and leaves the audit nothing to check the approval against. The Map has 7 parts:
  1. Scope recap (one line, anchored to Phase 0).
  2. World picture — main axes/sub-themes, each tagged `[mature | emerging | contested]` with a landmark
     study/guideline anchor and consensus strength.
  3. Local (Vietnam) picture — is there Vietnamese-population data? If not, label it a population/
     implementation gap. Never fabricate local studies (Law 1).
  4. Research gaps — by the 5 types, each with evidence for *why* it's a gap.
  5. Next directions — each tied to a specific gap.
  6. **Source approval list (must be approved before appraisal/writing)** — every record the team
     would feed to the appraiser, each with: `relevance_tier` (HIGH/MEDIUM/LOW), full-text vs
     abstract-only status, and source type (peer-reviewed / preprint / trial-registry / landmark
     review = Level III). HIGH records that are still abstract-only must be called out (the team
     should have attempted full-text upgrade first; flag any paywalled HIGH record for the user to
     supply). The user **approves, drops, or re-tiers** sources here.
  7. Closing questions — "Which sources are in scope (approve the list)? Which gaps to dig into?
     Keep/drop which axes? Add which searches?"
  **The team does NOT proceed to deep appraisal/writing until the user approves the source list.**
  The appraiser summarizes and the writer writes **only from user-approved sources**. The user's
  comments may loop back to Phase 1/2 for more searching or full-text fetching. Before Phase 4,
  re-confirm one line: "Per your comments I'll use sources [...], drop [...], re-tier [...], dig into
  [gaps], add [search]. Correct?"
  ***"Gate cleared" requires an explicit user approval message received AFTER the map was shown.*** It is
  NOT "small scope," NOT "unambiguous/fixed test-case scope," NOT "standing approval inferred from the
  request." **Presenting the map and proceeding to draft in the same turn is a violation** (v1 Entry #9,
  recurred in v2 Entry #2). The audit must be able to quote the user's approval; if it cannot, the gate is
  NOT cleared and nothing is delivered. (See L-014.) Delivery is sacred only *after* gates are cleared.

**4 · Appraisal** — `critical-appraiser` → `04_appraisal.md`: evidence table, GRADE per outcome, RoB
tool per design, contradictions, gaps, and an **Assumption Register** (every extrapolation logged →
surfaces in Limitations).

**Gate 4b (post-appraisal) — STOP, await user OK before Phase 5.** Present: (a) GRADE certainty per axis
(Strong/Adequate/Thin/Absent), (b) flagged contradictions, (c) key Assumption Register items, (d) the **quote-lock result** from
`04c_quote_locks.md` — how many evidence cards were accepted and how many REJECTED. A rejected card's
claim is not citable, so the user is seeing the real evidence base, not the intended one. Ask: "Có muốn
điều chỉnh gì trước khi viết bài không?" Wait for explicit user OK. If user requests changes: fix → present
update → ask again. Do NOT launch writer until OK received. (L-024)

**5 · Synthesis** — `synthesis-writer` → `05_draft_review.md` in the **confirmed language** (Vietnamese →
load `.claude/skills/review-synthesis/references/vi-terminology.md`), inline Vancouver `[n]`, citing **only** from
`reference/<topic>.md`.

**5b · Coach (best-self, read-only, one pass) — conditional on the effort tag.**
- **`full` / `high-stakes` → run it.** Also run it on any level when the user asks for it.
- **`tiny` / `normal` → do not spawn it.** The writer runs its six-angle self-check before handoff
  (`synthesis-writer.md`), and you write `05a_coach.md` with one line:
  `SKIPPED — effort=<tag>; writer self-check done` (+ the user's words if they waived or asked). The
  skip is declared, never silent (R4, L-025). Why conditional: across runs #7/#8/#10 the coach was
  skipped once, added real depth once, and returned SHIP-AS-IS once — and the two defects the user later
  caught in #8 (calques, a buried PICO subgroup) it missed; both are now writer checks (L-037, L-038). An
  opus pass over the whole draft earns its cost where the bar is highest, not on every review.

When it runs: `quality-coach` reads the draft + appraisal and asks,
across six angles (clarity, depth, completeness, stronger framing, honesty, genuine insight), whether
this is the *best* version the evidence allows — it raises the ceiling, distinct from QA which raises the
floor. It writes `05a_coach.md` and returns `SHIP-AS-IS` or `ONE-IMPROVEMENT-PASS`. If the latter, send
the named changes back to `synthesis-writer` **once**, then proceed to verification. The coach is
read-only and never edits the draft or touches citation correctness (that is QA's job). It must stay
within the user-approved scope (no new axes). Keep it one pass, not a loop (R6).

**6 · Verification (QA, incremental)** — `citation-verifier`: cross-check each claim against its source
section-by-section; then **score the rubric** (`references/rubric.md`) and **run the audit**
(`references/audit.md`). Writer fixes FIX/BLOCK items; loop until PASS → `06_final_review.md`. Deliver
with the audit report (rubric total + band + violations). Fabricated citation or uncleared gate → do
NOT deliver.

**Manifest (proof package) — assembled by the lead at delivery → `_workspace/06c_manifest.md`.** A single
one-page cover sheet the user reads instead of digging through five artifacts. It contains:
  1. **Scope line** — purpose, audience, depth, language, effort tag, date window (anchored to Phase 0).
  2. **Confidence list** — each *major* claim/finding with its GRADE certainty and its primary source ID
     (PMID/DOI/NCT). Built from the appraisal + verification report, not re-derived from memory.
  3. **Open assumptions** — the Assumption Register items that survived into the final review (Law 5).
  4. **Receipts index** — the artifacts that prove each step ran (`00`…`06`, `04b`, gate-approval file),
     plus the rubric total + band and any recorded violations.
  Honest limit: the manifest indexes that the steps ran and what was found; it does not re-vouch for
  thoroughness — that is the verifier's verdict (Phase 6) and the human gates.

**7 · Learn** — `lessons-curator`: draft `07_proposed_lessons.md` from QA defects + user feedback and an
`evolution-log.md` entry; present to the user; on approval append lessons to `lessons.md` and the entry
to `evolution-log.md`.

## Error Handling
- **MCP source fails:** retriever retries once. If still failing → **STOP and ask the user** (do NOT silently
  continue): "Source X unavailable. Options: (a) proceed without it + note gap; (b) try WebSearch fallback;
  (c) you supply materials." Wait for choice; record decision in search log. (L-022) *(Known: Consensus
  tool-ID can drift per session — resolve via ToolSearch "consensus search"; Consensus years may differ from
  PubMed, confirm PMIDs separately.)*
- **Agent fails/returns nothing:** retry once; else proceed without it and note the omission in Limitations.
- **Conflicting evidence:** never delete the minority finding — appraiser documents the conflict, both cited.
- **Unverifiable citation:** QA marks BLOCK; the claim is corrected or removed.

## Team Size
Six specialists (four always run: retriever, appraiser, writer, verifier; the coach on `full`/`high-stakes`;
the curator at Phase 7), one task chain; keep each agent's tasks within its phase to limit coordination
overhead (R6 — too many cooks). The protocol is the lead's own work: a separate strategist agent had to
re-derive the scope the lead already held, and pre-specification comes from the file on disk, not from a
separate author. Keep the four core separations — retrieval (context isolation), appraisal (deep
judgment), and above all writer ≠ verifier (generation never clears its own citations). **Four human gates** (scope, post-retrieval, Research Map,
post-appraisal) are where quality is won cheaply — never skip or self-clear any of them, on any effort level.

## Test Scenarios
**Normal:** "Tổng quan chuyên sâu về GLP-1 RA cho béo phì không đái tháo đường, tập trung kết cục tim
mạch, cho BS nội tiết, ~2500 từ." → Phase 0 scope+language confirm → protocol+curiosity budget →
retrieval + source/ ask → **Research Map → STOP for approval** → GRADE appraisal + assumption register →
Vietnamese draft citing only the reference store → QA cross-check + rubric (e.g. 0.78 MET) + audit →
delivered with audit report → lessons + evolution-log entry proposed.

**Error:** ClinicalTrials.gov MCP rate-limits → retriever retries once, fails → **STOP at Gate 2b** and
presents to user: "CT.gov unavailable. Proceed without / try WebSearch / supply NCT list?" → user chooses
→ decision recorded in search log → appraiser notes possible unpublished-trial bias → writer adds to
Limitations → audit records coverage gap honestly. (L-022)

**Gate test:** user gives a "small" topic and says "just write it." → lead still presents the Research
Map and STOPS — the gate has no small-scope exception (v1's most expensive repeated lesson).

**Follow-up:** "The appraisal was too shallow on risk of bias — redo it." → Phase 0 detects existing
`_workspace/` + partial-refine → re-invoke only `critical-appraiser` on the existing corpus → writer
updates affected claims → QA re-verifies + re-scores changed sections.

## Regression safety (after editing the harness)
When the harness itself changes (new agent, changed skill, reworded constitution), run the checks in
this order — cheapest first.

**1 · Automated suite (seconds, always).** `python3 -m unittest discover -s .claude/tests -t .claude/tests`
must exit 0 before anything else. It pins the deterministic layer's thresholds and every HARD-FAIL
category, and it catches the two structural bugs this harness has actually shipped: an agent the
orchestrator spawns but no file defines, and a rule citing a lesson ID that resolves to nothing. It is
mechanical and cannot be talked past. A red suite means stop and fix, never "proceed and note it".

**2 · Qualitative cases (minutes to hours).** Then guard *judgment* quality with
`references/test-cases.md` — 3 fixed cases (EASY / HARD / EDGE) + a qualitative ratchet. The suite
proves the harness is still wired correctly; only these prove it still reviews well.
Minimum after any edit: run the cheap **EDGE** case (it must refuse to proceed without scope — tests the
gate + Law 2 in seconds). For edits touching retrieval/appraisal/synthesis, run one full case end-to-end
and have the verifier compare **per-criterion rubric + law/gate checks** to the prior run's evolution-log
entry — keep only if no criterion or check regressed. One change at a time.

**`test-cases.md` is for whoever grades a run, never for the run.** It contains each case's pass
criteria — and for the HARD case, content the review is expected to find. A lead or agent that reads it
while running a review is sitting an open-book exam, and the result stops being evidence. So: do **not**
open `references/test-cases.md` during a review, even when the request looks like one of its cases.
Grading happens afterwards, in the same or another session, by reading the run's artifacts. If it was
opened during a run anyway, say so in the run's report and evolution-log entry (the 2026-10-27 Case 3
re-check is the precedent).

## Why this design
Generation and verification live in different agents, so the writer never clears its own citations —
this catches hallucinated references that a self-grading single agent would protect. The read-only
quality-coach sits between them to raise the ceiling (depth/insight) before QA raises the floor
(correctness), so "correct" is not mistaken for "best." The Research Map
gate puts a human checkpoint before expensive work. Provenance-on-disk severs citations from fallible
memory. The two-tier learning loop (digest + archive) makes mistakes non-recurring. Live MCP sources
(incl. preprints + trial registry) keep reviews current.
