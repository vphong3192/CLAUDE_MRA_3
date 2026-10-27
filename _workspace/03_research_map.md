# 03_research_map.md — Research Map (Phase 3, HARD GATE)

**Lead-authored 2026-10-27**, from `reference/metformin-t2d.md` (33 studies) + `02_corpus.md`. Written to disk before it is shown to the user.
**Status: CLEARED — see `03a_gate_approval.md`** (user: "Duyệt, tiếp tục", 2026-10-27). Originally presented as AWAITING USER APPROVAL; no appraisal or drafting ran before that approval (L-014).

## 1. Scope recap
Hiệu quả và an toàn của metformin trong ĐTĐ týp 2 ở người lớn. Mục đích: hỗ trợ quyết định lâm sàng. Đối tượng: BS nội khoa. ~1500 từ. Nguồn 2015–nay. Viết bằng tiếng Việt. Effort `normal` (`00_scope.md`).

## 2. World picture (axes)
| Axis | Status | Landmark anchor(s) | Consensus strength (pre-appraisal) |
|---|---|---|---|
| A1 Glycaemic efficacy (HbA1c, vs other classes) | **mature** | Palmer 2016 JAMA NMA (M03); Maruthur 2016 AHRQ (H07) | Strong: HbA1c reduction ≥ other oral agents, weight-neutral/lower, low hypoglycaemia |
| A2 Cardiovascular outcomes & mortality | **contested** | Griffin 2017 (H04), Li 2021 (H05), Gnesin Cochrane 2020 (H06), Shi 2023 BMJ NMA (H08), Silverii 2026 (H10), Zhang 2020 observational (M05) | RCT data: low/very low certainty, mostly null CIs (UKPDS-dominated). Observational: large apparent benefit (confounding). Silverii 2026: MACE OR ~0.69 but low certainty. No modern T2D CVOT exists. |
| A3 Weight / hypoglycaemia | **mature** | Maruthur 2016 (H07), Palmer 2016 (M03), Shi 2023 (H08) | Strong: less hypoglycaemia than SU/insulin; weight neutral to modest loss |
| A4 Safety: GI, XR formulation, lactic acidosis, B12 | GI/B12 **mature**; lactic acidosis **emerging (low event rate, weak data)** | Nabrdalik 2022 RCT MA (H13), Nabrdalik 2024 (M10), Tan 2021 XR (M11), Atkinson 2024 B12 (M07), Jung 2025 PPI (M08) | Strong for GI (diarrhoea RR ~2.4) and dose/duration-dependent B12 deficiency; XR vs IR evidence mixed |
| A5 Special populations: CKD by eGFR | **contested** | El-Damanawi Cochrane 2024 (H14), Patiño-Cardona 2026 (H11), Lambourg 2024 TTE (H12), Hu 2020 (M04), Clegg 2021 (M15), Charytan 2019 TREAT (M16), Lalau 2018 dosing (M06), ADA/KDIGO 2022 (M12), KDIGO 2022 (H03) | Moderate: use with dose reduction in CKD 3; eGFR <30 is the live controversy (TTE: stopping associated with higher mortality) |
| A6 Place in therapy (first-line vs SGLT2i/GLP-1 RA from diagnosis) | **contested** | ADA/EASD 2026 (H01), ADA SOC 2026 (H02), Nong 2025 living NMA (H09), Tsapas 2020 (M01), Bin Hussain 2019 (M18, Level III) | Guidelines are shifting toward organ-protective agents "potentially from diagnosis" (H01 abstract); metformin's exact position in 2026 texts is NOT verifiable on disk |

## 3. Local (Vietnam) picture
- **Có:** 2 nghiên cứu cắt ngang về thiếu vitamin B12 (Huynh 2024, Vinmec, 18,6% — M09; Phan 2025, Chợ Rẫy, 22,1% — M14); 1 nghiên cứu mô tả kê đơn ở bệnh nhân suy thận tại Cần Thơ (Dang 2024 — M19).
- **Không có:** dữ liệu hiệu quả đường huyết, kết cục tim mạch hay nhiễm toan lactic ở người Việt Nam. → **Population/implementation gap.** Không bịa nghiên cứu địa phương (Law 1).

