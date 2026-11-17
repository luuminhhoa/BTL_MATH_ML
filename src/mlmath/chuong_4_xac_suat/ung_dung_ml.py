"""Ứng dụng ML của Chương 4: Bộ phân loại Naive Bayes rời rạc."""

from __future__ import annotations

from typing import Any

import numpy as np

from ..tien_ich.nhat_ky_tinh_toan import NhatKyTinhToan


class NaiveBayesRoiRac:
    """Bộ phân loại Naive Bayes rời rạc có làm trơn Laplace."""

    def fit(
        self,
        X: Any,
        y: Any,
        lam_lam_tron: float = 1.0,
        nhat_ky: NhatKyTinhToan | None = None,
    ) -> NaiveBayesRoiRac:
        """Huấn luyện mô hình từ dữ liệu rời rạc X và nhãn y."""
        raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")

    def predict_proba(self, X: Any) -> np.ndarray:
        """Dự đoán xác suất hậu nghiệm cho từng lớp."""
        raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")

    def predict(self, X: Any) -> np.ndarray:
        """Dự đoán nhãn lớp có xác suất hậu nghiệm cao nhất."""
        raise NotImplementedError("Chưa cài đặt — xem handoff/HOP_DONG_MODULE.md §4.")
