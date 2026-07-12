---
name: lessons-learned
description: >
  The learning-from-mistakes memory for the medical review harness. Loads the persistent lessons
  store and injects role-tagged rules at the start of every review; collects defects (from QA) and
  user feedback at the end, drafts generalized lessons, and — after human approval — appends them to
  the store. Used by the lessons-curator agent, and whenever the user wants to record a mistake,
  review proposed lessons, or see what the harness has learned.
---

# Lessons Learned

The mechanism that stops the team repeating mistakes. **Two tiers:**
- `lessons.md` — distilled, role-tagged "When X → do Y" digest, injected every run.
- `evolution-log.md` — the full per-run archive (task, rubric result, violations, lessons, actions);
  NOT auto-loaded; read it to investigate patterns or to append a new entry.

This harness is configured for **review-before-apply**: new lessons and log entries are proposed to
the user, never silently saved. A rule enters the digest only after it has an evolution-log entry
behind it and the user approved it.

## Two phases

### Inject (start of every run)
1. Read `lessons.md`.
2. **Select by `Scope:` ∩ `Role:` — never inject the whole file.** Load only lessons whose
   `Scope:` matches this run — `universal` (always) **+** `vi-language` (only when output is
   Vietnamese/non-English, the default) **+** `cardiology-ep` (only when the topic is cardiac /
   electrophysiology / arrhythmia). Then route each selected lesson to the agent(s) in its `Role:`
   line. This keeps each agent's set to a handful, so the store can grow without growing per-run weight.
3. Post a **role-tagged digest** to the team so each agent applies its own lessons. Format:
   `[writer] L-002: match language strength to GRADE certainty.`

### Capture (end of run)
1. Read `_workspace/05_verification_report.md` (QA defect categories + rubric/audit) + any user feedback relayed by the lead.
2. Draft an **evolution-log entry** (task, rubric total + band, violations, lessons, actions) and, for each recurring/important defect, a **generalized** digest lesson (see format).
3. Write both to `_workspace/07_proposed_lessons.md`.
4. Present to the user for **approve / edit / reject**.
5. On approval: append the entry to `evolution-log.md`, approved lessons to `lessons.md`, and any user-confirmed Vietnamese terms to `.claude/skills/review-synthesis/references/vi-terminology.md`. Record rejected proposals so they aren't re-surfaced.

## Lesson format
```
### L-<id>: <short title>
- **Role:** strategist | retriever | appraiser | writer | verifier | orchestrator · **Scope:** universal | vi-language | cardiology-ep
- **Trigger:** when this applies
- **Rule:** what to do
- **Why:** the rationale (so it transfers to new cases)
- **Origin:** run date / the defect that prompted it
```
Choose `Scope:` by the *rule's* generality, not the origin run's domain: tag `universal` when the
rule transfers across specialties (let a domain example illustrate it); tag `cardiology-ep` only when
the rule itself is cardiac-specific (voltage-modality thresholds, named-trial subgroups); tag
`vi-language` for Vietnamese/non-English composition rules.

## Generalize, never overfit
A lesson must be a reusable rule, not a note about one paper.
- ❌ "PMID 12345 was miscited in the statin review."
- ✅ "When citing an effect size, copy the CI from the source's results table, not the abstract's
  rounded summary — abstracts frequently round or omit the interval." `[verifier]`

A lesson without its *why* won't transfer; always include the rationale.

## Maintain the store
Before adding, check for an existing lesson that covers it — strengthen that one instead of
duplicating. Retire lessons proven wrong or obsolete. Keep each lesson one fact, role-tagged, so the
inject step can load only what's relevant.

## Why human approval
Auto-applying every observed quirk risks overfitting the harness to one bad run. Human review keeps
the store to durable, generalizable rules — which is exactly what makes them safe to auto-inject
later.
