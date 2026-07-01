# Bảng công tác mapping NHỊP XOANG + NHỊP TẠO (SR + pace) — EnSite X / Advisor FL Circular

**Dùng khi:** đã **sốc điện về xoang trước**, rồi map **trong nhịp xoang (SR)** và **trong nhịp tạo CS (pace)**
trên **cùng một model geometry đã khóa** (Cách A). Không map trong AF (nên **AFCL không áp dụng** ở đây).

Rút gọn từ `cs_pacing_mapping_protocol_ensitex.md` và khớp khối "Điều kiện đo" (ĐK-1…ĐK-9) trong
`crf_table_with_measurement_conditions.md`. Số liệu tham chiếu **verbatim từ Frontera** (REF-035, Heart Rhythm
2025;22:1401–1410, PMID 39278611). Cờ: [Frontera] = từ full-text · [kho] = REF-001/002/003 · ⚠️CAS = menu/tính
năng phụ thuộc phiên bản EnSite X, **chốt với ứng dụng viên Abbott trước khi chạy**.

---

## ⭐ 0. NGUYÊN TẮC CỐT LÕI — đọc trước khi vào bàn

**Bất thường được TÌM bằng bản đồ HOẠT HÓA (activation/isochrone), KHÔNG phải bản đồ điện thế.** Frontera chỉ
định nghĩa **hai loại bất thường**: **điểm xoay (pivot)** và **hành lang dẫn truyền chậm (corridor)** — đọc trên
kiểu lan truyền của sóng, ở **cả hai nhịp**, rồi so để phân **cố định (fixed)** vs **chức năng (functional)**.

- **Điện thế / LVZ = số đo MÔ TẢ đi kèm, KHÔNG dùng để sàng lọc bất thường.** Bằng chứng: **88% vị trí chức năng
  có điện thế BÌNH THƯỜNG** [Frontera] → map điện thế đơn thuần **bỏ sót phần lớn**. Đo điện thế để *mô tả* vị trí
  đã tìm được, không phải để đi tìm nó.
- **Điện thế phân mảnh KHÔNG phải tiêu chí** trong nghiên cứu này → xếp mục **tùy chọn** (§G).
- **Vì sao cần 2 nhịp:** một bất thường chỉ hiện ở một nhịp = **chức năng** (được "mở khóa" bởi nhịp tạo coupling
  ngắn); hiện ở cả hai = **cố định** (sẹo thật).

**Thứ tự ưu tiên khi đọc bản đồ:** ① Hoạt hóa (pivot + corridor) → ② Phân loại fixed/functional → ③ Đo mô tả
(điện thế, CV, thời lượng EGM) → ④ (tùy chọn) phân mảnh.

---

## A. Thứ tự thao tác (6 bước)

1. **Sốc điện về xoang.** Ghi **ĐK-9** = số phút từ lúc sốc đến khi bắt đầu map SR (phù nề sau sốc có thể hạ điện thế/CV thoáng qua).
2. **Dựng & KHÓA một model hình học NT** (Advisor FL Circular, Sensor Enabled). Không tạo geometry mới cho lớp pace — dùng chung để đồng đăng ký point-by-point. ⚠️CAS (field scaling / geometry lock).
3. **Cấu hình tín hiệu:** lọc lưỡng cực **30–300 Hz**; ngưỡng LVZ **< 0,5 mV**; mật độ **≥ 3000 EGM/bản đồ** (Frontera trung bình 4806±1315). [Frontera] · ⚠️CAS.
4. **Đo ERP tại chỗ** bằng ngoại kích **sensed** từ **CS 1-2**; coupling nhịp tạo = **ERP tại chỗ + 30 ms** (một beat sớm, KHÔNG phải drive S1S2). [Frontera]
5. **Đi theo TỪNG vùng (Cách A):** mỗi vùng → thu **bản đồ hoạt hóa SR** đủ mật độ → **chuyển ngay sang pace CS** thu lại **đúng vùng đó** → đủ cả 2 lớp mới sang vùng kế. Ghi thứ tự vùng + dấu thời gian.
6. **Phân tích isochrone** trên 2 propagation (SR vs paced) để tìm pivot + corridor; **2 người đọc**, bất đồng → **người thứ 3 đọc mù**. [Frontera]

**7 vùng giải phẫu chuẩn:** **① Trần (mái)** · **② Thành trước** · **③ Thành sau** · **④ Vách** · **⑤ Thành bên** ·
**⑥ Antra 4 TMP** (LSPV·LIPV·RSPV·RIPV) · **⑦ Sàn**.

---

## B. HAI LOẠI BẤT THƯỜNG — ĐỊNH NGHĨA CỤ THỂ (phần quan trọng nhất)

