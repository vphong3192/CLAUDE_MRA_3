# 05b — Writer notes for `05_draft_review.md` (Phase 5, length revision)

> Internal notes for the lead and the citation-verifier. Not part of the deliverable.
> They used to be the draft's "Phụ lục nội bộ" (Appendices A–D) and were moved out at the length revision.
> Re-run on the **shortened** draft, 2026-10-27.

## 0. Length revision: what was done

- **User decision** (`00_scope.md`, "Amendment — length", verbatim): "Rút còn ~1800–2000 từ (Recommended)".
- **Main-text count:** **1,996** whitespace tokens. Counted by script from the `# ` title line down to, but not including, the `## 6. Bảng tóm tắt kết quả` heading. Without the title and subtitle lines it is 1,973. The first draft (8a0baf2), counted the same way, had 4,158 tokens; the "~4,700" figure in the scope amendment counted more of the file.
  Script: `/tmp/claude-0/-home-user-CLAUDE-MRA-3/ceb9658b-7fe5-5852-b670-3ed1cc5309d0/scratchpad/count_main.py` (it counts `len(line.split())` per line, so Vietnamese syllables, `[n]` citations and GRADE tags all count as tokens).
- **References:** 33. Every approved record is still cited, so none was removed. They are renumbered by first appearance, and the SoF table counts too because it comes before the list. `citation_audit.py` gives **PASS**: 0 HARD-FAIL, 33/33 cited, 85% coverage. It also gives 4 WARNs, all `number_not_in_source`, all from separator formatting only. "1.000" corresponds to "1,000 mg" in quote-locked card MET-M12-c1, and "44,2" to "44.2%" in MET-H12-c5.
- **Sections merged or cut:**
  - Old §4.3 "Khoảng trống bằng chứng" is now the last bullet of the limitations section, "Còn bỏ ngỏ" (§4.3).
  - Old controversy (4), "phối hợp có hại" (C3), is now one sentence in §3.2.
  - Old §5 "Kết luận" and the 7-item "Thông điệp thực hành" are now §5, with one paragraph and 3 items. The heart–kidney message moved into the paragraph. The glycaemia, older-adult and HF items were cut because §3.1, §3.4.2 and §3.4.3 already say them.
  - Methods went from 3 paragraphs to 3 sentences.
  - Background went from 5 sentences to 2.
  - The abstract's bulleted findings became one paragraph.
- **Secondary numbers moved to the SoF table, so they are still in the document:**
  - glycaemia: SMDs; hypoglycaemia ORs (SU, basal insulin, severe with SU)
  - mortality: RR 0.98 (Li), OR 0.84 (Shi), the NMA sizes (301 and 816 RCTs); Cochrane 31/1454 vs 31/1441; observational OR 0.44; "combination harm" RR 1.49 with the UKPDS weight
  - MACE components: CIs for stroke and CV death; HF hospitalisation RR 1.02
  - GI: incidence 6.9% in observational data; discontinuation RR 1.080 and RR 2.19
  - B12: OR 4.10, PPI aHR 1.18, 17/21 studies
  - acidosis: eGFR 30–44 aHR 1.09; Patiño-Cardona HR 1.93
  - CKD: RR 1.00, Clegg HR 0.91, Hu RR 0.71, Charytan HR 0.49; Lalau doses 1,500/1,000/500 mg (new SoF row, GRADE Very low per `04_appraisal.md` §3, "Dose regimen by CKD stage"); Lambourg MACE HR 1.05
  - cirrhosis: decompensation aHR 1.15 and the >1000 mg aHR 1.42
  - Two SoF rows were added: "Ngừng thuốc do biến cố bất lợi" and "Tử vong trong dữ liệu quan sát" (CKD). Their contents were in the first draft's text, and their GRADE labels are taken from `04_appraisal.md` §3.
