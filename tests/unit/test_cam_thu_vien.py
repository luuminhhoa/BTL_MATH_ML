"""Kiểm thử tĩnh (AST) bảo vệ ranh giới thư viện cấm trong `src/mlmath/` (Quyết định D03)."""

from __future__ import annotations

import ast
from pathlib import Path

SRC_MLMATH = Path(__file__).resolve().parents[2] / "src" / "mlmath"

GOI_CAM_CHUNG = {
    ("np", "linalg"),
    ("numpy", "linalg"),
    ("scipy", "linalg"),
    ("np", "roots"),
    ("numpy", "roots"),
}

MODULE_CAM_IMPORT = {
    "numpy.linalg",
    "scipy.linalg",
    "sklearn",
}

GOI_CAM_CH1 = {
    ("np", "dot"),
    ("numpy", "dot"),
    ("np", "matmul"),
    ("numpy", "matmul"),
}


def _lay_chuoi_thuoc_tinh(node: ast.AST) -> list[str]:
    if isinstance(node, ast.Name):
        return [node.id]
    if isinstance(node, ast.Attribute):
        return _lay_chuoi_thuoc_tinh(node.value) + [node.attr]
    return []


def _quet_file(path: Path) -> list[str]:
    vi_pham: list[str] = []
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    la_chuong_1 = "chuong_1_ma_tran" in path.parts

    for node in ast.walk(tree):
        # Kiểm tra import bị cấm
        if isinstance(node, ast.Import):
            for alias in node.names:
                for cam in MODULE_CAM_IMPORT:
                    if alias.name == cam or alias.name.startswith(cam + "."):
                        vi_pham.append(f"{path.name}:{node.lineno}: cấm import '{alias.name}'")
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            for cam in MODULE_CAM_IMPORT:
                if mod == cam or mod.startswith(cam + "."):
                    vi_pham.append(f"{path.name}:{node.lineno}: cấm from '{mod}' import ...")

        # Kiểm tra thuộc tính / lời gọi bị cấm (vd np.linalg.inv, np.roots)
        if isinstance(node, ast.Attribute):
            chuoi = _lay_chuoi_thuoc_tinh(node)
            if len(chuoi) >= 2 and (chuoi[0], chuoi[1]) in GOI_CAM_CHUNG:
                vi_pham.append(f"{path.name}:{node.lineno}: cấm dùng '{'.'.join(chuoi)}'")
            if la_chuong_1 and len(chuoi) >= 2 and (chuoi[0], chuoi[1]) in GOI_CAM_CH1:
                vi_pham.append(f"{path.name}:{node.lineno}: Ch1 cấm dùng '{'.'.join(chuoi)}'")

        # Chương 1 cấm toán tử @ (MatMult)
        if la_chuong_1:
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.MatMult):
                vi_pham.append(f"{path.name}:{node.lineno}: Ch1 cấm dùng toán tử '@'")
            if isinstance(node, ast.AugAssign) and isinstance(node.op, ast.MatMult):
                vi_pham.append(f"{path.name}:{node.lineno}: Ch1 cấm dùng toán tử '@='")

    return vi_pham


def test_khong_dung_thu_vien_cam_trong_mlmath() -> None:
    """Quét AST toàn bộ `src/mlmath/` đảm bảo tuân thủ quyết định D03."""
    assert SRC_MLMATH.exists(), f"Không tìm thấy thư mục {SRC_MLMATH}"
    tat_ca_vi_pham: list[str] = []
    for py_file in sorted(SRC_MLMATH.rglob("*.py")):
        tat_ca_vi_pham.extend(_quet_file(py_file))
    assert not tat_ca_vi_pham, "Phát hiện vi phạm ranh giới thư viện (D03):\n" + "\n".join(tat_ca_vi_pham)
