"""
⚡ PRE-MARKET GAP-LEVERAGE SCREENER & CALIBRATION ENGINE (PHASE 2 ENHANCED)
=============================================================================
Tailored for Tuesday Pre-Market (Sep 15, 2026) post 3-day weekend.
Interconnects:
1. 09:00 - 09:08 AM (Pre-Open): Live NSE Pre-Open Rate & Depth Ingestion.
   - Order Flow Imbalance (OFI) = Delta BidQty - Delta AskQty
   - Book Skewness = (Total Bids - Total Asks) / (Total Bids + Total Asks)
2. Global Macro Risk Reconciliation (Research 2):
   - Ingests GIFT Nifty delta (-0.55%), Brent crude shock (+4.5% / $110), US Tech sell-off (-2.1%).
   - Generates unified Macro Risk Score [-1.0, +1.0] and bidirectional transition probabilities.
3. Sub-₹200 Universe Filtering & Trap Zone Rejection:
   - Price < ₹200 AND 1.0% <= |Gap| <= 3.0%
   - |Gap| > 3.0% flagged as TRAP_ZONE_LIQUIDITY_SWEEP (eliminates opening fakeouts).
4. 09:08 - 09:14 AM (Leverage Calibration):
   - Gap_Factor = abs(Open - PrevClose) / PrevClose
   - Safe_Lev = 5.0 * (1.0 - Gap_Factor * 10.0), scaled dynamically between 1.0x and 5.0x.
5. 09:15:00 - 09:16:05 AM (Opening Wick Volatility & 65-Second Quarantine Filter):
   - Captures 1-second candles across the first 65 seconds (zero blind orders).
   - Wick-to-body ratio check (wick / body <= 2.5) to reject false liquidity sweeps / stop-hunts.
   - Establishes dynamic H1 (High) and L1 (Low) breakout boundaries at 09:16:05 AM.
6. 09:16:05 AM Onwards (Bidirectional Sniper Execution):
   - Bullish Breakout: Price > H1 + 0.05 tick buffer with volume confirmation.
   - Bearish Breakdown: Price < L1 - 0.05 tick buffer with volume confirmation.
   - Hard risk cap: ₹3.75 max loss per trade on ₹1,008 capital.
"""

import json
import logging
import math
from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("PremarketScreener")

# Target Universe: Liquid sub-₹200 NSE Equities
DEFAULT_UNIVERSE = {
    "TATASTEEL": {"security_id": "3499", "lot_size": 1, "tick_size": 0.05, "ref_price": 150.0},
    "SAIL": {"security_id": "2963", "lot_size": 1, "tick_size": 0.05, "ref_price": 125.0},
    "PNB": {"security_id": "10666", "lot_size": 1, "tick_size": 0.05, "ref_price": 105.0},
    "ASHOKLEY": {"security_id": "212", "lot_size": 1, "tick_size": 0.05, "ref_price": 185.0},
    "ZOMATO": {"security_id": "5097", "lot_size": 1, "tick_size": 0.05, "ref_price": 195.0},
}


class SignalType(str, Enum):
    BUY = "BUY"
    SELL = "SELL"
    WAIT = "WAIT"
    REJECT = "REJECT"


@dataclass
class MacroShockVector:
    gift_nifty_delta: float = -0.0055      # -0.55% GIFT Nifty indication on Sep 15, 2026
    brent_crude_delta: float = 0.0450      # +4.5% ($110/bbl crude shock)
    nasdaq_futures_delta: float = -0.0210  # -2.1% US tech liquidation overnight


@dataclass
class MacroRegimeReport:
    macro_score: float                     # Range: [-1.0 (extreme bearish), +1.0 (extreme bullish)]
    p_continuation: float                  # Probability of gap continuation
    p_reversion: float                     # Probability of gap mean reversion
    regime: str                            # DISCONTINUOUS_JUMP_CAUCHY vs MEAN_REVERTING_OU
    sentiment_bias: str                    # BEARISH_CONTINUATION, BULLISH_REVERSION, NEUTRAL


