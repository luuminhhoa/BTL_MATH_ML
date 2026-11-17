"""Đóng gói và xuất kết quả tính toán ra Terminal, TXT và JSON."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from fractions import Fraction
import json
from pathlib import Path
from typing import Any

import numpy as np

from .da_thuc import DaThuc
from .dinh_dang_ma_tran import dinh_dang_ma_tran, dinh_dang_so
from .nhat_ky_tinh_toan import BuocTinhToan


@dataclass
class KetQuaKiemChung:
    """Kết quả của một phép kiểm chứng tính đúng đắn."""

    ten: str
    dat: bool
    sai_so: float | None
    mo_ta: str


@dataclass
class KetQuaTinhToan:
    """Cấu trúc thống nhất trả về từ tầng dịch vụ để xuất ra mọi định dạng."""

    ten_thuat_toan: str
    dau_vao: dict[str, Any]
    ket_qua: Any
    cac_buoc: list[BuocTinhToan] = field(default_factory=list)
    kiem_chung: list[KetQuaKiemChung] = field(default_factory=list)
    thoi_gian_giay: float = 0.0
    ghi_chu: str = ""


def _dinh_dang_gia_tri(val: Any) -> str:
    if isinstance(val, np.ndarray):
        return dinh_dang_ma_tran(val)
    if isinstance(val, (int, float, complex, Fraction, np.number)):
        return dinh_dang_so(val)
    if isinstance(val, dict):
        return "\n".join(f"  {k}: {_dinh_dang_gia_tri(v)}" for k, v in val.items())
    return str(val)


def _tao_noi_dung_van_ban(kq: KetQuaTinhToan, chi_tiet: bool = True) -> str:
    dong = [
        f"=== {kq.ten_thuat_toan} ===",
        f"Thời gian chạy: {kq.thoi_gian_giay:.6f} s",
    ]
    if kq.ghi_chu:
        dong.append(f"Ghi chú: {kq.ghi_chu}")

    if chi_tiet and kq.cac_buoc:
        dong.append("\n--- Quá trình tính toán ---")
        for idx, b in enumerate(kq.cac_buoc, start=1):
            dong.append(f"[{idx}] {b.ten_buoc}")
            if b.cong_thuc:
                dong.append(f"    Công thức: {b.cong_thuc}")
            if b.trang_thai is not None:
                dong.append("    Trạng thái:")
                for line in _dinh_dang_gia_tri(b.trang_thai).splitlines():
                    dong.append(f"      {line}")
            if b.ket_qua is not None:
                dong.append("    Kết quả bước:")
                for line in _dinh_dang_gia_tri(b.ket_qua).splitlines():
                    dong.append(f"      {line}")

    dong.append("\n--- Kết quả cuối cùng ---")
    dong.append(_dinh_dang_gia_tri(kq.ket_qua))

    if kq.kiem_chung:
        dong.append("\n--- Kiểm chứng ---")
        for kc in kq.kiem_chung:
            trang_thai = "ĐẠT" if kc.dat else "KHÔNG ĐẠT"
            ss = f" (sai số={kc.sai_so:.3e})" if kc.sai_so is not None else ""
            dong.append(f"- {kc.ten}: {trang_thai}{ss} — {kc.mo_ta}")

    return "\n".join(dong)


def hien_thi_terminal(kq: KetQuaTinhToan, chi_tiet: bool = True) -> None:
    """Hiển thị kết quả và các bước tính toán ra Terminal."""
    print(_tao_noi_dung_van_ban(kq, chi_tiet=chi_tiet))


def _ten_file_mac_dinh(ten_thuat_toan: str, duoi: str) -> str:
    ten_sach = ten_thuat_toan.replace(".", "_").replace(" ", "_")
    moc = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{ten_sach}_{moc}.{duoi}"


def ghi_txt(kq: KetQuaTinhToan, thu_muc: str | Path, chi_tiet: bool = True) -> Path:
    """Ghi kết quả ra file TXT cùng nội dung với Terminal."""
    dir_path = Path(thu_muc)
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / _ten_file_mac_dinh(kq.ten_thuat_toan, "txt")
    file_path.write_text(_tao_noi_dung_van_ban(kq, chi_tiet=chi_tiet), encoding="utf-8")
    return file_path


def _tuan_tu_hoa(obj: Any) -> Any:
    """Chuyển đổi các đối tượng toán học sang kiểu JSON hợp lệ theo hợp đồng §0.3."""
    if isinstance(obj, np.ndarray):
        return [_tuan_tu_hoa(x) for x in obj.tolist()]
    if isinstance(obj, np.generic):
        return _tuan_tu_hoa(obj.item())
    if isinstance(obj, Fraction):
        return f"{obj.numerator}/{obj.denominator}"
    if isinstance(obj, complex):
        return {"re": obj.real, "im": obj.imag}
    if isinstance(obj, DaThuc):
        return {"he_so": [_tuan_tu_hoa(c) for c in obj.he_so]}
    if isinstance(obj, dict):
        return {str(k): _tuan_tu_hoa(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_tuan_tu_hoa(x) for x in obj]
    if isinstance(obj, BuocTinhToan):
        return {
            "ten_thuat_toan": obj.ten_thuat_toan,
            "ten_buoc": obj.ten_buoc,
            "cong_thuc": obj.cong_thuc,
            "trang_thai": _tuan_tu_hoa(obj.trang_thai),
            "ket_qua": _tuan_tu_hoa(obj.ket_qua),
            "kiem_chung": obj.kiem_chung,
        }
    if isinstance(obj, KetQuaKiemChung):
        return {
            "ten": obj.ten,
            "dat": obj.dat,
            "sai_so": obj.sai_so,
            "mo_ta": obj.mo_ta,
        }
    return obj


def ghi_json(kq: KetQuaTinhToan, thu_muc: str | Path) -> Path:
    """Ghi kết quả ra file JSON theo quy tắc tuần tự hóa trong hợp đồng §0.3."""
    dir_path = Path(thu_muc)
    dir_path.mkdir(parents=True, exist_ok=True)
    file_path = dir_path / _ten_file_mac_dinh(kq.ten_thuat_toan, "json")
    payload = {
        "ten_thuat_toan": kq.ten_thuat_toan,
        "dau_vao": _tuan_tu_hoa(kq.dau_vao),
        "ket_qua": _tuan_tu_hoa(kq.ket_qua),
        "cac_buoc": [_tuan_tu_hoa(b) for b in kq.cac_buoc],
        "kiem_chung": [_tuan_tu_hoa(kc) for kc in kq.kiem_chung],
        "thoi_gian_giay": kq.thoi_gian_giay,
        "ghi_chu": kq.ghi_chu,
    }
    file_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return file_path
