# Phase 4 — Thẩm định bằng chứng (Critical Appraisal)

**Chủ đề:** Đặc điểm điện học, điện sinh lý nhĩ trái ở bệnh nhân rung nhĩ cao tuổi
**Ngày:** 2026-06-30 · **Effort:** full (Chuyên sâu) · **Người thực hiện:** critical-appraiser
**Đầu vào:** `_workspace/02_corpus.md` (72 bản ghi citable), `reference/la-electrophysiology-elderly-af.md`, `_workspace/03b_numbers.md` (số liệu verbatim, P2)
**Cổng đã qua:** Phase 3 Research Map — phê duyệt "ok" (`research_map_gate_approval.md`)
**Chuẩn bị cho:** Gate 4b (GRADE + contradictions + assumptions)

> **Nguyên tắc số liệu (Law 1):** Mọi giá trị định lượng trong bảng dưới đây được LOAD từ `03b_numbers.md`
> (bucket verbatim) hoặc đọc trực tiếp các giá trị mean±SD/ms/cm·s⁻¹ từ kho tham chiếu (các giá trị này
> không nằm trong bucket regex). Bucket rỗng = "không báo cáo". Không có số liệu nào được tự tay chế ra.

---

## 0. Tóm tắt điều hành (cho Gate 4b)

- **Phân bố GRADE:** trên 11 nhóm outcome/thông số chính — **0 High · 3 Moderate · 5 Low · 3 Very Low.**
  Không có outcome nào đạt High vì nền tảng bằng chứng là quan sát/cắt ngang, ngoại suy theo tuổi, hoặc
  bị hạ cấp vì gián tiếp (đo trong nhịp xoang/không-RN). Các nhóm Moderate đều là tham số ECG bề mặt có
  meta-analysis lớn (PWD, IAB, P-axis).
- **RoB tổng quan:** đa số corpus là nghiên cứu quan sát (Newcastle-Ottawa) với RoB **Moderate**; chỉ 3
  RCT thật (REF-010 STAR AF II, REF-012 DECAAF II, REF-073 Haïssaguerre — và REF-018 là phân tích dưới
  nhóm RCT). Các meta-analysis (ROBINS-I/AMSTAR-style) phần lớn tổng hợp dữ liệu quan sát → trần chất
  lượng bị giới hạn bởi đầu vào.
- **Mâu thuẫn/gap nổi bật nhất:**
  1. **AFCL (G-2) — GAP THỰC SỰ chưa giải quyết:** không có MỘT bản ghi nào cung cấp AFCL phân tầng theo
     tuổi. REF-073 chỉ cho baseline chung (186±19ms, tuổi TB 53). REF-074 KHÔNG phải AFCL (nhịp xoang).
  2. **Nghịch lý AERP theo tuổi (G-1/G-9):** rút ngắn do nhịp nhanh (REF-044/045) vs kéo dài do lão hóa
     cấu trúc (REF-042/043). Đây là tranh luận thật trong y văn (REF-048), không phải lỗi tìm kiếm.
  3. **Rotor/CFAE (Axis 3):** CONFIRM dương tính (REF-005) vs STAR AF II âm tính (REF-010) — giải quyết
     được bằng chất lượng nghiên cứu (RCT đa trung tâm > thử nghiệm đơn trung tâm nhãn mở).
  4. **CABANA ≥75y:** lợi ích cắt đốt biến mất/đảo chiều ở ≥75y cho outcome cứng (aHR tử vong 1.92) dù
     giảm tái phát RN nhất quán mọi lứa tuổi — nghịch lý hiệu lực-vs-an toàn theo tuổi.
- **File đã ghi:** `/home/user/CLAUDE_MRA_3/_workspace/04_appraisal.md`.

---

## 1. Phân loại theo bậc bằng chứng (đã rà soát lại §Evidence Hierarchy của 02_corpus.md)

Sau khi rà soát, tôi tinh chỉnh bảng phân bố trong `02_corpus.md` (vốn có một vài ô đếm trùng/chưa chuẩn):

| Bậc bằng chứng | Số bản ghi citable | Bản ghi |
|---|---|---|
| Meta-analysis / SR | 12 | REF-013, 014, 015, 016, 017, 032, 039, 040, 058, 062, 070 (+REF-070) — *lưu ý: phần lớn tổng hợp dữ liệu quan sát* |
| Hướng dẫn / đồng thuận chuyên gia | 5 | REF-029, 030, 031, 064, (+ REF-038/065 là review-consensus) |
| RCT đa trung tâm (>200) | 2 | REF-010 (STAR AF II, N=589), REF-012 (DECAAF II, N=843) |
| RCT nhỏ (<100) | 1 | REF-073 (Haïssaguerre 2004, N=70) |
| Phân tích dưới nhóm của RCT | 1 | REF-018 (CABANA age subgroup, N=2,204) |
| Cohort tiến cứu / registry | 9 | REF-011, 019, 020, 037, 043, 066, 068, 069 + REF-025 (CHS), REF-024 (ARIC) |
| Cắt ngang / case-control / EP-mapping | ~20 | REF-001, 002, 003, 022, 023, 026, 027, 033, 034, 035, 041, 042, 047, 049, 051, 052, 053, 054, 055, 059, 061, 067, 074 |
| Review / narrative | ~11 | REF-004*, 007, 008, 036, 038, 048, 056, 057, 060, 063, 065 |
| Animal / ex-vivo | 2 | REF-004, 006 |
| Preprint | 0 | — |
| Trial registry | 0 | ClinicalTrials.gov MCP không khả dụng |

\* REF-004 là động vật, không phải review — đã sửa nhãn so với 02_corpus.md (vốn đếm REF-004 cả ở dòng review và animal).

**Nhận định bậc bằng chứng:** Corpus là một **kho mô tả/tiên lượng**, KHÔNG phải kho can thiệp. Phần lớn
"bằng chứng mạnh nhất" (meta-analysis) thực ra tổng hợp các nghiên cứu quan sát → khi áp GRADE, điểm xuất
phát của các MA này KHÔNG phải High mà là Low (đầu vào quan sát), trừ khi MA tổng hợp RCT. Đây là điểm
mấu chốt để writer không over-state.

---

## 2. Bảng evidence-table (one-row-per-study, số liệu LOAD từ 03b_numbers.md)