**Mốc "bình thường" để so:** *hoạt hóa bình thường = mặt sóng lan ĐỀU, các đường isochrone song song – cách đều,
đi theo MỘT hướng chính* [Frontera]. Bất thường = **kiểu lan truyền thay đổi**. Chỉ có 2 loại:

### ① ĐIỂM XOAY — PIVOT
- **Định nghĩa [Frontera]:** vùng khu trú nơi **mặt sóng bẻ hướng** (xoay **theo hoặc ngược chiều kim đồng hồ**),
  hướng đi mới **lệch > 45°** so với hướng tới.
- **Nhìn thấy gì trên EnSite:** các đường isochrone **quạt/xoay quanh một điểm**; mũi tên lan truyền đổi hướng rõ (>45°).
- **Ý nghĩa lâm sàng:** điểm sóng "rẽ" — có thể là **neo cho vòng vào lại**.
- **Điện thế điển hình tại pivot [Frontera]:** ~**1,75 ± 0,51 mV** (thường CAO hơn corridor) · thời lượng EGM ngắn hơn **~35 ± 5 ms**.

### ② HÀNH LANG DẪN TRUYỀN CHẬM — SLOW-CONDUCTION CORRIDOR
- **Định nghĩa [Frontera]:** dải mô nơi sóng đi chậm — cụ thể **> 3 đường isochrone chụm trong bán kính 1 cm**.
- **Nhìn thấy gì trên EnSite:** vùng đường isochrone **dồn/chen sát nhau (crowding)**; **CV thấp** tại đó. ⚠️CAS (isochrone spacing).
- **Ý nghĩa lâm sàng:** đường dẫn chậm — **chất nền cho vào lại**.
- **Số đo điển hình tại corridor [Frontera]:** CV ~**0,52 ± 0,17 m/s** · thời lượng EGM dài hơn **~47 ± 10 ms** · điện thế ~**0,73 ± 0,47 mV**.

> **Cả pivot lẫn corridor đều tìm trên bản đồ HOẠT HÓA, ở CẢ hai nhịp (SR và pace).** Điện thế bên dưới chỉ để mô tả.

---

## C. BẢNG ĐIỀN CHÍNH — bất thường hoạt hóa theo VÙNG × NHỊP

Với mỗi vùng, đánh **có/không** cho pivot và corridor, **riêng cho SR và cho pace**. Điền "—" nếu chưa thu.

| Vùng | Pivot — **SR** | Corridor chậm — **SR** | Pivot — **Pace** | Corridor chậm — **Pace** |
|---|---|---|---|---|
| ① Trần (mái) |  |  |  |  |
| ② Thành trước |  |  |  |  |
| ③ Thành sau |  |  |  |  |
| ④ Vách |  |  |  |  |
| ⑤ Thành bên |  |  |  |  |
| ⑥ Antra 4 TMP |  |  |  |  |
| ⑦ Sàn |  |  |  |  |

*Gợi ý phân bố [Frontera]: functional hay gặp ở* ***thành trước (bộc lộ trong SR)*** *và* ***antra TMP (bộc lộ trong pace)****; thành sau 25,6%, vách 18,4%.*

---

## D. PHÂN LOẠI cố định / chức năng (per vị trí bất thường) — DẪN XUẤT

Với **mỗi vị trí bất thường** tìm được ở §C, đối chiếu 2 nhịp theo **3 hành vi [Frontera]**:
**(A)** bất thường **chỉ** ở nhịp xoang · **(B)** **chỉ** ở nhịp tạo · **(C)** ở **cả hai**.
→ **Functional (chức năng) = A hoặc B** · **Fixed (cố định) = C**.

| Vị trí bất thường (vùng + loại) | Xuất hiện ở | Phân loại | Ghi chú nghi giả do hướng? |
|---|---|---|---|
|  | {SR only (A) / Pace only (B) / Cả hai (C)} | {**functional** = A/B · **fixed** = C} | (có/không) |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

**Quy tắc chống-nhiễu-hướng (lab bipolar, thao tác hóa REF-034):** một bất thường/LVZ **chỉ thấy ở MỘT nhịp** mà
bình thường ở nhịp kia → có thể là **functional THẬT** *hoặc* **giả do hướng mặt sóng đập vào điện cực**. **KHÔNG**
ghi là sẹo cố định; đánh dấu để soi lại (đổi hướng tạo nhịp/điểm nhìn nếu nghi ngờ).

---

## E. SỐ ĐO MÔ TẢ tại mỗi vị trí bất thường (thứ cấp — không dùng để sàng lọc)

Sau khi đã xác định vị trí bằng hoạt hóa, đo thêm để mô tả. **Lưu ý: điện thế tại đây THƯỜNG BÌNH THƯỜNG** (88%).

