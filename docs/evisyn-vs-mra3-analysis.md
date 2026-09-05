# Evisyn ↔ CLAUDE_MRA_3 — phân tích so sánh và lộ trình nâng cấp

Ngày: 2026-09-05 · Người phân tích: Claude (session `claude/evisyn-ai-mra3-analysis-ja73s5`)
Vật liệu: `evisyn.rar` (3.2 MB, giải nén 5.5 MB) do người dùng cung cấp · repo `CLAUDE_MRA_3` @ `7c970f4`

> **Bản quyền — đọc trước khi port bất cứ thứ gì.** Mọi `SKILL.md` của Evisyn mang dòng
> `© TS.BS Đăng Kiên — chỉ dành cho học viên trả phí. Cấm chia sẻ/thương mại hoá dưới mọi hình thức.`
> Tài liệu này phân tích **nguyên tắc thiết kế**, không sao chép mã nguồn. Mọi hạng mục trong lộ trình
> ở Phần 4 là **viết lại từ đầu theo ý tưởng**, không phải copy file. Không đưa mã hay `SKILL.md` của
> Evisyn vào repo này.

---

## 1. Evisyn là gì — số liệu đo được

| Hạng mục | Số đo |
|---|---|
| Runtime | Node.js 22 LTS, **zero npm dependency** (chỉ `fs`, `path`, `crypto`, `fetch`) |
| Mã nguồn | 92 file `.mjs` · ~10.300 dòng script (không tính test) |
| Kiểm thử | 24 file test · ~3.000 dòng · **~711 assertion · `npm test` PASS toàn bộ** (đã chạy thật) |
| Skill | 19 skill = 19 bước, mỗi `SKILL.md` **≤200 dòng** (trần cứng) |
| Nguồn tìm kiếm | 4 DB no-key qua `fetch`: PubMed · Europe PMC · OpenAlex · Semantic Scholar |
| Nhập ngoài | Bước 2B: đọc file export Scopus/WoS/Embase/CENTRAL từ đĩa (không bao giờ tự query) |
| Đa ngành | 4 profile từ **một nguồn duy nhất**: medicine · economics · social · cross |
| Trích dẫn | 20 CSL bundled + catalogue >10.000 style · export `.bib/.ris/.enw/.nbib/.json/.csv` |
| Báo cáo | PRISMA 2020 flow (`.svg/.mmd/.csv/.json`) + bảng chiến lược tìm kiếm |
| Đóng gói | `dist/evisyn-<discipline>.zip` × 4, build từ nguồn, ZIP writer tự viết bằng `node:zlib` |
| Đầu ra cuối | `manuscript.docx` / `.tex` qua Pandoc (bước 15, tùy chọn) |

**USP tự tuyên bố:** *claim-level citation verification* — mọi câu factual phải có ≥1 trích dẫn, mọi
trích dẫn phải truy về một bài trong **pool đóng** và về một ô evidence card lấy từ abstract của
chính bài đó.

**Kiến trúc:** AI harness = tầng điều phối + suy luận; **Node script = tầng thực thi tất định**.
Nguyên tắc số 2 của Evisyn: *"Deterministic work is HARDCODED in a Node script; the LLM/skill is
used only where judgement is required"* — chỉ 4 chỗ dùng LLM: sàng lọc (5B), gom chủ đề outline (11),
đọc full-text (12F tier 2), và viết (13).

**Ba cơ chế cứng đáng chú ý:**

1. **Bước 15 là HARD GATE** — từ chối export `.docx` nếu `citation_audit.json` (bước 14) không `PASS`.
   Cờ `--allow-failed-audit` chỉ để đọc nháp trên màn hình và được ghi vào báo cáo là đã bị bỏ qua.
2. **6 khóa của bước 12F (full-text):** IDENTITY · ECHO · PARAPHRASE · LENGTH · QUOTE · NUMBER.
   QUOTE đòi substring verbatim; NUMBER đòi con số trong claim phải nằm trong chính quote đó. Hai
   tier báo cáo tách bạch: tier 1 = Europe PMC XML (`verification: machine`), tier 2 = harness tự đọc
   PDF (`human_auditable`).
