"""Alias tiếng Anh cho Chương 1 (D02 — chỉ re-export, không chứa logic)."""

from __future__ import annotations

from .chuong_1_ma_tran.dinh_thuc import dinh_thuc_gauss as det_gauss
from .chuong_1_ma_tran.dinh_thuc import dinh_thuc_laplace as det_laplace
from .chuong_1_ma_tran.hang import hang_ma_tran as rank
from .chuong_1_ma_tran.nghich_dao import nghich_dao_gauss_jordan as inverse_gj
from .chuong_1_ma_tran.nghich_dao import nghich_dao_phu_hop as inverse_adj
from .chuong_1_ma_tran.phep_toan import chuyen_vi as transpose
from .chuong_1_ma_tran.phep_toan import chuyen_vi_lien_hop as conj_transpose
from .chuong_1_ma_tran.phep_toan import luy_thua as matpow
from .chuong_1_ma_tran.phep_toan import nhan_ma_tran as matmul

__all__ = [
    "inverse_gj",
    "inverse_adj",
    "det_laplace",
    "det_gauss",
    "rank",
    "matmul",
    "transpose",
    "conj_transpose",
    "matpow",
]
