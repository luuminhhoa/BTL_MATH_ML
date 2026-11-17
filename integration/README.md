# Mini-pipeline Tích hợp (`integration/` — Phần C1)

Nối các thành phần từ Chương 1–6 thành một luồng ML hoàn chỉnh:
1. Chuẩn hóa dữ liệu
2. Giảm chiều bằng `pca` (Chương 2)
3. Huấn luyện `hoi_quy_logistic_l2` (Chương 5)
4. Ước lượng tham số (`mle_*` / `map_*`) và đánh giá khoảng tin cậy (Chương 6)

- Mã nguồn: `integration/src/pipeline.py`
- Kiểm thử: `integration/tests/`
