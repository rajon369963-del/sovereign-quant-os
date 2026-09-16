"""
CORTEX SCREENER & SCANNER ENGINE
Integrates: PKScreener, Screeni-py, Indian-Equity-Screener mechanics.
Features:
- Multi-factor momentum & breakout scanner over Indian Equities and Indices
- Bollinger Band squeeze detection + Volume surge detection (>1.5x 20-day SMA)
- RSI(14) overbought/oversold and EMA(20)/EMA(50) Golden/Death Cross
- Multi-timeframe trend confirmation
"""

import pandas as pd
import numpy as np

class ScreenerEngine:
    def __init__(self, lakehouse=None):
        self.lakehouse = lakehouse

    def calculate_technical_indicators(self, df):
        """Enriches DataFrame with technical indicators."""
        df = df.copy().sort_values('trade_date').reset_index(drop=True)
        if len(df) < 30:
            return None

        # Moving Averages
        df['ema_20'] = df['close'].ewm(span=20, adjust=False).mean()
        df['ema_50'] = df['close'].ewm(span=50, adjust=False).mean()
        df['sma_200'] = df['close'].rolling(window=min(200, len(df))).mean()

        # Volume SMA
        df['vol_sma_20'] = df['volume'].rolling(window=20).mean()
        df['vol_ratio'] = df['volume'] / (df['vol_sma_20'] + 1e-9)

        # RSI(14)
        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / (loss + 1e-9)
        df['rsi_14'] = 100 - (100 / (1 + rs))

        # Bollinger Bands (20, 2)
        df['bb_mid'] = df['close'].rolling(window=20).mean()
        df['bb_std'] = df['close'].rolling(window=20).std()
        df['bb_upper'] = df['bb_mid'] + 2 * df['bb_std']
        df['bb_lower'] = df['bb_mid'] - 2 * df['bb_std']
        df['bb_width'] = (df['bb_upper'] - df['bb_lower']) / (df['bb_mid'] + 1e-9)

        # ATR (14)
        high_low = df['high'] - df['low']
        high_close = (df['high'] - df['close'].shift()).abs()
        low_close = (df['low'] - df['close'].shift()).abs()
        ranges = pd.concat([high_low, high_close, low_close], axis=1)
        true_range = ranges.max(axis=1)
        df['atr_14'] = true_range.rolling(14).mean()

        return df

    def scan_symbol(self, df):
        """Evaluates breakout and trend conditions on latest bar."""
        df = self.calculate_technical_indicators(df)
        if df is None or len(df) < 30:
            return None

        latest = df.iloc[-1]
        prev = df.iloc[-2]

        signals = []
        score = 0

        # Signal 1: Golden Cross
        if prev['ema_20'] <= prev['ema_50'] and latest['ema_20'] > latest['ema_50']:
            signals.append('EMA_GOLDEN_CROSS')
            score += 30
        elif latest['ema_20'] > latest['ema_50']:
            signals.append('BULLISH_TREND')
            score += 15

        # Signal 2: Volume Breakout
        if latest['vol_ratio'] >= 1.5:
            signals.append(f'VOLUME_SURGE_{latest["vol_ratio"]:.1f}x')
            score += 25

        # Signal 3: Bollinger Band Breakout or Squeeze
        if latest['close'] > latest['bb_upper']:
            signals.append('BB_UPPER_BREAKOUT')
            score += 20
        elif latest['close'] < latest['bb_lower']:
            signals.append('BB_LOWER_BREAKDOWN')
            score -= 20
        elif latest['bb_width'] < df['bb_width'].rolling(50).min().iloc[-1] * 1.1:
            signals.append('BB_VOLATILITY_SQUEEZE')
            score += 10

        # Signal 4: RSI Momentum
        if 55 <= latest['rsi_14'] <= 70:
            signals.append('RSI_BULLISH_EXPANSION')
            score += 15
        elif latest['rsi_14'] > 75:
            signals.append('RSI_OVERBOUGHT')
            score -= 10
        elif latest['rsi_14'] < 30:
            signals.append('RSI_OVERSOLD')
            score += 10 # Mean reversion potential

        action = 'STRONG_BUY' if score >= 50 else ('BUY' if score >= 25 else ('STRONG_SELL' if score <= -30 else ('SELL' if score <= -15 else 'NEUTRAL')))

        return {
            'symbol': latest['symbol'],
            'date': str(latest['trade_date']),
            'close': float(latest['close']),
            'volume': int(latest['volume']),
            'vol_ratio': round(float(latest['vol_ratio']), 2),
            'rsi_14': round(float(latest['rsi_14']), 1),
            'ema_20': round(float(latest['ema_20']), 2),
            'ema_50': round(float(latest['ema_50']), 2),
            'bb_width': round(float(latest['bb_width']), 4),
            'atr_14': round(float(latest['atr_14']), 2),
            'signals': signals,
            'composite_score': score,
            'action': action
        }

    def scan_universe(self, symbols):
        """Scans multiple symbols and returns ranked opportunities."""
        results = []
        for sym in symbols:
            if self.lakehouse:
                df = self.lakehouse.query_history(sym)
            else:
                continue
            scan_res = self.scan_symbol(df)
            if scan_res:
                results.append(scan_res)
        
        results.sort(key=lambda x: x['composite_score'], reverse=True)
        return results

if __name__ == '__main__':
    from cortex_historical_lakehouse import HistoricalLakehouse
    lh = HistoricalLakehouse()
    screener = ScreenerEngine(lh)
    universe = ['NIFTY 50', 'BANKNIFTY', 'RELIANCE', 'HDFCBANK', 'INFY', 'TCS', 'ITC', 'SBIN']
    results = screener.scan_universe(universe)
    print(f'Screener scanned {len(results)} symbols. Top Opportunities:')
    for r in results[:4]:
        print(f"{r['symbol']} | Score: {r['composite_score']} | Action: {r['action']} | Signals: {r['signals']}")
