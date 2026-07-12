# Lessons Learned — Medical Review Harness

Persistent, human-approved store of generalized rules the team has learned from past mistakes.
Injected (role- **and scope-**tagged) at the start of every review. New lessons are appended only
after user approval. One lesson = one reusable rule, with its rationale.

> Seeded with starter lessons capturing the most common AI-review failure modes. Remove or edit any
> that don't fit your practice; the curator will add more as real defects surface.

## Selective injection (keep the digest light)

Each lesson carries a **`Scope:`** tag in addition to its **`Role:`**. At inject time the lead loads
**only the lessons that match this run** — never the whole file — by intersecting:
- **Scope match:** `universal` (always) **+** `vi-language` (only when the output language is
  Vietnamese/non-English — the default, so usually on) **+** `cardiology-ep` (only when the topic is
  cardiac / electrophysiology / arrhythmia). A nephrology review never sees the AF-ablation lessons.
- **Role match:** post each lesson only to the agent(s) named in its `Role:` line.

This keeps each agent's injected set to a handful of relevant rules instead of the full store. Adding
a lesson does not add per-run weight unless its scope matches. When a lesson's example is domain-bound
but its *rule* is general, tag it `universal` and let the example illustrate — do not tag it
`cardiology-ep` just because the origin was a cardiac run.

---

### L-001: Every substantive claim needs a resolvable citation
- **Role:** writer · **Scope:** universal
- **Trigger:** writing any factual/quantitative statement
- **Rule:** Do not write a claim unless it maps to a real corpus record with a stable ID. No record → soften, remove, or request retrieval.
- **Why:** Fabricated/unsupported citations are the cardinal failure of AI reviews and destroy trust in the whole document.
- **Origin:** seed

### L-002: Match language strength to GRADE certainty and study design
- **Role:** writer · **Scope:** universal
- **Trigger:** stating any finding
- **Rule:**
  1. **GRADE-level language:** High/Moderate → confident; Low → "may/suggests"; Very Low → explicitly tentative + "requires confirmation." Never state Low/Very-Low as fact.
  2. **Observational data:** Use associative verbs ("associated with," "linked to"), not causal ("causes," "reduces"), unless the design supports causation. Even Moderate-GRADE observational evidence cannot establish causation.
- **Why:** Two defects, same root — language must match both evidence certainty (GRADE) and study design. Overstating either misleads clinical readers.
- **Origin:** seed (L-002 + L-007); consolidated 2026-06-16

### L-003: Verify the source supports the specific sentence, not just that it exists
- **Role:** verifier · **Scope:** universal
- **Trigger:** checking any inline `[n]`
- **Rule:** Read claim and source side by side; confirm population, intervention, and endpoint match. A real-but-mismatched citation is a BLOCK, not a pass.
- **Why:** "Reference exists" is the weak check that lets hallucinated support through.
- **Origin:** seed

### L-004: Always include preprints and trial registries, and label them
- **Role:** retriever · **Scope:** universal
- **Trigger:** building the corpus
- **Rule:** Sweep bioRxiv/medRxiv and ClinicalTrials.gov every run; tag preprints as not-peer-reviewed; never silently exclude them.
- **Why:** The newest evidence lives in preprints and registries; omitting them makes the review stale, which violates the up-to-date requirement.
- **Origin:** seed

### L-005: Copy effect sizes and CIs from the results table, not the abstract
- **Role:** appraiser · **Scope:** universal
- **Trigger:** recording a quantitative effect estimate
- **Rule:** Take effect size, CI, N, and follow-up from the full-text results/tables; abstracts round or omit intervals. If only the abstract is available, mark the value provisional.
- **Why:** Abstract numbers are frequently rounded or selectively reported, corrupting GRADE imprecision judgments.
- **Origin:** seed

### L-006: Document contradictions; never drop the minority finding
- **Role:** appraiser · **Scope:** universal
- **Trigger:** studies disagree on an outcome
- **Rule:** Report both sides with citations and a methodological reason for the discrepancy. Do not present only the majority result.
- **Why:** Hiding conflict produces a falsely confident review and erases real clinical uncertainty.
- **Origin:** seed

### L-008: Don't over-constrain ClinicalTrials.gov queries
- **Role:** retriever · **Scope:** universal
- **Trigger:** searching ClinicalTrials.gov
- **Rule:** Don't combine intervention + condition + phase in the first query; over-constrained queries return 0 silently. Start broad (intervention OR condition alone), then narrow.
- **Why:** A 0 here looks like "no trials exist" and gets reported as a false evidence gap.
- **Origin:** Entry #1 — search returned 0; retry recovered 11 trials.

