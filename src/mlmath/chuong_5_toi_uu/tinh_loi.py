"""Kiểm tra tính lồi theo định nghĩa và theo ma trận Hessian."""

from __future__ import annotations

from typing import Any, Callable, Sequence

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan
from ..tien_ich.xuat_ket_qua import KetQuaKiemChung

BANG_HAM_KIEM_TRA_LOI: dict[str, Any] = {}


def kiem_tra_loi_theo_dinh_nghia(
    f: Callable[[np.ndarray], float],
    mien: Sequence[tuple[float, float]],
    so_cap: int = 2000,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaKiemChung:
    """Lấy mẫu ngẫu nhiên tìm phản ví dụ của bất đẳng thức Jensen (chỉ bác bỏ được)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def kiem_tra_loi_theo_hessian(
    f: Callable[[np.ndarray], float],
    mien_mau: Sequence[np.ndarray],
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaKiemChung:
    """Kiểm tra Hessian bán xác định dương tại các điểm mẫu."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")
