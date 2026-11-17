"""Tính xấp xỉ Gradient, Jacobian và Hessian bằng sai phân số (D09)."""

from __future__ import annotations

from typing import Any, Callable

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def gradient_so(
    f: Callable[[np.ndarray], float],
    x: Any,
    delta: float = 1e-5,
    kieu: str = "trung_tam",
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tính gradient số ∇f(x) với x có shape bất kỳ; kết quả cùng shape với x."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")


def jacobian_so(
    f: Callable[[np.ndarray], np.ndarray],
    x: Any,
    delta: float = 1e-5,
    kieu: str = "trung_tam",
    bo_tri: str = "bai_giang",
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tính Jacobian số cho f: ℝᵐ → ℝⁿ (bo_tri='bai_giang' trả (m, n), 'chuan' trả (n, m))."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")


def hessian_so(
    f: Callable[[np.ndarray], float],
    x: Any,
    delta: float = 1e-4,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tính ma trận Hessian số ∇²f(x) đối xứng."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")
