# Hợp đồng module

Đây là chữ ký hàm và điều kiện mà các module phải tuân theo. Đây là **hợp đồng thiết kế**, chưa phải mã đã cài. Agent có thể thêm hàm trợ giúp nội bộ (tên bắt đầu bằng `_`), nhưng **không đổi tên, đổi tham số hay đổi kiểu trả về** của hàm trong tài liệu này mà không báo.

Quy ước kiểu: `Ma_tran = np.ndarray` (2 chiều), `Vec_to = np.ndarray` (1 chiều), `So = float | complex | Fraction`. Quy ước bố trí dữ liệu xem `docs/QUY_UOC_DAT_TEN.md`. Mọi hàm thuật toán có thêm tham số cuối `nhat_ky: NhatKyTinhToan | None = None` (không ghi trong bảng cho gọn).

---

## 0. Phần chung

### 0.1 `mlmath.loi`
`LoiDuLieu(ValueError)`; `LoiKichThuoc(LoiDuLieu)`; `LoiMaTranSuyBien(LoiDuLieu)`; `LoiDieuKien(LoiDuLieu)`; `LoiHoiTu(RuntimeError)`.

### 0.2 `tien_ich.nhat_ky_tinh_toan`
| Thành phần | Mô tả |
|---|---|
| `BuocTinhToan` (dataclass, bất biến) | `ten_thuat_toan: str`, `ten_buoc: str`, `cong_thuc: str`, `trang_thai: Any`, `ket_qua: Any`, `kiem_chung: str = ""` |
| `NhatKyTinhToan` | `ghi_buoc(ten_buoc, cong_thuc, trang_thai=None, ket_qua=None, kiem_chung="")`; thuộc tính `cac_buoc: list[BuocTinhToan]`; `NhatKyTinhToan.rong()` trả nhật ký không ghi gì (đối tượng "null") để thuật toán không cần `if nhat_ky:` |
| Quy tắc | `trang_thai`, `ket_qua` được **sao chép** (`copy`) khi ghi, tránh bị sửa về sau |

### 0.3 `tien_ich.xuat_ket_qua`
| Thành phần | Mô tả |
|---|---|
| `KetQuaKiemChung` | `ten: str`, `dat: bool`, `sai_so: float | None`, `mo_ta: str` |
| `KetQuaTinhToan` (dataclass) | `ten_thuat_toan: str`, `dau_vao: dict`, `ket_qua: Any`, `cac_buoc: list[BuocTinhToan]`, `kiem_chung: list[KetQuaKiemChung]`, `thoi_gian_giay: float`, `ghi_chu: str = ""` |
| `hien_thi_terminal(kq, chi_tiet=True) -> None` | In bước và kết quả; ma trận căn cột |
| `ghi_txt(kq, thu_muc) -> Path` | Cùng nội dung với Terminal |
| `ghi_json(kq, thu_muc) -> Path` | Quy tắc tuần tự hóa: `ndarray → list`; `Fraction → "p/q"` (chuỗi); `complex → {"re":…, "im":…}`; `DaThuc → {"he_so":[…]}` |
| Ràng buộc | Chỉ định dạng và ghi, không tính lại. Cả Terminal, TXT và JSON sinh từ **cùng** một `KetQuaTinhToan` |

### 0.4 `tien_ich.dinh_dang_ma_tran`
| Hàm | Mô tả |
|---|---|
| `dinh_dang_so(x, che_do="tu_dong", so_chu_so=6) -> str` | `che_do`: `"tu_dong"` (Fraction → `p/q`, số thực → thập phân), `"phan_so"` (chỉ khi đầu vào là `Fraction` hoặc nguyên), `"thap_phan"` |
| `dinh_dang_ma_tran(A, che_do="tu_dong", so_chu_so=6) -> str` | Căn chỉnh theo cột; ma trận phức hiển thị `a+bi` |
| Ràng buộc | **Không bao giờ** tự đổi số thực sang phân số; đổi chỉ khi người dùng chọn `"phan_so"` và đầu vào đã là hữu tỉ |

### 0.5 `tien_ich.kiem_tra_du_lieu`
| Hàm | Mô tả |
|---|---|
| `xac_thuc_ma_tran(A, ten="A") -> Ma_tran` | Chấp nhận danh sách lồng nhau; trả `ndarray` 2 chiều; dtype ∈ {float64, complex128, object-Fraction}; từ chối `nan`, `inf`, rỗng. Không sửa mảng đầu vào |
| `xac_thuc_vec_to(x, ten="x") -> Vec_to` | Tương tự cho 1 chiều |
| `xac_thuc_vuong(A) -> Ma_tran` | Thêm điều kiện vuông; `LoiKichThuoc` |
| `xac_thuc_nhan_duoc(A, B) -> None` | Cột `A` = hàng `B`; `LoiKichThuoc` |

