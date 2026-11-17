"""Ước lượng điểm: OLS, MLE và MAP."""

from __future__ import annotations

from typing import Any, Callable

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def ols_duong_thang(x: Any, y: Any, nhat_ky: NhatKyTinhToan | None = None) -> tuple[float, float]:
    """Ước lượng bình phương tối thiểu (a, b) cho đường thẳng y = ax + b."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def ols_tong_quat(
    X: Any,
    y: Any,
    bac_da_thuc: int | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Giải phương trình chuẩn (XᵀX)w = Xᵀy bằng `giai_he_gauss_jordan` (Ch1)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def mle_chuan(x: Any, nhat_ky: NhatKyTinhToan | None = None) -> tuple[float, float]:
    """Ước lượng MLE (μ̂, σ̂²) của phân phối chuẩn với σ̂² = S² (chia n)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def mle_chuan_nhieu_chieu(X: Any, nhat_ky: NhatKyTinhToan | None = None) -> tuple[np.ndarray, np.ndarray]:
    """Ước lượng MLE (μ̂, Λ̂) của phân phối chuẩn nhiều chiều."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def mle_categorical(dem: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Ước lượng MLE λ̂ᵢ = Xᵢ / n cho phân phối Categorical."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def mle_nhi_thuc(m: int, n: int, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Ước lượng MLE p̂ = m / n cho phân phối nhị thức."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def mle_poisson(x: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Ước lượng MLE λ̂ = x̄ cho phân phối Poisson."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def mle_mu(x: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Ước lượng MLE λ̂ = 1 / x̄ cho phân phối mũ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def cuc_dai_hoa_log_hop_ly_bang_so(
    log_hop_ly: Callable[[np.ndarray], float],
    grad: Callable[[np.ndarray], np.ndarray],
    theta0: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Cực đại hóa log-likelihood bằng `gradient_descent` (Ch5) cho −log L."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def map_beta_bernoulli(
    m: int,
    n: int,
    alpha: float,
    beta: float,
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Ước lượng MAP với tiên nghiệm liên hợp Beta(α, β): θ̂ = (m+α−1)/(n+α+β−2)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")
