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

### L-018: Specify voltage modality (unipolar vs bipolar) when citing mapping studies
- **Role:** writer, appraiser
- **Trigger:** citing any voltage value or LVZ threshold from an electroanatomic mapping study
- **Rule:** Always state whether the cited voltage is unipolar or bipolar — they measure different tissue properties with different clinical thresholds (bipolar LVZ typically <0.5 mV; unipolar LVZ typically <0.5–1.0 mV depending on protocol). Write "điện thế lưỡng cực" or "điện thế đơn cực" explicitly; never write "điện thế" alone for a mapping value.
- **Why:** Entry #5 draft wrote generic "điện thế" for van der Does 2021 which measured unipolar voltage — a meaningful distinction QA had to fix. Expert electrophysiology readers notice this immediately.
- **Origin:** Entry #5 — LA electrophysiology elderly AF review (2026-06-15)

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

### L-021: Verify a trial PMID is the results paper, not the design/protocol paper
- **Role:** retriever
- **Trigger:** storing the PMID for any landmark or registered trial
- **Rule:** Run a separate search "[trial name] results [year range]" in addition to "[trial name]" to distinguish the design/protocol paper from the primary endpoint/results paper. Store the **results paper** PMID; if the design paper is also needed, label it explicitly as "design paper — not the results."
- **Why:** Entry #5 initially stored STAR AF II's design paper PMID (22795275, 2012) instead of the NEJM results paper (25946280, 2015). A "wrong but real" PMID passes naive existence checks and would misdirect any reader who follows it.
- **Origin:** Entry #5 — LA electrophysiology elderly AF review (2026-06-15)

### L-022: When a data source is unavailable, STOP and ask the user before continuing with reduced coverage
- **Role:** retriever, orchestrator
- **Trigger:** any planned search source is unavailable (MCP permission-denied, tool absent, rate-limited after retries)
- **Rule:** Do NOT silently continue with reduced coverage. STOP and inform the user: "Source X is unavailable (reason). Options: (a) proceed without it and note the gap in Limitations; (b) I try WebSearch as a fallback; (c) you supply materials directly." Wait for the user's choice. Record the decision and its rationale in the search log. "Silently continuing" produces a review whose coverage gap is invisible to the user until they read the Limitations footnote — too late to add value.
- **Why:** Entry #5: bioRxiv/medRxiv tool was permission-denied, ClinicalTrials.gov had no tool, ScienceDirect/Google Scholar were unavailable — retriever noted these in the log and continued without asking the user whether to try WebSearch or other fallbacks. User feedback: "không dừng lại hỏi xem có dùng websearch không, có cố thử lại không mà buồng luôn → khả năng thiếu sót cao."
- **Origin:** Entry #5 — LA electrophysiology elderly AF review (2026-06-15); user-approved lesson

### L-023: When full-text retrieval is incomplete, STOP and ask the user before advancing to appraisal
- **Role:** retriever, orchestrator
- **Trigger:** after the retrieval phase, when HIGH-tier records remain abstract-only
- **Rule:** Before handing off to the critical-appraiser, count how many HIGH-tier records are still abstract-only. If ≥3 HIGH records lack full text, STOP and report: "X of Y HIGH records are abstract-only. Key missing: [list top 3–5]. Do you want to: (a) proceed with current depth and flag in Limitations; (b) grant full-text tool permission; (c) supply PDFs?" Do not advance to Phase 4 without this check.
- **Why:** Entry #5: 28/31 records were abstract-only after retrieval (5 of the most important ones paywalled). The retriever reported this in the log but moved immediately to appraisal without asking the user whether to supplement. User feedback: "PHẢI hỏi user lại xem có muốn bổ sung không… đã chuyển bước sau luôn mà không hỏi user." Abstract-only appraisal of landmark RCTs forces the appraiser to rely on abstracts for RoB domains that require full methods — exactly the weakness user identified as making the review "sơ sài."
- **Origin:** Entry #5 — LA electrophysiology elderly AF review (2026-06-15); user-approved lesson

### L-024: User must explicitly OK each major phase handoff; fix-then-re-ask, never fix-then-proceed
- **Role:** orchestrator
- **Trigger:** before handing off to the critical-appraiser (Phase 4) AND before handing off to the synthesis-writer (Phase 5); and after fixing any user-requested change at either gate
- **Rule:** The orchestrator presents the phase output (retrieval summary / appraisal summary) and STOPS for explicit user OK before launching the next agent. If the user requests changes or supplements (e.g., "find more full text," "add a search," "fix the tier"), the orchestrator makes those changes and ASKS AGAIN — it does NOT proceed to the next phase automatically after fixing. The loop continues until the user explicitly signals approval (e.g., "ok," "tiếp tục," "approve"). Two specific gates:
  - **Gate 2b (post-retrieval):** After retrieval + corpus update, present: corpus size, full-text status, source availability gaps (L-022/L-023), any PMID issues. Ask: "Có muốn bổ sung gì trước khi thẩm định không?" Wait for OK.
  - **Gate 4b (post-appraisal):** After appraisal, present: GRADE summary per axis, flagged contradictions, Assumption Register highlights. Ask: "Có muốn điều chỉnh gì trước khi viết bài không?" Wait for OK.