> Cột "Hiệu ứng chính" ghi giá trị verbatim. RoB tool = công cụ áp dụng theo thiết kế.

### 2.1 Thông số EP xâm lấn — AERP, SNRT, CV, AFCL (Axis 8)

| REF | Thiết kế | N | Quần thể | Hiệu ứng/giá trị chính (verbatim) | RoB tool · phán định | Ghi chú |
|---|---|---|---|---|---|---|
| REF-041 Michelucci 1984 | EP xâm lấn cắt ngang | 17 (9<40y, 8≥40y) | Người bình thường 17–78y, không RN | Phân tán AERP tương quan tuổi r=0.75 (p<0.001); SNRT tăng theo tuổi | NOS · **High RoB** (n cực nhỏ, không nhóm RN) | Dữ liệu lão hóa-EP xâm lấn sớm nhất; nền móng G-9 |
| REF-042 Kistler 2004 | EP xâm lấn + CARTO, cắt ngang | 41 (15/13/13) | 3 nhóm tuổi ≤30/31–59/≥60y, không bệnh tim cấu trúc, không RN | AERP↑ theo tuổi (r=0.56 @600ms, p<0.01); PWD 103.5±1.9 (≥60y) vs 91.4±2.9ms (≤30y); voltage lưỡng cực 1.9±0.1 (≥60y) vs 3.0±0.3mV; cSNRTmax↑ theo tuổi; CV giảm | NOS · **Moderate RoB** (cắt ngang, n nhỏ/nhóm, không nhóm RN, đơn trung tâm) | **Landmark** — nguồn age-stratified xâm lấn tốt nhất hiện có; ≥60y n chỉ 13 |
| REF-043 Lee 2016 | Cohort hồi cứu + EP nền, theo dõi 12y | 1,308 | BN làm EP (SVT), không RN nền | AERP nền 234±31ms; AERP≥280ms → aHR 2.08 (95%CI 1.03–4.21, p=0.041) cho RN mới; tuổi aHR 1.40/10y | NOS · **Moderate RoB** (hồi cứu, quần thể SVT không đại diện, biến cố thấp 3.9%) | Bằng chứng dọc duy nhất AERP→RN; CI rộng |
| REF-044 Yu 1998 | EP xâm lấn, protocol kiểu-RCT | không rõ (abstract) | BN PAF | Nhịp nhanh → rút ngắn AERP (rate-dependent) | RoB 2 (không đủ thông tin) · **Some concerns/abstract** | Cơ chế remodeling điện — chiều "rút ngắn" của nghịch lý |
| REF-045 Yu 1999 | Tiến cứu, EP nối tiếp sau sốc điện | không rõ | RN dai dẳng sau chuyển nhịp | AERP hồi phục trong ~1 tháng (đảo ngược remodeling) | NOS · **High RoB** (abstract, n nhỏ, đơn TT) | Xác nhận AERP ngắn trong RN là có được/đảo ngược |
| REF-047 Raitt 2004 | Tiến cứu, EP nối tiếp | không rõ | RN dai dẳng chuyển nhịp | cSNRT 606ms (trong RN) → 408ms (1 tháng sau) | NOS · **High RoB** (abstract, n nhỏ, không phân tầng tuổi) | Giá trị tham chiếu cSNRT chính cho G-3 |
| REF-049 Hocini 2003 | Tiến cứu, EP trước/sau PVI | 12 | PAF + khoảng ngừng xoang kéo dài | cSNRT bình thường hóa 11/12 sau PVI | NOS · **High RoB** (n=12, chọn lọc cao) | Rối loạn nút xoang trong RN có thể đảo ngược |
| REF-051 Ye 2024 | Mapping thượng tâm mạc trong mổ, cắt ngang | 319 | BN mổ tim (nhịp xoang) | CV tại vị trí phân mảnh điện thế thấp 46.0 cm/s vs 64.5 (không phân mảnh), P<0.001; ngưỡng chậm <50cm/s | NOS · **Moderate RoB** (cắt ngang, quần thể phẫu thuật, không tuổi) | Giá trị CV verbatim cho G-4; KHÔNG phân tầng tuổi |
| REF-052 Vickneson 2025 | CTA + mapping điện giải phẫu, cắt ngang | 37 chứng + 44 RN | BN RN vs chứng | RN: voltage 1.75±1.72 vs 2.11±2.02mV (P<0.001); CV 0.627±0.55 vs 0.683±0.48 m/s (P<0.001) | NOS · **Moderate RoB** (cắt ngang, đơn chương trình) | Giá trị CV/voltage verbatim; cơ chế mỡ quanh nhĩ (gián tiếp với tuổi) |
| **REF-073 Haïssaguerre 2004** | **RCT nhỏ (PVI vs PVI+đường mitral)** | **70** | **RN kháng thuốc, tuổi TB 53±8 / 53±9 — KHÔNG phân tầng tuổi** | **AFCL nền (CS) 186±19ms; PVI kéo dài AFCL → 214±24ms (kết thúc RN) vs 194±19ms (RN tồn tại); Δ lớn hơn dự báo không-tạo-được-RN** | **RoB 2 · Some concerns** (n nhỏ, đơn TT, endpoint thay thế) | **G-2: chỉ baseline AFCL CHUNG; KHÔNG giải gap tuổi** |
| **REF-074 Kojodjojo 2006** | EP điện giải phẫu (CARTO), tiến cứu | 23 (RA), 15 (LA) | 17–75y (TB 47), tim bình thường, **không tiền sử RN — nhịp xoang** | **WPV nghịch biến mạnh với tuổi: RA r=−0.77 (P<0.0001), LA r=−0.79 (P<0.001); ERP↑ theo tuổi chỉ ở vách (r=0.53); bước sóng LA r=−0.56; PWD↔tuổi r=0.42 nhưng KHÔNG↔WPV** | NOS · **Moderate RoB** (n nhỏ, quần thể đường phụ/ngất, cắt ngang) | **CV phân tầng tuổi xâm lấn TỐT NHẤT trong kho — NHƯNG nhịp xoang, KHÔNG phải AFCL → KHÔNG lấp G-2** |

### 2.2 Voltage nhĩ trái / LVZ / strain (Axis 1, 6)

