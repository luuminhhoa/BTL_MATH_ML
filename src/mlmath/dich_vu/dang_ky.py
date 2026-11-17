"""Bảng đăng ký thuật toán tập trung dùng chung cho CLI và Menu."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass(frozen=True)
class ThamSo:
    """Mô tả một tham số đầu vào của thuật toán."""

    ten: str
    kieu: str  # "ma_tran" | "vec_to" | "so" | "chuoi" | "lua_chon"
    mo_ta: str
    mac_dinh: Any = None


@dataclass(frozen=True)
class MucThuatToan:
    """Mục đăng ký một thuật toán trong `DANG_KY`."""

    ma: str
    chuong: int
    ten_hien_thi: str
    ham: Callable[..., Any]
    tham_so: list[ThamSo] = field(default_factory=list)
    kiem_chung: Callable[..., Any] | None = None


DANG_KY: dict[str, MucThuatToan] = {}


def dang_ky_thuat_toan(muc: MucThuatToan) -> None:
    """Thêm một mục thuật toán vào bảng đăng ký toàn cục."""
    DANG_KY[muc.ma] = muc


def liet_ke(chuong: int | None = None) -> list[MucThuatToan]:
    """Trả về danh sách các thuật toán đã đăng ký (lọc theo chương nếu có)."""
    mucs = list(DANG_KY.values())
    if chuong is not None:
        mucs = [m for m in mucs if m.chuong == chuong]
    return sorted(mucs, key=lambda m: (m.chuong, m.ma))
