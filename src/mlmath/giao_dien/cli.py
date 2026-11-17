"""Giao diện dòng lệnh (CLI) cho `mlmath`."""

from __future__ import annotations

import argparse
import ast
from fractions import Fraction
from pathlib import Path
from typing import Any

import numpy as np

from ..dich_vu import DANG_KY, chay, liet_ke
from ..tien_ich.xuat_ket_qua import ghi_json, ghi_txt, hien_thi_terminal
from .menu import chay_menu

_THU_MUC_CHUONG = {
    1: "ch1_linear_algebra",
    2: "ch2_vector_spaces",
    3: "ch3_matrix_calculus",
    4: "ch4_probability",
    5: "ch5_optimization",
    6: "ch6_estimation",
}


def _chuyen_phan_tu_phan_so(obj: Any) -> Any:
    if isinstance(obj, list):
        return [_chuyen_phan_tu_phan_so(x) for x in obj]
    if isinstance(obj, str) and "/" in obj:
        return Fraction(obj.strip())
    return obj


def phan_tich_du_lieu(chuoi: str) -> Any:
    """Phân tích chuỗi đầu vào an toàn bằng `ast.literal_eval` (không dùng `eval`)."""
    gia_tri = ast.literal_eval(chuoi)
    chuyen = _chuyen_phan_tu_phan_so(gia_tri)
    if isinstance(chuyen, list):
        # Kiểm tra nếu chứa Fraction thì giữ dtype=object
        def _co_phan_so(x: Any) -> bool:
            if isinstance(x, Fraction):
                return True
            if isinstance(x, list):
                return any(_co_phan_so(e) for e in x)
            return False

        if _co_phan_so(chuyen):
            return np.array(chuyen, dtype=object)
        return np.array(chuyen)
    return chuyen


def _xuat_ket_qua(kq: Any, chuong: int, che_do_xuat: list[str]) -> None:
    thu_muc_out = Path("chapters") / _THU_MUC_CHUONG.get(chuong, "outputs") / "outputs"
    if "terminal" in che_do_xuat:
        hien_thi_terminal(kq)
    if "txt" in che_do_xuat:
        p = ghi_txt(kq, thu_muc_out)
        print(f"Đã ghi TXT: {p}")
    if "json" in che_do_xuat:
        p = ghi_json(kq, thu_muc_out)
        print(f"Đã ghi JSON: {p}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python -m mlmath.giao_dien",
        description="Giao diện dòng lệnh và menu tương tác cho thư viện mlmath",
    )
    sub = parser.add_subparsers(dest="lenh")

    sub.add_parser("menu", help="Mở menu tương tác")

    p_lk = sub.add_parser("liet-ke", help="Liệt kê các thuật toán đã đăng ký")
    p_lk.add_argument("--chuong", type=int, default=None, help="Lọc theo chương (1..6)")

    p_chay = sub.add_parser("chay", help="Chạy một thuật toán theo mã")
    p_chay.add_argument("ma", help="Mã thuật toán, ví dụ: ch1.nghich_dao_gauss_jordan")
    p_chay.add_argument("--ma-tran", dest="ma_tran", default=None, help="Ma trận A dạng JSON/Python literal")
    p_chay.add_argument("--ma-tran-b", dest="ma_tran_b", default=None, help="Ma trận B (nếu có)")
    p_chay.add_argument("--vec-to", dest="vec_to", default=None, help="Vector x hoặc b")
    p_chay.add_argument("--xuat", default="terminal", help="Các định dạng xuất: terminal,txt,json")

    args = parser.parse_args(argv)

    if args.lenh in (None, "menu"):
        chay_menu()
        return 0

    if args.lenh == "liet-ke":
        ds = liet_ke(chuong=args.chuong)
        if not ds:
            print("Chưa có thuật toán nào được đăng ký.")
            return 0
        for muc in ds:
            print(f"[Ch{muc.chuong}] {muc.ma:35s} — {muc.ten_hien_thi}")
        return 0

    if args.lenh == "chay":
        if args.ma not in DANG_KY:
            print(f"Lỗi: không tìm thấy mã thuật toán {args.ma!r}.")
            return 1
        tham_so: dict[str, Any] = {}
        if args.ma_tran is not None:
            tham_so["A"] = phan_tich_du_lieu(args.ma_tran)
        if args.ma_tran_b is not None:
            tham_so["B"] = phan_tich_du_lieu(args.ma_tran_b)
        if args.vec_to is not None:
            tham_so["b"] = phan_tich_du_lieu(args.vec_to)

        kq = chay(args.ma, **tham_so)
        che_do = [x.strip() for x in args.xuat.split(",") if x.strip()]
        _xuat_ket_qua(kq, DANG_KY[args.ma].chuong, che_do)
        return 0

    return 0
