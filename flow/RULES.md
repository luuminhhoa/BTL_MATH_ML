# Quy tắc Vibe Coding (`flow/RULES.md`)

Đây là nguồn quy tắc duy nhất cho việc sử dụng AI trong dự án `mlmath`.

## 1. Quy trình 8 bước bắt buộc
1. **Không sinh mã khi chưa có `spec.md` và test oracle.**
2. Sinh từng hàm nhỏ theo `handoff/HOP_DONG_MODULE.md`, không sinh cả chương trong một lần.
3. Sau khi AI sinh mã, sinh viên phải **đọc hiểu từng dòng** và có thể giải thích lại khi vấn đáp.
4. **Tự động ghi Prompt Log (Bắt buộc):** Sau mỗi lượt làm việc có sinh/sửa mã, viết đặc tả, viết test hoặc gỡ lỗi, AI Agent **phải tự động nối thêm một mục mới** vào cuối `docs/PROMPT_LOG.md` (theo đúng mẫu trong file đó). Nếu lượt làm việc thuộc Chương `X`, trích các prompt tiêu biểu (đặc biệt là lần AI sai hoặc sửa lỗi) vào `chapters/chX_*/prompts.md`. Chỉ ghi đúng prompt thực tế, kết quả kiểm chứng thực tế và nguyên nhân thật — không bịa đặt.

## 2. Ranh giới thư viện (Quyết định D03)
- **Chương 1 (`chuong_1_ma_tran/`):** CẤM dùng `@`, `np.dot`, `np.matmul`, `np.linalg.*`, `scipy.linalg.*`.
- **Từ Chương 2 trở đi:** Được dùng `@` cho phép nhân ma trận. Vẫn **CẤM** dùng `np.linalg.*` (`inv`, `solve`, `det`, `eig`, `eigh`, `cholesky`, `qr`, `lstsq`, `matrix_rank`, `norm`), `scipy.linalg.*`, `sklearn.*` trong mã tự cài (`src/mlmath/`).
- Các thư viện trên **chỉ** được phép xuất hiện trong `tests/`, `chapters/*/tests/`, `chapters/*/doi_chieu/`.
- Kiểm tra tự động bằng `pytest tests/unit/test_cam_thu_vien.py`.

## 3. Quy tắc kiến trúc (Quyết định D01, D02, D14, D15)
- Mã thuật toán chỉ nằm ở `src/mlmath/chuong_N_*/`. Cấm đặt logic trong `chapters/*/src/`.
- Tên gốc bằng tiếng Việt không dấu; alias tiếng Anh chỉ re-export trong `ch1.py … ch6.py`.
- Thuật toán thuần túy: không `print`, không ghi file, không đọc `argv`; nhận `nhat_ky: NhatKyTinhToan | None = None`.
- Ngoại lệ dữ liệu kế thừa `LoiDuLieu(ValueError)`, lỗi lặp kế thừa `LoiHoiTu(RuntimeError)`.

## 4. Trung thực học thuật (Quyết định D16, D17)
- Đáp án oracle phải kiểm chứng độc lập (tính tay theo định nghĩa, thư viện, tính chất toán học), không tin mù quáng vào đáp án in trong slide (có thể có lỗi in).
- Tuyệt đối không bịa đặt prompt log, kết quả chạy test, hay lỗi AI chưa từng xảy ra.
