# Quyết định kiến trúc

Tài liệu này là nguồn duy nhất cho các quyết định thiết kế. AI Agent **không tự thay đổi** bất kỳ mục nào; nếu thấy một quyết định sai hoặc không thực hiện được, hãy dừng lại và báo (xem `CONG_VIEC_TIEP_THEO.md`).

**Trạng thái:**
- **Chốt**: người dùng đã xác nhận.
- **Mặc định**: do giai đoạn thiết kế đề xuất, áp dụng cho đến khi người dùng đổi.

Nguồn yêu cầu ưu tiên cao nhất là đề bài của giảng viên. Bộ slide bài giảng (Chương 1–6) và file bài tập 12 câu là nguồn tham chiếu về ký hiệu, thuật toán và dữ liệu mẫu.

---

## D01. Mã nguồn thật nằm ở `src/mlmath/` — Chốt
Đề yêu cầu mỗi chương có `src/`. Để tránh trùng lặp, cài đặt dùng chung nằm ở `src/mlmath/`. Mỗi `chapters/chX_*/src/` chỉ chứa:
- `chay_chuong.py`: điểm vào mỏng, chạy menu hoặc các ví dụ của chương đó bằng cách gọi tầng dịch vụ.
- `README.md`: bảng ánh xạ "yêu cầu của đề → module trong `src/mlmath/`".

Cấm đặt logic thuật toán trong `chapters/`.

## D02. Tên tiếng Việt là bản gốc; alias tiếng Anh chỉ re-export — Chốt
Hàm, module, biến dùng tên tiếng Việt không dấu (xem `docs/QUY_UOC_DAT_TEN.md`). Test mẫu trong đề import `from mlmath.ch1 import inverse_gj`, nên có thêm các module `src/mlmath/ch1.py … ch6.py` chỉ gồm `from .chuong_N_... import ... as <ten_anh>`. Alias không chứa logic và không được test riêng ngoài một test "alias trỏ đúng hàm gốc".

Alias tối thiểu cho Chương 1: `inverse_gj`, `inverse_adj`, `det_laplace`, `det_gauss`, `rank`, `matmul`, `transpose`, `conj_transpose`, `matpow`.

## D03. Ranh giới thư viện — Chốt
- **Chương 1**: không dùng `@`, `np.dot`, `np.matmul`, `np.linalg.*` trong mã tự cài.
- **Từ Chương 2**: được dùng `@` cho phép nhân ma trận thông thường. Vẫn **cấm** trong mã tự cài: `np.linalg.inv, solve, det, eig, eigh, cholesky, qr, lstsq, matrix_rank, norm, null_space` và tương đương.
- Các hàm trên chỉ xuất hiện trong `tests/`, `chapters/*/tests/`, `chapters/*/doi_chieu/`.
- Có một test tĩnh `tests/unit/test_cam_thu_vien.py` quét AST của `src/mlmath/` và thất bại nếu gặp import hoặc lời gọi bị cấm. Đây là cơ chế bắt buộc, không phải khuyến nghị.
- Được phép trong mã tự cài: `numpy` (mảng, `zeros`, `eye`, `empty`, vòng lặp, `sqrt`, `exp`, `log`, `random.Generator`), `math`, `fractions`, `itertools`, `time`, `matplotlib`.

## D04. Trị riêng làm theo slide bài giảng — Chốt (theo yêu cầu "xem slide")
Slide Chương 2 (mục 2.5.3): B1 giải `det(A − λI) = 0`; B2 giải `(A − λI)x = 0` để có không gian riêng; chéo hóa trực giao bằng Gram–Schmidt trên từng không gian riêng. Cài đặt đúng thứ tự này:
1. Đa thức đặc trưng = `dinh_thuc_laplace` (Chương 1) áp dụng cho ma trận có phần tử là `DaThuc` (đa thức một biến `λ`, hệ số `Fraction` hoặc `float`).
2. Nghiệm: thử nghiệm hữu tỉ trước (khi hệ số hữu tỉ), phần còn lại bằng Durand–Kerner. Nghiệm phức được báo rõ; vector riêng chỉ tìm trong ℝ cho trị riêng thực.
3. Không gian riêng = nhân của `A − λI`, tính bằng Gauss–Jordan của Chương 1.
4. Mặc định `da_thuc_dac_trung` chỉ nhận `n ≤ 6` (Laplace O(n!)). Với `n > 6` ném `LoiDieuKien` kèm gợi ý dùng Jacobi.
5. **Nâng cao, không bắt buộc**: `jacobi_doi_xung(A)` cho ma trận đối xứng cỡ lớn (dùng cho PCA). Chỉ làm sau khi mọi mục bắt buộc của Chương 2 đã đạt.

