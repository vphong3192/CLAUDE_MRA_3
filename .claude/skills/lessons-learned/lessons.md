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

### L-025: Phase 5b quality-coach pass must be explicitly declared SKIPPED — silent absence is R4
- **Role:** orchestrator
- **Trigger:** effort=full (or normal) run reaches handoff between Phase 5 (draft) and Phase 6 (QA)
- **Rule:** Before routing the draft to QA, confirm that 04b_coach.md exists in `_workspace/`. If it does not, the orchestrator must either (a) run the quality-coach pass, or (b) write a brief `04b_coach_skip.md` stating the reason (e.g., effort=tiny, user-waived). Silent omission for effort=full constitutes R4 ("Faking the steps") even when the draft meets the rubric.
- **Why:** Entry #7 — 04b_coach.md was absent with no declared reason; QA flagged V-01 as R4. The coach pass is an audit-visible step: QA checks for its artifact, and absence without justification is indistinguishable from never having run it.
- **Origin:** Entry #7 — CBA-vs-PFA review, V-01 process violation (2026-06-17)

### L-026: Law 4 section headers must be explicit labels in the draft body, not implicit content
- **Role:** writer
- **Trigger:** finishing any review draft, before handoff to quality-coach or QA
- **Rule:** The draft must contain the literal section labels "**Established consensus**" and "**Ongoing controversy**" (or their Vietnamese equivalents) as visible headers or sub-headers — organizing the content topically is not enough. If the structure makes separate labeled sections awkward (e.g., a thematic multi-section draft), add a brief labeled sub-section inside the synthesis section rather than omitting the labels.
- **Why:** Entry #7 — §11 "Balanced synthesis" covered both consensus and controversy in substance but lacked Law 4's explicit structural markers; QA issued V-03 and deducted T4 to 0.75. The rule exists so a reader (or auditor) can instantly locate each category — absent labels defeat that purpose regardless of content quality.
- **Origin:** Entry #7 — CBA-vs-PFA review, Law 4 partial fail / V-03 (2026-06-17)

### L-027: Assemble 08_manifest.md before routing to QA — it is a deliverable, not an afterthought
- **Role:** orchestrator / synthesis-writer
- **Trigger:** draft is complete and ready for QA handoff
- **Rule:** Before submitting to the citation-verifier, the orchestrator (or synthesis-writer) assembles `_workspace/08_manifest.md` — a one-page confidence list, assumption register summary, and receipts index (listing all `_workspace/` artifacts on disk). QA checks for its presence; absence = process violation V-02. The manifest is written from `_workspace/` artifacts already on disk, so it requires no new work — only assembly.
- **Why:** Entry #7 — 08_manifest.md not found at QA time; cited as V-02. The manifest's value is precisely that it is assembled pre-QA: it lets the verifier confirm what steps ran without relying on conversation memory (anti-R4). Creating it after QA flags its absence defeats the purpose.
- **Origin:** Entry #7 — CBA-vs-PFA review, V-02 process violation (2026-06-17)

### L-028: When citing sub-group statistics, name the sub-cohort N, not the parent-study N
- **Role:** writer
- **Trigger:** reporting any outcome that applies to a sub-cohort within a larger study (e.g., last-N-patient subgroup, per-protocol subset, age subgroup)
- **Rule:** Write the sub-cohort N inline with the sub-group statistic. Do not write the parent-study N in the same parenthetical as a sub-group outcome — it implies the statistic applies to all parent-study participants. Pattern: "…finding X (sub-cohort n=25)" not "…finding X (study N=64)." If the parent N is also relevant, state it separately.
- **Why:** Entry #7 D-02 — Chéhirlian §5.1 wrote "24% persisting at discharge in its fluoroscopy subgroup (N=64)" but N=64 was the whole study; the 24% figure (6/25) applied only to the last-25-patient fluoroscopy sub-cohort. A reader would reasonably infer 24% of 64 had the outcome — inflating the actual count from 6 to ~15.
- **Origin:** Entry #7 — CBA-vs-PFA review, D-02 minor mismatched citation (2026-06-17)

### L-029: Abstract GRADE labels must match body GRADE stamps; resolve dual-level certainty explicitly
- **Role:** writer
- **Trigger:** the abstract summarizes an evidence finding whose GRADE certainty was formally assigned in the appraisal section
- **Rule:** Before finalizing the abstract, cross-check every certainty parenthetical "(High/Moderate/Low/Very-Low certainty)" against the GRADE stamp in the corresponding body section. If meta-analysis evidence justifies a higher certainty than the underlying RCT base (a legitimate GRADE upgrade), state both levels and the reason: e.g., "(Low–Moderate certainty: Low for the single RCT; Moderate for the pooled meta-analytic direction — see §3)." Never leave an unexplained discrepancy between the abstract label and the body stamp.
- **Why:** Entry #7 D-03 — abstract wrote "equivalent (Moderate certainty)" while §3 assigned GRADE LOW for head-to-head efficacy; the difference was defensible (MA level vs. RCT level) but unexplained, creating an apparent inconsistency QA had to flag.
- **Origin:** Entry #7 — CBA-vs-PFA review, D-03 minor overstated-certainty (2026-06-17)

