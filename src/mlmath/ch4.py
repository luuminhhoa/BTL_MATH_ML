"""Alias tiếng Anh cho Chương 4 (chỉ re-export)."""

from __future__ import annotations

from .chuong_4_xac_suat.dem import to_hop as comb
from .chuong_4_xac_suat.ung_dung_ml import NaiveBayesRoiRac as DiscreteNaiveBayes
from .chuong_4_xac_suat.xac_suat import bayes as bayes_posterior

__all__ = [
    "comb",
    "bayes_posterior",
    "DiscreteNaiveBayes",
]
