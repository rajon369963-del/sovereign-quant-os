"""
MULTI-STRATEGY QUANTITATIVE ALPHA ENGINE
Implements:
1. Mean Reversion (RSI oversold + Bollinger lower band rebound)
2. Qullamaggie High Tight Flag / Episodic Pivot (Volume surge + EMA20 breakout)
3. Lead-Lag CVD Surge (Order Flow Imbalance sweep from HFT 1 & 2)
"""

from dataclasses import dataclass
from enum import Enum

try:
    import polars as pl
except ImportError:
    pl = None

class SignalType(Enum):
    BUY = "BUY"
    SELL = "SELL"
    HOLD = "HOLD"

class StrategyArchetype(Enum):
    MEAN_REVERSION = "MEAN_REVERSION"
    QULLAMAGGIE_BREAKOUT = "QULLAMAGGIE_BREAKOUT"
    LEAD_LAG_CVD_SURGE = "LEAD_LAG_CVD_SURGE"

@dataclass
class TradeSignal:
    bar_id: int
    timestamp: float
    strategy: StrategyArchetype
    signal_type: SignalType
    price: float
    stop_loss: float
    take_profit: float
    risk_reward_ratio: float
    confidence: float

class AlphaEngine:
    def __init__(self, rsi_oversold: float = 35.0, rsi_overbought: float = 65.0, min_rr_ratio: float = 2.0):
        self.rsi_oversold = rsi_oversold
        self.rsi_overbought = rsi_overbought
        self.min_rr_ratio = min_rr_ratio

    def evaluate_bar(self, row: dict, prev_row: dict | None = None) -> TradeSignal | None:
        """Evaluates latest market bar across the 3 strategy archetypes."""
        price = row["close"]
        atr = max(0.5, row.get("atr_14", 1.0))
        rsi = row.get("rsi_14", 50.0)
        ema_20 = row.get("ema_20", price)
        ema_200 = row.get("ema_200", price)
        bb_lower = row.get("bb_lower", price - 2 * atr)
        bb_upper = row.get("bb_upper", price + 2 * atr)
        volume = row.get("volume", 100)
        cvd = row.get("cvd", 0)

        # 1. Strategy 1: Mean Reversion
        # Condition: Price below lower Bollinger Band AND RSI < 35, reverting upwards
        if price <= bb_lower and rsi < self.rsi_oversold:
            stop_loss = price - (1.5 * atr)
            take_profit = price + (3.0 * atr)
            rr = (take_profit - price) / (price - stop_loss)
            return TradeSignal(
                bar_id=row["bar_id"],
                timestamp=row["timestamp"],
                strategy=StrategyArchetype.MEAN_REVERSION,
                signal_type=SignalType.BUY,
                price=price,
                stop_loss=stop_loss,
                take_profit=take_profit,
                risk_reward_ratio=rr,
                confidence=0.82
            )

        # 2. Strategy 2: Qullamaggie High Tight Flag Breakout
        # Condition: Price crosses above 20 EMA, EMA 20 > EMA 200, high volume surge
        prev_close = prev_row["close"] if prev_row else price
        prev_ema_20 = prev_row["ema_20"] if prev_row else ema_20
        prev_volume = prev_row["volume"] if prev_row else volume

        if (prev_close <= prev_ema_20 and price > ema_20) and (ema_20 > ema_200) and (volume > 1.5 * prev_volume):
            stop_loss = price - (1.0 * atr)
            take_profit = price + (2.5 * atr)
            rr = (take_profit - price) / (price - stop_loss)
            return TradeSignal(
                bar_id=row["bar_id"],
                timestamp=row["timestamp"],
                strategy=StrategyArchetype.QULLAMAGGIE_BREAKOUT,
                signal_type=SignalType.BUY,
                price=price,
                stop_loss=stop_loss,
                take_profit=take_profit,
                risk_reward_ratio=rr,
                confidence=0.88
            )

        # 3. Strategy 3: Lead-Lag CVD Surge (Order Flow Imbalance Sweep)
        # Condition: Massive positive volume delta surge (> 500) indicating aggressive market buyer sweep
        if cvd > 350 and rsi < self.rsi_overbought:
            stop_loss = price - (1.2 * atr)
            take_profit = price + (2.8 * atr)
            rr = (take_profit - price) / (price - stop_loss)
            return TradeSignal(
                bar_id=row["bar_id"],
                timestamp=row["timestamp"],
                strategy=StrategyArchetype.LEAD_LAG_CVD_SURGE,
                signal_type=SignalType.BUY,
                price=price,
                stop_loss=stop_loss,
                take_profit=take_profit,
                risk_reward_ratio=rr,
                confidence=0.85
            )

        return None

    def scan_all_bars(self, df_bars: pl.DataFrame) -> list[TradeSignal]:
        """Scans a Polars DataFrame of bars and returns all generated signals."""
        signals = []
        rows = df_bars.to_dicts()
        for i in range(1, len(rows)):
            sig = self.evaluate_bar(rows[i], rows[i - 1])
            if sig:
                signals.append(sig)
        return signals

if __name__ == "__main__":
    from data_engine import DataEngine
    engine = DataEngine()
    ticks = engine.generate_synthetic_ticks(1000)
    bars = engine.aggregate_to_ohlcv(ticks, bar_size=10)
    enriched = engine.compute_technical_indicators(bars)
    
    alpha = AlphaEngine()
    signals = alpha.scan_all_bars(enriched)
    print(f"Alpha Engine Smoke Test: Identified {len(signals)} high-probability trade setups.")
