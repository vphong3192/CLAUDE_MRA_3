# Proposed Lessons & Evolution-Log Entry — Run #4 (ablation metrics RF-PVI)

> **Status: PENDING USER APPROVAL.** Nothing here is saved to `lessons.md` or `evolution-log.md` yet.
> Curator will append on the lead's confirmation that the user approved.
> Run: ablation metrics in RF-PVI for AF · 2026-06-14 · Rubric 0.98 — EXCELLENT.

---

## Part A — Proposed new lessons (L-016, L-017)

### L-016: Reconcile inline citations against the reference list before handoff
- **Role:** writer
- **Trigger:** finishing any draft that has a numbered reference list
- **Rule:** Before handing the draft to QA, run a two-way reconciliation: every reference-list entry [n] must appear at least once inline, and every inline [n] must have a list entry. Resolve orphans (listed-but-uncited) by either citing them in the relevant section or removing them from the list. Do not rely on QA to catch this.
- **Why:** This run left refs [29–34] (3 CF-catheter benchmarks + 3 society guidelines) in the list but uncited inline — orphan references that QA had to fix. An orphan reference signals retrieved-but-unused evidence and looks like sloppy scholarship to an expert reader; catching it pre-handoff keeps the writer, not QA, accountable for completeness.
- **Origin:** Entry #4 — ablation metrics RF-PVI review (2026-06-14)

### L-017: Embed L-011 guideline citations in the consensus section, not just the reference list
- **Role:** writer
- **Trigger:** the strategy ran an L-011 guideline-body search (ESC / AHA / ACC / ADA / NICE / HRS) and those guidelines are in the store
- **Rule:** When society guidelines were retrieved per L-011, cite them explicitly in the "Established consensus" section to anchor each consensus statement — do not leave them sitting only in the reference list. The guideline must do interpretive work in the text (what it recommends and at what strength), not merely appear as a number.
- **Why:** L-011 exists to make reviews read as complete to clinicians; that value is lost if the guidelines are retrieved and then forgotten at the writing stage. This run retrieved the 2024 ESC/EACTS, 2023 ACC/AHA, and 2017 HRS guidelines but did not embed them until QA's FIX — guideline citations are easy to fetch and easy to forget to use, so the omission slightly weakened L-011 coverage (cost C10 0.1).
- **Origin:** Entry #4 — ablation metrics RF-PVI review (2026-06-14)

---

## Part B — Proposed evolution-log entry (Entry #4)

