# Hướng dẫn sử dụng `mlmath`

## 1. Cài đặt môi trường
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r docs/requirements.txt
pip install -e .
```

## 2. Sử dụng qua giao diện dòng lệnh (CLI)
```bash
# Mở menu tương tác
python -m mlmath.giao_dien menu

# Liệt kê thuật toán (tất cả hoặc theo chương)
python -m mlmath.giao_dien liet-ke
python -m mlmath.giao_dien liet-ke --chuong 1

# Chạy một thuật toán cụ thể
python -m mlmath.giao_dien chay ch1.nghich_dao_gauss_jordan --ma-tran "[[1,2,-1],[1,2,1],[2,3,0]]" --xuat terminal,txt,json
```

**Lưu ý nhập liệu trên CLI:**
- Ma trận và vector được phân tích an toàn bằng `ast.literal_eval`.
- Để nhập phân số chính xác (`Fraction`), dùng chuỗi trong danh sách, ví dụ: `"[[\"1/2\", 1], [0, \"3/4\"]]"`.

## 3. Sử dụng trong mã Python / Test
- Tên gốc tiếng Việt:
  ```python
  from mlmath.chuong_1_ma_tran.nghich_dao import nghich_dao_gauss_jordan
  ```
- Alias tiếng Anh (tương thích test mẫu):
  ```python
  from mlmath.ch1 import inverse_gj
  ```

## 4. Chạy kiểm thử
```bash
pytest                  # Chạy toàn bộ test (trừ nếu cấu hình khác)
pytest -m "not cham"    # Bỏ qua các test chạy chậm
pytest tests/unit/test_cam_thu_vien.py   # Kiểm tra ranh giới thư viện
```
