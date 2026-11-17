"""Alias tiếng Anh cho Chương 3 (chỉ re-export)."""

from __future__ import annotations

from .chuong_3_giai_tich_ma_tran.dao_ham_so import (
    gradient_so as numerical_gradient,
    hessian_so as numerical_hessian,
    jacobian_so as numerical_jacobian,
)

__all__ = [
    "numerical_gradient",
    "numerical_jacobian",
    "numerical_hessian",
]
