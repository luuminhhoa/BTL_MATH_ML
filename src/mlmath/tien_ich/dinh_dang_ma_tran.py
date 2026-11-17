"""Định dạng số và ma trận để hiển thị rõ ràng trên Terminal và file TXT."""

from __future__ import annotations

from fractions import Fraction
from typing import Any

import numpy as np


def dinh_dang_so(
    x: Any,
    che_do: str = "tu_dong",
    so_chu_so: int = 6,
) -> str:
    """Định dạng một số thực, phức, nguyên hoặc Fraction thành chuỗi.

    Không bao giờ tự động đổi số thực (float) sang phân số.
    """
    if che_do not in {"tu_dong", "phan_so", "thap_phan"}:
        raise ValueError(f"Chế độ định dạng không hợp lệ: {che_do!r}")

    if isinstance(x, Fraction):
        if che_do == "thap_phan":
            return f"{float(x):.{so_chu_so}g}"
        return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else f"{x.numerator}"

    if isinstance(x, (int, np.integer)):
        return str(int(x))

    if isinstance(x, (complex, np.complexfloating)):
        re = float(x.real)
        im = float(x.imag)
        if abs(im) < 1e-12:
            return f"{0.0 if abs(re) < 1e-12 else re:.{so_chu_so}g}"
        dau = "+" if im >= 0 else "-"
        return f"{re:.{so_chu_so}g}{dau}{abs(im):.{so_chu_so}g}i"

    if isinstance(x, (float, np.floating)):
        val = 0.0 if abs(float(x)) < 1e-12 else float(x)
        return f"{val:.{so_chu_so}g}"

    return str(x)


def dinh_dang_ma_tran(
    A: np.ndarray,
    che_do: str = "tu_dong",
    so_chu_so: int = 6,
) -> str:
    """Định dạng ma trận 2 chiều (hoặc vector 1 chiều) căn chỉnh theo cột."""
    arr = np.asarray(A)
    if arr.ndim == 1:
        phan_tu = [dinh_dang_so(v, che_do=che_do, so_chu_so=so_chu_so) for v in arr]
        return "[ " + "  ".join(phan_tu) + " ]"
    if arr.ndim != 2:
        return str(arr)

    m, n = arr.shape
    bang = [
        [dinh_dang_so(arr[i, j], che_do=che_do, so_chu_so=so_chu_so) for j in range(n)]
        for i in range(m)
    ]
    do_rong = [
        max((len(bang[i][j]) for i in range(m)), default=1) for j in range(n)
    ]
    cac_dong = []
    for i in range(m):
        hang_str = "  ".join(bang[i][j].rjust(do_rong[j]) for j in range(n))
        cac_dong.append(f"[ {hang_str} ]")
    return "\n".join(cac_dong)
