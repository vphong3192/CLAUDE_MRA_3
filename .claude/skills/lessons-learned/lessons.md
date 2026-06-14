# Lessons Learned — Medical Review Harness

Persistent, human-approved store of generalized rules the team has learned from past mistakes.
Injected (role-tagged) at the start of every review. New lessons are appended only after user
approval. One lesson = one reusable rule, with its rationale.

> Seeded with starter lessons capturing the most common AI-review failure modes. Remove or edit any
> that don't fit your practice; the curator will add more as real defects surface.

---

### L-001: Every substantive claim needs a resolvable citation
- **Role:** writer
- **Trigger:** writing any factual/quantitative statement
- **Rule:** Do not write a claim unless it maps to a real corpus record with a stable ID. No record → soften, remove, or request retrieval.
- **Why:** Fabricated/unsupported citations are the cardinal failure of AI reviews and destroy trust in the whole document.
- **Origin:** seed

### L-002: Match language strength to GRADE certainty
- **Role:** writer
- **Trigger:** stating a finding the appraiser graded
- **Rule:** High/Moderate → confident; Low → "may/suggests"; Very Low → explicitly tentative + "requires confirmation." Never state Low/Very-Low as fact.
- **Why:** Overstating weak evidence misleads clinical readers and is the most damaging interpretive error.
- **Origin:** seed

### L-003: Verify the source supports the specific sentence, not just that it exists
- **Role:** verifier
- **Trigger:** checking any inline `[n]`
- **Rule:** Read claim and source side by side; confirm population, intervention, and endpoint match. A real-but-mismatched citation is a BLOCK, not a pass.
- **Why:** "Reference exists" is the weak check that lets hallucinated support through.
- **Origin:** seed

### L-004: Always include preprints and trial registries, and label them
- **Role:** retriever
- **Trigger:** building the corpus
- **Rule:** Sweep bioRxiv/medRxiv and ClinicalTrials.gov every run; tag preprints as not-peer-reviewed; never silently exclude them.
- **Why:** The newest evidence lives in preprints and registries; omitting them makes the review stale, which violates the up-to-date requirement.
- **Origin:** seed

### L-005: Copy effect sizes and CIs from the results table, not the abstract
- **Role:** appraiser
- **Trigger:** recording a quantitative effect estimate
- **Rule:** Take effect size, CI, N, and follow-up from the full-text results/tables; abstracts round or omit intervals. If only the abstract is available, mark the value provisional.
- **Why:** Abstract numbers are frequently rounded or selectively reported, corrupting GRADE imprecision judgments.
- **Origin:** seed

### L-006: Document contradictions; never drop the minority finding
- **Role:** appraiser
- **Trigger:** studies disagree on an outcome
- **Rule:** Report both sides with citations and a methodological reason for the discrepancy. Do not present only the majority result.
- **Why:** Hiding conflict produces a falsely confident review and erases real clinical uncertainty.
- **Origin:** seed

### L-007: Avoid causal language for observational data
- **Role:** writer
- **Trigger:** reporting cohort/case-control findings
- **Rule:** Use associative verbs ("associated with," "linked to"), not causal ("causes," "reduces"), unless the design supports causation.
- **Why:** Observational designs cannot establish causation; causal phrasing overstates the evidence.
- **Origin:** seed

### L-008: Don't over-constrain ClinicalTrials.gov queries
- **Role:** retriever
- **Trigger:** searching ClinicalTrials.gov
- **Rule:** Don't combine intervention + condition + phase in the first query; over-constrained queries return 0 silently. Start broad (intervention OR condition alone), then narrow.
- **Why:** A 0 here looks like "no trials exist" and gets reported as a false evidence gap.
- **Origin:** Entry #1 — search returned 0; retry recovered 11 trials.