- **Why:** User feedback (Entry #5, 2026-06-15): "ghi nhận rõ, trước khi giao việc cho appraiser và writer, người dùng phải ok mới làm. Nếu người dùng OK → yêu cầu sửa, sửa xong lại hỏi tiếp chứ không được giao việc luôn." These checkpoints cost one extra message per phase; the alternative is delivering a review the user considers shallow because coverage gaps were not caught early.
- **Origin:** Entry #5 — user-stated requirement, 2026-06-15; approved immediately

### L-025: Verify signal modality (bipolar / unipolar / omnipolar) before bundling citations for a voltage-threshold claim
- **Role:** synthesis-writer, citation-verifier
- **Trigger:** writing a claim that a voltage threshold is "used consistently" across multiple studies
- **Rule:** Before bundling citations for any electrophysiology voltage-threshold sentence, check each study's signal modality. Bipolar (< 0.5 mV LVZ), unipolar (~5th-percentile-derived, ≈ 0.7 mV), and omnipolar (systematically higher than bipolar) use *different, non-interchangeable* thresholds. If modalities differ across studies, cite each separately with its own threshold — never merge them into a single "[X,Y,Z]" bundle.
- **Why:** Entry #6 (LA-EP elderly AF review): van der Does [8] uses unipolar voltage with a 5th-percentile threshold (~0.73 mV), yet the draft bundled it with bipolar studies [5,7] in a "< 0.5 mV used consistently [5,7,8]" claim. The QA verifier caught this as I-01 (mismatched-citation). Fix: remove [8] from the blanket threshold statement and distinguish the modality explicitly.
- **Origin:** Entry #6 — 2026-06-16

### L-026: Khi MCP tools bị chặn, dùng WebSearch ngay để xác nhận PMID — không để "pending"
- **Role:** retriever, orchestrator
- **Trigger:** bất kỳ PMID nào chưa xác nhận sau khi MCP tool bị từ chối/blocked
- **Rule:** Nếu `get_article_metadata` hoặc các PubMed MCP POST tools cần approval/bị chặn, **ngay lập tức** dùng WebSearch với query `site:pubmed.ncbi.nlm.nih.gov "[tên tác giả đầu] [từ khóa tiêu đề] [năm]"` để xác nhận PMID trước khi ghi vào store. Không được ghi "⏳ PMID pending" rồi chuyển sang bước tiếp theo — PMID phải được xác nhận tại bước retrieval.
- **Why:** REF-040 (Huang 2020 PTFV1 MA) bị để "pending" suốt cả quá trình vì MCP tools cần approval. WebSearch tìm ra PMID 32022368 ngay lập tức — user phải tự làm thay. Một bản ghi với PMID chưa xác nhận không phải là bản ghi "đã thẩm định".
- **Origin:** Entry #6 — 2026-06-16, user-caught

### L-027: Xác nhận PMID bằng cách mở trang PubMed và kiểm tra tiêu đề — không tin vào kết quả từ Consensus hay agent mà không kiểm tra chéo
- **Role:** retriever
- **Trigger:** trước khi ghi bất kỳ PMID nào vào reference store, đặc biệt khi PMID đến từ Consensus search hoặc agent
- **Rule:** Sau khi có một PMID từ bất kỳ nguồn nào (Consensus, PubMed search, agent), mở trang `pubmed.ncbi.nlm.nih.gov/[PMID]/` và xác nhận **(a) tên tác giả đầu khớp** và **(b) tiêu đề/journal/năm khớp** với paper dự định lưu. Chỉ ghi vào store sau khi hai trường này khớp.
- **Why:** REF-021 (Mené 2024) bị ghi với PMID 40171797 — một PMID có thật nhưng là bài khác. PMID đúng là 39245073. Lỗi "wrong-but-real PMID" (đã có trong L-021 cho RCT results paper, nay tái xuất hiện cho bài registry) đặc biệt nguy hiểm vì vượt qua kiểm tra "PMID tồn tại".
- **Origin:** Entry #6 — 2026-06-16, user-caught
