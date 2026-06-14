---
name: literature-retrieval
description: >
  Executes a medical-review search strategy across live MCP sources — PubMed/PMC, bioRxiv/medRxiv
  preprints, ClinicalTrials.gov, Consensus, and (for drug/target topics) ChEMBL/Open Targets —
  retrieves metadata and full text, deduplicates across sources, and records full provenance plus
  a PRISMA-ready search log. Used by the evidence-retriever agent and whenever a review needs its
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
| `study_limitations` | the study's **own** stated limitations (from full text). Abstract-only → write `not captured (abstract-only)` |
| `author_suggestions` | future-research directions the **authors** propose (from full text). Abstract-only → write `not captured (abstract-only)` |

`study_limitations` and `author_suggestions` let the writer report each study's IMRAD faithfully —
its own limitations and the authors' suggested next steps — instead of only a corpus-level summary.
They are populated only from full text; mark them `not captured (abstract-only)` until the record is
upgraded, never invent them.

## Deduplication
The same study can surface as a preprint, a journal article, and a trial registration. Use
`convert_article_ids` and `search_published_preprints` to link them under one `study_id`. Never
let one study count as three.

## Search log (PRISMA numbers)
Record, per source: the exact query, date run, and hit count. Then the flow:
`identified → after dedup → screened → included`. These numbers feed the writer's Methods section
and the PRISMA diagram, and make the search reproducible.

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
