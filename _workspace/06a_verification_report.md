# 06a_verification_report.md — Phase 6 QA · metformin in adult T2D · 2026-10-27

**Verifier:** citation-verifier (independent; read draft + store + cards + NCBI XML in `source/metformin-t2d/` directly; `05b_writer_notes.md` used only to locate items).
**Draft verified:** `_workspace/05_draft_review.md` (commit ae13729 + f066067). **Pass:** 1 (first verification).

## DECISION: **FIX — do NOT deliver yet; `06_final_review.md` NOT produced.**
No fabricated or unresolvable citation (no BLOCK). Law 1 clean, Research Map gate cleared, Vietnamese, rubric 0.785 (MET) — the regression Case-1 PASS criteria are met. But 12 FIX items remain, five of them substantive misreads or over-readings (F1–F5) that a clinician reader would act on. All are correctable with word-neutral edits.

---

## A. Mechanical floors (re-run by me, not inherited)

| Check | Result |
|---|---|
| `verify_quotes.py` re-run on `04b_cards.jsonl` + `source/metformin-t2d/` (P8) | **104 accepted / 0 rejected**, exit 0; output identical to `04c_quote_locks.md` apart from one trailing slash. No claim in the draft rests on a REJECTED card. |
| `citation_audit.py` on `05_draft_review.md` → `06b_citation_audit.md` | **PASS, exit 0.** 0 HARD-FAIL; 33 entries / 33 distinct inline; 33 of 39 store records cited (85%). 4 WARN `number_not_in_source`, all separator formatting ("1.000" = 1,000 mg in card M12-c1; "44,2" = 44.2% in card H12-c5). |
| Reference identity (my own script vs. NCBI PubMed XML on disk) | All 33 entries: PMID, DOI, title, first-author, first-six-authors-then-et-al, journal, year, volume(issue), pages **match the PubMed record**. 0 mismatches. [28] has no vol/pages because PubMed has none (declared in the entry). |
| NCT02915198 (cited inline, no ref entry) | Re-fetched from ClinicalTrials.gov MCP: **exists** — VA-IMPACT, metformin XR vs placebo, **prediabetes** + ASCVD, n=7,410, recruiting, primary completion 2029-09-28. The sentence is true; the attribution is the problem (F9). |
| Dropped M02/M13/M17 cited? | **No** (PMIDs 38639546, 36148880/36151309, 42365335 absent from draft). |
| Preprints cited? | None. No preprint-unlabeled defect possible. |
| Length | Counted by the amendment's own method: 1,996 whitespace tokens incl. title, **1,967 excl. title/subtitle**, up to the `## 6.` heading. Within "~1800–2000" (user's verbatim choice). **Constraint for the writer: net word change ≤ 0** (margin is only +4 by the writer's count, +33 by mine). |
| Numbers with no card (checked directly in NCBI text) | 301 RCT (Palmer abstract), 816 RCT (Shi abstract), 71 RCT (Nabrdalik abstract), 21 articles (Atkinson abstract), FDA 2008 (Griffin full text) — all real. They are simply not card-locked (see F6). |

**Residual stated, not hidden:** the locks prove a quote is in NCBI-served text and the claim's numbers are in that quote. They did **not** catch F1 (0.98 is a real number, from the wrong stratum) or F2 (31/1454 is a real number, for the wrong endpoint). Those were caught only by reading claim vs. source side by side.

---

## B. FIX list (for the writer) — section · sentence · problem · required change

Tags: `MC` mismatched-citation · `OC` overstated-certainty · `MX` missed-contradiction · `FE` format-error · `PR` process-claim overstated (R4-adjacent).

| # | Sev | Where | Problem | Required change (keep net words ≤ 0) |
|---|---|---|---|---|
| **F1** `MC` | High | §3.3 "Nhiễm toan lactic", sentence 1; SoF row "A4 Nhiễm toan, eGFR ≥30" | "Khi eGFR ≥30 … (aHR 0,98; 0,89–1,08)". In Lazarus [7] (abstract, card S01-c1) 0.98 is the **overall** estimate "overall or in eGFR 45–59 and 30–44"; the overall cohort **includes eGFR <30** (where aHR is 2.07). It is not an eGFR ≥30 estimate. The eGFR-specific values are 45–59 aHR 1.16 (0.95–1.41) and 30–44 aHR 1.09 (0.83–1.44). | Say "toàn đoàn hệ (mọi mức eGFR) aHR 0,98" **or** replace by the two stratum values (1,16 và 1,09, đều không có ý nghĩa). Same fix in the SoF row. |
| **F2** `MC` | High | §3.2 "So với SU, kết quả không nhất quán [GRADE: thấp] [2,12]"; SoF row "Tử vong so với SU" | Endpoint mismatch. AHRQ [2] = **cardiovascular** mortality lower with metformin; the Cochrane 31/1454 vs 31/1441 [12] is **all-cause** mortality (checked in PubMed XML of H06). The two are not in conflict; Cochrane's own CV-mortality result (4/1441 vs 8/1447, very low certainty) points the same way as AHRQ. The SoF row prints 31 vs 31 beside "tử vong tim mạch thấp hơn" as if it were the same outcome. (The 4-vs-8 figures have no card; do not add them without one.) | Reword: "So với SU: AHRQ thấy tử vong tim mạch thấp hơn [2]; Cochrane thấy tử vong chung tương đương, độ chắc chắn rất thấp [12] — hai kết cục khác nhau, chưa đủ kết luận." Drop "không nhất quán". In SoF label the Cochrane figure "tử vong chung". Keep the appraiser's label [thấp] (the appraisal's C9 "inconsistency" rationale does not hold, see §E). |
| **F3** `MC`/`OC` | Med | §3.3 "Tiêu hoá": "ngừng thuốc do biến cố bất lợi **chỉ** tăng so với giả dược ở bệnh thận mạn [3,14]" | "chỉ" (only) is unsupported. [3] reports RR 1.080 (NS) against **all controls pooled** — it never reports a placebo-only discontinuation estimate in non-CKD patients, so nothing shows the excess is confined to CKD. [14]'s population is CKD with 4/11 ADPKD. | "…không tăng so với mọi nhóm chứng gộp [3]; so với giả dược, rút khỏi thử nghiệm do không dung nạp tăng trong RCT ở bệnh thận mạn (gồm cả thận đa nang) [14]". Delete "chỉ". |
| **F4** `OC` | High | §4.2 (1) | (a) **Kết luận**: "nếu có thì không đến từ đột quỵ hay tử vong tim mạch" over-reads null, imprecise CIs. Stroke RR 1.04 (0.73–1.48) and CV death 0.97 (0.80–1.16) are compatible with benefit up to ~27% and ~20% (the draft itself uses CI-compatibility for the steelman). Absence of significance is not evidence the benefit does not come from them. (b) Steelman: "mọi ước tính điểm từ RCT cho tử vong … đều nghiêng về metformin" — false as worded: Li's CV death RR 1.13 and the combination RR 1.49/2.21 (the draft's own §3.2) do not favour metformin. True only for all-cause death, monotherapy vs control. (c) "khoảng ấy cũng tương thích với tăng đột quỵ" — "khoảng ấy" is the mortality CI; the 48% is the **stroke** CI [4]. (d) "Tách thành phần" components are Griffin's [4], a different synthesis from Silverii's MACE [6]; say so. | (a) "…và ước tính điểm chỉ nghiêng về nhồi máu cơ tim, không phải đột quỵ hay tử vong tim mạch [GRADE: thấp]." (b) "mọi ước tính điểm đơn trị so với đối chứng cho tử vong chung và nhồi máu". (c) "khoảng tin cậy của đột quỵ cũng tương thích…". (d) "Trong phân tích của Griffin [4], các thành phần: …". |
| **F5** `MX` | High | Summary ("chưa được thử *thay* metformin [9]"); §3.5 last sentence; SoF row "A6 Thay metformin đầu tay… Không có thử nghiệm đối đầu [9,22]" | Silverii [6] (card H10-c6, full text): "significant inconsistency … only for metformin vs SGLT2i (with **metformin superior in direct comparison** but not in indirect comparison and NMA)". So a direct trial-level comparison exists in the corpus and favours metformin; the writer dropped it (verified: absent from draft). "Không có thử nghiệm đối đầu"/"chưa được thử" is therefore inaccurate, is cited to [9] (which does not say it), and omits a datum on the metformin side of controversy (3). What is true: no source tests SGLT2i/GLP-1 RA vs metformin **as first-line in drug-naive adults on hard outcomes**. | Summary: "…nhưng bằng chứng chủ yếu trên nền metformin [9]". §3.5 and SoF: "Không nguồn nào cho thấy so sánh đối đầu ở người chưa dùng thuốc về kết cục cứng; Silverii ghi nhận so sánh trực tiếp metformin–SGLT2i nghiêng về metformin nhưng không nhất quán với NMA [6]". Cite [6], not [9,22]. Offset words elsewhere (see §D). |
| **F6** `PR` | Med | §2 last clause "mọi con số đã khoá với trích dẫn nguyên văn từ NCBI"; Summary "Tổng quan hệ thống đăng ký trước" | (a) Not every number is locked: PRISMA counts are machine counts, and 301/816/71/21/2008 are on no card (they are real — I checked). Claiming a verification step beyond what the artifact shows is the R4 pattern. (b) "đăng ký trước" will be read by internists as a PROSPERO-type registration; it is an internal protocol saved before the search (§2 says "Đề cương … lưu trước"), single-pass AI screening, 68 records deferred unread. | (a) "các ước tính hiệu ứng chính đã khoá…" (b) "Tổng quan có phương pháp (PRISMA, GRADE), đề cương lưu trước khi tìm". |
| **F7** `MC` | Low–Med | §3.1 | (a) "SU, TZD, DPP-4i đều cho HbA1c cao hơn [1,2]": [2] AHRQ says reductions were **similar** across monotherapies **except** DPP-4i (card H07-c1); only [1] supports SU/TZD higher (TZD lower CI 0.00). The SoF row states this correctly; the text does not. (b) "làm tăng **tới 5 kg**" — source: "between-group differences up to 5 kg" (card H07-c2); SoF has it right ("chênh lệch tới 5 kg"). | (a) "…cho HbA1c cao hơn [1]; AHRQ cho kết quả tương tự, trừ DPP-4i [2]". (b) "chênh lệch giữa các nhóm tới 5 kg". |
| **F8** `MC`/`OC` | Low–Med | §3.5 | (a) "vị trí của metformin trong đó **chưa xác định được**" reads as if the 2026 consensus leaves it open; in truth only the abstract was readable (H01 abstract silent on metformin). (b) "khuyên dùng … phối hợp khi có bệnh tim mạch…": source says combination "should be considered" (card H01-c2). (c) "SGLT2i và GLP-1 RA giảm tử vong [GRADE: cao] [5,29]": [29] (Nong, abstract) says "cardiovascular and kidney benefits … moderate-to-high" — not mortality; the High certainty is [5]. | (a) "…chưa xác định được vì chỉ đọc được tóm tắt". (b) "cân nhắc phối hợp". (c) cite [5] for mortality; [29] for lợi ích tim–thận. |
| **F9** `FE`/`MC` | Low–Med | §4.3 "Còn bỏ ngỏ" and "Tìm kiếm" | (a) "(NCT02915198 chỉ ở tiền đái tháo đường) [4,12]": neither [4] nor [12] mentions that trial; it has no reference entry or hyperlink (Law 1: a specific citation traceable to a record). (b) Limitations omit that the medRxiv source was a **single one-page, one-category date sweep** (no keyword search) and Consensus returned only the free-tier top-10 per query, though §2 lists both as sources. | (a) Move NCT out of the [4,12] group and hyperlink inline: `[NCT02915198](https://clinicaltrials.gov/study/NCT02915198)` (or add as ref 34 in Vancouver registry form). (b) Add "medRxiv chỉ quét một trang/một chuyên mục; Consensus 10 kết quả/truy vấn". |
| **F10** `MC` | Low | SoF row "A5 Tử vong so với giả dược (RCT)" | Row mixes RCT RR 1.00 [14] with MACE HR 0.91 from Clegg [23], a PS-matched **non-randomised** metformin-user vs non-user comparison inside two CVOTs (appraisal: ROBINS-I serious). The row label "(RCT)" misdescribes it. | Split or relabel: "…; so sánh người dùng/không dùng metformin trong hậu kiểm (không ngẫu nhiên): MACE HR 0,91 [23]". |
| **F11** `OC` | Low–Med | Summary "Kết luận" and §5 first sentence: "an toàn khi eGFR ≥30" | Unhedged on GRADE-Low observational evidence with an ICD-code outcome (the draft's own §3.3 says so); Summary conclusion carries no GRADE tag. "An toàn" > "không thấy tăng nhiễm toan". | "dùng được khi eGFR ≥30 (đồng thuận ADA/KDIGO 2022; không thấy tăng nhiễm toan) [GRADE: thấp]". |
| **F12** `FE` | Low | Title block and reference header | Internal artifacts for a deliverable: "*Bản nháp*" subtitle; the italic reference header ("Mã nguồn nội bộ (MET-…)"); `(MET-xx)` tag at the end of each of the 33 entries. | Remove at finalisation (the lead may do it mechanically; re-run `citation_audit.py` afterwards on `06_final_review.md`). Removing the subtitle also frees ~7 tokens toward the word budget. |

### Advisory (non-blocking; writer's discretion, word-neutral)
- A1 §3.2 and §3.4.1: "nhiều khả năng do nhiễu theo chỉ định" / "khó tin" are the review's own inference, not the cited authors'. §4.2 (3) already labels such text "(suy luận)"; do the same here for consistency (Law 1: inference must be flagged).
- A2 §4.2 (3) Kết luận: "metformin là thuốc phối hợp hợp lý [22]" — [22] is a CKD consensus; the sentence is framed "bệnh tim mạch hoặc bệnh thận mạn". Support exists only for the CKD arm; say "ở bệnh thận mạn".
- A3 §3.4.1: the "hậu kiểm hai thử nghiệm [23]" clause sits directly after a placebo-RCT clause; add "(không ngẫu nhiên)" (see F10).
- A4 §4.2 (1) "Chỉ Silverii thấy giảm MACE có ý nghĩa" — add "trong các phân tích gộp RCT" (observational data [13,24,25] also show lower CV events).
- A5 COI not flagged (e.g., Tsapas [9]: EFSD with unrestricted AstraZeneca grant, per appraisal). Rubric T4 box; optional given length cap.

---

## C. Claim-by-claim table (section clusters; all inline [n] examined)

| Section / claim | Cites | Verdict | Note |
|---|---|---|---|
| Summary: HbA1c ≥ other orals, weight, hypoglycaemia, diarrhoea [Moderate] | 1–3 | PASS | cards M03-c1/c3, H07-c2, H13-c2 |
| Summary: no proven mortality/MACE benefit [Low] | 4–6 | PASS | Silverii significant MACE disclosed in §4.2 |
| Summary: eGFR ≥30 no acidosis [Low]; <30 contested [Very low] | 7,8 | PASS (see F11 for conclusion) | S01-c1/c2, H12 |
| Summary: SGLT2i/GLP-1 RA ↓ mortality [High]; "chưa được thử thay metformin" | 5, 9 | **FIX F5** | first half PASS (H08-c3) |
| Summary Methods "đăng ký trước" | — | **FIX F6** | |
| §1: FDA 2008; new drugs tested on metformin; first-line reopened | 4, 9, 10 | PASS | FDA 2008 verified in Griffin full text (no card); M01-c1/c2; M18-c1 |
| §2: PRISMA 260→228→160→30 (+6 manual −3 = 33) | — | PASS | reconciles with `02i/02j` and store summary (36 = 30 + 6; −3 dropped) |
| §2: "mọi con số đã khoá" | — | **FIX F6** | |
| §3.1 HbA1c / weight / hypoglycaemia / durability | 1,2,5 | **FIX F7**; durability PASS (H07-c6) | |
| §3.2 RCT few/old, UKPDS 52.3–70.5%, 4 trials, no low-RoB | 4 | PASS | H04-c2/c3/c4 |
| §3.2 mortality null in 3 MAs; Cochrane no clear evidence | 4,5,11,12 | PASS | H04-c1, H05-c1, H08-c1, H06-c4 |
| §3.2 vs SU "không nhất quán" | 2,12 | **FIX F2** | |
| §3.2 observational CV mortality OR 0.44 | 13 | PASS (A1) | M05-c2 |
| §3.2 "phối hợp có hại" depends on UKPDS, unconfirmed by NMAs | 11,1,9 | PASS | H05-c2/c3, M03-c2, M01-c1 |
| §3.3 diarrhoea 12.94%, RR 2.445 | 3 | PASS | H13-c1/c2 |
| §3.3 discontinuation "chỉ … CKD" | 3,14 | **FIX F3** | |
| §3.3 XR may help | 3,15,16 | PASS | M11-c3, H13-c4, M10-c2 |
| §3.3 B12 dose/duration; VN 18.6% / 22.1%; PPI | 17–20 | PASS | M07-c2, M09-c1, M14-c1 (abstract also shows dose+duration), M08-c1 |
| §3.3 acidosis aHR 0.98 "eGFR ≥30" | 7,21 | **FIX F1** | rest of sentence PASS (M12-c4) |
| §3.4.1 CKD vs placebo; post hoc; observational implausible | 14,23,24,25 | PASS (A3) | H14-c2, M15-c1, M04-c1, M16-c2 |
| §3.4.1 eGFR strata bullets | 7,22,26,8 | PASS | S01-c1/c2, M12-c1/c2, H11-c2, H12-c3 |
| §3.4.2 older adults: no direct evidence (inference flagged) | 8 | PASS | H12-c4; protocol subgroup labelled (L-038 ✓) |
| §3.4.3 HF: no direct evidence; no effect on HF admission | 5,11 | PASS | H05-c1, H08-c5 |
| §3.4.4 cirrhosis aHR 1.13 / decompensation / >1000 mg | 27 | PASS | S02-c1/c2; dose trend also significant for decompensation in abstract |
| §3.5 AHRQ first-line; ADA/KDIGO 2022 | 2,22 | PASS | H07-c5; M12-c7/c8 |
| §3.5 ADA/EASD 2026 | 28 | **FIX F8** | H01-c1/c2 |
| §3.5 low-risk no difference [9]; "không nguồn nào so sánh trực tiếp" | 9 | **FIX F5** | |
| §4.1 consensus bullets (4) | 1–3,17–19,7,22,5 | PASS | B12 as "consensus" is Low-graded; acceptable, labelled |
| §4.2 (1) MACE controversy | 6,4 | **FIX F4** | OR 0.68/0.69 pair and component numbers PASS |
| §4.2 (2) eGFR <30 | 8,30,7 | PASS | HR 1.23 / 1.26 pair, MSM 1.34, 44.2% SU, PK 500 mg all match cards; "không khuyến cáo tiếp tục dưới 30" consistent with appraisal |
| §4.2 (3) first-line | 4,5,9,22 | PASS (A2) | "(suy luận)" correctly flagged |
| §4.3 Limitations | 8,22,28,31,32,21,4,11,12,17–19,33 | **FIX F9**; otherwise PASS | H02 [31]/H03 [32] cited only to record "not readable" (per appraisal) ✓; NICE/FDA second-hand ✓; 68 deferred ✓; 9/16 abstract-only ✓ |
| §5 conclusion + 3 practice items | 5,22,15,17,18,20,27 | PASS (F11) | doses match M12-c1/c2; B12 check consistent with M07-c3/M09-c3 |
| §6 SoF (26 rows) | various | PASS except F1, F2, F5, F10 rows | every effect estimate matches an accepted card; every GRADE label equals `04_appraisal.md` §3 |
| References [1]–[33] | — | PASS | identity script; all hyperlinked (DOI + PMID); Vancouver consistent; see F12 |

**GRADE alignment (both directions):** Moderate/High findings are stated plainly (HbA1c, weight, diarrhoea, SGLT2i/GLP-1 RA mortality) — no weasel verbs. Low/Very-low findings are hedged ("chưa được chứng minh", "gợi ý", "liên quan"). Over-claims on Low evidence found only at F4(a), F11 (and F3 "chỉ"). No Low finding stated as fact elsewhere. Steelmen present for all three controversies (F4(b) corrects the one over-absolute).

**Spot-check coverage:** every inline citation was read against its card or source text; ≈ 60 cited sentences + 26 SoF rows (>> 10%). Direct NCBI-text reads (beyond cards) for: Griffin FDA 2008; Cochrane H06 CV/all-cause endpoints; Lazarus abstract; Yen dose-response; Phan abstract; Nabrdalik discontinuation; Palmer/Shi/Nabrdalik/Atkinson totals.

---

## D. Word-budget suggestions (so fixes stay ≤ 2,000)
Net adds ≈ +45 tokens across F1–F11. Offsets: delete "*Bản nháp · bằng chứng đến 27/10/2026*" (−7, also F12); Background sentence 2 "Vì vậy, vai trò đầu tay của metformin đang bị đặt lại [10]" can lose "Vì vậy," (−2); in §3.3 delete "dù kết cục là mã ICD" duplicate wording only if F1 replaces it (keep the ICD caveat; it is important); §4.3 "Sai lệch" bullet can fold "chỉ tiếng Anh và tiếng Việt" into the language clause (−5). The writer decides; the cap is a hard user choice, not a preference.

---

## E. Upstream notes (for lead / lessons-curator; not writer fixes)
1. `04_appraisal.md` C9/§3 rates "CV mortality vs SU" Low on "−1 inconsistency (AHRQ lower vs Cochrane very low, 4 vs 8 events)". Cochrane's 4 vs 8 CV deaths is the **same direction** as AHRQ; the apparent conflict arose only because the all-cause 31 vs 31 figure was set beside a CV outcome. The Low label is defensible on imprecision/depth, not on inconsistency. Recommend correcting the appraisal's reason at Phase 7.
2. `04_appraisal.md` C-L-010 "any MACE benefit is not carried by stroke or CV death" and the "every RCT point estimate for ACM/MI favours metformin" steelman are both over-absolute; the draft inherited them (F4).
3. `03_research_map.md` still carries the header "Status: AWAITING USER APPROVAL" although `03a_gate_approval.md` records clearance — cosmetic, but a reader of the map alone would conclude the gate is open.
4. The "Methods" line "mọi con số đã khoá" mirrors `04_appraisal.md` §0 wording scoped to *cards*; the scope was lost in translation to the reader-facing draft.

## F. Defect tags for lessons-curator
`mismatched-citation` ×4 (F1 stratum mislabel; F2 endpoint mismatch; F7; F10) · `overstated-certainty` ×4 (F3 "chỉ", F4 null-as-absence + "mọi", F11 "an toàn") · `missed-contradiction` ×1 (F5, Silverii direct comparison dropped in the length cut) · `process-claim-overstated` ×1 (F6) · `format-error` ×2 (F9 NCT attribution/link, F12 internal tags) · wording ×1 (F8).
**Candidate lessons:** (i) A number-lock proves the number is in the quote, not that it describes the stated stratum/endpoint — verifier must check *which stratum/endpoint* each number belongs to (L-003 refinement). (ii) A length cut that drops a contradicting datum (H10-c6) can turn a true scoped absence-claim into a false general one — after any cut, re-check every "không có/chưa có" statement against the cards. (iii) "Null CI ≠ no effect" phrases ("không đến từ …") need a CI-compatibility check. (iv) Reader-facing process claims ("mọi con số đã khoá") must be scoped to what the lock covers.
**Questions for the lead (verifier cannot ask the user):** (1) Keep or strip the 33 `(MET-xx)` store tags in the delivered reference list (F12)? The task wording ("without any internal notes") suggests strip. (2) Accept advisory A5 (COI note) given the length cap, or leave out? (3) Add NCT02915198 as numbered ref 34 or inline hyperlink only (F9)?

---

# RUBRIC SCORE (pre-FIX state; `references/rubric.md`)

| Criterion (weight) | Score | Evidence |
|---|---|---|
| T1 Search comprehensiveness (25%) | **0.8** | 6/7 boxes: ≥2 sources (PubMed, Consensus, CT.gov, medRxiv) ✓; SR/MA ✓ (18); guidelines ✓ (ADA/KDIGO 2022 full text, ADA/EASD 2026 abstract); research-gap probes ✓ (CVOT, Vietnam; `02a`); current to 2026 ✓; Research Map approved ✓. ✗ MeSH/keywords not listed in the draft's Methods (they exist in `01_protocol.md`). 33 sources, but search capped (25/query) and one source failed (Elicit) — declared. |
| T2 Source quality (20%) | **0.8** | 4/5: SR/MA/NMA 18 + guideline 4 = 22/33 (67%), ≈80% with the large cohorts — borderline on ">70% tiers 1–3"; Cochrane/Q1/BMJ/JAMA/ADA cited ✓; each key claim has a high-tier cite ✓; GRADE per outcome ✓; no preprint cited. 9/16 HIGH abstract-only (declared). |
| T3 Synthesis (20%) | **0.8** | Thematic by axis, not a list ✓; agree/diverge explained (UKPDS dominance, confounding by indication, active comparators) ✓; supporting vs opposing counted ("ba phân tích gộp", "hai NMA") ✓; pattern ✓; three steelmans ✓ (one over-absolute, F4b). ✗ Mechanism barely discussed (only PK/dose). |
| T4 Critical appraisal (15%) | **0.7** | Consensus/controversy sections ✓; sample sizes/limits of key studies ✓ (4 trials, UKPDS weight, 4-study node, prevalent users, 44.2% SU); RoB tools named ✓; association vs causation ✓; abstract-vs-text discrepancies disclosed for Silverii and Lambourg ✓. ✗ COI not flagged; ✗ language slips F3/F4a/F11. Between 0.6 and 0.8 — set to 0.7; 0.8 expected after FIX. |
| T5 Citation accuracy (10%) | **0.7** | 33/33 resolve and match NCBI records; 0 fabricated; no naked numbers except NCT/FDA-2008 (real). ✗ Faithfulness: 4 mismatches (F1, F2, F7, F10) + attribution F9 in ≈ 130 cited sentences/rows (~96% faithful) — but two are clinically consequential. Pre-FIX 0.7; 0.9–1.0 after FIX. |
| T6 Applicability (10%) | **0.9** | Doses by eGFR, B12 checking, XR, cirrhosis caution, explicit "do not continue <30" ✓; limits (adults; older adults/HF absent; US/Scotland/Asia data; guideline text unread) ✓; internist level ✓; next steps (RCTs, head-to-head) ✓. Not 1.0: 2026 guideline position of metformin unknown. |

**TOTAL = 0.25·0.8 + 0.20·0.8 + 0.20·0.8 + 0.15·0.7 + 0.10·0.7 + 0.10·0.9 = 0.785 → MET (0.70–0.84).** No fabricated citation → no auto-fail. Expected after FIX: ≈ 0.82–0.84 (T4 0.8, T5 0.9); EXCEEDED (≥0.85) not reachable without the T1/T2 gaps.

---

# AUDIT REPORT — metformin in adult T2D (Case 1, EASY)

```
RUBRIC TOTAL: 0.785 → MET
PROCESS: 8/8 phases PASS   LAWS: 6/6 PASS (Law 6 pending Phase 7)   SCOPE: PASS
DETERMINISTIC CITATION AUDIT: PASS (exit 0) — 0 HARD-FAIL, 4 WARN (formatting only)
QUOTE LOCKS (re-run): 104 accepted / 0 rejected
RESEARCH MAP GATE: CLEARED
DECISION: [x] DO NOT deliver yet — FIX list F1–F12 (no BLOCK; no fabricated citation; gate cleared)
```

## Part A — Process
- **Phase-0 scope confirm — PASS.** `00_scope.md`: purpose "Đúng, giữ nguyên"; audience "Đúng, giữ nguyên"; length "Đúng, giữ nguyên"; language "Tiếng Việt (Recommended)"; effort "normal (Recommended)"; databases "Không".
- **Protocol — PASS.** `01_protocol.md`: PICO, inclusion/exclusion, concept blocks + 6 PubMed queries, pre-registered outcomes/subgroups, change log (supplementary search; M02/M13/M17 dropped).
- **Retrieval — PASS.** PubMed + Consensus + CT.gov + medRxiv (partial) ; Elicit/Europe PMC/OpenAlex/Semantic Scholar failed and are recorded; curiosity probes run; `source/` folder checked and user asked (`02a`). Machine-fetched NCBI text placed in `source/` with `_PROVENANCE.md` after user's Gate 4b choice "Giữ ở source/ kèm nhãn (Recommended)".
- **Gate 2b — PASS.** `02a_search_log.md`: user's verbatim approval **"Duyệt, tiếp tục"**, asked alone after content decisions.
- **Research Map HARD GATE — CLEARED.** `03a_gate_approval.md`: content decisions "Đồng ý đề xuất (Recommended)", "Tìm bổ sung ngắn (Recommended)", "Nhận cả 3 (Recommended)", "Giữ cả 6, cân bằng (Recommended)"; gate-closing question asked alone; user's approval verbatim **"Duyệt, tiếp tục"**; unconditional. Git order confirms the receipt precedes all downstream work: gate commit 54b04d4 (04:20) < appraisal dcd98cd (04:37) < draft 8a0baf2 (04:55). Verifier limit: the quoted approval is lead-recorded on disk; I cannot see the chat transcript, so I rely on the receipt and its commit order.
- **Appraisal — PASS.** Assumption Register AR-1…AR-16; ROBIS-lite / NOS / ROBINS-I + GRADE per outcome; 104 quote-locked cards; contradictions C1–C10 with steelmen; do-not-cite list (H02, H03, M02, M13, M17) honoured. **Gate 4b — PASS:** §13 verbatim **"Duyệt, tiếp tục"**.
- **Synthesis — PASS with FIX.** Grouped by sub-theme; consensus vs controversy labelled; every pre-registered subgroup has a locatable place (eGFR strata §3.4.1; age ≥65 §3.4.2; HF §3.4.3; hepatic §3.4.4; ASCVD via §3.5 clause; monotherapy vs combination §3.2; IR vs XR §3.3) — L-038 satisfied, ASCVD is the thinnest (clause, not heading; evidence absent for metformin, stated). Language calibration: see F3/F4/F11.
- **Coach — PASS (SKIPPED, declared).** `05a_coach.md`: "SKIPPED — effort=normal; writer self-check done"; effort tag matches `00_scope.md`; not a silent omission.
- **Draft — PASS.** Full structure; 33/33 approved sources cited; every claim cited from the store.
- **Manifest — pre-QA version present** (`06c_manifest.md`); verdict row to be filled by lead after FIX.

## Part B — Laws
- **Law 1 — PASS.** 33/33 references real and identical to PubMed records; NCT02915198 real; no fabricated PMID/DOI/NCT/author/year; F1/F2/F7 are misreads of real numbers, not fabrications.
- **Law 2 — PASS.** Purpose, audience, window, language match scope; length reduced only by the user's explicit choice "Rút còn ~1800–2000 từ (Recommended)" (recorded in `00_scope.md` amendment).
- **Law 3 — PASS.** SR/MA > guideline > RCT-derived > cohort ordering; conflicts stated (RCT vs observational; Silverii vs others) — see F5 for one dropped conflict datum.
- **Law 4 — PASS.** "4.1 Đồng thuận đã xác lập" and "4.2 Tranh cãi đang diễn ra" present.
- **Law 5 — PASS with FIX.** "4.3 Hạn chế của tổng quan này" covers databases, terms-scope, language, bias, unanswered questions; F9(b) adds two omitted coverage limits.
- **Law 6 — PENDING.** Evolution-log entry and lesson proposals belong to Phase 7 (lessons-curator); candidate lessons listed above.

## Part C — Scope integrity: PASS
Right topic (metformin efficacy/safety, adult T2D), right audience (internists), 2015–2026, Vietnamese, ~1,967 tokens per the user-chosen amendment, no unrequested additions or silent removals. Dropped detail (writer notes §0) changed no conclusion except the F5 omission.

## Violations
None of the Supreme-rule type. Process receipts present for every claimed step (R4 clear). One reader-facing process overclaim (F6). Briefed-inspector risk (R5): I did not use `05b_writer_notes.md` for any truth claim; all verdicts rest on the draft, store, cards and NCBI XML.

## Self-update proposals
Evolution-log entry (regression Case 1, EASY): rubric 0.785 MET pre-FIX; first-pass QA found 5 substantive misreads that all 104/104 green locks could not see (stratum/endpoint mismatch, null-as-absence, dropped contradicting datum after length cut). Lessons: see §F. No constitution change proposed.

## Next step
Writer applies F1–F12 (net words ≤ 0); verifier re-runs: `citation_audit.py` on the revised file, quick re-check of F1–F5 against the cards, then produces `06_final_review.md` (clean, no internal notes) and refreshes `06b_citation_audit.md` against it.
