"""Tọa độ và ma trận chuyển cơ sở P(B→S) theo quy ước bài giảng (D11)."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def ma_tran_chuyen_co_so(
    B: Any,
    S: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tính P(B→S) có cột j là [sⱼ]_B, sao cho [u]_B = P·[u]_S, bằng (B | S) → (I | P)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def toa_do_trong_co_so(
    u: Any,
    B: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tìm tọa độ [u]_B của vector u (đang cho ở cơ sở chính tắc)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def doi_toa_do(
    u_S: Any,
    P: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Đổi tọa độ [u]_B = P · [u]_S với P = P(B→S)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")
