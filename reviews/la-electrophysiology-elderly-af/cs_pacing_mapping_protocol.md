# Protocol tạo nhịp xoang vành (CS) cho lập bản đồ cơ chất chức năng nhĩ trái

**Tái dựng theo phương pháp Frontera A và cộng sự** — *"The functional substrate in patients with atrial
fibrillation is predictive of recurrences following catheter ablation."* Heart Rhythm 2025;22:1401–1410.
PMID 39278611. DOI 10.1016/j.hrthm.2024.09.017. **[REF-035]**

**Soạn:** 2026-07-01 · cho nghiên cứu điện sinh lý nhĩ trái ở bệnh nhân rung nhĩ cao tuổi (khung CRF).
**Nguyên tắc trích dẫn (Luật 1):** mọi thông số ghi "[Frontera]" lấy verbatim từ full-text đã lưu
(`source/la-ep-elderly-af/REF025-Frontera 2024.html`). Mọi thông số ghi "[thêm cho NC này]" là bổ sung/điều
chỉnh của người soạn, KHÔNG phải của Frontera — cần lab tự chuẩn hóa.

---

## 1. Mục tiêu & nguyên lý

Lập **hai bản đồ điện giải phẫu mật độ siêu cao của nhĩ trái trên cùng một hình học (shell)**:
- **Bản đồ 1 — nhịp xoang (SR):** đặc trưng cơ chất nền.
- **Bản đồ 2 — nhịp tạo bằng một ngoại kích được cảm nhận (sensed extrastimulus) từ CS đoạn xa:** áp một
  mặt sóng khử cực **phi sinh lý, chuẩn hóa, một hướng** để **bộc lộ bất thường dẫn truyền phụ thuộc nhịp
  (chức năng)** vốn ẩn trong nhịp xoang. [Frontera]

**Vì sao CS đoạn xa + ngoại kích (không phải "straight pacing"):** mục tiêu là tạo một mặt sóng chuẩn, một
hướng để **tối đa hóa độ nhạy phát hiện vùng dẫn truyền chậm chức năng**; Frontera nêu rõ *"straight pacing
alone would not capture real-time conduction differences at specific sites"* — chính **ngoại kích có coupling
ngắn** mới làm đổi cả hướng lẫn vận tốc mặt sóng, bộc lộ block chức năng. Cơ sở sinh lý: hướng mặt sóng và
coupling interval quyết định sự hình thành điện đồ phức tạp giữa các sợi có tính bất đẳng hướng cấu trúc.
Rate-dependency của block CS↔LA theo tần số tạo nhịp CS đã được Huang và cs. chứng minh trước đó [Frontera,
trích ref 20]. [Frontera]

---

## 2. Tiêu chuẩn bệnh nhân

- Bệnh nhân RN có chỉ định triệt đốt (PAF hoặc PsAF). Frontera: 76 BN sàng lọc liên tiếp → **63 phân tích**
  (PAF 41, PsAF 22; tuổi trung bình 63,5±7,5). [Frontera]
- **PsAF phải được chuyển nhịp về xoang TRƯỚC thủ thuật** — vì cả hai bản đồ đều cần nền nhịp xoang. [Frontera]
- **[thêm cho NC này]** Với trọng tâm cao tuổi: ghi rõ tuổi, frailty index, LAVi, eGFR, thời gian RN — đây là
  các biến điều chỉnh khả năng bộc lộ cơ chất (nhĩ lão hóa nhiều xơ hơn).

---

## 3. Chuẩn bị & tiếp cận mạch

1. Ký cam kết. [Frontera]
2. **Catheter CS:** quadripolar hoặc decapolar cố định/uốn được (Frontera dùng *Viking, Boston Scientific*)
   đưa tới **đoạn xa xoang vành** qua **tĩnh mạch đùi phải**. Dùng để (a) tạo nhịp/ngoại kích và (b) làm mốc
   tham chiếu. [Frontera]
3. **Tiếp cận nhĩ trái:** xuyên vách liên nhĩ theo đường xuôi dòng, **hướng dẫn bằng siêu âm qua thực quản
   (TEE)**. [Frontera]
4. **Kháng đông:** heparin bolus **100 IU/kg** + truyền liên tục, duy trì **ACT > 280 giây**. [Frontera]

---

## 4. Thiết bị & cấu hình mapping

