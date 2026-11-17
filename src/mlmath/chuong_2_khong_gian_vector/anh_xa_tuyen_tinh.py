"""Ánh xạ tuyến tính: kiểm tra tính tuyến tính, ma trận ánh xạ, Im, Ker, đồng dạng."""

from __future__ import annotations

from typing import Any, Callable

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan
from ..tien_ich.xuat_ket_qua import KetQuaKiemChung


def kiem_tra_tuyen_tinh(
    f: Callable[[np.ndarray], np.ndarray],
    n: int,
    so_mau: int = 20,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaKiemChung:
    """Kiểm tra cộng tính và thuần nhất trên mẫu ngẫu nhiên (chỉ là bằng chứng số)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def ma_tran_anh_xa(
    f: Callable[[np.ndarray], np.ndarray],
    n_vao: int,
    co_so_vao: Any = None,
    co_so_ra: Any = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tìm ma trận của ánh xạ tuyến tính f trong cặp cơ sở (cột j = [f(uⱼ)]_S)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def co_so_khong_gian_anh(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tìm cơ sở của không gian ảnh Im(A) (các cột trả về là vector cơ sở)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def co_so_khong_gian_nhan(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tìm cơ sở của không gian nhân Ker(A) = {x : Ax = 0} bằng Gauss–Jordan."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def kiem_tra_dinh_ly_so_chieu(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> KetQuaKiemChung:
    """Kiểm chứng định lý số chiều: dim Im(A) + dim Ker(A) = n."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def doi_co_so_bien_doi(
    A: Any,
    P: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tính ma trận đồng dạng A′ = P⁻¹ · A · P."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")
