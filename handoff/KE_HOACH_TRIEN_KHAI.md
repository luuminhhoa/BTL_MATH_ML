# Kế hoạch Triển khai (`KE_HOACH_TRIEN_KHAI.md`)

Thứ tự triển khai bắt buộc (xem `docs/KIEN_TRUC.md` §5):

1. **Giai đoạn 0 — Hạ tầng & Phần A (Đã dựng khung):**
   - `flow/` (sơ đồ, quy tắc, templates, checklist, risks, pilot).
   - `mlmath.loi`, `mlmath.tien_ich`, `mlmath.dich_vu`, `mlmath.giao_dien`.
   - `tests/unit/test_cam_thu_vien.py` và `tests/unit/test_tien_ich.py`.
2. **Giai đoạn 1 — Chương 1 (`chuong_1_ma_tran`):**
   - Phép toán cơ bản (cấm `@`, `np.dot`), dạng ma trận, định thức Laplace & Gauss, hạng, nghịch đảo Gauss–Jordan & phụ hợp, giải hệ, tìm tham số suy biến.
3. **Giai đoạn 2 — Chương 2 (`chuong_2_khong_gian_vector`):**
   - Chuẩn & hình cầu đơn vị, độc lập tuyến tính, đổi cơ sở `P(B→S)`, Gram–Schmidt, ánh xạ tuyến tính, trị riêng/chéo hóa, Sylvester/Cholesky, vết, PCA.
4. **Giai đoạn 3 — Chương 3 (`chuong_3_giai_tich_ma_tran`):**
   - Sai phân số, `BANG_DAO_HAM`, quy tắc tích/chuỗi, Taylor, khảo sát sai số theo `delta`, cực trị.
5. **Giai đoạn 4 — Chương 4 (`chuong_4_xac_suat`):**
   - Tự học (`selfstudy.md`), đếm, Bayes, phân phối, đặc trưng rời rạc, bất đẳng thức, Monte Carlo, vector ngẫu nhiên, Naive Bayes rời rạc.
6. **Giai đoạn 5 — Chương 5 (`chuong_5_toi_uu`):**
   - Kiểm tra lồi, QHTT, Gradient Descent & Newton, Lagrange KKT, QP điểm gần nhất trên đa diện, Logistic L2.
7. **Giai đoạn 6 — Chương 6 (`chuong_6_uoc_luong`):**
   - Đặc trưng mẫu (`ddof=0` vs `ddof=1`), khoảng tin cậy (quy tắc bài giảng), OLS, MLE, MAP, Gaussian Generative Classifier.
8. **Giai đoạn 7 — Phần C (`integration/` & `reports/`):**
   - Mini-pipeline C1, tổng hợp số liệu thực tế vào `reports/reflection.md`.
