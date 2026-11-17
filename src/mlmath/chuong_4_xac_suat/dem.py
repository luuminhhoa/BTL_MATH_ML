"""Tổ hợp, chỉnh hợp, hoán vị và log-tổ hợp."""

from __future__ import annotations

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def hoan_vi(n: int, nhat_ky: NhatKyTinhToan | None = None) -> int:
    """Tính n! (số nguyên chính xác)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def chinh_hop(n: int, k: int, nhat_ky: NhatKyTinhToan | None = None) -> int:
    """Tính chỉnh hợp A(n, k) với 0 ≤ k ≤ n."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def to_hop(n: int, k: int, nhat_ky: NhatKyTinhToan | None = None) -> int:
    """Tính tổ hợp C(n, k) với 0 ≤ k ≤ n."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def log_to_hop(n: int, k: int, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính ln C(n, k) bằng `math.lgamma` cho n lớn."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")
