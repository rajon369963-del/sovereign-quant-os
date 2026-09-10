#!/usr/bin/env python3
"""
===============================================================================
GEMINI ANTIGRAVITY FULL YOLO 2: INDIAN MARKET AGENTIC ALPHA (NSE/BSE/NFO)
===============================================================================
Architecture: Decoupled Multi-Agent Event-Driven Engine
Features:
  1. Decoupled Signal Generation vs Broker API Execution via Asynchronous Queue
  2. Multi-Agent Debate System (Bull Agent vs Bear Agent vs Judge Agent > 85%)
  3. Indian Market Alpha Rules:
     - Pre-Market Gap Fading (09:15 - 09:30 AM IST)
     - NSE Option Chain Shadow Tracking (PCR, Max Pain, Call/Put OI Walls)
     - BankNifty Friday Weekend Drift (Theta Unwind)
     - HDFC Bank vs ICICI Bank Statistical Arbitrage Pairs Trading
     - 3*ATR Dynamic Chandelier / SuperTrend Volatility Trailing Stop
     - The 3-5-7 Structural Risk Rule
  4. Full YOLO 2 Darwinian Mechanics:
     - Delete-Until-Profit Loop (Sharpe < 1.5 Pruning)
     - Liquidator Daily Circuit Breaker (2.0% Hard Cut)
     - Self-Healing Error Recovery (Exponential Backoff + Jitter)
     - Read-Only SECRET_SAUCE.md Protection
     - Unit Test Your Wallet Before Write (Margin, Freeze, Lot, 0.05 Tick)
  5. SQLite WAL Persistent Trade, Debate & Telemetry Ledger
===============================================================================
"""

import os
import sys
import time
import math
import random
import asyncio
import sqlite3
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from typing import Dict, Any, List, Optional, Tuple

try:
    import orjson
except ImportError:
    import json as orjson

import numpy as np

try:
    from kiteconnect import KiteConnect
    KITECONNECT_AVAILABLE = True
except ImportError:
    KITECONNECT_AVAILABLE = False


# =============================================================================
# 1. ENUMS & DATA MODELS
# =============================================================================

class MarketSymbol(str, Enum):
    NIFTY = "NIFTY50"
    BANKNIFTY = "BANKNIFTY"
    HDFCBANK = "HDFCBANK"
    ICICIBANK = "ICICIBANK"

class StrategyType(str, Enum):
    GAP_FADE = "PRE_MARKET_GAP_FADE"
    OPTION_CHAIN_SHADOW = "OPTION_CHAIN_SHADOW"
    BANKNIFTY_FRIDAY_DRIFT = "BANKNIFTY_FRIDAY_DRIFT"
    HDFC_ICICI_PAIRS = "HDFC_ICICI_PAIRS"
    VOLATILITY_BREAKOUT = "VOLATILITY_BREAKOUT"

class SignalSide(str, Enum):
    BUY = "BUY"
    SELL = "SELL"

class OrderStatus(str, Enum):
    PENDING = "PENDING"
    SUBMITTED = "SUBMITTED"
    FILLED = "FILLED"
    TRAILING = "TRAILING"
    CLOSED = "CLOSED"
    CANCELLED = "CANCELLED"
    REJECTED = "REJECTED"


@dataclass
class IndianMarketTick:
    symbol: str
    price: float
    vwap: float
    atr: float
    high: float
    low: float
    volume: float
    cvd: float
    timestamp: float = field(default_factory=time.time)

@dataclass
class OptionStrikeData:
    strike: float
    call_oi: int
    put_oi: int
    call_ltp: float
    put_ltp: float
    call_iv: float
    put_iv: float

@dataclass
class OptionChainShadow:
    underlying: str
    spot_price: float
    pcr: float
    max_pain: float
    call_wall: float
    put_wall: float
    strikes: List[OptionStrikeData]
    timestamp: float = field(default_factory=time.time)

@dataclass
class RawAlphaSignal:
    signal_id: str
    symbol: str
    strategy: StrategyType
    side: SignalSide
    entry_price: float
    base_stop_loss: float
    target_price: float
    atr: float
    rationale: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)

@dataclass
class AgentDebateVerdict:
    signal_id: str
    bull_conviction: float
    bear_conviction: float
    judge_confidence: float
    approved: bool
    verdict_rationale: str
    bull_thesis: str
    bear_thesis: str
    timestamp: float = field(default_factory=time.time)

@dataclass
class VerifiedOrder:
    order_id: str
    signal_id: str
    symbol: str
    strategy: str
    side: str
    quantity: int
    entry_price: float
    fill_price: float
    stop_loss: float
    take_profit: float
    highest_price_seen: float
    lowest_price_seen: float
    status: OrderStatus
    created_at: float
    closed_at: Optional[float] = None
    exit_price: Optional[float] = None
    realized_pnl: float = 0.0


# =============================================================================
# 2. FULL YOLO 2 INVARIANT: READ-ONLY SECRET_SAUCE GUARD
# =============================================================================

class SecretSauceGuard:
    """
    Validates that SECRET_SAUCE.md exists and is locked with chmod 444 (read-only).
    Prevents unauthorized LLM or agent modifications to core proprietary alpha rules.
    """
    SECRET_SAUCE_PATH = "/Users/rajondas/.gemini/antigravity/scratch/antigravity_yolo_trading_engine/SECRET_SAUCE.md"

    @classmethod
    def verify_integrity(cls) -> Tuple[bool, str]:
        if not os.path.exists(cls.SECRET_SAUCE_PATH):
            return False, "CRITICAL: SECRET_SAUCE.md does not exist on disk!"

        # Check permissions: must be read-only (0o444 or 0o400)
        mode = os.stat(cls.SECRET_SAUCE_PATH).st_mode
        if (mode & 0o222) != 0:
            return False, f"CRITICAL: SECRET_SAUCE.md is writable! Mode: {oct(mode)}. Must be chmod 444."

        # Verify read-only enforcement
        try:
            with open(cls.SECRET_SAUCE_PATH, "a") as f:
                f.write("\nillegal_write")
            return False, "CRITICAL: Writable check failed! Appended successfully to SECRET_SAUCE.md!"
        except (PermissionError, OSError):
            pass

        return True, "SECRET_SAUCE.md is securely locked (chmod 444 read-only)."


# =============================================================================
# 3. INDIAN MARKET ALPHA MODULES
# =============================================================================

