"""Khảo sát sai số sai phân số theo bước δ và vẽ đồ thị log–log."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Sequence

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def khao_sat_theo_delta(
    f: Callable[[np.ndarray], float],
    gradient_giai_tich: Callable[[np.ndarray], np.ndarray],
    x: Any,
    cac_delta: Sequence[float],
    nhat_ky: NhatKyTinhToan | None = None,
) -> dict[str, Any]:
    """So sánh sai số của sai phân tiến o(δ) và trung tâm o(δ²) theo các mức δ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")


def ve_sai_so_theo_delta(
    ket_qua: dict[str, Any],
    duong_dan: str | Path,
    nhat_ky: NhatKyTinhToan | None = None,
) -> Path:
    """Vẽ đồ thị log–log sai số theo δ và lưu ra `duong_dan`."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §3.")
