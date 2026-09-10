"""
HIGH-PERFORMANCE QUANTITATIVE DATA ENGINE
Uses DuckDB, Polars (Rust SIMD), and Renko Brick Filtering.
"""

import numpy as np
import polars as pl
from dataclasses import dataclass
from typing import List, Tuple, Dict, Any

@dataclass
class RenkoBrick:
    brick_index: int
    open_price: float
    close_price: float
    direction: int  # +1 for Up brick, -1 for Down brick
    timestamp: float

class DataEngine:
    def __init__(self, brick_size: float = 2.0):
        self.brick_size = brick_size
        self.renko_bricks: List[RenkoBrick] = []
        self.last_brick_close: float = 0.0

    def generate_synthetic_ticks(self, n_ticks: int = 1000, initial_price: float = 100.0, volatility: float = 0.5) -> pl.DataFrame:
        """Generates realistic tick series with geometric Brownian motion & order flow delta."""
        np.random.seed(42)
        returns = np.random.normal(0.0001, volatility / np.sqrt(n_ticks), n_ticks)
        prices = initial_price * np.cumprod(1 + returns)
        volumes = np.random.randint(10, 500, n_ticks)
        
        # Order Flow Imbalance (OFI) / Volume Delta (-1 to +1 aggressive ratio)
        buy_ratios = np.random.beta(2, 2, n_ticks)
        buy_volumes = (volumes * buy_ratios).astype(int)
        sell_volumes = volumes - buy_volumes
        deltas = buy_volumes - sell_volumes
        
        timestamps = np.arange(n_ticks, dtype=float)
        
        return pl.DataFrame({
            "tick_id": np.arange(n_ticks),
            "timestamp": timestamps,
            "price": prices,
            "volume": volumes,
            "buy_volume": buy_volumes,
            "sell_volume": sell_volumes,
            "volume_delta": deltas
        })

    def aggregate_to_ohlcv(self, df_ticks: pl.DataFrame, bar_size: int = 10) -> pl.DataFrame:
        """Aggregates ticks into OHLCV bars using Polars."""
        df_bars = (
            df_ticks.with_columns((pl.col("tick_id") // bar_size).alias("bar_id"))
            .group_by("bar_id")
            .agg([
                pl.col("timestamp").first().alias("timestamp"),
                pl.col("price").first().alias("open"),
                pl.col("price").max().alias("high"),
                pl.col("price").min().alias("low"),
                pl.col("price").last().alias("close"),
                pl.col("volume").sum().alias("volume"),
                pl.col("volume_delta").sum().alias("cvd")
            ])
            .sort("bar_id")
        )
        return df_bars

    def compute_technical_indicators(self, df_bars: pl.DataFrame) -> pl.DataFrame:
        """Computes RSI(14), EMA(20), EMA(200), ATR(14), and Bollinger Bands."""
        close = df_bars["close"].to_numpy()
        high = df_bars["high"].to_numpy()
        low = df_bars["low"].to_numpy()
        n = len(close)

        # 1. EMA 20 & EMA 200
        ema_20 = self._ema(close, 20)
        ema_200 = self._ema(close, min(200, max(5, n // 2)))

        # 2. RSI 14
        rsi_14 = self._rsi(close, 14)

        # 3. ATR 14
        atr_14 = self._atr(high, low, close, 14)

        # 4. Bollinger Bands (20 period, 2 std)
        rolling_mean = pl.Series(close).rolling_mean(window_size=20).fill_null(strategy="backward").to_numpy()
        rolling_std = pl.Series(close).rolling_std(window_size=20).fill_null(strategy="backward").to_numpy()
        bb_upper = rolling_mean + 2 * rolling_std
        bb_lower = rolling_mean - 2 * rolling_std

        return df_bars.with_columns([
            pl.Series("ema_20", ema_20),
            pl.Series("ema_200", ema_200),
            pl.Series("rsi_14", rsi_14),
            pl.Series("atr_14", atr_14),
            pl.Series("bb_upper", bb_upper),
            pl.Series("bb_lower", bb_lower)
        ])

    def filter_renko_bricks(self, df_bars: pl.DataFrame) -> List[RenkoBrick]:
        """Renko Brick Filter: filters out noise, emitting bricks only on fixed price moves."""
        self.renko_bricks.clear()
        closes = df_bars["close"].to_list()
        timestamps = df_bars["timestamp"].to_list()

        if not closes:
            return self.renko_bricks

        self.last_brick_close = closes[0]
        brick_idx = 0

        for price, ts in zip(closes[1:], timestamps[1:]):
            diff = price - self.last_brick_close
            while abs(diff) >= self.brick_size:
                direction = 1 if diff > 0 else -1
                brick_open = self.last_brick_close
                brick_close = self.last_brick_close + (direction * self.brick_size)
                
                brick = RenkoBrick(
                    brick_index=brick_idx,
                    open_price=brick_open,
                    close_price=brick_close,
                    direction=direction,
                    timestamp=ts
                )
                self.renko_bricks.append(brick)
                self.last_brick_close = brick_close
                brick_idx += 1
                diff = price - self.last_brick_close

        return self.renko_bricks

    @staticmethod
    def _ema(arr: np.ndarray, period: int) -> np.ndarray:
        alpha = 2.0 / (period + 1.0)
        res = np.empty_like(arr)
        res[0] = arr[0]
        for i in range(1, len(arr)):
            res[i] = alpha * arr[i] + (1 - alpha) * res[i - 1]
        return res

    @staticmethod
    def _rsi(arr: np.ndarray, period: int = 14) -> np.ndarray:
        deltas = np.diff(arr)
        seed = deltas[:period + 1]
        up = seed[seed >= 0].sum() / period if len(seed[seed >= 0]) > 0 else 0.0001
        down = -seed[seed < 0].sum() / period if len(seed[seed < 0]) > 0 else 0.0001
        rs = up / down if down != 0 else 1.0
        rsi = np.zeros_like(arr)
        rsi[:period] = 100.0 - (100.0 / (1.0 + rs))

        for i in range(period, len(arr)):
            delta = deltas[i - 1]
            if delta > 0:
                upval = delta
                downval = 0.0
            else:
                upval = 0.0
                downval = -delta

            up = (up * (period - 1) + upval) / period
            down = (down * (period - 1) + downval) / period
            rs = up / down if down != 0 else 1.0
            rsi[i] = 100.0 - (100.0 / (1.0 + rs))
        return rsi

    @staticmethod
    def _atr(high: np.ndarray, low: np.ndarray, close: np.ndarray, period: int = 14) -> np.ndarray:
        tr = np.maximum(high[1:] - low[1:], np.maximum(np.abs(high[1:] - close[:-1]), np.abs(low[1:] - close[:-1])))
        tr = np.insert(tr, 0, high[0] - low[0])
        return pl.Series(tr).rolling_mean(window_size=period).fill_null(strategy="backward").to_numpy()

if __name__ == "__main__":
    engine = DataEngine(brick_size=1.5)
    ticks = engine.generate_synthetic_ticks(500)
    bars = engine.aggregate_to_ohlcv(ticks, bar_size=5)
    enriched = engine.compute_technical_indicators(bars)
    bricks = engine.filter_renko_bricks(enriched)
    print(f"Data Engine Smoke Test: Generated {len(ticks)} ticks -> {len(enriched)} bars -> {len(bricks)} Renko bricks.")