3. **Guard chống tự phá hoại:** bước 10 **từ chối ghi và exit 1** nếu pool cũ còn bài `status:
   "enriched"` (dữ liệu 12F chỉ tồn tại trong pool, mỗi bài tốn một lượt đọc) · bước 2 từ chối chạy
   lại khi config không đổi · `validateProfile` chặn profile có thứ tự ngưỡng sai · throttle per-host
   đọc `Retry-After` và **nới vĩnh viễn** khoảng cách cho host đó sau một lần 429.

---

## 2. So sánh trục 1 — kiến trúc & cơ chế chất lượng

| Chiều | Evisyn | CLAUDE_MRA_3 |
|---|---|---|
| Triết lý | Pipeline tất định 19 bước, LLM chỉ vào nơi cần phán đoán | Đội 7 agent chuyên trách, LLM là chủ thể, script là sàn dưới |
| Tỷ lệ tất định | ~10.300 dòng script phủ gần toàn bộ pipeline | ~770 dòng Python phủ 3 khâu (P1 citation · P2 số · P3 search log) |
| Kiểm thử | ~711 assertion tự động, `npm test` một lệnh | 3 test case định tính, chạy tay |
| Cổng người duyệt | STOP sau **mỗi** bước (19 lần), thủ tục | **4 cổng chọn theo nội dung**, có Research Map hard gate |
| Thẩm định bằng chứng | **KHÔNG CÓ** — grep `risk of bias` = 0 hit | GRADE + RoB 2 / ROBINS-I / NOS / QUADAS-2 |
| Đồng thuận vs tranh cãi | không có | Law 4 — bắt buộc hai mục có nhãn rõ |
| Steelman | không có | bắt buộc trong hiến pháp + rubric + appraiser + writer |
| Nguồn viết | **abstract** (12F full-text là opt-in, mặc định bỏ) | **full text** là mặc định; Gate 2b STOP nếu ≥3 bài HIGH còn abstract-only |
| Nhật ký tiến trình | `SESSION.md` do **script** ghi | `_workspace/` do LLM kể |
| Bộ nhớ học | bài học nằm rải trong `AGENTS.md` dạng prose | 44 lesson có mã · evolution-log 10 entry · glossary Việt · vòng học có người duyệt |
| Ngôn ngữ deliverable | **tiếng Anh** (tiếng Việt chỉ cho hướng dẫn học viên) | **tiếng Việt mặc định** + L-033/L-037 (soạn bản địa, không dịch máy) |
| Xuất bản | `.docx`/`.tex`/CSL/RIS/PRISMA SVG | `.md` |
| Quy mô corpus điển hình | ~100 bài, `target_words` mặc định 10.000 | ~20–40 bài |

### 2.1 Bảy chỗ Evisyn mạnh hơn rõ rệt

1. **Tỷ lệ tất định.** MRA_3 mới đẩy được 3 khâu cơ học ra khỏi LLM (L-039). Evisyn đẩy gần như toàn
   bộ: normalize, dedup, prefilter, pool, extract, PRISMA, audit, export đều là script.
2. **Kiểm thử tự động.** 711 assertion vs 3 case chạy tay. Đây là chênh lệch về *độ tin cậy khi sửa
   harness* — MRA_3 sửa một dòng constitution thì không có gì bắt được hồi quy.
3. **Quyết định thiết kế bằng đo, không bằng cảm nhận.** Evisyn ghi số cho từng lựa chọn: PMC phủ
   75–83% pool y học nhưng **0%** kinh tế/xã hội · ECHO fingerprint cùng bài 0,51–0,64 vs khác bài
   0,08–0,36 → ngưỡng fail 0,40 nằm đúng khe · prefilter cắt 25% một pool 154 bài làm mất 77 bài
   **trong đó 47 bài khớp cả 4 concept** → sinh ra `full_coverage_floor`. MRA_3 quyết định bằng bài
   học định tính, không có phép đo nào.