### L-030: A conditional gate option is not a cleared gate until the specific edits are received
- **Role:** orchestrator / lead
- **Trigger:** a user selects a conditional-approval option (e.g., "Duyệt có chỉnh" / "Chỉnh trước khi viết" / "Approve with changes") at any human gate
- **Rule:** Treat a conditional approval as a HOLD, not a clearance. Ask immediately: "What specific changes do you want before I proceed?" Do NOT advance to the next phase, infer the edits from context, or self-determine that the changes are minor enough to skip. The gate is cleared only when (a) the user specifies the edits AND the orchestrator confirms they are applied, or (b) the user explicitly says "proceed" / "tiếp tục" after seeing the conditional option applied. Document the edit specification and the user's final proceed signal in the gate approval file alongside the original conditional response.
- **Why:** This run — the user twice selected "Duyệt có chỉnh" without specifying edits; the lead correctly held and asked for specifics rather than self-clearing. This pattern is the same failure mode as L-014 (self-clearing the Research Map gate) extended to any gate with a conditional option. The lesson generalizes: a user clicking "approve with edits" is expressing intent to change something — proceeding without knowing what treats the conditional as unconditional.
- **Origin:** Entry #7 — CBA-vs-PFA review, process observation (a) (2026-06-17)

### L-031: Investigation dimensions set by the user are evidence axes, not conclusion steers
- **Role:** synthesis-writer / quality-coach / orchestrator (lead)
- **Trigger:** the user asks to "investigate" or "explore" dimensions that appear to favour one option (e.g., "focus on cost, learning curve, and maturity" when comparing two technologies where one option has advantages on those dimensions)
- **Rule:** Treat user-specified investigation dimensions as search axes only — collect and grade evidence for those dimensions on both sides. Do not interpret a dimension list as a signal that the user expects (or prefers) a particular conclusion. Frame the synthesis by following the evidence, not by confirming the dimension set's implied prior. Explicitly steelman the weaker side on each requested dimension before concluding. If the lead notices the framing drifting toward the implied prior, flag it to the user before writing the synthesis.
- **Why:** This run — the lead framed Gate-4b as a "CBA advantage" synthesis because the user's requested dimensions (cost, learning curve, maturity) happened to favour CBA. The user corrected: those dimensions were search directions, not a license to conclude in CBA's favour. An investigator who confirms the asker's implied prior fails the steelman-before-concluding operating principle (constitution) and produces a review that serves the reader's prior, not the truth.
- **Origin:** Entry #7 — CBA-vs-PFA review, process observation (b) (2026-06-17)

### L-032: Output language is gated — confirm with a quotable user choice; default Vietnamese, fail closed
- **Role:** orchestrator / lead (and research-strategist)
- **Trigger:** setting `output language` in `00_protocol.md` / scope at Phase 0
- **Rule:** Output language defaults to Vietnamese (CLAUDE.md). Any non-default language (e.g. English) MUST be confirmed by the user in Phase 0 with a **quotable** confirmation recorded in the protocol/scope file. The strategist must NOT unilaterally set a non-default language. If no quotable user confirmation exists, the language is Vietnamese — fail closed (same discipline as the gate-clearance lessons L-014/L-030).
- **Why:** Entry #7 addendum — `00_protocol.md` set "Output language: English" with no recorded user confirmation; the final review was delivered in English, and the user then asked why it wasn't Vietnamese (the harness default). A non-default language is a scope decision, not a strategist default.
- **Origin:** Entry #7 addendum — CBA-vs-PFA review, post-delivery language correction (2026-06-17)

### L-033: Non-English output is composed natively, never literal-translated from English
- **Role:** synthesis-writer
- **Trigger:** producing a Vietnamese (or any non-English) deliverable, including re-issuing an English draft in another language
- **Rule:** Compose directly in the target language for that audience. Do NOT translate sentence-by-sentence: break English run-on sentences into short native clauses, use native connectors (*vì, do đó, ngược lại, trong khi đó*), follow topic–comment order, and avoid calques ("ở nơi… và ở nơi…", "mà ở đó…"). If an English draft exists, use it as a **content source** and re-compose for fluency — do not transliterate syntax. Preserve all numerics/CIs/P-values/GRADE labels/`[n]` citations and the reference list verbatim.
- **Why:** Entry #7 addendum — the first Vietnamese re-issue was a literal translation; the user flagged it as unnatural and clunky (90-word run-on sentences, calque structures). A full native rewrite was required. Faithfulness to content ≠ faithfulness to English syntax.
- **Origin:** Entry #7 addendum — CBA-vs-PFA review, Vietnamese fluency correction (2026-06-17)
