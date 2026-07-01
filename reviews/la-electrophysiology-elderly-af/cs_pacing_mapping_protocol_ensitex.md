# Protocol bản đồ cơ chất chức năng NT — thích ứng cho EnSite X (Abbott) + Advisor Circular (bipolar, KHÔNG omnipolar)

**Phái sinh từ:** `cs_pacing_mapping_protocol.md` (tái dựng Frontera A và cs., Heart Rhythm 2025;22:1401–1410,
PMID 39278611, **[REF-035]**). Tài liệu này **chỉ đổi phần hệ thống mapping** (CARTO/Pentaray → EnSite X/Advisor
FL Circular); phần **tạo nhịp CS, định nghĩa fixed/functional, ngưỡng điện thế** giữ nguyên theo Frontera.

**Soạn:** 2026-07-01. Quy ước: "[Frontera]" = verbatim từ full-text; "[thích ứng EnSite]" = điều chỉnh hệ
thống của người soạn; "⚠️[chốt với CAS]" = giá trị/tên tính năng tùy phiên bản phần mềm, **phải xác nhận với
ứng dụng viên (clinical application specialist) Abbott** trước khi chạy — không lab nào chạy protocol mới mà
không có CAS tại chỗ.

---

## 0. Vì sao thiếu omnipolar KHÔNG chặn phương pháp này

- Frontera đo **bipolar** (lọc 30–300 Hz), **không** omnipolar. [Frontera]
- Phụ-thuộc-hướng của điện thế bipolar được **bù bằng thiết kế 2-nhịp** (đo 2 hướng mặt sóng rồi so), **không**
  bằng omnipolar. Advisor FL Circular (bipolar) là **đủ** cho phương pháp này.
- **Hệ quả duy nhất cần xử lý:** một "vùng điện thế thấp" thấy ở **chỉ một** nhịp mà bình thường ở nhịp kia →
  nhiều khả năng là **giả do va chạm/hướng mặt sóng (hoặc functional)**, KHÔNG phải sẹo cố định. Đây chính là
  phát hiện Butcher 2023 [REF-034] — và bản đồ kép của bạn **tự phát hiện được điều này**, đó là ưu điểm.
- (Tùy chọn) Nếu thỉnh thoảng mượn được **Advisor HD Grid**, có thể dùng riêng nó cho **bản đồ điện thế** để có
  omnipolar (OT) giảm nhiễu hướng; nhưng KHÔNG bắt buộc để chạy phương pháp chức năng.

---

## 1. Ánh xạ thiết bị CARTO → EnSite X

| Hạng mục | Frontera (CARTO) | Thích ứng EnSite X |
|---|---|---|
| Hệ thống EAM | CARTO 3 | **EnSite X** (Abbott) |
| Catheter mapping | Pentaray 2-6-2 mm / Octaray | **Advisor FL Circular, Sensor Enabled** (loop bipolar) |
| Định vị | từ trường + impedance | **Sensor Enabled** (từ trường) + impedance/field scaling — dùng bản Sensor Enabled để giảm trôi hình học |
| Thu điểm tự động | ConfiDENSE | **AutoMap** (tự động, có tiêu chí chấp nhận beat) ⚠️[chốt với CAS] |
| Thu 2 nhịp đồng thời | **Parallel mapping** (đồng thời) | **KHÔNG có tương đương đồng thời** → xem §2 (2 giải pháp) |
| Xử lý lại offline | — | **TurboMap** (dựng lại bản đồ từ dữ liệu đã ghi) ⚠️[chốt với CAS] |
| Điện thế/omnipolar | bipolar | bipolar (Advisor Circular) — omnipolar chỉ có với HD Grid |

---

## 2. Vấn đề then chốt #1 — không có "parallel mapping" đồng thời

