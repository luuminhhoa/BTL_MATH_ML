# Các công việc tiếp theo (`CONG_VIEC_TIEP_THEO.md`)

Khung dự án đã được khởi tạo hoàn chỉnh (cấu trúc thư mục, tài liệu `flow/`, `docs/`, `handoff/`, hạ tầng `loi`, `tien_ich`, `dich_vu`, `giao_dien`, các stub module 6 chương theo đúng `HOP_DONG_MODULE.md`, và `test_cam_thu_vien.py`).

Thứ tự thực hiện tiếp theo:
1. **Chạy thử khung & kiểm tra hạ tầng:**
   - Cài đặt môi trường (`pip install -r requirements.txt && pip install -e .`).
   - Chạy `pytest tests/unit/test_cam_thu_vien.py tests/unit/test_tien_ich.py`.
2. **Thực hiện Pilot (`flow/pilot/README.md`):** Chọn 1 hàm nhỏ (ví dụ `nghich_dao_gauss_jordan` hoặc `gradient_so`), chạy đủ 8 bước flow và ghi lại vào `PROMPT_LOG.md`.
3. **Triển khai lần lượt Chương 1 → Chương 6:**
   - Viết `chapters/chX_*/spec.md` + test oracle trước.
   - Cài đặt mã trong `src/mlmath/chuong_N_*/` và đăng ký vào `dich_vu/dang_ky.py`.
   - Hoàn thiện `examples/`, `doi_chieu/`, `analysis.md`, `prompts.md`, `NHAT_KY.md`.
4. **Phần C:** Cài đặt `integration/src/pipeline.py` và hoàn thiện `reports/reflection.md` từ số liệu thực tế.
