"""Trị riêng, vector riêng, không gian riêng và chéo hóa (theo D04)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import numpy as np

from ..tien_ich.da_thuc import DaThuc, So
from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


@dataclass
class KetQuaRieng:
    """Kết quả phân tích trị riêng / vector riêng của ma trận vuông."""

    cac_tri_rieng: list[tuple[So, int, int, np.ndarray | None]]
    cheo_hoa_duoc: bool


def da_thuc_dac_trung(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> DaThuc:
    """Tính det(A − λI) qua Laplace trên DaThuc (giới hạn n ≤ 6 theo D04)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def tri_rieng(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> list[tuple[So, int]]:
    """Tìm trị riêng (thực hoặc phức) và bội đại số từ đa thức đặc trưng."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def khong_gian_rieng(A: Any, lam: float, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tìm cơ sở của không gian riêng N_λ = ker(A − λI) (chỉ cho λ thực)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def phan_tich_rieng(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> KetQuaRieng:
    """Phân tích trị riêng, bội đại số, bội hình học, không gian riêng và khả năng chéo hóa."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def cheo_hoa(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Chéo hóa A thành (P, D) với P⁻¹AP = D; ném LoiDieuKien nếu không chéo hóa được trên ℝ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def cheo_hoa_truc_giao(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Chéo hóa trực giao ma trận đối xứng A (P trực giao, PᵀAP = D)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def luy_thua_qua_cheo_hoa(A: Any, k: int, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tính Aᵏ = P · Dᵏ · P⁻¹ thông qua chéo hóa."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def jacobi_doi_xung(
    A: Any,
    so_vong_toi_da: int = 1000,
    dung_sai: float = 1e-10,
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Thuật toán Jacobi tìm trị riêng & vector riêng cho ma trận đối xứng cỡ lớn (nâng cao)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")