EnSite X không sao chép tính năng thu **đồng thời** 2 bản đồ SR + paced như CARTO.
**Phương pháp CHÍNH THỨC của protocol này = Cách A (người dùng chọn, 2026-07-01).** Cách B chỉ nêu làm phương
án dự phòng/kiểm chứng, không phải quy trình vận hành.

### ★ Cách A (PHƯƠNG PHÁP CHÍNH THỨC) — **thu cặp theo VÙNG, tuần tự, trên CÙNG một model hình học**
Vì mấu chốt là so **cùng một điểm ở hai nhịp**, và circular loop phủ hẹp hơn Pentaray, chia NT thành các vùng
giải phẫu (**mái, thành trước, vách, thành sau, thành bên, antra 4 TMP, sàn**) và với **mỗi vùng**, theo đúng
trình tự:
1. Thu bản đồ vùng đó **trong nhịp xoang** (đạt tiêu chí chấp nhận beat + mật độ vùng).
2. **Chuyển ngay sang ngoại kích CS** (§4), thu lại **đúng vùng đó**.
3. Chỉ khi cả hai lớp (SR + paced) của vùng đạt yêu cầu **mới di chuyển sang vùng kế**.

→ Giữ so sánh SR-vs-paced **cục bộ về không gian và gần nhau về thời gian**, giảm trôi hình học — tái lập gần
nhất tinh thần "same site, two rhythms" của Frontera trên hệ không có parallel module. [thích ứng EnSite]

**Ba quy tắc bắt buộc của Cách A:**
- **Khóa một model geometry duy nhất** dùng cho cả hai lớp bản đồ (SR và paced) để điểm đồng đăng ký
  (co-register) point-by-point — không tạo geometry mới cho lớp paced.
- **Không rời vùng khi chưa đủ cặp:** một vùng chỉ "xong" khi có cả lớp SR và lớp paced đạt mật độ; tránh vùng
  khuyết một trong hai nhịp (sẽ không phân loại được fixed/functional).
- **Ghi thứ tự vùng + dấu thời gian mỗi lớp** để truy vết trôi hình học nếu cần.

### Cách B (chỉ dự phòng/kiểm chứng, KHÔNG dùng vận hành) — ghi liên tục + TurboMap offline
Ghi liên tục toàn bộ rồi dùng **TurboMap** dựng lại hai bản đồ, gate theo nhịp. Chỉ dùng khi Cách A gặp sự cố
(vd trôi hình học nặng) hoặc để kiểm chứng hậu kỳ. ⚠️[chốt với CAS về khả năng gate theo nhịp trong TurboMap]

---

## 3. Vấn đề then chốt #2 — circular loop phủ hẹp hơn Pentaray

- Advisor FL Circular là **một vòng đơn** → phủ diện tích/1 vị trí nhỏ hơn "sao" Pentaray → cần **sweep có hệ
  thống, nhiều vị trí hơn** để đạt mật độ mục tiêu **≥3000 EGM/bản đồ** [Frontera]. Dự trù **nhiều thời gian
  hơn 18±6 phút của Frontera**.
- **Kiểm tiếp xúc:** Advisor FL Circular **không có lực tiếp xúc (CF)**. Thay "starfish deployment" của Pentaray
  bằng: **ổn định điện đồ + chỉ báo tiệm cận mô (tissue proximity) + hình dạng loop áp đều**. Đặt tiêu chí chấp
  nhận beat trong AutoMap: ổn định vị trí, ổn định LAT, cửa sổ chu kỳ, khoảng cách bề mặt. ⚠️[chốt với CAS]
- Circular loop **rất hợp** để quét antra TMP và thành buồng liên tục — tận dụng cho các vùng Frontera hay thấy
  functional (**antra TMP trong nhịp tạo**, **thành trước trong nhịp xoang**). [Frontera]

---

## 4. Tạo nhịp CS — GIỮ NGUYÊN Frontera (độc lập hệ mapping)

