# CLAUDE_MRA_2

## Harness: Medical Literature Review

**Goal:** Produce high-quality, in-depth, systematic-style medical literature reviews from live,
up-to-date sources (PubMed/PMC, bioRxiv/medRxiv, ClinicalTrials.gov, Consensus), with a constitution,
a human-approved Research Map gate, provenance-on-disk, rubric+audit scoring, and a learning loop.

**Constitution:** `.claude/constitution.md` — the 6 immutable Laws bind every agent. Law 1 (no
fabricated citations → auto-fail) and the Research Map hard gate are non-negotiable.

**Trigger:** For any request to write, update, expand, redo, score, or audit a medical/clinical/
biomedical literature review (or "review the evidence on <topic>"), use the
`medical-review-orchestrator` skill. It runs a 7-agent team (strategist → retriever → appraiser →
writer → coach → verifier, plus a lessons-curator). A single factual medical question is answered directly.

**Four human gates:** (1) Phase-0 scope confirm; (2) Gate 2b post-retrieval (corpus + full-text/source
gaps, L-022/L-024); (3) Phase-3 **Research Map** — the **hard gate**; (4) Gate 4b post-appraisal (GRADE +
contradictions + assumptions, L-024). All four run on every effort level (incl. `tiny`); the Research Map
hard gate has no small-scope exception. The team STOPS and waits for explicit user approval at each.

**Directory contract:**
- `reference/<topic>.md` — persistent verified-citation store; the writer cites ONLY from here.
- `source/<folder>/` — user-supplied full-text PDFs; checked and asked-about every run.
- `_workspace/` — per-run artifacts (preserved for audit / partial re-runs).
- `.claude/skills/lessons-learned/lessons.md` — distilled digest (injected each run) ·
  `evolution-log.md` — full archive (not auto-loaded).

**Config defaults:** systematic rigor (PRISMA + GRADE) · Vancouver citations · **output language
defaults to Vietnamese but is user-selectable per review** (confirm in Phase 0) · lessons saved only
after user approval.

**Workflow — branch-per-study (repo hygiene):** The harness on `main` is the reusable tool; each
research project is its own data. For every new review: (1) `git checkout main && git pull && git
checkout -b review/<topic>` so the branch inherits the latest harness + lessons; (2) run the harness on
that branch — `source/`, `reference/<topic>.md`, and `reviews/<topic>/` land here and are committed to
the branch; (3) when done and the user has approved the lessons, update `main` with a *small* commit
touching ONLY the three cross-session knowledge files — `lessons.md`, `evolution-log.md`, and
`vi-terminology.md` (the glossary is part of "the lesson"; omitting it lets terminology errors recur);
(4) keep `review/<topic>` as the permanent archive of that study — do NOT merge it into `main`. Always
branch from a fresh `main` so each study starts with the newest lessons. (Note: branching keeps *future*
checkouts light but does not shrink `.git` history; that is acceptable on a private repo.)