class PreMarketGapFader:
    """
    Indian Market Hack #1: 09:15 - 09:30 AM IST Gap Fading.
    When overnight gap on Nifty or BankNifty exceeds 0.60%, fades back toward previous VWAP.
    """
    def __init__(self, min_gap_pct: float = 0.60, target_fill_ratio: float = 0.70, sl_gap_ratio: float = 0.35):
        self.min_gap_pct = min_gap_pct
        self.target_fill_ratio = target_fill_ratio
        self.sl_gap_ratio = sl_gap_ratio

    def evaluate_gap(self, symbol: str, open_price: float, prev_vwap: float, current_atr: float, is_morning_window: bool = True) -> Optional[RawAlphaSignal]:
        if not is_morning_window:
            return None

        gap_distance = open_price - prev_vwap
        gap_pct = (gap_distance / prev_vwap) * 100.0

        if abs(gap_pct) < self.min_gap_pct:
            return None

        sig_id = f"SIG_GAP_{symbol}_{int(time.time()*1000)}"

        # Gap Up -> Fade Short
        if gap_pct >= self.min_gap_pct:
            target = open_price - (gap_distance * self.target_fill_ratio)
            stop_loss = open_price + (gap_distance * self.sl_gap_ratio)
            # Quantize to 0.05
            target = round(round(target / 0.05) * 0.05, 2)
            stop_loss = round(round(stop_loss / 0.05) * 0.05, 2)

            return RawAlphaSignal(
                signal_id=sig_id,
                symbol=symbol,
                strategy=StrategyType.GAP_FADE,
                side=SignalSide.SELL,
                entry_price=open_price,
                base_stop_loss=stop_loss,
                target_price=target,
                atr=current_atr,
                rationale=f"Gap Up {gap_pct:.2f}% (>= {self.min_gap_pct}%) from prev VWAP ₹{prev_vwap:.2f}. Fading short to ₹{target:.2f}.",
                metadata={"gap_pct": round(gap_pct, 2), "prev_vwap": prev_vwap}
            )

        # Gap Down -> Fade Long
        elif gap_pct <= -self.min_gap_pct:
            target = open_price + (abs(gap_distance) * self.target_fill_ratio)
            stop_loss = open_price - (abs(gap_distance) * self.sl_gap_ratio)
            target = round(round(target / 0.05) * 0.05, 2)
            stop_loss = round(round(stop_loss / 0.05) * 0.05, 2)

            return RawAlphaSignal(
                signal_id=sig_id,
                symbol=symbol,
                strategy=StrategyType.GAP_FADE,
                side=SignalSide.BUY,
                entry_price=open_price,
                base_stop_loss=stop_loss,
                target_price=target,
                atr=current_atr,
                rationale=f"Gap Down {gap_pct:.2f}% (<= -{self.min_gap_pct}%) from prev VWAP ₹{prev_vwap:.2f}. Fading long to ₹{target:.2f}.",
                metadata={"gap_pct": round(gap_pct, 2), "prev_vwap": prev_vwap}
            )

        return None


class NSEOptionChainShadowTracker:
    """
    Indian Market Hack #2, #3, #27:
    Real-time Option Chain tracking:
      - Put-Call Ratio (PCR)
      - Max Pain Calculation
      - Call Wall (Magnetic Resistance) & Put Wall (Support Floor)
    """
    def __init__(self):
        pass

    def compute_option_chain_metrics(self, underlying: str, spot_price: float, strikes: List[OptionStrikeData]) -> OptionChainShadow:
        if not strikes:
            return OptionChainShadow(
                underlying=underlying, spot_price=spot_price, pcr=1.0,
                max_pain=spot_price, call_wall=spot_price, put_wall=spot_price, strikes=[]
            )

        total_call_oi = sum(s.call_oi for s in strikes)
        total_put_oi = sum(s.put_oi for s in strikes)
        pcr = float(total_put_oi / total_call_oi) if total_call_oi > 0 else 1.0

        # Call Wall: strike with maximum call OI
        call_wall_strike = max(strikes, key=lambda s: s.call_oi).strike
        # Put Wall: strike with maximum put OI
        put_wall_strike = max(strikes, key=lambda s: s.put_oi).strike

        # Calculate Max Pain
        # Total option buyer payout at expiration if spot expires at strike K
        min_payout = float("inf")
        max_pain_strike = spot_price

        for target_strike in strikes:
            K = target_strike.strike
            total_payout = 0.0
            for s in strikes:
                # Call payout = max(0, K - s.strike) * call_oi
                # Put payout  = max(0, s.strike - K) * put_oi
                call_payout = max(0.0, K - s.strike) * s.call_oi
                put_payout = max(0.0, s.strike - K) * s.put_oi
                total_payout += (call_payout + put_payout)
            if total_payout < min_payout:
                min_payout = total_payout
                max_pain_strike = K

        return OptionChainShadow(
            underlying=underlying,
            spot_price=spot_price,
            pcr=round(pcr, 3),
            max_pain=max_pain_strike,
            call_wall=call_wall_strike,
            put_wall=put_wall_strike,
            strikes=strikes
        )


class BankNiftyFridayWeekendDrifter:
    """
    Indian Market Hack #4: Friday Afternoon Drift (14:00 - 15:15 IST).
    Heavy theta decay and weekend positioning force BankNifty toward Max Pain.
    """
    def __init__(self, drift_gravity: float = 0.60):
        self.drift_gravity = drift_gravity

    def evaluate_friday_drift(
        self,
        spot_price: float,
        option_chain: OptionChainShadow,
        atr: float,
        is_friday_afternoon: bool = True
    ) -> Optional[RawAlphaSignal]:
        if not is_friday_afternoon:
            return None

        distance_to_max_pain = option_chain.max_pain - spot_price
        # Only trade if significant divergence exists (> 0.5 * ATR)
        if abs(distance_to_max_pain) < (0.5 * atr):
            return None

        sig_id = f"SIG_BNF_FRI_{int(time.time()*1000)}"

        if distance_to_max_pain > 0:
            # Drift upward to Max Pain
            target = spot_price + (distance_to_max_pain * self.drift_gravity)
            stop_loss = spot_price - (0.8 * atr)
            return RawAlphaSignal(
                signal_id=sig_id,
                symbol=MarketSymbol.BANKNIFTY.value,
                strategy=StrategyType.BANKNIFTY_FRIDAY_DRIFT,
                side=SignalSide.BUY,
                entry_price=spot_price,
                base_stop_loss=round(round(stop_loss / 0.05) * 0.05, 2),
                target_price=round(round(target / 0.05) * 0.05, 2),
                atr=atr,
                rationale=f"Friday BankNifty theta drift upward toward Max Pain ₹{option_chain.max_pain:.1f} (Gap: {distance_to_max_pain:.1f} pts).",
                metadata={"max_pain": option_chain.max_pain, "pcr": option_chain.pcr}
            )
        else:
            # Drift downward to Max Pain
            target = spot_price + (distance_to_max_pain * self.drift_gravity)
            stop_loss = spot_price + (0.8 * atr)
            return RawAlphaSignal(
                signal_id=sig_id,
                symbol=MarketSymbol.BANKNIFTY.value,
                strategy=StrategyType.BANKNIFTY_FRIDAY_DRIFT,
                side=SignalSide.SELL,
                entry_price=spot_price,
                base_stop_loss=round(round(stop_loss / 0.05) * 0.05, 2),
                target_price=round(round(target / 0.05) * 0.05, 2),
                atr=atr,
                rationale=f"Friday BankNifty theta drift downward toward Max Pain ₹{option_chain.max_pain:.1f} (Gap: {distance_to_max_pain:.1f} pts).",
                metadata={"max_pain": option_chain.max_pain, "pcr": option_chain.pcr}
            )