| Hạng mục | Giá trị Frontera | Ghi chú |
|---|---|---|
| Hệ thống EAM | **CARTO 3** (Biosense Webster) | [Frontera] |
| Catheter mapping | **Pentaray** (spacing 2-6-2 mm) *hoặc* **Octaray** (2-2-2-2-2 mm) | 55/63 (87,3%) dùng Pentaray [Frontera] |
| Module | **Parallel mapping** — thu **đồng thời 2 bản đồ hoạt hóa** (SR + paced) | mấu chốt để so real-time [Frontera] |
| Mật độ điểm | **≥3000 EGM/bản đồ**, phân bố đều | thực đạt 4806±1315 EGM/map [Frontera] |
| Lowest color threshold | **đặt = 5** | [Frontera] |
| Lọc EGM lưỡng cực | **30–300 Hz** | dùng cho phân tích duration + amplitude [Frontera] |
| Thời gian tạo cả 2 bản đồ | ~**18±6 phút** (nhờ parallel mapping) | mốc thực tế [Frontera] |
| Kiểm tiếp xúc mô | xác nhận **nở đủ splines kiểu "starfish"** tại mỗi điểm | [Frontera] |
| Cài đặt isochrone / CARTO | **theo Supplemental file của Frontera** | ⚠️ **[cần lấy]** không có trong text chính — phải chuẩn hóa trước khi chạy |

---

## 5. Quy trình lập bản đồ kép (từng bước)

### Bước A — Bản đồ nhịp xoang (Map 1)
Trong nhịp xoang ổn định, dùng Pentaray/Octaray lập bản đồ hoạt hóa + điện thế lưỡng cực NT tới mật độ
mục tiêu (≥3000 EGM). Kiểm tiếp xúc "starfish" từng điểm. [Frontera]

### Bước B — Xác định ERP tại chỗ từ CS đoạn xa
Đo **thời gian trơ hiệu quả (ERP) tại chỗ bằng ngoại kích được cảm nhận (sensed extrastimulus)** phóng từ
CS 1-2. Giá trị ERP này là mốc để đặt coupling ở bước C. [Frontera]

### Bước C — Bản đồ nhịp tạo bằng ngoại kích (Map 2)
Phóng **một ngoại kích được cảm nhận từ CS đoạn xa (CS 1-2)** với **coupling interval = ERP tại chỗ + 30 ms**
(tức ERP+30 ms). Thu bản đồ thứ hai trên **cùng hình học** với Map 1 nhờ module parallel mapping (đồng thời).
[Frontera]

> Lưu ý bản chất: đây **không** phải chuỗi drive S1-S2 cổ điển, mà là **một ngoại kích đơn đồng bộ theo nhịp
> xoang cảm nhận được**, coupling ngắn (ERP+30 ms) — đủ để đổi hướng + vận tốc mặt sóng và bộc lộ block chức
> năng. [Frontera]

### Bước D — Đối chiếu hai propagation
Hai propagation (SR vs. nhịp-tạo-ngoại-kích) được phân tích bằng **isochrone** để tìm vùng dẫn truyền bất
thường. Frontera: hai người đọc (F.V., F.C.); bất đồng → người thứ ba (A.F.) đọc mù. [Frontera]

---

## 6. Định nghĩa & phân tích (verbatim Frontera)

- **Hoạt hóa bình thường:** mặt sóng lan truyền đồng nhất, kiểu lan tuyến tính theo hướng chính.
- **Bất thường CỐ ĐỊNH (fixed):** hiện diện ở **CẢ hai** nhịp.
- **Bất thường CHỨC NĂNG (functional, phụ thuộc nhịp):** **chỉ bộc lộ ở MỘT trong hai** nhịp.
- **Điện đồ phân mảnh (fractionated):** EGM có **>3 deflection**.
- **Vận tốc dẫn truyền tại chỗ (CV):** tính trên CARTO từ chênh thời gian và khoảng cách đã biết giữa điểm
  vào–ra vùng dẫn truyền chậm (theo phương pháp đã công bố).
- **Corridor dẫn truyền chậm vs. pivot point:** thời lượng EGM ở corridor **47±10 ms** vs. pivot **35±5 ms**
  (P<0,001); CV trung bình tại vị trí chức năng bất thường **0,52±0,17 m/s**; điện thế tại vị trí dẫn truyền
  chậm **0,73±0,47 mV**.

**Kết quả tham chiếu Frontera (để so sánh khi chạy):** 234 bất thường dẫn truyền; **125 (53,4%) chức năng**
(chỉ hiện ở nhịp tạo); vị trí hay gặp: thành trước (nhịp xoang) và antra TMP (nhịp tạo); 82,6% trùng cấu trúc
ngoài tim (xoang Valsalva ĐM chủ lên phía trước, thực quản phía sau). Cơ chất chức năng tồn dư sau PVI là
yếu tố **độc lập** dự báo tái phát RN: **HR 2,539 (95% CI 1,458–4,420; P=0,001)**. [Frontera]

---

## 7. Điểm mấu chốt về điện thế (lý do phải làm bản đồ kép, không chỉ voltage-SR)

