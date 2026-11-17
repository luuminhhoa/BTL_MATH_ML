# Checklist trước khi hoàn thành một hàm / một chương

## Checklist cho mỗi hàm
- [ ] Đã có mục đặc tả trong `chapters/chX_*/spec.md` trước khi sinh mã.
- [ ] Đã có test oracle trước hoặc song song khi sinh mã.
- [ ] Đúng tên hàm, tham số, kiểu trả về trong `handoff/HOP_DONG_MODULE.md`.
- [ ] Gọi `xac_thuc_*` ở đầu hàm, không sửa đổi mảng đầu vào (copy nếu cần).
- [ ] Ghi bước vào `nhat_ky` (dùng `NhatKyTinhToan.rong()` khi `nhat_ky is None`).
- [ ] Không có `print`, không ghi file, không `except:` trần.
- [ ] Đầy đủ type hints và docstring tiếng Việt có dấu.
- [ ] `pytest tests/unit/test_cam_thu_vien.py` PASS.
- [ ] Tất cả unit test + oracle test của hàm PASS.
- [ ] Đã đọc hiểu và tự giải thích được từng dòng mã.
- [ ] AI Agent đã tự động nối mục mới vào `docs/PROMPT_LOG.md` với kết quả kiểm chứng thực tế.

## Checklist cho mỗi chương
- [ ] Đủ các hàm bắt buộc theo đề và `HOP_DONG_MODULE.md`.
- [ ] Đủ bài tập mẫu từ bài giảng + tối thiểu 2 bài tự đặt (1 cơ bản, 1 ứng dụng ML) trong `examples/`.
- [ ] Đã chạy `doi_chieu/` và lưu kết quả thật vào `outputs/`.
- [ ] Đã cập nhật bảng ánh xạ trong `chapters/chX_*/src/README.md`.
- [ ] Đã hoàn thiện `chapters/chX_*/prompts.md`, `NHAT_KY.md`, `analysis.md` (kèm trả lời câu hỏi phản biện).