4. **Guard chống chính mình.** Ba cơ chế ở §1.3 — MRA_3 không có tương đương nào; `reference/` có thể
   bị ghi đè mà không ai chặn.
5. **Hạ tầng xuất bản.** CSL/Pandoc/RIS/PRISMA SVG. MRA_3 dừng ở `.md`, người dùng phải tự làm phần
   nộp tạp chí.
6. **Đa ngành từ một nguồn.** Kèm bài học đắt được ghi lại: hai fork tay `aglr-eco`/`aglr-social` chỉ
   khác ~111 dòng nhưng **cả hai đều mất** tính năng đọc full-text và bảo vệ rate-limit của nhánh
   chính. Đúng nguyên tắc "ratchet" của hiến pháp MRA_3, nhưng Evisyn thi hành bằng kiến trúc.
7. **Nhật ký do script ghi.** `SESSION.md` viết bởi `appendSession()` trong `main()` của từng runner,
   không phải từ trí nhớ agent — đúng tinh thần chống R4 (fake-step) mà MRA_3 phát biểu nhưng chưa
   thi hành bằng máy.

### 2.2 Sáu chỗ MRA_3 mạnh hơn rõ rệt

1. **Thẩm định bằng chứng — Evisyn không có.** Đây là khác biệt lớn nhất. `grep -c "risk of bias"`
   trên toàn bộ Evisyn = **0**. `GRADE` xuất hiện đúng 1 lần trong nội dung thật
   (`skills/step-13-write-review/disciplines/medicine.md:19`), và câu đó là:
   *"Name an instrument **only if it was actually applied**… If none was applied, say so plainly and
   name none."* Nghĩa là Evisyn **cố ý không thẩm định** và trung thực khai báo điều đó. Sản phẩm của
   nó là một tổng quan có trích dẫn sạch nhưng **không phân tầng độ chắc chắn, không đánh giá nguy cơ
   sai lệch, không tách đồng thuận khỏi tranh cãi**. MRA_3 có toàn bộ tầng này.
2. **Viết từ abstract là điểm yếu chết người cho y học.** Chính MRA_3 đã học bài này: **L-005 — "Copy
   effect sizes and CIs from the results table, not the abstract"**. Evisyn viết core từ abstract và
   để full-text làm opt-in mặc định tắt, với lý do "12F tốn thời gian thật của học viên". Đối với
   chương tổng quan luận án tiến sĩ hay bài nộp tạp chí y học, đó là đánh đổi sai hướng.