- **Dropped from the document entirely.** None of these is a Law-4/Law-5 item and none changes a conclusion:
  1. Silverii's certainty discrepancy (abstract "low" vs main text "low to high"). The draft keeps [GRADE: thấp], and the MACE value discrepancy (0.68 vs 0.69) is kept.
  2. Silverii's direct-vs-indirect inconsistency for metformin vs SGLT2i (MET-H10-c6).
  3. Lambourg's 3-year survival percentages (63.4% vs 70.3%). The main-text HR and the abstract HR are kept.
  4. Cần Thơ detail: insulin monotherapy as the dominant regimen and eGFR not reported. MET-M19 is still cited, for "dữ liệu Việt Nam chỉ về… kê đơn".
  5. NICE's position "as reported by Lambourg" as a separate clause. It is now covered by the limitations clause "NICE, FDA chỉ qua nguồn thứ cấp".
  6. "Three supplementary queries" for older adults, and "RCT participants mostly young/white" (MET-H04).
  7. The Background's three-question framing and the practice item on holding the drug during acute illness, which was labelled inference.
  8. The ADA/EASD 2026 heart-failure practice item. The 2026 recommendation is still stated in §3.5.
  9. The meta-regression and observational XR detail. Both are still cited ([3,16]), and the detail is in the SoF.
  10. The "đa số eGFR >30" qualifier for the PCI meta-analysis.
- **No new claim, number or source was added.** Every number in the draft comes from the first draft (8a0baf2), which was built from accepted cards in `04c_quote_locks.md` (104/104 accepted). One change to the steelman wording in 4.2(1): it now says "mọi ước tính điểm từ RCT **cho tử vong và nhồi máu**", which restores the qualifier from the first draft. Stroke does not favour metformin.

## 1. PICO × outcome coverage matrix (L-038), re-run on the shortened draft

| Pre-registered subgroup / outcome (`01_protocol.md`) | Labelled location in the draft | Evidence status |
|---|---|---|
| O: HbA1c (A1) | §3.1; SoF | Present, Moderate |
| O: glycaemic durability (A1) | §3.1, last sentence; SoF | Very low |
| O: MACE / CV death (A2) | §4.2 (1), MACE broken into components (L-010); SoF "MACE" and "Thành phần MACE" | Low |
| O: all-cause mortality (A2) | §3.2; SoF | Low |
| O: weight (A3) | §3.1 | Moderate |
| O: hypoglycaemia (A3/A4) | §3.1; SoF | Moderate |
| O: GI events / discontinuation (A4) | §3.3 "Tiêu hoá"; SoF (2 rows) | Moderate / Low |
| O: lactic acidosis (A4) | §3.3 "Nhiễm toan lactic"; §3.4.1 eGFR strata; §4.2 (2) | Low (≥30) / Very low (<30) |
| O: B12 / neuropathy (A4) | §3.3 "Vitamin B12"; §4.3 "Còn bỏ ngỏ" | B12 Low; **neuropathy: no source in the approved set**, stated as a gap |
| O: heart-failure outcomes (A2/A5) | §3.4.3; SoF "Nhập viện do suy tim" | Very low / Absent |
| O: cancer, dementia (observational, flagged) | §4.3 "Còn bỏ ngỏ" ("ung thư, sa sút trí tuệ nằm ngoài bộ nguồn") | Not in the approved set; no result sentence written |
| P: CKD eGFR ≥45 | §3.4.1 "*eGFR ≥45:*" | Present |
| P: CKD eGFR 30–44 | §3.4.1 "*eGFR 30–44:*" | Present |
| P: CKD eGFR <30 | §3.4.1 "*eGFR <30:*"; §4.2 (2) | Present, contested |
| P: age ≥65 | §3.4.2 (own heading) | **No direct evidence**, stated with the verbatim Law-1 sentence |
| P: with/without ASCVD | §3.5 (CV-risk sentence plus "metformin không có dữ liệu riêng theo nguy cơ tim mạch"); §5 | Data for newer agents; none specific to metformin |
| P: heart failure | §3.4.3 (own heading) | **No direct evidence**, stated with the verbatim Law-1 sentence |
| P: hepatic impairment | §3.4.4 | Very low (one cohort) |
| I: monotherapy vs combination | §3.2 ("phối hợp có hại" sentence); SoF | Very low |
| I: IR vs XR | §3.3 "Tiêu hoá"; SoF | Low |
| C: vs SU | §3.1; §3.2 ("So với SU"); SoF | Moderate / Low |
| C: first-line SGLT2i/GLP-1 RA instead of metformin (A6) | §3.5, last sentence; §4.2 (3); SoF | Very low |
| A6: guideline position | §3.5 | ADA/KDIGO 2022 in full text; ADA/EASD 2026 abstract only; ADA 2026 and KDIGO 2022 unreadable (§4.3) |
| Local (Vietnam) | §3.3 B12; §4.3 "Còn bỏ ngỏ" | B12 and prescribing only |

