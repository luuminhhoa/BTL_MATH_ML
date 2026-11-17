"""Chuẩn vector, chuẩn Frobenius và vẽ hình cầu đơn vị."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Sequence

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def chuan_euclid(x: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính chuẩn Euclid ‖x‖₂."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def chuan_vo_cung(x: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính chuẩn vô cùng ‖x‖∞ = max |xᵢ|."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def chuan_p(x: Any, p: float, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính chuẩn ℓₚ (p ≥ 1); ném LoiDieuKien nếu p < 1."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def chuan_frobenius(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính chuẩn Frobenius ‖A‖_F = √(Σ |aᵢⱼ|²)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def khoang_cach_frobenius(A: Any, B: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính khoảng cách Frobenius ‖A − B‖_F."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def gan_nhat_theo_frobenius(
    A: Any,
    ung_vien: Sequence[Any],
    nhat_ky: NhatKyTinhToan | None = None,
) -> tuple[int, list[float]]:
    """Tìm chỉ số ứng viên gần A nhất theo chuẩn Frobenius và danh sách khoảng cách."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def ve_hinh_cau_don_vi(
    cac_chuan: Sequence[float],
    duong_dan: str | Path,
    nhat_ky: NhatKyTinhToan | None = None,
) -> Path:
    """Vẽ hình cầu đơn vị trong ℝ² cho nhiều chuẩn ℓₚ và lưu ra `duong_dan`."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")