### 0.6 `tien_ich.sai_so`
`sai_so_tuyet_doi(a, b)`, `sai_so_tuong_doi(a, b, eps=1e-300)`, `gan_bang(a, b, rtol=1e-9, atol=1e-10) -> bool`. Dùng chuẩn viết trong chính `tien_ich` (không dùng `np.linalg.norm`).

### 0.7 `tien_ich.da_thuc`
| Thành phần | Mô tả |
|---|---|
| `DaThuc(he_so: Sequence[So])` | Hệ số **từ bậc thấp đến cao**; hỗ trợ `+ − * **` (số mũ nguyên ≥ 0), `==`, `bac`, `__call__(x)`, `__neg__`, nhân với số vô hướng ở cả hai phía; in dạng `λ^2 - 3λ + 2` |
| `tim_nghiem(P: DaThuc, dung_sai=1e-10) -> list[tuple[So, int]]` | Trả `(nghiệm, bội đại số)`. Bước 1: thử nghiệm hữu tỉ khi hệ số hữu tỉ; bước 2: Durand–Kerner cho phần còn lại; gộp nghiệm trùng theo `dung_sai`. Không dùng `np.roots` trong mã tự cài |
| Mục đích | (a) `dinh_thuc_laplace` chạy được trên ma trận có phần tử là `DaThuc`; (b) đa thức đặc trưng `det(A − λI)`; (c) tìm tham số `m` làm ma trận suy biến |

### 0.8 `tien_ich.phan_vi`
`phan_vi_chuan(p)`, `phan_vi_student(p, bac_tu_do)`, `phan_vi_khi_binh_phuong(p, bac_tu_do)`. `p` là mức xác suất tích lũy dưới. Bọc `scipy.stats` (D07).

### 0.9 `dich_vu`
| Thành phần | Mô tả |
|---|---|
| `MucThuatToan` (dataclass) | `ma: str` (ví dụ `"ch1.nghich_dao_gauss_jordan"`), `chuong: int`, `ten_hien_thi: str`, `ham: Callable`, `tham_so: list[ThamSo]`, `kiem_chung: Callable | None` |
| `ThamSo` | `ten`, `kieu` (`"ma_tran"`, `"vec_to"`, `"so"`, `"chuoi"`, `"lua_chon"`), `mo_ta`, `mac_dinh` |
| `DANG_KY: dict[str, MucThuatToan]` | Nguồn duy nhất cho menu và CLI |
| `liet_ke(chuong: int | None = None) -> list[MucThuatToan]` | |
| `chay(ma: str, **tham_so) -> KetQuaTinhToan` | Tạo nhật ký, gọi `ham`, đo thời gian, chạy `kiem_chung`; **không** in, **không** ghi file |

---

## 1. Chương 1 — `chuong_1_ma_tran`

