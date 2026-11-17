"""Các lớp ngoại lệ dùng chung trong thư viện `mlmath` (theo quyết định D15)."""

from __future__ import annotations


class LoiDuLieu(ValueError):
    """Lỗi dữ liệu đầu vào không hợp lệ (nan, inf, rỗng, kiểu không hỗ trợ)."""


class LoiKichThuoc(LoiDuLieu):
    """Lỗi kích thước ma trận hoặc vector không tương thích."""


class LoiMaTranSuyBien(LoiDuLieu):
    """Lỗi ma trận suy biến (det = 0 hoặc không khả nghịch)."""


class LoiDieuKien(LoiDuLieu):
    """Lỗi vi phạm điều kiện toán học (không đối xứng, không xác định dương, v.v.)."""


class LoiHoiTu(RuntimeError):
    """Lỗi thuật toán lặp không hội tụ trong số vòng cho phép."""