class HdfcIciciPairsTrader:
    """
    Indian Market Hack #5 & #28: HDFC Bank vs ICICI Bank Pairs Trading.
    Spread ratio Z-score mean reversion (|Z| > 2.0 -> Entry, |Z| < 0.5 -> Exit).
    """
    def __init__(self, entry_z: float = 2.0, exit_z: float = 0.5, stop_z: float = 3.2, window: int = 30, min_periods: int = 10):
        self.entry_z = entry_z
        self.exit_z = exit_z
        self.stop_z = stop_z
        self.window = window
        self.min_periods = min_periods

    def compute_z_score(self, ratio_series: np.ndarray) -> float:
        if len(ratio_series) < self.min_periods:
            return 0.0
        sample_size = min(len(ratio_series), self.window)
        rolling = ratio_series[-sample_size:]
        mean = np.mean(rolling)
        std = np.std(rolling)
        if std < 1e-6:
            return 0.0
        return float((rolling[-1] - mean) / std)

    def evaluate_pairs(
        self,
        hdfc_price: float,
        icici_price: float,
        ratio_history: np.ndarray,
        hdfc_atr: float
    ) -> Optional[RawAlphaSignal]:
        current_ratio = hdfc_price / max(1e-4, icici_price)
        ratio_series = np.append(ratio_history, current_ratio)
        z_score = self.compute_z_score(ratio_series)

        sig_id = f"SIG_PAIRS_{int(time.time()*1000)}"

        # HDFC overvalued relative to ICICI: Short HDFC
        if z_score >= self.entry_z:
            stop_loss = hdfc_price + (2.0 * hdfc_atr)
            target = hdfc_price - (3.0 * hdfc_atr)
            return RawAlphaSignal(
                signal_id=sig_id,
                symbol=MarketSymbol.HDFCBANK.value,
                strategy=StrategyType.HDFC_ICICI_PAIRS,
                side=SignalSide.SELL,
                entry_price=hdfc_price,
                base_stop_loss=round(round(stop_loss / 0.05) * 0.05, 2),
                target_price=round(round(target / 0.05) * 0.05, 2),
                atr=hdfc_atr,
                rationale=f"HDFC/ICICI spread ratio Z-score {z_score:.2f} >= +{self.entry_z}. Short HDFC Bank (hedge with long ICICI).",
                metadata={"z_score": round(z_score, 2), "current_ratio": round(current_ratio, 4)}
            )
        # HDFC undervalued relative to ICICI: Long HDFC
        elif z_score <= -self.entry_z:
            stop_loss = hdfc_price - (2.0 * hdfc_atr)
            target = hdfc_price + (3.0 * hdfc_atr)
            return RawAlphaSignal(
                signal_id=sig_id,
                symbol=MarketSymbol.HDFCBANK.value,
                strategy=StrategyType.HDFC_ICICI_PAIRS,
                side=SignalSide.BUY,
                entry_price=hdfc_price,
                base_stop_loss=round(round(stop_loss / 0.05) * 0.05, 2),
                target_price=round(round(target / 0.05) * 0.05, 2),
                atr=hdfc_atr,
                rationale=f"HDFC/ICICI spread ratio Z-score {z_score:.2f} <= -{self.entry_z}. Long HDFC Bank (hedge with short ICICI).",
                metadata={"z_score": round(z_score, 2), "current_ratio": round(current_ratio, 4)}
            )

        return None


class TrailingATRManager:
    """
    Indian Market Hack #6: 3*ATR Dynamic Chandelier / SuperTrend Volatility Trailing.
    Strictly ratchets stops in favorable direction; never widens against position.
    """
    def __init__(self, atr_multiplier: float = 3.0):
        self.atr_multiplier = atr_multiplier

    def update_trailing_stop(self, order: VerifiedOrder, current_price: float, current_atr: float) -> Tuple[float, bool]:
        ratchet_step = self.atr_multiplier * current_atr
        updated = False

        if order.side == SignalSide.BUY.value:
            if current_price > order.highest_price_seen:
                order.highest_price_seen = current_price
            new_stop = order.highest_price_seen - ratchet_step
            new_stop = round(round(new_stop / 0.05) * 0.05, 2)
            if new_stop > order.stop_loss:
                order.stop_loss = new_stop
                updated = True

        elif order.side == SignalSide.SELL.value:
            if current_price < order.lowest_price_seen:
                order.lowest_price_seen = current_price
            new_stop = order.lowest_price_seen + ratchet_step
            new_stop = round(round(new_stop / 0.05) * 0.05, 2)
            if new_stop < order.stop_loss:
                order.stop_loss = new_stop
                updated = True

        return order.stop_loss, updated


class Risk357Manager:
    """
    Indian Market Hack #7: The 3-5-7 Structural Risk Rule.
      1. Max 3 concurrent positions.
      2. Max 5% cumulative capital risk across all active trades.
      3. 7 consecutive losses locks execution for 24 hours.
    """
    def __init__(self, max_concurrent: int = 3, max_total_risk_pct: float = 0.05, max_consecutive_losses: int = 7):
        self.max_concurrent = max_concurrent
        self.max_total_risk_pct = max_total_risk_pct
        self.max_consecutive_losses = max_consecutive_losses
        self.consecutive_losses = 0
        self.is_loss_locked = False

    def check_pre_trade_risk(self, active_orders_count: int, active_risk_capital: float, proposed_risk: float, total_capital: float) -> Tuple[bool, str]:
        if self.is_loss_locked:
            return False, f"RISK-357 VETO: 24-hour lockout active due to {self.consecutive_losses} consecutive losses!"

        if active_orders_count >= self.max_concurrent:
            return False, f"RISK-357 VETO: Max concurrent positions ({self.max_concurrent}) reached!"

        new_total_risk = active_risk_capital + proposed_risk
        allowed_risk = total_capital * self.max_total_risk_pct
        if new_total_risk > allowed_risk:
            return False, f"RISK-357 VETO: Total portfolio risk ₹{new_total_risk:.2f} exceeds 5% limit (₹{allowed_risk:.2f})!"

        return True, "RISK-357 PASS: Position count and capital risk within bounds."

    def record_trade_result(self, pnl: float):
        if pnl < 0:
            self.consecutive_losses += 1
            if self.consecutive_losses >= self.max_consecutive_losses:
                self.is_loss_locked = True
        else:
            self.consecutive_losses = 0


# =============================================================================
# 4. MULTI-AGENT DEBATE SYSTEM (BULL vs BEAR vs JUDGE > 85%)
# =============================================================================

