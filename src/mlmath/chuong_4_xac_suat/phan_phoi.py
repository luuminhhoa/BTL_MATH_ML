"""Các phân phối xác suất tự cài (PMF, PDF, CDF) và sinh mẫu (D07)."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def nhi_thuc_pmf(k: int, n: int, p: float, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """PMF của phân phối nhị thức B(n, p)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def nhi_thuc_cdf(k: int, n: int, p: float, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """CDF của phân phối nhị thức B(n, p)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def sieu_boi_pmf(k: int, N: int, K: int, n: int, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """PMF của phân phối siêu bội."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def poisson_pmf(k: int, lam: float, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """PMF của phân phối Poisson(λ)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def poisson_cdf(k: int, lam: float, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """CDF của phân phối Poisson(λ)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def chuan_pdf(x: float, mu: float = 0.0, sigma: float = 1.0, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """PDF của phân phối chuẩn N(μ, σ²)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def chuan_cdf(x: float, mu: float = 0.0, sigma: float = 1.0, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """CDF của phân phối chuẩn N(μ, σ²) dùng `math.erf`."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def deu_pdf(x: float, a: float = 0.0, b: float = 1.0, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """PDF của phân phối đều U(a, b)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def deu_cdf(x: float, a: float = 0.0, b: float = 1.0, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """CDF của phân phối đều U(a, b)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def mu_pdf(x: float, lam: float = 1.0, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """PDF của phân phối mũ Exp(λ)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def mu_cdf(x: float, lam: float = 1.0, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """CDF của phân phối mũ Exp(λ)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def sinh_mau_deu(
    a: float,
    b: float,
    n: int,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Sinh n mẫu U(a, b) bằng biến đổi ngược từ U(0, 1)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def sinh_mau_mu(
    lam: float,
    n: int,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Sinh n mẫu Exp(λ) bằng biến đổi ngược từ U(0, 1)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")


def sinh_mau_chuan_nhieu_chieu(
    mu: Any,
    Lambda: Any,
    n: int,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Sinh n mẫu N(μ, Λ) dùng X = μ + L·z với L từ Cholesky (Ch2)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")
