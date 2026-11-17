"""Ghi nhật ký các bước tính toán trung gian của thuật toán."""

from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class BuocTinhToan:
    """Một bước tính toán bất biến được ghi lại trong nhật ký."""

    ten_thuat_toan: str
    ten_buoc: str
    cong_thuc: str
    trang_thai: Any
    ket_qua: Any
    kiem_chung: str = ""


class NhatKyTinhToan:
    """Lưu trữ tuần tự các bước tính toán trung gian."""

    def __init__(self, ten_thuat_toan: str = "", _la_rong: bool = False) -> None:
        self.ten_thuat_toan = ten_thuat_toan
        self._la_rong = _la_rong
        self._cac_buoc: list[BuocTinhToan] = []

    @classmethod
    def rong(cls) -> NhatKyTinhToan:
        """Trả về đối tượng nhật ký rỗng (null-object), không ghi gì."""
        return cls(ten_thuat_toan="", _la_rong=True)

    @property
    def cac_buoc(self) -> list[BuocTinhToan]:
        """Danh sách các bước đã ghi."""
        return list(self._cac_buoc)

    def ghi_buoc(
        self,
        ten_buoc: str,
        cong_thuc: str = "",
        trang_thai: Any = None,
        ket_qua: Any = None,
        kiem_chung: str = "",
        ten_thuat_toan: str | None = None,
    ) -> None:
        """Ghi một bước mới vào nhật ký; sao chép dữ liệu để tránh bị sửa về sau."""
        if self._la_rong:
            return
        buoc = BuocTinhToan(
            ten_thuat_toan=ten_thuat_toan or self.ten_thuat_toan,
            ten_buoc=ten_buoc,
            cong_thuc=cong_thuc,
            trang_thai=copy.deepcopy(trang_thai),
            ket_qua=copy.deepcopy(ket_qua),
            kiem_chung=kiem_chung,
        )
        self._cac_buoc.append(buoc)
