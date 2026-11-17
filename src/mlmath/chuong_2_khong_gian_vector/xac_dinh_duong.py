"""Tiêu chuẩn Sylvester, tính xác định dương và phân rã Cholesky (D12)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


@dataclass
class KetQuaSylvester:
    """Kết quả kiểm tra theo tiêu chuẩn Sylvester."""

    loai: str  # "xac_dinh_duong" | "xac_dinh_am" | "chua_ket_luan"
    dinh_thuc_con: list[float]


def tieu_chuan_sylvester(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> KetQuaSylvester:
    """Áp dụng tiêu chuẩn Sylvester cho ma trận đối xứng (chỉ kết luận xác định)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def la_xac_dinh_duong(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận đối xứng có xác định dương hay không."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def la_ban_xac_dinh_duong(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra bán xác định dương bằng mọi định thức con chính (n ≤ 10) hoặc trị riêng."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def phan_ra_cholesky(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Phân rã Cholesky A = L · Lᴴ với L tam giác dưới, đường chéo dương."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def giai_he_cholesky(A: Any, b: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Giải hệ Ax = b với A xác định dương bằng thế xuôi và thế ngược qua Cholesky."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")
