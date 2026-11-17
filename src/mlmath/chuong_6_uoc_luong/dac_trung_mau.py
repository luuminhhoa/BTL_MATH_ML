"""Đặc trưng mẫu: trung bình, phương sai mẫu (chia n) vs điều chỉnh (chia n−1)."""

from __future__ import annotations

from typing import Any, Callable, Sequence

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


def trung_binh_mau(x: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính trung bình mẫu x̄ = (1/n) Σ xᵢ."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def phuong_sai_mau(x: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính phương sai mẫu S² chia cho n (tương ứng ddof=0)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def phuong_sai_mau_dieu_chinh(x: Any, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính phương sai mẫu điều chỉnh S′² chia cho n − 1 (tương ứng ddof=1)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def do_lech_mau(x: Any, dieu_chinh: bool = True, nhat_ky: NhatKyTinhToan | None = None) -> float:
    """Tính độ lệch chuẩn mẫu (căn bậc hai của S′² hoặc S²)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def tan_suat_mau(
    x: Any,
    tinh_chat: Callable[[Any], bool],
    nhat_ky: NhatKyTinhToan | None = None,
) -> float:
    """Tính tần suất mẫu f = m / n thỏa mãn `tinh_chat`."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def dac_trung_tu_bang_tan_so(
    gia_tri: Any,
    tan_so: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> dict[str, float]:
    """Tính trung bình, phương sai mẫu và điều chỉnh từ bảng tần số."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def dac_trung_tu_bang_khoang(
    cac_khoang: Sequence[tuple[float, float]],
    tan_so: Any,
    nhat_ky: NhatKyTinhToan | None = None,
) -> dict[str, float]:
    """Tính đặc trưng mẫu từ bảng phân bố khoảng (dùng điểm giữa làm trị đại diện)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def vec_to_trung_binh_mau(X: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tính vector trung bình mẫu từ ma trận X shape (n, k) (hàng là quan sát)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def ma_tran_hiep_phuong_sai_mau(X: Any, nhat_ky: NhatKyTinhToan | None = None) -> np.ndarray:
    """Tính ma trận hiệp phương sai mẫu S²(X) = (1/n) Σ (Xᵢ − X̄)(Xᵢ − X̄)ᵀ (chia n)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def mo_phong_do_chech(
    sigma2: float,
    n: int,
    so_mau: int,
    hat: np.random.Generator | None = None,
    nhat_ky: NhatKyTinhToan | None = None,
) -> dict[str, float]:
    """Mô phỏng cho thấy E[S²] = (n−1)/n · σ² (chệch) và S′² không chệch."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")
