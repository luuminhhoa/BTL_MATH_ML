"""Mô phỏng Monte Carlo, Luật số lớn và Xấp xỉ chuẩn."""

from __future__ import annotations

from typing import Any, Callable

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def uoc_luong_xac_suat(
    thi_nghiem: Callable[[np.random.Generator], bool],
    n: int,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[float, float]:
    """Ước lượng xác suất và sai số chuẩn √(p̂(1−p̂)/n) qua n lần thử."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def mo_phong_luat_so_lon(
    sinh_mau: Callable[[np.random.Generator, int], np.ndarray],
    cac_n: list[int],
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> dict[int, float]:
    """Tính trung bình mẫu theo các cỡ mẫu tăng dần để minh họa Luật số lớn."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def mo_phong_xap_xi_chuan(
    sinh_mau: Callable[[np.random.Generator, int], np.ndarray],
    n: int,
    so_lan: int = 2000,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> dict[str, Any]:
    """Mô phỏng phân phối trung bình mẫu và so sánh với N(μ, σ²/n)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")
