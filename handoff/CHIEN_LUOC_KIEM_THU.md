# Chiến lược Kiểm thử (`CHIEN_LUOC_KIEM_THU.md`)

## 1. Ba tầng kiểm thử bắt buộc
1. **Tầng 1 — Tự cài & trường hợp biên:** Ma trận 1×1, suy biến, pivot = 0 cần đổi hàng, dữ liệu `Fraction`/`complex128`/`float64`, dữ liệu rỗng/`nan`/`inf` ném đúng ngoại lệ.
2. **Tầng 2 — Đối chiếu thư viện (Oracle):** Dùng `numpy.linalg`, `scipy.stats`, `scipy.optimize`, `sympy`, `sklearn` trong `chapters/*/tests/` và `chapters/*/doi_chieu/`.
   - Dung sai mặc định: `rtol=1e-9, atol=1e-10` cho thuật toán trực tiếp; `1e-6` cho sai phân số.
3. **Tầng 3 — Tính chất toán học (Property-based):**
   - `A @ A⁻¹ ≈ I`, `det(A @ B) ≈ det(A) * det(B)`
   - `Qᵀ @ Q ≈ I` (Gram–Schmidt), `P⁻¹ @ A @ P ≈ D` (chéo hóa)
   - `L @ Lᴴ ≈ A` (Cholesky), `dim Im + dim Ker = n`
   - Đối chiếu với đáp án giải tay độc lập (lưu ý D16: kiểm tra lại đáp án in trong slide).

## 2. Kiểm thử ranh giới thư viện
- `tests/unit/test_cam_thu_vien.py` quét AST toàn bộ `src/mlmath/` để bảo đảm không dùng `@`/`np.dot` ở Ch1 và không dùng `np.linalg.*`/`scipy.linalg.*` trong toàn bộ mã tự cài.

## 3. Đánh dấu test chậm
- Gắn `@pytest.mark.cham` cho các test đo thời gian Laplace (`n ≤ 9`) hoặc mô phỏng Monte Carlo / độ phủ (`so_mau >= 10000`).
