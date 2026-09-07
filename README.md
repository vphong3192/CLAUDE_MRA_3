# CLAUDE_MRA_3 — lean medical-review harness

**4 agents including the lead · 2 required gates · independent QA · offline deterministic checks.**
Candidate revision: 2026-09-07, based on `ad6477b5`. Runtime token savings and clinical quality are
not yet established by full A/B reviews; see [evaluation guide](docs/lean-harness-evaluation.md).

## Workflow
Scope → lead protocol → retriever search/screen/PRISMA → **Research Map + corpus approval** →
appraisal → lead synthesis → independent verification → final Markdown + audit + manifest.

Explicit scope values in your prompt count; only missing/conflicting details are asked again.
Vietnamese is default. Research Map always waits for approval after presentation. Appraisal pauses
only for material decisions; coach runs only for a concrete editorial need. Lead captures useful
lessons without a curator worker, and asks before saving cross-study knowledge.

## What remains rigorous
- Citation store on disk; RoB/GRADE, contradictions, subgroup effects and Assumption Register.
- P1 citation audit; P2 number extraction; P3 reproducibility-log validation; P4 dedupe/screen/PRISMA;
  P7 author-export import; P8 source quote/number locks; plus draft→card→citation linkage checks.
- A separate verifier reads original sources; mechanical PASS never substitutes for semantic support.
- All deterministic scripts use Python standard library, no network/LLM. Paid retrieval needs explicit
  authorization. PDFs need text/HTML; agent transcripts are labelled with their weaker provenance.

## Start
Open a fresh `review/<topic>` branch from this harness version and ask, for example:
> Tổng quan về [chủ đề]. Mục đích: nghiên cứu; người đọc: [đối tượng]; khoảng 2000 từ;
> tài liệu 2020–2026-09-07; tiếng Việt; source/[topic] là thư mục tài liệu; không có export ngoài.

The lead uses [orchestrator](.claude/skills/medical-review-orchestrator/SKILL.md).
Operational contract: [CLAUDE.md](CLAUDE.md). State/rendering: [run-state](docs/run-state.md).
Claim format: [claim links](docs/claim-links.md). History: [history](docs/history.md).

## Test
Python 3.10+. On Windows PowerShell first set `$env:PYTHONUTF8 = "1"`.
```bash
python -m unittest discover -s .claude/tests -t .claude/tests
```
Follow [the Vietnamese A/B guide](docs/lean-harness-evaluation.md) for paired runs and actual usage.
`main` remains reusable; study data stays on study branches. `06_final_review.md` is the deliverable;
there is no required Word/Pandoc export layer.
