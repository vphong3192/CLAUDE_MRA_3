# Medical-review harness
For a medical literature review or a revision/audit of one, read
`.claude/skills/medical-review-orchestrator/SKILL.md`. Single factual questions and repository
maintenance do not trigger a review. Native Claude agent definitions remain in `.claude/agents/`;
other hosts should use these role files with their available subagent tools and record actual models.

Change: 2026-09-07 — four agents including lead; two required gates; conditional appraisal/coach;
claim-to-card checks and paired evaluation. Details: `docs/lean-harness-evaluation.md`.