Chỉ **18,4%** bất thường dẫn truyền biểu hiện kèm vùng điện thế thấp (LVA <0,5 mV); và **chỉ 12% vị trí chức
năng** rơi vào LVA — tức **~88% cơ chất chức năng có điện thế lưỡng cực BÌNH THƯỜNG** (ví dụ 1,25±0,59 mV).
Kết luận Frontera: **ngưỡng điện thế quy ước <0,5 mV bỏ sót phần lớn cơ chất chức năng** → bản đồ điện thế
nhịp xoang đơn thuần là không đủ. [Frontera]

---

## 8. An toàn & xử lý khởi phát RN

- Frontera cảnh báo: **khởi phát RN có thể xảy ra** trong lúc mapping — do chính protocol ngoại kích **hoặc**
  (thường gặp hơn) do thao tác catheter mapping trong NT. [Frontera]
- **[thêm cho NC này]** Kế hoạch xử trí: nếu RN khởi phát và không tự dứt → chuyển nhịp điện đồng bộ, ổn định
  lại nhịp xoang, rồi tiếp tục. Theo dõi nhiệt độ thực quản khi thao tác thành sau. Duy trì ACT >280 s suốt
  thời gian ở NT.

---

## 9. Bối cảnh triệt đốt (Frontera)

PVI thực hiện thường quy; nếu corridor chức năng nằm gần đường triệt đốt dự kiến → operator đưa vào phác đồ
triệt đốt antra rộng (WACA). Kiểm block vào/ra; test adenosine tùy operator. Hiện tượng chức năng tồn dư được
đưa vào phân tích. [Frontera]

---

## 10. Tích hợp CRF cho nghiên cứu cao tuổi (biến số cần ghi bắt buộc)

Vì "voltage/CV không phải thuộc tính bất biến của mô" (phụ thuộc nhịp + hướng mặt sóng), mọi biến điện học
trong CRF phải kèm **điều kiện đo**. Đề xuất trường bắt buộc:

| Nhóm trường | Trường CRF |
|---|---|
| Điều kiện đo | nhịp lúc đo (SR / paced-extrastimulus / AF); vị trí tạo nhịp (CS 1-2); coupling (ERP+30 ms); ERP tại chỗ đo được (ms) |
| Hệ thống | EAM (CARTO/EnSite); catheter (Pentaray 2-6-2 / Octaray); số EGM/bản đồ; ngưỡng màu; lọc (30–300 Hz) |
| Kết cục cơ chất | tổng bất thường; số fixed; số functional (%); vị trí; CV tại chỗ (m/s); điện thế tại vị trí bất thường (mV); LVA% (<0,5 mV) |
| Phân tầng tuổi | tuổi; frailty; LAVi; eGFR; type RN; thời gian RN |

**[thêm cho NC này] — khoảng trống mà NC của bạn có thể lấp:** Frontera **không phân tầng theo tuổi** (tuổi
hỗn hợp, TB 63,5). Câu hỏi mở giá trị cao: *tỷ lệ cơ chất chức năng (functional %) có tăng theo tuổi không, và
có dự báo tái phát mạnh hơn ở nhóm ≥75 không?* Đây là đóng góp nguyên bản khả thi với chính protocol này.

---

## 11. Điểm cần chuẩn hóa trước khi chạy (chưa có trong text chính Frontera)

1. **Cài đặt isochrone + tham số CARTO cụ thể** — Frontera để ở Supplemental file; phải lấy/định nghĩa
   (window of interest, isochrone spacing, fill/color threshold chi tiết) để tái lập được.
2. **Ngưỡng CV định nghĩa "dẫn truyền chậm"** — Frontera tính CV nhưng ngưỡng phân loại corridor dựa trên
   EGM duration + hình thái isochrone; nếu NC muốn ngưỡng CV tuyệt đối (vd <0,5 m/s) cần định nghĩa tiên
   nghiệm trong protocol.
3. **Nhịp nền (baseline cycle length) khi đo Map 1** — Frontera lưu ý tần số nền nhịp xoang ảnh hưởng khả năng
   bộc lộ hiện tượng chức năng (nhịp nhanh hơn bộc lộ nhiều hơn); cân nhắc chuẩn hóa (vd tạo nhịp nhĩ nền cố
   định) nếu muốn so sánh giữa bệnh nhân — **đây là hạn chế Frontera tự nêu**.

---

## Nguồn
Frontera A, Villella F, Cristiano E, et al. The functional substrate in patients with atrial fibrillation is
predictive of recurrences following catheter ablation. **Heart Rhythm 2025;22:1401–1410.**
PMID [39278611](https://pubmed.ncbi.nlm.nih.gov/39278611/). DOI 10.1016/j.hrthm.2024.09.017. [REF-035]
Full text: `source/la-ep-elderly-af/REF025-Frontera 2024.html`.

*Phương pháp bổ trợ về tính phụ-thuộc-hướng của điện thế: REF-034 (Butcher 2023, JACC CE), REF-033 (Dittrich
2023, JICE) — trong kho `reference/la-electrophysiology-elderly-af.md`.*
