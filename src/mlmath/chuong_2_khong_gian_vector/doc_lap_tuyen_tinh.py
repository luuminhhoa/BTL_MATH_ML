"""Độc lập tuyến tính, hạng hệ vector và trích cơ sở."""

from __future__ import annotations

from typing import Any

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def hang_he_vec_to(V: Any, nhat_ky: NhatKyTinhToan | None = None) -> int:
    """Tính hạng của hệ vector (các cột của ma trận V)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def la_doc_lap_tuyen_tinh(V: Any, nhat_ky: NhatKyTinhToan | None = None) -> bool:
    """Kiểm tra hệ các vector cột của V có độc lập tuyến tính không."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def trich_co_so(V: Any, nhat_ky: NhatKyTinhToan | None = None) -> list[int]:
    """Trích chỉ số các cột của V tạo thành cơ sở của không gian sinh (theo vị trí pivot)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")


def so_chieu(V: Any, nhat_ky: NhatKyTinhToan | None = None) -> int:
    """Tính số chiều dim span(V)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §2.")