## D05. Kiểu dữ liệu — Chốt
Hỗ trợ `float64`, `complex128`, và `fractions.Fraction` (mảng `dtype=object`).
- Chương 1: hỗ trợ cả ba. Số thực không bao giờ tự đổi sang phân số.
- Gram–Schmidt trực chuẩn hóa cần căn bậc hai nên chỉ chạy trên `float64`. Bản trực giao (không chuẩn hóa) chạy được trên `Fraction`.
- Cholesky `A = L·Lᴴ` hỗ trợ `float64` và `complex128`.

## D06. Tối ưu: `linprog` là mặc định — Chốt
- LP giải bằng `scipy.optimize.linprog` (đề cho phép thay CVXOPT). CVXOPT là phụ thuộc tùy chọn trong `requirements-optional.txt`.
- QP "điểm gần nhất trên đa diện lồi": luôn có bản gradient chiếu tự cài để chạy được khi không có CVXOPT; CVXOPT dùng để đối chiếu nếu cài được. Frank–Wolfe là mục nâng cao.
- Bài có biến nguyên (số thanh cắt, số cuốn sách): giải LP, kiểm tra nghiệm có nguyên không; nếu cần ép nguyên thì dùng `scipy.optimize.milp` và ghi rõ trong `analysis.md`.
- Giải LP bằng thư viện là việc đề cho phép; kiểm chứng bằng: nghiệm thỏa mọi ràng buộc, đối chiếu nghiệm tính tay, và đối chiếu một solver thứ hai nếu có.

## D07. Phân vị lấy từ `scipy.stats` như "bảng tra phụ lục" — Mặc định
Slide Chương 6 dùng phân vị chuẩn, Student, χ² "tra bảng". Đề không yêu cầu tự cài hàm nghịch đảo phân phối. Gói trong một module `tien_ich/phan_vi.py` (`phan_vi_chuan`, `phan_vi_student`, `phan_vi_khi_binh_phuong`) để dễ thay bằng bản tự cài. Hàm mật độ và phân phối tích lũy của Chương 4 (chuẩn, Poisson, nhị thức, đều, mũ) **vẫn tự cài** (dùng `math.erf`, `math.lgamma`).

## D08. Quy tắc khoảng tin cậy theo bài giảng, có tùy chọn Student — Mặc định
Slide: σ² đã biết → phân vị chuẩn; σ² chưa biết và n < 30 → Student(n−1); σ² chưa biết và n ≥ 30 → phân vị chuẩn. `scipy.stats.t.interval` luôn dùng Student nên **sẽ khác** khi n ≥ 30. Hàm KTC có tham số `quy_tac="bai_giang" | "student"`, mặc định `"bai_giang"`. Test đối chiếu `scipy` phải chọn đúng quy tắc tương ứng và ghi rõ trong `analysis.md`.

## D09. Quy ước đạo hàm theo bài giảng — Mặc định
- `∇f(x) ∈ ℝⁿ` là vector cột; Hessian `∇²f(x) ∈ ℝⁿˣⁿ`; `∇_X f(X)` có **cùng kích thước với X**.
- Với `f: ℝᵐ → ℝⁿ`, slide định nghĩa `∇f(x) ∈ ℝᵐˣⁿ` với phần tử `(i, j) = ∂fⱼ/∂xᵢ` (hàng là biến vào). Đây là **chuyển vị của Jacobian thông thường**.
- `jacobian_so(..., bo_tri="bai_giang")` trả theo slide; `bo_tri="chuan"` trả Jacobian chuẩn (`n×m`).
- Quy tắc tích: `∇(fᵀg) = ∇f·g + ∇g·f`. Quy tắc chuỗi: `∇ₓg(f(x)) = ∇ₓf · ∇_f g`. Thứ tự nhân là bắt buộc.

## D10. Gradient của định thức dùng ma trận phần phụ đại số — Mặc định
`∇det(X)` = ma trận phần phụ đại số (cofactor), đúng cho mọi `X`. Slide ghi `det X · X⁻ᵀ` khi khả nghịch (đúng) và `0` khi `det X = 0` (**không đúng** khi `rank X = n − 1`; ví dụ `X = diag(1, 0)` có gradient `diag(0, 1) ≠ 0`). Test phải có một ca `rank = n − 1` đối chiếu bằng sai phân.

