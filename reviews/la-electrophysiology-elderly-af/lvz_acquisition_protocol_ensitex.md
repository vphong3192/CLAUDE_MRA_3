# Protocol lấy LVZ (vùng điện thế thấp) nhĩ trái — EnSite X (Abbott) + Advisor FL Circular (bipolar)

**Phạm vi:** CHỈ bản đồ điện thế lưỡng cực + định lượng LVZ. Đây là bản dùng-ngay, đơn giản hơn protocol
functional-kép (`cs_pacing_mapping_protocol_ensitex.md`). Ngưỡng/giá trị số verbatim từ kho
`reference/la-electrophysiology-elderly-af.md`. **Soạn 2026-07-01.**

Quy ước: "[kho]" = giá trị từ bằng chứng đã lưu · "⚠️[CAS]" = giá trị/menu tùy phiên bản EnSite X, **phải chốt
với ứng dụng viên Abbott** tại lab.

---

## 0. Nguyên tắc cốt lõi (đọc trước khi làm)

LVZ = **% diện tích NT có điện thế lưỡng cực đỉnh-đỉnh < 0,5 mV** [kho: REF-001, REF-002, REF-034]. Ba nguồn
sai số làm **LVZ giả** trên máy bipolar không-lực-tiếp-xúc, xếp theo mức độ:
1. **Tiếp xúc kém** → điện thế thấp giả → LVZ giả *(sai số lớn nhất với Advisor Circular)*.
2. **Nhịp lúc đo** → AF thổi phồng LVZ (66,7% vs 42,4% thực) do va chạm mặt sóng [REF-034].
3. **Nội suy/fill quá rộng** → tô LVZ lên vùng chưa lấy điểm.
→ Toàn bộ protocol này xoay quanh việc **triệt 3 nguồn sai số đó**.

---

## 1. Nhịp lúc đo — quy tắc quyết định

| Tình huống | Xử trí | Ghi CRF |
|---|---|---|
| Bệnh nhân **đang nhịp xoang** | Map **trong nhịp xoang** (ưu tiên) | ĐK-1 = SR |
| Muốn chuẩn hóa hướng mặt sóng | Tạo nhịp **CS đoạn xa cố định** (vd CL 600 ms ⚠️[CAS]), map trong nhịp tạo ổn định | ĐK-1 = paced-CS |
| Bệnh nhân **đang RN, KHÔNG chuyển nhịp** (theo ràng buộc protocol lab) | Vẫn map được nhưng **PHẢI gắn cờ "LVZ đo trong AF — thổi phồng, không phải sẹo thật"**; chỉ dùng mô tả, không dùng làm cơ chất nền sạch | ĐK-1 = AF + cờ artifact [REF-034] |

**Khuyến nghị:** để LVZ có giá trị so sánh, thu **trong nhịp xoang** (tự nhiên hoặc sau chuyển nhịp nếu protocol
cho phép). LVZ đo trong AF chỉ là số mô tả, **không** là substrate thật.

---

## 2. Thiết bị & cấu hình

| Hạng mục | Giá trị | Nguồn |
|---|---|---|
| Hệ thống | EnSite X | — |
| Catheter | **Advisor FL Circular, Sensor Enabled** (loop bipolar) | — |
| Điện thế dùng | **lưỡng cực đỉnh-đỉnh (peak-to-peak)** | chuẩn LVZ |
| Lọc bipolar | **30–300 Hz** | [kho: REF-035] ⚠️[CAS đặt đúng chỗ] |
| Ngưỡng LVZ | **< 0,5 mV** | [kho: REF-001/002/034] |
| Sẹo dày (tùy chọn) | **< 0,1 mV** | pre-specify |
| Bình thường | **≥ 0,5 mV** | — |
| Nội suy/fill tối đa | đặt **bảo thủ** (không tô lên vùng chưa lấy điểm) | ⚠️[CAS — ghi lại giá trị dùng] |
| Thu điểm | **AutoMap** + tiêu chí chấp nhận beat | ⚠️[CAS] |
| Gating | ổn định vị trí + hô hấp | ⚠️[CAS] |

**Đặt ngưỡng thang màu voltage TRƯỚC khi thu** (0,1 / 0,5 mV) và **khóa lại** — không chỉnh thang màu sau khi
nhìn bản đồ (tránh bias điều chỉnh cho ra kết quả mong muốn).

---

## 3. Quy trình thu (từng bước)

1. **Chuẩn bị:** xuyên vách dưới hướng dẫn TEE (loại trừ huyết khối tiểu nhĩ); heparin 100 IU/kg, ACT >280 s.
2. **Dựng model hình học NT** bằng Advisor FL Circular; xác định rõ **ranh giới cần loại** khi tính LVZ: 4 TMP,
   vòng van hai lá, tiểu nhĩ trái (LAA) — đánh dấu ngay trên model.
3. **Chọn nhịp** theo §1; nếu tạo nhịp thì bật máy kích thích CS đoạn xa trước khi thu.
4. **Thu theo VÙNG có hệ thống** (mái → thành trước → vách → thành sau → thành bên → sàn → antra 4 TMP), đảm bảo
   **phủ đều**, không để mảng trống rồi để máy nội suy.
5. **Tại mỗi điểm — kiểm tiếp xúc BẮT BUỘC** (Advisor Circular không có CF):
   - Chỉ báo tiệm cận mô (tissue proximity) dương;
   - Điện đồ **ổn định qua nhiều nhịp** (hình thái không đổi);
   - Loop áp đều, không "trôi";
   - **Loại điểm** nếu điện đồ chỉ có thành phần trường-xa/nhiễu hoặc loop mất áp → **điểm tiếp xúc kém đọc điện
     thế thấp giả là nguyên nhân LVZ giả số 1**.
