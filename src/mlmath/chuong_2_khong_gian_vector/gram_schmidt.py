"""Trực giao hóa và trực chuẩn hóa Gram–Schmidt."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan
from ..tien_ich.xuat_ket_qua import KetQuaKiemChung


def gram_schmidt(
    V: Any,
    chuan_hoa: bool = True,
    dung_sai: float = 1e-12,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Trực giao (hoặc trực chuẩn) hóa các cột của V bằng Gram–Schmidt cổ điển."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def do_mat_truc_giao(Q: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Đo độ mất trực giao ‖QᵀQ − I‖_F."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def kiem_tra_khong_gian_sinh_khong_doi(
    V: Any,
    Q: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaKiemChung:
    """Kiểm tra span(V) = span(Q) bằng so sánh hạng."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def gram_schmidt_cai_tien(
    V: Any,
    chuan_hoa: bool = True,
    dung_sai: float = 1e-12,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Gram–Schmidt cải tiến (MGS) ổn định số hơn (nâng cao)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")
