"""Đặc trưng của biến ngẫu nhiên rời rạc (kỳ vọng, phương sai, mốt, trung vị)."""

from __future__ import annotations

from typing import Any

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def ky_vong(gia_tri: Any, xac_suat: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính E[X] từ bảng phân phối rời rạc."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def phuong_sai(gia_tri: Any, xac_suat: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính Var(X) từ bảng phân phối rời rạc."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def mot(gia_tri: Any, xac_suat: Any, nhat_ky: NhatKyTinhToan | None = None) -> list[Any]:
    """Tìm các giá trị mốt (mode) của phân phối rời rạc."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def trung_vi(gia_tri: Any, xac_suat: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tìm trung vị (median) của phân phối rời rạc."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")
