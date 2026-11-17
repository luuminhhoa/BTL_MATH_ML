"""Ma trận nghịch đảo (Gauss–Jordan, phụ hợp) và khảo sát khả nghịch."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def nghich_dao_gauss_jordan(
    A: Any,
    chon_pivot: bool = True,
    dung_sai: float | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tìm A⁻¹ bằng biến đổi (A | I) → (I | A⁻¹) hai pha."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def phan_phu_dai_so(
    A: Any,
    i: int,
    j: int,
    nhat_ky: NhatKyTinhToan | None = None,
) -> Any:
    """Tính phần phụ đại số Cᵢⱼ = (−1)^{i+j} · det(Aᵢⱼ)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def ma_tran_phu_hop(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tính ma trận phụ hợp adj(A) = (Cᵢⱼ)ᵀ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def nghich_dao_phu_hop(
    A: Any,
    dung_sai: float | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tìm A⁻¹ = adj(A) / det(A)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def khao_sat_kha_nghich(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> dict[str, Any]:
    """Khảo sát khả nghịch của A qua định thức và hạng để đối chiếu nhau."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def so_dieu_kien(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính số điều kiện κ₁(A) = ‖A‖₁ · ‖A⁻¹‖₁."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")
