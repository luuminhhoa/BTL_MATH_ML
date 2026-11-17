# Nhật ký Prompt đầy đủ (`PROMPT_LOG.md`)

> **Hướng dẫn điền (theo quyết định D17):**
> - Mọi lần tương tác với AI để sinh mã, viết test, gỡ lỗi hoặc giải thích toán học đều phải được ghi lại tại đây theo thứ tự thời gian.
> - **Không bịa đặt** số liệu, kết quả chạy hoặc lỗi chưa từng xảy ra.
> - Các prompt tiêu biểu của từng chương (tối thiểu 2 prompt/chương, gồm ít nhất 1 prompt AI trả lời sai hoặc chưa tốt) được trích sang `chapters/chX_*/prompts.md`.

## Thông tin công cụ AI sử dụng
- Công cụ: *(điền tên & phiên bản công cụ, ví dụ: Claude / Gemini / Cursor / Copilot)*
- Thành viên nhóm & tỷ lệ đóng góp: *(điền khi nộp bài)*

---

## Mẫu ghi một mục

```markdown
### [ChX-NN] <Tiêu đề ngắn gọn>
- **Người thực hiện:** <Tên thành viên>
- **Thời gian:** YYYY-MM-DD
- **Mục tiêu:** <Hàm / module / test cần làm>
- **Prompt:**
  > ...
- **Kết quả AI:** <Tóm tắt ngắn gọn hoặc đoạn mã chính>
- **Kiểm chứng:** <Kết quả chạy test / đối chiếu oracle: ĐẠT hoặc SAI kèm sai số>
- **Nguyên nhân (nếu sai):** <AI sai ở bước nào?>
- **Prompt sửa lỗi (nếu có):**
  > ...
- **Kết quả cuối:** <Đạt, sai số ...>
- **Bài học rút ra:** <1–2 câu>
```

---

*(Bắt đầu ghi các mục thực tế bên dưới dòng này)*

### [Setup-01] Hoàn thiện khung dự án và thiết lập tự động ghi Prompt Log
- **Người thực hiện:** Sinh viên + AI Agent (Antigravity)
- **Thời gian:** 2026-11-17
- **Mục tiêu:** Dựng khung dự án `ToanHocChoMachineLearning` (`mlmath`) theo `KIEN_TRUC.md`, `QUYET_DINH_KIEN_TRUC.md`, `QUY_UOC_DAT_TEN.md`, `HOP_DONG_MODULE.md` và cập nhật quy tắc tự động ghi Prompt Log.
- **Prompt:**
  > hoàn thiện tiếp phần đang dang dở ( khung project ) cho folder BTL Toán ML nếu cần kiến thức j thì tìm thêm trong folderr mẹ nha
  > với sao không tự động ghi prmot log z bạn thêm tự động ghi promt log vào trong ai rule đi
- **Kết quả AI:**
  - Tạo đầy đủ cấu trúc `docs/`, `handoff/`, `flow/`, `src/mlmath/` (hoàn chỉnh tầng `loi`, `tien_ich`, `dich_vu`, `giao_dien` và các stub đúng hợp đồng cho `chuong_1_ma_tran` … `chuong_6_uoc_luong`, `ch1.py` … `ch6.py`), `chapters/ch1_*` … `ch6_*`, `integration/`, `notebooks/`, `reports/`, `tests/unit/`.
  - Bổ sung quy tắc bắt buộc AI tự động nối mục mới vào `docs/PROMPT_LOG.md` sau mỗi lượt làm việc trong `flow/RULES.md`, `docs/CLAUDE.md`, `docs/AGENTS.md` và `flow/checklist.md`.
- **Kiểm chứng:**
  - `python3 -m unittest tests/unit/test_tien_ich.py -v`: ĐẠT (6/6 tests OK).
  - `test_khong_dung_thu_vien_cam_trong_mlmath()` (`tests/unit/test_cam_thu_vien.py`): ĐẠT (không phát hiện vi phạm D03).
  - `PYTHONPATH=src python3 -m mlmath.giao_dien liet-ke` và import toàn bộ `mlmath`, `ch1`…`ch6`: ĐẠT.
