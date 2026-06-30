# Bảng biến số đề xuất (CRF) — bản nháp để người dùng duyệt trước Phase 5

**Mục đích:** Đây là bảng biến số/CRF cho nghiên cứu mô tả thông số điện học/điện sinh lý nhĩ trái ở
bệnh nhân RN cao tuổi — một trong hai mục tiêu đã khóa ở Phase 0 (tổng quan tường thuật + bảng CRF).
Nguồn: `_workspace/04_appraisal.md` (GRADE, RoB, evidence-table), kho `reference/la-electrophysiology-elderly-af.md`.

**Quy ước cột:**
- **Khả thi:** EP xâm lấn (cần phòng EP-lab) / ECG bề mặt (không xâm lấn) / Cần thiết bị đặc biệt (SAECG, omnipolar, CARTO).
- **Mức bằng chứng:** GRADE theo nhóm thông số (§3, `04_appraisal.md`).
- Mọi giá trị số trong bảng là verbatim từ kho, không tự suy diễn.

---

| # | Nhóm thông số | Định nghĩa / Đơn vị | Phương pháp đo | Khả thi | Xu hướng/giá trị tham chiếu theo tuổi (nếu có) | GRADE | Bằng chứng neo |
|---|---|---|---|---|---|---|---|
| 1 | **AERP** (Atrial Effective Refractory Period) | Thời gian trơ hiệu lực nhĩ, ms | Kích thích theo chương trình (S1S2), đo tại CS/RA/LA | EP xâm lấn | ↑ theo tuổi ở quần thể không-RN (r=0,56, p<0,01); AERP≥280ms → RN mới aHR 2,08; **giá trị tuyệt đối trong RN ở người cao tuổi: KHÔNG XÁC ĐỊNH** (nghịch lý rút ngắn-do-nhịp-nhanh vs kéo dài-do-xơ hóa) | **Low** | REF-042, 043, 041, 044, 045, 048 |
| 2 | **AFCL** (AF Cycle Length) | Khoảng cách giữa các sóng rung nhĩ liên tiếp trong RN đang diễn ra, ms | Điện đồ nội mạc (thường tại CS) trong lúc RN | EP xâm lấn | Baseline chung (không phân tầng tuổi, TB 53y): 186±19ms (REF-073); **KHÔNG có dữ liệu phân tầng theo tuổi nào trong y văn đã tìm được** | **Very Low / GAP** | REF-073 (chỉ baseline chung — gắn nhãn rõ "không age-stratified") |
| 3 | **SNRT / cSNRT** (Sinus Node Recovery Time, hiệu chỉnh) | Thời gian phục hồi nút xoang sau kích thích vượt tần số, ms | Overdrive pacing, đo khoảng nghỉ xoang đầu tiên | EP xâm lấn | cSNRT trong RN dai dẳng 606ms → 408ms sau 1 tháng chuyển nhịp (đảo ngược); chưa có chuẩn theo tuổi | **Low** | REF-047, 049, 042 |
| 4 | **CV** (Conduction Velocity) | Vận tốc dẫn truyền xung động nhĩ, cm/s hoặc m/s | Mapping điện giải phẫu (CARTO/EnSite), đo giữa 2 điểm/khoảng cách-thời gian | EP xâm lấn, cần thiết bị mapping | Giảm theo tuổi: WPV nghịch r=-0,77 (RA)/-0,79 (LA), P<0,0001 (nhịp xoang, không-RN); CV thấp ở vùng phân mảnh điện thế (46,0 vs 64,5cm/s) | **Low** | REF-074, 003, 051, 052 (đo trong **nhịp xoang**, ngoại suy sang RN — xem Hạn chế A-1) |
| 5 | **Voltage nhĩ trái (bipolar/unipolar) & LVZ** | Biên độ điện thế nội mạc, mV; LVZ = % diện tích <0,5mV | Mapping điện giải phẫu biên độ-điện thế (voltage map) | EP xâm lấn, cần thiết bị mapping | ↓ rõ theo tuổi: 1,5mV (≥75y) vs 2,4mV (<75y); LVZ 67% vs 30%; theo thập niên: 1,0±0,4mV (≥80y) | **Moderate** | REF-001, 002, 042, 003 |
| 6 | **PWD** (P-wave Duration) | Thời gian sóng P trên ECG 12 chuyển đạo, ms | Đo thủ công/tự động ECG bề mặt | ECG bề mặt | Tăng theo tuổi (103,5ms ở ≥60y vs 91,4ms ở ≤30y); ngưỡng ≥110ms dự báo RN (Se88/Sp75); PWD>120ms → tái phát sau cắt đốt OR 2,04 | **Moderate** | REF-042, 037, 039, 059 |
| 7 | **P-wave dispersion** | Chênh lệch PWD lớn nhất–nhỏ nhất giữa các chuyển đạo, ms | Đo PWD 12 chuyển đạo, tính hiệu số | ECG bề mặt | PWD≥40ms dự báo PAF (Se83/Sp85); **bias công bố đã xác nhận** (Egger p=0,01); ES nhạy với loại bỏ outlier (0,7→0,1) | **Low** | REF-059, 058, 061 |
| 8 | **SAECG filtered P-wave** | Thời gian sóng P lọc nhiễu tần số cao, ms | Signal-averaged ECG (kỹ thuật chuyên biệt) | Cần thiết bị đặc biệt (ít dùng lâm sàng hiện nay) | Ngưỡng 120–155ms tùy nghiên cứu dự báo PAF/POAF (Se80–91%); MA lớn N=20.201, ES=0,8 cho SAECG-PWD | **Moderate** (nhưng công nghệ cũ) | REF-053, 054, 055, 058 |
| 9 | **IAB / Hội chứng Bayés** (Interatrial Block) | Block dẫn truyền liên nhĩ qua bó Bachmann; PWD≥120ms (partial), ±dạng hai pha ở DII/III/aVF (advanced) | ECG 12 chuyển đạo, phân loại theo tiêu chuẩn ISE/ISHNE | ECG bề mặt | Phổ biến tăng rõ theo tuổi (~1% chung → 9–10% cao tuổi, 20–26% rất cao tuổi); aIAB → RN HR 2,7–4,9 (trực tiếp ở ≥70y, BAYES registry) | **Moderate** (nhóm mạnh nhất) | REF-066, 068, 063, 064, 069 |
| 10 | **P-wave axis** | Trục điện học sóng P trên mặt phẳng trán, độ (°) | Đo ECG 12 chuyển đạo (chuyển đạo chi) | ECG bề mặt | Trục bất thường → RN: OR 2,12 (Abstract) / 2,10 (Kết quả) — **mâu thuẫn nội tại nguồn, trích cả hai** | **Moderate** | REF-070, 064 |
| 11 | **PTFV1** (P-terminal Force in V1) | Diện tích pha âm sóng P ở V1, mm·s | Đo ECG chuyển đạo V1 | ECG bề mặt | >0,04mm·s → RN OR 1,39 (ngưỡng gốc Morris >0,03mm·s — chưa thống nhất) | **Low** | REF-040, 064 |
| 12 | **LA strain (hồ chứa)** | Biến dạng cơ học nhĩ trái thì hồ chứa, % | Siêu âm tim đánh dấu mô (STE) | Không xâm lấn (siêu âm) | ↓ theo tuổi (β=-0,37%/năm); <65y 24,6% vs ≥65y 17,8%; dự báo RN mới HR 1,80 | **Moderate** | REF-023, 025, 024 |
| 13 | **Rotor / CFAE** *(đề cập ngắn theo phạm vi đã thống nhất)* | Nguồn khu trú/điện đồ phân mảnh phức tạp trong RN | Mapping FIRM hoặc phân tích điện đồ CFAE | EP xâm lấn, cần thiết bị mapping | Khái niệm cơ chế lịch sử quan trọng nhưng **RCT chất lượng cao (STAR AF II) bác bỏ giá trị hướng dẫn cắt đốt thêm vào PVI** | **Moderate (âm tính)** | REF-005, 010 |

