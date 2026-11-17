# Mẫu Prompt chuẩn (`flow/prompt_templates.md`)

## 1. Mẫu sinh hàm thuật toán
```text
Vai trò: Trợ giảng lập trình toán cho Máy học.
Bối cảnh: Tôi đang cài đặt [tên hàm] trong module [src/mlmath/chuong_X_.../...] của thư viện mlmath.
Quy tắc bắt buộc:
- Chỉ dùng Python chuẩn và NumPy cơ bản; CẤM dùng [np.linalg.*, @ / np.dot nếu là Ch1].
- Tuân thủ chữ ký hàm trong handoff/HOP_DONG_MODULE.md và quy ước trong docs/QUY_UOC_DAT_TEN.md.
- Đầu hàm gọi xac_thuc_*, không làm biến đổi mảng đầu vào.
- Ghi các bước có ý nghĩa toán học vào nhat_ky (NhatKyTinhToan).
- Không print, không đọc/ghi file.
- Đầy đủ type hints và docstring tiếng Việt có dấu (công thức Unicode, đầu vào/ra, điều kiện, ngoại lệ, độ phức tạp).

Bài toán: [Mô tả công thức toán, kích thước ma trận, kiểu dữ liệu hỗ trợ].
Trước khi viết mã: Hãy nêu ngắn gọn các bước thuật toán và các trường hợp biên cần xử lý.
```

## 2. Mẫu sinh test Oracle & Trường hợp biên
```text
Vai trò: Kỹ sư kiểm thử toán học.
Nhiệm vụ: Viết bộ pytest cho hàm [tên_hàm] đặt tại [chapters/chX_.../tests/test_...py].
Yêu cầu 3 tầng kiểm thử:
1. Tầng tự cài & biên: ma trận 1x1, ma trận suy biến, pivot = 0 cần đổi hàng, kiểu Fraction/float64/complex128, đầu vào sai ném đúng LoiKichThuoc/LoiMaTranSuyBien.
2. Tầng đối chiếu thư viện (oracle): so sánh với [np.linalg.* / scipy.*] với rtol=1e-9, atol=1e-10.
3. Tầng tính chất toán học: ví dụ A @ A⁻¹ ≈ I, det(AB) ≈ det(A)det(B).
Lưu ý: Không dùng chính hàm đang test để tạo đáp án kỳ vọng. Seed ngẫu nhiên dùng np.random.default_rng(seed).
```

## 3. Mẫu gỡ lỗi (Debug)
```text
Hàm [tên_hàm] đang thất bại ở test [tên_test].
Đầu vào tối thiểu tái hiện lỗi: [...]
Kết quả thực tế: [...]
Kết quả kỳ vọng (từ oracle): [...]
Thông báo lỗi / Traceback: [...]
Hãy phân tích nguyên nhân gốc (toán học hoặc số học) và đề xuất bản sửa tối thiểu.
```

## 4. Mẫu yêu cầu giải thích mã (dùng cho bước 5)
```text
Hãy giải thích từng khối lệnh trong hàm [tên_hàm] vừa viết, đối chiếu trực tiếp với công thức toán học [công thức] và chỉ ra tại sao xử lý trường hợp biên [biên] lại đúng.
```
