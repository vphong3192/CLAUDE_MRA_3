# vi-terminology.md — Vietnamese medical-term standardization

Load when writing a review in Vietnamese. These mappings were **verified directly by the user** in v1
and are binding for Vietnamese output. Convention: use the Vietnamese term first, with the English in
parentheses on first appearance; afterward the abbreviation or Vietnamese is fine.

> This is a living glossary. When the user confirms a new term, the lead appends it here
> (user-approved only). When the user corrects a translation, record it here **before** doing anything
> else — translation errors recur otherwise (v1 lesson).

## Electrophysiology / ablation (verified)
| English | ❌ Wrong/old | ✅ Standard Vietnamese |
|---|---|---|
| Global Impedance Drop | GID (bare abbrev.) | Giảm trở kháng toàn cục (global impedance drop — GID) |
| Pulmonary Vein Isolation | PVI (unexplained) | Cô lập tĩnh mạch phổi (PVI) |
| Operator / Electrophysiologist | Phẫu thuật viên | Bác sỹ can thiệp |
| Atrial Fibrillation | — | Rung nhĩ (AF) |
| Contact Force | — | Lực tiếp xúc (CF) |
| Force-Time Integral | — | Tích phân lực-thời gian (FTI) |
| Ablation Index | — | Chỉ số ablation (AI) |
| Lesion Size Index | — | Chỉ số kích thước tổn thương (LSI) |
| Local Impedance Drop | — | Giảm trở kháng tại chỗ (LID) |
| First-pass isolation | — | Cô lập lần đầu (first-pass isolation) |
| Interlesion distance | — | Khoảng cách liên điểm (ITD) |
| High-power short-duration | — | Năng lượng cao thời gian ngắn (HPSD) |
| Transmurality | — | Xuyên thấu qua thành (transmurality) |
| Pulmonary vein reconnection | — | Kết nối lại tĩnh mạch phổi (PVR) |

## General review terms
| English | ✅ Standard Vietnamese |
|---|---|
| Systematic review | Tổng quan hệ thống |
| Meta-analysis | Phân tích gộp |
| Randomized controlled trial (RCT) | Thử nghiệm ngẫu nhiên có đối chứng (RCT) |
| Cohort study | Nghiên cứu đoàn hệ |
| Risk of bias | Nguy cơ sai lệch |
| Certainty of evidence (GRADE) | Mức độ chắc chắn của bằng chứng (GRADE) |
| Preprint (not peer-reviewed) | Bản tiền in (chưa bình duyệt) |
| Consensus / Controversy | Đồng thuận / Tranh cãi |
| Limitations | Giới hạn |
| Confidence interval (CI) | Khoảng tin cậy (CI) |

## Cardiometabolic / CV prevention (verified Entry #1, 2026-06-14)
| English | ✅ Standard Vietnamese |
|---|---|
| Major adverse cardiovascular events (MACE) | biến cố tim mạch bất lợi nặng (MACE) |
| Hazard ratio (HR) | tỷ số nguy cơ (HR) |
| Relative risk (RR) | nguy cơ tương đối (RR) |
| Primary / secondary prevention | dự phòng nguyên phát / thứ phát |
| Body mass index (BMI) | chỉ số khối cơ thể (BMI) |
| GLP-1 receptor agonist | chất chủ vận thụ thể GLP-1 (GLP-1 RA) |

## LA electrophysiology / elderly AF (verified Entry #5, 2026-06-15)
| English | ✅ Standard Vietnamese |
|---|---|
| Unipolar voltage | Điện thế đơn cực |
| Bipolar voltage | Điện thế lưỡng cực |
| Low-voltage zone (LVZ) | Vùng điện thế thấp (LVZ) |

## Ablation modalities — CBA vs PFA (verified Entry #7, 2026-06-18)
| English | ❌ Wrong/old | ✅ Standard Vietnamese |
|---|---|---|
| ablation (the procedure/verb) | triệt phá | **triệt đốt** |
| Cryoballoon ablation (CBA) | triệt phá bằng bóng lạnh | Triệt đốt bằng bóng áp lạnh (cryoballoon ablation, CBA); short form: **bóng áp lạnh** |
| Pulsed-field ablation (PFA) | triệt phá bằng trường xung điện | Triệt đốt bằng trường xung (pulsed-field ablation, PFA); short form: **trường xung** |
| Implantable cardiac monitor (ICM) | máy theo dõi tim cấy ghép | thiết bị theo dõi tim cấy ghép (ICM) |
| Head-to-head randomized trial (CBA vs PFA) | thử nghiệm ngẫu nhiên CBA-đối-PFA | thử nghiệm ngẫu nhiên so sánh đối đầu CBA và PFA |

