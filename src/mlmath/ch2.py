"""Alias tiếng Anh cho Chương 2 (chỉ re-export)."""

from __future__ import annotations

from .chuong_2_khong_gian_vector.anh_xa_tuyen_tinh import (
    co_so_khong_gian_anh as image_basis,
    co_so_khong_gian_nhan as null_space_basis,
)
from .chuong_2_khong_gian_vector.doc_lap_tuyen_tinh import (
    la_doc_lap_tuyen_tinh as is_linearly_independent,
)
from .chuong_2_khong_gian_vector.doi_co_so import (
    ma_tran_chuyen_co_so as change_of_basis_matrix,
)
from .chuong_2_khong_gian_vector.gram_schmidt import gram_schmidt
from .chuong_2_khong_gian_vector.tri_rieng import (
    cheo_hoa as diagonalize,
    cheo_hoa_truc_giao as orthogonal_diagonalize,
    tri_rieng as eigenvalues,
)
from .chuong_2_khong_gian_vector.ung_dung_pca import pca
from .chuong_2_khong_gian_vector.vet import vet_ma_tran as trace
from .chuong_2_khong_gian_vector.xac_dinh_duong import phan_ra_cholesky as cholesky

__all__ = [
    "is_linearly_independent",
    "change_of_basis_matrix",
    "gram_schmidt",
    "image_basis",
    "null_space_basis",
    "eigenvalues",
    "diagonalize",
    "orthogonal_diagonalize",
    "cholesky",
    "trace",
    "pca",
]