3. **Research Map hard gate.** Evisyn STOP sau mỗi bước — nhưng đó là dừng **thủ tục** ("đã xong bước
   N, xác nhận để sang N+1"). Nó không có chỗ nào người duyệt **bức tranh nghiên cứu và danh sách
   nguồn** trước khi tốn công thẩm định/viết. Dừng 19 lần theo thủ tục không thay được 1 lần duyệt
   đúng chỗ theo nội dung.
4. **Bộ nhớ học có cấu trúc.** Evisyn học rất tốt — nhưng bài học nằm trong `AGENTS.md` 45 KB dạng
   văn xuôi, không có mã, không có cơ chế thu thập lỗi sau mỗi lần chạy, không có người duyệt trước
   khi ghi. MRA_3 có L-001→L-044 + evolution-log + vòng học có gate.
5. **Tiếng Việt như deliverable.** Evisyn viết review bằng tiếng Anh; tiếng Việt chỉ dành cho
   `README_START_HERE.md` và các câu agent nói với học viên. MRA_3 mặc định tiếng Việt, có glossary
   102 dòng và hai bài học riêng về soạn bản địa (L-033) + tự kiểm độ trôi chảy với blacklist calque
   (L-037).
6. **Tách sinh khỏi kiểm bằng agent độc lập + quality-coach.** Evisyn tách bằng *script* (bước 14
   không tin bước 13) — mạnh về traceability. MRA_3 tách thêm bằng *tác nhân* (verifier đọc thẳng
   draft + nguồn, writer không được biện hộ — chống R5) và có coach nâng trần chất lượng. Hai cách bổ
   sung nhau chứ không thay thế.

### 2.3 Một rủi ro chung, mỗi hệ hở một nửa

Bước 14 của Evisyn tự khai limitation rất trung thực: *"A script verifies traceability, not meaning…
Always spot-check ~10% of cited sentences."* Cộng với mặc định `target_words: 10.000` viết từ
abstract, đây chính là failure mode mà hiến pháp MRA_3 đặt tên là **R2 — Faking "done"**: văn tự tin,
tiêu đề gọn, trích dẫn truy được 100% — mà tầng bằng chứng bên dưới là abstract chưa qua thẩm định.

Ngược lại MRA_3 hở nửa kia: nó *có* thẩm định sâu nhưng **không đo được độ phủ** — không biết corpus
của mình bỏ sót bao nhiêu, vì recall do LLM quyết và P3 chỉ kiểm *tính tự nhất quán của ledger*, không
kiểm con số có đúng không.

**Traceability mà không có appraisal = tin cậy giả. Appraisal mà không có recall đo được = kết luận
trên mẫu không biết thiên lệch ra sao.** Hai hệ hở hai nửa khác nhau của cùng một vấn đề.

---

## 3. Trục 2 — năng lực nghiên cứu thực tế

Hai hệ trả lời hai câu hỏi khác nhau, không phải hai phiên bản của cùng một thứ:

- **Evisyn** trả lời: *"Cho tôi một chương tổng quan 10.000 từ trên ~100 bài, mọi câu truy được về
  nguồn, PRISMA đầy đủ, xuất `.docx` đúng style tạp chí."*
- **MRA_3** trả lời: *"Bằng chứng về X chắc đến đâu, ai mâu thuẫn ai, chỗ nào là đồng thuận chỗ nào
  còn tranh cãi, tôi nên tin điều gì và với mức tự tin nào."*

| Năng lực | Evisyn | MRA_3 |
|---|---|---|
| Độ phủ tìm kiếm | 4 DB + phân trang đến hết + nhập Scopus/WoS/Embase | MCP (PubMed/bioRxiv/CT.gov/Consensus) + ledger tự kiểm |
| Sàng lọc | prefilter tất định + LLM verdict + 2 recall floor đo được | LLM thuần, không có sàn recall |
| Khử trùng lặp | script, ngưỡng cố định (fuzzy 0,9 · yearGuard 1 · blockPrefix 12) | LLM |
| PRISMA | `prisma.json/csv/svg` do script sinh, nhãn trung thực với pipeline thật | LLM kể trong search log |
| Chống bịa trích dẫn | pool đóng + audit script + gate xuất bản | store trên đĩa + `citation_audit.py` + verifier LLM |
| Xác minh trích dẫn verbatim | **6 khóa, QUOTE + NUMBER cấp ký tự** | không có |
| Trích số | regex có kiểu + card full-text | `extract_numbers.py`, 5 bucket |
| Thẩm định chất lượng | **không có** | GRADE + 4 công cụ RoB |
| Xử lý mâu thuẫn | không có | bắt buộc giữ, không được xóa phe thiểu số |
| Full text | opt-in, mặc định tắt | mặc định đòi, có gate |
| Đầu ra | `.docx`/`.tex`/`.bib`/`.ris`/PRISMA SVG | `.md` |
| Ngôn ngữ | Anh | Việt |

**Kết luận trục 2:** Evisyn mạnh hơn ở **recall, traceability, quy mô, khả năng tái lập**. MRA_3 mạnh
hơn ở **chiều sâu phán đoán**. Với một chương tổng quan luận án hoặc một bài nộp tạp chí y học, hội
đồng và phản biện sẽ hỏi cả hai — nhưng câu hỏi họ hỏi *trước* là câu của MRA_3 ("bằng chứng chắc đến
đâu"), còn câu họ dùng để *đánh trượt* là câu của Evisyn ("số này lấy ở đâu, tìm kiếm có tái lập
được không").

---

## 4. Trục 3 — lộ trình nâng cấp MRA_3

### 4.1 Ba phương án chiến lược

| | Mô tả | Đánh giá |
|---|---|---|
| **A. Dùng song song, không hợp nhất** | Evisyn làm tầng recall + traceability + xuất bản; MRA_3 làm tầng thẩm định. Nối bằng cách chuyển `citation_pool.json` → `reference/<topic>.md`. | **Khuyến nghị.** Rẻ nhất, không đụng bản quyền, khai thác đúng thế mạnh mỗi hệ, dùng được ngay. |
| **B. Port năng lực Evisyn vào MRA_3** | Viết lại các tầng tất định trong MRA_3 theo ý tưởng Evisyn. | Đúng hướng dài hạn, nhưng tốn công. Là nội dung P4–P8 dưới đây. |
| **C. Port thẩm định vào Evisyn** | Thêm GRADE/RoB vào Evisyn. | **Không nên.** `AGENTS.md` là sản phẩm có bản quyền của người khác; sửa nó là fork trái phép, và chính Evisyn ghi lại bài học fork là hỏng. |

### 4.2 Roadmap P4 → P8 (nối tiếp P1/P2/P3 đã có)

Xếp theo **tỷ lệ giá trị / công sức**, không theo số thứ tự.

**P5 — Bộ test tự động cho harness _(làm trước, rẻ nhất)_**
Hiện MRA_3 có 3 script Python và 3 test case chạy tay. Viết `unittest` cho `citation_audit.py`,
`extract_numbers.py`, `validate_search_log.py` với fixture PASS/FAIL sẵn có, gộp vào một lệnh
`python -m unittest discover`. Chi phí: một buổi. Giá trị: mọi sửa đổi harness sau này có lưới an toàn
— đúng nguyên tắc "ratchet" của hiến pháp, nhưng thi hành được bằng máy.

**P4 — Pipeline tất định cho sàng lọc & PRISMA _(lỗ hổng lớn nhất còn lại)_**
Hiện MRA_3 để LLM kể luồng PRISMA. Viết bằng Python stdlib: `normalize.py` → `dedup.py` →
`prefilter.py` → `screen_worksheet.py` → `prisma.py`. Ba chi tiết đáng học nguyên vẹn từ Evisyn:
- **Hai sàn recall.** `min_candidates` (pool nhỏ hơn sàn thì đọc hết, không cắt) và
  `full_coverage_floor` (bài khớp **mọi** concept không bao giờ bị cắt). Lý do đo được: cắt 25% một
  pool 154 bài đã bỏ 47 bài khớp cả 4 concept chỉ vì tiêu đề không lặp lại cụm từ.
- **Prefilter chỉ CỘNG điểm, không TRỪ.** Bài ngoài phạm vi xếp sau chứ không bị phạt.
- **Rỗng nghĩa là KHÔNG BIẾT, không phải NGOÀI PHẠM VI.** Ba trạng thái `in`/`out`/`unknown`.
Đầu ra: `prisma.json` + sơ đồ, nhãn trung thực với pipeline thật (nếu xét theo title+abstract thì
ghi đúng như vậy, không mượn hộp của review full-text rồi điền `n/a`).

**P8 — Khóa xác minh trích dẫn verbatim kiểu 12F**
MRA_3 đã đòi full text nhưng **không có khóa nào** kiểm câu trích có thật nằm trong nguồn. Hai khóa
đáng port nhất, viết lại bằng Python:
- **QUOTE** — substring verbatim; lệch một ký tự thì thẻ bị TỪ CHỐI, không phải cảnh báo.
- **NUMBER** — con số trong claim phải xuất hiện trong chính quote đó, không phải "ở đâu đó trong bài".
Đây là thứ nâng `citation_audit.py` từ *"trích dẫn truy được về pool"* lên *"câu này có thật trong
nguồn"* — đúng khoảng trống mà chính script P1 tự khai là không kiểm được.
Kèm nguyên tắc của Evisyn: **không bao giờ nới ngưỡng để cho nhiều bài lọt qua hơn.**

**P7 — Mở rộng và đo độ phủ**
- Thêm nguồn no-key bên cạnh MCP hiện có: **Europe PMC · OpenAlex · Semantic Scholar**. Cả ba đều
  không cần key, gọi thẳng bằng HTTP.
- Thêm **Elicit MCP** (`create_systematic_review`, `search_papers`, `search_trials`) — session này đã
  có sẵn; `literature-retrieval/SKILL.md` hiện chưa nhắc đến. Đây là khoảng trống năng lực rõ nhất
  giữa MRA_3 và những gì Claude cung cấp sẵn.
- Thêm nhập file export **Scopus/WoS** từ đĩa (bước 2B của Evisyn) — người dùng có tài khoản thư viện
  thì đây là nguồn recall lớn nhất, và harness không cần credential nào.
- **Throttle theo host + học từ 429**, thay vì mỗi script tự đoán khoảng cách.
- **Đo thật thay vì tự thuật:** ghi lại độ phủ full-text, tỷ lệ OA, số bài mất do mỗi bước cắt.

**P6 — Tầng xuất bản**
CSL + Pandoc → `.docx` theo style tạp chí đích; export `.ris/.bib/.nbib` cho EndNote/Zotero; sơ đồ
PRISMA dạng ảnh. Claude đã có sẵn skill `docx` và `pdf`, nên phần lớn là nối dây chứ không phải viết
mới. Kèm **gate xuất bản kiểu bước 15**: từ chối xuất bản chính thức nếu audit chưa PASS.

### 4.3 Thứ KHÔNG nên port

- **Viết từ abstract.** Trái L-005 của chính MRA_3. Giữ nguyên mặc định đòi full text.
- **`target_words` 10.000 mặc định.** MRA_3 hỏi độ dài ở Phase 0 (L-015) — đó là cách đúng; một con số
  mặc định lớn khuyến khích viết dài hơn bằng chứng cho phép (R2).
- **Dừng sau mỗi bước.** 19 lần dừng thủ tục làm loãng ý nghĩa của cổng. 4 cổng chọn theo nội dung của
  MRA_3 tốt hơn — giữ nguyên.
- **Bỏ thẩm định.** Hiển nhiên, nhưng cần nói rõ: đừng vì Evisyn nhanh hơn mà cắt GRADE/RoB.

### 4.4 Đường nối cụ thể cho phương án A (dùng song song)

```
Evisyn bước 1→12E            →  cầu nối          →  MRA_3 Phase 3→7
(recall, dedup, PRISMA,         citation_pool.json    (Research Map gate,
 pool đóng, metadata)           → reference/<topic>.md GRADE/RoB, steelman,
                                                       viết tiếng Việt, QA)
                             ←  Evisyn bước 15    ←
                                (.docx theo CSL)
```
Cần viết đúng **một** script chuyển đổi: `citation_pool.json` (Evisyn) → `reference/<topic>.md`
(định dạng store của MRA_3, có PMID/DOI/NCT + ngày). Đây là hạng mục rẻ nhất trong toàn bộ tài liệu
này và mở khóa được cả hai thế mạnh ngay lập tức.

---

## 5. Việc cần làm ngay với chính repo MRA_3

Không liên quan Evisyn, phát hiện trong lúc khảo sát:

1. **`26260733_Reddy_TOCCASTAR_2015.html` 18 MB nằm ở thư mục gốc repo** — phải chuyển vào
   `source/af-ablation-metrics/` (bản sao đã có ở đó).
2. **`main` đang vi phạm chính workflow branch-per-study của nó.** `CLAUDE.md` quy định dữ liệu
   nghiên cứu nằm trên nhánh `review/<topic>`, nhưng `main` đang mang `_workspace/`,
   `_workspace_prev/`, `_workspace_tc1_metformin/`, `source/` (~40 full-text) và `reviews/`.
3. **`literature-retrieval/SKILL.md` chưa nhắc Elicit** dù MCP đã sẵn sàng trong môi trường.