**Result:** every pre-registered subgroup still has a labelled place. The first draft gave Vietnamese prescribing a labelled sub-paragraph in §3.4.1. It now survives only as a limitation, which is acceptable because it carries no efficacy or safety outcome. Nothing in scope fell below the labelled-section threshold.

## 2. Six-angle self-check (replaces quality-coach at effort `normal`), re-run

| Angle | Outcome | Fixed during the revision |
|---|---|---|
| Clarity | Each axis paragraph opens with the conclusion and its GRADE tag; numbers follow. | — |
| Depth | Still a synthesis, not a list. The draft explains why sources disagree: UKPDS dominance, confounding by indication, active comparators (GI discontinuation), and Lambourg's prevalent users and SU co-use. The steelman for each of C1/C2, C5 and C10 is kept. | The C3 explanation was folded into §3.2 so it was not lost when the section was cut. |
| Completeness | 33/33 approved sources are cited (16 HIGH, 17 MEDIUM). The L-038 matrix is complete (§1 above). Law-4 labels are present: "Đồng thuận đã xác lập" and "Tranh cãi đang diễn ra". The Law-5 section "Hạn chế của tổng quan này" keeps all six limitation areas plus the unanswered questions. | The cancer/dementia gap was restored to §4.3 after the first cut lost it. A no-data statement for metformin by ASCVD stratum was restored to §3.5. |
| Framing | The abstract and §5 lead with the clinical bottom line for internists: use metformin for glycaemia, rely on SGLT2i/GLP-1 RA for organ protection, and dose by eGFR. | The three-question Background framing was cut for length. The title and abstract carry the purpose. |
| Honesty | No Low or Very-low finding is stated as fact. Observational findings use associative verbs (L-002). The main-text values for Silverii and Lambourg are given, with the abstract discrepancy named for each (L-005). "Chưa xác định được" is used for the 2026 guideline position. No preprint is cited. | §3.4.1: the first cut implied MET-M15 (Clegg) was a placebo comparison. It was reworded to "hậu kiểm hai thử nghiệm". §3.2: RR 0.96 had been attached to three citations. The numbers were moved to the SoF and the sentence now says "trong ba phân tích gộp". The 4.2(1) steelman qualifier "cho tử vong và nhồi máu" was restored. |
| Insight | So what: metformin's value is glycaemic, and its CV benefit is unproven and, if real, not carried by stroke or CV death. The eGFR <30 question is a real equipoise, but the review does not recommend continuing. | — |
| Fluency (L-037) | Calque blacklist scanned: none of "câu chuyện", "tạo tác", "biểu kiến", "sống sót qua", "neo", "gộp ngây thơ". A script check found two sentences over 40 syllable-tokens: the abstract Background (41) and the "Còn bỏ ngỏ" bullet (43). Both are lists split by commas and semicolons, so they were left as they are. Native connectors are used (vì vậy, nhưng, còn, trong khi). | "Steelman" is glossed once as "Phản biện mạnh nhất (steelman)"; later uses say "Phản biện cho…". |
| Reconciliation (L-016) | The build script numbers citations from the placeholders and emits the list. Inline numbers and list entries match one to one (audit: 33 entries, 33 distinct inline). | — |
| Abstract vs body GRADE (L-029) | The abstract tags (moderate, low, low/very low, high) match §3, §4.1 and the SoF. | — |

## 3. Provisional Vietnamese terms (not in `vi-terminology.md`; user to confirm)

| English | Vietnamese used (provisional) |
|---|---|
| Target trial emulation | mô phỏng thử nghiệm mục tiêu |
| Cardiovascular outcomes trial (CVOT) | thử nghiệm kết cục tim mạch (the acronym is no longer used in the text) |
| Confounding by indication | nhiễu theo chỉ định (first draft: "nhiễu do chỉ định"; changed to avoid "do… do") |
| Adjusted hazard ratio (aHR) | used as "aHR" only; the shortened text does not spell it out |
| Network meta-analysis | phân tích gộp mạng lưới |
| Immediate / extended release | phóng thích tức thời / phóng thích kéo dài (XR) |
| Lactic acidosis | nhiễm toan lactic |
| Compensated / decompensated cirrhosis | xơ gan còn bù / mất bù |
| Marginal structural model | mô hình cấu trúc biên |
| Post hoc analysis | hậu kiểm |
| Steelman | phản biện mạnh nhất (steelman) |
| Network node | nút (metformin của Silverii) |

