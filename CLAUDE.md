# CLAUDE_MRA_3 — lean harness

For writing, updating, expanding or auditing a medical literature review, use
`.claude/skills/medical-review-orchestrator/SKILL.md`. Single medical facts and maintenance of
this repository are not review runs. Read `.claude/constitution.md` for shared invariants.

Four default agents INCLUDING the lead: lead does protocol, synthesis and learning; retriever,
appraiser and independent verifier have separate contexts. Optional coach only on a concrete need.
Two required gates: scope (explicit prompt values count), then Research Map + corpus approval.
Appraisal pauses only on a material decision. Full operational policy is in the orchestrator.

Default output: Vietnamese, Vancouver, PRISMA/GRADE with honest limits; Markdown is the final product.
All deterministic checks remain required. Scripts are offline Python stdlib; Python 3.10+ required.
On Windows set PYTHONUTF8=1 before Python commands (see docs/lean-harness-evaluation.md).

## Artifact ownership
`NN` is the producing phase; the unsuffixed file is the human view; letters are supporting files.
Read only the artifacts needed for the current role. Data lives on disk, not in handoff prose.

| Artifact | Phase | Who writes it | Read at |
|---|---|---|---|
| `00_scope.md` | 0 | lead | — |
| `01_protocol.md` · `01a_concepts.json` | 1 | lead | — |
| `02_corpus.md` | 2 | evidence-retriever | Research Map |
| `02a_search_log.md` | 2 | evidence-retriever | Research Map |
| `02b_records.jsonl` · `02b_records_external.jsonl` · `02b_import.md` | 2 | retriever · `import_external.py` | — |
| `02c_studies.jsonl` → `02d_dedup.md` → `02e_candidates.jsonl` → `02f_deferred.jsonl` → `02g_worksheet.md` → `02h_verdicts.jsonl` → `02i_prisma.json` | 2 | P4 scripts + retriever | — |
| `02j_prisma.md` | 2 | `prisma_flow.py` | Research Map |
| `03_research_map.md` | 3 | lead | **hard gate** |
| `03a_gate_approval.md` | 3 | lead (L-019) | audit |
| `04_appraisal.md` | 4 | critical-appraiser | appraisal decision |
| `04a_numbers.md` | 4 | `extract_numbers.py` | — |
| `04b_cards.jsonl` | 4 | critical-appraiser | — |
| `04c_quote_locks.md` | 4 | `verify_quotes.py` | appraisal decision |
| `05_draft_review.md` | 5 | lead | — |
| `05a_coach.md` | 5b | quality-coach | — |
| `06_final_review.md` | 6 | lead | **deliverable** |
| `06a_verification_report.md` | 6 | citation-verifier | delivery |
| `06b_citation_audit.md` | 6 | `citation_audit.py` | delivery |
| `06c_manifest.md` | 6 | lead | delivery |
| `07_proposed_lessons.md` | 7 | lead | user approval |

| `00a_run.json` | 0, updated at decisions | lead | audit + manifest |
| `00b_lessons.md` | phase entry | lesson selector | relevant role only |
| `04d_evidence_table.md` | 4 | artifact renderer | appraisal |
| `05b_claim_links.jsonl` | 5, refreshed on revision | lead | QA |
| `06d_claim_audit.json` | 6 | claim-link checker | delivery |

`reference/<topic>.md` is the verified citation store; only approved records are citable.
`source/<topic>/` contains full texts and their machine-extracted text/HTML; a PDF alone is not
readable by quote locks. Agent transcripts must be labelled as such: internal consistency is not
proof of fidelity to the PDF. Bibliographic exports go in `source/<topic>/_exports/` with a manifest.
Concatenate `02b_records.jsonl` + `02b_records_external.jsonl` before dedupe; same schema.

Partial updates: invalidate downstream checks when their inputs change. Reuse unchanged evidence
and revise affected claims/sections; always rerun cheap global checks against the exact final draft.
Never deliver a stale draft or a manifest combining incompatible runs. `06c_manifest.md` is generated
from artifacts, state and hashes, not rewritten from memory. Optional artifacts are recorded as skipped.

## Repository workflow
`main` is the reusable harness. Start each study from current main on `review/<topic>`; keep its
source/reference/review/workspace data there. Do not merge study branches into main. Only approved
cross-study lessons, evolution log and terminology updates flow back. To continue an archived study,
branch current main as `review/<topic>-v2` and copy its inputs; do not reuse its frozen harness.
Historical study branches: `review/af-ablation-metrics`, `review/cryoballoon-pfa-af`,
`review/la-ep-elderly-af`, `review/test-cases`.

After harness edits run `python -m unittest discover -s .claude/tests -t .claude/tests`.
See `docs/lean-harness-evaluation.md` for controlled A/B trials, and `docs/history.md` for history.
The lean architecture is a candidate until real review evaluations confirm quality and usage.
