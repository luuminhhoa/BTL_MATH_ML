"""Alias tiếng Anh cho Chương 6 (chỉ re-export)."""

from __future__ import annotations

from .chuong_6_uoc_luong.dac_trung_mau import (
    phuong_sai_mau as sample_variance,
    phuong_sai_mau_dieu_chinh as unbiased_sample_variance,
    trung_binh_mau as sample_mean,
)
from .chuong_6_uoc_luong.uoc_luong import (
    map_beta_bernoulli,
    mle_chuan as mle_normal,
    ols_tong_quat as ols,
)

__all__ = [
    "sample_mean",
    "sample_variance",
    "unbiased_sample_variance",
    "ols",
    "mle_normal",
    "map_beta_bernoulli",
]
