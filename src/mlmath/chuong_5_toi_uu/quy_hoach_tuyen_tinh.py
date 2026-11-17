"""Quy hoạch tuyến tính (QHTT), bài toán cắt vật liệu và bài toán vận tải (D06)."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Sequence

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan
from ..tien_ich.xuat_ket_qua import KetQuaKiemChung


@dataclass
class MoHinhQHTT:
    """Mô hình bài toán Quy hoạch tuyến tính."""

    c: np.ndarray
    A_ub: np.ndarray | None = None
    b_ub: np.ndarray | None = None
    A_eq: np.ndarray | None = None
    b_eq: np.ndarray | None = None
    can: Sequence[tuple[float | None, float | None]] | None = None
    ten_bien: list[str] | None = None
    mo_ta: str = ""


@dataclass
class KetQuaQHTT:
    """Kết quả giải bài toán Quy hoạch tuyến tính."""

    x: np.ndarray | None
    gia_tri_muc_tieu: float | None
    thanh_cong: bool
    trang_thai: str


def dua_ve_dang_chuan(mo_hinh: MoHinhQHTT, nhat_ky: NhatKyTinhToan | None = None) -> MoHinhQHTT:
    """Đưa mô hình QHTT về dạng chuẩn Ax = b, x ≥ 0 bằng biến bù."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def giai_qhtt(
    mo_hinh: MoHinhQHTT,
    phuong_phap: str = "linprog",
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaQHTT:
    """Giải bài toán QHTT bằng `scipy.optimize.linprog` (D06)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def kiem_tra_nghiem_chap_nhan(
    mo_hinh: MoHinhQHTT,
    x: Any,
    dung_sai: float = 1e-7,
    nhat_ky: NhatKyTinhToan | None = None,
) -> KetQuaKiemChung:
    """Kiểm tra nghiệm x có thỏa mãn mọi ràng buộc của mô hình QHTT không."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def liet_ke_cach_cat(
    L: float,
    cac_do_dai: Sequence[float],
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Liệt kê tất cả các cách cắt một thanh dài L thành các đoạn trong `cac_do_dai`."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def mo_hinh_cat_vat_lieu(
    L: float,
    cac_do_dai: Sequence[float],
    so_luong: Sequence[int],
    nhat_ky: NhatKyTinhToan | None = None,
) -> MoHinhQHTT:
    """Xây dựng mô hình QHTT cho bài toán cắt vật liệu (chú ý biến nguyên theo D06)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")


def mo_hinh_van_tai(
    cung: Sequence[float],
    cau: Sequence[float],
    cuoc_phi: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> MoHinhQHTT:
    """Xây dựng mô hình bài toán vận tải (tự thêm trạm phát/thu giả nếu không cân bằng)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §5.")