---

## Cột bổ sung đề xuất (chờ ý kiến người dùng)

Các cột sau **chưa đưa vào bảng trên** — hỏi trước khi viết bản đầy đủ:
1. **"Ngoại suy/giả định"** — đánh dấu các dòng dựa trên dữ liệu không-RN/nhịp xoang ngoại suy sang RN cao tuổi (AERP, CV — theo Assumption Register A-1/A-3). Có muốn thêm cột riêng, hay ghi trong cột "Xu hướng" như hiện tại đủ?
2. **"Trạng thái ở Việt Nam"** — phần lớn thông số chưa có dữ liệu chuẩn Việt Nam (population gap A-8); có muốn một cột/dòng ghi chú riêng?
3. Có muốn tách AFCL ra thành dòng "highlight" riêng (in đậm/khung cảnh báo) trong bài để nhấn mạnh đây là gap, thay vì chỉ một dòng trong bảng?

---

**Trạng thái:** Đây là bản nháp 13 dòng phản ánh đúng evidence-table đã thẩm định ở Phase 4. Nếu được duyệt
(có/không chỉnh sửa), bảng này sẽ là khung cho mục "Bảng biến số đề xuất (CRF)" trong bài tổng quan cuối,
và synthesis-writer sẽ viết phần narrative tương ứng theo đúng GRADE/ngôn ngữ ở mỗi dòng.
