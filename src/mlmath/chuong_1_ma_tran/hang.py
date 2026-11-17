"""Đưa ma trận về dạng bậc thang và tính hạng ma trận."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def dua_ve_bac_thang(
    A: Any,
    chon_pivot: bool = True,
    dung_sai: float | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[np.ndarray, int]:
    """Đưa A về dạng bậc thang; trả về `(A_bac_thang, so_lan_doi_hang)`."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def hang_ma_tran(
    A: Any,
    dung_sai: float | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> int:
    """Tính hạng rank(A) bằng số hàng khác 0 của dạng bậc thang."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")
