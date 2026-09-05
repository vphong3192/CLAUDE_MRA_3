# CLAUDE_MRA_3 — Harness viết tổng quan y văn (bản có tầng kiểm tất định)

Harness đa-agent (do LLM lái) để sản xuất các bản **tổng quan y văn chuyên sâu, kiểu hệ thống** từ
nguồn sống, cập nhật (PubMed/PMC, bioRxiv/medRxiv, ClinicalTrials.gov, Consensus) — kèm hiến pháp 6
Luật, 4 cổng người-duyệt (Research Map là cổng cứng), GRADE/PRISMA, provenance trên đĩa, và một
**learning loop**.

Đây là bản fork từ `CLAUDE_MRA_2`, bổ sung **tầng kiểm tra tất định (deterministic layer)**: rút các
khâu *thuần cơ học* ra khỏi tay LLM, giao cho ba script chạy **sau** agent, **không gọi LLM, không
mạng**, cho kết quả **giống hệt mỗi lần chạy** và phát **PASS/FAIL bằng exit code** — để không thể
"tự thuyết phục" rằng đã đạt. Chiều sâu phán đoán (RoB/GRADE/tổng hợp/đa nguồn) vẫn nằm ở LLM; ba
script chỉ **thêm một sàn**, không thay thế.

> Luật vận hành đầy đủ: xem `CLAUDE.md` và `.claude/constitution.md`. Tầng tất định ghi ở change-log
> `CLAUDE.md` (P1/P2/P3) và lesson **L-039**.

---

## Triết lý cốt lõi

> Giữ NGUYÊN chiều sâu phán xét + đa nguồn của các agent LLM. CHỈ rút những tác vụ thuần cơ học
> (đếm, đối chiếu citekey/ID, bóc số nguyên văn, kiểm coverage, log recall) ra một tầng tất định
> chạy độc lập, sau agent, và không thể bị thương lượng.

Mỗi script đều tự in rõ **nó kiểm gì** và **KHÔNG kiểm gì** (truy vết ≠ ngữ nghĩa) — sàn cơ học
không thay con người/LLM soát nội dung.

---

## Tầng kiểm tất định — 3 script (Python stdlib, zero-dependency)

### P1 · Kiểm citation tất định — `.claude/skills/citation-verification/scripts/citation_audit.py`
Chạy **sau** agent `citation-verifier`, trước khi giao bài. Đối chiếu mọi citation trong bản thảo
với kho đóng `reference/<topic>.md` theo PMID/DOI/NCT.
```bash
python3 .claude/skills/citation-verification/scripts/citation_audit.py \
  --draft _workspace/06_final_review.md \
  --store reference/<topic>.md \
  --min-coverage-frac 0.4 \
  --out _workspace/06b_citation_audit.md
```
- **HARD-FAIL (exit 1 → không giao được, Luật 1):** `fabricated_citation`, `missing_in_store`,
  `placeholder_leftover` (`[N] [?] CITATION_NEEDED TODO [@NEW:…]`), `coverage_below_threshold`.
- **WARN (không chặn):** `number_not_in_source`, `uncited_claim`.
- **KHÔNG kiểm:** nguồn có *thực sự ủng hộ* câu không, số có *đúng* không, GRADE. → vẫn cần
  LLM-verifier + người soát ~10% câu.

### P2 · Bóc số tất định cho appraisal — `.claude/skills/evidence-appraisal/scripts/extract_numbers.py`
Chạy **trước** khi appraiser điền bảng chứng cứ. Bóc **nguyên văn** số từ kho vào 5 rổ/record:
`sample_sizes · percentages · p_values · confidence_intervals · ratios` (OR/RR/HR/aHR/MD/SMD/β/coef).
```bash
python3 .claude/skills/evidence-appraisal/scripts/extract_numbers.py \
  --store reference/<topic>.md --out _workspace/04a_numbers.md
```
Appraiser **nạp** số từ `04a_numbers.md` thay vì chép tay (diệt lỗi gãy thập phân / nhầm số
Methods thành kết quả). Rổ rỗng = "(none)", không bao giờ bịa. **KHÔNG kiểm:** số nào là outcome
chính vs nền — việc đó của LLM.

### P3 · Kiểm log recall/tái lập — `.claude/skills/literature-retrieval/scripts/validate_search_log.py`
Kiểm *định dạng* "Recall & reproducibility ledger" trong search log (offline).
```bash
python3 .claude/skills/literature-retrieval/scripts/validate_search_log.py \
  --log _workspace/02a_search_log.md
```
- **HARD-FAIL (exit 1):** thiếu ledger, thiếu cột, số không phải integer, `call` không có
  params/URL, hoặc verdict recall mâu thuẫn số (vd "complete ✓" nhưng `retrieved < total`).
- Ba thói quen retriever đi kèm: **probe đếm trước** (`esearch retmax=0`) · **phân trang tới
  `retrieved==total`** hoặc cap có lý do · **log call tái lập** (params/URL).
- **KHÔNG kiểm:** số có thật không, search có tốt không — chỉ kiểm log đầy đủ & tự nhất quán.

Mỗi thư mục `scripts/` đều có `fixtures/` minh hoạ đường PASS/FAIL, chạy offline, tất định.

---

## Bốn cổng người-duyệt (không bao giờ bỏ qua)
(1) Phase-0 xác nhận phạm vi · (2) Gate 2b sau retrieval · (3) **Research Map — cổng cứng** ·
(4) Gate 4b sau appraisal. Cả bốn chạy ở mọi mức effort (kể cả `tiny`); Research Map không có ngoại lệ.

## Workflow branch-per-study
`main` là công cụ tái dùng; mỗi nghiên cứu là một nhánh `review/<topic>` riêng. Khi xong và lesson
được duyệt, chỉ đồng bộ về `main` ba file tri thức: `lessons.md`, `evolution-log.md`,
`vi-terminology.md`.

## Bắt đầu một review
Kích hoạt skill `medical-review-orchestrator` (hoặc yêu cầu "review the evidence on <chủ đề>"). Đội
7 agent chạy: strategist → retriever → appraiser → writer → coach → verifier (+ lessons-curator).

## Cấu hình mặc định
PRISMA + GRADE · trích dẫn Vancouver · **ngôn ngữ output mặc định tiếng Việt** (chọn được mỗi review,
xác nhận ở Phase 0) · lesson chỉ lưu sau khi người dùng duyệt.
