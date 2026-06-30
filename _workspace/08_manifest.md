# Manifest — Proof Package (Phase Delivery)

**Topic:** Đặc điểm điện học, điện sinh lý nhĩ trái ở bệnh nhân rung nhĩ cao tuổi
**Delivered:** 2026-06-30

## 1. Scope line

Tổng quan tường thuật chuyên sâu (effort=full, ~3000–4000 từ) **+** bảng biến số đề xuất (CRF), tiếng
Việt, cho bác sỹ tim mạch/EP và học viên nghiên cứu, trích dẫn Vancouver, không giới hạn khoảng thời
gian xuất bản, dựa trên kho 72 bản ghi citable (REF-001…REF-074, trừ REF-046/REF-050).

## 2. Confidence list (major claims, GRADE + primary source)

| Claim | GRADE | Nguồn chính |
|---|---|---|
| Điện thế nhĩ trái giảm & LVZ lan rộng theo tuổi | Moderate | REF-001, 002, 042, 003 |
| AERP "kéo dài theo tuổi" — chỉ đo ở quần thể không-RN; giá trị tuyệt đối trong RN không xác định | Low | REF-042, 043, 044, 045 |
| **AFCL theo tuổi — GAP, không có dữ liệu phân tầng tuổi nào** | **Very Low / GAP** | REF-073 (chỉ baseline chung, không phân tầng tuổi) |
| CV giảm theo tuổi (đo trong nhịp xoang, không-RN) | Low | REF-074, 003, 051, 052 |
| SNRT/cSNRT kéo dài trong RN, đảo ngược sau chuyển nhịp | Low | REF-047, 049, 042 |
| PWD kéo dài dự báo RN mới & tái phát | Moderate | REF-037, 039, 042, 059 |
| Phân tán sóng P — bias công bố đã xác nhận | Low | REF-058, 059, 061 |
| SAECG filtered P-wave dự báo PAF/POAF | Moderate (công nghệ cũ) | REF-053, 054, 055, 058 |
| IAB tiến triển → RN/đột quỵ ở ≥70 tuổi (bằng chứng trực tiếp nhất) | Moderate (mạnh nhất) | REF-066, 068, 063, 064 |
| Trục sóng P bất thường → RN (mâu thuẫn nội tại nguồn 2.12 vs 2.10, trích cả hai) | Moderate | REF-070, 064 |
| PTFV1 → RN (ngưỡng không nhất quán 0,03 vs 0,04) | Low | REF-040, 064 |
| LA strain hồ chứa giảm theo tuổi, dự báo RN mới | Moderate | REF-023, 025, 024 |
| Rotor/CFAE — STAR AF II (RCT) bác bỏ giá trị hướng dẫn cắt đốt thêm | Moderate (âm tính) | REF-010, 005 |
| Kết cục cứng triệt đốt ở ≥75 tuổi — không chắc chắn, cần cá thể hóa theo frailty | Very Low | REF-018 (CABANA subgroup), 026 |

## 3. Open assumptions (Assumption Register — Law 5, đều xuất hiện trong Hạn chế §12.4)

A-1 (Cao) CV đo trong nhịp xoang · A-2 (Rất cao) AFCL không có dữ liệu cao tuổi · A-3 (Cao) AERP đo ở
quần thể không-RN · A-4 (Trung bình-cao) ngưỡng SAECG/PWD từ PAF vô căn trẻ · A-5 (Trung bình) cSNRT
không phân tầng tuổi · A-6 (Thấp-trung bình) IAB chủ yếu từ bệnh tim cấu trúc/suy tim · A-7 (Thấp)
hướng dẫn ESC/ACC còn hiệu lực · A-8 (Cao) không có dữ liệu Việt Nam (EP xâm lấn) · A-9 (Trung bình)
ngưỡng PTFV1 không nhất quán · A-10 (Trung bình) MA triệt đốt cao tuổi là dữ liệu quan sát · A-11
(Thấp-trung bình) AHRE ≈ RN lâm sàng.

## 4. Receipts index

| Artifact | Trạng thái |
|---|---|
| `00_protocol.md`, `00_scope_phase0.md` | Phase 0/1 |
| `01_search_log.md`, `02_corpus.md`, `02b_fulltext_request.md` | Phase 2 (Gate 2b cleared) |
| `03_research_map.md`, `research_map_gate_approval.md` | Phase 3 (hard gate, **CLEARED** — "ok") |
| `03b_numbers.md`, `04_appraisal.md`, `gate4b_approval.md` | Phase 4 (Gate 4b **CLEARED** — "bắt đầu viết") |
| `04b_crf_table_preview.md` | CRF table, cấu trúc người dùng duyệt 2026-06-30 |
| `05_draft_review.md` | Phase 5 (synthesis-writer) |
| `05b_coach.md` | Phase 5b (quality-coach) — **SHIP-AS-IS** |
| `06_verification_report.md`, `06_citation_audit_output.md` | Phase 6 (citation-verifier) |
| `06_final_review.md` | **Bản giao cuối cùng** |
| Rubric | **0.92 — EXCEEDED** |
| Audit | 6/6 Laws PASS · process PASS · scope PASS |
| Deterministic citation_audit.py | exit 0, 0 hard-fail, 95% coverage |

Lưu ý trung thực: manifest này xác nhận các bước đã chạy và kết quả thu được; mức độ kỹ lưỡng tổng thể
do citation-verifier (Phase 6) và hai cổng người dùng (Phase 3, Gate 4b) bảo chứng.
