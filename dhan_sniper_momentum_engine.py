"""
⚡ DHAN SNIPER MOMENTUM & COMPOUNDING ENGINE (PHASE 2 PRODUCTION)
=================================================================
Implements the 4-Hour Micro-Capital "Sniper Triangle" Compounding Protocol:
- Target: Double ₹1,008 cash equity to ₹2,016 - ₹2,538 via 5x MIS leverage.
- 3-Stage Asymmetric 1:2 R:R Progression:
    * Stage 1: Capital ₹1,008 | Risk ₹200 | Target ₹400 | Balance -> ₹1,358
    * Stage 2: Capital ₹1,358 | Risk ₹270 | Target ₹540 | Balance -> ₹1,848
    * Stage 3: Capital ₹1,848 | Risk ₹370 | Target ₹740 | Balance -> ₹2,538
- Dynamic ATR-based ratcheting trailing stop-loss.
- Hard 20% drawdown circuit breaker (halts if daily loss >= ₹200).
- Auto square-off at 03:10 PM IST (zero broker RMS penalty).
- Interconnected with:
    * Native Apple Silicon M1 Zig NEON Variance Shield (`libvariance_shield.dylib`)
    * 3-Gate Variance Shield (`risk_gatekeeper.py`)
    * SQLite WAL Tick Pipeline (`data_engine.py`)
    * Forced-IPv4 Token-Bucket Broker Bridge (`dhan_live_bridge.py`)
"""

import datetime
import logging
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from data_engine import DataEngine
from dhan_live_bridge import DhanLiveBridge
from premarket_screener import CandidateStock, PremarketScreener
from risk_gatekeeper import RiskConfig, RiskGatekeeper

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SniperMomentumEngine")

# Genuine YouTube NotebookLM Consensus Universe (17 Sept 2026 Morning Analysts Picks)
SNIPER_UNIVERSE = {
    "YESBANK": {"security_id": "11915", "lot_size": 1, "tick_size": 0.05, "ref_price": 22.50, "theme": "UPI_MDR_CATALYST"},
    "ITC": {"security_id": "1660", "lot_size": 1, "tick_size": 0.05, "ref_price": 264.50, "theme": "DEFENSIVE_FMCG_SUPPORT"},
    "COLPAL": {"security_id": "15141", "lot_size": 1, "tick_size": 0.05, "ref_price": 1850.00, "theme": "FMCG_OUTPERFORMER"},
    "HDFCBANK": {"security_id": "1333", "lot_size": 1, "tick_size": 0.05, "ref_price": 732.00, "theme": "PRIVATE_BANK_CONSENSUS"},
    "SBIN": {"security_id": "3045", "lot_size": 1, "tick_size": 0.05, "ref_price": 800.00, "theme": "PSU_BANK_DIP_BUY"},
    "RBLBANK": {"security_id": "18391", "lot_size": 1, "tick_size": 0.05, "ref_price": 403.00, "theme": "MOMENTUM_BREAKOUT"},
    "TATASTEEL": {"security_id": "3499", "lot_size": 1, "tick_size": 0.05, "ref_price": 183.00, "theme": "CONTRA_VALUE_SUPPORT"},
    "PNB": {"security_id": "10666", "lot_size": 1, "tick_size": 0.05, "ref_price": 116.80, "theme": "PSU_BANK_EXPANSION"},
    "M&M": {"security_id": "2031", "lot_size": 1, "tick_size": 0.05, "ref_price": 3100.00, "theme": "AUTO_PAIR_BUY"},
    "TVSMOTOR": {"security_id": "8479", "lot_size": 1, "tick_size": 0.05, "ref_price": 2450.00, "theme": "AUTO_PAIR_SELL"},
    "TCS": {"security_id": "11536", "lot_size": 1, "tick_size": 0.05, "ref_price": 2190.00, "theme": "IT_SELL_ON_RISE"},
    "TECHM": {"security_id": "13538", "lot_size": 1, "tick_size": 0.05, "ref_price": 1410.00, "theme": "IT_BEARISH_MARUBOZU"},
}