### L-009: Confirm Consensus hits via PubMed before citing
- **Role:** retriever
- **Trigger:** a study surfaces via Consensus without a PMID/DOI
- **Rule:** Confirm the PMID/DOI with a PubMed title search before the record enters the citable store; leave unconfirmed records uncited.
- **Why:** Consensus metadata (including publication year) can be imprecise; citing an unconfirmed record risks a Law-1 violation.
- **Origin:** Entry #1 — Yin 2025 confirmed (PMID 40207414); Kelkar 2024 left unconfirmed and therefore uncited.

### L-010: Decompose composite endpoints before stating the headline
- **Role:** appraiser / writer
- **Trigger:** reporting a composite outcome (e.g., MACE)
- **Rule:** Break the composite into its components before writing the headline number; the benefit may rest on only some components.
- **Why:** "↓20% CV events" was driven by MI + all-cause mortality, NOT CV death or stroke — stating the composite as if all components moved overstates the evidence.
- **Origin:** Entry #1 — Yin 2025 component analysis.

### L-011: Search the relevant guideline body
- **Role:** strategist
- **Trigger:** topic has society guidance (cardiology / obesity / endocrine, etc.)
- **Rule:** Add an explicit guideline-body search (ESC / AHA / ACC / ADA / NICE) to the strategy.
- **Why:** A review missing the relevant guideline reads as incomplete to clinicians and costs search-comprehensiveness.
- **Origin:** Entry #1 — T1 scored 0.75 partly for no guideline cited.

### L-012: List source/ and ask — every run, including tests
- **Role:** orchestrator / retriever
- **Trigger:** the start of every review's retrieval phase
- **Rule:** List the `source/` folder and ask the user which to read, even when you expect it empty.
- **Why:** Silence here was a v1 failure and recurred as a deviation; user PDFs are often the full text of paywalled key papers.
- **Origin:** Entry #1 — audit flagged source/ not checked.

### L-013: An established drug's "efficacy safety" query returns add-on/comparator trials
- **Role:** retriever
- **Trigger:** searching the evidence for an established first-line drug (e.g., metformin, aspirin, statins)
- **Rule:** A `<drug> efficacy safety` query returns mostly trials where the drug is the *background* and a newer agent is the subject. To get the drug's own evidence, search `<drug> monotherapy` + the landmark trial (e.g., UKPDS) + the relevant guideline.
- **Why:** The naive query silently mis-frames the corpus toward comparators, weakening the review's coverage of the actual subject drug.
- **Origin:** Entry #2 — first metformin query returned tirzepatide/SGLT2/GLP-1 add-on meta-analyses.

### L-014: The Research Map gate has NO exception — never self-clear it
- **Role:** orchestrator
- **Trigger:** after presenting the Research Map, before any drafting
- **Rule:** STOP and wait for an explicit user approval message. "Gate cleared" requires a real user reply received *after* the map was shown — not "small scope," not "unambiguous/fixed test-case scope," not "standing approval inferred from the request." Presenting the map and proceeding in the same turn is a violation. The audit must quote the user's approval; if it cannot, the gate is NOT cleared and the review is not deliverable.
- **Why:** This is v1's Entry #9 failure recurring in v2 — and worse, the audit then falsely recorded "gate cleared," laundering the breach. The gate's whole value is the human checkpoint before expensive/мis-framed work.
- **Origin:** Entry #2 — metformin run self-cleared the gate; user caught it.

### L-015: Always ask depth + purpose (+ audience + language) before writing
- **Role:** orchestrator / strategist
- **Trigger:** the start of every review, before Phase 1
- **Rule:** Explicitly ask the user for the review's **purpose** (clinical / research / education), **depth/length**, audience, and output language, and STOP for the answer. Do not infer these from the request or from a fixed test-case prompt. Confirm scope in the user's own words before proceeding.
- **Why:** Depth and purpose change the whole review (a 1500-word clinical aid ≠ a 3000-word research gap-analysis). Guessing them violates Law 2 (serve the purpose, not the process) and produces the wrong artifact confidently.
- **Origin:** user feedback, 2026-06-14 — both test runs assumed scope instead of confirming it.
