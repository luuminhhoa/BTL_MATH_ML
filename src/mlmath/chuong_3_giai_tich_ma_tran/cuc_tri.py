"""Phân loại điểm dừng dựa trên ma trận Hessian."""

from __future__ import annotations

from typing import Any

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def phan_loai_diem_dung(H: Any, nhat_ky: NhatKyTinhToan | None = None) -> str:
    """Phân loại điểm dừng bằng Sylvester (Ch2): 'cuc_tieu' | 'cuc_dai' | 'yen_ngua' | 'chua_ket_luan'."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")