## Merged from legacy root glossary (PROVISIONAL — chờ người dùng xác nhận)
These terms existed only in the old root-level `review-synthesis/references/vi-terminology.md` (Entry #4,
ablation metrics RF-PVI) before the two glossaries were unified into this single canonical file. They are
**not yet user-verified in this file** — confirm or correct before treating as binding.
| English | Provisional Vietnamese | Note |
|---|---|---|
| Radiofrequency (RF) ablation | triệt đốt bằng năng lượng tần số radio (sóng cao tần) | aligns "ablation"→"triệt đốt" (Entry #7) |
| Durable lesion | tổn thương bền vững | |
| Averaged impedance drop (AID) | giảm trở kháng trung bình (AID) | TactiFlex SE / EnSite X term |

> **Resolved (user decision, 2026-06-23):** *Ablation Index (AI)* is standardized as
> **"chỉ số ablation (AI)"** — the proper index name keeps "Ablation" in English. This is intentionally
> distinct from the translated *verb* "triệt đốt" (Entry #7): the procedure/verb is translated, the named
> index is not. Do NOT re-translate AI as "chỉ số triệt đốt".


When a needed term is missing here: translate carefully, mark it provisional, and ask the user to
confirm — then it gets added (approved). Never invent a Vietnamese term silently for a key concept.

## Confirmed Entry #8 (elderly CB-vs-RF review, user-verified 2026-06-23)
| English | ✅ Standard Vietnamese | Note |
|---|---|---|
| Mechanism-specific (safety) trade-off | **đánh đổi rủi ro theo cơ chế** | CBA↔liệt thần kinh hoành vs RF↔rò nhĩ-thực quản/chèn ép/đột quỵ; không phải "an toàn hơn toàn cục" |
| Irrigated (ablation) catheter | **catheter đốt tưới lạnh** | RF tưới lạnh; *open-irrigated* = **tưới lạnh hở** (tưới nước muối làm lạnh đầu đốt) |
| Excess recurrence (in the elderly) | **tái phát tăng thêm (ở người cao tuổi)** | phần tái phát vượt trội ở người cao tuổi so với người trẻ; tránh "dư thừa tái phát" |
| Excess complications / excess stroke | **biến chứng tăng thêm / đột quỵ tăng thêm** | cùng khái niệm "excess"; trật tự tự nhiên: danh từ + "tăng thêm" |
| Phrenic nerve palsy (PNP) | **liệt thần kinh hoành (PNP)** | biến chứng đặc trưng của CBA, thường thoáng qua |
| Atrio-oesophageal fistula (AEF) | **rò nhĩ-thực quản (AEF)** | biến chứng thảm khốc, nghiêng mạnh về RF (~25×) |
| Blanking period | **giai đoạn blanking** | giữ "blanking" (thuật ngữ EP quy ước; 3 tháng theo Calkins) |
| Monitoring intensity | **cường độ theo dõi** | yếu tố gây sai lệch phát hiện (CIRCA-DOSE) |

> **Style note (Entry #8, user 2026-06-23):** *artifact (of methodology)* — KHÔNG dịch chữ thành "tạo tác". Diễn đạt theo ý để người đọc tự hiểu, ví dụ "ưu thế của CBA một phần **do được so sánh với** kỹ thuật RF cũ" / "**phản ánh** việc so với nhánh RF dưới chuẩn" / "**do** sai lệch xuất bản". Nguyên tắc chung: dịch theo nghĩa, tránh dịch word-by-word các thuật ngữ trừu tượng.

| Binary / dichotomous endpoint | **tiêu chí (đánh giá) kiểu có–không** | vd "tự do khỏi loạn nhịp theo tiêu chí có–không tái phát (ngưỡng ≥30 giây)"; tránh "điểm cuối nhị phân" (tối nghĩa) |