Phần này chạy trên **máy kích thích EP**, không phụ thuộc EnSite:
1. Catheter CS: quadri/decapolar → **CS đoạn xa (CS 1-2)**, qua TM đùi phải. [Frontera]
2. Xác định **ERP tại chỗ bằng ngoại kích ĐƯỢC CẢM NHẬN (sensed)** phóng từ CS 1-2. [Frontera]
3. Bản đồ paced = **một ngoại kích sensed từ CS 1-2, coupling = ERP tại chỗ + 30 ms**. [Frontera]
   - **Không** phải chuỗi drive S1-S2 đều; là **một beat sớm đồng bộ nhịp xoang cảm nhận**, coupling ngắn.
4. Lặp lại ngoại kích tại mỗi vị trí thu để mỗi điểm bản đồ paced có một beat ngoại kích tương ứng. [thích ứng EnSite]

---

## 5. Cấu hình tín hiệu EnSite X (để khớp Frontera)

| Thông số | Giá trị | Nguồn |
|---|---|---|
| Lọc EGM lưỡng cực | **30–300 Hz** | [Frontera] — đặt khớp trong amplifier config ⚠️[chốt với CAS] |
| Ngưỡng LVZ | **< 0,5 mV** (bipolar) | [Frontera] + kho REF-001/002 |
| Phân mảnh (fractionated) | EGM có **> 3 deflection** | [Frontera] |
| Mật độ | **≥ 3000 EGM/bản đồ**, phân bố đều | [Frontera] |
| Bản đồ hoạt hóa | isochrone; đọc **vùng chen isochrone (crowding)/vùng giảm tốc** = corridor dẫn truyền chậm | [thích ứng EnSite — tương đương phân tích isochrone của Frontera] |
| Vận tốc dẫn truyền (CV) | tính từ **gradient LAT / khoảng cách** giữa điểm vào–ra vùng chậm | [Frontera]; hiển thị CV tự động tùy phiên bản ⚠️[chốt với CAS] |

**Tham chiếu Frontera để so khi chạy:** CV tại vị trí chức năng bất thường **0,52±0,17 m/s**; điện thế tại vị
trí dẫn truyền chậm **0,73±0,47 mV**; thời lượng EGM corridor **47±10 ms** vs pivot **35±5 ms** (P<0,001). [Frontera]

---

## 6. Quy trình từng bước (EnSite X)

1. **Chuẩn bị:** PsAF chuyển nhịp về xoang trước thủ thuật; xuyên vách dưới hướng dẫn TEE; heparin 100 IU/kg,
   ACT >280 s; đặt catheter CS đoạn xa. [Frontera]
2. **Dựng model hình học NT** bằng Advisor FL Circular (Sensor Enabled) trên EnSite X; **khóa geometry** để tái
   dùng cho cả hai bản đồ. [thích ứng EnSite]
3. **Đo ERP tại chỗ** từ CS 1-2 (sensed extrastimulus). [Frontera]
4. **Với từng vùng** (mái → thành trước → vách → thành sau → thành bên → antra 4 TMP → sàn), theo **Cách A §2**:
   thu SR → thu ngay paced (ngoại kích CS, coupling ERP+30 ms) → sang vùng kế. AutoMap với tiêu chí chấp nhận
   beat đã đặt. [thích ứng EnSite]
5. Đạt **≥3000 EGM** cho **mỗi** bản đồ (SR và paced). [Frontera]
6. **Đối chiếu 2 propagation** bằng isochrone (SR vs paced); nếu dùng Cách B thì dựng bằng TurboMap rồi so. Hai
   người đọc; bất đồng → người thứ ba đọc mù (theo Frontera). [Frontera]

---

## 7. Phân tích & định nghĩa (verbatim Frontera)