- **Nguyên nhân (nếu sai):** Không có.
- **Kết quả cuối:** Đạt; khung dự án sẵn sàng cho bước Pilot và triển khai Chương 1.
- **Bài học rút ra:** Cần ghi rõ quy tắc tự động ghi `docs/PROMPT_LOG.md` ngay trong `flow/RULES.md` và các tệp hướng dẫn AI (`CLAUDE.md`, `AGENTS.md`) để mọi phiên làm việc đều lưu vết đầy đủ.

### [Setup-02] Rà soát trùng lặp và đổi tên tài liệu sang tiếng Việt
- **Người thực hiện:** Sinh viên + AI Agent (Antigravity)
- **Thời gian:** 2026-11-17
- **Mục tiêu:** Loại bỏ các tệp trùng lặp giữa `docs/` và `handoff/`, chuyển tên các tệp tài liệu nội bộ sang tiếng Việt không dấu và cập nhật tham chiếu.
- **Prompt:**
  > bạn rà soát lại các file bị trừng lặp đổi tên file sang tiếng việt
- **Kết quả AI:**
  - Xóa 2 tệp trùng lặp ở `docs/` (`ARCHITECTURE_DECISIONS.md`, `MODULE_CONTRACTS.md`) và giữ bản duy nhất trong `handoff/`.
  - Đổi tên 7 tệp trong `handoff/` (`QUYET_DINH_KIEN_TRUC.md`, `HOP_DONG_MODULE.md`, `TOM_TAT_DU_AN.md`, `KE_HOACH_TRIEN_KHAI.md`, `CHUAN_VIET_MA.md`, `CHIEN_LUOC_KIEM_THU.md`, `CONG_VIEC_TIEP_THEO.md`) và `reports/outline.md` → `reports/de_cuong.md`; cập nhật tham chiếu trong 61 tệp.
  - Giữ nguyên các tên tệp bắt buộc theo đề bài (`README.md`, `PROMPT_LOG.md`, `flow/RULES.md`, `chapters/*/spec.md`, `prompts.md`, `analysis.md`, `reports/reflection.md`).
- **Kiểm chứng:** `test_tien_ich.py` (6/6 OK) và `test_cam_thu_vien.py` (OK).
- **Nguyên nhân (nếu sai):** Không có.
- **Kết quả cuối:** Đạt.
- **Bài học rút ra:** Khi đổi tên tài liệu, cần giữ nguyên các tên tệp cố định trong mục Sản phẩm nộp của đề bài để tránh sai lệch khi chấm.

### [Setup-03] Làm gọn dự án và chú thích chi tiết cấu trúc trong README
- **Người thực hiện:** Sinh viên + AI Agent (Antigravity)
- **Thời gian:** 2026-11-17
- **Mục tiêu:** Dọn bỏ các thư mục/tệp dư thừa và chú thích chi tiết từng mục trong cây thư mục của `README.md`.
- **Prompt:**
  > bạn xem cấu trúc thư mục trong readme bạn chú thích kĩ lại xem xét các file/ thư mục rác bỏ bớt đi làm gọn lại project
- **Kết quả AI:**
  - Xóa `notebooks/` (trống), `docs/TONG_QUAN.md` và `handoff/TOM_TAT_DU_AN.md` (trùng nội dung với `README.md`), `chapters/*/THIET_KE.md` (trùng vai trò với `spec.md`), cùng `.DS_Store` và `__pycache__/`.
  - Cập nhật mục 4 trong `README.md` với chú thích rõ ràng vai trò từng thư mục và tệp chính.
- **Kiểm chứng:** `test_tien_ich.py` (6/6 OK) và `test_cam_thu_vien.py` (OK).
- **Nguyên nhân (nếu sai):** Không có.
- **Kết quả cuối:** Đạt.
- **Bài học rút ra:** Giữ cấu trúc gọn, mỗi thông tin chỉ có một nguồn duy nhất giúp tránh lệch tài liệu khi phát triển.
