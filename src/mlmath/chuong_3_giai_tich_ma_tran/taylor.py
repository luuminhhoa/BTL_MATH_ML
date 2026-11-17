"""Khai triển Taylor bậc 1, bậc 2 cho hàm nhiều biến và đánh giá sai số."""

from __future__ import annotations

from typing import Any, Callable, Sequence

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def taylor_bac_1(
    f: Callable[[np.ndarray], float],
    gradient: Callable[[np.ndarray], np.ndarray],
    a: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> Callable[[np.ndarray], float]:
    """Trả về hàm xấp xỉ Taylor bậc 1 quanh điểm a."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")


def taylor_bac_2(
    f: Callable[[np.ndarray], float],
    gradient: Callable[[np.ndarray], np.ndarray],
    hessian: Callable[[np.ndarray], np.ndarray],
    a: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> Callable[[np.ndarray], float]:
    """Trả về hàm xấp xỉ Taylor bậc 2 quanh điểm a."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")


def sai_so_taylor(
    f: Callable[[np.ndarray], float],
    xap_xi: Callable[[np.ndarray], float],
    a: Any,
    huong: Any,
    cac_h: Sequence[float],
    nhat_ky: NhatKyTinhToan | None = None,
) -> dict[str, Any]:
    """Đo sai số theo bước h và ước lượng bậc hội tụ qua hệ số góc log–log."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")
