"""Thực thi thuật toán qua bảng đăng ký, ghi nhật ký, đo thời gian và kiểm chứng."""

from __future__ import annotations

import inspect
import time
from typing import Any

from ..loi import LoiDuLieu
from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan
from ..tien_ich.xuat_ket_qua import KetQuaKiemChung, KetQuaTinhToan
from .dang_ky import DANG_KY


def chay(ma: str, **tham_so: Any) -> KetQuaTinhToan:
    """Chạy thuật toán có mã `ma` với các tham số `tham_so`.

    Không in ra màn hình và không ghi file (D14).
    """
    if ma not in DANG_KY:
        raise LoiDuLieu(f"Không tìm thấy thuật toán có mã {ma!r} trong DANG_KY.")

    muc = DANG_KY[ma]
    nhat_ky = NhatKyTinhToan(ten_thuat_toan=muc.ten_hien_thi)

    # Điền giá trị mặc định cho tham số chưa truyền
    tham_so_day_du: dict[str, Any] = {}
    for ts in muc.tham_so:
        if ts.ten in tham_so:
            tham_so_day_du[ts.ten] = tham_so[ts.ten]
        elif ts.mac_dinh is not None:
            tham_so_day_du[ts.ten] = ts.mac_dinh

    # Truyền thêm các tham số phụ hợp lệ nếu có
    for k, v in tham_so.items():
        if k not in tham_so_day_du:
            tham_so_day_du[k] = v

    sig = inspect.signature(muc.ham)
    goi_tham_so = dict(tham_so_day_du)
    if "nhat_ky" in sig.parameters:
        goi_tham_so["nhat_ky"] = nhat_ky

    bat_dau = time.perf_counter()
    ket_qua = muc.ham(**goi_tham_so)
    thoi_gian = time.perf_counter() - bat_dau

    ds_kiem_chung: list[KetQuaKiemChung] = []
    if muc.kiem_chung is not None:
        kc_res = muc.kiem_chung(ket_qua=ket_qua, **tham_so_day_du)
        if isinstance(kc_res, KetQuaKiemChung):
            ds_kiem_chung.append(kc_res)
        elif isinstance(kc_res, list):
            ds_kiem_chung.extend(kc_res)

    return KetQuaTinhToan(
        ten_thuat_toan=muc.ten_hien_thi,
        dau_vao=tham_so_day_du,
        ket_qua=ket_qua,
        cac_buoc=nhat_ky.cac_buoc,
        kiem_chung=ds_kiem_chung,
        thoi_gian_giay=thoi_gian,
    )
