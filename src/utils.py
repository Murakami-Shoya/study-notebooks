"""
共通ヘルパー関数（必要に応じて追加）

例：
- データ生成
- プロット設定
- 評価指標
"""

import numpy as np


def generate_synthetic_signal(n_samples: int, sampling_rate: float, seed: int = 42) -> np.ndarray:
    """
    合成信号を生成する簡易ヘルパー

    Parameters
    ----------
    n_samples : int
        サンプル数
    sampling_rate : float
        サンプリングレート (Hz)
    seed : int
        乱数シード

    Returns
    -------
    np.ndarray
        生成された信号
    """
    np.random.seed(seed)
    t = np.arange(n_samples) / sampling_rate
    signal = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.randn(n_samples)
    return signal
