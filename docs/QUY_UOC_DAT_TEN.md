# Quy ước đặt tên và quy ước toán học

Hai nhóm quy ước: (1) đặt tên trong mã và tài liệu; (2) cách bố trí dữ liệu toán học. Nhóm (2) quan trọng hơn vì sai quy ước tạo ra lỗi im lặng (kết quả sai nhưng chạy bình thường). Quyết định gốc nằm ở `handoff/QUYET_DINH_KIEN_TRUC.md`.

## 1. Đặt tên trong mã

| Đối tượng | Quy tắc | Ví dụ |
|---|---|---|
| Module, hàm, biến | `snake_case`, tiếng Việt không dấu | `nghich_dao_gauss_jordan`, `ma_tran`, `sai_so_tuong_doi` |
| Lớp | `CamelCase`, tiếng Việt không dấu | `NhatKyTinhToan`, `KetQuaTinhToan`, `DaThuc` |
| Hằng số | `UPPER_SNAKE` | `DUNG_SAI_MAC_DINH`, `BANG_DAO_HAM` |
| Ngoại lệ | Tiền tố `Loi` | `LoiKichThuoc`, `LoiMaTranSuyBien` |
| Tên toán học quốc tế giữ nguyên | `gradient`, `hessian`, `jacobian` | `gradient_so`, `hessian_so` |
| Thư mục chương trong `src/mlmath/` | `chuong_N_ten_ngan` | `chuong_1_ma_tran` |
| Thư mục chương trong `chapters/` | Theo đề | `ch1_linear_algebra` |
| Alias tiếng Anh | Chỉ trong `ch1.py … ch6.py` | `inverse_gj` |

**Tiền tố động từ có nghĩa cố định:**

| Tiền tố | Ý nghĩa | Trả về | Ví dụ |
|---|---|---|---|
| `la_` | Vị từ | `bool` | `la_doi_xung(A)` |
| `xac_thuc_` | Kiểm tra đầu vào; ném lỗi nếu sai | Dữ liệu đã chuẩn hóa | `xac_thuc_ma_tran(A)` |
| `kiem_tra_` | Chạy một phép kiểm chứng | `KetQuaKiemChung` | `kiem_tra_dao_ham(...)` |
| `tinh_`, tên danh từ | Tính toán | Giá trị | `dinh_thuc_laplace(A)` |
| `ve_` | Vẽ hình, lưu ra `outputs/` | `Path` | `ve_hinh_cau_don_vi(...)` |
| `doi_chieu_` | Chạy trong `doi_chieu/`, so với thư viện | Bảng so sánh | `doi_chieu_nghich_dao(...)` |

**Test:** file `test_<module>.py`; hàm `test_<hanh_vi>_<dieu_kien>`, ví dụ `test_nghich_dao_ma_tran_suy_bien_nem_loi`.

**Tham số thường gặp (giữ nhất quán giữa các chương):**

| Tên | Ý nghĩa |
|---|---|
| `ma_tran`, `A`, `B` | Ma trận 2 chiều |
| `vec_to`, `x`, `b` | Vector 1 chiều |
| `dung_sai` | Ngưỡng coi số bằng 0 hoặc hai số bằng nhau |
| `chon_pivot` | `True`: chọn phần tử trụ lớn nhất theo trị tuyệt đối |
| `nhat_ky` | `NhatKyTinhToan` hoặc `None` |
| `delta` | Bước sai phân số |
| `hat` | `numpy.random.Generator` (luôn truyền vào, không dùng seed toàn cục) |

**Văn bản:** tài liệu, chú thích, docstring, thông báo cho người dùng viết tiếng Việt **có dấu**. Công thức dùng Unicode (`Aᵀ`, `Aᴴ`, `A⁻¹`, `Σ`, `‖x‖₂`) hoặc khối mã; không dùng LaTeX trong docstring.

## 2. Quy ước toán học (bám slide bài giảng)

