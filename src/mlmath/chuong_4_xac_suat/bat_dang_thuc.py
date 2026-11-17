"""Các bất đẳng thức xác suất: Markov, Chebyshev, Chernoff."""

from __future__ import annotations

from typing import Callable

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def can_markov(ky_vong_val: float, u: float, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Cận trên Markov P(X ≥ u) ≤ E[X] / u với X ≥ 0, u > 0."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def can_chebyshev(phuong_sai_val: float, u: float, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Cận trên Chebyshev P(|X − μ| ≥ u) ≤ Var(X) / u²."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def can_chernoff(
    mgf: Callable[[float], float],
    u: float,
    t_duong: float,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Cận trên Chernoff P(X ≥ u) ≤ exp(-t·u) · M_X(t) với t > 0."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")
