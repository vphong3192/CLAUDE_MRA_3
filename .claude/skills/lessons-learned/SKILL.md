---
name: lessons-learned
description: Select relevant medical-review lessons and propose new reusable lessons from actual defects or user feedback. Lead owns this skill; no curator agent.
---
# Lessons
`lessons.md` is the approved digest; `evolution-log.md` is historical and never auto-loaded.
At phase entry lead runs the orchestrator's `scripts/select_lessons.py` with roles and scopes.
Select Role intersection AND Scope intersection; universal and unknown scopes stay included.
Add vi-language for Vietnamese output and cardiology-ep only when applicable. Pass the resulting
IDs, rules and rationale to the worker; do not make every worker reread the full file. Legacy role
aliases are supported. Filtering is deterministic; topic judgment belongs to lead.

At completion record outcome/defects in run state. No new reusable insight → no_new_lesson and finish.
For a new lesson or material recurring failure, read the relevant existing entry and propose a merge
or addition in `_workspace/07_proposed_lessons.md`, with a short evolution entry. Format: ID, Role,
Scope, Trigger, Rule, Why, Origin. Each rule needs observed evidence and a reusable trigger; no
study-specific facts promoted as policy. Bundle approval with delivery. After explicit approval,
save lessons, evolution entry and approved terminology. Never silently persist new cross-run rules.