| Module | Hàm | Đầu vào → Đầu ra | Điều kiện / lỗi |
|---|---|---|---|
| `phep_toan` | `chuyen_vi(A)` | `m×n → n×m` | |
| | `chuyen_vi_lien_hop(A)` | `Aᴴ` (chuyển vị rồi liên hợp) | |
| | `cong_ma_tran(A, B)`, `tru_ma_tran(A, B)` | cùng cấp | `LoiKichThuoc` |
| | `nhan_so(k, A)` | `k·A` | |
| | `nhan_ma_tran(A, B)` | `cᵢⱼ = Σ aᵢₖ·bₖⱼ` bằng vòng lặp tường minh | Cấm `@`, `np.dot`; `LoiKichThuoc`. Độ phức tạp O(mnp) |
| | `luy_thua(A, k)` | `Aᵏ`, bình phương liên tiếp | `A` vuông, `k` nguyên ≥ 0 (`A⁰ = I`); `k < 0` → `LoiDieuKien` |
| `dang_ma_tran` | `la_bac_thang`, `la_vuong`, `la_tam_giac_tren`, `la_tam_giac_duoi`, `la_cheo`, `la_don_vi`, `la_doi_xung`, `la_hermitian` | `(A, dung_sai=0 hoặc mặc định) → bool` | `dung_sai` mặc định `0` cho `Fraction`, `1e-12` cho số thực |
| | `nhan_dang_dang_ma_tran(A)` | `dict[str, bool]` | Dùng cho menu và báo cáo |
| `dinh_thuc` | `dinh_thuc_laplace(A, hang=0)` | `det A` khai triển theo hàng `hang`, đệ quy | Vuông; phần tử có thể là `float`, `complex`, `Fraction`, `DaThuc`. Độ phức tạp O(n!) |
| | `dinh_thuc_gauss(A, chon_pivot=True)` | `det A` bằng đưa về tam giác, **theo dõi dấu khi đổi hàng** | Vuông. O(n³). Ghi nhật ký từng phép biến đổi |
| | `do_thoi_gian_dinh_thuc(cac_n, so_lan=3, n_toi_da_laplace=9, hat=None) -> list[dict]` | Mỗi dict: `n`, `t_laplace`, `t_gauss`, `khop: bool` | Bỏ Laplace khi `n > n_toi_da_laplace` |
| `hang` | `dua_ve_bac_thang(A, chon_pivot=True, dung_sai=None)` | `(A_bac_thang, so_lan_doi_hang)` | `dung_sai=None`: `max(m,n)·eps·max|A|` cho số thực, `0` cho `Fraction` |
| | `hang_ma_tran(A, dung_sai=None) -> int` | Số hàng khác 0 của dạng bậc thang | |
| `nghich_dao` | `nghich_dao_gauss_jordan(A, chon_pivot=True, dung_sai=None)` | `A⁻¹` bằng `(A\|I) → (I\|A⁻¹)`, hai pha như slide | `LoiMaTranSuyBien` khi không tìm được pivot khác 0; xử lý pivot bằng 0 bằng đổi hàng |
| | `phan_phu_dai_so(A, i, j)` | `Cᵢⱼ = (−1)^{i+j}·det(Aᵢⱼ)` | |
| | `ma_tran_phu_hop(A)` | `adj(A) = (Cᵢⱼ)ᵀ` | |
| | `nghich_dao_phu_hop(A, dung_sai=None)` | `adj(A) / det(A)` | `LoiMaTranSuyBien` khi `det = 0` (hoặc `|det| ≤ dung_sai`) |
| | `khao_sat_kha_nghich(A) -> dict` | `det`, `hang`, `kha_nghich: bool` bằng nhiều đường, để đối chiếu nhau | |
| | `so_dieu_kien(A) -> float` | `κ₁(A) = ‖A‖₁·‖A⁻¹‖₁` (chuẩn 1 tự cài) | `LoiMaTranSuyBien` nếu suy biến |
| `giai_he` | `giai_he_gauss_jordan(A, b) -> KetQuaHe` | `KetQuaHe(loai: "duy_nhat" \| "vo_nghiem" \| "vo_so_nghiem", nghiem_rieng, co_so_khong_gian_nghiem, hang_A, hang_Ab)` | Phân loại đúng bằng so sánh `rank(A)` và `rank(A\|b)`. Dùng cho phương trình chuẩn `(XᵀX)w = Xᵀy` |
| `tham_so` | `tim_tham_so_suy_bien(ma_tran_theo_m: Callable[[DaThuc], Ma_tran]) -> list[tuple[So, int]]` | Nghiệm của `det A(m) = 0` | Gọi `dinh_thuc_laplace` trên phần tử `DaThuc`, rồi `tim_nghiem`. Cho bài "tìm m để A khả nghịch" |

**Alias (`ch1.py`):** xem D02.

## 2. Chương 2 — `chuong_2_khong_gian_vector`

