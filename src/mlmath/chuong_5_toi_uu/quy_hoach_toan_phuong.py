"""Quy hoạch toàn phương (QP): điểm gần nhất trên đa diện lồi (D06)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


@dataclass
class KetQuaQP:
    """Kết quả bài toán quy hoạch toàn phương."""

    x: np.ndarray
    gia_tri_muc_tieu: float
    hoi_tu: bool


def diem_gan_nhat_tren_da_dien(
    a: Any,
    G: Any,
    h: Any,
    phuong_phap: str = "gradient_chieu",
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaQP:
    """Tìm x giải min ½‖x − a‖² với Gx ≤ h bằng gradient chiếu (hoặc cvxopt nếu có)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def frank_wolfe(
    a: Any,
    G: Any,
    h: Any,
    so_vong: int = 500,
    dung_sai: float = 1e-8,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaQP:
    """Thuật toán Frank–Wolfe giải bài toán QP trên đa diện lồi (nâng cao)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")
