# Chạy thử và đánh giá harness tinh gọn

Bản này dùng **4 agent tính cả lead**, 2 cổng bắt buộc (Scope và Research Map gộp corpus),
appraisal/coach có điều kiện. Script và kiểm thử cơ học không chứng minh chất lượng tổng quan
y văn hoặc phần trăm tiết kiệm token. Chỉ dùng kết quả A/B thực tế để kết luận hai điều đó.

## 1. Chạy kiểm thử cơ học trước

Mở terminal tại thư mục repo, cần Python 3.10 trở lên.

PowerShell:
```powershell
$env:PYTHONUTF8 = "1"
python -m unittest discover -s .claude/tests -t .claude/tests
```
Nếu máy bạn dùng `py`, thay `python` bằng `py -3`. Trên máy Phong tại thời điểm triển khai,
Python hệ thống chưa cài; có thể dùng runtime sẵn của Codex:
```powershell
$env:PYTHONUTF8 = "1"
& "$env:USERPROFILE/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/python.exe" -m unittest discover -s .claude/tests -t .claude/tests
```
Linux/macOS:
```bash
PYTHONUTF8=1 python3 -m unittest discover -s .claude/tests -t .claude/tests
```
PASS cần exit 0. Các test gồm pipeline có sẵn, lỗi mapping/card/citation/số, thiếu abstract,
lọc lessons, artifact/manifest và phép so sánh usage. Không cần API, model hay tiền Elicit.
Bản baseline có lỗi đường dẫn test trên Windows; để kiểm baseline nguyên trạng có thể dùng
Linux/WSL. Đừng sửa code baseline rồi vẫn gọi nó là cùng commit chưa sửa.

## 2. Chạy một review trên bản mới

Sau khi fetch nhánh mới, tạo nhánh nghiên cứu riêng. Nếu đã ở nhánh candidate, dùng HEAD:
```bash
git fetch origin
git switch -c review/lean-pilot origin/codex/lean-four-agent-harness
```
Mở thư mục trong Claude Code hoặc host agent bạn dùng, bắt đầu một phiên sạch rồi gửi:

> Dùng medical-review-orchestrator để tổng quan [chủ đề]. Mục đích: nghiên cứu;
> đối tượng đọc: [chuyên khoa]; khoảng 2000 từ; nguồn 2020–2026-09-07;
> tiếng Việt; source/[topic] là thư mục tài liệu tôi cung cấp; không có export ngoài.
> Ghi actual model/settings và usage của toàn bộ agent nếu host cung cấp;
> không có số đo thì ghi null. Không dùng công cụ trả phí nếu chưa được tôi cho phép.

Kỳ vọng: không hỏi lại các scope field đã rõ; lead lập protocol, retriever thu thập/sàng lọc,
rồi dừng ở Research Map để bạn duyệt cả danh sách nguồn, full text và gaps.
Đọc map rồi tự gửi approve/edit/reject. Nếu cần thêm PDF, nói rõ; hứa cung cấp PDF không phải approve.
Sau appraisal, bất định thông thường được phản ánh trong bài; thay đổi phạm vi/giả định quan trọng
mới cần hỏi tiếp. Coach chỉ chạy có lý do. Bạn nhận Markdown và bộ bằng chứng kiểm tra.

Claude Code dùng `.claude/agents/` trực tiếp. Host khác phải đọc role file và ánh xạ sang công cụ/model
thực sự có sẵn; ghi cấu hình, không giả định tên `opus`/`sonnet` có cùng ý nghĩa ở mọi host.
Lead là phiên chính; không spawn thêm review-lead thành worker thứ năm.

Đầu ra cần xem:

| File trong `_workspace/` | Bạn kiểm gì |
|---|---|
| `03_research_map.md` | Đúng câu hỏi, đủ nguồn chính, gaps thật, đầy đủ status full text |
| `04_appraisal.md` | RoB/GRADE có lý do, mâu thuẫn và ngoại suy được nêu |
| `06_final_review.md` | Kết luận đúng nguồn, đủ sắc thái, đọc dễ hiểu |
| `06a_verification_report.md` | Lỗi đã sửa; QA đọc nguồn; không tự nhận có human review |
| `06b_citation_audit.md`, `06d_claim_audit.json` | PASS trên đúng bản cuối |
| `06c_manifest.md` | Scope, quyết định, confidence index và hash artifacts |

