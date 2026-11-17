"""Ứng dụng ML của Chương 6: Bộ phân loại sinh Gaussian và Hồi quy tuyến tính MLE/MAP."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


class PhanLoaiSinhGaussian:
    """Bộ phân loại sinh Gaussian (QDA/LDA) dùng MLE theo lớp và quy tắc Bayes (Ch4)."""

    def fit(self, X: Any, y: Any, nhat_ky: NhatKyTinhToan | None = None) -> PhanLoaiSinhGaussian:
        """Ước lượng MLE μₖ, Λₖ và xác suất tiên nghiệm cho từng lớp."""
        raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")

    def predict(self, X: Any) -> np.ndarray:
        """Dự đoán nhãn lớp cho các mẫu X."""
        raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")


def hoi_quy_tuyen_tinh_mle_map(
    X: Any,
    y: Any,
    lam: float = 0.0,
    nhat_ky: NhatKyTinhToan | None = None,
) -> np.ndarray:
    """Hồi quy tuyến tính MAP với tiên nghiệm chuẩn (tương ứng hồi quy Ridge)."""
    raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §6.")