### L-009: PMID verification protocol — always confirm before storing
- **Role:** retriever · **Scope:** universal
- **Trigger:** before writing any PMID into the reference store, from any source
- **Rule:**
  1. **Cross-check on PubMed:** Open `pubmed.ncbi.nlm.nih.gov/[PMID]/` and confirm: (a) first author matches, (b) title/journal/year matches the intended paper. A "wrong-but-real" PMID passes existence checks but is a Law-1-adjacent error.
  2. **Source = Consensus:** Confirm the PMID/DOI via PubMed title search before the record enters the citable store; leave unconfirmed records uncited.
  3. **Trial papers:** Run a separate search "[trial name] results [year range]" to distinguish the design/protocol paper from the primary results paper. Store the results paper PMID; label the design paper explicitly if also stored.
  4. **When MCP is blocked:** Immediately use WebSearch (`site:pubmed.ncbi.nlm.nih.gov "[first author] [title keyword] [year]"`) to confirm the PMID. Never write "⏳ PMID pending" and proceed — PMID must be confirmed at retrieval time.
- **Why:** Four entry-failures (Consensus hits, trial results vs. design, MCP-blocked, wrong-but-real PMID) all stem from the same discipline lapse — trusting a PMID without verification.
- **Origin:** Entry #1, #5, #6; consolidated L-009 + L-021 + L-026 + L-027 (2026-06-16)

### L-010: Decompose composite endpoints before stating the headline
- **Role:** appraiser / writer · **Scope:** universal
- **Trigger:** reporting a composite outcome (e.g., MACE)
- **Rule:** Break the composite into its components before writing the headline number; the benefit may rest on only some components.
- **Why:** "↓20% CV events" was driven by MI + all-cause mortality, NOT CV death or stroke — stating the composite as if all components moved overstates the evidence.
- **Origin:** Entry #1 — Yin 2025 component analysis.

### L-011: Search the relevant guideline body
- **Role:** strategist · **Scope:** universal
- **Trigger:** topic has society guidance (cardiology / obesity / endocrine, etc.)
- **Rule:** Add an explicit guideline-body search (ESC / AHA / ACC / ADA / NICE) to the strategy.
- **Why:** A review missing the relevant guideline reads as incomplete to clinicians and costs search-comprehensiveness.
- **Origin:** Entry #1 — T1 scored 0.75 partly for no guideline cited.

### L-012: List source/ and ask — every run, including tests
- **Role:** orchestrator / retriever · **Scope:** universal
- **Trigger:** the start of every review's retrieval phase
- **Rule:** List the `source/` folder and ask the user which to read, even when you expect it empty.
- **Why:** Silence here was a v1 failure and recurred as a deviation; user PDFs are often the full text of paywalled key papers.
- **Origin:** Entry #1 — audit flagged source/ not checked.

### L-013: An established drug's "efficacy safety" query returns add-on/comparator trials
- **Role:** retriever · **Scope:** universal
- **Trigger:** searching the evidence for an established first-line drug (e.g., metformin, aspirin, statins)
- **Rule:** A `<drug> efficacy safety` query returns mostly trials where the drug is the *background* and a newer agent is the subject. To get the drug's own evidence, search `<drug> monotherapy` + the landmark trial (e.g., UKPDS) + the relevant guideline.
- **Why:** The naive query silently mis-frames the corpus toward comparators, weakening the review's coverage of the actual subject drug.
- **Origin:** Entry #2 — first metformin query returned tirzepatide/SGLT2/GLP-1 add-on meta-analyses.

