"""Tìm tham số m làm ma trận suy biến (det A(m) = 0)."""

from __future__ import annotations

from typing import Any, Callable

import numpy as np

from ..tien_ich.da_thuc import DaThuc, So
from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def tim_tham_so_suy_bien(
    ma_tran_theo_m: Callable[[DaThuc], np.ndarray],
    nhat_ky: NhatKyTinhToan | None = None,
) -> list[tuple[So, int]]:
    """Tìm các giá trị m làm det(A(m)) = 0 bằng cách tính định thức trên DaThuc."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")