```
═══════════════════════════════════════════════
### Entry #4 — 2026-06-14 — Ablation metrics in RF-PVI for AF (AI/LSI/LID/CF/AID, TactiFlex SE)
**Task:** So sánh các chỉ số tổn thương trong triệt đốt RF-PVI điều trị rung nhĩ (AI, LSI, LID, CF,
AID/TactiFlex SE). Mục đích: nghiên cứu/học thuật. Đối tượng: BS điện sinh lý can thiệp. Ngôn ngữ:
tiếng Việt. Độ sâu: ~3000+ từ.
**Rubric total:** 0.98 → EXCELLENT (≥0.90)
**Per-criterion:** C1 1.0 · C2 1.0 · C3 1.0 · C4 1.0 · C5 1.0 · C6 1.0 · C7 1.0 · C8 1.0 · C9 1.0 · C10 0.9
(10-criterion verifier rubric; C10 Completeness held at 0.9 for thin guideline integration pre-FIX).
**Process:** protocol → retrieval (source/ checked — L-012 applied; 10 user PDFs/HTML used) → Research Map
**GATE CLEARED** (user answered all map questions + uploaded 10 PDFs + "tiếp tục quy trình nghiên cứu",
2026-06-14 08:28 UTC, received after the map was shown — satisfies L-014, no self-clear) → appraisal
(GRADE + RoB) → Vietnamese draft → QA + rubric + audit. Law-compliance 6/6 PASS.
**Records:** 35 PMID-verified records (2 UNCONFIRMED — Segreti A022, Pedersen — excluded/uncited per L-009);
10 load-bearing records full-text-confirmed via user-supplied HTML+PDF in source/af-ablation-metrics/.
**Process notes (non-law, recorded):**
- Full-text retrieval initially BLOCKED — PubMed metadata/full-text MCP + NCBI E-utilities permission-denied
  → user uploaded 10 HTML+PDF files → resolved. QA could not independently re-resolve PMIDs (same egress
  block); mitigated by retriever title-confirmation at capture + verifier full-text re-read of the 10
  highest-stakes records. Recommend re-granting PubMed metadata permission for future runs.
- bioRxiv/medRxiv preprint sweep permission-denied → 0 preprints → flagged in §11 Limitations (L-004 honoured
  in intent; gap disclosed honestly).
- Synthesis writer hit Consensus API session limit → file was already complete (204 lines), no data loss.
- AutoMark Index: 0 PubMed results → reported as "not peer-reviewed literature, future direction only"
  (Law 1 "no source found" treatment, not a fabrication).
**Violations found:** none blocking; no fabricated citation; both human gates honoured.
**Defects:** LOW (writer) — orphan reference entries [29–34] listed but uncited inline; L-011 society
guidelines (ESC/AHA/HRS) retrieved but not embedded in the consensus section. → QA FIX applied (added
[29,30,31] to §6.4 and [32,33,34] to §10.1; numbers verified vs A018/A019/A020). Non-blocking.
**Key scientific findings (method knowledge for future cardiac-EP reviews):**
- No RCT exists for ANY lesion-quality index (AI/LSI/LID/AID) vs conventional — the entire efficacy thesis
  rests on cohort/historical-control data (GRADE LOW for AI/LSI, VERY LOW for LID/AID).
- Both CF RCTs (TOCCASTAR, Ullah) are NEGATIVE for 12-mo clinical benefit — the strongest conclusion in the
  whole review is this MODERATE-certainty negative; cohort-positive CF data must NOT override it (Law 3).
- A028 (Lian, LID-vs-LSI head-to-head) is fatally confounded: the LID arm had NO contact-force sensing, so
  the comparison is not metric-vs-metric. Internal stat inconsistency too (KM P=0.037 vs Table-2 P=0.09).
- AID/TactiFlex SE is an emerging paradigm with pilot-level evidence only (single-arm n=30, pivotal n=334).
**Lessons applied:** L-001/002/003/006/007/009/010/011/012/014/015 — all fired correctly.
**Lessons learned → proposed (pending approval):** L-016 (inline-vs-list reconciliation before handoff),
L-017 (embed L-011 guideline citations in the consensus section).
**Actions taken:** built `reference/af-ablation-metrics-pvi-rf.md` (35 verified records); 10 full-text-backed
via source/af-ablation-metrics/; delivered `_workspace/06_final_review.md` (clean, post-FIX). Vietnamese
terms for the glossary to be confirmed with the user (see Part C).
**Status:** clean EXCELLENT run; first run to clear the gate via PDF-upload + explicit Vietnamese approval and
to operate fully on user-supplied full text under an egress block — good positive evidence the gate + provenance
disciplines hold under degraded retrieval.
═══════════════════════════════════════════════
```

---

## Part C — Vietnamese terminology candidates (to confirm with user before saving to vi-terminology.md)

These English↔Vietnamese term choices were used in the draft and, if the user confirms, should be appended
to `review-synthesis/references/vi-terminology.md` for consistency across future cardiac-EP reviews:

- **pulmonary vein isolation (PVI)** — cô lập tĩnh mạch phổi
- **radiofrequency (RF) ablation** — triệt đốt bằng năng lượng tần số radio (sóng cao tần)
- **Ablation Index (AI)** — chỉ số triệt đốt (giữ nguyên "Ablation Index/AI" trong ngoặc)
- **Lesion Size Index (LSI)** — chỉ số kích thước tổn thương
- **Local Impedance Drop (LID)** — mức sụt trở kháng tại chỗ
- **contact force (CF)** — lực tiếp xúc
- **first-pass isolation** — cô lập ngay lần đốt đầu (first-pass)
- **durable lesion** — tổn thương bền vững
- **inter-lesion distance (ILD)** — khoảng cách giữa các điểm đốt

(Curator note: confirm these match the EP audience's preferred Vietnamese usage before persisting.)

---

## Approval checklist (for the lead to relay to the user)

- [ ] Approve **L-016** (writer: inline-vs-list reconciliation) — as-is / edit / reject
- [ ] Approve **L-017** (writer: embed L-011 guideline citations in consensus) — as-is / edit / reject
- [ ] Approve **Entry #4** for the evolution-log archive
- [ ] Approve which **Vietnamese terms** (Part C) to add to the glossary