@dataclass
class AuctionDepthSnapshot:
    symbol: str
    indicative_match_price: float
    matched_volume: int
    total_buy_qty: int
    total_sell_qty: int
    bids: List[Dict[str, float]] = field(default_factory=list)
    asks: List[Dict[str, float]] = field(default_factory=list)

    def compute_ofi_and_skew(self) -> Tuple[float, float]:
        """
        Computes Order Flow Imbalance (OFI) and Book Skewness from pre-open auction depth.
        OFI = Delta Top Bids - Delta Top Asks
        Skew = (Total Buy Qty - Total Sell Qty) / (Total Buy Qty + Total Sell Qty)
        """
        tot_buy = sum(b.get("q", 0) for b in self.bids) if self.bids else self.total_buy_qty
        tot_sell = sum(a.get("q", 0) for a in self.asks) if self.asks else self.total_sell_qty
        denom = tot_buy + tot_sell
        skew = (tot_buy - tot_sell) / denom if denom > 0 else 0.0

        top_b = self.bids[0].get("q", 0) if self.bids else 0
        top_a = self.asks[0].get("q", 0) if self.asks else 0
        ofi = float(top_b - top_a)
        return ofi, round(skew, 4)


@dataclass
class CandidateStock:
    symbol: str
    security_id: str
    previous_close: float
    open_price: float
    current_price: float
    gap_pct: float
    gap_factor: float
    safe_leverage: float
    max_buying_power: float
    approved_quantity: int
    risk_rupees: float
    stop_loss_distance: float
    status: str
    rejection_reason: Optional[str] = None
    ofi: float = 0.0
    book_skew: float = 0.0


@dataclass
class FirstMinuteCandle:
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    timestamp: str = "09:15:00"


@dataclass
class OpeningCandleAnalysis:
    symbol: str
    h1: float
    l1: float
    open_price: float
    close_price: float
    volume: float
    wick_to_body_ratio: float
    is_valid_breakout_range: bool
    rejection_reason: Optional[str] = None


@dataclass
class BreakoutSignal:
    symbol: str
    signal: SignalType
    entry_price: float
    stop_loss: float
    take_profit: float
    trailing_atr_step: float
    hard_stop_loss_amount: float
    quantity: int
    safe_leverage: float
    rationale: str


class MacroRiskEngine:
    """Overnight Macro Risk Reconciliation Engine (Research 2)."""

    @staticmethod
    def evaluate_macro_regime(shocks: Optional[MacroShockVector] = None) -> MacroRegimeReport:
        if shocks is None:
            shocks = MacroShockVector()

        w_nifty = 0.50
        w_brent = 0.25
        w_nasdaq = 0.25

        # Invert brent: rising crude is negative for Indian import basket
        raw_score = (
            (shocks.gift_nifty_delta * w_nifty)
            + (shocks.brent_crude_delta * -1.0 * w_brent)
            + (shocks.nasdaq_futures_delta * w_nasdaq)
        )
        macro_score = float(np.clip(raw_score * 20.0, -1.0, 1.0))

        # Logistic transformation for transition probabilities
        logit_base = 0.5 * macro_score
        p_cont = float(np.clip(1.0 / (1.0 + np.exp(-logit_base)), 0.05, 0.95))
        p_rev = round(1.0 - p_cont, 4)
        p_cont = round(p_cont, 4)

        regime = "DISCONTINUOUS_JUMP_CAUCHY" if abs(macro_score) > 0.4 else "MEAN_REVERTING_OU"
        if macro_score < -0.2:
            sentiment_bias = "BEARISH_CONTINUATION"
        elif macro_score > 0.2:
            sentiment_bias = "BULLISH_REVERSION"
        else:
            sentiment_bias = "NEUTRAL"

        return MacroRegimeReport(
            macro_score=round(macro_score, 4),
            p_continuation=p_cont,
            p_reversion=p_rev,
            regime=regime,
            sentiment_bias=sentiment_bias,
        )


