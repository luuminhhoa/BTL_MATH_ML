"""Menu tương tác trên Terminal gọi `dich_vu.liet_ke` và `dich_vu.chay`."""

from __future__ import annotations

from ..dich_vu import chay, liet_ke
from ..tien_ich.xuat_ket_qua import hien_thi_terminal


def chay_menu(chuong_mac_dinh: int | None = None) -> None:
    """Chạy vòng lặp menu tương tác trên Terminal."""
    from .cli import phan_tich_du_lieu

    while True:
        ds = liet_ke(chuong=chuong_mac_dinh)
        print("\n=== MENU THUẬT TOÁN MLMATH ===")
        if not ds:
            print("(Chưa có thuật toán nào được đăng ký trong DANG_KY.)")
            print("0. Thoát")
        else:
            for idx, muc in enumerate(ds, start=1):
                print(f"{idx}. [Ch{muc.chuong}] {muc.ten_hien_thi} ({muc.ma})")
            print("0. Thoát")

        lua_chon = input("Chọn số thứ tự: ").strip()
        if lua_chon == "0":
            break
        if not lua_chon.isdigit() or not (1 <= int(lua_chon) <= len(ds)):
            print("Lựa chọn không hợp lệ.")
            continue

        muc = ds[int(lua_chon) - 1]
        tham_so = {}
        for ts in muc.tham_so:
            nhap = input(f"Nhập {ts.ten} ({ts.kieu} - {ts.mo_ta}): ").strip()
            if not nhap and ts.mac_dinh is not None:
                tham_so[ts.ten] = ts.mac_dinh
            elif ts.kieu in {"ma_tran", "vec_to", "so"}:
                tham_so[ts.ten] = phan_tich_du_lieu(nhap)
            else:
                tham_so[ts.ten] = nhap

        try:
            kq = chay(muc.ma, **tham_so)
            hien_thi_terminal(kq)
        except Exception as exc:
            print(f"Lỗi khi thực thi: {exc}")
