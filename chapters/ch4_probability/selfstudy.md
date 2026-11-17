# Ghi chú Tự học — Chương 4: Xác suất (`selfstudy.md`)

> **Hướng dẫn điền (theo quyết định D17):**
> Chương 4 là phần tự học có hướng dẫn. Sinh viên tự ghi lại tài liệu đã đọc, tóm tắt định nghĩa/định lý cốt lõi bằng lời của mình và các điểm dễ nhầm lẫn trước khi lập trình.

## 1. Tài liệu tham khảo đã sử dụng
- *(Ví dụ: Slide bài giảng Chương 4; Mathematics for Machine Learning — Deisenroth et al.; PRML — Bishop)*

## 2. Tóm tắt kiến thức cốt lõi
1. **Không gian xác suất, xác suất có điều kiện, định lý Bayes:** *(tự tóm tắt)*
2. **Các phân phối xác suất rời rạc & liên tục:** *(Nhị thức, Siêu bội, Poisson, Chuẩn, Đều, Mũ)*
3. **Kỳ vọng, phương sai, hiệp phương sai, hệ số tương quan:** *(tự tóm tắt)*
4. **Các bất đẳng thức (Markov, Chebyshev, Chernoff) & Luật số lớn / Định lý giới hạn trung tâm:** *(tự tóm tắt)*

## 3. Điểm lưu ý khi lập trình
- Hàm PDF/CDF tự cài (dùng `math.erf` cho chuẩn), đối chiếu với `scipy.stats`.
- Sinh mẫu biến đổi ngược cho phân phối đều, mũ; sinh mẫu chuẩn nhiều chiều dùng Cholesky từ Chương 2.