@dataclass
class SniperStageState:
    stage_id: int               # 1, 2, or 3
    starting_equity: float      # e.g., 1008.0
    current_equity: float       # dynamically tracked
    risk_budget: float          # 20% of starting equity
    target_profit: float        # 40% gain (1:2 R:R)
    target_equity: float        # target balance to graduate
    trades_executed: int
    wins: int
    losses: int
    is_completed: bool


class DhanSniperMomentumEngine:
    def __init__(
        self,
        initial_capital: float = 1008.0,
        db_path: str = "micro_canary_1k_ledger.sqlite",
        tick_db_path: str = "micro_capital_live.db",
        dry_run: bool = True,
    ):
        self.initial_capital = initial_capital
        self.current_equity = initial_capital
        self.daily_loss = 0.0
        self.max_daily_loss = min(50.0, round(initial_capital * 0.055, 2))  # Strict Gate 2: ₹50.00 hard circuit breaker
        self.dry_run = dry_run
        self.db_path = db_path
        self.tick_db_path = tick_db_path

        # Components
        self.data_engine = DataEngine(db_path=self.tick_db_path)
        self.bridge = DhanLiveBridge(dry_run=self.dry_run)
        trade_risk = min(22.96, round(self.current_equity * 0.025, 2))  # Gate 1: 2.5% Half-Kelly
        self.risk_config = RiskConfig(
            max_capital=self.current_equity,
            single_trade_risk_limit=trade_risk,
            daily_loss_limit=self.max_daily_loss,
            max_spread_pct=0.15,
            max_variance=2.5,
        )
        self.gatekeeper = RiskGatekeeper(
            config=self.risk_config,
            account_equity=self.current_equity,
            base_risk_unit=trade_risk,
        )

        # Stage Setup (The Sniper Triangle - 2.5% Half-Kelly Sizing)
        self.stage_definitions = [
            {"stage": 1, "target_gain": round(trade_risk * 2.0, 2), "risk": trade_risk, "next_eq": round(self.current_equity + trade_risk * 2.0, 2)},
            {"stage": 2, "target_gain": round(trade_risk * 2.2, 2), "risk": round(trade_risk * 1.1, 2), "next_eq": round(self.current_equity + trade_risk * 4.2, 2)},
            {"stage": 3, "target_gain": round(trade_risk * 2.5, 2), "risk": round(trade_risk * 1.25, 2), "next_eq": round(self.current_equity + trade_risk * 6.7, 2)},
        ]
        self.current_stage_idx = 0
        self.active_stage = self._init_stage(0)
        self.max_concurrent_positions = 3
        self.active_positions: dict[str, dict[str, Any]] = {}
        self.circuit_breaker_tripped = False

        # Phase 2 Pre-Market Screener & Gap-Leverage Engine
        self.screener = PremarketScreener(cash_equity=self.current_equity, base_leverage=5.0, max_trade_risk=trade_risk)
        self.premarket_candidates: dict[str, CandidateStock] = {}

        self._init_ledger_db()

    @property
    def active_position(self) -> dict[str, Any] | None:
        """Backward-compatible single active position view."""
        if self.active_positions:
            return next(iter(self.active_positions.values()))
        return None

    @active_position.setter
    def active_position(self, pos: dict[str, Any] | None):
        if pos is None:
            self.active_positions.clear()
        elif isinstance(pos, dict) and "symbol" in pos:
            self.active_positions[pos["symbol"]] = pos

    def sync_broker_equity(self):
        """Synchronizes internal equity and loss metrics directly with DhanHQ broker truth."""
        if self.bridge and self.bridge.is_connected and not self.dry_run and self.bridge.dhan:
            try:
                funds = self.bridge.dhan.get_fund_limits()
                if funds and funds.get("status") == "success":
                    data = funds.get("data", {})
                    avail = float(data.get("availabelBalance", 0.0))
                    util = float(data.get("utilizedAmount", 0.0))
                    sod = float(data.get("sodLimit", self.initial_capital))
                    real_equity = round(avail + util, 2)
                    if real_equity > 0:
                        self.current_equity = real_equity
                        self.daily_loss = max(0.0, round(sod - real_equity, 2))
                        self.active_stage.current_equity = self.current_equity

                # Position reconciliation with Dhan Broker Truth
                pos_resp = self.bridge.dhan.get_positions()
                if pos_resp and pos_resp.get("status") == "success":
                    broker_positions = {p.get("tradingSymbol"): p for p in pos_resp.get("data", [])}
                    for sym in list(self.active_positions.keys()):
                        bp = broker_positions.get(sym)
                        if not bp or bp.get("netQty", 0) == 0:
                            logger.info(f"Reconciling closed/rejected position for {sym} (Net Qty on Dhan = 0)")
                            del self.active_positions[sym]
            except Exception as e:
                logger.debug(f"Failed to sync broker equity: {e}")


    def run_premarket_screening(self, quotes_override: dict[str, dict[str, float]] | None = None) -> list[CandidateStock]:
        """
        Executes pre-market screening (09:00 - 09:14 AM IST):
        - Sub-₹200 price filter
        - 1.5% <= |Gap| <= 3.0% qualification
        - Dynamic Gap-Leverage calibration: Safe_Lev = 5.0 * (1 - Gap_Factor * 10)
        - Trap zone rejection (|Gap| > 3.0%)
        """
        candidates = self.screener.screen(quotes_override=quotes_override)
        self.premarket_candidates = {c.symbol: c for c in candidates}
        logger.info(f"📊 Pre-Market Screening Complete. Total Scanned: {len(candidates)} | Qualified: {sum(1 for c in candidates if 'TARGET' in c.status)}")
        for c in candidates:
            if "TARGET" in c.status:
                logger.info(f"  ⭐ QUALIFIED: {c.symbol} | Gap: {c.gap_pct:+.2f}% | Safe Lev: {c.safe_leverage:.2f}x | Qty: {c.approved_quantity} | Risk: ₹{c.risk_rupees:.2f}")
            else:
                logger.debug(f"  ❌ REJECTED: {c.symbol} | Reason: {c.rejection_reason}")
        return candidates

    def _init_stage(self, idx: int) -> SniperStageState:
        defn = self.stage_definitions[idx]
        return SniperStageState(
            stage_id=defn["stage"],
            starting_equity=self.current_equity,
            current_equity=self.current_equity,
            risk_budget=defn["risk"],
            target_profit=defn["target_gain"],
            target_equity=defn["next_eq"],
            trades_executed=0,
            wins=0,
            losses=0,
            is_completed=False,
        )

    def _init_ledger_db(self):
        """Initializes SQLite WAL ledger for deterministic pre/post commit tracking."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA synchronous=NORMAL;")
            conn.execute("""
                CREATE TABLE IF NOT EXISTS sniper_trades (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cl_ord_id TEXT UNIQUE,
                    timestamp REAL,
                    stage INTEGER,
                    symbol TEXT,
                    side TEXT,
                    quantity INTEGER,
                    entry_price REAL,
                    stop_loss REAL,
                    take_profit REAL,
                    exit_price REAL,
                    realized_pnl REAL,
                    status TEXT,
                    execution_mode TEXT
                )
            """)
            conn.commit()

    def is_square_off_time(self) -> bool:
        """Enforce 03:10 PM IST hard square-off rule to bypass Dhan RMS penalty."""
        now_ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
        cutoff = now_ist.replace(hour=15, minute=10, second=0, microsecond=0)
        return now_ist >= cutoff

    def is_market_open_for_entry(self) -> bool:
        """Enforces opening buffer (09:16:05 IST) and square-off cutoff (15:10:00 IST)."""
        now_ist = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
        if now_ist.weekday() >= 5:
            return False
        entry_start = now_ist.replace(hour=9, minute=16, second=5, microsecond=0)
        cutoff = now_ist.replace(hour=15, minute=10, second=0, microsecond=0)
        return entry_start <= now_ist < cutoff

    async def evaluate_tick_stream(
        self,
        symbol: str,
        price: float,
        bid: float,
        ask: float,
        volume: float = 100.0,
        side: str = "BUY",
    ) -> dict[str, Any] | None:
        """
        Processes an incoming live tick stream:
        1. Ingests tick into SQLite WAL.
        2. Checks circuit breaker and square-off rules.
        3. Updates active trailing stop-loss if position is open.
        4. Evaluates 3-Gate Variance Shield if seeking new entry.
        5. Dispatches dry-run or live order.
        """
        # Ingest tick
        self.data_engine.append_tick(symbol, price, bid, ask, volume)

        # 1. Circuit Breaker Check
        if self.daily_loss >= self.max_daily_loss:
            if not self.circuit_breaker_tripped:
                logger.error(f"🛑 CIRCUIT BREAKER TRIPPED! Daily loss ₹{self.daily_loss:.2f} >= ₹{self.max_daily_loss:.2f}. System Locked Down.")
                self.circuit_breaker_tripped = True
            return {"status": "HALTED", "reason": "CIRCUIT_BREAKER_ACTIVE"}

        # 2. Hard Square-off Check
        if self.is_square_off_time():
            results = []
            for sym in list(self.active_positions.keys()):
                logger.warning(f"⏰ 03:10 PM Cutoff Hit: Executing Auto-Square-Off for {sym} to protect capital.")
                res = await self.close_position(price, symbol=sym, reason="TIME_CUTOFF_0310_PM")
                results.append(res)
            if results:
                return {"status": "INACTIVE", "reason": "POST_MARKET_HOURS", "closed": results}
            return {"status": "INACTIVE", "reason": "POST_MARKET_HOURS"}

        # 3. Active Position Management (Ratcheting Trailing SL for this symbol)
        if symbol in self.active_positions:
            return await self._manage_active_position(price, symbol=symbol)

        # 4. New Entry Evaluation (Concurrent Multi-Slot Engine up to 3 slots)
        if len(self.active_positions) < self.max_concurrent_positions and not self.circuit_breaker_tripped:
            if not self.is_market_open_for_entry():
                return {"status": "WAITING_FOR_MARKET_OPEN", "reason": "Pre-market / Zero-order opening buffer active"}
            return await self._check_entry_opportunity(symbol, price, bid, ask, side=side)

        return None

    async def _check_entry_opportunity(
        self,
        symbol: str,
        price: float,
        bid: float,
        ask: float,
        side: str = "BUY",
    ) -> dict[str, Any] | None:
        """Evaluates entry conditions against 3-Gate Variance Shield and concurrent slot capacity."""
        if symbol in self.active_positions:
            return None

        # Capacity Gate: Bound to max_concurrent_positions
        if len(self.active_positions) >= self.max_concurrent_positions:
            logger.debug(f"Max concurrent positions ({self.max_concurrent_positions}) reached. Skipping {symbol}.")
            return None

        # Sanity check on tick price
        if price <= 0.0 or price > 50000.0:
            logger.warning(f"Rejecting abnormal tick for {symbol}: ₹{price}")
            return None

        # Sector Diversification Gate: Prevent holding 2 correlated stocks from same industry
        sector_map = {
            "TATASTEEL": "METALS", "SAIL": "METALS", "NATIONALUM": "METALS",
            "ASHOKLEY": "AUTO",
            "PNB": "BANKING", "IDFCFIRSTB": "BANKING",
            "IRFC": "RAILWAY_PSU",
            "SUZLON": "POWER_GREEN",
            "BHEL": "CAP_GOODS_PSU", "NBCC": "REALTY_PSU",
            "ZENSARTECH": "IT", "HCLTECH": "IT"
        }
        sym_sector = sector_map.get(symbol, "GENERAL")
        active_sectors = [sector_map.get(s, "GENERAL") for s in self.active_positions.keys()]
        if sym_sector in active_sectors:
            logger.debug(f"Sector {sym_sector} already represented in active positions ({list(self.active_positions.keys())}). Skipping.")
            return None

        # 1:2 Risk-Reward Setup: 0.5% risk (SL), 1.0% target (TP)
        sl_distance = round(price * 0.005, 2)
        tp_distance = round(price * 0.010, 2)
        order_side = side.upper()
        if order_side == "BUY":
            stop_loss = round(price - sl_distance, 2)
            take_profit = round(price + tp_distance, 2)
        else:
            stop_loss = round(price + sl_distance, 2)
            take_profit = round(price - tp_distance, 2)

        # Retrieve recent ticks for rolling variance
        ticks_df = self.data_engine.get_recent_ticks_df(symbol, limit=20)
        
        # 3-Gate Variance Shield Evaluation
        gates_passed = self.gatekeeper.verify_3_gates(
            price_df=ticks_df,
            asset_price=price,
            bid=bid,
            ask=ask,
            stop_loss=stop_loss,
            side=order_side,
        )

        if not gates_passed:
            logger.debug(f"Risk Gates VETO for {symbol} ({order_side}) @ ₹{price}")
            return None

        # Position Sizing: Bound by remaining loss budget, slot allocation, and 5x MIS leverage
        remaining_loss_budget = max(0.0, self.max_daily_loss - self.daily_loss)
        if remaining_loss_budget <= 1.0:
            logger.warning(f"Remaining daily loss budget (₹{remaining_loss_budget:.2f}) too small. Skipping entry.")
            return None

        candidate = self.premarket_candidates.get(symbol)
        effective_leverage = candidate.safe_leverage if candidate else 5.0

        # Sync live Dhan funds
        self.sync_broker_equity()
        live_avail_cash = self.current_equity
        if self.bridge.is_connected and not self.dry_run and self.bridge.dhan:
            try:
                fund_limits = self.bridge.dhan.get_fund_limits()
                if fund_limits and fund_limits.get("status") == "success":
                    live_avail_cash = float(fund_limits.get("data", {}).get("availabelBalance", self.current_equity))
            except Exception:
                pass

        free_slots = max(1, self.max_concurrent_positions - len(self.active_positions))
        cash_per_slot = (live_avail_cash * 0.90) / free_slots
        max_margin = cash_per_slot * effective_leverage
        shares_by_margin = int(max_margin / price)
        
        # Sizing scaled per slot
        base_stage_risk = 25.00 if self.active_stage.stage_id == 1 else min(self.active_stage.risk_budget * 5.0, 50.0)
        slot_risk = base_stage_risk / self.max_concurrent_positions
        effective_risk_budget = min(slot_risk, remaining_loss_budget / free_slots)
        shares_by_risk = int(effective_risk_budget / max(sl_distance, 0.05))
        quantity = max(1, min(shares_by_risk, shares_by_margin))

        # Re-check that total possible loss does not exceed remaining budget
        if (quantity * sl_distance) > (remaining_loss_budget + 5.0):
            quantity = max(1, int(remaining_loss_budget / sl_distance))
            if quantity < 1:
                return None

        logger.info(f"🎯 SNIPER TRIGGER: {symbol} Passed 3 Gates! Stage: {self.active_stage.stage_id} | Side: {order_side} | Qty: {quantity} | Entry: ₹{price} | SL: ₹{stop_loss} | TP: ₹{take_profit} | Open Slots: {len(self.active_positions)+1}/{self.max_concurrent_positions}")

        # Limit-Market Hybrid Order: Cap slippage to ±0.3% to avoid 0-DTE expiry spikes while guaranteeing execution (Strict NSE 0.05 Tick Size)
        raw_limit = price * 1.003 if order_side == "BUY" else price * 0.997
        hybrid_limit_price = round(round(raw_limit / 0.05) * 0.05, 2)

        # Execute Order via Bridge
        sec_info = SNIPER_UNIVERSE.get(symbol, {"security_id": "0"})
        order_res = self.bridge.execute_micro_order(
            symbol=symbol,
            security_id=sec_info["security_id"],
            quantity=quantity,
            side=order_side,
            price=hybrid_limit_price,
            order_type="LIMIT",
            product_type="INTRADAY",
            dry_run=self.dry_run,
        )

        if order_res.get("status") in ("SUCCESS", "ORDER_PLACED"):
            cl_ord_id = order_res.get("cl_ord_id", f"SNIPER_{int(time.time()*1000)}")
            new_pos = {
                "cl_ord_id": cl_ord_id,
                "symbol": symbol,
                "security_id": sec_info["security_id"],
                "side": order_side,
                "quantity": quantity,
                "entry_price": price,
                "stop_loss": stop_loss,
                "initial_stop_loss": stop_loss,
                "take_profit": take_profit,
                "highest_price": price,
                "lowest_price": price,
                "breakeven_locked": False,
                "stage_id": self.active_stage.stage_id,
            }
            self.active_positions[symbol] = new_pos

            # Commit to SQLite WAL Ledger
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    """INSERT INTO sniper_trades 
                       (cl_ord_id, timestamp, stage, symbol, side, quantity, entry_price, stop_loss, take_profit, status, execution_mode)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (cl_ord_id, time.time(), self.active_stage.stage_id, symbol, order_side, quantity, price, stop_loss, take_profit, "OPEN", "DRY_RUN" if self.dry_run else "LIVE")
                )
                conn.commit()

            return {"status": "POSITION_OPENED", "position": new_pos}

        return None

    async def _manage_active_position(self, current_price: float, symbol: str | None = None) -> dict[str, Any] | None:
        """Ratchets trailing stop-loss and checks TP/SL triggers for both BUY and SELL."""
        if symbol:
            pos = self.active_positions.get(symbol)
        else:
            pos = self.active_position

        if not pos:
            return None

        # Data outlier check: Ignore tick if price deviates more than 15% from entry in single tick
        if current_price <= 0 or abs(current_price - pos["entry_price"]) / pos["entry_price"] > 0.15:
            logger.warning(f"Ignoring suspicious outlier tick for {pos['symbol']}: ₹{current_price} vs entry ₹{pos['entry_price']}")
            return None

        pos_side = pos.get("side", "BUY").upper()
        pos.setdefault("breakeven_locked", False)
        target_sym = pos["symbol"]

        # Ingest dynamic matrix parameters (Chandelier Stop, Breakeven Ratchet, Expiry Mode)
        matrix_file = Path(__file__).resolve().parent / "dynamic_strategy_matrix.json"
        chand_mult = 1.1
        be_trigger_ratio = 0.7  # Activate breakeven at 0.7R (~0.35% gain) instead of waiting for 1.0R
        atr_val = 0.35
        be_buffer_fixed = 0.10
        if matrix_file.exists():
            try:
                with open(matrix_file, "r", encoding="utf-8") as mf:
                    strat_m = json.load(mf)
                    sym_m = strat_m.get(target_sym, {})
                    chand_mult = float(sym_m.get("chandelier_multiplier", 1.1))
                    atr_val = float(sym_m.get("atr_14", 0.35))
                    be_buffer_fixed = float(sym_m.get("breakeven_buffer", 0.10))
            except Exception:
                pass

        if pos_side == "BUY":
            pos.setdefault("highest_price", pos.get("entry_price", current_price))
            pos.setdefault("initial_stop_loss", pos.get("stop_loss", current_price - 0.75))
            pos["highest_price"] = max(pos["highest_price"], current_price)

            gain_from_peak = pos["highest_price"] - pos["entry_price"]
            sl_distance = pos["entry_price"] - pos["initial_stop_loss"]
            safe_buffer = be_buffer_fixed if self.dry_run else max(0.10, round(be_buffer_fixed, 2))

            # Ratchet Rule: Move SL to Breakeven (+safe_buffer) once peak gain reaches 0.7R (~+0.35%)
            if not pos["breakeven_locked"] and gain_from_peak >= (be_trigger_ratio * sl_distance):
                pos["stop_loss"] = round(pos["entry_price"] + safe_buffer, 2)
                pos["breakeven_locked"] = True
                logger.info(f"🔒 RATCHET ACTIVATED (0-DTE EXPIRY): {target_sym} Stop-Loss moved to Breakeven+ ₹{pos['stop_loss']:.2f} (Buffer: ₹{safe_buffer:.2f})")

            # Dynamic Chandelier Trailing SL once locked: Highest Price - (Chandelier_Mult * ATR)
            if pos["breakeven_locked"]:
                chandelier_sl = round(pos["highest_price"] - (chand_mult * atr_val), 2)
                if chandelier_sl > pos["stop_loss"]:
                    pos["stop_loss"] = chandelier_sl
                    logger.info(f"📈 CHANDELIER TRAILING SL RATCHETED: {target_sym} New SL ₹{pos['stop_loss']:.2f} (Peak: ₹{pos['highest_price']:.2f} | Chandelier: {chand_mult}x ATR)")

            # Check Take-Profit Trigger
            if current_price >= pos["take_profit"]:
                logger.info(f"🎉 TAKE-PROFIT HIT: {target_sym} at ₹{current_price:.2f} (Target: ₹{pos['take_profit']:.2f})")
                return await self.close_position(current_price, symbol=target_sym, reason="TAKE_PROFIT")

            # Check Stop-Loss Trigger
            if current_price <= pos["stop_loss"]:
                logger.warning(f"🛑 STOP-LOSS HIT: {target_sym} at ₹{current_price:.2f} (SL: ₹{pos['stop_loss']:.2f})")
                return await self.close_position(current_price, symbol=target_sym, reason="STOP_LOSS")
        else:
            # SHORT / SELL POSITION
            pos.setdefault("lowest_price", pos.get("entry_price", current_price))
            pos.setdefault("initial_stop_loss", pos.get("stop_loss", current_price + 0.75))
            pos["lowest_price"] = min(pos["lowest_price"], current_price)

            gain_from_trough = pos["entry_price"] - pos["lowest_price"]
            sl_distance = pos["initial_stop_loss"] - pos["entry_price"]
            safe_buffer = be_buffer_fixed if self.dry_run else max(0.10, round(be_buffer_fixed, 2))

            # Ratchet Rule: Move SL to Breakeven (-safe_buffer) once trough gain reaches 0.7R (~+0.35%)
            if not pos["breakeven_locked"] and gain_from_trough >= (be_trigger_ratio * sl_distance):
                pos["stop_loss"] = round(pos["entry_price"] - safe_buffer, 2)
                pos["breakeven_locked"] = True
                logger.info(f"🔒 SHORT RATCHET ACTIVATED (0-DTE EXPIRY): {target_sym} Stop-Loss moved to Breakeven- ₹{pos['stop_loss']:.2f} (Buffer: ₹{safe_buffer:.2f})")

            # Dynamic Chandelier Trailing SL once locked: Lowest Price + (Chandelier_Mult * ATR)
            if pos["breakeven_locked"]:
                chandelier_sl = round(pos["lowest_price"] + (chand_mult * atr_val), 2)
                if chandelier_sl < pos["stop_loss"]:
                    pos["stop_loss"] = chandelier_sl
                    logger.info(f"📉 SHORT CHANDELIER TRAILING SL RATCHETED: {target_sym} New SL ₹{pos['stop_loss']:.2f} (Trough: ₹{pos['lowest_price']:.2f} | Chandelier: {chand_mult}x ATR)")

            # Check Take-Profit Trigger for Short
            if current_price <= pos["take_profit"]:
                logger.info(f"🎉 SHORT TAKE-PROFIT HIT: {target_sym} at ₹{current_price:.2f} (Target: ₹{pos['take_profit']:.2f})")
                return await self.close_position(current_price, symbol=target_sym, reason="TAKE_PROFIT")

            # Check Stop-Loss Trigger for Short
            if current_price >= pos["stop_loss"]:
                logger.warning(f"🛑 SHORT STOP-LOSS HIT: {target_sym} at ₹{current_price:.2f} (SL: ₹{pos['stop_loss']:.2f})")
                return await self.close_position(current_price, symbol=target_sym, reason="STOP_LOSS")

        return None

    async def close_position(self, exit_price: float, symbol: str | None = None, reason: str = "MANUAL") -> dict[str, Any]:
        """Closes active position for given symbol, records PnL, syncs broker funds, and progresses stage."""
        if symbol:
            pos = self.active_positions.get(symbol)
        else:
            pos = self.active_position

        if not pos:
            return {"status": "NO_ACTIVE_POSITION"}

        target_sym = pos["symbol"]
        pos_side = pos.get("side", "BUY").upper()
        if pos_side == "BUY":
            pnl = round((exit_price - pos["entry_price"]) * pos["quantity"], 2)
        else:
            pnl = round((pos["entry_price"] - exit_price) * pos["quantity"], 2)

        # Approximate statutory equity brokerage & STT
        friction = 1.05  # sub-₹2 statutory fees
        net_pnl = round(pnl - friction, 2)

        # Dispatch offsetting exit order via Bridge (Live or Dry-Run)
        if self.bridge:
            sec_info = SNIPER_UNIVERSE.get(target_sym, {"security_id": pos.get("security_id", "0")})
            exit_side = "SELL" if pos.get("side", "BUY") == "BUY" else "BUY"
            raw_exit_limit = exit_price * 0.997 if exit_side == "SELL" else exit_price * 1.003
            exit_hybrid_limit = round(round(raw_exit_limit / 0.05) * 0.05, 2)
            exit_res = self.bridge.execute_micro_order(
                symbol=target_sym,
                security_id=sec_info["security_id"],
                quantity=pos["quantity"],
                side=exit_side,
                price=exit_hybrid_limit,
                order_type="LIMIT",
                product_type="INTRADAY",
                dry_run=self.dry_run,
            )
            logger.info(f"Broker exit order dispatched for {target_sym}: {exit_res}")

        self.current_equity += net_pnl
        if net_pnl < 0:
            self.daily_loss += abs(net_pnl)

        self.active_stage.trades_executed += 1
        if net_pnl > 0:
            self.active_stage.wins += 1
        else:
            self.active_stage.losses += 1

        self.active_stage.current_equity = self.current_equity
        self.gatekeeper.record_trade_outcome(net_pnl)

        # Sync physical broker equity if live
        self.sync_broker_equity()

        # Update SQLite WAL Ledger
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """UPDATE sniper_trades 
                   SET exit_price = ?, realized_pnl = ?, status = ?
                   WHERE cl_ord_id = ?""",
                (exit_price, net_pnl, f"CLOSED_{reason}", pos["cl_ord_id"])
            )
            conn.commit()

        logger.info(f"📋 TRADE CLOSED ({reason}): {target_sym} | Qty: {pos['quantity']} | Entry: ₹{pos['entry_price']} | Exit: ₹{exit_price} | Net PnL: ₹{net_pnl:+.2f} | Balance: ₹{self.current_equity:.2f}")

        # Stage Progression Check
        if self.current_equity >= self.active_stage.target_equity:
            self.active_stage.is_completed = True
            logger.info(f"🏆 STAGE {self.active_stage.stage_id} COMPLETED! Balance reached ₹{self.current_equity:.2f}.")
            if self.current_stage_idx < len(self.stage_definitions) - 1:
                self.current_stage_idx += 1
                self.active_stage = self._init_stage(self.current_stage_idx)
                logger.info(f"🚀 ADVANCING TO STAGE {self.active_stage.stage_id} (Target: ₹{self.active_stage.target_equity:.2f})")
            else:
                logger.info(f"🌟 GRAND MISSION ACCOMPLISHED! ₹1,000 doubled to ₹{self.current_equity:.2f}!")

        closed_pos_info = {
            "symbol": target_sym,
            "quantity": pos["quantity"],
            "entry_price": pos["entry_price"],
            "exit_price": exit_price,
            "net_pnl": net_pnl,
            "reason": reason,
            "new_balance": self.current_equity,
            "current_stage": self.active_stage.stage_id,
        }

        # Remove from active positions dictionary
        if target_sym in self.active_positions:
            del self.active_positions[target_sym]

        return {"status": "POSITION_CLOSED", "details": closed_pos_info}

    def get_summary(self) -> dict[str, Any]:
        """Provides full operational telemetry with multi-slot awareness."""
        return {
            "initial_capital": self.initial_capital,
            "current_equity": self.current_equity,
            "total_return_pct": round(((self.current_equity - self.initial_capital) / self.initial_capital) * 100.0, 2),
            "daily_loss": self.daily_loss,
            "circuit_breaker_active": self.circuit_breaker_tripped,
            "current_stage": self.active_stage.stage_id,
            "max_concurrent_positions": self.max_concurrent_positions,
            "open_position_count": len(self.active_positions),
            "has_active_position": len(self.active_positions) > 0,
            "active_positions": list(self.active_positions.values()),
            "active_position": self.active_position,
            "dry_run": self.dry_run,
        }

