"""Quy tắc tính đạo hàm tích và đạo hàm hàm hợp (quy tắc chuỗi) theo D09."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def quy_tac_tich(
    jac_f: Any,
    jac_g: Any,
    f_x: Any,
    g_x: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tính ∇(fᵀg) = ∇f·g + ∇g·f (theo bố trí bài giảng D09)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")


def quy_tac_chuoi(
    jac_x_f: Any,
    jac_f_g: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tính ∇ₓg(f(x)) = ∇ₓf · ∇_f g (thứ tự nhân cố định theo D09)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")