## D11. Quy ước ma trận chuyển cơ sở — Chốt (bám slide)
`P(B→S)` có cột `j` là tọa độ của `sⱼ` trong cơ sở `B`, và `[u]_B = P·[u]_S`. Thuật toán: `(B* | S*) → (I | P)` với `B*`, `S*` là ma trận có **các cột** là vector cơ sở. Hàm `ma_tran_chuyen_co_so(B, S)` trả `P(B→S)` theo đúng nghĩa này và docstring phải nêu rõ hướng. Đề có câu phản biện "AI có nhầm P(B→S) với P(S→B) không?" nên cần test riêng cho hướng.

## D12. Tiêu chuẩn Sylvester chỉ kết luận xác định, Cholesky yêu cầu xác định dương — Mặc định
- Slide T/c 3 phát biểu Sylvester cho cả bán xác định (định thức con góc trái ≥ 0). Điều này **không đủ**: `[[0,0],[0,-1]]` có các định thức góc trái bằng 0 nhưng không bán xác định dương. Bán xác định dương cần mọi định thức con chính ≥ 0 (hoặc mọi trị riêng ≥ 0).
- `tieu_chuan_sylvester` trả `xac_dinh_duong | xac_dinh_am | chua_ket_luan`. `la_ban_xac_dinh_duong` dùng mọi định thức con chính (n ≤ 10) hoặc trị riêng.
- Slide T/c 5 nói Cholesky cho ma trận bán xác định dương; với ma trận suy biến, phân rã không duy nhất hoặc không có đường chéo dương. `phan_ra_cholesky` yêu cầu xác định dương và ném `LoiDieuKien` khi gặp pivot ≤ 0.

## D13. Ba loại nhật ký tách biệt — Chốt
| Loại | Nơi lưu | Tạo bởi |
|---|---|---|
| Nhật ký tính toán lúc chạy | `NhatKyTinhToan` → `outputs/` của chương | Chương trình |
| Nhật ký phát triển | `chapters/chX/NHAT_KY.md` | Nhóm / Agent |
| Nhật ký prompt và phản hồi AI | `PROMPT_LOG.md` (đầy đủ), `chapters/chX/prompts.md` (trích tiêu biểu) | Nhóm |

## D14. Ba lớp, phụ thuộc một chiều — Chốt
`giao_dien` → `dich_vu` → `chuong_N` → `tien_ich`. Thuật toán thuần túy: không `print`, không ghi file, không đọc `argv`. Thuật toán nhận tham số tùy chọn `nhat_ky: NhatKyTinhToan | None = None`; khi `None` dùng nhật ký rỗng. Hàm trả giá trị thuần (ví dụ `nghich_dao_gauss_jordan(A)` trả ma trận) để `A @ inverse_gj(A)` trong test của đề chạy được.

## D15. Ngoại lệ — Mặc định
Mọi lỗi dữ liệu kế thừa `ValueError` (test mẫu của đề dùng `pytest.raises(ValueError)`): `LoiDuLieu`, `LoiKichThuoc`, `LoiMaTranSuyBien`, `LoiDieuKien`. Lỗi không hội tụ của thuật toán lặp dùng `LoiHoiTu(RuntimeError)`. Không dùng `except:` hoặc `except Exception:` để che lỗi.

## D16. Bộ đáp án oracle phải độc lập với đáp án in trong slide — Chốt
Slide có lỗi in. Ví dụ ở Chương 2 (VD2 đổi cơ sở): `u = 2s₁ − 3s₂ + 5s₃ = (2, 1, 11)` và đáp án đúng là `[u]_B = (6, −4, 5)`, slide in `(6, −4, 1)`. Quy tắc: đáp án kỳ vọng trong test lấy từ (a) tính trực tiếp bằng định nghĩa, (b) thư viện, (c) tính chất toán học; đáp án in trong slide chỉ dùng làm tham khảo và nếu khác thì ghi vào `analysis.md`.

## D17. Nội dung sinh viên phải tự viết — Chốt
Chỉ tạo **khung và hướng dẫn điền** cho: `chapters/ch4_probability/selfstudy.md`, `reports/reflection.md`, mọi mục trong `PROMPT_LOG.md`, `prompts.md`, `NHAT_KY.md`, `analysis.md`, `flow/pilot/README.md`. Không điền số liệu, kết quả chạy, lần AI sai hay nhận xét chưa từng xảy ra.

## D18. Bài tập mẫu của giảng viên là bộ ca nghiệm thu — Mặc định
File bài tập 12 câu và các đề mẫu trong slide được ánh xạ vào từng chương (xem `CHIEN_LUOC_KIEM_THU.md`). Đó là **điểm xuất phát**; mỗi chương vẫn phải có ít nhất 2 bài tự đặt (1 cơ bản, 1 ứng dụng ML) với dữ liệu cụ thể.
