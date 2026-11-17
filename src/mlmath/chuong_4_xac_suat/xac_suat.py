"""Công thức xác suất đầy đủ, Bayes và lược đồ Bernoulli."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def xac_suat_day_du(
    p_he: Any,
    p_co_dieu_kien: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Tính P(A) = Σ P(Aⱼ)·P(A|Aⱼ)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def bayes(
    p_he: Any,
    p_co_dieu_kien: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Tính vector hậu nghiệm P(Aₖ|A) cho mọi k."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def bernoulli(
    n: int,
    p: float,
    k: int,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Tính xác suất P(X = k) theo lược đồ Bernoulli."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def so_thanh_cong_kha_nang_nhat(
    n: int,
    p: float,
    nhat_ky: NhatKyTinhToan | None = None,
) -> list[int]:
    """Tìm k* khả năng nhất trong lược đồ Bernoulli (xử lý trường hợp (n+1)p nguyên)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")
