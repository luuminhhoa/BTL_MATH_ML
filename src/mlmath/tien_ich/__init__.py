"""Các tiện ích dùng chung cho toàn bộ thư viện `mlmath`."""

from __future__ import annotations

from .da_thuc import DaThuc, tim_nghiem
from .dinh_dang_ma_tran import dinh_dang_ma_tran, dinh_dang_so
from .kiem_tra_du_lieu import (
    xac_thuc_ma_tran,
    xac_thuc_nhan_duoc,
    xac_thuc_vec_to,
    xac_thuc_vuong,
)
from .nhat_ky_tinh_toan import BuocTinhToan, NhatKyTinhToan
from .phan_vi import phan_vi_chuan, phan_vi_khi_binh_phuong, phan_vi_student
from .sai_so import gan_bang, sai_so_tuong_doi, sai_so_tuyet_doi
from .xuat_ket_qua import (
    KetQuaKiemChung,
    KetQuaTinhToan,
    ghi_json,
    ghi_txt,
    hien_thi_terminal,
)

__all__ = [
    "BuocTinhToan",
    "NhatKyTinhToan",
    "KetQuaKiemChung",
    "KetQuaTinhToan",
    "hien_thi_terminal",
    "ghi_txt",
    "ghi_json",
    "dinh_dang_so",
    "dinh_dang_ma_tran",
    "xac_thuc_ma_tran",
    "xac_thuc_vec_to",
    "xac_thuc_vuong",
    "xac_thuc_nhan_duoc",
    "sai_so_tuyet_doi",
    "sai_so_tuong_doi",
    "gan_bang",
    "DaThuc",
    "tim_nghiem",
    "phan_vi_chuan",
    "phan_vi_student",
    "phan_vi_khi_binh_phuong",
]
