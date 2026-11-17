"""Phép toán ma trận cơ bản (tự cài, cấm `@` và `np.dot`)."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def chuyen_vi(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tính ma trận chuyển vị Aᵀ (m×n → n×m)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def chuyen_vi_lien_hop(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tính ma trận chuyển vị liên hợp Aᴴ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def cong_ma_tran(A: Any, B: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Cộng hai ma trận cùng kích thước A + B."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def tru_ma_tran(A: Any, B: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Trừ hai ma trận cùng kích thước A - B."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def nhan_so(k: Any, A: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Nhân vô hướng k · A."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def nhan_ma_tran(A: Any, B: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Nhân hai ma trận A · B bằng vòng lặp tường minh O(mnp), cấm `@` và `np.dot`."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def luy_thua(A: Any, k: int, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tính Aᵏ bằng bình phương liên tiếp (A vuông, k nguyên >= 0; A⁰ = I)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")
