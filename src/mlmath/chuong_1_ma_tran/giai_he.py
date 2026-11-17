"""Giải hệ phương trình tuyến tính Ax = b bằng Gauss–Jordan."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


@dataclass
class KetQuaHe:
    """Kết quả phân loại và giải hệ phương trình tuyến tính Ax = b."""

    loai: str  # "duy_nhat" | "vo_nghiem" | "vo_so_nghiem"
    nghiem_rieng: np.ndarray | None
    co_so_khong_gian_nghiem: np.ndarray | None
    hang_A: int
    hang_Ab: int


def giai_he_gauss_jordan(
    A: Any,
    b: Any,
    dung_sai: float | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaHe:
    """Giải hệ Ax = b bằng Gauss–Jordan và phân loại nghiệm theo rank(A), rank(A|b)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")