## 3. So sánh baseline với candidate một cách công bằng

Baseline cố định: `ad6477b52e94f70c8befd615adc5d7c0df7bbd5a`.
Candidate: ghi **commit SHA thực tế**, không chỉ tên nhánh có thể thay đổi.
Tạo hai checkout riêng sau khi candidate đã commit (đừng dùng HEAD có sửa chưa commit):
```bash
git fetch origin
git worktree add --detach ../mra3-baseline ad6477b52e94f70c8befd615adc5d7c0df7bbd5a
git worktree add --detach ../mra3-candidate origin/codex/lean-four-agent-harness
```
Nếu bản clone quá nông không có baseline, chạy `git fetch origin ad6477b52e94f70c8befd615adc5d7c0df7bbd5a`
rồi thêm worktree. Không ghi đè workspace của review đang chạy. Dữ liệu thử ở hai checkout riêng,
không đưa PDF hay kết quả nghiên cứu vào nhánh main. Mỗi lần lặp dùng workspace/phiên sạch.

**Hai phép thử riêng, không cộng lẫn số đo:**

1. **Frozen corpus:** chuẩn bị bộ tài liệu thật một lần và chép cùng bytes vào hai bên (nguồn,
   metadata, danh sách records đã truy hồi và provenance). Chỉ chép đầu vào, không chép appraisal,
   draft, lessons mới hay QA của bên kia. Dùng cùng cutoff, tiêu chí và thông tin truy hồi;
   nói rõ Phase 2 dùng dữ liệu đã truy hồi, không tuyên bố vừa live search. Từ corpus đó mỗi
   harness thực hiện map/approval/appraisal/synthesis/QA riêng. Đây là phép thử phần downstream.
2. **Live retrieval:** cùng prompt, tool access, cutoff và chạy gần nhau; corpus có thể khác.
   Đánh giá khả năng tìm nguồn quan trọng và mất recall riêng. Khác biệt corpus ở đây là kết quả,
   không phải điều kiện cấm. Ghi đủ query, cap, lỗi nguồn, ngày giờ và export restrictions.

Có thể lấy đầu vào thật từ các nhánh archive `review/test-cases`, `review/cryoballoon-pfa-af`, v.v.
Chỉ dùng tài liệu bạn có quyền truy cập. Manifest checksum của bộ frozen phải liệt kê đường dẫn tương
đối + SHA-256 từng file theo thứ tự ổn định; hash manifest đó thành `corpus_sha256`. Đừng dùng tên
folder như bằng chứng rằng hai corpus giống nhau. Với live, hash từng corpus kết quả riêng.

Giữ giống nhau: exact prompt, model thực tế theo chức năng, reasoning/settings, công cụ, budget,
nguồn đầu vào, mục tiêu độ dài, quyền trả phí và môi trường host. Trong vòng đầu ưu tiên cùng một
model có năng lực cho mọi vai trò ở cả hai bên để cô lập thay đổi kiến trúc. **Sau đó** mới thử routing
model rẻ hơn; không trộn hai thay đổi vào một kết luận. Lưu settings vào một file chung, dùng ID/hash
của file làm `settings_id`. Đổi thứ tự baseline/candidate giữa các lần lặp để hạn chế ảnh hưởng cache.

Bắt đầu với 3 loại ca trong `evals/lean/cases.json`: EASY, HARD/mâu thuẫn, thiếu full text quan trọng.
Giữ prompt lịch sử trong `test-cases.md` nguyên văn; bổ sung cùng một scope packet ở cả hai bên cho
các field còn thiếu. Khóa “nay” thành cùng cutoff trong packet. Với ca thiếu full text, chọn trước
một bài quyết định và gỡ nó khỏi cả hai bộ đầu vào; không giả lập kết quả y khoa.
Một cặp mỗi ca chỉ là pilot; khuyến nghị ít nhất 3 lần lặp/ca trước khi kết luận tiết kiệm ổn định.
Mỗi lần cần bạn tự duyệt gate thật; không dùng một prompt giả làm lời approve của người dùng.

## 4. Ghi số đo thật

Copy `evals/lean/runs.template.json` thành file kết quả ngoài main. Thay các hash null bằng giá trị
thực và điền số đo từ log/export của host; chỉ nhập số đã quan sát, trường không có để null.
Template cố ý chưa chạy được như một kết quả hợp lệ khi hash còn thiếu.

