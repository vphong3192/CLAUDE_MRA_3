# 07_proposed_lessons.md — PROPOSED (awaiting user approval before saving)

Per review-before-apply, nothing below is saved until you approve. On approval: lessons → `lessons.md`,
the entry → `evolution-log.md`.

## Proposed evolution-log entry
```
### Entry #1 — 2026-06-14 — Semaglutide CV prevention in non-diabetic obesity (HARD test case)
Task: Tổng quan semaglutide trong dự phòng tim mạch ở người béo phì không ĐTĐ; nghiên cứu/tìm gap;
      BS tim mạch/nội tiết; ~2500 từ; tiếng Việt. (Frame broadened from primary→CV prevention per user.)
Rubric: 0.82 → MET. (T1 .75 T2 .85 T3 .85 T4 .80 T5 .85 T6 .85)
Process: protocol→retrieval→Research Map GATE CLEARED→appraisal→draft→QA. source/ not checked (no PDFs).
Violations: none blocking. Deviation: source/ folder not listed/asked.
Lessons: see below (L-008…L-012).
Actions: built reference/glp1-cv-primary-prevention.md (R1–R9 verified); confirmed Yin 2025 PMID 40207414;
         Vietnam search → no on-topic data (population gap). Baseline recorded for Test Case 2.
```

## Proposed digest lessons (role-tagged)
- **L-008 [retriever]** — Trigger: querying ClinicalTrials.gov. Rule: don't combine intervention + condition
  + phase in one query first; over-constrained queries return 0 silently. Start broad (intervention OR
  condition alone), then narrow. Why: a 0 here looks like "no trials exist" and gets reported as a false gap.
  Origin: search #3 returned 0, retry recovered 11 trials.
- **L-009 [retriever]** — Trigger: a study surfaces via Consensus without a PMID. Rule: confirm PMID/DOI via
  a PubMed title search before it enters the citable store. Why: Consensus metadata (incl. year) can be
  imprecise; unconfirmed IDs risk Law-1 violations. Origin: Yin 2025 confirmed (40207414); Kelkar left
  unconfirmed and therefore uncited.
- **L-010 [appraiser/writer]** — Trigger: reporting a composite endpoint (e.g., MACE). Rule: decompose into
  components before stating the headline; the benefit may rest on only some. Why: "↓20% CV events" was driven
  by MI + all-cause mortality, NOT CV death or stroke — stating the composite as if all moved overstates it.
  Origin: Yin 2025 component analysis.
- **L-011 [strategist]** — Trigger: topic has society guidance (CV/obesity/endocrine). Rule: add a guideline-
  body search (ESC/AHA/ACC/ADA) explicitly; absence cost a search-comprehensiveness point. Why: a review
  without the relevant guideline reads as incomplete to clinicians. Origin: T1 = 0.75 (no guideline cited).
- **L-012 [orchestrator]** — Trigger: every run, including tests. Rule: list `source/` and ask the user, even
  when you expect it empty. Why: silence here was a v1 failure and recurred this run as a deviation. Origin:
  audit flagged source/ not checked.

## For the Vietnamese glossary (vi-terminology.md) — new terms used, confirm to add
| English | Used Vietnamese |
|---|---|
| Major adverse cardiovascular events (MACE) | biến cố tim mạch bất lợi nặng (MACE) |
| Hazard ratio | tỷ số nguy cơ (HR) |
| Relative risk | nguy cơ tương đối (RR) |
| Primary/secondary prevention | dự phòng nguyên phát / thứ phát |
| Body mass index | chỉ số khối cơ thể (BMI) |
| GLP-1 receptor agonist | chất chủ vận thụ thể GLP-1 (GLP-1 RA) |
```
Approve all / edit / reject which?
```