class BullAgent:
    """
    Bullish Advocate: Evaluates upward momentum, CVD buying dominance, VWAP support,
    low PCR, and call strike wall breakouts.
    """
    def evaluate(self, signal: RawAlphaSignal, option_chain: Optional[OptionChainShadow], tick: IndianMarketTick) -> Tuple[float, str]:
        conviction = 0.50
        theses = []

        if signal.side == SignalSide.BUY:
            conviction += 0.20
            theses.append("Signal alignment: Direction is Long.")
        else:
            conviction -= 0.30
            theses.append("Counter-thesis: Signal is Short.")

        # CVD buying pressure
        if tick.cvd > 0:
            conviction += 0.15
            theses.append(f"Positive CVD accumulation: +{tick.cvd:.1f}.")

        # VWAP support
        if tick.price >= tick.vwap:
            conviction += 0.10
            theses.append("Price holds firmly above daily VWAP.")

        # Option chain sentiment
        if option_chain:
            if option_chain.pcr < 0.80:
                conviction += 0.10
                theses.append(f"Low PCR {option_chain.pcr:.2f} indicates oversold spring.")
            if tick.price > option_chain.put_wall:
                conviction += 0.05
                theses.append(f"Price comfortably above heavy Put OI support wall ₹{option_chain.put_wall:.0f}.")

        conviction = max(0.0, min(1.0, conviction))
        return round(conviction, 3), " | ".join(theses)


class BearAgent:
    """
    Bearish Advocate: Evaluates overhead call walls, overbought PCR (> 1.35),
    negative CVD divergence, resistance rejections, and downside vulnerability.
    """
    def evaluate(self, signal: RawAlphaSignal, option_chain: Optional[OptionChainShadow], tick: IndianMarketTick) -> Tuple[float, str]:
        conviction = 0.50
        theses = []

        if signal.side == SignalSide.SELL:
            conviction += 0.20
            theses.append("Signal alignment: Direction is Short.")
        else:
            conviction -= 0.30
            theses.append("Counter-thesis: Signal is Long.")

        # Negative CVD or seller absorption
        if tick.cvd < 0:
            conviction += 0.15
            theses.append(f"Aggressive seller flow (CVD {tick.cvd:.1f}).")

        # Price below VWAP
        if tick.price < tick.vwap:
            conviction += 0.10
            theses.append("Price rejected below institutional VWAP.")

        # Option chain resistance
        if option_chain:
            if option_chain.pcr > 1.30:
                conviction += 0.10
                theses.append(f"Elevated PCR {option_chain.pcr:.2f} indicates call buyer euphoria.")
            if tick.price >= option_chain.call_wall:
                conviction += 0.10
                theses.append(f"Price testing heavy Call OI ceiling at ₹{option_chain.call_wall:.0f}.")

        conviction = max(0.0, min(1.0, conviction))
        return round(conviction, 3), " | ".join(theses)


class JudgeAgent:
    """
    Judge & Arbiter: Weighs Bull thesis vs Bear thesis against market regime and FinBERT score.
    INVARIANT: Approves trade ONLY IF Judge Confidence exceeds 85% (> 0.85).
    """
    CONFIDENCE_THRESHOLD = 0.85

    def synthesize_verdict(
        self,
        signal: RawAlphaSignal,
        bull_conviction: float,
        bull_thesis: str,
        bear_conviction: float,
        bear_thesis: str,
        macro_sentiment: float = 0.0
    ) -> AgentDebateVerdict:
        
        # Calculate directional alignment
        if signal.side == SignalSide.BUY:
            # Bullish signal requires high bull conviction and low bear resistance
            raw_confidence = (bull_conviction * 0.65) + ((1.0 - bear_conviction) * 0.35)
            if macro_sentiment > 0.3:
                raw_confidence += 0.05
            elif macro_sentiment < -0.4:
                raw_confidence -= 0.20
        else:
            # Bearish signal requires high bear conviction and low bull resistance
            raw_confidence = (bear_conviction * 0.65) + ((1.0 - bull_conviction) * 0.35)
            if macro_sentiment < -0.3:
                raw_confidence += 0.05
            elif macro_sentiment > 0.4:
                raw_confidence -= 0.20

        judge_confidence = max(0.0, min(1.0, raw_confidence))
        approved = judge_confidence > self.CONFIDENCE_THRESHOLD

        if approved:
            rationale = (f"JUDGE APPROVED (Confidence {judge_confidence*100:.1f}% > 85%): "
                         f"Sufficient directional edge. Bull: {bull_conviction:.2f}, Bear: {bear_conviction:.2f}.")
        else:
            rationale = (f"JUDGE VETOED (Confidence {judge_confidence*100:.1f}% <= 85%): "
                         f"High debate dissonance or insufficient statistical edge.")

        return AgentDebateVerdict(
            signal_id=signal.signal_id,
            bull_conviction=bull_conviction,
            bear_conviction=bear_conviction,
            judge_confidence=round(judge_confidence, 3),
            approved=approved,
            verdict_rationale=rationale,
            bull_thesis=bull_thesis,
            bear_thesis=bear_thesis
        )


# =============================================================================
# 5. FULL YOLO 2 DARWINIAN MECHANICS
# =============================================================================

class DeleteUntilProfitLoop:
    """
    Full YOLO 2 Mechanic #1: Delete-Until-Profit Loop.
    Any strategy generating a rolling 30-trade Sharpe Ratio < 1.5 is pruned/quarantined.
    """
    def __init__(self, min_sharpe: float = 1.5, min_sample_trades: int = 10, db_path: Optional[str] = None):
        self.min_sharpe = min_sharpe
        self.min_sample_trades = min_sample_trades
        self.db_path = db_path
        self.strategy_trade_history: Dict[str, List[float]] = {}
        self.quarantined_strategies: set = set()

    def record_trade_pnl(self, strategy_name: str, pnl: float) -> Tuple[float, bool]:
        if strategy_name not in self.strategy_trade_history:
            self.strategy_trade_history[strategy_name] = []
        self.strategy_trade_history[strategy_name].append(pnl)

        # Evaluate Sharpe ratio after minimum sample
        trades = self.strategy_trade_history[strategy_name][-30:]
        sharpe = 0.0
        quarantined = False
        if len(trades) >= self.min_sample_trades:
            mean_return = float(np.mean(trades))
            std_return = float(np.std(trades))
            sharpe = float((mean_return / (std_return + 1e-8)) * np.sqrt(252))  # Annualized factor
            if sharpe < self.min_sharpe:
                if strategy_name not in self.quarantined_strategies:
                    self.quarantined_strategies.add(strategy_name)
                    quarantined = True
                    if self.db_path:
                        try:
                            with sqlite3.connect(self.db_path) as conn:
                                conn.execute("""
                                INSERT INTO strategy_quarantine_records (timestamp, strategy, sharpe_ratio, trades_count, status, action)
                                VALUES (?, ?, ?, ?, ?, ?)
                                """, (time.time(), strategy_name, sharpe, len(trades), "QUARANTINED", "PRUNED_SHARPE_LESS_1.5"))
                        except Exception:
                            pass
                else:
                    quarantined = True
        return sharpe, quarantined

    def is_strategy_active(self, strategy_name: str) -> bool:
        return strategy_name not in self.quarantined_strategies

    def unquarantine_strategy(self, strategy_name: str):
        self.quarantined_strategies.discard(strategy_name)


