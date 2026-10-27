# CLAUDE_MRA_2

## Harness: Medical Literature Review

**Goal:** Produce high-quality, in-depth, systematic-style medical literature reviews from live,
up-to-date sources (PubMed/PMC, Elicit, bioRxiv/medRxiv, ClinicalTrials.gov, Consensus), with a constitution,
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
- `source/<folder>/` — user-supplied full text; checked and asked-about every run. PDFs live
  here, but **a PDF is not quotable**: `verify_quotes.py` (P8) reads only HTML/text, so each
  paper needs a text file beside it (same basename). Machine extraction — `pdftotext`, or the
  publisher's HTML — makes the quote lock proof against text no model wrote; an agent's own
  transcript proves internal consistency only, and must be declared as such in the appraisal.
- `_workspace/` — per-run artifacts (preserved for audit / partial re-runs). **`NN` = the phase that
  produces it; `NN` with no letter = the artifact a human reads; `NNa…` = supporting or machine
  artifacts, lettered in production order.**

| Artifact | Phase | Who writes it | Read at |
|---|---|---|---|
| `00_scope.md` | 0 | lead | — |
| `01_protocol.md` · `01a_concepts.json` | 1 | research-strategist | — |
| `02_corpus.md` | 2 | evidence-retriever | Gate 2b |
| `02a_search_log.md` | 2 | evidence-retriever | Gate 2b |
| `02b_records.jsonl` · `02b_records_external.jsonl` · `02b_import.md` | 2 | retriever · `import_external.py` | — |
| `02c_studies.jsonl` → `02d_dedup.md` → `02e_candidates.jsonl` → `02f_deferred.jsonl` → `02g_worksheet.md` → `02h_verdicts.jsonl` → `02i_prisma.json` | 2 | P4 scripts + retriever | — |
| `02j_prisma.md` | 2 | `prisma_flow.py` | Gate 2b |
| `03_research_map.md` | 3 | lead | **hard gate** |
| `03a_gate_approval.md` | 3 | lead (L-019) | audit |
| `04_appraisal.md` | 4 | critical-appraiser | Gate 4b |
| `04a_numbers.md` | 4 | `extract_numbers.py` | — |
| `04b_cards.jsonl` | 4 | critical-appraiser | — |
| `04c_quote_locks.md` | 4 | `verify_quotes.py` | Gate 4b |
| `05_draft_review.md` | 5 | synthesis-writer | — |
| `05a_coach.md` | 5b | quality-coach | — |
| `06_final_review.md` | 6 | lead | **deliverable** |
| `06a_verification_report.md` | 6 | citation-verifier | delivery |
| `06b_citation_audit.md` | 6 | `citation_audit.py` | delivery |
| `06c_manifest.md` | 6 | lead | delivery |
| `07_proposed_lessons.md` | 7 | lessons-curator | user approval |

  **`02b` is one logical artifact in several files: the record stream and how it was built.**
  `02b_records.jsonl` is what the MCP sources returned; `02b_records_external.jsonl` is what the
  author's own database exports contributed; `02b_import.md` says which export files those came
  from, under which query, on which date. Concatenate both JSONL files before dedupe — the schema
  is identical, so nothing downstream distinguishes them except the `source` and `prisma_column`
  each record carries.

  **`source/<folder>/_exports/`** holds the author's bibliographic exports (RIS/NBIB/BibTeX/CSV)
  plus the `manifest.json` declaring each file's query, date, database and PRISMA column. The
  underscore keeps them apart from the full-text files in the same study folder.

  **Re-running a phase makes everything downstream stale.** The numbering makes this checkable: after
  re-running phase `N`, every artifact numbered above `N` describes a run that no longer exists.
  Re-generate them or delete them — never leave a stale `06_final_review.md` next to a fresh
  `04_appraisal.md`, and never let the manifest index artifacts from two different runs.

  **Reading an old evolution-log entry.** Entries before 2026-09-05 use the pre-renumbering names, and
  the log is a historical record that is never rewritten. Translate with:
  `00_protocol`→`01_protocol` · `01_search_log`→`02a_search_log` · `03_appraisal`→`04_appraisal` ·
  `03b_numbers`→`04a_numbers` · `04_draft_review`→`05_draft_review` · `04b_coach`→`05a_coach` ·
  `05_verification_report`→`06a_verification_report` · `05b_citation_audit`→`06b_citation_audit` ·
  `08_manifest`→`06c_manifest` · `research_map_gate_approval`→`03a_gate_approval`.
  `02_corpus`, `06_final_review` and `07_proposed_lessons` are unchanged.

  **Markdown is the deliverable; there is no export layer, by decision.** `06_final_review.md` is
  the finished product — not a draft awaiting conversion. A CSL/Pandoc `.docx` path was scoped and
  **cancelled** (2026-09-06): it would add a non-stdlib dependency, a second place for the citation
  audit to be bypassed, and a format nobody asked for. One earlier run wrote a hand-built
  `_workspace/index.html`; producing such a thing on request is fine, but it is ad-hoc, it has no
  generator in this harness, and **nothing downstream may depend on an export existing**.
- `.claude/skills/lessons-learned/lessons.md` — distilled digest (each agent loads its role slice via `scripts/lessons_digest.py`) ·
  `evolution-log.md` — full archive (not auto-loaded).
- `.claude/tests/` — automated regression suite; run
  `python3 -m unittest discover -s .claude/tests -t .claude/tests` after ANY harness edit.

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
branch from a fresh `main` so each study starts with the newest lessons.

**Archive branches (do NOT merge into `main`):** every completed study lives on its own branch, each
carrying only that study's `reference/`, `source/`, `reviews/` and `_workspace*` artifacts. `main`
keeps the harness plus empty `.gitkeep` scaffolding for the four data directories.

| Branch | Study | evolution-log |
|---|---|---|
| `review/af-ablation-metrics` | Ablation metrics in RF-PVI for AF (AI/LSI/LID/CF/AID) — final review is in `_workspace/06_final_review.md`, it has no `reviews/` folder | #4 |
| `review/cryoballoon-pfa-af` | Cryoballoon in the PFA era · CBA vs RF (+PFA) in the elderly | #7, #8 |
| `review/la-ep-elderly-af` | Left-atrial electrophysiology in elderly AF | #5, #6, #10 |
| `review/test-cases` | Regression baselines — metformin (EASY) + semaglutide/GLP-1 (HARD) | #1, #2, #3 |

To revisit a study: `git checkout review/<topic>`. To *continue* one, branch a fresh
`review/<topic>-v2` from current `main` and copy in the store — never build new work on an archive,
whose harness is frozen at the version the study was run with. (Note: branching keeps *future*
checkouts light but does not shrink `.git` history; that is acceptable on a private repo.)

**Change log:** `.claude/CHANGELOG.md` — one row per harness change (date · change · target ·
reason). Not auto-loaded: CLAUDE.md is injected into every agent, the history is not needed to run
a review. Add a row there for every harness edit.