## 4. Research gaps (5 types)
| Type | Gap | Evidence why |
|---|---|---|
| Evidence | No adequately powered placebo-controlled CVOT of metformin in T2D | Griffin 2017 (H04): only 4 placebo trials with CV outcomes, n=417 on metformin; CT.gov: only VA-IMPACT (prediabetes, completes 2029) |
| Contradiction | RCT (null/uncertain) vs observational (OR 0.44–0.57) CV/mortality signals; Li 2021 "combination harm" signal vs NMAs | H04, H05, M05, H10 |
| Contradiction | eGFR <30: guidelines say stop; TTE suggests stopping is associated with higher mortality | H12 vs H03/M12 (guideline text not on disk) |
| Methodological | Metformin CV evidence rests on old, small, high-risk-of-bias trials; most modern trials use metformin only as background | H06 (no trial low RoB), H10, M01 |
| Population | Older adults (≥65) and hepatic impairment: **no dedicated record in corpus**; Asian/Vietnamese efficacy data absent | corpus coverage |
| Implementation | GI intolerance and B12 monitoring in practice; PPI co-use | H13, M10, M08, M09, M14 |

## 5. Next directions (tied to gaps)
1. Modern pragmatic CVOT of metformin vs no metformin, or factorial add-on design (→ evidence gap; Griffin's suggestion).
2. RCT of continuing vs stopping low-dose metformin at eGFR <30 (→ contradiction gap; Lambourg's suggestion).
3. Head-to-head first-line metformin vs SGLT2i/GLP-1 RA on hard outcomes in drug-naive patients (→ A6).
4. Vietnamese cohort data on efficacy/safety and B12 screening yield (→ population gap).

## 6. Source approval list (33 records) — user approves / drops / re-tiers
FT = full text read; ABS = abstract only. Type: G = guideline/consensus; SR = SR/MA/NMA; P = primary (RCT post hoc/cohort/cross-sectional/PK); III = Level III narrative.

| ID | First author, year | Type | Tier | FT? | Axis | Lead's note |
|---|---|---|---|---|---|---|
| H01 | Davies 2026 ADA/EASD | G | HIGH | **ABS ⚠** | A6 | metformin position not in abstract |
| H02 | Bajaj 2026 ADA SOC s9 | G | HIGH | **ABS ⚠** | A6 | abstract generic; no recommendation text |
| H03 | KDIGO 2022 | G | HIGH | **ABS ⚠ (no abstract at all)** | A5 | eGFR thresholds not on disk |
| H04 | Griffin 2017 | SR | HIGH | FT | A2 | |
| H05 | Li 2021 | SR | HIGH | FT | A2 | combination-harm signal (UKPDS-driven) |
| H06 | Gnesin 2020 Cochrane | SR | HIGH | **ABS ⚠** | A2 | detailed abstract with GRADE |
| H07 | Maruthur 2016 AHRQ | SR | HIGH | **ABS ⚠** | A1/A2/A3 | |
| H08 | Shi 2023 BMJ | SR | HIGH | FT | A2/A3 | |
| H09 | Nong 2025 BMJ living | SR | HIGH | **ABS ⚠** | A6 | no metformin numbers in abstract → **propose re-tier MEDIUM** |
| H10 | Silverii 2026 | SR | HIGH | FT | A2 | abstract vs text OR discrepancy |
| H11 | Patiño-Cardona 2026 | SR (obs.) | HIGH | **ABS ⚠** | A5 | |
| H12 | Lambourg 2024 | P (TTE) | HIGH | FT | A5 | |
| H13 | Nabrdalik 2022 | SR | HIGH | FT | A4 | |
| H14 | El-Damanawi 2024 Cochrane | SR | HIGH | **ABS ⚠** | A5 | mixed T2D/ADPKD population |
| M01 | Tsapas 2020 | SR | MED | ABS | A6 | |
| M02 | Qaseem 2024 ACP | G | MED | ABS | A6 | recommendations truncated in abstract → **propose drop** (nothing citable on metformin) |
| M03 | Palmer 2016 JAMA | SR | MED | ABS | A1/A3 | **propose re-tier HIGH** (main A1 anchor) |
| M04 | Hu 2020 | SR | MED | ABS | A5 | |
| M05 | Zhang 2020 | SR (obs.) | MED | ABS | A2 | |
| M06 | Lalau 2018 | P | MED | ABS | A5 | dosing by CKD stage |
| M07 | Atkinson 2024 | SR (mini) | MED | ABS | A4 | |
| M08 | Jung 2025 | P | MED | ABS | A4 | |
| M09 | Huynh 2024 (VN) | P | MED | ABS | A4/local | |
| M10 | Nabrdalik 2024 | SR (obs.) | MED | ABS | A4 | |
| M11 | Tan 2021 | SR | MED | ABS | A4 | |
| M12 | de Boer 2022 ADA/KDIGO | G | MED | ABS | A5 | metformin cut-offs not in abstract |
| M13 | Davies 2022 ADA/EASD | G | MED | ABS | A6 | superseded; historical only → **propose drop** |
| M14 | Phan 2025 (VN) | P | MED | ABS | A4/local | |
| M15 | Clegg 2021 | P (RCT post hoc) | MED | ABS | A5 | |
| M16 | Charytan 2019 TREAT | P (RCT post hoc) | MED | ABS | A5 | |
| M17 | Mohammadi 2026 | SR | MED | ABS | A2 | no metformin estimates in abstract → **propose drop** |
| M18 | Bin Hussain 2019 | III | MED | ABS | A6 | controversy framing only |
| M19 | Dang 2024 (VN) | P | MED | ABS | local | descriptive |

**HIGH abstract-only: 8/14** — full text attempted (PMC MCP returned empty bodies; WebFetch DNS-blocked); user chose at Gate 2b to proceed and flag in Limitations.
**Known coverage holes (not fixable from the current store):** no 2015+ SR quantifying lactic-acidosis incidence; no older-adult-specific record; no hepatic-impairment record; guideline recommendation text (ADA SOC/ADA-EASD/KDIGO/NICE/FDA) not on disk.

## 7. Closing questions
1. Approve the source list, with the lead's proposals (re-tier H09→MEDIUM and M03→HIGH; drop M02, M13, M17)?
2. Coverage holes (older adults, lactic acidosis, hepatic): run a short supplementary search, or proceed and declare them in Limitations?
3. Keep all six axes (A1–A6)? Any axis to emphasise?
4. Then, separately: is the Research Map gate approved?

## Research Map — user content decisions (2026-10-27, verbatim structured answers; gate NOT yet approved)
1. Source list: **"Đồng ý đề xuất (Recommended)"** → re-tier H09→MEDIUM, M03→HIGH; drop M02, M13, M17 → 30 sources.
2. Coverage holes: **"Tìm bổ sung ngắn (Recommended)"** → short supplementary PubMed search (older adults; lactic acidosis; hepatic if yield) — new records to be shown to the user before appraisal.
3. Axes: **"Giữ cả 6, cân bằng (Recommended)"** → A1–A6 balanced; controversy concentrated on A2/A5/A6.
Gate-closing approval: pending — to be asked alone after the supplement (L-044/L-024).

## Supplementary search result (commit d11e9aa) and user decision
Added: MET-S01 Lazarus 2018 (cohort, acidosis by eGFR; HIGH; ABS), MET-S02 Yen 2021 (Taiwan cirrhosis cohort; HIGH; FT), MET-S03 Sakellariou 2023 (SR/MA peri-PCI; MEDIUM; ABS). Older adults: no metformin-specific T2D record found (3 queries) → evidence gap → Limitations. Prefilter not re-run after hand-appending the new candidates (disclose in Methods).
User decision (verbatim): **"Nhận cả 3 (Recommended)"**.

### Final approved-for-appraisal source list (pending gate approval): 33 sources
HIGH (16): H01, H02, H03, H04, H05, H06, H07, H08, H10, H11, H12, H13, H14, M03, S01, S02 (H09 moved to MEDIUM)
MEDIUM (17): H09, M01, M04, M05, M06, M07, M08, M09, M10, M11, M12, M14, M15, M16, M18, M19, S03
Dropped (kept in store, not for citation): M02, M13, M17.
HIGH abstract-only 9/16: H01, H02, H03, H06, H07, H11, H14, M03, S01.
