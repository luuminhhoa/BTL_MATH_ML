# Bảng Rủi ro & Cách phòng tránh (`flow/risks.md`)

| STT | Rủi ro | Biểu hiện | Cách phòng tránh / Kiểm chứng |
|---|---|---|---|
| 1 | **AI dùng hàm thư viện bị cấm** | AI tự động gọi `np.linalg.inv`, `np.linalg.det`, `@` ở Ch1 | Chạy `test_cam_thu_vien.py` bằng AST tự động |
| 2 | **Nhầm quy ước bố trí ma trận/đạo hàm** | Nhầm `P(B→S)` với `P(S→B)`; nhầm Jacobian `m×n` (slide) với `n×m` (chuẩn); nhầm `ddof=0` vs `ddof=1` | Tuân thủ `docs/QUY_UOC_DAT_TEN.md` §2; có test riêng kiểm tra hướng và kích thước |
| 3 | **Lỗi in trong slide bài giảng** | Ch2 VD2 in `(6,−4,1)` thay vì `(6,−4,5)`; Ch3 ghi `∇det(X)=0` khi `det X=0` | Áp dụng D10, D12, D16: kiểm tra oracle độc lập bằng định nghĩa/thư viện |
| 4 | **Sai số số học & pivot = 0** | Chia cho 0 khi phần tử trụ = 0; mất chính xác với ma trận gần suy biến | Chọn pivot lớn nhất theo trị tuyệt đối; đổi hàng khi cần; kiểm tra `so_dieu_kien` |
| 5 | **Test "cho có" (self-oracle)** | Test dùng chính hàm đang kiểm tra để tính đáp án kỳ vọng | Bắt buộc dùng oracle độc lập (tính tay, `numpy`/`scipy`/`sympy`, tính chất toán học) |
| 6 | **Bùng nổ độ phức tạp** | Chạy `dinh_thuc_laplace` hoặc `da_thuc_dac_trung` với `n` lớn | Giới hạn `n ≤ 9` cho đo thời gian Laplace, `n ≤ 6` cho `da_thuc_dac_trung` (D04) |
| 7 | **Sinh viên không hiểu mã AI viết** | Không giải thích được khi vấn đáp (−50% điểm) | Bắt buộc thực hiện Bước 5 của flow trước khi commit |
