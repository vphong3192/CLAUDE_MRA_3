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

**Two human gates:** (1) Phase-0 scope confirm; (2) Phase-3 **Research Map** — the team STOPS and waits
for approval before deep appraisal/writing. The gate has no small-scope exception.

**Directory contract:**
- `reference/<topic>.md` — persistent verified-citation store; the writer cites ONLY from here.
- `source/<folder>/` — user-supplied full-text PDFs; checked and asked-about every run.
- `_workspace/` — per-run artifacts (preserved for audit / partial re-runs).
- `.claude/skills/lessons-learned/lessons.md` — distilled digest (injected each run) ·
  `evolution-log.md` — full archive (not auto-loaded).

**Config defaults:** systematic rigor (PRISMA + GRADE) · Vancouver citations · **output language
defaults to Vietnamese but is user-selectable per review** (confirm in Phase 0) · lessons saved only
after user approval.

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
