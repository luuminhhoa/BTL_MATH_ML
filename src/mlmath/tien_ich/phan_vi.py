"""Bảng tra phân vị chuẩn, Student và Chi-bình phương bọc từ `scipy.stats` (D07)."""

from __future__ import annotations

from ..loi import LoiDieuKien


def _kiem_tra_xac_suat(p: float) -> None:
    if not (0.0 < p < 1.0):
        raise LoiDieuKien(f"Xác suất tích lũy p phải nằm trong (0, 1), nhận được {p}.")


def phan_vi_chuan(p: float) -> float:
    """Phân vị mức p (tích lũy dưới) của phân phối chuẩn tắc N(0, 1)."""
    _kiem_tra_xac_suat(p)
    from scipy.stats import norm

    return float(norm.ppf(p))


def phan_vi_student(p: float, bac_tu_do: int) -> float:
    """Phân vị mức p của phân phối Student t(bac_tu_do)."""
    _kiem_tra_xac_suat(p)
    if bac_tu_do < 1:
        raise LoiDieuKien(f"Bậc tự do phải >= 1, nhận được {bac_tu_do}.")
    from scipy.stats import t

    return float(t.ppf(p, df=bac_tu_do))


def phan_vi_khi_binh_phuong(p: float, bac_tu_do: int) -> float:
    """Phân vị mức p của phân phối Chi-bình phương χ²(bac_tu_do)."""
    _kiem_tra_xac_suat(p)
    if bac_tu_do < 1:
        raise LoiDieuKien(f"Bậc tự do phải >= 1, nhận được {bac_tu_do}.")
    from scipy.stats import chi2

    return float(chi2.ppf(p, df=bac_tu_do))
