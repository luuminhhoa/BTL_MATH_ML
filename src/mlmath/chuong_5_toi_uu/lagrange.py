"""Nhân tử Lagrange cho bài toán toàn phương có ràng buộc đẳng thức."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def giai_lagrange_toan_phuong_rang_buoc_dang_thuc(
    P: Any,
    q: Any,
    A: Any,
    b: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Giải hệ KKT [[P, Aᵀ], [A, 0]] [x; λ] = [−q; b] bằng Ch1; trả (x*, λ*)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")