- **Fixed:** bất thường dẫn truyền hiện ở **CẢ hai** nhịp.
- **Functional (phụ thuộc nhịp):** **chỉ 1** nhịp bộc lộ.
- **Corridor dẫn truyền chậm** = vùng chen isochrone/giảm tốc, EGM kéo dài (~47 ms); **pivot** = điểm xoay (~35 ms).
- **Chốt điện thế (lý do làm bản đồ kép):** ~**88%** vị trí chức năng có **điện thế bipolar bình thường** (chỉ
  12% rơi vào LVA <0,5 mV) → **bản đồ điện thế nhịp xoang đơn thuần bỏ sót phần lớn**. [Frontera]
- **Quy tắc chống-nhiễu-hướng cho lab bipolar (thao tác hóa Butcher):** mọi "LVZ" chỉ thấy ở MỘT nhịp mà bình
  thường ở nhịp kia → **gắn cờ "nghi giả do hướng/functional", KHÔNG ghi là sẹo cố định** cho tới khi xác nhận
  ở cả hai nhịp. [thích ứng EnSite dựa REF-034]

---

## 7b. Thông số EnSite X thu được theo protocol này → đưa vào CRF (kèm CÁCH LẤY)

**Bối cảnh vận hành đã chốt (2026-07-01):** chuyển nhịp điện về xoang trước → map **trong nhịp xoang (SR)**
rồi map **trong nhịp tạo CS (paced)** trên **cùng một model geometry đã khóa** (Cách A §2). Vì vậy **mọi thông
số định lượng dưới đây đều thu THÀNH CẶP: một giá trị ở SR, một giá trị ở paced** — chính cặp này mới cho phép
phân loại fixed/functional (§7). Nhập CRF theo cặp cột **(SR) | (paced)**.

**Nguyên tắc bắt buộc:** mỗi ô số dưới đây **KHÔNG có nghĩa nếu thiếu khối "Điều kiện đo"** — luôn ghi kèm:
nhịp (SR/paced), vị trí tạo nhịp (**CS 1-2**), coupling (**ERP tại chỗ + 30 ms**), catheter (**Advisor FL
Circular, bipolar**), lọc (**30–300 Hz**), ngưỡng LVZ (**< 0,5 mV**), và geometry-model dùng chung. (Khớp khối
ĐK-1…ĐK-8 trong `crf_table_with_measurement_conditions.md`.)