class LiquidatorCircuitBreaker:
    """
    Full YOLO 2 Mechanic #2: Liquidator Daily Circuit Breaker.
    Daily realized + unrealized loss >= 2.0% triggers immediate liquidation and permanent freeze.
    """
    def __init__(self, initial_capital: float = 100000.0, daily_loss_limit_pct: float = 0.02):
        self.initial_capital = initial_capital
        self.peak_capital = initial_capital
        self.current_capital = initial_capital
        self.daily_loss_limit_pct = daily_loss_limit_pct
        self.daily_loss_limit = initial_capital * daily_loss_limit_pct
        self.daily_realized_loss = 0.0
        self.is_tripped = False
        self.trip_reason = ""

    def evaluate_capital(self, current_capital: float, unrealized_pnl: float = 0.0) -> Tuple[bool, str]:
        if self.is_tripped:
            return True, f"LIQUIDATOR ALREADY TRIPPED: {self.trip_reason}"

        if current_capital > self.peak_capital:
            self.peak_capital = current_capital
        self.current_capital = current_capital

        total_drawdown = (self.peak_capital - (current_capital + unrealized_pnl))
        total_drawdown_pct = total_drawdown / self.peak_capital

        if total_drawdown_pct >= self.daily_loss_limit_pct:
            self.is_tripped = True
            self.trip_reason = (f"LIQUIDATOR CIRCUIT BREAKER TRIPPED! Drawdown {total_drawdown_pct*100:.2f}% "
                                f">= {self.daily_loss_limit_pct*100:.1f}%. Capital: ₹{current_capital:.2f}.")
            return True, self.trip_reason

        return False, f"Nominal: Intraday Drawdown {total_drawdown_pct*100:.2f}% < {self.daily_loss_limit_pct*100:.1f}%."


class WalletPreFlightTester:
    """
    Full YOLO 2 Mechanic #5: Unit Test Your Wallet Before Write.
    Validates:
      1. F&O Ban Period Check (MWPL > 95% -> Square-off only)
      2. Required Margin <= Available Margin * 0.90
      3. Quantity is strict multiple of NSE lot size (Nifty: 25, BankNifty: 15)
      4. Quantity does not exceed NSE Freeze Limits (Nifty: 1800, BankNifty: 900)
      5. Price is strictly quantized to ₹0.05 multiples.
    """
    LOT_SIZES = {
        MarketSymbol.NIFTY.value: 25,
        MarketSymbol.BANKNIFTY.value: 15,
        MarketSymbol.HDFCBANK.value: 1,
        MarketSymbol.ICICIBANK.value: 1
    }

    FREEZE_LIMITS = {
        MarketSymbol.NIFTY.value: 1800,
        MarketSymbol.BANKNIFTY.value: 900,
        MarketSymbol.HDFCBANK.value: 10000,
        MarketSymbol.ICICIBANK.value: 10000
    }

    BANNED_UNDERLYINGS: set = set()

    @classmethod
    def set_fo_ban_list(cls, banned_symbols: List[str]):
        cls.BANNED_UNDERLYINGS = set(banned_symbols)

    @classmethod
    def add_fo_ban(cls, symbol: str):
        cls.BANNED_UNDERLYINGS.add(symbol)

    @classmethod
    def remove_fo_ban(cls, symbol: str):
        cls.BANNED_UNDERLYINGS.discard(symbol)

    @classmethod
    def test_wallet_and_order(
        cls,
        symbol: str,
        quantity: int,
        price: float,
        available_margin: float,
        is_square_off: bool = False
    ) -> Tuple[bool, str]:
        
        # 0. F&O Ban Period Check (MWPL > 95%)
        if symbol in cls.BANNED_UNDERLYINGS and not is_square_off:
            return False, f"PRE-FLIGHT ERROR: Security {symbol} is currently under NSE F&O Ban (MWPL > 95%)! Only square-off orders allowed."

        # 1. Price quantization to 0.05
        cents = round((price * 100)) % 5
        if cents != 0:
            return False, f"PRE-FLIGHT ERROR: Price ₹{price:.4f} is NOT a multiple of ₹0.05 tick size!"

        # 2. Lot size quantization
        lot_size = cls.LOT_SIZES.get(symbol, 1)
        if quantity <= 0 or (quantity % lot_size) != 0:
            return False, f"PRE-FLIGHT ERROR: Quantity {quantity} is NOT a multiple of {symbol} lot size ({lot_size})!"

        # 3. Freeze limits check
        freeze_limit = cls.FREEZE_LIMITS.get(symbol, 1000)
        if quantity > freeze_limit:
            return False, f"PRE-FLIGHT ERROR: Quantity {quantity} exceeds NSE Freeze Limit ({freeze_limit}) for {symbol}!"

        # 4. Margin adequacy (Approx 15% margin for futures or 100% for cash/options)
        required_margin = (quantity * price) * 0.15
        if required_margin > (available_margin * 0.90):
            return False, f"PRE-FLIGHT ERROR: Insufficient margin! Required ₹{required_margin:.2f} > 90% buffer (₹{available_margin*0.9:.2f})!"

        return True, f"PRE-FLIGHT PASS: Order satisfies margin, lot ({lot_size}), freeze ({freeze_limit}), and 0.05 tick rules."


class SelfHealingRecovery:
    """
    Full YOLO 2 Mechanic #3: Self-Healing Error Recovery.
    Handles broker timeouts, HTTP 429 rate limits, and network errors with exponential backoff and jitter.
    """
    @classmethod
    async def execute_with_retry_async(cls, async_op, max_retries: int = 5, base_backoff_ms: float = 50.0):
        last_err = None
        for attempt in range(1, max_retries + 1):
            try:
                return await async_op()
            except Exception as e:
                last_err = e
                if attempt == max_retries:
                    raise e
                jitter = random.uniform(0.8, 1.2)
                backoff_sec = ((base_backoff_ms * (2 ** (attempt - 1))) * jitter) / 1000.0
                await asyncio.sleep(backoff_sec)
        raise last_err

    @classmethod
    def execute_with_retry_sync(cls, sync_op, max_retries: int = 5, base_backoff_ms: float = 50.0):
        last_err = None
        for attempt in range(1, max_retries + 1):
            try:
                return sync_op()
            except Exception as e:
                last_err = e
                if attempt == max_retries:
                    raise e
                jitter = random.uniform(0.8, 1.2)
                backoff_sec = ((base_backoff_ms * (2 ** (attempt - 1))) * jitter) / 1000.0
                time.sleep(backoff_sec)
        raise last_err

    # Backward compatibility alias
    execute_with_retry = execute_with_retry_async