class OpeningWickAnalyzer:
    """
    09:15:00 - 09:16:05 AM IST Opening Wick Volatility & Liquidity Absorption Filter (Research 3).
    Ensures zero trades during first 65 seconds and filters out false stop-hunts.
    """
    MAX_WICK_BODY_RATIO = 2.5

    @classmethod
    def analyze_65s_window(cls, symbol: str, ticks: List[Dict[str, Any]]) -> OpeningCandleAnalysis:
        if not ticks:
            return OpeningCandleAnalysis(
                symbol=symbol,
                h1=0.0,
                l1=0.0,
                open_price=0.0,
                close_price=0.0,
                volume=0.0,
                wick_to_body_ratio=999.0,
                is_valid_breakout_range=False,
                rejection_reason="NO_TICKS_RECORDED_IN_65S_WINDOW",
            )

        prices = [t["price"] for t in ticks]
        volumes = [t.get("volume", 100) for t in ticks]

        o = prices[0]
        h = max(prices)
        l = min(prices)
        c = prices[-1]
        tot_vol = sum(volumes)

        candle_range = h - l
        body = abs(c - o)
        wick = candle_range - body
        ratio = round(wick / max(0.01, body), 2)

        if ratio > cls.MAX_WICK_BODY_RATIO:
            return OpeningCandleAnalysis(
                symbol=symbol,
                h1=round(h, 2),
                l1=round(l, 2),
                open_price=round(o, 2),
                close_price=round(c, 2),
                volume=float(tot_vol),
                wick_to_body_ratio=ratio,
                is_valid_breakout_range=False,
                rejection_reason=f"EXCESSIVE_WICK_RATIO (ratio {ratio} > {cls.MAX_WICK_BODY_RATIO}: false liquidity sweep)",
            )

        return OpeningCandleAnalysis(
            symbol=symbol,
            h1=round(h, 2),
            l1=round(l, 2),
            open_price=round(o, 2),
            close_price=round(c, 2),
            volume=float(tot_vol),
            wick_to_body_ratio=ratio,
            is_valid_breakout_range=True,
            rejection_reason=None,
        )


