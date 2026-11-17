"""Bảng các công thức đạo hàm ma trận giải tích và kiểm tra bằng sai phân số."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan
from ..tien_ich.xuat_ket_qua import KetQuaKiemChung


@dataclass(frozen=True)
class MucDaoHam:
    """Một mục trong bảng đạo hàm ma trận/vector."""

    ten: str
    cong_thuc: str
    f: Callable[..., Any]
    gradient_giai_tich: Callable[..., np.ndarray]
    tao_dau_vao: Callable[[np.random.Generator, int], dict[str, Any]]


BANG_DAO_HAM: dict[str, MucDaoHam] = {}


def kiem_tra_dao_ham(
    muc: MucDaoHam,
    hat: np.random.Generator,
    so_mau: int = 20,
    delta: float = 1e-5,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaKiemChung:
    """Kiểm chứng gradient giải tích so với gradient số (< 1e-6 với sai phân trung tâm)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")