The terminology guide renders "Limitations" as "Giới hạn". The draft keeps "Hạn chế của tổng quan này", as the lead asked for this run.

## 4. Notes for the citation-verifier and the lead

1. **Store corrections made in this phase.** All are logged at the end of `reference/metformin-t2d.md` under "Phase 5 corrections", and the source for each is the on-disk NCBI PubMed XML.
   - **MET-M14:** full title restored ("…a cross-sectional study in a South Vietnam tertiary hospital.").
   - **MET-H02:** authors changed to the collective author "American Diabetes Association Professional Practice Committee for Diabetes", and the entry heading renamed. The upstream phase artifacts still say "Bajaj"; they were not edited.
   - **MET-M01:** the verified finding now states both counts with their denominators: 296 add-on-to-metformin trials, and 298 low-CV-risk trials on metformin background. The draft uses neither count.
   - **Not changed (reported in the first draft, not requested now):** MET-H12 and MET-S02 issue year vs online year. The reference list already gives the issue year and notes the online year.
2. **A sentence based on the search log, not on a cited reference:** "NCT02915198 chỉ ở tiền đái tháo đường" (§4.3 "Còn bỏ ngỏ"). It comes from `02a_search_log.md` and the store's "Context-only registry records". The NCT number is written inline and is not a numbered reference, because the record is not one of the 33 approved sources. The registry entry gives primary completion as 2029-09-28; the first draft gave this date and the shortened text dropped it.
3. **Sources cited only to record that their content could not be read:** MET-H02 [31] and MET-H03 [32], in §4.3 "Hướng dẫn" (per `04_appraisal.md` §7).
4. **Sentences labelled as inference:** all of §3.4.2 and §3.4.3, and the cost clause in §4.2 (3).
5. **Audit WARNs:** 4, all separator formatting, listed in §0.
6. **Process:** the draft was built from a placeholder source (`{MET-id}` tags), and a script renumbered the citations and copied each reference entry verbatim from the first draft's verified list.
   - Source: `/tmp/claude-0/-home-user-CLAUDE-MRA-3/ceb9658b-7fe5-5852-b670-3ed1cc5309d0/scratchpad/draft_src.md`
   - Script: `/tmp/claude-0/-home-user-CLAUDE-MRA-3/ceb9658b-7fe5-5852-b670-3ed1cc5309d0/scratchpad/build.py`
   - The reference list's MET-M14 and MET-H02 entries already matched the PubMed XML before the store was corrected.

## Phase 6 fixes (round 1)

Source: `06a_verification_report.md` §B (verdict FIX). Main text is now **1,996** tokens (title to SoF, same script), so there is no net increase. `citation_audit.py` gives **PASS**: 0 HARD-FAIL, 33/33 cited, 3 WARNs, all separator formatting ("1.000", "44,2").

- **F1 — applied.** §3.3 no longer gives aHR 0.98 as an eGFR ≥30 value. The stratum values (45–59: 1.16; 30–44: 1.09) are now in the §3.4.1 bullets. The SoF row labels 0.98 as "toàn đoàn hệ (mọi mức eGFR)".
- **F2 — applied.** §3.2 now says AHRQ found CV mortality lower and Cochrane found all-cause mortality similar, with [GRADE: thấp]. "Không nhất quán" was removed. In the SoF the Cochrane figure is labelled "tử vong chung (hai kết cục khác nhau)". I left out the words "chưa đủ kết luận" for length; the Low GRADE tag carries that meaning.
- **F3 — applied.** "Chỉ" was removed. Discontinuation does not increase against pooled controls [3], but increases against placebo in CKD, which includes polycystic kidney disease [14].
- **F4 — applied (a–d).**
  - (a) The conclusion now says "ước tính điểm chỉ nghiêng về nhồi máu, không về đột quỵ hay tử vong tim mạch".
  - (b) The steelman now reads "đơn trị so với đối chứng cho tử vong chung và nhồi máu", cited [4,5,11]. The 16% figure stays [4].
  - (c) "Khoảng tin cậy của đột quỵ".
  - (d) "Thành phần MACE theo Griffin".