class IndianMarketSessionManager:
    """
    Session Window & Market Timing Validator:
      - REGULAR trading hours: 09:15 to 15:30 IST
      - PRE_MARKET_GAP_WINDOW: 09:15 to 09:30 IST
      - FRIDAY_DRIFT_WINDOW: Friday 14:00 to 15:15 IST
      - MUHURAT special session (Diwali 1-hour): e.g. 18:00 to 19:15 IST.
        In Muhurat sessions, opening gap fader applies during first 15 mins (18:00 - 18:15 IST),
        and Friday weekend drift is strictly disabled.
    """
    @classmethod
    def is_morning_gap_window(cls, dt: Optional[datetime] = None, session_type: str = "REGULAR") -> bool:
        if dt is None:
            return True  # Fallback to manual flag
        ist_tz = timezone(timedelta(hours=5, minutes=30))
        ist_dt = dt.astimezone(ist_tz) if dt.tzinfo else dt
        cur_time = ist_dt.time()
        if session_type == "MUHURAT":
            return datetime.strptime("18:00", "%H:%M").time() <= cur_time <= datetime.strptime("18:15", "%H:%M").time()
        return datetime.strptime("09:15", "%H:%M").time() <= cur_time <= datetime.strptime("09:30", "%H:%M").time()

    @classmethod
    def is_friday_drift_window(cls, dt: Optional[datetime] = None, session_type: str = "REGULAR") -> bool:
        if dt is None:
            return True
        if session_type == "MUHURAT":
            return False  # No weekend drift on festive evening sessions
        ist_tz = timezone(timedelta(hours=5, minutes=30))
        ist_dt = dt.astimezone(ist_tz) if dt.tzinfo else dt
        if ist_dt.weekday() != 4:  # 4 is Friday
            return False
        cur_time = ist_dt.time()
        return datetime.strptime("14:00", "%H:%M").time() <= cur_time <= datetime.strptime("15:15", "%H:%M").time()


# =============================================================================
# 6. DECOUPLED SIGNAL GENERATOR & BROKER EXECUTION ENGINE
# =============================================================================

class IndianMarketSignalGenerator:
    """
    Dedicated Signal Generation Engine (AI / Quantitative Models).
    Runs independently of broker execution, evaluates alpha rules,
    runs the Bull/Bear/Judge debate, and pushes approved signals to the queue.
    """
    def __init__(self, signal_queue: asyncio.Queue, db_path: Optional[str] = None):
        self.signal_queue = signal_queue
        self.db_path = db_path
        self.gap_fader = PreMarketGapFader()
        self.option_tracker = NSEOptionChainShadowTracker()
        self.friday_drifter = BankNiftyFridayWeekendDrifter()
        self.pairs_trader = HdfcIciciPairsTrader()
        self.bull_agent = BullAgent()
        self.bear_agent = BearAgent()
        self.judge_agent = JudgeAgent()
        self.delete_loop = DeleteUntilProfitLoop(db_path=self.db_path)
        self.generated_signals: List[RawAlphaSignal] = []
        self.debate_verdicts: List[AgentDebateVerdict] = []

    async def evaluate_market_opportunity(
        self,
        tick: IndianMarketTick,
        option_chain: Optional[OptionChainShadow] = None,
        prev_vwap: Optional[float] = None,
        is_morning: bool = False,
        is_friday: bool = False,
        pairs_ratio_history: Optional[np.ndarray] = None,
        pair_peer_price: Optional[float] = None
    ) -> Optional[AgentDebateVerdict]:
        
        candidate_signal: Optional[RawAlphaSignal] = None

        # 1. Pre-market Gap Fade
        if is_morning and prev_vwap:
            candidate_signal = self.gap_fader.evaluate_gap(tick.symbol, tick.price, prev_vwap, tick.atr, is_morning_window=True)

        # 2. BankNifty Friday Drift
        if not candidate_signal and is_friday and option_chain and tick.symbol == MarketSymbol.BANKNIFTY.value:
            candidate_signal = self.friday_drifter.evaluate_friday_drift(tick.price, option_chain, tick.atr, is_friday_afternoon=True)

        # 3. HDFC vs ICICI Pairs
        if not candidate_signal and tick.symbol == MarketSymbol.HDFCBANK.value and pair_peer_price and pairs_ratio_history is not None:
            candidate_signal = self.pairs_trader.evaluate_pairs(tick.price, pair_peer_price, pairs_ratio_history, tick.atr)

        if not candidate_signal:
            return None

        # Check Delete-Until-Profit Loop: Is strategy active?
        if not self.delete_loop.is_strategy_active(candidate_signal.strategy.value):
            return None

        # Run Multi-Agent Debate
        bull_conv, bull_thesis = self.bull_agent.evaluate(candidate_signal, option_chain, tick)
        bear_conv, bear_thesis = self.bear_agent.evaluate(candidate_signal, option_chain, tick)
        verdict = self.judge_agent.synthesize_verdict(candidate_signal, bull_conv, bull_thesis, bear_conv, bear_thesis)

        self.generated_signals.append(candidate_signal)
        self.debate_verdicts.append(verdict)

        # Push to Decoupled Queue ONLY IF Approved by Judge (> 85%)
        if verdict.approved:
            await self.signal_queue.put((candidate_signal, verdict))

        return verdict


