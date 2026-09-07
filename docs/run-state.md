# Run state and generated views

Lead writes `00a_run.json`. It records actual decisions, never invents user replies or model usage.
Use null for unknown usage. Update state on each decision, not each tool call. Historical revisions
and invalidated artifacts can be recorded in `revisions`; worker/model settings in `workers`.

```json
{
  "run_id": "topic-2026-09-07",
  "scope": {"status": "approved", "receipt": "Actual user message text/id; explicit prompt values count"},
  "research_map": {"status": "pending", "receipt": null, "sha256": null},
  "appraisal_decision": {"status": "pending", "reason": "Not appraised yet"},
  "coach": {"status": "not_needed", "reason": "No concrete editorial need"},
  "qa": {"status": "pending", "draft_sha256": null},
  "learning": {"status": "pending"},
  "workers": [],
  "usage": null,
  "revisions": []
}
```

Research Map approval must have the actual post-presentation reply and SHA-256 of the approved map.
Compute hashes with `Get-FileHash -Algorithm SHA256 FILE` in PowerShell (store lowercase), or `sha256sum FILE`.
Appraisal decision: `not_needed` + reason, or `pending` until actual reply then `approved` + reason + receipt.
Coach: `not_needed` + reason, or `completed` + reason with `05a_coach.md` present.
QA: verifier's actual PASS on final draft and its lowercase SHA-256; blocked/unfinished stays pending/FAIL.
Learning: no_new_lesson / proposed / approved. Do not write global lessons until approved.

At phase entry (role selectors: lead, retriever, appraiser, verifier, coach):
```bash
python .claude/skills/medical-review-orchestrator/scripts/select_lessons.py --roles appraiser --scopes universal vi-language cardiology-ep --out _workspace/00b_lessons.md
```
Only add cardiology-ep for matching topics. Selector reads the digest once and emits relevant rules;
it includes untagged/unknown-scope lessons conservatively. This output can be overwritten per phase.

Cards additionally carry `outcome` and `certainty` (High/Moderate/Low/Very Low/not_assessed).
Optional design/sample_size/effect/rob support a table without retyping. Certainty refers to the outcome
body of evidence, not a new rating computed per card. Detailed judgments/reasons stay in appraisal.
```bash
python .claude/skills/medical-review-orchestrator/scripts/render_artifacts.py evidence --cards _workspace/04b_cards.jsonl --out _workspace/04d_evidence_table.md
python .claude/skills/medical-review-orchestrator/scripts/render_artifacts.py manifest --workspace _workspace --store reference/TOPIC.md --source-dir source/TOPIC --out _workspace/06c_manifest.md
```
Evidence view has one row per card (not a study count). Manifest indexes decisions, source IDs, certainty,
assumptions and current artifact hashes; rejects missing mandatory artifacts or changed approved map/final
draft. It does not authenticate an agent-authored receipt or replace rerunning checks. Run all required
checks immediately before manifest, without intervening edits. There is no host-enforced delivery hook.