| Module | Hàm | Mô tả | Điều kiện / lỗi |
|---|---|---|---|
| `chuan` | `chuan_euclid(x)`, `chuan_vo_cung(x)`, `chuan_p(x, p)` | `‖x‖₂`, `‖x‖∞`, `‖x‖ₚ` | `p ≥ 1`, `LoiDieuKien` nếu `p < 1` |
| | `chuan_frobenius(A)` | `√(Σ aᵢⱼ²)` | |
| | `khoang_cach_frobenius(A, B)` | `‖A − B‖_F` | `LoiKichThuoc` |
| | `gan_nhat_theo_frobenius(A, ung_vien) -> tuple[int, list[float]]` | Chỉ số ứng viên gần `A` nhất và các khoảng cách | |
| | `ve_hinh_cau_don_vi(cac_chuan, duong_dan) -> Path` | Vẽ hình cầu đơn vị trong ℝ² cho nhiều chuẩn | Dùng matplotlib backend không giao diện |
| `doc_lap_tuyen_tinh` | `hang_he_vec_to(V)` | Hạng của hệ (cột của `V`) | Dùng `hang_ma_tran` của Ch1 |
| | `la_doc_lap_tuyen_tinh(V) -> bool` | `hang == số cột` | |
| | `trich_co_so(V) -> list[int]` | Chỉ số các cột tạo thành một cơ sở của không gian sinh | Chọn theo vị trí pivot |
| | `so_chieu(V) -> int` | `dim span` | |
| `doi_co_so` | `ma_tran_chuyen_co_so(B, S) -> Ma_tran` | `P(B→S)` theo D11, bằng `(B\|S) → (I\|P)` | `B` khả nghịch; `LoiKichThuoc`, `LoiMaTranSuyBien` |
| | `toa_do_trong_co_so(u, B) -> Vec_to` | `[u]_B` với `u` ở cơ sở chính tắc | |
| | `doi_toa_do(u_S, P) -> Vec_to` | `[u]_B = P·[u]_S` | |
| `gram_schmidt` | `gram_schmidt(V, chuan_hoa=True, dung_sai=1e-12) -> Ma_tran` | Cột của kết quả là hệ trực (chuẩn) giao | `LoiDieuKien` nếu hệ phụ thuộc tuyến tính. `chuan_hoa=True` chỉ cho `float64` |
| | `do_mat_truc_giao(Q) -> float` | `‖QᵀQ − I‖_F` | |
| | `kiem_tra_khong_gian_sinh_khong_doi(V, Q) -> KetQuaKiemChung` | Kiểm tra `span(V) = span(Q)` bằng hạng | |
| | `gram_schmidt_cai_tien(V)` (nâng cao) | Bản Gram–Schmidt cải tiến để so sánh mất trực giao | Nâng cao |
| `anh_xa_tuyen_tinh` | `kiem_tra_tuyen_tinh(f, n, so_mau=20, hat=...) -> KetQuaKiemChung` | Kiểm tra cộng tính và thuần nhất trên mẫu ngẫu nhiên | **Chỉ là bằng chứng số**, không phải chứng minh; ghi rõ trong kết quả |
| | `ma_tran_anh_xa(f, n_vao, co_so_vao=None, co_so_ra=None) -> Ma_tran` | Cột `j` = `[f(uⱼ)]_S` | Mặc định cơ sở chính tắc |
| | `co_so_khong_gian_anh(A) -> Ma_tran`, `co_so_khong_gian_nhan(A) -> Ma_tran` | Cột là các vector cơ sở | Bằng Gauss–Jordan; nhân là nghiệm cơ sở của `Ax = 0` |
| | `kiem_tra_dinh_ly_so_chieu(A) -> KetQuaKiemChung` | `dim Im + dim Ker = n` | |
| | `doi_co_so_bien_doi(A, P) -> Ma_tran` | `A′ = P⁻¹·A·P` | |
| `tri_rieng` | `da_thuc_dac_trung(A) -> DaThuc` | `det(A − λI)` qua Laplace trên `DaThuc` | `n ≤ 6` (D04) |
| | `tri_rieng(A) -> list[tuple[So, int]]` | Trị riêng (thực hoặc phức) và bội đại số | |
| | `khong_gian_rieng(A, lam) -> Ma_tran` | Cơ sở của `N_λ = ker(A − λI)` (cột) | `lam` thực; trị riêng phức → `LoiDieuKien` kèm giải thích |
| | `phan_tich_rieng(A) -> KetQuaRieng` | `[(lam, boi_dai_so, boi_hinh_hoc, co_so)]`, `cheo_hoa_duoc: bool` | Không giả định chéo hóa được. Báo rõ khi `bội hình học < bội đại số` |
| | `cheo_hoa(A) -> tuple[Ma_tran, Ma_tran]` | `(P, D)` với `P⁻¹AP = D` | `LoiDieuKien` nếu không chéo hóa được trên ℝ |
| | `cheo_hoa_truc_giao(A) -> tuple[Ma_tran, Ma_tran]` | `P` trực giao: Gram–Schmidt trên từng không gian riêng | `A` đối xứng, nếu không `LoiDieuKien` |
| | `luy_thua_qua_cheo_hoa(A, k)` | `P·Dᵏ·P⁻¹` | Dùng `cheo_hoa` |
| | `jacobi_doi_xung(A, so_vong_toi_da, dung_sai)` (nâng cao) | Trị riêng và vector riêng của ma trận đối xứng | Chỉ làm sau mục bắt buộc |
| `xac_dinh_duong` | `tieu_chuan_sylvester(A) -> KetQuaSylvester` | `loai ∈ {"xac_dinh_duong","xac_dinh_am","chua_ket_luan"}` kèm các định thức con góc trái | Đối xứng; D12 |
| | `la_xac_dinh_duong(A)`, `la_ban_xac_dinh_duong(A)` | Bán xác định dương dùng mọi định thức con chính (n ≤ 10) | |
| | `phan_ra_cholesky(A) -> Ma_tran` | `L` tam giác dưới, `A = L·Lᴴ`, đường chéo dương | Đối xứng (hoặc Hermitian) xác định dương; `LoiDieuKien` khi pivot ≤ 0 |
| | `giai_he_cholesky(A, b)` (tùy chọn) | Giải bằng thế xuôi và thế ngược | |
| `vet` | `vet_ma_tran(A)` | `trace A` | Vuông |
| `ung_dung_pca` | `pca(X, k) -> KetQuaPCA` | Trung tâm hóa, ma trận hiệp phương sai (đối xứng, bán xác định dương), chéo hóa trực giao, chiếu lên `k` thành phần | Ứng dụng ML của Ch2. Với số đặc trưng lớn hơn giới hạn của `da_thuc_dac_trung`, dùng `jacobi_doi_xung` |

