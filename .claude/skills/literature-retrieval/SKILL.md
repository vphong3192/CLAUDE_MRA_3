---
name: literature-retrieval
description: >
  Executes a medical-review search strategy across live MCP sources — PubMed/PMC, Elicit,
  bioRxiv/medRxiv preprints, ClinicalTrials.gov, Consensus, and (for drug/target topics)
  ChEMBL/Open Targets — retrieves metadata and full text, deduplicates across sources, and records
  full provenance plus a PRISMA-ready search log. Used by the evidence-retriever agent and whenever a review needs its
  evidence corpus built or refreshed from up-to-date sources.
---

# Literature Retrieval

Turn the protocol's search strategy into a corpus pulled from **live** sources, with provenance
strong enough that every later claim is traceable. Produce `_workspace/01_search_log.md` and
`_workspace/02_corpus.md`.

## Source map — which MCP for what

| Source | Tools (server) | Use for |
|---|---|---|
| **PubMed/PMC** | `search_articles`, `get_article_metadata`, `get_full_text_article`, `find_related_articles`, `lookup_article_by_citation`, `convert_article_ids` | Peer-reviewed indexed literature; full text; ID conversion (PMID↔DOI↔PMCID) |
| **bioRxiv/medRxiv** | `search_preprints`, `get_preprint`, `search_published_preprints` | Newest preprints (NOT peer-reviewed); check if a preprint was later published |
| **ClinicalTrials.gov** | `search_trials`, `get_trial_details`, `analyze_endpoints`, `search_by_sponsor` | Registered/ongoing/completed trials, unpublished results, endpoint design |
| **Consensus** | `search` | AI-ranked evidence + fast coverage check across the field |
| **Elicit** | `search_papers`, `search_trials` | Large-scale recall: semantic **or** Lucene-keyword search over a corpus wider than PubMed, up to 10,000 hits per call, with filters PubMed cannot express — `typeTags` (RCT / Meta-Analysis / Systematic Review / Review / Longitudinal), `maxQuartile` (journal quartile), `minYear`/`maxYear`, `hasPdf`, `retracted` |
| **Elicit** *(paid — see gate below)* | `create_systematic_review`, `create_report`, `get_systematic_review`, `get_report`, `list_sessions`, `resume_session`, `get_usage` | Screening + structured extraction at corpus scale, with per-decision supporting quotes |
| **ChEMBL / Open Targets** | `compound_search`, `drug_search`, `get_mechanism`, `get_bioactivity`, target tools | Drug/compound/target-specific reviews: mechanism, activity, target–disease links |
| **Google Scholar** *(web)* | `WebSearch` — query: `site:scholar.google.com OR "Google Scholar" <terms>` | Supplementary: catch papers not indexed in PubMed (conference, non-English, very recent); results must be PMID/DOI-verified before entering corpus |
| **ScienceDirect** *(web)* | `WebSearch` — query: `site:sciencedirect.com <terms>` | Supplementary: Elsevier journals sometimes lag PubMed indexing; full text usually paywalled — use for metadata/DOI only |

Run the protocol's per-source query strings. Honor each server's usage rules (e.g., Consensus
requires inline numbered citations and its sign-up message preserved verbatim).

### Web search protocol (Google Scholar & ScienceDirect)
Web search is **supplementary only** — run it after PubMed/Consensus to fill gaps, not as a primary source.

1. Run the protocol's key query strings through `WebSearch` targeting each domain.
2. For each result: extract the DOI or PMID and **verify in PubMed** before adding to corpus. If PubMed confirms it → add normally. If PubMed has no record → treat as unverified, do not cite.
3. If a web-found paper appears important (high citations, directly on-topic, pivotal design) but full text is **paywalled and unavailable** via any MCP tool: **alert the user explicitly** — state the title, DOI, and why it looks important — and ask if they can supply the PDF to `source/`. Do not silently skip it.
4. Log web-found additions in the search log with source noted as `(web-supplementary)`.

### Elicit protocol — recall breadth, retraction safety, and the credit gate

Elicit does three things no other source in this map does. Use it deliberately, not reflexively.

**1 · Recall breadth (free tier of the tooling — use on every review).**
`search_papers` reaches a corpus wider than PubMed and returns up to 10,000 hits per call, in either
`semantic` mode (natural-language question) or `keyword` mode (Lucene boolean — mutually exclusive
with `filters`, so put the filter expressions inside the query string). Run it **alongside** the
PubMed query, never instead of it: PubMed remains the ID authority, Elicit is the recall widener.
Set `corpus: "elicit"` for breadth; `corpus: "pubmed"` only to cross-check a PubMed count.