| REF | Thiết kế | N | Quần thể | Hiệu ứng chính (verbatim) | RoB tool · phán định | Ghi chú |
|---|---|---|---|---|---|---|
| REF-001 Marzak 2024 | Cohort hồi cứu, ghép điểm xu hướng | 353 (286<75y/67≥75y) | RN dai dẳng cắt đốt ≥75y | Voltage 1.5 [1.2–2.3] (≥75y) vs 2.4 [1.7–2.8]mV (P<.01); LVZ 67% vs 30%; sống không-RN 36mo 68.1% vs 69.7% (P=.507) | NOS · **Moderate RoB** (hồi cứu; nhưng có ghép điểm) | Bằng chứng voltage trực tiếp ≥75y mạnh nhất |
| REF-002 Lin K-b 2021 | Lâm sàng cắt ngang + động vật | 132 chứng + 117 RN | Phân tầng <65/65–79/≥80y | Voltage RN ≥80y 1.0±0.4mV vs <65y 1.9±0.4; GLAS↓ theo tuổi (AF r=−0.807); voltage~tuổi β=−0.04 (p<0.001) | NOS · **Moderate RoB** (cắt ngang; thành phần động vật riêng) | Tham chiếu voltage phân tầng tuổi rất hữu ích |
| REF-003 van der Does 2021 | Mapping thượng tâm mạc trong mổ, cắt ngang | 216 | **Không RN** (CABG), 36–83y | CV hai nhĩ 86.9 [81.8–91.8]cm/s; CV thấp nhất↓ tuổi (coef−.210,p=.002); block↑ tuổi; voltage↓ tuổi mạnh nhất ở RA/BB | NOS · **Moderate RoB** (cắt ngang; nhưng nền không-RN quý) | Neo "lão hóa-không-RN" cho Axis 2 |
| REF-013 Boehmer 2024 | SR/MA (19 NC, 108,419) | 6,575 ≥75y | <75 vs ≥75y cắt đốt | Tái phát RR 1.24 (1.09–1.42); an toàn RR 1.64 (1.53–1.76); **voltage: KHÔNG báo cáo** | AMSTAR/ROBINS-I (đầu vào QS) · **Moderate** | Outcome lâm sàng, không phải EP substrate |
| REF-022 Lin C-H 2021 | Cohort hồi cứu lớn | 1,585 (175/1134/276) | 20–40/41–64/≥65y | Voltage LA cao hơn ở trẻ (chỉ hình, mV không trích được); ổ ngoài-PV trẻ 8.6% vs già 3.3% (P<0.01) | NOS · **Moderate RoB** | Voltage age-trend định tính (số trong hình) |
| REF-023 Howie 2025 | Cohort tiến cứu + huyết động xâm lấn | 125 | RN, LVEF bảo tồn, lưỡng phân 65y | Strain hồ chứa LA β=−0.37/năm (P<0.001); <65y 24.6±9.8% vs ≥65y 17.8±8.2%; cứng LA↑; **KHÔNG mapping voltage** | NOS · **Moderate RoB** | "LA cardiomyopathy" theo tuổi; không EAM |
| REF-025 Patel 2020 (CHS) | Cohort cộng đồng tiến cứu | 4,341 | Người cao tuổi cộng đồng | Strain hồ chứa LA → RN mới HR 1.80 (1.31–2.45) | NOS · **Low RoB** (cohort lớn, theo dõi dài) | Strain dự báo RN ở người cao tuổi |
| REF-024 Inciardi 2024 (ARIC) | Cohort cộng đồng | (abstract) | Người cao tuổi cộng đồng | LA function↓ → RN (29% liên quan) | NOS · **Low-Moderate RoB** | Bổ trợ CHS |
| REF-026 Yang 2021 | Cohort/registry | nhiều | RN cao tuổi (frailty) | HR cắt đốt theo frailty (0.48–0.83) | NOS · **Moderate RoB** | Outcome, không EP substrate |
| REF-027 Parks 2024 | Review + dữ liệu | nhiều | RN cao tuổi | Tổng hợp voltage/cắt đốt | N/A (review) | Bối cảnh |

### 2.3 Tham số ECG bề mặt — PWD, dispersion, SAECG, IAB, P-axis, PTFV1 (Axis 9)