| # | Thông số (đơn vị) | Cách lấy trên EnSite X (thao tác cụ thể) | Đo ở nhịp | Trường CRF đề xuất | Nguồn / cờ |
|---|---|---|---|---|---|
| E-1 | **Điện thế lưỡng cực đỉnh–đỉnh** (mV) | Bản đồ **voltage** (Advisor Circular, lọc 30–300 Hz); AutoMap gán biên độ peak-to-peak mỗi điểm; đọc **trung vị + khoảng** theo từng vùng giải phẫu | SR **và** paced | `dien_the_trungvi_vung__SR` / `__paced` (mV) | lọc & phương pháp [Frontera]; hiển thị/menu ⚠️CAS |
| E-2 | **Diện tích LVZ (<0,5 mV) & % diện tích** (cm²; %) | Công cụ **area measurement** trên bản đồ voltage, đặt ngưỡng **<0,5 mV**; đọc diện tích vùng <0,5 mV và **% so với diện tích model** (toàn NT và từng vùng) | SR **và** paced | `LVZ_pctarea_toanNT__SR` / `__paced`; `LVZ_pctarea_vung__…` | ngưỡng [Frontera + REF-001/002]; công cụ area ⚠️CAS |
| E-3 | **Thời gian hoạt hóa tại chỗ (LAT)** (ms) | Annotation LAT tự động của **AutoMap**, tham chiếu CS/khởi kích cố định; **không nhập thô vào CRF** — là nền để dựng bản đồ hoạt hóa & suy CV (E-4) | mỗi nhịp | *(nội bộ, không nhập; ghi ref-channel)* | [thích ứng EnSite] |
| E-4 | **Vận tốc dẫn truyền (CV)** (m/s) | Từ **gradient LAT / khoảng cách** giữa điểm vào–ra vùng chậm; hoặc mô-đun CV tự động nếu phiên bản có. Ghi **CV tối thiểu tại vùng dẫn truyền chậm** | SR **và** paced, cùng vùng | `CV_min_vungcham__SR` / `__paced` (m/s) | [Frontera] (tham chiếu **0,52±0,17 m/s** tại vị trí chức năng bất thường); menu CV ⚠️CAS |
| E-5 | **Vùng chen isochrone / vùng giảm tốc** (đếm; vị trí giải phẫu) | Bản đồ **activation isochrone**; đọc nơi isochrone chụm = **corridor dẫn truyền chậm**; đặt **isochrone spacing / window of interest** phù hợp | SR **và** paced | `so_corridor_cham__SR` / `__paced`; `vitri_corridor` (danh mục vùng) | [thích ứng EnSite ~ phân tích isochrone Frontera]; spacing ⚠️CAS |
| E-6 | **Thời lượng EGM** (ms) | Đo **bề rộng EGM lưỡng cực** trên cửa sổ tại vị trí corridor và pivot | tại nhịp bộc lộ | `EGM_duration_corridor` / `EGM_duration_pivot` (ms) | [Frontera] (tham chiếu **corridor 47±10 ms** vs **pivot 35±5 ms**, P<0,001) |
| E-7 | **Phân mảnh (fractionation, EGM >3 deflection)** (có/không; số điểm; CFE-mean ms) | Đọc hình dạng EGM; nếu phiên bản có **bản đồ CFE** thì lấy **CFE-mean** theo vùng | SR **và** paced | `phanmanh_vung__SR` / `__paced` (có/không); `CFE_mean_vung` (ms) | định nghĩa >3 deflection [Frontera]; bản đồ CFE ⚠️CAS |
| E-8 | **Mật độ điểm / số EGM mỗi bản đồ** (đếm) | **Map statistics** của EnSite X: tổng EGM chấp nhận; dùng để **kiểm chất lượng ≥3000 EGM/bản đồ** | mỗi bản đồ (SR; paced) | `so_EGM_map__SR` / `__paced` (kiểm QC ≥3000) | mục tiêu [Frontera] |
| E-9 | **Diện tích bề mặt model NT** (cm²) | Đọc **surface area** của geometry Advisor Circular đã khóa (dùng chung 2 lớp) | 1 lần (model chung) | `dientich_bemat_NT` (cm²) | [thích ứng EnSite] |
| E-10 | **Phân loại fixed vs functional** (đếm; % ) — **DẪN XUẤT, không phải readout** | **So cặp** bản đồ SR vs paced theo §7 (KHÔNG có nút xuất trực tiếp): bất thường ở **cả hai** nhịp = fixed; **chỉ một** nhịp = functional | so SR↔paced | `so_vitri_fixed`; `so_vitri_functional`; `pct_functional_dienthe_binhthuong` | định nghĩa [Frontera] (tham chiếu **~88%** vị trí chức năng có điện thế bipolar bình thường) |
| E-11 | **Cờ "LVZ nghi giả do hướng/functional"** (có/không) | Áp **quy tắc §7**: "LVZ" chỉ thấy ở MỘT nhịp mà bình thường ở nhịp kia → gắn cờ, **không** ghi là sẹo cố định | so SR↔paced | `co_LVZ_nghigia_huong` (có/không) + vùng | [thích ứng EnSite dựa REF-034] |
| E-12 | **Kiểu lan truyền / hướng mặt sóng** (mô tả) | Bản đồ **propagation** động (SR vs paced) | SR **và** paced | `kieu_lantruyen_vung__SR` / `__paced` | [thích ứng EnSite] |

**Ghi chú vận hành khi đưa vào CRF:**
- **Đơn vị vùng:** mọi thông số vùng dùng đúng danh mục 7 vùng của Cách A (**mái · thành trước · vách · thành
  sau · thành bên · antra 4 TMP · sàn**) để cặp SR–paced khớp point-by-point trên geometry đã khóa.
