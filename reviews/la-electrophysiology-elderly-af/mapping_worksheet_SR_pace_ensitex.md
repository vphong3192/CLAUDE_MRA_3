# Bảng công tác mapping NHỊP XOANG + NHỊP TẠO (SR + pace) — EnSite X / Advisor FL Circular

**Dùng khi:** đã **sốc điện về xoang trước**, rồi map **trong nhịp xoang (SR)** và **trong nhịp tạo CS (pace)**
trên **cùng một model geometry đã khóa** (Cách A). Không map trong AF (nên **AFCL không áp dụng** ở đây).

**Đây là bản điền-tại-bàn**, rút gọn từ `cs_pacing_mapping_protocol_ensitex.md` (§4 tạo nhịp, §6 quy trình, §7
định nghĩa, §7b biến số) và khớp khối "Điều kiện đo" (ĐK-1…ĐK-9) trong `crf_table_with_measurement_conditions.md`.

**Quy ước cờ:** [Frontera] = giá trị verbatim từ full-text REF-035; [kho] = từ `reference/…` (REF-001/002/003);
⚠️CAS = tên menu/tính năng phụ thuộc phiên bản EnSite X → **chốt với ứng dụng viên Abbott trước khi chạy**.

---

## A. Thứ tự thao tác (rút gọn — 6 bước)

1. **Sốc điện về xoang.** Ghi **ĐK-9** = số phút từ lúc sốc đến khi bắt đầu map SR (phù nề sau sốc có thể hạ điện thế/CV thoáng qua).
2. **Dựng & KHÓA một model hình học NT** (Advisor FL Circular, Sensor Enabled). **Không** tạo geometry mới cho lớp pace — dùng chung để đồng đăng ký point-by-point. ⚠️CAS (field scaling/geometry lock).
3. **Đặt cấu hình tín hiệu:** lọc lưỡng cực **30–300 Hz**; ngưỡng LVZ **< 0,5 mV**; mục tiêu mật độ **≥ 3000 EGM/bản đồ**. [Frontera] · ⚠️CAS (chỗ đặt trong amplifier)
4. **Đo ERP tại chỗ** bằng ngoại kích **sensed** từ **CS 1-2**; coupling nhịp tạo = **ERP tại chỗ + 30 ms** (một beat sớm, KHÔNG phải drive S1S2). [Frontera]
5. **Đi theo TỪNG vùng (Cách A):** với mỗi vùng → thu **SR** đủ mật độ → **chuyển ngay sang pace CS** thu lại **đúng vùng đó** → chỉ khi đủ cả 2 lớp mới sang vùng kế. Ghi thứ tự vùng + dấu thời gian mỗi lớp.
6. **Đối chiếu 2 bản đồ** (SR vs pace) bằng isochrone/propagation; 2 người đọc, bất đồng → người thứ ba đọc mù. [Frontera]

**7 vùng giải phẫu chuẩn (điền cho MỖI vùng):**
**① Trần (mái)** · **② Thành trước** · **③ Thành sau** · **④ Vách (septum)** · **⑤ Thành bên (lateral)** ·
**⑥ Antra 4 TMP** (LSPV · LIPV · RSPV · RIPV) · **⑦ Sàn (floor)**.

---

## B. Biến số nên lấy — theo NHÓM PHÁT HIỆN (điền cả cột SR và cột Pace)

> Mọi trị số phải kèm khối Điều kiện đo (nhịp, CS 1-2, coupling ERP+30 ms, Advisor bipolar, 30–300 Hz, <0,5 mV, ĐK-9). Điền "—" nếu vùng chưa thu.

### 1) Điện thế & Vùng điện thế thấp (LVZ)  — *gồm "LVZ xoang" và "LVZ pace"*

| Vùng | Điện thế trung vị — **SR** (mV) | Điện thế trung vị — **Pace** (mV) | **LVZ xoang** <0,5 mV (có/không · % vùng) | **LVZ pace** <0,5 mV (có/không · % vùng) | Nghi giả do hướng? (chỉ 1 nhịp) |
|---|---|---|---|---|---|
| ① Trần (mái) |  |  |  |  |  |
| ② Thành trước |  |  |  |  |  |
| ③ Thành sau |  |  |  |  |  |
| ④ Vách |  |  |  |  |  |
| ⑤ Thành bên |  |  |  |  |  |
| ⑥ Antra 4 TMP |  |  |  |  |  |
| ⑦ Sàn |  |  |  |  |  |

*Lấy thế nào:* bản đồ **voltage** EnSite X, đọc biên độ đỉnh–đỉnh mỗi điểm → **trung vị theo vùng**; công cụ **area** đặt ngưỡng <0,5 mV → **% diện tích vùng** và toàn NT. ⚠️CAS (menu voltage/area).

### 2) Vùng dẫn truyền chậm

| Vùng | Corridor chậm — **SR** (có/không) | CV tối thiểu — **SR** (m/s) | Corridor chậm — **Pace** (có/không) | CV tối thiểu — **Pace** (m/s) | Vị trí **pivot** (nếu có) |
|---|---|---|---|---|---|
| ① Trần (mái) |  |  |  |  |  |
| ② Thành trước |  |  |  |  |  |
| ③ Thành sau |  |  |  |  |  |
| ④ Vách |  |  |  |  |  |
| ⑤ Thành bên |  |  |  |  |  |
| ⑥ Antra 4 TMP |  |  |  |  |  |
| ⑦ Sàn |  |  |  |  |  |

