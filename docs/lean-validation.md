# Candidate validation — 2026-09-07

Base: `ad6477b52e94f70c8befd615adc5d7c0df7bbd5a`.
Candidate branch: `codex/lean-four-agent-harness`.

## Executed
- Windows, bundled Python, `PYTHONUTF8=1`.
- `python -m unittest discover -s .claude/tests -t .claude/tests`: **220 tests, PASS**.
- `git diff --check`: no whitespace errors.
- Lesson-selector CLI smoke: appraiser + universal/vi-language selected 6 lessons; output written
  outside the repository so test artifacts do not become study data on the harness branch.
- Claim-link tests exercise actual CLI files and corrupt JSON; reject stale draft text, changed draft
  numbers even when link text is refreshed, dangling/orphan/duplicate links, wrong bibliography,
  missing fulltext abstract, rejected quotes and path traversal. Supported table rows pass.
- Manifest tests reject changed map/draft/card/source, pending decisions, missing coach receipt and
  failed/unbound claim reports. Explicitly does not authenticate human receipts or certify semantics.
- Paired-evaluation tests reject incompatible frozen inputs/settings, invalid measurements and
  duplicates; null usage/human scoring stays incomplete; critical errors cannot be offset by savings.

Baseline Windows run (before changes) had 174 tests, with 4 fixture-path errors and 2 encoding failures.
Fixture lookup now uses pathlib; documented PYTHONUTF8=1 also applies to subprocesses. Existing
scientific/checker assertions and thresholds were retained.

## Static size observations, NOT runtime usage
| File | Baseline characters | Candidate characters |
|---|---:|---:|
| CLAUDE.md | 30,294 | 4,607 |
| orchestrator SKILL.md | 20,781 | 12,518 |

Counts are UTF-8-decoded text character lengths compared with baseline git objects. Historical
content is retained in docs/history.md. Smaller automatically read text does not by itself establish
review token/cost savings, especially with the new claim-link artifact and stronger verifier default.

## Still pending
- Live model/user gate behavior, including full scope without repeat questions and pending Map approval.
- Frozen-corpus EASY/HARD/missing-fulltext reviews with real user approvals and blinded human assessment.
- Live retrieval comparison and >=3 paired repeats per case for stable usage observations.
- Actual per-model token/cache/cost/latency measurements. No percentage saving or clinical
  non-inferiority is claimed. Mechanical tests do not substitute for these evaluations.

Use docs/lean-harness-evaluation.md and evals/lean/runs.template.json to complete these trials.
Keep this branch as a candidate until the human assessment and actual usage support adoption.
