---
name: review-protocol
description: >
  Builds a systematic, reproducible medical-review protocol — research question, PICO/PECO
  framing, inclusion/exclusion criteria, and a database search strategy with MeSH/Emtree terms
  and Boolean logic. Used by the lead (orchestrator) in Phase 1 of any medical literature
  review, and whenever the user asks to define scope, framing, or a search strategy for a review.
---

# Review Protocol Design

A protocol is what makes a review *systematic* instead of an opinion: it fixes the question and
method before searching, so the result is reproducible and not cherry-picked. Produce
`_workspace/01_protocol.md` with the sections below.

## 1. Research question (PICO/PECO)
State the question in one sentence, then decompose into a table:

| Element | Definition |
|---|---|
| **P**opulation | who (condition, demographics, setting) |
| **I**ntervention / **E**xposure | what is being studied |
| **C**omparator | against what (placebo, standard of care, none) |
| **O**utcome | primary + secondary endpoints |

Adapt for question type: diagnostic → add Index test + Reference standard (PIRT/QUADAS framing);
prognostic → Population + Prognostic factor + Outcome + Timing.

## 2. Inclusion / exclusion criteria
A table covering: study designs admitted, population limits, intervention/exposure limits,
comparators, outcomes required, **date window**, language, and publication type (peer-reviewed /
preprint / trial registry). Be explicit about what is *excluded* and why.

## 3. Search strategy (per source)
For each concept block, list synonyms + controlled vocabulary, then combine:
- `OR` within a concept block (synonyms, MeSH/Emtree variants).
- `AND` across concept blocks.
- Give the **exact query string** you will run for each source (PubMed, bioRxiv/medRxiv,
  ClinicalTrials.gov, Consensus), adapted to each source's syntax.

Example block (anticoagulation in AF):
```
Block 1 (population): "atrial fibrillation"[MeSH] OR "atrial flutter" OR AF
Block 2 (intervention): apixaban OR rivaroxaban OR "direct oral anticoagulant" OR DOAC
Block 3 (outcome): stroke OR "systemic embolism" OR "major bleeding"
Final: Block1 AND Block2 AND Block3, filter: 2019/01/01–present, humans
```

## 4. Recency requirement
Always set a date window and explicitly plan a preprint + trial-registry sweep. The user wants
*up-to-date* reviews — a strategy that only mines older indexed literature fails the brief. State
the cutoff date of "current" for this run.

## 5. Pre-registered outcomes & subgroups
List the outcomes of interest and any planned subgroup splits *now*, so the synthesis can't be
steered by what the data happened to show.

## 6. Curiosity budget (mandatory)
Reserve ≥1–2 searches aimed not at the abundant evidence but at what's **missing or conflicting**.
Plan one query per gap type that applies:
- **Evidence gap** — what question has no adequate evidence yet?
- **Contradiction gap** — where do studies disagree (effective here, not there; inconsistent across
  age/country/ethnicity)?
- **Methodological gap** — over-reliance on one design, old measurement tools, dated statistics?
- **Population gap** — which patient groups are under-represented or unvalidated? (Include the
  **local/Vietnam** population here.)
- **Implementation gap** — strong on paper, weak or unclear in real-world application?
A review that only mines what's plentiful misses the gaps that make it valuable. The retriever
executes these; the appraiser and Research Map report what they find.

## 7. Machine-readable PICO concepts — `_workspace/01a_concepts.json`
Write this beside the prose protocol. The deterministic prefilter (P4) consumes it and cannot run
without it — omit it and screening silently loses its ranking. One concept per PICO element:

```json
{"concepts": [{"name": "population",   "terms": ["atrial fibrillation", "AF", "rung nhĩ"]},
              {"name": "intervention", "terms": ["cryoballoon", "cryoablation"]},
              {"name": "comparator",   "terms": ["radiofrequency", "versus"]},
              {"name": "outcome",      "terms": ["recurrence", "freedom from AF"]}],
 "scope_terms": ["ablation", "electrophysiolog"]}
```

`terms` are the surface forms a title or abstract actually uses — synonyms, abbreviations, and the
Vietnamese form where the corpus may contain it — **not MeSH descriptors**, which the prefilter cannot
expand. `scope_terms` marks the discipline: leave it `[]` rather than guessing, because an empty list
means "unknown" and costs nothing, while a wrong one mis-sorts the entire pool.

## 8. Output language and re-runs
- The protocol records the output language **from `00_scope.md`**; it never sets a non-default
  language on its own (L-032).
- On a refinement request, read the existing `01_protocol.md` and amend only the requested parts,
  logging what changed and why — a silently rewritten protocol is no longer pre-specified.

## Why pre-specify
Pre-specifying the question, criteria, and search means a different person re-running your protocol
gets the same corpus. That reproducibility is the difference between evidence synthesis and
narrative bias. If the topic is too broad to bound, say so and offer 2–3 scoped interpretations
rather than guessing.