**Change log:**
| Date | Change | Target | Reason |
|------|--------|--------|--------|
| 2026-06-13 | Initial build — 6 agents, 7 skills, orchestrator, seeded lessons store | full harness | - |
| 2026-06-13 | Ported v1 (CLAUDE_MRA) disciplines: constitution (6 Laws), Research Map hard gate, provenance store + `source/` folder, rubric + audit, two-tier learning (evolution-log), curiosity budget + assumption register, Vietnamese default + verified terminology glossary | constitution, orchestrator, all agents/skills, new references | Learn from battle-tested v1; keep v2's multi-agent + GRADE/PRISMA + live trial-registry edge |
| 2026-06-14 | Live test review run to the Research Map gate (GLP-1 case) — validated retrieval, error-retry, provenance store, and the gate | _workspace/, reference/ | Verify the harness end-to-end |
| 2026-06-14 | Added lightweight regression layer: 3 fixed test cases + qualitative ratchet (per-criterion + law/gate, no brittle 0.01 numeric gate) | orchestrator references/test-cases.md | Guard against quality regression as the harness evolves, without v1's costly AutoTest |
| 2026-06-14 | First full review completed (semaglutide CV prevention, MET 0.82); learning loop closed — 5 lessons (L-008…L-012) + evolution-log Entry #1 + 6 glossary terms approved and saved; run recorded as Test Case 2 baseline | lessons.md, evolution-log.md, vi-terminology.md | Validate end-to-end incl. the human-approved learning loop |
| 2026-06-14 | Test Case 1 (metformin EASY) run; L-013 + evolution-log Entry #2 saved | lessons.md, evolution-log.md | Seed the EASY baseline; validate the ratchet |
| 2026-06-14 | **Correction (user-caught):** TC1 self-cleared the Research Map gate and assumed Phase-0 scope; QA falsely recorded "gate cleared." Corrected records (Entry #2, TC1 audit → process FAIL, score 0.84→0.81, baseline PROVISIONAL); hardened Phase 0 + Phase 3 + audit (gate-cleared now requires a quotable user approval; fail closed); added L-014 (gate no exception) + L-015 (always ask depth/purpose before writing) | orchestrator SKILL.md, audit.md, lessons.md, evolution-log.md, TC1 QA | Honor the two human gates; stop the audit from laundering gate breaches |
| 2026-06-14 | Properly-gated metformin re-run (Entry #3): Phase-0 confirmed (user changed depth 1500→500w), Research Map approved via quotable "approve" before drafting; MET 0.81 | evolution-log.md | Positive evidence the gate corrections hold |
| 2026-06-23 | Harness fix + PR salvage: added missing `quality-coach` agent (was spawned but undefined → would break TeamCreate); unified `vi-terminology` to one canonical file; replaced blanket all-opus spawn rule with per-agent frontmatter allocation; fixed dead `(L-023)`→`L-022` pointer. Repo set **PRIVATE** (resolves full-text copyright exposure; no history rewrite needed). Salvaged two completed reviews into `reviews/<topic>/` (LA-EP elderly AF ← PR#2; cryoballoon-vs-PFA ← PR#3) plus their `reference/` stores & `source/` corpora; pulled PR#3 harness upgrades (anti-hedging + steelman in constitution; steelman/calibration in rubric; coach+manifest checks in audit). Closed PRs #1 (superseded), #2, #3. | CLAUDE.md, constitution.md, orchestrator, quality-coach.md, rubric.md, audit.md, reviews/, reference/, source/ | Make the harness runnable as documented; preserve finished reviews durably; keep gate + fix integrity |
| 2026-06-23 | Completed the PR#3 steelman/anti-hedging theme across the pipeline: added a **Steelman the opposing case** principle to `critical-appraiser` and a both-directions language-calibration + **Steelman before you conclude** bullet to `synthesis-writer` (the appraiser/writer halves of the constitution+rubric+audit changes already merged). Documented the **branch-per-study** workflow (study data on `review/<topic>` branches; only `lessons.md`+`evolution-log.md`+`vi-terminology.md` flow back to `main`). | critical-appraiser.md, synthesis-writer.md, CLAUDE.md | Make steelman/calibration consistent end-to-end; codify repo-hygiene workflow |
| 2026-06-29 | **P1 — Deterministic citation audit** (borrowed aglr-med's tactic, not its shallowness): added `scripts/citation_audit.py` (Python stdlib, zero-dep, no LLM/network, identical output run-to-run) as a mandatory traceability floor that runs AFTER the LLM citation-verifier and cannot be talked past — HARD-FAIL on `fabricated_citation`/`missing_in_store`/`placeholder_leftover`/`coverage_below_threshold` (exit 1, Law 1 not-deliverable); WARN on `number_not_in_source`/`uncited_claim`. Format-agnostic (keys on PMID/DOI/NCT; handles both `[REF-NNN]` and table-style stores; Vietnamese decimal commas). Regression: both completed reviews PASS deterministically, 0 false HARD-FAILs; FAIL-path fixtures included. Wired into citation-verifier agent + SKILL.md + audit.md. Branch `claude/mra-deterministic-layer-n0t4yj`. | citation-verifier.md, citation-verification/SKILL.md, .../references/audit.md, .../scripts/, CLAUDE.md | Close the gate-laundering hole: pull mechanical citation checks out of the LLM's hands into a layer that can't self-persuade |
| 2026-06-29 | **P2 — Deterministic number extraction for appraisal**: added `evidence-appraisal/scripts/extract_numbers.py` (Python stdlib, zero-dep, no LLM/network) that pulls VERBATIM numbers from `reference/<topic>.md` into five typed buckets per record — `sample_sizes·percentages·p_values·confidence_intervals·ratios` (OR/RR/HR/aHR/MD/SMD/β/coef). The appraiser now LOADS evidence-table numbers from `_workspace/03b_numbers.md` instead of hand-copying (kills the broken-decimal / Methods-as-result Law-1 hazard); all interpretation (which number is the graded result, RoB, GRADE, mean±SD) stays with the LLM. Metadata (PMID/DOI/URL/date) scrubbed as spans so a findings line ending in "(Source: …DOI…)" keeps its numbers; word-boundary guards stop "Circ" matching "CI". Deterministic on both stores (identical reruns); empty bucket = "(none)", never a placeholder. Wired into evidence-appraisal SKILL §4 + critical-appraiser agent. | evidence-appraisal/SKILL.md, critical-appraiser.md, evidence-appraisal/scripts/, CLAUDE.md | Take the mechanical number-copying out of the LLM's hands; keep the depth of judgment with it |
| 2026-06-29 | **P3 — Recall proof + reproducibility for search**: codified three retriever habits — (1) cheap **count-target probe first** (`esearch retmax=0` / `countTotal=true`) before pulling, (2) **paginate to `retrieved==total`** or cap with a logged reason (a one-page MCP pull must not pose as complete), (3) log the **reproducible call** (params/URL), not just the human query — emitted as a fixed **"Recall & reproducibility ledger"** table. Added `literature-retrieval/scripts/validate_search_log.py` (Python stdlib, zero-dep, no LLM/network, offline) that HARD-FAILs (exit 1) on a missing ledger, missing column, non-integer count, a `call` with no params/URL, or a recall verdict inconsistent with the numbers. Format-check only (completeness/self-consistency, NOT whether counts are true or sources well-chosen); multi-source breadth unchanged. Valid/invalid fixtures included; deterministic (identical reruns). Wired into literature-retrieval SKILL + evidence-retriever agent. | literature-retrieval/SKILL.md, evidence-retriever.md, literature-retrieval/scripts/, CLAUDE.md | Make recall claims auditable — pull the "did you get everything / can it be rebuilt" check out of the LLM's narration into a layer that can't be implied past |
