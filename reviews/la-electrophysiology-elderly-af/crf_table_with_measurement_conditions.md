# Bảng biến số đề xuất (CRF) — bản CHỐT, đã người dùng duyệt cấu trúc (2026-06-30)

**Mục đích:** Đây là bảng biến số/CRF cho nghiên cứu mô tả thông số điện học/điện sinh lý nhĩ trái ở
bệnh nhân RN cao tuổi — một trong hai mục tiêu đã khóa ở Phase 0 (tổng quan tường thuật + bảng CRF).
Nguồn: `_workspace/04_appraisal.md` (GRADE, RoB, evidence-table, Assumption Register), kho
`reference/la-electrophysiology-elderly-af.md`.

**Quyết định cấu trúc (người dùng, 2026-06-30):** (1) Thêm cột "Ngoại suy/giả định" — **có**; (2) thêm cột
"Trạng thái Việt Nam" — **có**; (3) tách AFCL thành khung cảnh báo riêng — **không**, giữ AFCL là một dòng
bình thường trong bảng (dòng #2), không có box/highlight đặc biệt.

**Quy ước cột:**
- **Khả thi:** EP xâm lấn (cần phòng EP-lab) / ECG bề mặt (không xâm lấn) / Cần thiết bị đặc biệt (SAECG, omnipolar, CARTO) / Không xâm lấn (siêu âm).
- **Ngoại suy/giả định:** tham chiếu trực tiếp đến mục Assumption Register tương ứng trong `04_appraisal.md` §5.
- **Mức bằng chứng:** GRADE theo nhóm thông số (§3, `04_appraisal.md`).
- Mọi giá trị số trong bảng là verbatim từ kho, không tự suy diễn.

---

| # | Nhóm thông số | Định nghĩa / Đơn vị | Phương pháp đo | Khả thi | Xu hướng/giá trị tham chiếu theo tuổi (nếu có) | Ngoại suy/giả định | Trạng thái Việt Nam | GRADE | Bằng chứng neo |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **AERP** | Thời gian trơ hiệu lực nhĩ, ms | Kích thích theo chương trình (S1S2), đo tại CS/RA/LA | EP xâm lấn | ↑ theo tuổi ở quần thể không-RN (r=0,56, p<0,01); AERP≥280ms → RN mới aHR 2,08; **giá trị tuyệt đối trong RN ở người cao tuổi: KHÔNG XÁC ĐỊNH** | **A-3 (Cao):** "kéo dài theo tuổi" đo ở quần thể KHÔNG-RN/SVT; trong RN thực tế AERP bị rút ngắn do remodeling — chiều ngược lại | Không có dữ liệu | **Low** | REF-042, 043, 041, 044, 045, 048 |
| 2 | **AFCL** | Khoảng cách giữa các sóng rung nhĩ liên tiếp trong RN đang diễn ra, ms | Điện đồ nội mạc (thường tại CS) trong lúc RN | EP xâm lấn | Baseline chung (không phân tầng tuổi, TB 53y): 186±19ms (REF-073); **không có dữ liệu phân tầng theo tuổi** | **A-2 (Rất cao):** không có dữ liệu cao tuổi nào — mọi phát biểu AFCL theo tuổi là ngoại suy/suy đoán, GAP thực sự | Không có dữ liệu | **Very Low / GAP** | REF-073 (chỉ baseline chung) |
| 3 | **SNRT / cSNRT** | Thời gian phục hồi nút xoang sau kích thích vượt tần số, ms | Overdrive pacing, đo khoảng nghỉ xoang đầu tiên | EP xâm lấn | cSNRT trong RN dai dẳng 606ms → 408ms sau 1 tháng chuyển nhịp (đảo ngược); chưa có chuẩn theo tuổi | **A-5 (Trung bình):** giá trị từ RN dai dẳng/khoảng ngừng xoang, nguồn không phân tầng tuổi | Không có dữ liệu | **Low** | REF-047, 049, 042 |
| 4 | **CV** | Vận tốc dẫn truyền xung động nhĩ, cm/s hoặc m/s | Mapping điện giải phẫu (CARTO/EnSite) | EP xâm lấn, cần thiết bị mapping | Giảm theo tuổi: WPV nghịch r=-0,77 (RA)/-0,79 (LA), P<0,0001 (nhịp xoang, không-RN); CV thấp ở vùng phân mảnh điện thế (46,0 vs 64,5cm/s) | **A-1 (Cao):** đo trong NHỊP XOANG/không-RN, ngoại suy sang bối cảnh nhĩ lão hóa có RN — CV trong RN có thể khác do remodeling điện | Không có dữ liệu | **Low** | REF-074, 003, 051, 052 |
| 5 | **Voltage nhĩ trái (bipolar/unipolar) & LVZ** | Biên độ điện thế nội mạc, mV; LVZ = % diện tích <0,5mV | Mapping điện giải phẫu biên độ-điện thế | EP xâm lấn, cần thiết bị mapping | ↓ rõ theo tuổi: 1,5mV (≥75y) vs 2,4mV (<75y); LVZ 67% vs 30%; theo thập niên: 1,0±0,4mV (≥80y) | Nhẹ — một phần dữ liệu (REF-003) đo ở quần thể không-RN | Không có dữ liệu | **Moderate** | REF-001, 002, 042, 003 |
| 6 | **PWD** | Thời gian sóng P trên ECG 12 chuyển đạo, ms | Đo thủ công/tự động ECG bề mặt | ECG bề mặt | Tăng theo tuổi (103,5ms ở ≥60y vs 91,4ms ở ≤30y); ngưỡng ≥110ms dự báo RN; PWD>120ms → tái phát OR 2,04 | **A-4 (Trung bình-cao):** ngưỡng chẩn đoán (Dilaveris ≥110ms) rút ra từ PAF vô căn TRẺ, có thể dịch ở người cao tuổi (PWD nền tăng theo tuổi) | **Có gián tiếp:** REF-071 (Nguyễn 2024) — PWD ở BN COPD cao tuổi Hà Nội, không thuần RN | **Moderate** | REF-042, 037, 039, 059 |
| 7 | **P-wave dispersion** | Chênh lệch PWD lớn nhất–nhỏ nhất giữa các chuyển đạo, ms | Đo PWD 12 chuyển đạo, tính hiệu số | ECG bề mặt | PWD≥40ms dự báo PAF (Se83/Sp85); **bias công bố đã xác nhận**; ES nhạy outlier (0,7→0,1) | **A-4 (Trung bình-cao):** cùng nguồn ngưỡng PAF vô căn trẻ | Không có dữ liệu | **Low** | REF-059, 058, 061 |
| 8 | **SAECG filtered P-wave** | Thời gian sóng P lọc nhiễu tần số cao, ms | Signal-averaged ECG (kỹ thuật chuyên biệt) | Cần thiết bị đặc biệt (ít dùng lâm sàng hiện nay) | Ngưỡng 120–155ms dự báo PAF/POAF (Se80–91%); MA N=20.201, ES=0,8 | **A-4 (Trung bình-cao):** ngưỡng từ PAF vô căn trẻ + công nghệ 1990s | Không có dữ liệu | **Moderate** (công nghệ cũ) | REF-053, 054, 055, 058 |
| 9 | **IAB / Hội chứng Bayés** | Block dẫn truyền liên nhĩ qua bó Bachmann; PWD≥120ms (partial), ±2 pha DII/III/aVF (advanced) | ECG 12 chuyển đạo, phân loại ISE/ISHNE | ECG bề mặt | Phổ biến ↑ rõ theo tuổi (~1%→9–10% cao tuổi, 20–26% rất cao tuổi); aIAB → RN HR 2,7–4,9 (trực tiếp ≥70y) | **A-6 (Thấp-trung bình):** chủ yếu từ quần thể bệnh tim cấu trúc/suy tim ≥70y — đây là nhóm trực tiếp nhất, rủi ro ngoại suy thấp nhất trong bảng | Không có dữ liệu | **Moderate** (mạnh nhất) | REF-066, 068, 063, 064, 069 |
| 10 | **P-wave axis** | Trục điện học sóng P mặt phẳng trán, độ (°) | ECG 12 chuyển đạo (chuyển đạo chi) | ECG bề mặt | Trục bất thường → RN: OR 2,12 (Abstract)/2,10 (Kết quả) — **mâu thuẫn nội tại nguồn, trích cả hai** | Thấp — quần thể N≈78k đa dạng tuổi, không ngoại suy lớn | Không có dữ liệu | **Moderate** | REF-070, 064 |
| 11 | **PTFV1** | Diện tích pha âm sóng P ở V1, mm·s | Đo ECG chuyển đạo V1 | ECG bề mặt | >0,04mm·s → RN OR 1,39 (ngưỡng gốc Morris >0,03mm·s) | **A-9 (Trung bình):** hai ngưỡng không nhất quán (0,03 vs 0,04) — nêu cả hai | Không có dữ liệu | **Low** | REF-040, 064 |
| 12 | **LA strain (hồ chứa)** | Biến dạng cơ học nhĩ trái thì hồ chứa, % | Siêu âm tim đánh dấu mô (STE) | Không xâm lấn (siêu âm) | ↓ theo tuổi (β=-0,37%/năm); <65y 24,6% vs ≥65y 17,8%; dự báo RN mới HR 1,80 | Thấp — cohort cộng đồng cao tuổi trực tiếp (CHS, ARIC) | Không có dữ liệu | **Moderate** | REF-023, 025, 024 |
| 13 | **Rotor / CFAE** *(đề cập ngắn theo phạm vi đã thống nhất)* | Nguồn khu trú/điện đồ phân mảnh phức tạp trong RN | Mapping FIRM hoặc phân tích điện đồ CFAE | EP xâm lấn, cần thiết bị mapping | Khái niệm cơ chế lịch sử quan trọng nhưng **RCT chất lượng cao (STAR AF II) bác bỏ giá trị hướng dẫn cắt đốt thêm vào PVI** | Thấp — kết luận dựa trên RCT đa trung tâm, không phải ngoại suy quần thể | Không có dữ liệu | **Moderate (âm tính)** | REF-005, 010 |

---

**Ghi chú Việt Nam (tổng quát):** Không có dữ liệu chuẩn điện sinh lý xâm lấn nào (AERP/AFCL/SNRT/CV/voltage)
công bố trên quần thể Việt Nam (population gap A-8, xem `03_research_map.md` §3). Riêng PWD có dữ liệu gián
tiếp (REF-071) nhưng trên quần thể COPD, không thuần RN — không dùng làm ngưỡng chính, chỉ làm bối cảnh.

---

## Khối "Điều kiện đo" — BẮT BUỘC kèm mỗi biến điện học đo trong EP study (bổ sung 2026-07-01, theo yêu cầu người dùng)

**Lý do:** điện thế và CV **không phải thuộc tính bất biến của mô** — chúng phụ thuộc **nhịp lúc đo** và **hướng
mặt sóng** (xem `cs_pacing_mapping_protocol_ensitex.md` §0; bằng chứng REF-034 Butcher, REF-035 Frontera). Cùng
một điểm mô cho trị số khác nhau ở nhịp xoang vs nhịp tạo. Do đó **mọi trị số của các biến đo xâm lấn — dòng #1
AERP, #2 AFCL, #3 SNRT/cSNRT, #4 CV, #5 Voltage/LVZ, #13 Rotor/CFAE — phải ghi kèm khối điều kiện đo dưới đây**;
thiếu khối này thì trị số **không so sánh được** giữa bệnh nhân hay giữa nghiên cứu.

| Trường | Định dạng / giá trị hợp lệ | Ghi chú (khớp protocol) |
|---|---|---|
| **ĐK-1. Nhịp lúc đo** | {Nhịp xoang / Nhịp tạo CS-ngoại kích / Rung nhĩ} | Frontera: mỗi biến có 2 lớp (SR + paced); AF chỉ cho AFCL |
| **ĐK-2. Vị trí tạo nhịp** | {CS đoạn xa (CS 1-2) / khác: ghi rõ} | Protocol §4 — mặc định CS 1-2 |
| **ĐK-3. Kiểu kích thích** | {Ngoại kích sensed đơn / Drive S1S2 / Không tạo nhịp} | Frontera dùng **ngoại kích sensed đơn**, không phải drive S1S2 |
| **ĐK-4. Coupling & ERP** | ERP tại chỗ đo được (ms) · coupling thực (ms) = ERP + 30 ms | Protocol §4 — coupling = ERP tại chỗ + 30 ms |
| **ĐK-5. Hệ thống mapping** | {EnSite X + Advisor FL Circular (bipolar) / EnSite X + HD Grid (OT) / khác} | Lab hiện dùng **EnSite X + Advisor Circular, bipolar (không omnipolar)** |
| **ĐK-6. Cấu hình tín hiệu** | Lọc bipolar (Hz) · ngưỡng LVZ (mV) · mật độ EGM/bản đồ | Mặc định khớp Frontera: **30–300 Hz · <0,5 mV · ≥3000 EGM** |
| **ĐK-7. Phương pháp thu 2 nhịp** | {Cách A — cặp theo vùng, cùng model / Cách B — TurboMap} | Protocol §2: **Cách A là phương pháp chính thức** |
| **ĐK-8. Phân loại bất thường** | {Cố định (fixed) / Chức năng (functional) / Không xác định} | fixed = hiện ở cả 2 nhịp; functional = chỉ 1 nhịp (Frontera) |

**Quy tắc chống-nhiễu-hướng (lab bipolar):** nếu một vùng ghi LVZ (<0,5 mV) ở **chỉ một** nhịp mà bình thường ở
nhịp kia → **đánh dấu ĐK-8 = "chức năng/nghi giả do hướng", KHÔNG ghi là sẹo cố định** (thao tác hóa REF-034).

**Áp dụng theo dòng:** ĐK-1…ĐK-8 bắt buộc cho dòng #4 (CV) và #5 (Voltage/LVZ); ĐK-1…ĐK-4 bắt buộc cho #1 AERP,
#2 AFCL, #3 SNRT/cSNRT (các biến kích thích-phụ thuộc); #13 Rotor/CFAE ghi ĐK-1, ĐK-5, ĐK-6. Các biến ECG bề
mặt (#6–#11) và siêu âm (#12) **không** cần khối này (đo không xâm lấn, không phụ thuộc nhịp tạo/hệ mapping).

---

**Trạng thái:** Cấu trúc 13 dòng × 9 cột đã được người dùng duyệt (2026-06-30). Bảng này là khung CHỐT cho
mục "Bảng biến số đề xuất (CRF)" trong bài tổng quan cuối; synthesis-writer viết phần narrative tương ứng
theo đúng GRADE/ngôn ngữ/ngoại suy ở mỗi dòng, không tự thêm/bớt cột.

**Bổ sung 2026-07-01 (theo yêu cầu người dùng):** thêm **Khối "Điều kiện đo" (ĐK-1…ĐK-8)** để CRF khớp với
protocol tạo nhịp CS trên EnSite X (`cs_pacing_mapping_protocol_ensitex.md`, Cách A). Đây là phần MỞ RỘNG sau
khi cấu trúc gốc 13×9 đã duyệt — không sửa 13 dòng gốc, chỉ thêm khối điều kiện đo áp cho các biến xâm lấn.