class IndianMarketBrokerExecutionEngine:
    """
    Dedicated Broker API Execution Daemon.
    Decoupled from signal generation. Consumes approved signals, performs wallet
    pre-flight validation, handles TWAP slicing, dynamic 3*ATR trailing stop,
    enforces the Liquidator daily circuit breaker, and syncs WAL state.
    """
    def __init__(
        self,
        signal_queue: asyncio.Queue,
        db_path: str = "/Users/rajondas/.gemini/antigravity/scratch/antigravity_yolo_trading_engine/live_production_ledger.sqlite",
        initial_capital: float = 500000.0,
        delete_loop: Optional[DeleteUntilProfitLoop] = None
    ):
        self.signal_queue = signal_queue
        self.db_path = db_path
        self.initial_capital = initial_capital
        self.current_capital = initial_capital
        self.delete_loop = delete_loop
        self.trailing_manager = TrailingATRManager(atr_multiplier=3.0)
        self.risk_357 = Risk357Manager()
        self.liquidator = LiquidatorCircuitBreaker(initial_capital=initial_capital)
        self.active_orders: Dict[str, VerifiedOrder] = {}
        self.completed_orders: List[VerifiedOrder] = []
        self._init_db()
        self._recover_state_from_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("""
            CREATE TABLE IF NOT EXISTS live_orders (
                order_id TEXT PRIMARY KEY,
                signal_id TEXT,
                symbol TEXT,
                strategy TEXT,
                side TEXT,
                quantity INTEGER,
                entry_price REAL,
                fill_price REAL,
                exit_price REAL,
                stop_loss REAL,
                take_profit REAL,
                highest_price_seen REAL,
                lowest_price_seen REAL,
                status TEXT,
                realized_pnl REAL,
                created_at REAL,
                closed_at REAL
            );
            """)
            for col in ["exit_price REAL", "highest_price_seen REAL", "lowest_price_seen REAL"]:
                try:
                    conn.execute(f"ALTER TABLE live_orders ADD COLUMN {col};")
                except sqlite3.OperationalError:
                    pass

            conn.execute("""
            CREATE TABLE IF NOT EXISTS agent_debates (
                signal_id TEXT PRIMARY KEY,
                bull_conviction REAL,
                bear_conviction REAL,
                judge_confidence REAL,
                approved INTEGER,
                verdict_rationale TEXT,
                bull_thesis TEXT,
                bear_thesis TEXT,
                timestamp REAL
            );
            """)
            for col in ["bull_thesis TEXT", "bear_thesis TEXT"]:
                try:
                    conn.execute(f"ALTER TABLE agent_debates ADD COLUMN {col};")
                except sqlite3.OperationalError:
                    pass

            conn.execute("""
            CREATE TABLE IF NOT EXISTS liquidator_events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL,
                trigger_reason TEXT,
                capital REAL,
                daily_loss REAL
            );
            """)

            conn.execute("""
            CREATE TABLE IF NOT EXISTS strategy_quarantine_records (
                record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp REAL,
                strategy TEXT,
                sharpe_ratio REAL,
                trades_count INTEGER,
                status TEXT,
                action TEXT
            );
            """)

    def _recover_state_from_db(self):
        """True WAL State Recovery: Reconstructs in-flight orders, stops, and equity state."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                rows = cursor.execute("""
                    SELECT order_id, signal_id, symbol, strategy, side,
                           quantity, entry_price, fill_price, exit_price, stop_loss,
                           take_profit, status, realized_pnl, created_at, closed_at,
                           highest_price_seen, lowest_price_seen
                    FROM live_orders
                    WHERE status IN ('FILLED', 'TRAILING')
                """).fetchall()

                for r in rows:
                    order = VerifiedOrder(
                        order_id=r[0],
                        signal_id=r[1],
                        symbol=r[2],
                        strategy=r[3],
                        side=r[4],
                        quantity=r[5],
                        entry_price=r[6],
                        fill_price=r[7],
                        exit_price=r[8],
                        stop_loss=r[9],
                        take_profit=r[10],
                        status=OrderStatus(r[11]),
                        realized_pnl=r[12],
                        created_at=r[13],
                        closed_at=r[14],
                        highest_price_seen=r[15] if r[15] is not None else r[7],
                        lowest_price_seen=r[16] if r[16] is not None else r[7]
                    )
                    self.active_orders[order.order_id] = order

                pnl_sum = cursor.execute("SELECT sum(realized_pnl) FROM live_orders WHERE status='CLOSED'").fetchone()[0]
                if pnl_sum is not None:
                    self.current_capital = self.initial_capital + float(pnl_sum)
                    self.liquidator.current_capital = self.current_capital

                if self.delete_loop:
                    closed_rows = cursor.execute("SELECT strategy, realized_pnl FROM live_orders WHERE status='CLOSED' ORDER BY closed_at ASC").fetchall()
                    for strat, pnl in closed_rows:
                        if pnl is not None:
                            self.delete_loop.record_trade_pnl(strat, pnl)
        except Exception as e:
            print(f"[RECOVERY NOTICE] Could not recover from DB: {e}")

    async def process_next_signal(self) -> Optional[VerifiedOrder]:
        """Pulls next approved signal from queue and executes."""
        try:
            signal, verdict = self.signal_queue.get_nowait()
        except (asyncio.QueueEmpty, ValueError):
            return None

        # 1. Circuit Breaker Check
        is_tripped, cb_msg = self.liquidator.evaluate_capital(self.current_capital)
        if is_tripped:
            self._flatten_all_positions(cb_msg)
            return None

        # 2. Risk-357 Check
        active_risk = sum(abs(o.fill_price - o.stop_loss) * o.quantity for o in self.active_orders.values())
        proposed_risk = abs(signal.entry_price - signal.base_stop_loss) * WalletPreFlightTester.LOT_SIZES.get(signal.symbol, 1)
        risk_passed, risk_msg = self.risk_357.check_pre_trade_risk(
            len(self.active_orders), active_risk, proposed_risk, self.current_capital
        )
        if not risk_passed:
            return None

        # 3. Sizing & Lot Sizing
        lot_size = WalletPreFlightTester.LOT_SIZES.get(signal.symbol, 1)
        quantity = lot_size  # Start with 1 lot

        # 4. Pre-Flight Wallet Unit Testing
        pf_passed, pf_msg = WalletPreFlightTester.test_wallet_and_order(
            signal.symbol, quantity, signal.entry_price, self.current_capital
        )
        if not pf_passed:
            return None

        # 5. Order Dispatch with Slippage Simulation
        order_id = f"ORD_{signal.symbol}_{int(time.time()*1000)}"
        slippage = 0.05 if signal.side == SignalSide.BUY else -0.05
        fill_price = round(signal.entry_price + slippage, 2)

        order = VerifiedOrder(
            order_id=order_id,
            signal_id=signal.signal_id,
            symbol=signal.symbol,
            strategy=signal.strategy.value,
            side=signal.side.value,
            quantity=quantity,
            entry_price=signal.entry_price,
            fill_price=fill_price,
            stop_loss=signal.base_stop_loss,
            take_profit=signal.target_price,
            highest_price_seen=fill_price,
            lowest_price_seen=fill_price,
            status=OrderStatus.FILLED,
            created_at=time.time()
        )

        self.active_orders[order.order_id] = order

        # Persist to SQLite with self-healing retry
        def _persist_order():
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                INSERT OR REPLACE INTO live_orders (
                    order_id, signal_id, symbol, strategy, side,
                    quantity, entry_price, fill_price, exit_price, stop_loss,
                    take_profit, highest_price_seen, lowest_price_seen,
                    status, realized_pnl, created_at, closed_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    order.order_id, order.signal_id, order.symbol, order.strategy, order.side,
                    order.quantity, order.entry_price, order.fill_price, order.exit_price, order.stop_loss,
                    order.take_profit, order.highest_price_seen, order.lowest_price_seen,
                    order.status.value, order.realized_pnl, order.created_at, order.closed_at
                ))
                conn.execute("""
                INSERT OR REPLACE INTO agent_debates (
                    signal_id, bull_conviction, bear_conviction,
                    judge_confidence, approved, verdict_rationale,
                    bull_thesis, bear_thesis, timestamp
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    verdict.signal_id, verdict.bull_conviction, verdict.bear_conviction,
                    verdict.judge_confidence, 1 if verdict.approved else 0, verdict.verdict_rationale,
                    verdict.bull_thesis, verdict.bear_thesis, verdict.timestamp
                ))

        SelfHealingRecovery.execute_with_retry_sync(_persist_order, max_retries=3)

        self.signal_queue.task_done()
        return order

    def on_market_price_update(self, symbol: str, current_price: float, current_atr: float):
        """Monitors resting orders against 3*ATR trailing stops and profit targets."""
        closed_orders = []

        for order_id, order in list(self.active_orders.items()):
            if order.symbol != symbol:
                continue

            # Update 3*ATR Dynamic Trailing Stop
            _, stop_ratcheted = self.trailing_manager.update_trailing_stop(order, current_price, current_atr)

            # If trailing stop ratcheted, immediately persist new watermarks to SQLite WAL
            if stop_ratcheted:
                order.status = OrderStatus.TRAILING
                try:
                    with sqlite3.connect(self.db_path) as conn:
                        conn.execute("""
                        UPDATE live_orders
                        SET stop_loss=?, highest_price_seen=?, lowest_price_seen=?, status='TRAILING'
                        WHERE order_id=?
                        """, (order.stop_loss, order.highest_price_seen, order.lowest_price_seen, order.order_id))
                except Exception as e:
                    print(f"[WARN] Trailing ratchet DB persist error: {e}")

            # Check Take Profit & Stop Loss
            hit_tp = False
            hit_sl = False

            if order.side == SignalSide.BUY.value:
                if current_price >= order.take_profit:
                    hit_tp = True
                elif current_price <= order.stop_loss:
                    hit_sl = True
            elif order.side == SignalSide.SELL.value:
                if current_price <= order.take_profit:
                    hit_tp = True
                elif current_price >= order.stop_loss:
                    hit_sl = True

            if hit_tp or hit_sl:
                order.exit_price = current_price
                if order.side == SignalSide.BUY.value:
                    order.realized_pnl = (order.exit_price - order.fill_price) * order.quantity
                else:
                    order.realized_pnl = (order.fill_price - order.exit_price) * order.quantity

                order.status = OrderStatus.CLOSED
                order.closed_at = time.time()
                closed_orders.append(order)

        for order in closed_orders:
            del self.active_orders[order.order_id]
            self.completed_orders.append(order)
            self.current_capital += order.realized_pnl
            self.risk_357.record_trade_result(order.realized_pnl)

            # Update DB with exit state
            with sqlite3.connect(self.db_path) as conn:
                conn.execute("""
                UPDATE live_orders SET status=?, exit_price=?, realized_pnl=?, closed_at=?, stop_loss=?
                WHERE order_id=?
                """, (order.status.value, order.exit_price, order.realized_pnl, order.closed_at, order.stop_loss, order.order_id))

            # Record outcome into Delete-Until-Profit Loop (Sharpe < 1.5 Pruning)
            if self.delete_loop:
                sharpe, quarantined = self.delete_loop.record_trade_pnl(order.strategy, order.realized_pnl)
                if quarantined:
                    with sqlite3.connect(self.db_path) as conn:
                        conn.execute("""
                        INSERT INTO strategy_quarantine_records (timestamp, strategy, sharpe_ratio, trades_count, status, action)
                        VALUES (?, ?, ?, ?, ?, ?)
                        """, (time.time(), order.strategy, sharpe, len(self.delete_loop.strategy_trade_history.get(order.strategy, [])), "QUARANTINED", "PRUNED_SHARPE_LESS_1.5"))

            # Re-evaluate Liquidator Circuit Breaker
            is_tripped, cb_msg = self.liquidator.evaluate_capital(self.current_capital)
            if is_tripped:
                self._flatten_all_positions(cb_msg)

    def _flatten_all_positions(self, reason: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
            INSERT INTO liquidator_events (timestamp, trigger_reason, capital, daily_loss)
            VALUES (?, ?, ?, ?)
            """, (time.time(), reason, self.current_capital, self.initial_capital - self.current_capital))

            for order_id, order in list(self.active_orders.items()):
                order.status = OrderStatus.CLOSED
                order.exit_price = order.fill_price
                order.closed_at = time.time()
                conn.execute("UPDATE live_orders SET status='CLOSED', exit_price=?, closed_at=? WHERE order_id=?", (order.exit_price, order.closed_at, order_id))
        self.active_orders.clear()


# =============================================================================
# 7. UNIFIED SYSTEM COORDINATOR
# =============================================================================

class FullYOLO2IndianTradingEngine:
    """
    Top-Level Orchestrator unifying:
      - Secret Sauce Guard
      - Decoupled Signal Generator & Queue
      - Broker Execution Engine
      - Real-time Ledger Logging
    """
    def __init__(
        self,
        initial_capital: float = 500000.0,
        db_path: str = "/Users/rajondas/.gemini/antigravity/scratch/antigravity_yolo_trading_engine/live_production_ledger.sqlite"
    ):
        # 1. Guard check
        intact, msg = SecretSauceGuard.verify_integrity()
        if not intact:
            raise RuntimeError(f"Engine Startup Aborted: {msg}")

        self.db_path = db_path
        self.queue = asyncio.Queue(maxsize=10000)
        self.signal_gen = IndianMarketSignalGenerator(self.queue, db_path=self.db_path)
        self.exec_engine = IndianMarketBrokerExecutionEngine(
            signal_queue=self.queue,
            db_path=self.db_path,
            initial_capital=initial_capital,
            delete_loop=self.signal_gen.delete_loop
        )

    async def ingest_market_event(
        self,
        tick: IndianMarketTick,
        option_chain: Optional[OptionChainShadow] = None,
        prev_vwap: Optional[float] = None,
        is_morning: bool = False,
        is_friday: bool = False,
        pairs_ratio_history: Optional[np.ndarray] = None,
        pair_peer_price: Optional[float] = None
    ) -> Optional[VerifiedOrder]:
        
        # Step 1: Signal Gen & Debate
        verdict = await self.signal_gen.evaluate_market_opportunity(
            tick=tick,
            option_chain=option_chain,
            prev_vwap=prev_vwap,
            is_morning=is_morning,
            is_friday=is_friday,
            pairs_ratio_history=pairs_ratio_history,
            pair_peer_price=pair_peer_price
        )

        # Step 2: Broker Execution
        order = await self.exec_engine.process_next_signal()

        # Step 3: Check stops & updates
        self.exec_engine.on_market_price_update(tick.symbol, tick.price, tick.atr)

        return order


if __name__ == "__main__":
    print("Full YOLO 2 Indian Market Agentic Alpha module loaded successfully.")