- `input_tokens_total`: tổng input của lead + mọi worker + retry. Chuẩn hóa **đã bao gồm cache read
  và cache write**. Nếu provider báo input tổng đã gồm cache, không cộng cache lần nữa.
- `output_tokens_total`: tổng output; reasoning theo định nghĩa provider, chỉ tính một lần.
- `cost_usd`: chi phí thực của toàn run, kể cả worker/retry/công cụ trả phí; nếu chỉ có token hoặc
  gói thuê bao không quy được giá tiền thì null, không tự đổi sang giá API không áp dụng.
- `duration_seconds`: elapsed của run, thống nhất có/không thời gian chờ người duyệt; khuyến nghị
  ghi thời gian active riêng trong log gốc để giải thích latency.
- `gate_questions`: số lượt yêu cầu quyết định từ người dùng; không đếm commentary.
- `repair_rounds`: số vòng sửa sau verifier; không đếm lượt tool.

Giữ log raw để kiểm tra cách chuẩn hóa; cached token có thể rẻ hơn nhưng vẫn thuộc input token.
Nhận xét “prompt ngắn hơn X%” không phải đo “toàn bộ review tiết kiệm X% token”.

## 5. Đánh giá chất lượng trước khi nhìn giá

Nhờ người có chuyên môn đọc hai bài gắn nhãn A/B, ẩn tên model/phiên bản/chi phí. Chọn trước
các nguồn quan trọng và các tình huống dễ hiểu sai, không chọn đáp án theo bài candidate.
Đọc nguồn để đếm: `critical_errors`, `unsupported_claims`, `numeric_errors`, `missing_key_studies`,
`certainty_errors`, `lost_nuance`, `gate_violations`. Một lỗi có thể thuộc nhiều cột; không cộng các cột
thành số lỗi độc lập. Kèm bảng lỗi với claim/source/reason trong hồ sơ gốc. Điền `human_reviewed:true`
chỉ sau khi người thực đã đọc; AI judge là hỗ trợ, không đủ để bật cờ này.

So cả rubric theo tiêu chí và tính hữu ích: đúng đối tượng, đủ subgroup, không biến ngoại suy thành
kết luận trực tiếp, không làm nhạt bằng chứng mạnh. Vận hành gate được chấm theo policy của từng
phiên bản; ít gate hơn theo thiết kế không tự động là vi phạm. Research Map vẫn cần approve thật.

Chạy trình so sánh từ candidate:
```bash
python .claude/skills/medical-review-orchestrator/scripts/evaluate_runs.py --runs PATH_TO_RUNS.json --out comparison.json
```
Exit 0 / COMPARISON_READY: dữ liệu đủ để so, **không phải tự động phê duyệt harness**.
Exit 1: INCOMPLETE hoặc REGRESSION; mở report xem nguyên nhân. Exit 2: input không hợp lệ/không
so sánh được. Script ghép theo case + frozen/live + repeat, từ chối settings/prompt/corpus frozen
khác nhau; null không thành 0. Phần trăm chỉ tính khi baseline >0. Số âm là candidate dùng ít hơn.
Không tổng hợp một nhóm thiếu số đo hoặc gộp live với frozen.

## 6. Quyết định giữ hay chỉnh tiếp

Không chấp nhận candidate có lỗi nghiêm trọng hoặc vi phạm gate, kể cả baseline cũng mắc lỗi.
Nếu mất nguồn quan trọng, tăng lỗi claim/số/certainty hoặc mất sắc thái, sửa và chạy lại ca liên quan.
Chỉ chấp nhận tiết kiệm khi số đo toàn run giảm qua nhiều cặp, chất lượng không giảm ở các tiêu chí
quan trọng và số vòng sửa không tăng bất thường. Các ca pilot nhỏ không chứng minh non-inferiority
thống kê. Ghi rõ mức kiểm chứng thực tế, giới hạn và quyết định; không lấy rubric tự chấm làm bằng
chứng duy nhất. Khi đạt, mới dùng candidate làm bản mặc định/merge vào main.

Kiểm tra nhanh chính sách trước full run: vague topic → hỏi trước search; full scope → không hỏi lại;
map chưa approve → không appraisal; bất định thường → viết có calibration; đổi scope → hỏi lại map;
sửa một claim → chỉ sửa phần liên quan và chạy lại global checks. Unit tests không tự thực hiện các
tương tác model/người dùng này; cần phiên chạy thật và transcript để đánh giá.