## 3. Chương 3 — `chuong_3_giai_tich_ma_tran`

| Module | Hàm | Mô tả | Điều kiện / lỗi |
|---|---|---|---|
| `dao_ham_so` | `gradient_so(f, x, delta=1e-5, kieu="trung_tam") -> np.ndarray` | `x` có **shape bất kỳ**; kết quả cùng shape. `kieu ∈ {"tien","trung_tam"}`: `[f(x+δeᵢ)−f(x)]/δ` hoặc `[f(x+δeᵢ)−f(x−δeᵢ)]/(2δ)` | Không sửa `x`; `f` trả số thực (kể cả `int` thì ép `float`) |
| | `jacobian_so(f, x, delta=1e-5, kieu="trung_tam", bo_tri="bai_giang")` | `f: ℝᵐ→ℝⁿ`; `"bai_giang"` → shape `(m, n)` phần tử `(i,j)=∂fⱼ/∂xᵢ`; `"chuan"` → `(n, m)` | D09 |
| | `hessian_so(f, x, delta=1e-4)` | Đối xứng hóa kết quả; `delta` mặc định lớn hơn vì sai phân bậc hai nhạy với làm tròn | |
| `bang_dao_ham` | `BANG_DAO_HAM: dict[str, MucDaoHam]` | **Ít nhất 8** hàm (khuyến nghị đủ 12 mục slide) | |
| | `MucDaoHam` | `ten`, `cong_thuc: str`, `f`, `gradient_giai_tich`, `tao_dau_vao(hat, kich_thuoc)` | |
| | `kiem_tra_dao_ham(muc, hat, so_mau=20, delta=1e-5) -> KetQuaKiemChung` | Sai số tương đối giữa giải tích và số < `1e-6` (sai phân trung tâm) | |

**Các mục tối thiểu của `BANG_DAO_HAM`** (theo slide Ch3 §3.6):

| Hàm | Gradient giải tích (theo D09) |
|---|---|
| `aᵀx` | `a` |
| `Ax` (vector) | `Aᵀ` trong bố trí bài giảng |
| `xᵀAx` | `(A + Aᵀ)x` |
| `‖x‖²` | `2x` |
| `‖Ax − b‖²` | `2Aᵀ(Ax − b)` |
| `aᵀx·xᵀb` | `(a·bᵀ + b·aᵀ)x` |
| `trace(AX)` | `Aᵀ` |
| `trace(XᵀAX)` | `(A + Aᵀ)X` |
| `trace(XᵀX)`, `‖X‖²_F` | `2X` |
| `trace(AᵀXB)` | `A·Bᵀ` |
| `aᵀXb` | `a·bᵀ` |
| `‖AX − B‖²_F` | `2Aᵀ(AX − B)` |
| `det X` | ma trận phần phụ đại số (D10) |