**2 · Retraction screening — this closes a real Law 1 hole.**
`filters.retracted` defaults to `exclude_retracted`. Nothing else in this source map checks whether a
paper has been retracted, and citing a retracted study is a Law 1 failure the citation-verifier cannot
catch (the PMID resolves; the record is real; the science was withdrawn). Two obligations:
- Leave the default in place on every Elicit search — never pass `include_retracted` casually.
- Before the Research Map gate, re-run the corpus's key studies through `search_papers` with
  `retracted: "only_retracted"` and the study titles as `includeKeywords`. Any hit is a **BLOCK**:
  drop the record and say so at the gate. Log the check in the search log even when it returns nothing —
  a check that leaves no receipt did not happen (R4).

**3 · Filters that map onto rubric and law.**
- `typeTags: ["Meta-Analysis","Systematic Review","RCT"]` → Law 3 evidence hierarchy, applied at
  retrieval instead of after the fact.
- `maxQuartile: 1` → rubric Criterion 2 ("Q1 journals / Cochrane / major-body guidelines"). Use it to
  *check coverage*, never as a hard filter on the main pull — quartile is a journal property, not a
  study-quality property, and cutting on it silently drops registry reports and guideline documents.
- `search_trials` (`phase`, `recruitmentStatus`, `hasResults`) complements the ClinicalTrials.gov MCP;
  when both are available prefer the CT.gov MCP for trial *detail* and Elicit for trial *recall*.

**The credit gate — `create_systematic_review` and `create_report` SPEND THE USER'S MONEY.**
These two tools consume Elicit credits. They are **never** run on the retriever's own initiative.
- Present the plan at **Gate 2b** with the concrete parameters (searches, `maxResults`, screening
  criteria, `depth`, extraction columns) and the output of `get_usage`, and wait for an explicit
  user OK — the same fail-closed discipline as L-022/L-024. No quotable approval → do not run it.
- When approved, set `abstractScreening.depth: "thorough"`. `fast` costs less but "wrongly excludes
  more papers that met your criteria and returns decisions **without supporting quotes**" — a screen
  with no quote behind each decision is unauditable, which is exactly R4.
- Screening decisions and extracted values are **retrieval output, not appraisal**. They enter
  `reference/<topic>.md` as ordinary records; GRADE and risk-of-bias remain the critical-appraiser's
  work and are never inherited from Elicit.
- `list_sessions` / `resume_session` recover an interrupted review — resume rather than re-run, so a
  crash does not cost the credits twice.

## Provenance schema (every corpus row)
| Field | Notes |
|---|---|
| `study_id` | logical study key (group preprint+publication+registration as one) |
| `stable_id` | PMID / DOI / PMCID / NCT — **mandatory**; no ID → re-find or drop |
| `title`, `authors`, `year`, `source` | journal or server name |
| `source_type` | `peer-reviewed` \| `preprint` \| `trial-registry` \| `review-article` (landmark, Level III) |
| `abstract` | captured text |
| `fulltext` | `retrieved` \| `available` \| `unavailable` |
| `relevance_tier` | **`HIGH` \| `MEDIUM` \| `LOW`** — importance to the review question; drives full-text priority and is shown to the user at the gate |
| `relevance_note` | one line: why it's in scope |
| `study_context` | from the study's **Introduction**: its research background, the rationale/question it set out to answer, and the authors' approach/framing of the topic (from full text). Abstract-only → write `not captured (abstract-only)` |
| `study_limitations` | the study's **own** stated limitations (from full text). Abstract-only → write `not captured (abstract-only)` |
| `author_suggestions` | future-research directions the **authors** propose (from full text). Abstract-only → write `not captured (abstract-only)` |

`study_context`, `study_limitations`, and `author_suggestions` let the writer reflect each study's
IMRAD faithfully — why the authors did the study and how they framed the topic (Introduction), the
study's own limitations (Discussion), and the next steps they propose — instead of only a corpus-level
summary. Read the **Introduction** of every full-text record for `study_context`, not just methods/
results. All three are populated only from full text; mark them `not captured (abstract-only)` until
the record is upgraded, never invent them.

## Screening & PRISMA — the deterministic pipeline (P4)

Deduplication, relevance ranking and the PRISMA numbers are **mechanical**. They run as scripts so
the flow diagram is a count of records on disk rather than a recollection, and so a claim about
recall can be checked instead of believed. Judgment — is this study eligible? — stays with the LLM,
in the worksheet the pipeline hands it.

**Write the machine-readable layer as you retrieve.** Alongside `02_corpus.md` (for humans), append
one JSON object per retrieved record to `_workspace/02_records.jsonl`. **PRISMA needs the
pre-screening population, which `reference/<topic>.md` structurally cannot hold** — that store is
the *output* of screening, so without this file the identification and exclusion counts cannot be
derived at all.

