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

### L-002: Match language strength to GRADE certainty and study design
- **Role:** writer
- **Trigger:** stating any finding
- **Rule:**
  1. **GRADE-level language:** High/Moderate → confident; Low → "may/suggests"; Very Low → explicitly tentative + "requires confirmation." Never state Low/Very-Low as fact.
  2. **Observational data:** Use associative verbs ("associated with," "linked to"), not causal ("causes," "reduces"), unless the design supports causation. Even Moderate-GRADE observational evidence cannot establish causation.
- **Why:** Two defects, same root — language must match both evidence certainty (GRADE) and study design. Overstating either misleads clinical readers.
- **Origin:** seed (L-002 + L-007); consolidated 2026-06-16

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

### L-008: Don't over-constrain ClinicalTrials.gov queries
- **Role:** retriever
- **Trigger:** searching ClinicalTrials.gov
- **Rule:** Don't combine intervention + condition + phase in the first query; over-constrained queries return 0 silently. Start broad (intervention OR condition alone), then narrow.
- **Why:** A 0 here looks like "no trials exist" and gets reported as a false evidence gap.
- **Origin:** Entry #1 — search returned 0; retry recovered 11 trials.

### L-009: PMID verification protocol — always confirm before storing
- **Role:** retriever
- **Trigger:** before writing any PMID into the reference store, from any source
- **Rule:**
  1. **Cross-check on PubMed:** Open `pubmed.ncbi.nlm.nih.gov/[PMID]/` and confirm: (a) first author matches, (b) title/journal/year matches the intended paper. A "wrong-but-real" PMID passes existence checks but is a Law-1-adjacent error.
  2. **Source = Consensus:** Confirm the PMID/DOI via PubMed title search before the record enters the citable store; leave unconfirmed records uncited.
  3. **Trial papers:** Run a separate search "[trial name] results [year range]" to distinguish the design/protocol paper from the primary results paper. Store the results paper PMID; label the design paper explicitly if also stored.
  4. **When MCP is blocked:** Immediately use WebSearch (`site:pubmed.ncbi.nlm.nih.gov "[first author] [title keyword] [year]"`) to confirm the PMID. Never write "⏳ PMID pending" and proceed — PMID must be confirmed at retrieval time.
- **Why:** Four entry-failures (Consensus hits, trial results vs. design, MCP-blocked, wrong-but-real PMID) all stem from the same discipline lapse — trusting a PMID without verification.
- **Origin:** Entry #1, #5, #6; consolidated L-009 + L-021 + L-026 + L-027 (2026-06-16)

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
- **Why:** This is v1's Entry #9 failure recurring in v2 — and worse, the audit then falsely recorded "gate cleared," laundering the breach. The gate's whole value is the human checkpoint before expensive/mis-framed work.
- **Origin:** Entry #2 — metformin run self-cleared the gate; user caught it.

### L-015: Always ask depth + purpose (+ audience + language) before writing
- **Role:** orchestrator / strategist
- **Trigger:** the start of every review, before Phase 1
- **Rule:** Explicitly ask the user for the review's **purpose** (clinical / research / education), **depth/length**, audience, and output language, and STOP for the answer. Do not infer these from the request or from a fixed test-case prompt. Confirm scope in the user's own words before proceeding.
- **Why:** Depth and purpose change the whole review (a 1500-word clinical aid ≠ a 3000-word research gap-analysis). Guessing them violates Law 2 (serve the purpose, not the process) and produces the wrong artifact confidently.
- **Origin:** user feedback, 2026-06-14 — both test runs assumed scope instead of confirming it.

### L-016: Reconcile inline citations against the reference list before handoff
- **Role:** writer
- **Trigger:** finishing any draft that has a numbered reference list
- **Rule:** Before handing the draft to QA, run a two-way reconciliation: every reference-list entry [n] must appear at least once inline, and every inline [n] must have a list entry. Resolve orphans (listed-but-uncited) by either citing them in the relevant section or removing them from the list. Do not rely on QA to catch this.
- **Why:** Entry #4 left refs [29–34] (3 CF-catheter benchmarks + 3 society guidelines) listed but uncited inline — orphan references that QA had to fix. An orphan reference signals retrieved-but-unused evidence and looks like sloppy scholarship to an expert reader; catching it pre-handoff keeps the writer accountable for completeness.
- **Origin:** Entry #4 — ablation metrics RF-PVI review (2026-06-14)

### L-017: Embed L-011 guideline citations in the consensus section, not just the reference list
- **Role:** writer
- **Trigger:** the strategy ran an L-011 guideline-body search (ESC / AHA / ACC / ADA / NICE / HRS) and those guidelines are in the store
- **Rule:** When society guidelines were retrieved per L-011, cite them explicitly in the "Established consensus" section to anchor each consensus statement — do not leave them sitting only in the reference list. The guideline must do interpretive work in the text (what it recommends and at what strength), not merely appear as a number.
- **Why:** L-011 exists to make reviews read as complete to clinicians; that value is lost if the guidelines are retrieved then forgotten at the writing stage. Entry #4 retrieved ESC 2024, ACC/AHA 2023, HRS 2017 but did not embed them until QA's FIX.
- **Origin:** Entry #4 — ablation metrics RF-PVI review (2026-06-14)