| REF | Thiết kế | N | Quần thể | Hiệu ứng chính (verbatim) | RoB tool · phán định | Ghi chú |
|---|---|---|---|---|---|---|
| REF-037 Magnani 2011 (Framingham) | Cohort cộng đồng | 1,550 | ≥60y, không RN nền | PWD dài → RN mới (mỗi 10ms) độc lập | NOS · **Low RoB** (cohort lớn; ECG thập niên 1960–70) | Neo PWD cộng đồng ở người cao tuổi |
| REF-039 Intzes 2023 | SR/MA (22 NC) | 4,175 | RN cắt đốt | PWD>120ms OR 2.04 (1.16–3.58); aIAB OR 3.97 (1.79–8.85); PWD>150ms OR 10.89 (4.53–26.15); ΔPWD 7.8ms; KHÔNG bias công bố | AMSTAR/ROBINS-I (QS) · **Moderate** (I²=87% PWD>120) | Dose-response rõ; tiên lượng tái phát |
| REF-059 Dilaveris 1998 | Case-control tiến cứu | 60 BN + 40 chứng | PAF vô căn (TB 59y) | Pmax≥110ms (Se88/Sp75); PWD≥40ms (Se83/Sp85); Pmax 123±16 vs 101±10ms (p<0.0001) | NOS/QUADAS-2 · **Moderate RoB** (PAF vô căn trẻ/khỏe hơn; đơn TT) | Landmark ngưỡng PWD |
| REF-060 Dilaveris 2001 | Review | N/A | — | PWD = dẫn truyền không đồng nhất; chưa chuẩn hóa | N/A | abstract-only (PMC rỗng) |
| REF-061 Aytemir 2000 | Case-control | 40+40 | PAF vô căn | P-variance>120ms² (Se80/Sp74) | QUADAS-2 · **Moderate-High RoB** (n nhỏ) | Metric PWD thay thế |
| REF-062 Wattanachayakul 2024 | SR/MA (CIED) | gộp | BN CIED (chủ yếu cao tuổi) | IAB → AHRE RR 3.33 (1.66–6.66); PWD MD +20.56ms | AMSTAR (QS) · **Moderate** | Quần thể cao tuổi gần nhất; AHRE đại diện RN |
| REF-053 Fukunami 1991 | Case-control tiến cứu (SAECG) | 92 (42+50) | PAF vs chứng (nhịp xoang) | Phối hợp Ad>120ms & LP20≤3.5μV: Se91/Sp76/độ chính xác83% | QUADAS-2 · **Moderate-High RoB** (n nhỏ, công nghệ 1991, case-control) | Landmark ngưỡng SAECG |
| REF-054 Steinberg 1993 | Cohort tiến cứu | 130 | Phẫu thuật tim (đa số cao tuổi) | SAECG>140ms → POAF OR 3.90 (1.6–9.5, p=0.003); POAF 18% | NOS · **Moderate RoB** (đơn TT, công nghệ 1993) | Ngưỡng 140ms |
| REF-055 Guidera 1993 | Case-control tiến cứu | không rõ | PAF vs chứng | Vector composite≥155ms (Se80/Sp93/PPV89) | QUADAS-2 · **Moderate-High RoB** | Ngưỡng 155ms |
| REF-058 Kawczynski 2022 | SR/MA (32 NC) | 20,201 | Phẫu thuật tim | SAECG-PWD ES=0.8 (0.5–1.2), AUC 0.76; 12-lead PWD ES=0.4; dispersion ES=0.7 (nhạy outlier→0.1); **bias công bố có ý nghĩa** | AMSTAR/ROBINS-I (QS) · **Moderate→Low cho dispersion** | MA SAECG lớn nhất; dị nhất tính cao |
| REF-038 Bayés 2017 | Review/consensus | N/A | — | Định nghĩa aIAB; phổ biến ~1% chung, 9–10% cao tuổi | N/A | Định nghĩa |
| REF-063 Alexander 2021 | Review | N/A | — | aIAB→RN HR 2.42 (1.44–4.07, p=0.001); pIAB phổ biến ~40% (70s), >50% (80s) | N/A | Taxonomy P-wave |
| REF-064 Chen 2022 (ISE/ISHNE) | Đồng thuận chuyên gia | N/A | — | aIAB→RN HR 3.09 (2.51–3.79); P-axis→RN HR 2.34 (2.12–2.58); PTFV1/SD→RN +23%; Morris PTFV1>0.03mm·s | N/A | Tiêu chuẩn vàng tham số P-wave |
| REF-065 Bayés 2020 | Review | N/A | — | aIAB phổ biến 20–26% rất cao tuổi | N/A | abstract-only |
| REF-066 Martínez-Sellés 2020 (BAYES) | Registry tiến cứu đa TT | 556 | **≥70y, bệnh tim cấu trúc** | aIAB→RN HR 3.31 (1.87–5.86); →đột quỵ HR 4.89 (1.71–14.05); PWD/ms→RN HR 1.044; pIAB KHÔNG ý nghĩa | NOS · **Low-Moderate RoB** (tiến cứu đa TT, theo dõi 694 ngày, đúng quần thể đích) | **Trực tiếp ≥70y — bằng chứng IAB mạnh nhất** |
| REF-067 Martínez-Sellés 2015 | Cắt ngang | 80 centenarian + 269 (70s) | ≥100y vs 70–79y | Centenarian: IAB 47% (20% pIAB+26% aIAB) | NOS · **Moderate RoB** (cắt ngang, 1 thời điểm) | Dữ liệu cực cao tuổi hiếm |
| REF-068 Escobar-Robledo 2018 (Bayés-HF) | Cohort tiến cứu | 464 | Suy tim mạn TB 71y | aIAB→RN HR 2.71 (1.61–4.56); →đột quỵ HR 3.02 (1.07–8.53) | NOS · **Low-Moderate RoB** (tiến cứu, 5y, n đủ) | aIAB ở quần thể cao tuổi suy tim |
| REF-069 Lampert 2023 | Hồi cứu đa TT khổng lồ | 4.8M ECG | Không tiền sử RN | IAB phổ biến 19.6%; →RN/đột quỵ/suy tim (RMTLRC) | NOS · **Moderate RoB** (hồi cứu, không phân tầng cao tuổi) | Ước lượng phổ biến IAB chuẩn nhất |
| REF-070 Chattopadhyay 2022 | SR/MA (8 gộp/11) | ~78,222 | Hỗn hợp cộng đồng | P-axis bất thường→RN: **2.12 (1.49–3.01) [Abstract] vs 2.10 (1.48–2.72) [Results]**; I²=92%→70% | AMSTAR/ROBINS-I (QS) · **Moderate** (mâu thuẫn nội tại nguồn) | **Phải trích cả 2 giá trị** |
| REF-040 Huang 2020 | SR/MA (12 NC) | 51,372 | Hỗn hợp | PTFV1 bất thường (>0.04mm·s)→RN OR 1.39 (1.08–1.79); dị nhất theo quần thể | AMSTAR/ROBINS-I (QS) · **Moderate** | PTFV1; lưu ý ngưỡng Morris gốc >0.03 (REF-064) |

### 2.4 Cơ chế rotor/CFAE/xơ hóa + outcome cắt đốt (Axis 1, 3, 4)