```json
{"record_id":"P1-001","source":"pubmed","search_id":"P1","pmid":"33652425",
 "doi":"10.1056/NEJMoa2029554","nct":null,"title":"…","authors":"Andrade JG, et al.",
 "year":2021,"journal":"N Engl J Med","abstract":"…",
 "publication_types":["Randomized Controlled Trial"],"retracted":false}
```
`source` must be the real source name (`pubmed`, `elicit`, `consensus`, `biorxiv`, `medrxiv`,
`ctgov`, `source_folder`, `web`) — PRISMA splits identification by it, and an unrecognised value is
reported by name rather than silently binned. `search_id` ties the record back to its ledger row.

```bash
# 1 · one row per STUDY (a preprint + its paper + its registration are one study, not three)
python3 .claude/skills/literature-retrieval/scripts/dedupe_records.py   --records _workspace/02_records.jsonl   --out-studies _workspace/02b_studies.jsonl --out _workspace/02c_dedup.md

# 2 · rank by concept coverage and emit the screening worksheet
python3 .claude/skills/literature-retrieval/scripts/prefilter_records.py   --studies _workspace/02b_studies.jsonl --concepts _workspace/00b_concepts.json   --out-candidates _workspace/02d_candidates.jsonl --out-deferred _workspace/02e_deferred.jsonl   --out _workspace/02f_worksheet.md

# 3 · after screening: draw the flow from the stage files (exit 1 if the counts contradict)
python3 .claude/skills/literature-retrieval/scripts/prisma_flow.py   --records _workspace/02_records.jsonl --studies _workspace/02b_studies.jsonl   --candidates _workspace/02d_candidates.jsonl --deferred _workspace/02e_deferred.jsonl   --verdicts _workspace/02g_verdicts.jsonl   --out-json _workspace/02h_prisma.json --out _workspace/02i_prisma.md
```

`00b_concepts.json` comes from the protocol's PICO — one concept per PICO element:
`{"concepts":[{"name":"population","terms":["atrial fibrillation","AF"]}, …],"scope_terms":["ablation"]}`.

**You fill the worksheet, the script counts it.** Read `02f_worksheet.md`, judge each candidate
against the protocol's criteria, and write `_workspace/02g_verdicts.jsonl` — one line per screened
study: `{"study_id":"…","verdict":"include|exclude|maybe","reason":"…"}`. **Every exclusion needs a
reason**; PRISMA 2020 requires one and step 3 fails the flow without it. A `maybe` is NOT included —
it is listed for the user at the gate.

**Four things the pipeline will not let you say:**
- A **deferred** study is *unread*, never *excluded*. Nobody opened it. The diagram says so, and the
  Methods section must too.
- A **retracted** study is removed on its own line — never folded into duplicates or exclusion
  reasons. It was never eligible.
- **No full-text eligibility box** is drawn unless full text was actually assessed (`--fulltext-assessed`).
  Eligibility here is decided on **title and abstract**, and that is what the diagram is labelled.
- Screening is **AI-assisted with a human at the gates**. Never write "two reviewers independently
  screened" unless that literally happened.

Thresholds (fuzzy 0.92 · year guard ±1 · scope bonus < one concept hit · the two recall floors) are
hardcoded and pinned by tests. **Never loosen one to move a study across the line.** The floors in
particular are calibrated cautiously and are NOT measured on this harness's own corpora — re-measure
and record the measurement before tightening them.

## Deduplication
The same study can surface as a preprint, a journal article, and a trial registration. `dedupe_records.py`
above links them under one `study_id` by DOI, PMID, NCT, then fuzzy title within the year guard; use
`convert_article_ids` and `search_published_preprints` to supply the identifiers that make those links
possible. Never let one study count as three. A same-title pair whose years fall **outside** the guard is
reported, not merged — usually a preprint and its journal version, sometimes two different studies, and
the script will not guess for you.

## Search log (PRISMA numbers)
Record, per source: the exact query, date run, and hit count. Then the flow:
`identified → after dedup → screened → included`. These numbers feed the writer's Methods section
and the PRISMA diagram, and make the search reproducible.

### Recall & reproducibility — prove it, don't imply it (P3)
An MCP call usually returns one page, not the whole result set — so "I searched PubMed" silently
hides how much was missed. Close that hole with three habits, then leave a machine-checkable receipt:

1. **Count-target probe FIRST (cheap).** Before pulling any records, ask each source only for its
   total count (PubMed `esearch ... retmax=0`; ClinicalTrials.gov `countTotal=true`; Consensus: note
   the reported total). The total tells you whether to widen/narrow *before* spending tokens on a
   full pull.