| Module | Hàm | Mô tả |
|---|---|---|
| `quy_tac` | `quy_tac_tich(jac_f, jac_g, f_x, g_x) -> np.ndarray` | `jac_f·g + jac_g·f` (D09) |
| | `quy_tac_chuoi(jac_x_f, jac_f_g) -> np.ndarray` | `jac_x_f @ jac_f_g`; thứ tự cố định |
| `taylor` | `taylor_bac_1(f, gradient, a) -> Callable`, `taylor_bac_2(f, gradient, hessian, a) -> Callable` | Hàm 2 biến trở lên; trả hàm xấp xỉ |
| | `sai_so_taylor(f, xap_xi, a, huong, cac_h) -> dict` | Sai số theo `h`; ước lượng bậc hội tụ bằng hệ số góc log–log |
| `khao_sat_sai_so` | `khao_sat_theo_delta(f, gradient_giai_tich, x, cac_delta) -> dict` | Sai số của sai phân tiến và trung tâm theo `δ` (để thấy bậc `o(δ)` và `o(δ²)` và sai số làm tròn khi `δ` quá nhỏ) |
| | `ve_sai_so_theo_delta(ket_qua, duong_dan) -> Path` | Đồ thị log–log |
| `cuc_tri` | `phan_loai_diem_dung(H) -> str` | Dùng Sylvester của Ch2: `"cuc_tieu"`, `"cuc_dai"`, `"yen_ngua"`, `"chua_ket_luan"` |

## 4. Chương 4 — `chuong_4_xac_suat`

| Module | Hàm | Mô tả | Điều kiện / lỗi |
|---|---|---|---|
| `dem` | `hoan_vi(n)`, `chinh_hop(n, k)`, `to_hop(n, k)` | Số nguyên chính xác (số nguyên Python); `log_to_hop(n, k)` dùng `math.lgamma` cho `n` lớn | `0 ≤ k ≤ n`; `LoiDieuKien` |
| `xac_suat` | `xac_suat_day_du(p_he, p_co_dieu_kien)` | `Σ P(Aⱼ)P(A\|Aⱼ)` | `p_he` tổng bằng 1, hệ đầy đủ |
| | `bayes(p_he, p_co_dieu_kien) -> np.ndarray` | `P(Aₖ\|A)` cho mọi `k` | `P(A) > 0` |
| | `bernoulli(n, p, k)`, `so_thanh_cong_kha_nang_nhat(n, p)` | Công thức Bernoulli và `k*` (xử lý trường hợp `(n+1)p` nguyên) | |
| `phan_phoi` | `nhi_thuc_pmf/cdf`, `sieu_boi_pmf`, `poisson_pmf/cdf`, `chuan_pdf/cdf`, `deu_pdf/cdf`, `mu_pdf/cdf` | Tự cài; `chuan_cdf` bằng `math.erf` | Kiểm tra tham số |
| | `sinh_mau_deu(a, b, n, hat)`, `sinh_mau_mu(lam, n, hat)` | **Phương pháp biến đổi ngược** từ `U(0,1)` | |
| | `sinh_mau_chuan_nhieu_chieu(mu, Lambda, n, hat)` | `X = μ + L·z`, `L` từ `phan_ra_cholesky` của Ch2 | `Λ` đối xứng xác định dương |
| `dac_trung_roi_rac` | `ky_vong(gia_tri, xac_suat)`, `phuong_sai`, `mot`, `trung_vi` | Từ bảng phân phối rời rạc | Tổng xác suất = 1 (trong `dung_sai`) |
| `bat_dang_thuc` | `can_markov(ky_vong, u)`, `can_chebyshev(phuong_sai, u)`, `can_chernoff(...)` | Cận trên; dùng để so với xác suất thực nghiệm | Markov: `X ≥ 0` |
| `monte_carlo` | `uoc_luong_xac_suat(thi_nghiem, n, hat) -> tuple[float, float]` | Tần suất và sai số chuẩn `√(p̂(1−p̂)/n)` | |
| | `mo_phong_luat_so_lon(...)`, `mo_phong_xap_xi_chuan(...)` | Trung bình mẫu và so sánh với `N(μ, σ²/n)` | |
| `vec_to_ngau_nhien` | `phan_phoi_bien(bang_dong_thoi)`, `hiep_phuong_sai(...)`, `he_so_tuong_quan(...)`, `ky_vong_co_dieu_kien(bang, x)` | Từ bảng phân phối đồng thời hai chiều | |
| | `ti_le_phuong_sai_nho_nhat(bang) -> float` | `s` tối thiểu hóa `Var(sX + (1−s)Y)` (nghiệm giải tích `s = (DY − Cov)/(DX + DY − 2Cov)`) | |
| `ung_dung_ml` | `NaiveBayesRoiRac` | `fit(X, y, lam_lam_tron=1.0)`, `predict`, `predict_proba` | Làm trơn Laplace |

Hàm `phan_phoi` được đối chiếu với `scipy.stats` ở `doi_chieu/` và test.

## 5. Chương 5 — `chuong_5_toi_uu`