| REF | Thiết kế | N | Hiệu ứng chính (verbatim) | RoB tool · phán định | Ghi chú |
|---|---|---|---|---|---|
| REF-005 Narayan 2012 (CONFIRM) | RCT nhỏ/cơ chế | 101 | Rotor 97%; FIRM-guided sống không-RN 82.4% vs 44.9% (P<0.001) | RoB 2 · **High RoB** (đơn TT, nhãn mở, nhân rộng thất bại) | Dương tính rotor — đối lập STAR AF II |
| REF-009 Nademanee 2004 (CFAE) | Quan sát landmark | 121 | CFAE-guided: 91% không loạn nhịp 1 năm | NOS · **High RoB** (quan sát, không đối chứng) | Mô tả gốc CFAE |
| REF-010 Verma 2015 (STAR AF II) | **RCT đa TT (48 TT, 12 nước)** | 589 | PVI 59% vs PVI+CFAE 49% vs PVI+đường 46% (P=0.15) — **thêm CFAE/đường KHÔNG lợi** | RoB 2 · **Low RoB** | **Âm tính — bác bỏ CFAE; ưu thế chất lượng** |
| REF-011 Marrouche 2014 (DECAAF I) | Cohort tiến cứu đa TT | 260 | Xơ hóa LGE-MRI/1% → tái phát aHR 1.06 (1.03–1.09); tuổi KHÔNG dự báo (HR 1.05, p=.61) | NOS · **Moderate RoB** | Xơ hóa dự báo; không phân tầng cao tuổi |
| REF-012 Marrouche 2022 (DECAAF II) | **RCT đa TT** | 843 | Cắt đốt theo xơ hóa KHÔNG hơn PVI: HR 0.95 (0.77–1.17, P=.63); biến cố an toàn cao hơn (2.2% vs 0) | RoB 2 · **Low-Moderate RoB** | **Âm tính — bác bỏ hướng dẫn theo MRI** |
| REF-018 Bahnson 2021 (CABANA age) | Phân tích dưới nhóm RCT | 2,204 (308 ≥75y) | ≥75y: outcome chính aHR 1.39 (0.75–2.58); tử vong aHR 1.92 (0.88–4.17), p-tương tác=0.031; **tái phát RN giảm nhất quán mọi tuổi (aHR ≥75y 0.49)** | RoB 2 · **Moderate RoB** (dưới nhóm, không định trước cho tuổi, imprecision) | Nghịch lý hiệu lực-an toàn theo tuổi |
| REF-015 Prasitlumkum 2022 | SR/MA (27 QS) | 363,542 | Thành công OR 0.85 (0.69–1.05, NS); biến chứng OR 1.42 (1.21–1.68); cryo KHÔNG tăng biến chứng | AMSTAR (QS) · **Moderate** | Outcome cắt đốt cao tuổi |
| REF-017 Lee W-C 2021 | MA (18 QS) | 21,039 | Tái phát OR 1.21 (1.11–1.33); **≥75y subgroup OR 1.48 (0.95–2.29) NS** | AMSTAR (QS) · **Moderate** | Tín hiệu "rất cao tuổi tương đương" |
| REF-014/016/032 | SR/MA | 117,869/110,606/5,948 | RR tái phát 1.07–1.16; PFA cao tuổi tương đương | AMSTAR (QS) · **Moderate/Low** | Bổ trợ outcome |
| REF-019 Hirata 2026 (REHEALTH) | Registry tiến cứu, ≥80y | 703 | Cắt đốt vs không: aHR 0.44 (0.21–0.92) sau hiệu chỉnh | NOS · **Moderate RoB** | RCT-thiếu; chỉ quan sát ghép điểm |
| REF-020 Inoue 2024 | Registry quốc gia | 170,017 | Biến chứng↑ theo tuổi (≥85y 4.30%; OR≥80y 1.22); tái phát KHÔNG khác theo tuổi (P=0.473) | NOS · **Low-Moderate RoB** (rất lớn) | An toàn theo tuổi |

---

## 3. GRADE Summary of Findings (per outcome/nhóm thông số)

> Điểm xuất phát theo thiết kế; ↓ = lý do hạ cấp (RoB / inconsistency / indirectness / imprecision /
> publication bias). Không có nâng cấp nào đủ điều kiện (dose-response của PWD/Intzes được ghi nhận nhưng
> không đủ kéo lên High vì đầu vào quan sát + I² cao).

| # | Outcome / thông số | Bằng chứng neo | GRADE | Lý do hạ cấp |
|---|---|---|---|---|
| 1 | **Voltage LA / LVZ giảm theo tuổi** | REF-001, 002, 042, 003 | **Moderate** | ↓ indirectness (một phần đo nhịp xoang/không-RN), ↓ RoB (cắt ngang/hồi cứu) — bù lại bởi tính nhất quán cao đa nghiên cứu & ghép điểm (REF-001) |
| 2 | **AERP thay đổi theo tuổi (kéo dài)** | REF-042, 043, 041 | **Low** | ↓ RoB (cắt ngang/hồi cứu, n nhỏ), ↓ indirectness (quần thể không-RN/SVT), ↓ imprecision (CI rộng, REF-043) |
| 3 | **AFCL theo tuổi** | (KHÔNG có) | **Very Low / không xếp được** | **GAP** — không có dữ liệu phân tầng tuổi; REF-073 chỉ baseline chung. Xem §6 |
| 4 | **SNRT/cSNRT (kéo dài & đảo ngược)** | REF-042, 047, 049 | **Low** | ↓ RoB (n nhỏ, REF-049 n=12), ↓ imprecision, ↓ indirectness (đo trong/sau RN, không phân tầng tuổi) |
| 5 | **Vận tốc dẫn truyền (CV) giảm theo tuổi** | REF-074, 003, 051, 052 | **Low** | ↓ indirectness (REF-074/003/051/052 ĐỀU đo nhịp xoang, KHÔNG trong RN; REF-074 không-RN), ↓ RoB (cắt ngang, n nhỏ) — nhưng nhất quán hướng (đều giảm) |
| 6 | **PWD dự báo RN (cộng đồng & tái phát)** | REF-037, 039, 059 | **Moderate** | ↓ inconsistency (I²=87% Intzes) — bù bởi MA lớn, cohort cộng đồng ≥60y (Framingham), không bias công bố (Intzes) |
| 7 | **P-wave dispersion** | REF-059, 058, 061 | **Low** | ↓ inconsistency (I²=92%, nhạy outlier→ES 0.1), ↓ **publication bias** (xác nhận Egger p=0.01, REF-058) |
| 8 | **SAECG filtered P-wave dự báo RN** | REF-053, 054, 055, 058 | **Moderate** | ↓ indirectness (công nghệ 1990s, ít dùng nay), ↓ inconsistency (ngưỡng 122–155ms) — bù bởi MA N=20,201, ES 0.8, AUC 0.76 nhất quán cho SAECG-PWD |
| 9 | **IAB tiến triển → RN/đột quỵ** | REF-066, 068, 063, 064, 069 | **Moderate** | ↓ RoB (quan sát) — KHÔNG hạ thêm: nhất quán cao, hiệu ứng lớn (HR 2.7–4.9), trực tiếp quần thể ≥70y (REF-066/068), đa nguồn. Đây là nhóm mạnh nhất |
| 10 | **P-wave axis bất thường → RN** | REF-070, 064 | **Moderate** | ↓ inconsistency (I²=92%; mâu thuẫn nội tại nguồn 2.12 vs 2.10) — bù bởi N≈78k, hiệu ứng nhất quán hướng |
| 11 | **PTFV1 → RN** | REF-040, 064 | **Low** | ↓ inconsistency (dị nhất theo quần thể: HD OR 4.89 vs chung 1.15), ↓ indirectness (ngưỡng không thống nhất 0.03 vs 0.04) |
| 12 | **Cắt đốt RN ở cao tuổi: tái phát/an toàn** | REF-013, 015, 017, 018, 020 | **Low-Moderate** | Hiệu lực (tái phát) Low-Moderate (MA đầu vào QS); an toàn Moderate (nhất quán biến chứng↑); outcome cứng ≥75y **Very Low** (CABANA dưới nhóm imprecise) |
| 13 | **Xơ hóa LGE-MRI hướng dẫn cắt đốt** | REF-011 (+), REF-012 (−) | **Moderate** | Tiên lượng Moderate (DECAAF I cohort); **hướng dẫn điều trị: bác bỏ bởi RCT (DECAAF II)** — bằng chứng RCT High bị ↓ một chút cho indirectness quần thể |
| 14 | **Rotor/CFAE hướng dẫn cắt đốt** | REF-005 (+), REF-010 (−) | **Moderate (nghiêng âm tính)** | RCT đa TT (STAR AF II) âm tính lấn át thử nghiệm đơn TT nhãn mở (CONFIRM) |