6. **Mật độ mục tiêu:** phủ dày, đều; benchmark cao-mật-độ **≥3000 EGM** như Frontera [kho: REF-035] — nhưng với
   LVZ, **chất lượng tiếp xúc + độ phủ quan trọng hơn con số điểm thô**. Đặt tối thiểu điểm/vùng ⚠️[CAS].

---

## 4. Kiểm soát chất lượng — chống LVZ giả (bắt buộc trước khi tính)

- [ ] **Không có mảng trống bị nội suy:** mọi vùng LVZ phải có **điểm thật** bao quanh, không phải fill.
- [ ] **Kiểm ngẫu nhiên điện đồ trong vùng LVZ:** mỗi vùng <0,5 mV phải có điện đồ **tiếp xúc tốt thật sự thấp**,
  không phải trường-xa/mất áp. Loại và thu lại nếu nghi tiếp xúc.
- [ ] **Nhịp nhất quán toàn bản đồ** (không lẫn beat AF/ngoại tâm thu vào bản đồ SR).
- [ ] **Thang màu khóa ở 0,1/0,5 mV** từ đầu, không chỉnh sau.
- [ ] **Ghi giá trị nội suy/fill đã dùng** (để tái lập).

---

## 5. Định lượng LVZ (đầu ra)

Báo cáo đồng thời:
1. **LVZ (% diện tích NT)** = diện tích <0,5 mV ÷ tổng diện tích NT, **sau khi loại 4 TMP + vòng van hai lá +
   LAA** (định nghĩa bề mặt nhất quán) — đây là số so sánh chính.
2. **LVZ diện tích tuyệt đối (cm²)**.
3. **Điện thế NT trung bình toàn thể (mV)**.
4. **Phân bố theo vùng** (mái/trước/vách/sau/bên/sàn) — vùng nào chiếm LVZ.
5. (Tùy chọn) **Sẹo dày <0,1 mV (%)**.

---

## 6. Giá trị tham chiếu theo tuổi để đối chiếu (từ kho — verbatim)

| Chỉ số | Giá trị | Nguồn |
|---|---|---|
| Điện thế NT toàn thể, ≥75y vs <75y | **1,5 [1,2–2,3] mV** vs **2,4 [1,7–2,8] mV** (P<0,01) | REF-001 (Marzak) |
| LVZ, ≥75y vs <75y | **67% vs 30%** (P<0,01) | REF-001 |
| Điện thế NT theo thập niên (nhóm AF) | <65y **1,9±0,4** · 65–79y **1,2±0,4** · >80y **1,0±0,4 mV** | REF-002 |
| Điện thế NT theo thập niên (chứng) | <65y **3,4±0,4** · 65–79y **2,8±0,3** · >80y **1,6±0,7 mV** | REF-002 |
| Yếu tố dự báo LVZ | tuổi ≥75, nữ, eGFR, LAVi | REF-001 |

→ Dùng làm mốc: một bệnh nhân ≥75 tuổi RN có LVZ ~**60–70%** và điện thế toàn thể ~**1–1,5 mV** là **phù hợp y
văn**; nếu bản đồ của bạn cho LVZ ~90% thì **nghi tiếp xúc kém/artifact AF** trước khi kết luận "sẹo lan tỏa".

---

## 7. Ghi CRF (khớp khối "Điều kiện đo")

Bắt buộc kèm mỗi bản đồ LVZ: **ĐK-1** (nhịp lúc đo), **ĐK-2** (vị trí tạo nhịp nếu có), **ĐK-5** (hệ thống =
EnSite X + Advisor Circular bipolar), **ĐK-6** (lọc 30–300 Hz · ngưỡng 0,5 mV · mật độ EGM · **giá trị nội suy**),
**ĐK-8** (nếu LVZ chỉ thấy 1 nhịp → cờ functional/nghi giả). Đầu ra §5 nhập vào dòng #5 (Voltage/LVZ) của CRF.

---

## 8. Danh mục chốt với ứng dụng viên Abbott trước khi chạy
1. Chỗ đặt **lọc lưỡng cực 30–300 Hz**.
2. **Giá trị nội suy/fill tối đa** khuyến nghị cho tính diện tích LVZ (và cách khóa nó).
3. **Tiêu chí chấp nhận beat trong AutoMap** để loại điểm tiếp xúc kém tự động.
4. Cách **loại trừ TMP/van/LAA** khỏi phép tính diện tích bề mặt.
5. Đặt & **khóa thang màu voltage** ở 0,1/0,5 mV.

---

## 9. Nguồn
- REF-001 Marzak 2024, Heart Rhythm O2 (LVZ <0,5 mV; giá trị theo tuổi). DOI 10.1016/j.hroo.2024.12.006.
- REF-002 (điện thế NT theo thập niên; EnSite NAVX; LVZ <0,5 mV). DOI 10.3389/fcvm.2020.615065.
- REF-034 Butcher 2023, JACC CE (bipolar-trong-AF thổi phồng LVZ 66,7% vs 42,4%). PMID 37204357.
- REF-035 Frontera 2025, Heart Rhythm (lọc 30–300 Hz; benchmark ≥3000 EGM). PMID 39278611.

Kho đầy đủ: `reference/la-electrophysiology-elderly-af.md`.
