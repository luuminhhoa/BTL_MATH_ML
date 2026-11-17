"""Alias tiếng Anh cho Chương 5 (chỉ re-export)."""

from __future__ import annotations

from .chuong_5_toi_uu.giam_gradient import gradient_descent, newton
from .chuong_5_toi_uu.quy_hoach_tuyen_tinh import giai_qhtt as solve_lp

__all__ = [
    "gradient_descent",
    "newton",
    "solve_lp",
]