| Đại lượng | Quy ước | Nguồn |
|---|---|---|
| Vector `x ∈ ℝⁿ` | Vector **cột**; trong mã là mảng 1 chiều shape `(n,)` | Ch2 |
| Hệ vector | Truyền vào dạng **ma trận liên kết cột**: `V` shape `(n, k)`, cột `j` là vector thứ `j` | Ch2 §2.3.2 |
| Tọa độ | `[u]_B` là cột tọa độ; `(u)_B` là dòng. Trong mã dùng mảng `(n,)` | Ch2 §2.3.1 |
| Ma trận chuyển `P(B→S)` | Cột `j` = `[sⱼ]_B`; `[u]_B = P·[u]_S` | Ch2 (2.8) |
| Ma trận của ánh xạ tuyến tính | Cột `j` = `[f(uⱼ)]_S` | Ch2 (2.11) |
| Đồng dạng khi đổi cơ sở | `A′ = P⁻¹·A·P`, `P = P(B→B′)` | Ch2 Đ.lý 5 |
| Đạo hàm của `f: ℝⁿ→ℝ` | `∇f ∈ ℝⁿ` (cột); Hessian `ℝⁿˣⁿ` đối xứng | Ch3 (3.6), (3.7) |
| Đạo hàm theo ma trận | `∇_X f(X)` **cùng shape với X** | Ch3 (3.8) |
| Đạo hàm của `f: ℝᵐ→ℝⁿ` | `∇f ∈ ℝᵐˣⁿ`, phần tử `(i,j) = ∂fⱼ/∂xᵢ` (**chuyển vị Jacobian chuẩn**) | Ch3 (3.9) |
| Quy tắc chuỗi | `∇ₓg(f(x)) = ∇ₓf · ∇_f g` | Ch3 (3.13) |
| Quy tắc tích | `∇(fᵀg) = ∇f·g + ∇g·f` | Ch3 (3.11) |
| Phương sai mẫu `S²` | Chia cho **n**: `S² = (1/n)Σ(xᵢ−x̄)²` (tương ứng `np.var(ddof=0)`) | Ch6 §5.1.3b |
| Phương sai mẫu điều chỉnh `S′²` | Chia cho **n−1**: `S′² = n/(n−1)·S²` (tương ứng `ddof=1`) | Ch6 §5.2.1 |
| Hiệp phương sai mẫu | `S²(X) = (1/n)Σ(Xᵢ−X̄)(Xᵢ−X̄)ᵀ` (chia n) | Ch6 |
| Phân vị | Mức `1−α` (phân vị trên), không phải phân vị dưới | Ch6 |
| Chuẩn Frobenius | `‖A‖_F = √(Σ aᵢⱼ²)`; `‖X‖²_F = trace(XᵀX)` | Ch2 (2.5) |

**Hệ quả cho tên hàm:** vì thuật ngữ "phương sai mẫu" khác nhau giữa slide và phần mềm, tên hàm phải nói rõ: `phuong_sai_mau` (chia n) và `phuong_sai_mau_dieu_chinh` (chia n−1). Không có hàm tên chung chung `phuong_sai`.

## 3. Những chỗ slide cần đọc thận trọng

Các mục dưới đây đã được kiểm tra khi thiết kế. Agent phải xử lý đúng như cột "Làm gì" và ghi vào `analysis.md` của chương khi gặp.

| Chỗ trong slide | Vấn đề | Làm gì |
|---|---|---|
| Ch2 VD2, đáp án `[u]_B` | In `(6, −4, 1)`; tính lại cho `(6, −4, 5)` | Oracle tính trực tiếp (D16) |
| Ch2 T/c 3 (Sylvester) | Dùng cho cả bán xác định; không đủ | D12 |
| Ch2 T/c 5 (Cholesky) | Nói cho bán xác định dương, có "duy nhất" | D12 |
| Ch3 bảng đạo hàm, `∇det X` | Ghi `0` khi `det X = 0` | D10 |
| Ch6 KTC | `n ≥ 30` dùng phân vị chuẩn, khác `scipy.stats.t` | D08 |
| Ch2/Ch1 một số ký hiệu ma trận trong PDF | Trích xuất văn bản từ PDF bị lẫn ký hiệu | Đối chiếu bản gốc của giảng viên trước khi đưa vào test |

## 4. Quy ước về dữ liệu ví dụ

- Mọi ví dụ của đề mẫu và bài tập 12 câu đặt trong `chapters/chX/examples/` dưới dạng file `.json` (đầu vào) cùng `.md` (mô tả và đáp án kỳ vọng kèm **cách xác nhận đáp án**).
- Số ngẫu nhiên: luôn dùng `numpy.random.default_rng(seed)` với seed ghi rõ trong test; không dùng `np.random.seed`.
- Dung sai so sánh mặc định: `rtol=1e-9, atol=1e-10` cho thuật toán trực tiếp; `1e-6` cho sai phân số (theo đề); nới lỏng phải có lý do trong `spec.md`.