**Đếm GRADE (11 nhóm thông số EP cốt lõi, mục 1–11):** High 0 · Moderate 4 (voltage, PWD, SAECG, IAB,
P-axis = thực tế 5 nếu tách) · Low 5 (AERP, SNRT, CV, dispersion, PTFV1) · Very Low 1 (AFCL — không xếp).
Nếu gộp như tóm tắt điều hành: **0 High / 3–5 Moderate / 5 Low / Very Low cho AFCL.**

---

## 4. Risk-of-Bias Summary (theo công cụ phù hợp thiết kế)

**Cochrane RoB 2 (RCT):**
- REF-010 STAR AF II — **Low RoB** (đa TT, ngẫu nhiên, mù đánh giá kết cục; tài trợ St. Jude ghi nhận nhưng kết quả âm tính nên ít nguy cơ thiên lệch tài trợ).
- REF-012 DECAAF II — **Low-Moderate** (RCT nhưng full-text không lấy được; PVI không mù được).
- REF-073 Haïssaguerre 2004 — **Some concerns** (n=70, đơn TT, endpoint thay thế/cơ chế, không mù).
- REF-005 CONFIRM — **High RoB** (đơn TT, nhãn mở, nhân rộng thất bại ở các trung tâm khác).
- REF-018 CABANA age subgroup — **Moderate** (dưới nhóm; tuổi không phải phân tầng định trước có công suất; imprecision lớn ở ≥75y).

**ROBINS-I / AMSTAR (meta-analysis tổng hợp quan sát):** REF-013, 014, 015, 016, 017, 032, 039, 040, 058,
062, 070 — trần chất lượng bị giới hạn bởi **đầu vào quan sát**; RoB **Moderate** chung; **publication
bias** xác nhận cho REF-058 (PWD-dispersion, 12-lead PWD) và nghi ngờ REF-070 (funnel). I² cao (79–92%)
ở REF-039/058/070.

**Newcastle-Ottawa (cohort/case-control/cắt ngang):** đa số corpus. **Low RoB:** REF-025 (CHS), REF-037
(Framingham), REF-020 (registry 170k), REF-066/068 (tiến cứu đa TT ≥70y). **Moderate:** REF-001, 002, 003,
042, 043, 074, 011, 023. **High RoB:** REF-041 (n=17), REF-049 (n=12), REF-045/047 (abstract, n nhỏ).

**QUADAS-2 (nghiên cứu độ chính xác chẩn đoán — SAECG/PWD ngưỡng):** REF-053, 055, 059, 061 — **Moderate-High
RoB**: thiết kế case-control (spectrum bias: PAF vô căn trẻ/khỏe vs chứng → phóng đại Se/Sp), không làm mù
phán định, công nghệ cũ. Ngưỡng tối ưu hóa hậu kiểm (data-driven cutoff) là nguy cơ overfitting điển hình.

---

## 5. Assumption Register (mọi ngoại suy phải đưa vào Hạn chế — Law 5)