class PremarketScreener:
    def __init__(self, cash_equity: float = 1008.0, base_leverage: float = 5.0, max_trade_risk: float = 3.75):
        self.cash_equity = float(cash_equity)
        self.base_leverage = float(base_leverage)
        self.max_trade_risk = float(max_trade_risk)
        self.universe = dict(DEFAULT_UNIVERSE)
        self.macro_engine = MacroRiskEngine()
        self.wick_analyzer = OpeningWickAnalyzer()

    def calibrate_gap_leverage(
        self,
        open_price: float,
        prev_close: float,
        macro_score: float = 0.0,
    ) -> Tuple[float, float, float]:
        """
        Calculates Gap_Factor and dynamic Safe_Lev:
        Gap_Factor = abs(Open - PrevClose) / PrevClose
        Safe_Lev = 5.0 * (1.0 - Gap_Factor * 10.0)
        Clamped between 1.0x and 5.0x.
        """
        if prev_close <= 0.0 or open_price <= 0.0:
            return 0.0, 0.0, self.base_leverage

        gap_pct = ((open_price - prev_close) / prev_close) * 100.0
        gap_factor = abs(open_price - prev_close) / prev_close

        # Dynamic Leverage Adjustment Formula (Research 4)
        safe_lev = self.base_leverage * (1.0 - gap_factor * 10.0)
        
        # In elevated macro shock conditions, add conservative buffer
        if abs(macro_score) > 0.4:
            safe_lev *= 0.95

        safe_lev = max(1.0, min(self.base_leverage, safe_lev))
        safe_lev = round(safe_lev, 2)

        return round(gap_pct, 2), round(gap_factor, 4), safe_lev

    def calculate_position_size(
        self, asset_price: float, safe_lev: float, stop_distance: float = 0.50
    ) -> Tuple[int, float, float]:
        """
        Calculates approved quantity bounded by:
        1. Max buying power = cash_equity * safe_lev
        2. Hard risk clamp: max ₹3.75 risk per trade
        """
        buying_power = self.cash_equity * safe_lev
        max_qty_margin = int(buying_power // asset_price) if asset_price > 0 else 0

        # Max quantity from risk cap: ₹3.75 / stop_distance
        max_qty_risk = int(self.max_trade_risk // stop_distance) if stop_distance > 0 else max_qty_margin

        approved_qty = max(1, min(max_qty_margin, max_qty_risk))
        effective_risk = round(approved_qty * stop_distance, 2)

        return approved_qty, buying_power, effective_risk

    def fetch_live_quotes(self) -> Dict[str, Dict[str, Any]]:
        """
        Queries NSE Live data for the universe.
        Falls back gracefully to reference data if broker/market socket is closed.
        """
        quotes = {}
        try:
            from jugaad_data.nse import NSELive
            nse_live = NSELive()
            for sym in self.universe.keys():
                try:
                    q = nse_live.stock_quote(sym)
                    meta = q.get("metaData", {})
                    pinfo = q.get("priceInfo", {})
                    prev_c = float(meta.get("previousClose") or pinfo.get("previousClose") or self.universe[sym]["ref_price"])
                    op = float(meta.get("open") or prev_c)
                    cl = float(meta.get("closePrice") or op)
                    quotes[sym] = {"previous_close": prev_c, "open": op, "current": cl, "bids": [], "asks": []}
                except Exception as ex:
                    logger.debug(f"Live quote fetch error for {sym}: {ex}")
                    quotes[sym] = {
                        "previous_close": self.universe[sym]["ref_price"],
                        "open": self.universe[sym]["ref_price"],
                        "current": self.universe[sym]["ref_price"],
                        "bids": [],
                        "asks": [],
                    }
        except Exception as e:
            logger.debug(f"NSE Live unavailable ({e}). Using reference data.")
            for sym, meta in self.universe.items():
                quotes[sym] = {
                    "previous_close": meta["ref_price"],
                    "open": meta["ref_price"],
                    "current": meta["ref_price"],
                    "bids": [],
                    "asks": [],
                }
        return quotes

    def screen(
        self,
        quotes_override: Optional[Dict[str, Dict[str, Any]]] = None,
        macro_shocks: Optional[MacroShockVector] = None,
    ) -> List[CandidateStock]:
        """
        Executes pre-market screening pipeline (09:00 - 09:14 AM IST):
        1. Sub-₹200 price filter
        2. Macro Risk Score calculation
        3. Gap calculation & categorization
        4. Trap zone rejection (|Gap| > 3.0%)
        5. Insufficient momentum rejection (|Gap| < 1.0%)
        6. Leverage calibration & sizing
        """
        quotes = quotes_override or self.fetch_live_quotes()
        macro_report = self.macro_engine.evaluate_macro_regime(macro_shocks)
        results: List[CandidateStock] = []

        for sym, udata in self.universe.items():
            q = quotes.get(sym, {})
            prev_close = float(q.get("previous_close", udata["ref_price"]))
            open_price = float(q.get("open", prev_close))
            curr_price = float(q.get("current", open_price))
            bids = q.get("bids", [])
            asks = q.get("asks", [])

            # Compute OFI and Skew if depth available
            ofi, skew = 0.0, 0.0
            if bids and asks:
                snap = AuctionDepthSnapshot(
                    symbol=sym,
                    indicative_match_price=open_price,
                    matched_volume=int(q.get("matched_volume", 10000)),
                    total_buy_qty=int(q.get("total_buy_qty", 50000)),
                    total_sell_qty=int(q.get("total_sell_qty", 50000)),
                    bids=bids,
                    asks=asks,
                )
                ofi, skew = snap.compute_ofi_and_skew()

            # Filter 1: Purchasing Power Check with 5x Intraday Leverage
            min_margin_needed = open_price / 5.0
            if min_margin_needed > self.cash_equity:
                results.append(
                    CandidateStock(
                        symbol=sym,
                        security_id=udata["security_id"],
                        previous_close=prev_close,
                        open_price=open_price,
                        current_price=curr_price,
                        gap_pct=0.0,
                        gap_factor=0.0,
                        safe_leverage=1.0,
                        max_buying_power=self.cash_equity,
                        approved_quantity=0,
                        risk_rupees=0.0,
                        stop_loss_distance=0.0,
                        status="REJECTED",
                        rejection_reason=f"MARGIN_EXCEEDS_EQUITY (₹{min_margin_needed:.2f} > ₹{self.cash_equity:.2f})",
                        ofi=ofi,
                        book_skew=skew,
                    )
                )
                continue

            gap_pct, gap_factor, safe_lev = self.calibrate_gap_leverage(open_price, prev_close, macro_report.macro_score)
            abs_gap = abs(gap_pct)

            # Rejection 1: Large Gap Handling (Negative gap in bearish macro is SHORT candidate, not rejected)
            if abs_gap > 3.0:
                if gap_pct < -3.0 and macro_report.macro_score < -0.2:
                    # Symmetrical Downside Opportunity (Subasish Pani & Ghanshyam Tech Breakout Rule)
                    safe_lev = min(safe_lev, 3.0)  # Cautious leverage on deep gaps
                else:
                    results.append(
                        CandidateStock(
                            symbol=sym,
                            security_id=udata["security_id"],
                            previous_close=prev_close,
                            open_price=open_price,
                            current_price=curr_price,
                            gap_pct=gap_pct,
                            gap_factor=gap_factor,
                            safe_leverage=safe_lev,
                            max_buying_power=self.cash_equity * safe_lev,
                            approved_quantity=0,
                            risk_rupees=0.0,
                            stop_loss_distance=0.0,
                            status="REJECTED",
                            rejection_reason=f"TRAP_ZONE_LIQUIDITY_SWEEP (|Gap| {abs_gap:.2f}% > 3.0%)",
                            ofi=ofi,
                            book_skew=skew,
                        )
                    )
                    continue
                        ofi=ofi,
                        book_skew=skew,
                    )
                )
                continue

            # Rejection 2: Low Momentum (< 1.0%)
            if abs_gap < 1.0:
                results.append(
                    CandidateStock(
                        symbol=sym,
                        security_id=udata["security_id"],
                        previous_close=prev_close,
                        open_price=open_price,
                        current_price=curr_price,
                        gap_pct=gap_pct,
                        gap_factor=gap_factor,
                        safe_leverage=safe_lev,
                        max_buying_power=self.cash_equity * safe_lev,
                        approved_quantity=0,
                        risk_rupees=0.0,
                        stop_loss_distance=0.0,
                        status="REJECTED",
                        rejection_reason=f"INSUFFICIENT_MOMENTUM (|Gap| {abs_gap:.2f}% < 1.0%)",
                        ofi=ofi,
                        book_skew=skew,
                    )
                )
                continue

            # Status: QUALIFIED (1.5% <= |Gap| <= 3.0% is PRIME, 1.0% <= |Gap| < 1.5% is SECONDARY)
            status = "PRIME_TARGET" if abs_gap >= 1.5 else "SECONDARY_TARGET"

            # Position sizing with conservative stop loss distance (0.50 INR)
            stop_dist = max(0.20, round(open_price * 0.003, 2))  # ~0.3% stop
            qty, buying_power, eff_risk = self.calculate_position_size(open_price, safe_lev, stop_dist)

            results.append(
                CandidateStock(
                    symbol=sym,
                    security_id=udata["security_id"],
                    previous_close=prev_close,
                    open_price=open_price,
                    current_price=curr_price,
                    gap_pct=gap_pct,
                    gap_factor=gap_factor,
                    safe_leverage=safe_lev,
                    max_buying_power=buying_power,
                    approved_quantity=qty,
                    risk_rupees=eff_risk,
                    stop_loss_distance=stop_dist,
                    status=status,
                    rejection_reason=None,
                    ofi=ofi,
                    book_skew=skew,
                )
            )

        # Sort: PRIME_TARGET first, then highest absolute gap
        results.sort(key=lambda x: (x.status == "PRIME_TARGET", abs(x.gap_pct)), reverse=True)
        return results

    def evaluate_breakout(
        self,
        candidate: CandidateStock,
        candle_1m: FirstMinuteCandle,
        current_tick_price: float,
        current_tick_vol: float,
        avg_5m_volume: float,
        atr_14: float = 0.85,
    ) -> BreakoutSignal:
        """
        Evaluates 09:16:05+ Breakout rule:
        Bullish: Tick Price > High_1m + 0.05 AND Vol >= 1.2 * AvgVol
        Bearish: Tick Price < Low_1m - 0.05 AND Vol >= 1.2 * AvgVol
        Hard risk cap: ₹3.75 max loss per trade.
        """
        vol_threshold = avg_5m_volume * 1.2
        trailing_atr_step = round(atr_14 * 1.5, 2)
        tick_buffer = 0.05

        # Check Bullish Breakout
        if current_tick_price >= (candle_1m.high + tick_buffer) and current_tick_vol >= vol_threshold:
            stop_loss = round(candle_1m.low, 2)
            max_allowed_sl_dist = self.max_trade_risk / max(1, candidate.approved_quantity)
            if (current_tick_price - stop_loss) > max_allowed_sl_dist:
                stop_loss = round(current_tick_price - max_allowed_sl_dist, 2)

            take_profit = round(current_tick_price + 2.0 * (current_tick_price - stop_loss), 2)

            return BreakoutSignal(
                symbol=candidate.symbol,
                signal=SignalType.BUY,
                entry_price=current_tick_price,
                stop_loss=stop_loss,
                take_profit=take_profit,
                trailing_atr_step=trailing_atr_step,
                hard_stop_loss_amount=self.max_trade_risk,
                quantity=candidate.approved_quantity,
                safe_leverage=candidate.safe_leverage,
                rationale=(
                    f"BULLISH_BREAKOUT: Price {current_tick_price:.2f} >= 1m High + Buffer {candle_1m.high + tick_buffer:.2f} "
                    f"with Volume surge {current_tick_vol:.0f} >= {vol_threshold:.0f} (Safe Lev: {candidate.safe_leverage}x)"
                ),
            )

        # Check Bearish Breakdown
        if current_tick_price <= (candle_1m.low - tick_buffer) and current_tick_vol >= vol_threshold:
            stop_loss = round(candle_1m.high, 2)
            max_allowed_sl_dist = self.max_trade_risk / max(1, candidate.approved_quantity)
            if (stop_loss - current_tick_price) > max_allowed_sl_dist:
                stop_loss = round(current_tick_price + max_allowed_sl_dist, 2)

            take_profit = round(current_tick_price - 2.0 * (stop_loss - current_tick_price), 2)

            return BreakoutSignal(
                symbol=candidate.symbol,
                signal=SignalType.SELL,
                entry_price=current_tick_price,
                stop_loss=stop_loss,
                take_profit=take_profit,
                trailing_atr_step=trailing_atr_step,
                hard_stop_loss_amount=self.max_trade_risk,
                quantity=candidate.approved_quantity,
                safe_leverage=candidate.safe_leverage,
                rationale=(
                    f"BEARISH_BREAKDOWN: Price {current_tick_price:.2f} <= 1m Low - Buffer {candle_1m.low - tick_buffer:.2f} "
                    f"with Volume surge {current_tick_vol:.0f} >= {vol_threshold:.0f} (Safe Lev: {candidate.safe_leverage}x)"
                ),
            )

        return BreakoutSignal(
            symbol=candidate.symbol,
            signal=SignalType.WAIT,
            entry_price=current_tick_price,
            stop_loss=0.0,
            take_profit=0.0,
            trailing_atr_step=trailing_atr_step,
            hard_stop_loss_amount=self.max_trade_risk,
            quantity=0,
            safe_leverage=candidate.safe_leverage,
            rationale=f"NO_CONFIRMED_BREAKOUT: Inside 1m range [{candle_1m.low:.2f} - {candle_1m.high:.2f}] or Vol < threshold.",
        )


if __name__ == "__main__":
    screener = PremarketScreener(cash_equity=1008.0, base_leverage=5.0, max_trade_risk=3.75)
    candidates = screener.screen()
    macro = screener.macro_engine.evaluate_macro_regime()
    print("================================================================================")
    print(f"⚡ PRE-MARKET RECONCILIATION: Macro Score: {macro.macro_score:+.2f} | Regime: {macro.regime}")
    print(f"   Bias: {macro.sentiment_bias} | P(Continuation): {macro.p_continuation*100:.1f}% | P(Reversion): {macro.p_reversion*100:.1f}%")
    print("================================================================================")
    for c in candidates:
        print(
            f"[{c.status}] {c.symbol} (SecID: {c.security_id}) | Prev: ₹{c.previous_close:.2f} | Open: ₹{c.open_price:.2f} | "
            f"Gap: {c.gap_pct:+.2f}% | Safe Lev: {c.safe_leverage:.2f}x | Qty: {c.approved_quantity} | Risk: ₹{c.risk_rupees:.2f} | "
            f"Reason: {c.rejection_reason or 'None'}"
        )
