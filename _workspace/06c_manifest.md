# 06c_manifest.md — proof package (lead) · metformin in adult T2D · 2026-10-27

> Assembled from `_workspace/` artifacts on disk (L-027). Pre-QA version written before Phase 6; QA rows filled after the round-2 PASS.
> Honest limit: this indexes that the steps ran and what was found; it does not re-vouch for thoroughness — that is the verifier's verdict and the human gates.

## 1. Scope line
Clinical decision support · internists · Vietnamese · effort `normal` · sources 2015-01-01 → 2026-10-27 · length ~1,800–2,000 syllable-tokens (amended from "~1500 từ" by the user at Phase 5: "Rút còn ~1800–2000 từ (Recommended)") · MCP sources only (no Scopus/Embase/WoS/CENTRAL). Branch `review/regression-2026-10-27` (regression Case 1, EASY).

## 2. Confidence list (major findings; from `04_appraisal.md` §3/§7)
| Finding | GRADE | Primary source(s) |
|---|---|---|
| HbA1c lowering ≥ other oral classes | Moderate | PMID 27434443 (Palmer 2016); PMID 27088241 (Maruthur 2016) |
| Weight neutral/modest loss; low hypoglycaemia (excess with SU/insulin) | Moderate | PMID 27088241; PMID 37024129 (Shi 2023) |
| No proven all-cause mortality reduction vs placebo/no drug | Low | PMID 28770324 (Griffin 2017); PMID 33516224 (Li 2021); PMID 32501595 (Gnesin 2020) |
| Possible MACE reduction (OR 0.68, main text; 4 old trials) | Low | PMID 42530338 (Silverii 2026) |
| Observational CV/mortality benefit likely confounded | Very low | PMID 31904444 (Zhang 2020); PMID 33117278 (Hu 2020) |
| GI adverse events common (diarrhoea RR ~2.4) | Moderate | PMID 36187122 (Nabrdalik 2022) |
| B12 deficiency dose/duration-dependent; Vietnam 18.6–22.1% | Low | PMID 39526048; PMID 38662670; PMID 40374214 |
| No excess acidosis at eGFR ≥30; signal at eGFR <30 | Low / Very low | PMID 29868840 (Lazarus 2018) |
| Consensus: use if eGFR ≥30, 1,000 mg/d at 30–44, contraindicated <30 | consensus (not graded) | PMID 36189689 (ADA/KDIGO 2022) |
| Stopping at eGFR <30 associated with higher mortality (HR 1.23, main text) | Very low | PMID 39521399 (Lambourg 2024) |
| SGLT2i/GLP-1 RA reduce mortality on top of standard care | High | PMID 37024129; PMID 32598218 (Tsapas 2020) |
| Replacing metformin first-line improves outcomes | Very low (indirect) | PMID 42825450 (ADA/EASD 2026, abstract framing) |
| Older adults / heart failure population | Absent | — |

## 3. Open assumptions (Assumption Register items surviving into the review; `04_appraisal.md` §6)
AR-1 older adults extrapolated · AR-2 Vietnamese generalisability · AR-3 ADA/KDIGO 2022 thresholds assumed current (2026 texts not on disk) · AR-4 KDIGO/FDA/NICE positions second-hand · AR-5 UKPDS-era trials informative · AR-6 ICD acidosis code as lactic-acidosis proxy · AR-7 El-Damanawi (ADPKD) → T2D-CKD · AR-10 9/16 HIGH abstract-only.

## 4. Receipts index
| Step | Artifact(s) | Status |
|---|---|---|
| Phase 0 scope | `00_scope.md` (verbatim answers + length amendment) | ✔ |
| Phase 1 protocol | `01_protocol.md` (+ change log), `01a_concepts.json` | ✔ |
| Phase 2 retrieval | `02_corpus.md`, `02a_search_log.md`, `02b`–`02j` (PRISMA: identified 260 · included 30 · deferred-unread 68) | ✔ `prisma_flow.py` exit 0 |
| Gate 2b | `02a_search_log.md` — "Duyệt, tiếp tục" | ✔ cleared |
| Phase 3 Research Map | `03_research_map.md` | ✔ |
| Research Map hard gate | `03a_gate_approval.md` — "Duyệt, tiếp tục" | ✔ cleared |
| Phase 4 appraisal | `04_appraisal.md`, `04a_numbers.md`, `04b_cards.jsonl`, `04c_quote_locks.md` (104 accepted / 0 rejected) | ✔ |
| Gate 4b | `04_appraisal.md` §13 — "Duyệt, tiếp tục" | ✔ cleared |
| Machine-fetched text | `source/metformin-t2d/` (56 NCBI XML, `_PROVENANCE.md`, SHA-256 manifest) | ✔ (user: keep in source/ with label) |
| Phase 5 draft | `05_draft_review.md` (1,996 tokens), `05b_writer_notes.md` | ✔ |
| Phase 5b coach | `05a_coach.md` — SKIPPED, effort=normal (declared) | ✔ |
| Phase 6 QA | `06a_verification_report.md` (round 1: FIX ×12, no BLOCK; round 2: PASS), `06b_citation_audit.md` (PASS, exit 0), `06_final_review.md` (1,996 tokens incl. title; 33 refs) | ✔ |
| Rubric total / band / violations | **0.82 MET** — T1 0.8 · T2 0.8 · T3 0.8 · T4 0.8 · T5 0.9 · T6 0.9 (round 1: 0.785). Laws 6/6 (Law 6 completes at Phase 7). No fabricated citation; all 3 gates cleared with quotable approvals. Violations: none recorded. Advisory open: R2-1, A1, A4, A5 (non-blocking) | ✔ |
| Phase 7 lessons | `07_proposed_lessons.md` | pending |