### L-014: Gate discipline — a gate is cleared only by an explicit, quotable user approval received after the gate was shown
- **Role:** orchestrator · **Scope:** universal
- **Trigger:** any human gate (Phase-0 scope, the Research Map corpus/source gate, Gate 4b post-appraisal) has been presented and is awaiting the user's decision
- **Rule:** *(This is the harness's single most-repeated lesson. It absorbs former L-024, L-030, L-041, L-042, L-044.)*
  1. **Never self-clear.** "Gate cleared" requires a real user reply received *after* the gate content was shown — not "small scope," not "unambiguous/fixed test-case scope," not "standing approval inferred from the request." Presenting a gate and proceeding in the same turn is a violation. The audit must be able to quote the approval; if it cannot, the gate is NOT cleared and nothing downstream is deliverable. (former L-014)
  2. **Fix-then-re-ask, never fix-then-proceed.** If the user requests changes or supplements at a gate ("find more full text," "add a search," "fix the tier"), make the change and ASK AGAIN — do not advance automatically after fixing. Loop until the user explicitly signals approval ("ok," "tiếp tục," "approve," "bắt đầu viết"). (former L-024)
  3. **A conditional approval is a HOLD, not a clearance.** If the user picks "approve with changes" / "Duyệt có chỉnh" without specifying edits, ask "what specific changes?" and hold. Cleared only when the edits are specified + applied, or the user says "proceed" after seeing them applied. (former L-030)
  4. **Track gate state across interleaved side-conversation turns.** If side questions arrive before the approval, answer them on their merits without treating them as gate approval; before launching the next phase, re-confirm a distinct, quotable approval was received for the gate itself — not inferred from the side conversation's tone. (former L-041)
  5. **A second locked deliverable gets its own labeled sub-approval, nested but distinct.** When a gate also finalizes a second deliverable's structure (e.g., a CRF/structured table), present those structural questions as an explicitly labeled sub-approval, resolve and commit that artifact first, then re-ask the gate-closing question on its own. Do not let "answered the structural questions" stand in for "closed the gate." (former L-042)
  6. **Never bundle a content decision with the gate-approval decision in one question/reply** — especially under a tool-failure fallback. If `AskUserQuestion` errors and you fall back to plain text, ask the content question (e.g., "how should full-text be sourced?") alone first, process it, THEN ask the gate-closing question separately. Do not improvise a merged reply ("answer '1a, 2A'") that resolves two different kinds of decision at once. (former L-044)
- **Why:** This cluster is v1's Entry #9 failure recurring across many forms — self-clearing, fix-then-proceed, conditional-as-unconditional, interleaved-turn drift, dual-deliverable collapse, and tool-failure bundling. All share one root: treating something short of an explicit post-gate approval as clearance. Consolidating them makes the discipline one rule with named sub-cases instead of six near-duplicates diluting the digest.
- **Origin:** Entries #2, #7, #10; consolidated L-014 + L-024 + L-030 + L-041 + L-042 + L-044 (2026-07-12)

### L-015: Always ask depth + purpose (+ audience + language) before writing
- **Role:** orchestrator / strategist · **Scope:** universal
- **Trigger:** the start of every review, before Phase 1
- **Rule:** Explicitly ask the user for the review's **purpose** (clinical / research / education), **depth/length**, audience, and output language, and STOP for the answer. Do not infer these from the request or from a fixed test-case prompt. Confirm scope in the user's own words before proceeding.
- **Why:** Depth and purpose change the whole review (a 1500-word clinical aid ≠ a 3000-word research gap-analysis). Guessing them violates Law 2 (serve the purpose, not the process) and produces the wrong artifact confidently.
- **Origin:** user feedback, 2026-06-14 — both test runs assumed scope instead of confirming it.

### L-016: Reconcile inline citations against the reference list before handoff
- **Role:** writer · **Scope:** universal
- **Trigger:** finishing any draft that has a numbered reference list
- **Rule:** Before handing the draft to QA, run a two-way reconciliation: every reference-list entry [n] must appear at least once inline, and every inline [n] must have a list entry. Resolve orphans (listed-but-uncited) by either citing them in the relevant section or removing them from the list. Do not rely on QA to catch this.
- **Why:** Entry #4 left refs [29–34] listed but uncited inline — orphan references that QA had to fix. An orphan reference signals retrieved-but-unused evidence and looks like sloppy scholarship to an expert reader; catching it pre-handoff keeps the writer accountable for completeness.
- **Origin:** Entry #4 — ablation metrics RF-PVI review (2026-06-14)

### L-017: Embed guideline citations in the consensus section, not just the reference list
- **Role:** writer · **Scope:** universal
- **Trigger:** the strategy ran an L-011 guideline-body search and those guidelines are in the store
- **Rule:** When society guidelines were retrieved per L-011, cite them explicitly in the "Established consensus" section to anchor each consensus statement — do not leave them sitting only in the reference list. The guideline must do interpretive work in the text (what it recommends and at what strength), not merely appear as a number.
- **Why:** L-011 exists to make reviews read as complete to clinicians; that value is lost if the guidelines are retrieved then forgotten at the writing stage. Entry #4 retrieved ESC 2024, ACC/AHA 2023, HRS 2017 but did not embed them until QA's FIX.
- **Origin:** Entry #4 — ablation metrics RF-PVI review (2026-06-14)

### L-018: Voltage modality discipline — label explicitly and cite separately
- **Role:** writer, appraiser, citation-verifier · **Scope:** cardiology-ep
- **Trigger:** citing any voltage value, LVZ threshold, or electroanatomic mapping study
- **Rule:**
  1. **Label modality explicitly:** Write "điện thế lưỡng cực" or "điện thế đơn cực" (or "omnipolar"); never write "điện thế" alone for a mapping value.
  2. **Never bundle citations across modalities:** Bipolar (<0.5 mV LVZ), unipolar (~0.73 mV 5th-percentile-derived), and omnipolar (systematically higher than bipolar) use different, non-interchangeable thresholds. If studies differ in modality, cite each separately with its own threshold.
- **Why:** Two defects, same root: (a) Entry #5 "điện thế" used for van der Does 2021 (unipolar) — labeling failure; (b) Entry #6 van der Does [8] bundled into a bipolar "<0.5 mV used consistently [5,7,8]" claim — citation-modality mismatch caught by QA.
- **Origin:** Entry #5 + #6; consolidated L-018 + L-025 (2026-06-16)

### L-019: Persist the gate approval to disk at the moment it is received
- **Role:** orchestrator · **Scope:** universal
- **Trigger:** immediately after the user sends their Research Map approval message, before launching any downstream agent
- **Rule:** Write the verbatim user approval quote to `_workspace/research_map_gate_approval.md` before proceeding to Phase 4. This file is the audit's only way to verify gate compliance — if it does not exist, the audit must mark "process HOLD" regardless of what happened in the conversation. Complements L-014 (which forbids self-clearing); L-019 ensures a legitimate clearance is auditable.
- **Why:** Entry #5 gate was cleared correctly but approval was not persisted to disk — QA found no quotable gate record and had to flag a process hold. One extra Write call at approval time costs nothing; an unauditable gate costs a HOLD and rework.
- **Origin:** Entry #5 — LA electrophysiology elderly AF review (2026-06-15)

### L-020: Label sub-analyses within the same trial separately in the reference store
- **Role:** retriever · **Scope:** cardiology-ep
- **Trigger:** a major trial (CABANA, AFFIRM, CASTLE-AF, etc.) has multiple published sub-analyses (by age, sex, AF type, QoL, etc.)
- **Rule:** For each sub-analysis stored, record exactly which sub-analysis the PMID represents (e.g., "CABANA — age subgroup, Bahnson 2021"). When reusing the PMID, re-verify by title + first author — do not assume the stored PMID is the right paper just because the trial name matches.
- **Why:** Entry #5 initially stored the CABANA sex subgroup PMID (Russo, 33499668) in the slot intended for the age subgroup (Bahnson, 34933570). Caught in Phase 2b before synthesis; if it had reached the writer, a citation would have supported an age claim using a sex-differences paper — a Law-1-adjacent error.
- **Origin:** Entry #5 — LA electrophysiology elderly AF review (2026-06-15)

### L-022: STOP when coverage is incomplete — surface it at the Research Map corpus/source gate
- **Role:** retriever, orchestrator · **Scope:** universal
- **Trigger:** (a) any planned search source is unavailable, OR (b) ≥3 HIGH-tier records are still abstract-only after retrieval
- **Rule:** *(Since Gate 2b was folded into the Research Map, these are presented as part of the Map's corpus/source-approval section — not as a separate earlier stop.)*
  - **Source unavailable:** Do NOT silently continue with reduced coverage. Present in the Map: "Source X is unavailable (reason). Options: (a) proceed and note the gap in Limitations; (b) try WebSearch as a fallback; (c) you supply materials." Wait for the user's choice.
  - **Incomplete full text:** In the Map's source-approval list, count abstract-only HIGH records. If ≥3, report: "X of Y HIGH records are abstract-only. Key missing: [list top 3–5]. Do you want to: (a) proceed and flag in Limitations; (b) grant full-text tool permission; (c) supply PDFs?" Wait for OK.
  - In both cases: record the decision and rationale in the search log.
- **Why:** Entry #5: bioRxiv/ClinicalTrials.gov were unavailable AND 28/31 records were abstract-only — both gaps reported in the log but the retriever moved straight to appraisal without asking. User: "không dừng lại hỏi… khả năng thiếu sót cao." Folding the check into the Research Map keeps the one human corpus review instead of two adjacent stops.
- **Origin:** Entry #5; consolidated L-022 + L-023 (2026-06-16); corpus/source gate merged into Research Map (2026-07-12)

### L-025: The quality-coach pass is conditional — run it for full/high-stakes, and declare any skip (never silent)
- **Role:** orchestrator · **Scope:** universal
- **Trigger:** a run reaches the handoff between Phase 5 (draft) and Phase 6 (QA)
- **Rule:** The coach is spawned for `full` and `high-stakes` effort. For `normal` and `tiny` it is skipped by default, but the skip must be **declared**: write `_workspace/04b_coach_skip.md` naming the effort tag as the reason. Before routing the draft to QA, confirm that either `04b_coach.md` (ran) or `04b_coach_skip.md` (declared skip) exists. A silent absence on any run is R4 ("Faking the steps") even when the draft meets the rubric. The user may request the coach on any run.
- **Why:** Entry #7 — 04b_coach.md was absent with no declared reason; QA flagged V-01 as R4. The coach pass is audit-visible: QA checks for its artifact, and absence without justification is indistinguishable from never having run it. (Updated 2026-07-12: coach demoted to a conditional pass to lighten routine runs — the *declare-the-skip* discipline now covers `normal` too, not only `tiny`.)
- **Origin:** Entry #7 — CBA-vs-PFA review, V-01 process violation (2026-06-17); scope updated when coach became conditional (2026-07-12)

### L-026: Law 4 section headers must be explicit labels in the draft body, not implicit content
- **Role:** writer · **Scope:** universal
- **Trigger:** finishing any review draft, before handoff to quality-coach or QA
- **Rule:** The draft must contain the literal section labels "**Established consensus**" and "**Ongoing controversy**" (or their Vietnamese equivalents) as visible headers or sub-headers — organizing the content topically is not enough. If a thematic multi-section draft makes separate labeled sections awkward, add a brief labeled sub-section inside the synthesis rather than omitting the labels.
- **Why:** Entry #7 §11 "Balanced synthesis" covered both consensus and controversy in substance but lacked Law 4's explicit structural markers; QA issued V-03 and deducted T4 to 0.75. The rule lets a reader/auditor instantly locate each category — absent labels defeat that regardless of content quality.
- **Origin:** Entry #7 — CBA-vs-PFA review, Law 4 partial fail / V-03 (2026-06-17)

### L-027: Assemble 08_manifest.md before routing to QA — it is a deliverable, not an afterthought
- **Role:** orchestrator / synthesis-writer · **Scope:** universal
- **Trigger:** draft is complete and ready for QA handoff
- **Rule:** Before submitting to the citation-verifier, assemble `_workspace/08_manifest.md` — a one-page confidence list, assumption-register summary, and receipts index (listing all `_workspace/` artifacts on disk). QA checks for its presence; absence = process violation V-02. The manifest is written from artifacts already on disk, so it requires no new work — only assembly.
- **Why:** Entry #7 — 08_manifest.md not found at QA time; cited as V-02. Its value is precisely being assembled pre-QA: it lets the verifier confirm what ran without relying on conversation memory (anti-R4). Creating it after QA flags its absence defeats the purpose.
- **Origin:** Entry #7 — CBA-vs-PFA review, V-02 process violation (2026-06-17)

### L-028: When citing sub-group statistics, name the sub-cohort N, not the parent-study N
- **Role:** writer · **Scope:** universal
- **Trigger:** reporting any outcome that applies to a sub-cohort within a larger study (last-N-patient subgroup, per-protocol subset, age subgroup)
- **Rule:** Write the sub-cohort N inline with the sub-group statistic. Do not write the parent-study N in the same parenthetical as a sub-group outcome — it implies the statistic applies to all parent-study participants. Pattern: "…finding X (sub-cohort n=25)" not "…finding X (study N=64)." If the parent N is also relevant, state it separately.
- **Why:** Entry #7 D-02 — "24% persisting at discharge in its fluoroscopy subgroup (N=64)" but N=64 was the whole study; the 24% (6/25) applied only to the last-25-patient sub-cohort. A reader would infer 24% of 64 — inflating the count from 6 to ~15.
- **Origin:** Entry #7 — CBA-vs-PFA review, D-02 (2026-06-17)

### L-029: Abstract GRADE labels must match body GRADE stamps; resolve dual-level certainty explicitly
- **Role:** writer · **Scope:** universal
- **Trigger:** the abstract summarizes an evidence finding whose GRADE certainty was formally assigned in the appraisal
- **Rule:** Before finalizing the abstract, cross-check every certainty parenthetical against the GRADE stamp in the corresponding body section. If meta-analysis evidence justifies a higher certainty than the underlying RCT base (a legitimate GRADE upgrade), state both levels and the reason: "(Low–Moderate: Low for the single RCT; Moderate for the pooled direction — see §3)." Never leave an unexplained discrepancy between the abstract label and the body stamp.
- **Why:** Entry #7 D-03 — abstract wrote "equivalent (Moderate certainty)" while §3 assigned GRADE LOW; the difference was defensible (MA vs RCT level) but unexplained, creating an apparent inconsistency QA had to flag.
- **Origin:** Entry #7 — CBA-vs-PFA review, D-03 (2026-06-17)

### L-031: Investigation dimensions set by the user are evidence axes, not conclusion steers
- **Role:** synthesis-writer / quality-coach / orchestrator · **Scope:** universal
- **Trigger:** the user asks to "investigate" or "explore" dimensions that appear to favour one option (e.g., "focus on cost, learning curve, maturity" when comparing two technologies where one has advantages on those dimensions)
- **Rule:** Treat user-specified investigation dimensions as search axes only — collect and grade evidence for those dimensions on both sides. Do not read a dimension list as a signal that the user expects a particular conclusion. Follow the evidence, not the dimension set's implied prior. Steelman the weaker side on each requested dimension before concluding. If the framing drifts toward the implied prior, flag it to the user before writing.
- **Why:** Entry #7 — the lead framed Gate-4b as a "CBA advantage" synthesis because the requested dimensions happened to favour CBA. The user corrected: those were search directions, not a license to conclude for CBA. Confirming the asker's implied prior fails the steelman-before-concluding principle.
- **Origin:** Entry #7 — CBA-vs-PFA review, process observation (b) (2026-06-17)

### L-032: Output language is gated — confirm with a quotable user choice; default Vietnamese, fail closed
- **Role:** orchestrator / scoping-retriever · **Scope:** universal
- **Trigger:** setting `output language` in `00_protocol.md` / scope at Phase 0
- **Rule:** Output language defaults to Vietnamese (CLAUDE.md). Any non-default language (e.g. English) MUST be confirmed by the user in Phase 0 with a **quotable** confirmation recorded in the protocol/scope file. The strategist must NOT unilaterally set a non-default language. If no quotable confirmation exists, the language is Vietnamese — fail closed (same discipline as L-014).
- **Why:** Entry #7 addendum — `00_protocol.md` set "Output language: English" with no recorded user confirmation; the review was delivered in English, and the user asked why it wasn't Vietnamese (the default). A non-default language is a scope decision, not a strategist default.
- **Origin:** Entry #7 addendum — CBA-vs-PFA review, post-delivery language correction (2026-06-17)

### L-033: Non-English output is composed natively, with a fluency self-pass + calque blacklist before handoff
- **Role:** synthesis-writer (and quality-coach as a check) · **Scope:** vi-language
- **Trigger:** producing a Vietnamese (or any non-English) deliverable — BEFORE handoff to coach/QA, not after the user complains
- **Rule:** *(absorbs former L-037.)*
  1. **Compose natively, do not translate.** Write directly in the target language for that audience. Do NOT translate sentence-by-sentence: break English run-ons into short native clauses, use native connectors (*vì, do đó, ngược lại, trong khi đó*), follow topic–comment order, avoid calques ("ở nơi… và ở nơi…", "mà ở đó…"). If an English draft exists, use it as a **content source** and re-compose for fluency — do not transliterate syntax.
  2. **Run a dedicated fluency self-pass before handoff.** (a) Split any sentence >~40 words / with stacked em-dashes into short native clauses. (b) Scan for and rewrite a **calque blacklist** — abstract English idioms translated word-for-word. Known offenders (rewrite by MEANING, never the word): "the X story"→❌"câu chuyện X" ✅ reframe ("về X, vấn đề là…"); "artifact"→❌"tạo tác" ✅ "do được so sánh với…/phản ánh…"; "binary/dichotomous endpoint"→❌"điểm cuối nhị phân" ✅ "tiêu chí kiểu có–không"; "apparent"→❌"biểu kiến" ✅ "bề ngoài/có vẻ"; "survives the X / steelman"→❌"sống sót qua X" ✅ "vẫn đứng vững trước X"; "flatter (a result)"→❌"tâng bốc" ✅ "làm cao giả tạo/thổi phồng"; "anchor"→❌"neo" ✅ "cơ sở vững nhất/dựa vào"; "carry through the review"→❌"mang theo suốt" ✅ "cần ghi nhớ trong suốt…"; "naive pooling"→❌"gộp ngây thơ" ✅ "gộp một cách thiếu cân nhắc"; "driver"→❌"động lực gián tiếp" ✅ "nguồn gây tính gián tiếp/không nhất quán"; avoid over-hyphenation ("tất-cả-lứa-tuổi"→"mọi lứa tuổi").
  3. Preserve all numerics/CIs/P-values/GRADE labels/`[n]` citations and the reference list verbatim during the pass (fluency only, never content).
- **Why:** Entry #7 + #8 — the first Vietnamese re-issue was a literal translation (90-word run-ons, calque structures) the native-expert user flagged as clunky; Entry #8 passed QA at 0.895 but still leaked "tạo tác", "điểm cuối nhị phân", 60–90-word run-ons, requiring a post-hoc rework of ~83 paragraphs. L-033 ("compose natively") is necessary but not sufficient — first drafts still leak calques, so the explicit pre-handoff pass with a blacklist is required. Fluency is part of the deliverable, not optional polish.
- **Origin:** Entry #7 + #8 addenda; consolidated L-033 + L-037 (2026-07-12)

### L-034: A feature is only a "differentiator" if it actually differs between the arms — verify before contrasting
- **Role:** critical-appraiser / synthesis-writer · **Scope:** universal
- **Trigger:** writing any sentence that frames a device/procedure attribute as an advantage or distinguishing factor of one arm over another (cost mechanism, infrastructure, safety, workflow)
- **Rule:** Before presenting attribute X as a contrast between arm A and arm B, confirm X genuinely differs between them. Do not build a false mechanistic contrast from a shared attribute. Example: both CBA (Arctic Front) and PFA (Farawave) use **single-use disposable catheters**; the reusable item is the console, which **both** need. So "single-use catheter vs reusable console" is NOT a CBA-vs-PFA differentiator. When a real cost gap exists, attribute it to the correct driver (here: the higher price of the PFA disposable + anaesthesia), not a spurious single-use-vs-reusable distinction.
- **Why:** Entry #7 addendum — §8/§9 contrasted "PFA single-use catheter vs CBA reusable console," implying CBA avoids a disposable catheter. A domain-expert user flagged it: both arms use single-use catheters. The argument was logically void and had to be reframed.
- **Origin:** Entry #7 addendum — CBA-vs-PFA review, §8/§9 false-contrast correction (2026-06-18)

### L-035: Copy reference titles verbatim from PubMed metadata — never reconstruct from acronym or memory
- **Role:** retriever / writer · **Scope:** universal
- **Trigger:** writing any reference-list TITLE into the store or the draft
- **Rule:** Take the title string verbatim from `mcp__PubMed__get_article_metadata` (or the source full text). Do NOT reconstruct a title from the trial acronym, the topic, or memory (e.g. writing "CIRCA-DOSE comparison of energy sources and monitoring" instead of the real "Cryoballoon or Radiofrequency Ablation for Atrial Fibrillation Assessed by Continuous Monitoring: A Randomized Clinical Trial"). A reconstructed title is invisible to the writer (PMID/DOI/content can all be correct) and is only caught by a QA re-fetch.
- **Why:** Entry #8 FIX-01 — reference [2] CIRCA-DOSE carried a reconstructed title; PMID/DOI/content were correct, so nothing upstream flagged it. Only the verifier re-fetching the PubMed title caught it. Verbatim copy at retrieval time costs nothing and removes a whole class of silent format errors.
- **Origin:** Entry #8 — elderly CB-vs-RF review, FIX-01 (2026-06-23)

### L-036: Carry a missing/pending DOI as an explicit tag into the reference list, not as an empty field
- **Role:** retriever / writer · **Scope:** universal
- **Trigger:** a store record has "DOI: pending" or no DOI (e.g. not-yet-indexed recent papers)
- **Rule:** Propagate the status explicitly into the draft reference list as "DOI: not yet indexed" (or equivalent) rather than silently omitting the DOI field. An omitted field is ambiguous — indistinguishable from an oversight — and triggers a format-error flag at QA. An explicit tag documents that the absence is known and intentional.
- **Why:** Entry #8 FIX-02 — five references had no DOI consistent with not-yet-indexed status, but the omission read as incomplete formatting and was flagged. An explicit "not yet indexed" tag resolves the ambiguity.
- **Origin:** Entry #8 — elderly CB-vs-RF review, FIX-02 (2026-06-23)

### L-038: Build a PICO×outcome coverage matrix — every pre-registered subgroup gets an explicit, locatable section
- **Role:** synthesis-writer (check), quality-coach (completeness angle), citation-verifier (audit), orchestrator (gate emphasis) · **Scope:** universal
- **Trigger:** finishing a draft whose protocol pre-registered subgroups (AF type, age strata, first-vs-redo, sex, etc.); and whenever the user emphasizes some axes at a gate
- **Rule:** Before handoff, map every protocol-registered PICO subgroup to an **explicit, locatable** place in the draft (a labeled section/sub-section), not scattered prose. A subgroup with data but no findable, labeled treatment is a defect — even if the facts appear somewhere. Where a subgroup is an **effect modifier especially important for the target population** (e.g. persistent AF in the ≥75 elderly), foreground it as a clinical headline, not a buried clause. Critically: a user emphasis on some axes ADDS depth to those axes — it must NOT silently demote another in-scope subgroup below the labeled-section threshold. When relaying an emphasis at a gate, confirm the non-emphasized in-scope subgroups stay at least explicitly covered.
- **Why:** Entry #8 — the elderly CB-vs-RF review passed QA at 0.895 but the user flagged that the paroxysmal-vs-persistent distinction, and the salient point that ≥75 + persistent AF has the highest recurrence (Boehmer 57%), were present-but-scattered rather than given a labeled section. Root cause: the Gate-4b emphasis on safety + QoL implicitly de-prioritized an in-scope PICO subgroup. Data present + correct, but a salience/synthesis defect a PhD committee asks about first. Generalizes L-026 (explicit labels) from Law-4 sections to all pre-registered subgroups.
- **Origin:** Entry #8 addendum — elderly CB-vs-RF review, paroxysmal/persistent salience gap (2026-06-23)

### L-039: Push mechanical steps out of the LLM into a deterministic layer that runs AFTER and cannot be negotiated
- **Role:** citation-verifier, critical-appraiser, scoping-retriever (and every future QA step); harness design principle for every agent · **Scope:** universal
- **Trigger:** any purely mechanical step — counting, cross-checking citekeys/IDs, copying numbers verbatim, coverage checks, recall proofs, call logging. Especially when the evidence of "done" is currently just the LLM's own narration ("verified the citations," "searched everything," "copied the numbers").
- **Rule:** A step that needs no judgment must NOT be left to the LLM — a fluent agent can talk itself (or a QA-LLM) into "passed" (the exact bug that once let a test self-clear the Research Map gate). Move it to a zero-dependency, no-LLM, no-network script: (a) runs **after** the LLM step, (b) **deterministic** (same input → identical output), (c) emits **PASS/FAIL by exit code**, (d) states plainly what it checks and does NOT (traceability ≠ semantics). The script ADDS a floor, it does NOT replace the LLM's judgment layer (RoB/GRADE/meaning/synthesis stay with the LLM). Three floors run today: `citation_audit.py` (after the citation-verifier, before delivery — Law 1), `extract_numbers.py` (before the appraiser fills the evidence table — *loads* numbers, no hand-copy), `validate_search_log.py` (on the retriever's recall ledger).
- **Why:** borrowed the script-first tactic from a rival harness (aglr-med) — shallower in method but ahead on exactly one point: nailing mechanical steps so they can't be faked/self-persuaded. Building the three floors surfaced real errors an LLM eye waves through: a Vietnamese CI `[0,88–4,17]` misread as a citation; a valid NCT-only PEACE trial reference falsely flagged; a metadata filter swallowing a numbers line ending in "(Source: …DOI…)". Mechanical errors caught by mechanical checks.
- **Origin:** Entry #9 — building the deterministic layer (P1 citation audit · P2 number extraction · P3 search-log validation), 2026-06-29

### L-040: Commit each phase artifact immediately after it is written and verified, not at turn end
- **Role:** orchestrator · **Scope:** universal
- **Trigger:** any `_workspace/` artifact is written or finalized (appraisal, draft, coach report, QA output, table preview, gate-approval file)
- **Rule:** Run `git add` + commit for that artifact in the same tool-call batch that finishes writing it — before moving to the next phase step or ending the turn. Do not wait for the stop-hook to flag uncommitted changes as the trigger to commit.
- **Why:** The stop-hook fired ~5 times because newly-written artifacts were left uncommitted at turn boundaries. The hook is a safety net, not the intended commit trigger — relying on it costs a round-trip per phase and risks losing the per-phase audit trail if a session ends before it fires.
- **Origin:** Entry #10 — LA-EP elderly AF review, recurring stop-hook pattern (2026-06-30)

### L-043: Flag Consensus-only / abstract-only store entries at appraisal time so verifier WARNs are pre-triaged
- **Role:** appraiser, retriever · **Scope:** universal
- **Trigger:** a store record was retrieved via Consensus (or any abstract-only path) without a full-text pull, and it anchors a quantitative claim (effect size, coefficient, p-value) used in the draft
- **Rule:** When building the evidence table (Phase 4), explicitly tag such records — e.g., "Consensus-only / abstract-depth: numbers unconfirmable by audit heuristic" — in the appraisal artifact (and propagate the tag into `03b_numbers.md` or the store entry). At QA time, the citation-verifier treats a `number_not_in_source` WARN on a pre-tagged record as already triaged (known store-depth limitation) rather than re-investigating it as newly discovered.
- **Why:** Entry #10 — REF-003 (van der Does) was a Consensus-only retrieval lacking full-text verbatim numbers; `citation_audit.py` correctly WARN-flagged its cited coefficient/p-value as `number_not_in_source`, and the verifier had to manually re-derive that this was a store-completeness gap. A Phase-4 tag would have pre-empted the effort. Complements L-009 and L-005 by closing the loop when full text genuinely isn't available.
- **Origin:** Entry #10 — LA-EP elderly AF review, REF-003 WARN triage (2026-06-30)
