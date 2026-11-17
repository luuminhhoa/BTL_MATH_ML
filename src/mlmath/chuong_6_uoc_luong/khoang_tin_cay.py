"""Khoảng tin cậy theo quy tắc bài giảng và mô phỏng độ phủ (D08)."""

from __future__ import annotations

from typing import Any, Callable

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def ktc_trung_binh(
    x: Any,
    gamma: float,
    sigma2: float | None = None,
    phia: str = "hai_phia",
    quy_tac: str = "bai_giang",
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[float, float]:
    """Tính khoảng tin cậy cho kỳ vọng (quy_tac='bai_giang' | 'student' theo D08)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def ktc_ty_le(
    m: int,
    n: int,
    gamma: float,
    phia: str = "hai_phia",
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[float, float]:
    """Tính khoảng tin cậy cho tỷ lệ p với cỡ mẫu n lớn."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def ktc_phuong_sai(
    x: Any,
    gamma: float,
    phia: str = "hai_phia",
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[float, float]:
    """Tính khoảng tin cậy cho phương sai σ² dùng phân phối χ²."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def mo_phong_do_phu(
    ham_ktc: Callable[[np.ndarray], tuple[float, float]],
    tham_so_that: float,
    sinh_mau: Callable[[np.random.Generator], np.ndarray],
    so_mau: int = 10000,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Mô phỏng tỷ lệ khoảng tin cậy chứa `tham_so_that` trên `so_mau` ≥ 10.000 lần lặp."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")