| Module | Hàm | Mô tả | Điều kiện / lỗi |
|---|---|---|---|
| `tinh_loi` | `kiem_tra_loi_theo_dinh_nghia(f, mien, so_cap=2000, hat) -> KetQuaKiemChung` | Lấy mẫu cặp điểm `u, v` và `t`, tìm phản ví dụ của `f(tu+(1−t)v) ≤ t f(u) + (1−t) f(v)` | Chỉ **bác bỏ** được; không chứng minh lồi (nêu rõ trong kết quả) |
| | `kiem_tra_loi_theo_hessian(f, mien_mau, hat) -> KetQuaKiemChung` | Hessian bằng `hessian_so` (Ch3); bán xác định dương bằng Sylvester/trị riêng (Ch2) trên các điểm mẫu | |
| | `BANG_HAM_KIEM_TRA_LOI` | ≥ 6 hàm: lồi, lồi chặt, không lồi (kèm nhãn kỳ vọng) | |
| `quy_hoach_tuyen_tinh` | `MoHinhQHTT` (dataclass) | `c`, `A_ub`, `b_ub`, `A_eq`, `b_eq`, `can`, `ten_bien`, `mo_ta` | |
| | `dua_ve_dang_chuan(mo_hinh) -> MoHinhQHTT` | `Ax = b, x ≥ 0` bằng biến bù | |
| | `giai_qhtt(mo_hinh, phuong_phap="linprog") -> KetQuaQHTT` | Nghiệm, giá trị mục tiêu, trạng thái | Dùng `linprog` (D06) |
| | `kiem_tra_nghiem_chap_nhan(mo_hinh, x, dung_sai) -> KetQuaKiemChung` | Thỏa mọi ràng buộc | |
| | `liet_ke_cach_cat(L, cac_do_dai) -> Ma_tran` | Liệt kê các cách cắt một thanh `L` thành các đoạn (vòng lặp đệ quy), kèm phần dư | |
| | `mo_hinh_cat_vat_lieu(L, cac_do_dai, so_luong) -> MoHinhQHTT` | Biến `xⱼ` = số thanh cắt theo cách `j`; mục tiêu `Σ dⱼ xⱼ`; ràng buộc đủ số đoạn | **Ghi rõ** ràng buộc đẳng thức hay `≥`; nghiệm nguyên (D06) |
| | `mo_hinh_van_tai(cung, cau, cuoc_phi) -> MoHinhQHTT` | Tự thêm điểm phát hoặc thu giả (cước 0) khi không cân bằng | Phân biệt "đóng" và "mở" |
| `giam_gradient` | `gradient_descent(f, grad, x0, buoc="co_dinh"\|"giam_dan"\|"backtracking", eta=0.1, momentum=0.0, so_vong=1000, dung_sai=1e-8) -> KetQuaLap` | `KetQuaLap`: `x`, `lich_su_x`, `lich_su_f`, `lich_su_chuan_grad`, `so_vong`, `hoi_tu: bool` | `LoiHoiTu` hoặc `hoi_tu=False` có thể chọn; mặc định **không ném lỗi** mà trả `hoi_tu=False` để vẽ được đồ thị không hội tụ |
| | `newton(f, grad, hess, x0, so_vong, dung_sai)` | Giải `H·d = −g` bằng `giai_he_gauss_jordan` (Ch1) | `LoiMaTranSuyBien` nếu Hessian suy biến |
| | `ve_duong_dong_muc_va_quy_dao(...)` | Đường đồng mức cùng quỹ đạo; so số vòng lặp | |
| `lagrange` | `giai_lagrange_toan_phuong_rang_buoc_dang_thuc(P, q, A, b)` | Hệ KKT `[[P, Aᵀ],[A, 0]]` giải bằng Ch1; nghiệm giải tích | Đối chiếu nghiệm số |
| `quy_hoach_toan_phuong` | `diem_gan_nhat_tren_da_dien(a, G, h, phuong_phap="gradient_chieu") -> KetQuaQP` | `min ½‖x−a‖²` với `Gx ≤ h` | `"cvxopt"` chỉ khi cài được |
| | `frank_wolfe(...)` (nâng cao) | | Nâng cao |
| `ung_dung_ml` | `hoi_quy_logistic_l2(X, y, lam, phuong_phap="gradient_descent"\|"newton")` | Hàm mất mát, gradient (Ch3), Hessian; đối chiếu `scipy.optimize.minimize` | |

## 6. Chương 6 — `chuong_6_uoc_luong`

