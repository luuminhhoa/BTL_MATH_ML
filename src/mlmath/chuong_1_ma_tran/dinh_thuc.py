"""Tính định thức bằng khai triển Laplace và khử Gauss."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def dinh_thuc_laplace(
    A: Any,
    hang: int = 0,
    nhat_ky: NhatKyTinhToan | None = None,
) -> Any:
    """Tính det(A) bằng khai triển Laplace đệ quy theo hàng `hang`, O(n!)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def dinh_thuc_gauss(
    A: Any,
    chon_pivot: bool = True,
    nhat_ky: NhatKyTinhToan | None = None,
) -> Any:
    """Tính det(A) bằng đưa về dạng tam giác trên (O(n³)), theo dõi dấu khi đổi hàng."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")


def do_thoi_gian_dinh_thuc(
    cac_n: list[int],
    so_lan: int = 3,
    n_toi_da_laplace: int = 9,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> list[dict[str, Any]]:
    """Đo và so sánh thời gian chạy giữa Laplace và Gauss cho danh sách kích thước `cac_n`."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §1.")
