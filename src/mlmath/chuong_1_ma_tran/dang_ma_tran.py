"""Nhận dạng các dạng ma trận đặc biệt."""

from __future__ import annotations

from typing import Any

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def la_vuong(A: Any, dung_sai: float | None = None, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận có vuông (m == n) hay không."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def la_bac_thang(A: Any, dung_sai: float | None = None, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận có ở dạng bậc thang hay không."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def la_tam_giac_tren(A: Any, dung_sai: float | None = None, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận vuông tam giác trên."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def la_tam_giac_duoi(A: Any, dung_sai: float | None = None, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận vuông tam giác dưới."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def la_cheo(A: Any, dung_sai: float | None = None, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận đường chéo."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def la_don_vi(A: Any, dung_sai: float | None = None, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận đơn vị I."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def la_doi_xung(A: Any, dung_sai: float | None = None, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận đối xứng A = Aᵀ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def la_hermitian(A: Any, dung_sai: float | None = None, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra ma trận Hermitian A = Aᴴ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def nhan_dang_dang_ma_tran(A: Any, nhat_ky: NhatKyTinhToan | None = None) -> dict[str, bool]:
    """Trả về từ điển đánh dấu tất cả các dạng ma trận đặc biệt của A."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")