| Module | Hàm | Mô tả | Điều kiện / lỗi |
|---|---|---|---|
| `dac_trung_mau` | `trung_binh_mau(x)`, `phuong_sai_mau(x)`, `phuong_sai_mau_dieu_chinh(x)`, `do_lech_mau(x)`, `tan_suat_mau(x, tinh_chat)` | `phuong_sai_mau` chia **n**; `..._dieu_chinh` chia **n−1** | `len(x) ≥ 1` (hoặc ≥ 2 cho n−1) |
| | `dac_trung_tu_bang_tan_so(gia_tri, tan_so)`, `dac_trung_tu_bang_khoang(cac_khoang, tan_so)` | Khoảng được thay bằng trị đại diện (điểm giữa) | Các khoảng rời nhau |
| | `vec_to_trung_binh_mau(X)`, `ma_tran_hiep_phuong_sai_mau(X)` | `X` shape `(n, k)`, hàng là quan sát; công thức chia n | |
| | `mo_phong_do_chech(sigma2, n, so_mau, hat)` | Cho thấy `E[S²] = (n−1)/n·σ²` và `S′²` không chệch | |
| `khoang_tin_cay` | `ktc_trung_binh(x, gamma, sigma2=None, phia="hai_phia", quy_tac="bai_giang")` | `phia ∈ {"hai_phia","trai","phai"}`; quy tắc D08 | Trả `(can_duoi, can_tren)` có thể là `±inf` |
| | `ktc_ty_le(m, n, gamma, phia)`, `ktc_phuong_sai(x, gamma, phia)` | Tỷ lệ cho `n` lớn; phương sai dùng χ² | |
| | `mo_phong_do_phu(ham_ktc, tham_so_that, sinh_mau, so_mau=10000, hat) -> float` | Tỷ lệ khoảng chứa tham số thật | `so_mau ≥ 10000` theo đề |
| `uoc_luong` | `ols_duong_thang(x, y) -> tuple[float, float]` | `(a, b)` theo công thức đóng của slide | Cần ít nhất 2 giá trị `x` khác nhau |
| | `ols_tong_quat(X, y, bac_da_thuc=None) -> Vec_to` | Giải `(XᵀX)w = Xᵀy` bằng `giai_he_gauss_jordan` (Ch1) | `LoiMaTranSuyBien` nếu `XᵀX` suy biến |
| | `mle_chuan(x)` → `(mu, sigma2)` với `σ̂² = S²` (chia n); `mle_chuan_nhieu_chieu(X)`; `mle_categorical(dem)` → `λ̂ᵢ = Xᵢ/n`; `mle_nhi_thuc`, `mle_poisson`, `mle_mu` | Chọn **một** trong nhị thức/Poisson/mũ là bắt buộc, làm cả ba khi đủ thời gian | |
| | `cuc_dai_hoa_log_hop_ly_bang_so(log_hop_ly, grad, theta0)` | Dùng `gradient_descent` của Ch5 cho `−log L`; so với công thức đóng | |
| | `map_beta_bernoulli(m, n, alpha, beta)` | `θ̂ = (m+α−1)/(n+α+β−2)` | `n + α + β > 2`; `α = β = 1` trùng MLE |
| `ung_dung_ml` | `PhanLoaiSinhGaussian` | `fit` (MLE `μₖ, Λₖ` theo lớp), `predict` bằng quy tắc Bayes (Ch4) | |
| | `hoi_quy_tuyen_tinh_mle_map(X, y, lam)` | MAP với tiên nghiệm chuẩn tương ứng hồi quy ridge | |

## 7. `integration` (Phần C1)
`chay_pipeline(X, y, ...)`: chuẩn hóa dữ liệu → `pca` (Ch2) → `hoi_quy_logistic_l2` (Ch5) → ước lượng tham số bằng `mle_*`/`map_*` và khoảng tin cậy (Ch6). Hợp đồng chi tiết viết khi bắt đầu mục này; mục này là tùy chọn (khuyến khích) theo đề.

## 8. Quy tắc chung cho mọi hàm
1. Có type hints và docstring nêu: công thức, đầu vào/đầu ra, điều kiện, lỗi ném ra, độ phức tạp.
2. Gọi `xac_thuc_*` ở đầu hàm công khai; không sửa tham số đầu vào.
3. Ghi bước vào `nhat_ky` ở các mốc có ý nghĩa toán học (biến đổi hàng, chọn pivot, một vòng lặp, kết quả trung gian), không ghi từng phép cộng.
4. Không `print`. Không đọc biến môi trường hay `argv`.
5. Không `except:` trần.
