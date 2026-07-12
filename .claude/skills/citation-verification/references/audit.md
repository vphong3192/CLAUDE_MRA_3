# audit.md — Pre-delivery self-audit checklist

The verifier runs this audit and produces a structured report **before** the lead reports "done." The
audit is structured accounting, not a vibe check. Ported from v1, adapted to the team workflow.

> Load this only at the audit step (verifier), alongside rubric.md.

## Part A.0 — Deterministic citation pre-flight (run first, machine verdict)
Before any judgement call, run the deterministic checker (`scripts/citation_audit.py`, see
`SKILL.md`) on the final draft + `reference/<topic>.md`. It is the floor your prose cannot argue
past: a HARD-FAIL (`fabricated_citation` / `missing_in_store` / `placeholder_leftover` /
`coverage_below_threshold`, exit 1) means **NOT deliverable** (Law 1) — fix, then re-run to a clean
exit 0. WARNs (`number_not_in_source`, `uncited_claim`) are routed into your spot-check, not blocking.
This is **traceability only** — it does not read meaning, so it never replaces Part B's Law-1
spot-check; record both. Paste the checker's verdict line into the report.

## Part A — Process audit
Mark PASS / FAIL / SKIPPED with evidence per phase:
- **Protocol** — research question + PICO + inclusion/exclusion + search strategy written? (evidence: quote scope)
- **Retrieval** — ≥2 independent sources? curiosity-budget gap search run? `source/` folder checked and user asked?
- **Research Map (HARD GATE — also the corpus/source review)** — map presented with gaps + Vietnam/local picture **and the corpus/source-approval section** (corpus size + PMID status, abstract-only HIGH records flagged, any unavailable source surfaced — the old Gate 2b content, now folded in)? **Quote the user's explicit approval message received after the map was shown.** No quotable approval → gate is **NOT cleared** (fail closed) → **not deliverable**, regardless of how clear the scope seemed. Inferred/"standing"/"fixed-scope" approval does not count. Also confirm a Phase-0 scope confirmation (purpose + depth) was obtained before searching.
- **Appraisal** — Assumption Register written? RoB tool + GRADE applied?
- **Synthesis** — grouped by sub-theme (not listing)? consensus vs. controversy counted? language calibrated **both ways** (no Low/Very-Low stated as fact; no High/Moderate buried in weasel hedges)? each major conclusion **steelmanned** before concluding (strongest opposing case stated, not false balance)? **every pre-registered PICO subgroup (AF type, age strata, first-vs-redo, etc.) given an explicit, locatable treatment where data exist — and any subgroup that is a key effect modifier for the target population foregrounded, not buried (L-038)?**
- **Coach pass (conditional)** — for `full`/`high-stakes`: `04b_coach.md` exists with a verdict, and if `ONE-IMPROVEMENT-PASS` was the one pass applied? For `normal`/`tiny`: a declared skip `04b_coach_skip.md` exists naming the effort tag (L-025). Either the ran-artifact or the declared-skip artifact must be present — a silent absence is R4.
- **Draft** — full standard structure? every claim cited inline from `reference/<topic>.md`?
- **Manifest** — `08_manifest.md` assembled at delivery (scope line + confidence list + open assumptions + receipts index)? Numbers/grades trace to appraisal + verification, not re-derived from memory.

## Part B — Law-compliance audit
Check the 6 Laws (see `.claude/constitution.md`):
- **Law 1** — spot-check 3–5 citations: author+year+journal real? PMID/DOI/NCT resolves? no unsourced numbers?
- **Law 2** — output matches the requested scope (not widened/narrowed)? audience matches technical level?
- **Law 3** — high-tier sources prioritized? conflicts stated?
- **Law 4** — separate "consensus" and "controversy" sections? no controversy presented as consensus?
- **Law 5** — "Limitations" section present with search scope, language, bias?
- **Law 6** — evolution-log entry prepared? reusable knowledge captured?

## Part C — Scope integrity
Compare output to the Phase-0 scope: right topic? right depth/length? right audience? no unrequested
additions/removals? *(self-changed scope = serious violation — report it.)*

## Part D — Audit report format
```
═══════════════════════════════════════
AUDIT REPORT — <task>
RUBRIC TOTAL: <0.XX> → <band>
  T1 Search <0.X> — <reason>      T4 Appraisal <0.X> — <reason>
  T2 Quality <0.X> — <reason>     T5 Citation <0.X> — <reason>
  T3 Synthesis <0.X> — <reason>   T6 Applicability <0.X> — <reason>
PROCESS: <X phases PASS>   LAWS: <Y/6 PASS>   SCOPE: <PASS/FAIL>
DETERMINISTIC CITATION AUDIT: <PASS / FAIL — categories> (exit <0/1>)
RESEARCH MAP GATE: <CLEARED / NOT CLEARED>
VIOLATIONS: <list>
SELF-UPDATE PROPOSALS: <evolution-log entry · lessons to propose · skill/constitution change>
DECISION:
  [ ] Deliver — no violations
  [ ] Deliver — violations present, await user decision
  [ ] DO NOT deliver — fabricated citation or uncleared gate → fix first
═══════════════════════════════════════
```

## Supreme rules
- **Fabricated citation (Law 1) → do NOT deliver.** Stop, report, redo that part.
- **Output meets rubric but process violated → still deliver** (delivery is sacred), with the violation
  report attached — *unless* the Research Map gate was never cleared.
- **Never self-justify.** Finding a violation means reporting it, not excusing it.
