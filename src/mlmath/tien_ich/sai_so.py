"""Tính sai số tuyệt đối, sai số tương đối và so sánh gần bằng (không dùng np.linalg.norm)."""

from __future__ import annotations

import math
from typing import Any

import numpy as np


def _chuan_frobenius_noi_bo(x: Any) -> float:
    """Tính chuẩn Euclid / Frobenius tự cài cho vô hướng, vector hoặc ma trận."""
    arr = np.asarray(x)
    if arr.ndim == 0:
        return abs(complex(arr.item()))
    tong = 0.0
    for val in arr.flat:
        tong += abs(complex(val)) ** 2
    return math.sqrt(tong)


def sai_so_tuyet_doi(a: Any, b: Any) -> float:
    """Tính ‖a - b‖₂ (hoặc |a - b| nếu là vô hướng)."""
    arr_a = np.asarray(a)
    arr_b = np.asarray(b)
    if arr_a.shape != arr_b.shape:
        raise ValueError(f"Kích thước không khớp: {arr_a.shape} != {arr_b.shape}")
    return _chuan_frobenius_noi_bo(arr_a - arr_b)


def sai_so_tuong_doi(a: Any, b: Any, eps: float = 1e-300) -> float:
    """Tính ‖a - b‖ / max(‖a‖, ‖b‖, eps)."""
    tuyet_doi = sai_so_tuyet_doi(a, b)
    mau = max(_chuan_frobenius_noi_bo(a), _chuan_frobenius_noi_bo(b), eps)
    return tuyet_doi / mau


def gan_bang(a: Any, b: Any, rtol: float = 1e-9, atol: float = 1e-10) -> bool:
    """Kiểm tra |a - b| <= atol + rtol * |b| trên toàn bộ phần tử."""
    arr_a = np.asarray(a, dtype=np.complex128 if np.iscomplexobj(a) or np.iscomplexobj(b) else np.float64)
    arr_b = np.asarray(b, dtype=arr_a.dtype)
    if arr_a.shape != arr_b.shape:
        return False
    return bool(np.all(np.abs(arr_a - arr_b) <= atol + rtol * np.abs(arr_b)))