| Vùng / vị trí | Điện thế lưỡng cực (mV) — SR / Pace | CV tối thiểu (m/s) — SR / Pace | Thời lượng EGM (ms) — corridor / pivot | Trong vùng điện thế thấp <0,5 mV? |
|---|---|---|---|---|
| ① Trần (mái) |  |  |  |  |
| ② Thành trước |  |  |  |  |
| ③ Thành sau |  |  |  |  |
| ④ Vách |  |  |  |  |
| ⑤ Thành bên |  |  |  |  |
| ⑥ Antra 4 TMP |  |  |  |  |
| ⑦ Sàn |  |  |  |  |

*Mốc [Frontera]: mọi vị trí bất thường điện thế TB 1,25±0,59 mV; pivot 1,75±0,51 vs corridor 0,73±0,47 (P<0,001); CV corridor 0,52±0,17 m/s; EGM corridor 47±10 vs pivot 35±5 ms (P<0,001).*

---

## F. (TÙY CHỌN) Điện thế phân mảnh — KHÔNG phải tiêu chí Frontera

Chỉ ghi nếu lab muốn dữ liệu thêm; **không** dùng để định nghĩa bất thường trong thiết kế này.
- Phân mảnh = EGM có **>3 deflection**; CFE-mean theo vùng nếu phiên bản có bản đồ CFE. ⚠️CAS.

| Vùng | Phân mảnh — SR (có/không) | Phân mảnh — Pace (có/không) | CFE-mean (ms) |
|---|---|---|---|
| (điền theo vùng nếu làm) |  |  |  |

---

## G. Biến cấp BẢN ĐỒ / BỆNH NHÂN (điền 1 lần)

| Biến | SR | Pace | Ghi chú |
|---|---|---|---|
| Số EGM/bản đồ (QC **≥3000**) |  |  | Frontera TB 4806±1315 |
| Diện tích bề mặt NT (cm²) | (model chung) | — | mẫu số cho %LVZ |
| %LVZ toàn NT (<0,5 mV) |  |  | mô tả, không sàng lọc |
| Tổng số vị trí **fixed** / **functional** |  | — | dẫn xuất (§D) |
| % vị trí functional có điện thế **bình thường** |  | — | mốc [Frontera] ~88% |
| **Số vị trí functional còn NGOÀI vòng PVI ("residual")** |  | — | xem ghi chú dưới |
| ĐK-9: thời gian sốc → bắt đầu map SR (phút) |  | — | phù nề sau sốc |

> **Ghi chú "residual" (tránh hiểu nhầm map 2 lần):** Frontera map **MỘT lần, TRƯỚC đốt** (2 lớp nhịp SR + pace).
> Sau đó làm **PVI wide antral tiêu chuẩn**. "Residual" = số vị trí **functional nằm NGOÀI đường đốt** (PVI không
> phủ tới) — **không** phải map lại sau đốt. Chính con số residual này tiên lượng tái phát (HR đa biến 2,539
> [1,458–4,420]; P=0,001) [Frontera]. Nếu bạn muốn map xác nhận sau đốt → **tùy chọn thêm**, và cảnh giác nhiễu
> do phù nề/tổn thương sau đốt.

---

## H. Mốc tham chiếu tổng (đối chiếu, KHÔNG phải ngưỡng bắt buộc)

- **Gánh nặng [Frontera]:** 234 bất thường (3,7±1,6/BN); **functional 53,4%**, fixed 46,6%; PsAF nhiều functional hơn PAF.
- **Điện thế NT theo tuổi [kho]:** ~1,5 mV (≥75t) vs 2,4 mV (<75t); 1,0±0,4 mV (≥80t) — REF-001/002/003.
- **CV [kho]:** giảm theo tuổi; thấp ở vùng phân mảnh 46,0 vs 64,5 cm/s.
- **Điểm nhấn phương pháp [Frontera]:** 88% functional có điện thế bình thường; chỉ 18,4% bất thường trùng LVA → **phải dùng bản đồ hoạt hóa 2 nhịp, không dựa điện thế**.

---

## I. Nhắc an toàn
- Ngoại kích/thao tác có thể khởi phát RN → chuyển nhịp điện đồng bộ, ổn định xoang, tiếp tục (ghi lại; ảnh hưởng ĐK-9 nếu phải sốc lại). ACT >280 s; theo dõi nhiệt độ thực quản khi quét thành sau. [Frontera + thích ứng]

---

## J. Nguồn
- Frontera A, et al. Heart Rhythm 2025;22:1401–1410. PMID 39278611. **[REF-035]** — định nghĩa pivot/corridor, phân loại fixed/functional, residual tiên lượng tái phát.
- Butcher C, et al. JACC Clin Electrophysiol 2023;9(8 Pt 2):1500–12. PMID 37204357. **[REF-034]** — LVZ giả do hướng trên bản đồ bipolar (§D).
- Điện thế/LVZ theo tuổi: **REF-001, REF-002, REF-003** (kho `reference/la-electrophysiology-elderly-af.md`).