- **E-10/E-11 là kết luận, không phải số máy đọc:** ghi rõ trong CRF đây là biến dẫn xuất từ so sánh 2 lớp,
  kèm tên 2 người đọc (bất đồng → người thứ ba đọc mù, theo Frontera §6).
- **Vì đã chốt chuyển nhịp trước:** nên bổ sung điều kiện đo **"thời gian từ chuyển nhịp điện đến khi bắt đầu
  map SR (phút)"** (ứng viên **ĐK-9**) — phù nề/hồi phục sau sốc có thể ảnh hưởng điện thế & CV; ghi để hiệu
  chỉnh/loại trừ. *(Đề xuất, chưa thêm vào file CRF — chờ bạn chốt.)*
- **Tất cả ô ⚠️CAS:** xác nhận tên menu/khả năng xuất với ứng dụng viên Abbott trước khi khóa CRF (xem §9).

---

## 8. An toàn & xử lý khởi phát RN

- Khởi phát RN có thể do protocol ngoại kích **hoặc** thao tác catheter trong NT. [Frontera]
- Nếu RN không tự dứt → chuyển nhịp điện đồng bộ, ổn định lại xoang, tiếp tục. Theo dõi nhiệt độ thực quản khi
  quét thành sau. Duy trì ACT >280 s. [thích ứng EnSite]

---

## 9. Danh mục CẦN chốt với ứng dụng viên Abbott trước khi chạy

1. **Tiêu chí chấp nhận beat trong AutoMap** (ổn định vị trí/LAT, cửa sổ chu kỳ, khoảng cách bề mặt) — để đạt
   mật độ đều mà không nhận beat rác từ loop mất tiếp xúc.
2. **Khả năng gate theo nhịp trong TurboMap** (nếu chọn Cách B) — tách beat xoang vs beat ngoại kích khi dựng lại.
3. **Đặt lọc bipolar 30–300 Hz** đúng chỗ trong amplifier/EnSite config để khớp Frontera.
4. **Hiển thị/CV & cài đặt isochrone** (isochrone spacing, window of interest, deceleration-zone) trên phiên bản
   phần mềm EnSite X hiện có của lab.
5. **Field scaling / geometry lock** để hai bản đồ đồng đăng ký chính xác point-by-point.
6. (Tùy chọn) Nếu muốn giảm nhiễu-hướng cho bản đồ điện thế: khả năng mượn **Advisor HD Grid + OT**.

---

## 10. Nguồn
- Frontera A, et al. Heart Rhythm 2025;22:1401–1410. PMID [39278611](https://pubmed.ncbi.nlm.nih.gov/39278611/).
  DOI 10.1016/j.hrthm.2024.09.017. **[REF-035]** — full text: `source/la-ep-elderly-af/REF025-Frontera 2024.html`.
- Butcher C, et al. JACC Clin Electrophysiol 2023;9(8 Pt 2):1500–12. PMID 37204357. **[REF-034]** — cơ sở quy tắc
  chống-nhiễu-hướng §7 (LVZ giả do va chạm mặt sóng trên bản đồ bipolar).
- Dittrich S, et al. J Interv Card Electrophysiol 2024;67(2):399–408. PMID 37227537. **[REF-033]** — omnipolar vs
  bipolar (nền cho §0, tùy chọn HD Grid).

**Trung thực về giới hạn:** các mục ⚠️[chốt với CAS] là tên tính năng/giá trị cài đặt phụ thuộc phiên bản phần
mềm EnSite X; tài liệu này chuẩn hóa **quy trình và thông số điện sinh lý** (verbatim Frontera ở đâu có), còn
**menu/giá trị hệ thống cụ thể** phải do ứng dụng viên Abbott xác nhận tại lab.
