# Chuẩn viết mã (`CHUAN_VIET_MA.md`)

1. **Ngôn ngữ & Kiểu:** Python 3.10+, đầy đủ type hints (`from __future__ import annotations` nếu cần).
2. **Docstring & Chú thích:** Tiếng Việt có dấu. Mỗi hàm công khai phải nêu: mục đích, công thức toán (dùng Unicode `Aᵀ`, `A⁻¹`, `‖x‖₂`), đầu vào/đầu ra, điều kiện, ngoại lệ ném ra, độ phức tạp.
3. **Kiểm tra đầu vào:** Gọi `xac_thuc_*` ở đầu hàm công khai; tuyệt đối không làm biến đổi (mutate) mảng đầu vào.
4. **Ngoại lệ (D15):** Dùng các lớp trong `mlmath.loi` (`LoiDuLieu`, `LoiKichThuoc`, `LoiMaTranSuyBien`, `LoiDieuKien`, `LoiHoiTu`). Không dùng `except:` hoặc `except Exception:` trần để nuốt lỗi.
5. **Tách lớp (D14):** Trong `src/mlmath/chuong_N_*`: không `print`, không đọc/ghi file (trừ hàm `ve_*` lưu đồ thị ra đường dẫn được truyền vào), không đọc `argv`. Ghi bước vào `nhat_ky: NhatKyTinhToan | None = None`.
6. **Ranh giới thư viện (D03):** Tuân thủ nghiêm ngặt danh sách hàm cấm; chạy `pytest tests/unit/test_cam_thu_vien.py` sau mỗi thay đổi.
7. **Số ngẫu nhiên:** Luôn nhận tham số `hat: np.random.Generator | None = None`; không dùng `np.random.seed`.