| # | Giả định / ngoại suy | Nguồn | Mức rủi ro | Đưa vào Hạn chế |
|---|---|---|---|---|
| A-1 | **CV giảm theo tuổi (đo trong NHỊP XOANG, không-RN) ngoại suy sang bối cảnh nhĩ lão hóa có RN** | REF-074 (không-RN), REF-003 (không-RN), REF-051/052 (nhịp xoang) | **Cao** | Có — CV trong RN có thể khác do remodeling điện; không có dữ liệu CV-trong-RN phân tầng tuổi |
| A-2 | **AFCL: KHÔNG có dữ liệu cao tuổi — mọi phát biểu AFCL theo tuổi là ngoại suy/suy đoán** | REF-073 (TB 53y, không phân tầng) | **Rất cao** | **Bắt buộc** — xem §6. Không dùng REF-074 thay thế (không phải AFCL) |
| A-3 | **AERP "kéo dài theo tuổi" từ quần thể không-RN/SVT (Kistler, Lee) áp cho RN cao tuổi** | REF-042 (không-RN), REF-043 (SVT) | **Cao** | Có — trong RN, AERP bị rút ngắn do remodeling (REF-044/045) → giá trị tuyệt đối ở RN cao tuổi không xác định (nghịch lý, §7) |
| A-4 | **Ngưỡng SAECG/PWD (Fukunami 120ms, Guidera 155ms, Dilaveris 110/40ms) từ PAF vô căn trẻ áp cho cao tuổi** | REF-053, 055, 059 | Trung bình-cao | Có — spectrum bias; ngưỡng có thể dịch ở người cao tuổi (PWD tăng nền theo tuổi, REF-042/066) |
| A-5 | **SNRT (606→408ms) đại diện cho "cao tuổi" dù nguồn không phân tầng tuổi** | REF-047, 049 | Trung bình | Có — giá trị từ RN dai dẳng/khoảng ngừng, không phải chuẩn theo tuổi |
| A-6 | **IAB → RN/đột quỵ (HR mạnh) chủ yếu từ quần thể bệnh tim cấu trúc/suy tim ≥70y áp chung cho RN cao tuổi** | REF-066, 068 | Thấp-trung bình | Có — đây là nhóm trực tiếp nhất, nhưng có bệnh tim cấu trúc nền |
| A-7 | **Coi hướng dẫn ESC 2023/ACC-AHA 2023 còn hiệu lực (2026)** | REF-029, 030 | Thấp | Có — guideline 3 năm tuổi, có thể có cập nhật |
| A-8 | **Dữ liệu chủ yếu da trắng (Âu-Mỹ)/Đông Á áp cho quần thể Việt Nam** | toàn corpus; REF-071/072 không phải EP chuẩn | **Cao** | **Bắt buộc** — không có dữ liệu EP xâm lấn chuẩn Việt Nam (population gap) |
| A-9 | **PTFV1 ngưỡng: dùng >0.04 (Huang/REF-040) hay >0.03 mm·s (Morris gốc, REF-064)** | REF-040 vs REF-064 | Trung bình | Có — không nhất quán ngưỡng; nêu cả hai |
| A-10 | **Meta-analysis outcome cắt đốt (đầu vào quan sát) coi như bằng chứng hiệu lực** | REF-013/015/017 | Trung bình | Có — không phải RCT; nhiễu chỉ định (sicker→drug) |
| A-11 | **AHRE (REF-062) coi là đại diện cho RN lâm sàng ở người cao tuổi/CIED** | REF-062 | Thấp-trung bình | Có — AHRE là RN dưới lâm sàng, không hoàn toàn tương đương |

---

## 6. AFCL (G-2) — GAP CHƯA GIẢI QUYẾT (mục riêng, bắt buộc)

**Phán định:** Trong toàn bộ 72 bản ghi citable, **KHÔNG có một dữ liệu AFCL nào được phân tầng theo tuổi.**

- **REF-073 (Haïssaguerre 2004)** cung cấp **baseline AFCL CHUNG** = 186±19ms (xoang vành, RN tạo được)
  và động học AFCL khi cắt đốt — nhưng tuổi trung bình chỉ **53±8 / 53±9**, và bài báo **không phân tích
  tuổi như một biến**. Đây là giá trị định nghĩa/tham chiếu chung, KHÔNG phải dữ liệu cao tuổi.
- **REF-074 (Kojodjojo 2006)** có phân tầng tuổi xuất sắc cho CV/ERP, NHƯNG đo trong **nhịp xoang ở BN
  KHÔNG tiền sử RN** → **KHÔNG phải AFCL** (AFCL đòi hỏi RN đang diễn ra). **TUYỆT ĐỐI KHÔNG được dùng
  REF-074 để ngầm lấp gap AFCL** (cảnh báo từ brief; tôi xác nhận và khóa lại đây).
- REF-046 (Manios, vốn sẽ cho AFCL 161–180ms ở RN dai dẳng) **đã bị LOẠI BỎ HẲN** (2026-06-30) — không
  được phục hồi dưới bất kỳ hình thức nào.

**Hệ quả cho writer:**
1. AFCL theo tuổi GRADE = **Very Low / không xếp được** (không có bằng chứng trực tiếp).
2. Trong bảng biến số CRF, AFCL phải gắn nhãn **"ngoại suy / không có dữ liệu chuẩn cao tuổi"** (Assumption A-2).
3. Phần Hạn chế PHẢI nêu rõ đây là **evidence gap thực sự** (đã tìm kiếm hệ thống P-1…P-9 + 2 vòng bổ
   sung, vẫn trống), KHÔNG phải thiếu sót tìm kiếm. Có thể đề xuất như "next direction" (nghiên cứu AFCL
   phân tầng tuổi trong RN dai dẳng).
4. Giá trị 186±19ms của REF-073 CHỈ được dùng làm **định nghĩa/khoảng tham chiếu chung**, kèm chú thích
   tuổi-TB-53 rõ ràng.

---

## 7. Steelman các trục đang tranh cãi (đưa cả hai chiều cho writer)

### 7.1 Nghịch lý AERP theo tuổi (G-1/G-9)

**Phát biểu đồng thuận (mặc định):** Lão hóa nhĩ → AERP **kéo dài** (REF-042 Kistler: AERP↑ theo tuổi
r=0.56; REF-043 Lee: AERP≥280ms → RN aHR 2.08), phản ánh remodeling cấu trúc/xơ hóa.

**Steelman chiều đối lập (mạnh nhất):** Ở **chính bệnh nhân RN** (không phải quần thể không-RN của Kistler/
Lee), remodeling điện do nhịp nhanh làm AERP **rút ngắn** (REF-044 Yu 1998, REF-045 Yu 1999 — đảo ngược
sau chuyển nhịp). Do đó, giá trị AERP tuyệt đối ở một BN RN cao tuổi là **kết quả của hai lực đối nghịch**:
xơ hóa-tuổi kéo dài vs remodeling-RN rút ngắn. REF-048 (Laredo/Nattel) viết hẳn review "two-sided" để mô
tả nghịch lý này — xác nhận đây là **tranh luận thật**, KHÔNG do thiếu dữ liệu.

**Phán định khả-giải-quyết:** **Không giải quyết được bằng chất lượng nghiên cứu** — đây là mâu thuẫn cơ
chế thật. Writer phải trình bày cả hai chiều, KHÔNG chọn một bên im lặng. Quan trọng: **không tồn tại
nghiên cứu nào đo AERP phân tầng tuổi trong RN đang diễn ra** ở người cao tuổi → giá trị AERP "chuẩn của
RN cao tuổi" là **không xác định** (gắn vào A-3).

### 7.2 Rotor/CFAE (Axis 3) — CONFIRM dương tính vs STAR AF II âm tính

**Phát biểu pro-rotor (steelman dương tính):** REF-005 (CONFIRM) cho thấy rotor hiện diện 97% ca RN và
cắt đốt FIRM-guided cải thiện sống không-RN mạnh (82.4% vs 44.9%, P<0.001); REF-006 (Hansen) +REF-009
(Nademanee CFAE 91% thành công 1 năm) ủng hộ cơ chế nguồn khu trú/CFAE là có thật về mặt sinh lý.

