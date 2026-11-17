"""Mini-pipeline tích hợp: Chuẩn hóa → PCA (Ch2) → Logistic L2 (Ch5) → Ước lượng & KTC (Ch6)."""

from __future__ import annotations

from typing import Any


def chay_pipeline(X: Any, y: Any, k_pca: int = 2, lam: float = 0.01) -> dict[str, Any]:
    """Chạy luồng ML tích hợp từ đầu đến cuối (Phần C1)."""
    raise NotImplementedError("Chưa cài đặt — triển khai sau khi hoàn thành Chương 1–6.")
