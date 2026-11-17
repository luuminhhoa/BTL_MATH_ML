"""Thuật toán tối ưu lặp: Gradient Descent (cố định, giảm dần, backtracking, momentum) và Newton."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


@dataclass
class KetQuaLap:
    """Kết quả của thuật toán tối ưu lặp."""

    x: np.ndarray
    lich_su_x: list[np.ndarray]
    lich_su_f: list[float]
    lich_su_chuan_grad: list[float]
    so_vong: int
    hoi_tu: bool


def gradient_descent(
    f: Callable[[np.ndarray], float],
    grad: Callable[[np.ndarray], np.ndarray],
    x0: Any,
    buoc: str = "co_dinh",
    eta: float = 0.1,
    momentum: float = 0.0,
    so_vong: int = 1000,
    dung_sai: float = 1e-8,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaLap:
    """Tối ưu không ràng buộc bằng Gradient Descent; trả `hoi_tu=False` nếu chưa hội tụ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def newton(
    f: Callable[[np.ndarray], float],
    grad: Callable[[np.ndarray], np.ndarray],
    hess: Callable[[np.ndarray], np.ndarray],
    x0: Any,
    so_vong: int = 100,
    dung_sai: float = 1e-8,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaLap:
    """Phương pháp Newton giải H·d = −g bằng `giai_he_gauss_jordan` (Ch1)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def ve_duong_dong_muc_va_quy_dao(
    f: Callable[[np.ndarray], float],
    cac_quy_dao: dict[str, KetQuaLap],
    duong_dan: str | Path,
    nhat_ky: NhatKyTinhToan | None = None,
) -> Path:
    """Vẽ đường đồng mức của f cùng quỹ đạo hội tụ của các thuật toán."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")
