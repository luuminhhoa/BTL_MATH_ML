"""Kiểm tra và chuẩn hóa dữ liệu đầu vào (ma trận, vector)."""

from __future__ import annotations

from fractions import Fraction
from typing import Any

import numpy as np

from ..loi import LoiDuLieu, LoiKichThuoc


def _chuan_hoa_kieu_mang(arr: np.ndarray, ten: str) -> np.ndarray:
    """Kiểm tra dtype hợp lệ (float64, complex128, hoặc object-Fraction) và giá trị hữu hạn."""
    if arr.size == 0:
        raise LoiDuLieu(f"Dữ liệu '{ten}' không được rỗng.")

    if arr.dtype == object:
        # Kiểm tra từng phần tử là Fraction hoặc số hữu tỉ/nguyên
        ket_qua = np.empty(arr.shape, dtype=object)
        for idx, val in np.ndenumerate(arr):
            if isinstance(val, Fraction):
                ket_qua[idx] = val
            elif isinstance(val, (int, np.integer)):
                ket_qua[idx] = Fraction(int(val))
            else:
                raise LoiDuLieu(
                    f"Mảng object '{ten}' chứa phần tử không phải Fraction/int: {val!r}."
                )
        return ket_qua

    if np.issubdtype(arr.dtype, np.complexfloating):
        kq = np.array(arr, dtype=np.complex128, copy=True)
        if not np.all(np.isfinite(kq)):
            raise LoiDuLieu(f"Dữ liệu '{ten}' chứa giá trị NaN hoặc Inf.")
        return kq

    if np.issubdtype(arr.dtype, np.number) or np.issubdtype(arr.dtype, np.bool_):
        if np.issubdtype(arr.dtype, np.bool_):
            raise LoiDuLieu(f"Dữ liệu '{ten}' không hỗ trợ kiểu bool.")
        kq = np.array(arr, dtype=np.float64, copy=True)
        if not np.all(np.isfinite(kq)):
            raise LoiDuLieu(f"Dữ liệu '{ten}' chứa giá trị NaN hoặc Inf.")
        return kq

    raise LoiDuLieu(f"Kiểu dữ liệu của '{ten}' không được hỗ trợ: {arr.dtype}.")


def xac_thuc_ma_tran(A: Any, ten: str = "A") -> np.ndarray:
    """Chấp nhận danh sách lồng nhau hoặc ndarray; trả bản sao ndarray 2 chiều hợp lệ."""
    try:
        arr = np.asarray(A)
    except Exception as exc:
        raise LoiDuLieu(f"Không thể chuyển '{ten}' thành ma trận: {exc}") from exc

    if arr.ndim != 2:
        raise LoiKichThuoc(
            f"'{ten}' phải là ma trận 2 chiều, nhận được {arr.ndim} chiều (shape={arr.shape})."
        )
    return _chuan_hoa_kieu_mang(arr, ten=ten)


def xac_thuc_vec_to(x: Any, ten: str = "x") -> np.ndarray:
    """Chấp nhận danh sách hoặc ndarray; trả bản sao ndarray 1 chiều hợp lệ."""
    try:
        arr = np.asarray(x)
    except Exception as exc:
        raise LoiDuLieu(f"Không thể chuyển '{ten}' thành vector: {exc}") from exc

    if arr.ndim != 1:
        raise LoiKichThuoc(
            f"'{ten}' phải là vector 1 chiều, nhận được {arr.ndim} chiều (shape={arr.shape})."
        )
    return _chuan_hoa_kieu_mang(arr, ten=ten)


def xac_thuc_vuong(A: Any, ten: str = "A") -> np.ndarray:
    """Kiểm tra ma trận hợp lệ và vuông (n × n)."""
    mat = xac_thuc_ma_tran(A, ten=ten)
    m, n = mat.shape
    if m != n:
        raise LoiKichThuoc(
            f"Ma trận '{ten}' phải vuông, nhận được kích thước {m}×{n}."
        )
    return mat


def xac_thuc_nhan_duoc(A: np.ndarray, B: np.ndarray) -> None:
    """Kiểm tra số cột của A bằng số hàng của B để nhân A·B."""
    if A.ndim != 2 or B.ndim != 2:
        raise LoiKichThuoc("Cả hai toán hạng phải là ma trận 2 chiều.")
    if A.shape[1] != B.shape[0]:
        raise LoiKichThuoc(
            f"Không thể nhân ma trận kích thước {A.shape} với {B.shape}: "
            f"số cột A ({A.shape[1]}) != số hàng B ({B.shape[0]})."
        )