- **F5 — applied.**
  - Abstract: "bằng chứng chủ yếu trên nền metformin [9]".
  - §3.5: "Chưa có so sánh đối đầu ở người chưa dùng thuốc về kết cục cứng", followed by Silverii's direct comparison favouring metformin but inconsistent with the NMA [6] (card MET-H10-c6).
  - The SoF row is now cited [6]. NMA is spelled out at its first use in §3.2.
- **F6 — applied.** §2 now says "các ước tính hiệu ứng chính đã khoá…". The abstract says "Tổng quan có phương pháp (PRISMA, GRADE), đề cương lưu trước".
- **F7 — applied.** HbA1c: "cao hơn [1]; AHRQ thấy tương tự, trừ nhóm DPP-4 kém hơn [2]". Weight: "chênh lệch tới 5 kg".
- **F8 — applied.** (a) "…chưa xác định được vì chỉ đọc được tóm tắt". (b) "cân nhắc phối hợp". (c) Mortality is cited [5]; Nong [29] is cited only for "lợi ích tim–thận".
- **F9 — applied.** (a) The NCT number was moved out of the [4,12] group and is now an inline ClinicalTrials.gov hyperlink. It is not a numbered reference; adding it as ref 34 is for the lead to decide. (b) The search-limitations bullet now says Consensus gave 10 results per query and medRxiv was one page of one category (`02a_search_log.md` rows C1–C3 and M1).
- **F10 — applied.** The SoF row was split. RCT mortality RR 1.00 [14] keeps its own row. Clegg MACE HR 0.91 [23] is a new row labelled non-randomised, and its GRADE is **Rất thấp**, per `04_appraisal.md` §3 ("Mortality/CV benefit in CKD G1–3 (obs)" lists M15 as Very low). §3.4.1 text now says "so sánh không ngẫu nhiên" (advisory A3).
- **F11 — applied.** The abstract conclusion is "dùng được khi eGFR ≥30 [GRADE: thấp]". §5 is "dùng được khi eGFR ≥30 (đồng thuận ADA/KDIGO 2022; không thấy tăng nhiễm toan) [GRADE: thấp]".
- **F12 — applied now rather than left to finalisation.** I removed the "Bản nháp" subtitle, the italic reference-list header and the 33 `(MET-xx)` tags. Mapping from number to store ID: 1 M03 · 2 H07 · 3 H13 · 4 H04 · 5 H08 · 6 H10 · 7 S01 · 8 H12 · 9 M01 · 10 M18 · 11 H05 · 12 H06 · 13 M05 · 14 H14 · 15 M11 · 16 M10 · 17 M07 · 18 M09 · 19 M14 · 20 M08 · 21 S03 · 22 M12 · 23 M15 · 24 M04 · 25 M16 · 26 H11 · 27 S02 · 28 H01 · 29 H09 · 30 M06 · 31 H02 · 32 H03 · 33 M19.
- **Advisories:**
  - **A2 applied:** "phối hợp hợp lý ở bệnh thận mạn".
  - **A3 applied:** see F10.
  - **A1 not applied:** adding "(suy luận)" would have broken the token cap. The sentences already use hedged, associative wording.
  - **A4 not applied:** same reason.
  - **A5 not applied:** the COI note was optional, and it was left out for length.
- **Offsets that keep the total at or below 1,996.** Nothing was added beyond accepted cards, and no reference was dropped, so the numbering did not change.
  - Dropped from §2: the list of pre-registered subgroups. Each one keeps its labelled heading in §3.4, and the L-038 matrix is unchanged.
  - Dropped from §4.3: the clause "UKPDS chi phối bằng chứng tim mạch" (still stated in §3.2), and "thử nghiệm đối đầu ở người chưa dùng thuốc" (now stated in §3.5).
  - Dropped: "và cần RCT" in 4.2(2). The missing RCT is still listed in §4.3.
  - §5: the practice items were folded into one sentence. Dosing is now "chỉnh liều theo eGFR [22]"; the exact doses are in §3.4.1.
  - §3.5: the ASCVD statement is now "metformin thiếu dữ liệu theo nguy cơ tim mạch". It is still locatable for L-038.