2. **Paginate to exhaustion or cap on purpose.** Page until `retrieved == total`, or stop
   deliberately and record the cap with a reason — never let a one-page pull masquerade as complete.
3. **Log the reproducible call, not just the human query.** Record the actual params/URL
   (`db=pubmed term="..." retmax=...`, or the REST URL) so the search can be rebuilt exactly.

Emit these as a fixed table so a script can check them:
```
## Recall & reproducibility ledger (P3)
| id | source | query | call | total_count | retrieved | recall |
|----|--------|-------|------|-------------|-----------|--------|
| P1 | PubMed | ablation index AND PVI | esearch db=pubmed term="ablation+index AND PVI" retmax=200 | 148 | 148 | retrieved==total ✓ |
| P3 | PubMed | contact force AND PVI | esearch db=pubmed term="contact+force AND PVI" retmax=500 | 732 | 500 | capped ⚠ (landmark-filtered) |
```
Then validate the receipt's format (offline, deterministic — checks completeness/consistency, NOT
whether the counts are true or the search well-designed):
```
python3 .claude/skills/literature-retrieval/scripts/validate_search_log.py \
  --log _workspace/01_search_log.md
```
HARD-FAIL (exit 1) on a missing ledger, missing column, non-integer count, a `call` with no
params/URL, or a recall verdict inconsistent with the numbers (e.g. "complete ✓" but
`retrieved < total`). This is the floor under recall claims; multi-source breadth
(PubMed + preprint + trials + Consensus) is unchanged — the ledger just makes each source's coverage
auditable.

## The `source/` folder (every run, no exceptions)
List the subfolders under `source/` and ask the user which to read **whether or not files exist** —
staying silent here was a real v1 failure. User PDFs are usually the full text of paywalled key
papers. Reconcile each:
| Situation | Action |
|---|---|
| Duplicate of a record already found (same author+year+title) | "Already have it — skipped." |
| Full text where you only had an abstract | Upgrade the record; note "(full text from source/)" |
| Not yet in the corpus | Add it; note "(manually supplied)" |
When you read a full-text PDF, also read its **reference list** to harvest extra cited PMIDs.
*(Windows: `pdftotext.exe` ships with Git at `C:/Program Files/Git/mingw64/bin/`.)*

## Provenance store — `reference/<topic>.md`
Write every verified record into a persistent `reference/<topic>.md` (one topic = one file; check for
a near-match before creating a new one). This file is the **single source of truth the writer cites
from** — never the conversation. Each entry: stable ID + metadata + the verified figure/finding +
date captured. Externalize large metadata blobs (parse with Python for >15 PMIDs) rather than holding
raw JSON in context.

## Curiosity budget (execute the gap searches)
Run the strategist's ≥1–2 gap-directed searches (evidence/contradiction/methodological/population/
implementation). If PubMed returns <3 RCTs/SRs, expand to case reports/series, check
ClinicalTrials.gov for running trials, and flag the thin evidence base — don't let scarcity pass silently.

## Full text — prioritize HIGH-relevance records (do before the gate)
Every `relevance_tier: HIGH` record **must** be upgraded to full text before appraisal/writing, so
the appraiser reads primary methods/results (and can fill `study_limitations` + `author_suggestions`)
rather than an abstract. Order of attempts for each HIGH record:
1. `get_full_text_article` (PubMed/PMC).
2. The `source/` folder (user-supplied PDFs).
3. If still unavailable (paywalled): **alert the user** — title, ID, why it's HIGH — and ask them to
   supply the PDF. Do not let a HIGH record stay abstract-only silently.
MEDIUM/LOW records may remain abstract-derived; mark them `provisional`. Track in the search log how
many HIGH records are full-text vs still abstract-only. Note copyright status where the tool reports it.

## Source-approval handoff (the corpus is presented at the Research Map gate)
The retriever does **not** hand the corpus straight to the appraiser. The full record list — each
with its `relevance_tier` (HIGH/MEDIUM/LOW) and `fulltext` status — is surfaced to the **user at the
Phase 3 Research Map gate**. Appraisal (summarizing) and synthesis (writing) **do not begin until the
user approves which sources are in scope**. The user may drop sources, re-tier importance, or request
more searching/full-text before the team proceeds. This keeps the human in control of what becomes
evidence (see orchestrator Phase 3).

## Currency rule
Preprints and trial registries are where the newest evidence lives — always include them, tag them
clearly, and never silently exclude a preprint just because it isn't peer-reviewed. If a source
errors, retry once, then continue and log the gap explicitly rather than implying coverage.