*Lấy thế nào:* bản đồ **activation isochrone** — nơi **isochrone chụm sát/giảm tốc** = corridor dẫn truyền chậm; **CV** = gradient LAT / khoảng cách giữa điểm vào–ra vùng chậm (hoặc mô-đun CV nếu phiên bản có). ⚠️CAS (isochrone spacing/CV). *Mốc [Frontera]: CV tại vị trí chức năng bất thường **0,52±0,17 m/s**.*

### 3) Vùng điện thế phân mảnh (fractionated)

| Vùng | Phân mảnh — **SR** (có/không) | Phân mảnh — **Pace** (có/không) | CFE-mean (ms, nếu có bản đồ CFE) | Thời lượng EGM: corridor / pivot (ms) |
|---|---|---|---|---|
| ① Trần (mái) |  |  |  |  |
| ② Thành trước |  |  |  |  |
| ③ Thành sau |  |  |  |  |
| ④ Vách |  |  |  |  |
| ⑤ Thành bên |  |  |  |  |
| ⑥ Antra 4 TMP |  |  |  |  |
| ⑦ Sàn |  |  |  |  |

*Định nghĩa [Frontera]:* phân mảnh = EGM có **>3 deflection**; corridor **~47±10 ms** vs pivot **~35±5 ms** (P<0,001). CFE-mean lấy từ bản đồ CFE nếu phiên bản có. ⚠️CAS.

### 4) Tổng hợp fixed / functional (DẪN XUẤT — so 2 lớp SR↔Pace, ghi tên 2 người đọc)

| Vùng | Bất thường xuất hiện ở | Phân loại | Điện thế tại vị trí chức năng có bình thường? |
|---|---|---|---|
|  | {SR only / Pace only / Cả hai / Không} | {**fixed** = cả hai / **functional** = chỉ 1 nhịp / **nghi giả do hướng**} | (có/không) |
| ① Trần (mái) |  |  |  |
| ② Thành trước |  |  |  |
| ③ Thành sau |  |  |  |
| ④ Vách |  |  |  |
| ⑤ Thành bên |  |  |  |
| ⑥ Antra 4 TMP |  |  |  |
| ⑦ Sàn |  |  |  |

**Quy tắc đọc (thao tác hóa REF-034):** bất thường/LVZ **chỉ thấy ở MỘT nhịp** mà bình thường ở nhịp kia →
ghi **"functional / nghi giả do hướng"**, **KHÔNG** ghi là sẹo cố định cho tới khi xác nhận ở cả hai nhịp.

---

## C. Biến cấp BẢN ĐỒ / BỆNH NHÂN (điền 1 lần)

| Biến | SR | Pace | Ghi chú |
|---|---|---|---|
| Số EGM/bản đồ (QC **≥3000**) |  |  | mục tiêu [Frontera] |
| LVZ % diện tích **toàn NT** (<0,5 mV) |  |  | so SR vs pace để bắt LVZ chức năng |
| Diện tích bề mặt NT (cm²) | (model chung) | — | mẫu số cho %LVZ |
| Tổng số vị trí **fixed** / **functional** |  | — | dẫn xuất (mục 4) |
| % vị trí functional có điện thế **bình thường** |  | — | mốc [Frontera]: **~88%** |
| ĐK-9: thời gian sốc → bắt đầu map SR (phút) |  | — | phù nề sau sốc |

---

## D. Mốc tham chiếu để đối chiếu (KHÔNG phải ngưỡng bắt buộc)

- **Điện thế lưỡng cực NT theo tuổi [kho]:** ~**1,5 mV** ở **≥75 tuổi** vs ~2,4 mV ở <75; theo thập niên **1,0±0,4 mV** ở **≥80 tuổi** (REF-001/002/003).
- **LVZ theo tuổi [kho]:** **~67%** (≥75t) vs ~30% (<75t) có LVZ đáng kể (REF-001/002).
- **CV [kho/Frontera]:** giảm theo tuổi (r≈−0,77…−0,79, nhịp xoang, không-RN, REF-074); CV thấp ở vùng phân mảnh **46,0 vs 64,5 cm/s** [kho]; vị trí chức năng bất thường **0,52±0,17 m/s** [Frontera].
- **Vì sao cần cả 2 nhịp [Frontera]:** ~**88%** vị trí chức năng có **điện thế bipolar bình thường** → chỉ map điện thế nhịp xoang **bỏ sót phần lớn** cơ chất chức năng.

---

## E. Nhắc an toàn
- Ngoại kích/thao tác có thể khởi phát RN → chuyển nhịp điện đồng bộ, ổn định xoang, tiếp tục; ghi lại (ảnh hưởng ĐK-9 nếu phải sốc lại). ACT >280 s; theo dõi nhiệt độ thực quản khi quét thành sau. [Frontera + thích ứng]

---

## F. Nguồn
- Frontera A, et al. Heart Rhythm 2025;22:1401–1410. PMID 39278611. **[REF-035]** — dual-rhythm functional mapping.
- Butcher C, et al. JACC Clin Electrophysiol 2023;9(8 Pt 2):1500–12. PMID 37204357. **[REF-034]** — LVZ giả do hướng trên bản đồ bipolar.
- Điện thế/LVZ theo tuổi: **REF-001, REF-002, REF-003** (kho `reference/la-electrophysiology-elderly-af.md`).