**Phát biểu âm tính (đồng thuận hiện tại):** REF-010 (STAR AF II) — **RCT đa trung tâm, 48 TT, 12 nước,
N=589** — thêm CFAE hoặc đường vào PVI **KHÔNG cải thiện** (59% vs 49% vs 46%, P=0.15), thậm chí đường
nối còn kém hơn. REF-008 (Nattel) phê phán cân bằng paradigm rotor.

**Phán định khả-giải-quyết:** **GIẢI QUYẾT ĐƯỢC bằng chất lượng nghiên cứu.** CONFIRM là đơn trung tâm,
nhãn mở, và **nhân rộng thất bại** ở các trung tâm độc lập; STAR AF II là RCT đa trung tâm chất lượng cao
(RoB 2 = Low). Trọng số bằng chứng nghiêng rõ về phía âm tính. Writer nên trình bày: rotor/CFAE là khái
niệm cơ chế quan trọng lịch sử nhưng **không được RCT chất lượng cao xác nhận giá trị hướng dẫn cắt đốt**;
nay ít dùng lâm sàng. (Song song với DECAAF I dương-tính-tiên-lượng vs DECAAF II RCT-âm-tính-hướng-dẫn —
cùng một bài học: tiên lượng ≠ giá trị can thiệp.)

### 7.3 (Bổ sung) Nghịch lý hiệu lực-an toàn cắt đốt ở ≥75y

**Pro-ablation:** Tái phát RN giảm nhất quán mọi lứa tuổi (REF-018 CABANA: aHR ≥75y 0.49; REF-019 REHEALTH
aHR 0.44; REF-017: ≥75y subgroup tương đương non-elderly).

**Thận trọng:** Outcome **cứng** ở ≥75y xấu đi — CABANA tử vong aHR 1.92 (0.88–4.17), biến cố chính aHR
1.39, p-tương tác tử vong=0.031; biến chứng↑ theo tuổi (REF-015 OR 1.42; REF-020). **Steelman:** lợi ích
nhịp không tự động chuyển thành lợi ích sống còn ở người rất cao tuổi/yếu. Khả-giải-quyết một phần: dữ
liệu mâu thuẫn do **imprecision** (≥75y n nhỏ trong CABANA) + nhiễu chỉ định trong registry → cần thận
trọng, không kết luận chắc.

---

## 8. Per-claim "evidence strength" labels (writer phải mang vào bản thảo)

| Claim writer sẽ viết | Nhãn sức mạnh | Ngôn ngữ phù hợp |
|---|---|---|
| Voltage LA/LVZ giảm theo tuổi | **Moderate** | "nhất quán cho thấy", "có khả năng" |
| AERP kéo dài theo tuổi (quần thể không-RN) | **Low** | "một số nghiên cứu gợi ý", "có thể" — kèm nghịch lý |
| AERP ở RN cao tuổi (giá trị tuyệt đối) | **Không xác định** | "chưa có dữ liệu trực tiếp" |
| **AFCL theo tuổi** | **Very Low / GAP** | **"không có dữ liệu"; chỉ baseline chung ~186ms (tuổi TB 53)** |
| SNRT kéo dài & đảo ngược sau cắt đốt | **Low** | "bằng chứng hạn chế gợi ý" |
| CV giảm theo tuổi | **Low** | "gợi ý (đo trong nhịp xoang)" — gắn A-1 |
| PWD dự báo RN/tái phát | **Moderate** | "liên quan độc lập", "dự báo" |
| P-wave dispersion | **Low** | "có thể liên quan; bias công bố" |
| SAECG filtered P-wave | **Moderate** (nhưng công nghệ cũ) | "dự báo tốt nhưng ít dùng nay" |
| IAB tiến triển → RN/đột quỵ | **Moderate** (nhóm mạnh nhất) | "liên quan chặt chẽ", "dự báo mạnh" |
| P-axis bất thường → RN | **Moderate** | "liên quan" — trích cả 2.12 & 2.10 |
| PTFV1 → RN | **Low** | "liên quan; ngưỡng chưa thống nhất" |
| Cắt đốt cao tuổi: tái phát/an toàn | **Low-Moderate** | "tái phát cao hơn nhẹ; biến chứng cao hơn" |
| Cắt đốt ≥75y: outcome cứng | **Very Low** | "không chắc chắn; có thể không lợi" |
| Xơ hóa MRI hướng dẫn cắt đốt | **Moderate (âm tính)** | "RCT không chứng minh lợi ích" |
| Rotor/CFAE hướng dẫn cắt đốt | **Moderate (âm tính)** | "RCT chất lượng cao bác bỏ" |
| Dữ liệu Việt Nam (EP chuẩn) | **GAP** | "không có dữ liệu chuẩn EP Việt Nam" |

---

## 9. Gửi tới synthesis-writer

**Must-mention controversies (không được giấu):** (1) AFCL gap tuổi — §6; (2) nghịch lý AERP — §7.1;
(3) rotor/CFAE & DECAAF (tiên lượng ≠ can thiệp) — §7.2; (4) nghịch lý hiệu lực-an toàn cắt đốt ≥75y — §7.3;
(5) mâu thuẫn nội tại nguồn REF-070 (P-axis 2.12 vs 2.10) — phải trích cả hai.

**Nhóm bằng chứng MẠNH NHẤT để dựa vào:** IAB tiến triển (REF-066/068/064 — Moderate, trực tiếp ≥70y),
PWD (REF-037/039), voltage age-trend (REF-001/002/042).

**Nhóm YẾU NHẤT / phải hedge mạnh:** AFCL (gap), AERP-trong-RN (không xác định), CV (indirectness nhịp
xoang), outcome cứng ≥75y (imprecision).

**Cờ Law 1/5 cho writer:** mọi số AFCL theo tuổi → "không báo cáo"; mọi ngoại suy trong Assumption Register
(§5) phải xuất hiện ở phần Hạn chế.

**File:** `/home/user/CLAUDE_MRA_3/_workspace/04_appraisal.md` · **Số liệu nguồn:** `_workspace/03b_numbers.md`
