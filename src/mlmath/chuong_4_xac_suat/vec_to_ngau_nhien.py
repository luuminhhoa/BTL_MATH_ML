"""Vector ngẫu nhiên hai chiều rời rạc: biên, hiệp phương sai, tương quan."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def phan_phoi_bien(
    bang_dong_thoi: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Tính phân phối biên của X (theo hàng) và Y (theo cột) từ bảng đồng thời."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def hiep_phuong_sai(
    bang_dong_thoi: Any,
    gia_tri_x: Any,
    gia_tri_y: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Tính Cov(X, Y) từ bảng phân phối đồng thời."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def he_so_tuong_quan(
    bang_dong_thoi: Any,
    gia_tri_x: Any,
    gia_tri_y: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Tính hệ số tương quan Pearson ρ(X, Y)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def ky_vong_co_dieu_kien(
    bang_dong_thoi: Any,
    gia_tri_x: Any,
    gia_tri_y: Any,
    x_idx: int,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Tính E[Y | X = xᵢ] từ bảng phân phối đồng thời."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def ti_le_phuong_sai_nho_nhat(
    bang_dong_thoi: Any,
    gia_tri_x: Any,
    gia_tri_y: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Tìm s tối thiểu hóa Var(sX + (1−s)Y): s = (DY − Cov)/(DX + DY − 2Cov)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")