### L-018: Voltage modality discipline — label explicitly and cite separately
- **Role:** writer, appraiser, citation-verifier
- **Trigger:** citing any voltage value, LVZ threshold, or electroanatomic mapping study
- **Rule:**
  1. **Label modality explicitly:** Write "điện thế lưỡng cực" or "điện thế đơn cực" (or "omnipolar"); never write "điện thế" alone for a mapping value.
  2. **Never bundle citations across modalities:** Bipolar (<0.5 mV LVZ), unipolar (~0.73 mV 5th-percentile-derived), and omnipolar (systematically higher than bipolar) use different, non-interchangeable thresholds. If studies differ in modality, cite each separately with its own threshold.
- **Why:** Two defects, same root: (a) Entry #5: "điện thế" used for van der Does 2021 (unipolar) — labeling failure; (b) Entry #6: van der Does [8] bundled into a bipolar "<0.5 mV used consistently [5,7,8]" claim — citation-modality mismatch caught by QA.
- **Origin:** Entry #5 + #6; consolidated L-018 + L-025 (2026-06-16)

### L-019: Persist the Research Map gate approval to disk at the moment it is received
- **Role:** orchestrator
- **Trigger:** immediately after the user sends their Research Map approval message, before launching any downstream agent
- **Rule:** Write the verbatim user approval quote to `_workspace/research_map_gate_approval.md` before proceeding to Phase 4. This file is the audit's only way to verify gate compliance — if it does not exist, the audit must mark "process HOLD" regardless of what happened in the conversation. Complements L-014 (which forbids self-clearing); L-019 ensures that a legitimate clearance is auditable.
- **Why:** Entry #5 gate was cleared correctly but approval was not persisted to disk — QA found no quotable gate record and had to flag a process hold. The orchestrator reconstructed the file post-hoc. One extra Write call at approval time costs nothing; an unauditable gate costs a HOLD and rework.
- **Origin:** Entry #5 — LA electrophysiology elderly AF review (2026-06-15)

### L-020: Label sub-analyses within the same trial separately in the reference store
- **Role:** retriever
- **Trigger:** a major trial (CABANA, AFFIRM, CASTLE-AF, etc.) has multiple published sub-analyses (by age, sex, AF type, QoL, etc.)
- **Rule:** For each sub-analysis stored, record exactly which sub-analysis the PMID represents (e.g., "CABANA — age subgroup, Bahnson 2021"). When reusing the PMID, re-verify by title + first author — do not assume the stored PMID is the right paper just because the trial name matches.
- **Why:** Entry #5 initially stored the CABANA sex subgroup PMID (Russo, 33499668) in the slot intended for the age subgroup (Bahnson, 34933570). The error was caught in Phase 2b before synthesis; if it had reached the writer, a citation would have supported a claim about age outcomes using a paper about sex differences — a Law-1-adjacent error.
- **Origin:** Entry #5 — LA electrophysiology elderly AF review (2026-06-15)

### L-022: STOP when coverage is incomplete — ask before proceeding
- **Role:** retriever, orchestrator
- **Trigger:** (a) any planned search source is unavailable, OR (b) ≥3 HIGH-tier records are still abstract-only after retrieval
- **Rule:**
  - **Source unavailable:** Do NOT silently continue with reduced coverage. Inform the user: "Source X is unavailable (reason). Options: (a) proceed without it and note the gap in Limitations; (b) try WebSearch as a fallback; (c) you supply materials directly." Wait for the user's choice.
  - **Incomplete full text:** Before handing off to the critical-appraiser, count abstract-only HIGH records. If ≥3, report: "X of Y HIGH records are abstract-only. Key missing: [list top 3–5]. Do you want to: (a) proceed and flag in Limitations; (b) grant full-text tool permission; (c) supply PDFs?" Wait for OK.
  - In both cases: record the decision and rationale in the search log.
- **Why:** Entry #5: bioRxiv/ClinicalTrials.gov were unavailable AND 28/31 records were abstract-only — both gaps reported in the log but retriever moved immediately to appraisal without asking the user. User: "không dừng lại hỏi… khả năng thiếu sót cao."
- **Origin:** Entry #5; consolidated L-022 + L-023 (2026-06-16)

### L-024: User must explicitly OK each major phase handoff; fix-then-re-ask, never fix-then-proceed
- **Role:** orchestrator
- **Trigger:** before handing off to the critical-appraiser (Phase 4) AND before handing off to the synthesis-writer (Phase 5); and after fixing any user-requested change at either gate
- **Rule:** The orchestrator presents the phase output (retrieval summary / appraisal summary) and STOPS for explicit user OK before launching the next agent. If the user requests changes or supplements (e.g., "find more full text," "add a search," "fix the tier"), the orchestrator makes those changes and ASKS AGAIN — it does NOT proceed to the next phase automatically after fixing. The loop continues until the user explicitly signals approval (e.g., "ok," "tiếp tục," "approve"). Two specific gates:
  - **Gate 2b (post-retrieval):** After retrieval + corpus update, present: corpus size, full-text status, source availability gaps (L-022), any PMID issues. Ask: "Có muốn bổ sung gì trước khi thẩm định không?" Wait for OK.
  - **Gate 4b (post-appraisal):** After appraisal, present: GRADE summary per axis, flagged contradictions, Assumption Register highlights. Ask: "Có muốn điều chỉnh gì trước khi viết bài không?" Wait for OK.
- **Why:** User feedback (Entry #5, 2026-06-15): "ghi nhận rõ, trước khi giao việc cho appraiser và writer, người dùng phải ok mới làm. Nếu người dùng OK → yêu cầu sửa, sửa xong lại hỏi tiếp chứ không được giao việc luôn." These checkpoints cost one extra message per phase; the alternative is delivering a review the user considers shallow because coverage gaps were not caught early.
- **Origin:** Entry #5 — user-stated requirement, 2026-06-15; approved immediately
