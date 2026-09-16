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
from typing import Any

from data_engine import DataEngine
from dhan_live_bridge import DhanLiveBridge
from premarket_screener import CandidateStock, PremarketScreener
from risk_gatekeeper import RiskConfig, RiskGatekeeper

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("SniperMomentumEngine")

# High-Velocity Trending Momentum Universe (Sub-₹500 NSE Equities with Explosive Liquidity)
SNIPER_UNIVERSE = {
    "TATASTEEL": {"security_id": "3499", "lot_size": 1, "tick_size": 0.05, "ref_price": 181.74},
    "SAIL": {"security_id": "2963", "lot_size": 1, "tick_size": 0.05, "ref_price": 171.86},
    "NATIONALUM": {"security_id": "6364", "lot_size": 1, "tick_size": 0.05, "ref_price": 185.0},
    "ASHOKLEY": {"security_id": "212", "lot_size": 1, "tick_size": 0.05, "ref_price": 156.08},
    "PNB": {"security_id": "10666", "lot_size": 1, "tick_size": 0.05, "ref_price": 115.18},
    "IDFCFIRSTB": {"security_id": "11184", "lot_size": 1, "tick_size": 0.05, "ref_price": 72.50},
    "IRFC": {"security_id": "2029", "lot_size": 1, "tick_size": 0.05, "ref_price": 176.0},
    "SUZLON": {"security_id": "12018", "lot_size": 1, "tick_size": 0.05, "ref_price": 74.50},
    "BHEL": {"security_id": "438", "lot_size": 1, "tick_size": 0.05, "ref_price": 285.0},
    "NBCC": {"security_id": "31415", "lot_size": 1, "tick_size": 0.05, "ref_price": 172.0},
    "ZENSARTECH": {"security_id": "1076", "lot_size": 1, "tick_size": 0.05, "ref_price": 440.0},
    "HCLTECH": {"security_id": "7229", "lot_size": 1, "tick_size": 0.05, "ref_price": 1264.0},
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
        self.max_daily_loss = 200.0  # 20% hard circuit breaker
        self.dry_run = dry_run
        self.db_path = db_path
        self.tick_db_path = tick_db_path

        # Components
        self.data_engine = DataEngine(db_path=self.tick_db_path)
        self.bridge = DhanLiveBridge(dry_run=self.dry_run)
        self.risk_config = RiskConfig(
            max_capital=self.current_equity,
            single_trade_risk_limit=200.0,
            daily_loss_limit=self.max_daily_loss,
            max_spread_pct=0.15,
            max_variance=2.5,
        )
        self.gatekeeper = RiskGatekeeper(
            config=self.risk_config,
            account_equity=self.current_equity,
            base_risk_unit=200.0,
        )

        # Stage Setup (The Sniper Triangle)
        self.stage_definitions = [
            {"stage": 1, "target_gain": 400.0, "risk": 200.0, "next_eq": 1358.0},
            {"stage": 2, "target_gain": 540.0, "risk": 270.0, "next_eq": 1848.0},
            {"stage": 3, "target_gain": 740.0, "risk": 370.0, "next_eq": 2538.0},
        ]
        self.current_stage_idx = 0
        self.active_stage = self._init_stage(0)
        self.active_position: dict[str, Any] | None = None
        self.circuit_breaker_tripped = False

        # Phase 2 Pre-Market Screener & Gap-Leverage Engine
        self.screener = PremarketScreener(cash_equity=self.current_equity, base_leverage=5.0, max_trade_risk=3.75)
        self.premarket_candidates: dict[str, CandidateStock] = {}

        self._init_ledger_db()

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
            if self.active_position:
                logger.warning("⏰ 03:10 PM Cutoff Hit: Executing Auto-Square-Off to protect capital.")
                return await self.close_position(price, reason="TIME_CUTOFF_0310_PM")
            return {"status": "INACTIVE", "reason": "POST_MARKET_HOURS"}

        # 3. Active Position Management (Ratcheting Trailing SL)
        if self.active_position and self.active_position["symbol"] == symbol:
            return await self._manage_active_position(price)

        # 4. New Entry Evaluation
        if not self.active_position and not self.circuit_breaker_tripped:
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
        """Evaluates entry conditions against 3-Gate Variance Shield."""
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

        # Position Sizing: Bound by remaining loss budget and 5x MIS leverage
        remaining_loss_budget = max(0.0, self.max_daily_loss - self.daily_loss)
        if remaining_loss_budget <= 1.0:
            logger.warning(f"Remaining daily loss budget (₹{remaining_loss_budget:.2f}) too small. Skipping entry.")
            return None

        sec_info = SNIPER_UNIVERSE.get(symbol, {"security_id": "0"})
        candidate = self.premarket_candidates.get(symbol)
        effective_leverage = candidate.safe_leverage if candidate else 5.0
        max_margin = self.current_equity * effective_leverage
        shares_by_margin = int(max_margin / price)
        
        # God-Level Sizing: Scaled from ₹3.75 canary up to ₹25.00 aggressive risk (utilizing 5x MIS leverage power)
        stage_risk = 25.00 if self.active_stage.stage_id == 1 else min(self.active_stage.risk_budget * 5.0, 50.0)
        effective_risk_budget = min(stage_risk, remaining_loss_budget)
        shares_by_risk = int(effective_risk_budget / sl_distance)
        quantity = max(1, min(shares_by_risk, shares_by_margin))

        # Re-check that total possible loss does not exceed remaining budget
        if (quantity * sl_distance) > (remaining_loss_budget + 5.0):
            quantity = max(1, int(remaining_loss_budget / sl_distance))
            if quantity < 1:
                return None

        logger.info(f"🎯 SNIPER TRIGGER: {symbol} Passed 3 Gates! Stage: {self.active_stage.stage_id} | Side: {order_side} | Qty: {quantity} | Entry: ₹{price} | SL: ₹{stop_loss} | TP: ₹{take_profit}")

        # Execute Order via Bridge
        order_res = self.bridge.execute_micro_order(
            symbol=symbol,
            security_id=sec_info["security_id"],
            quantity=quantity,
            side=order_side,
            price=price,
            order_type="LIMIT",
            product_type="INTRADAY",
            dry_run=self.dry_run,
        )

        if order_res.get("status") in ("SUCCESS", "ORDER_PLACED"):
            cl_ord_id = order_res.get("cl_ord_id", f"SNIPER_{int(time.time()*1000)}")
            self.active_position = {
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

            # Commit to SQLite WAL Ledger
            with sqlite3.connect(self.db_path) as conn:
                conn.execute(
                    """INSERT INTO sniper_trades 
                       (cl_ord_id, timestamp, stage, symbol, side, quantity, entry_price, stop_loss, take_profit, status, execution_mode)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                    (cl_ord_id, time.time(), self.active_stage.stage_id, symbol, order_side, quantity, price, stop_loss, take_profit, "OPEN", "DRY_RUN" if self.dry_run else "LIVE")
                )
                conn.commit()

            return {"status": "POSITION_OPENED", "position": self.active_position}

        return None

    async def _manage_active_position(self, current_price: float) -> dict[str, Any] | None:
        """Ratchets trailing stop-loss and checks TP/SL triggers for both BUY and SELL."""
        pos = self.active_position
        if not pos:
            return None

        pos_side = pos.get("side", "BUY").upper()
        pos.setdefault("breakeven_locked", False)

        if pos_side == "BUY":
            pos.setdefault("highest_price", pos.get("entry_price", current_price))
            pos.setdefault("initial_stop_loss", pos.get("stop_loss", current_price - 0.75))
            pos["highest_price"] = max(pos["highest_price"], current_price)

            gain_per_share = current_price - pos["entry_price"]
            sl_distance = pos["entry_price"] - pos["initial_stop_loss"]

            # Ratchet Rule: Move SL to Breakeven (+0.05 buffer) once gain reaches +1R
            if not pos["breakeven_locked"] and gain_per_share >= sl_distance:
                pos["stop_loss"] = pos["entry_price"] + 0.05
                pos["breakeven_locked"] = True
                logger.info(f"🔒 RATCHET ACTIVATED: Stop-Loss moved to Breakeven+ ₹{pos['stop_loss']:.2f} (+1R reached)")

            # Trail SL further if gain expands beyond +1.5R
            if pos["breakeven_locked"] and gain_per_share > 1.5 * sl_distance:
                trailing_sl = pos["highest_price"] - (sl_distance * 0.6)
                if trailing_sl > pos["stop_loss"]:
                    pos["stop_loss"] = round(trailing_sl, 2)
                    logger.debug(f"📈 Trailing SL ratcheted to ₹{pos['stop_loss']:.2f}")

            # Check Take-Profit Trigger
            if current_price >= pos["take_profit"]:
                logger.info(f"🎉 TAKE-PROFIT HIT: {pos['symbol']} at ₹{current_price:.2f} (Target: ₹{pos['take_profit']:.2f})")
                return await self.close_position(current_price, reason="TAKE_PROFIT")

            # Check Stop-Loss Trigger
            if current_price <= pos["stop_loss"]:
                logger.warning(f"🛑 STOP-LOSS HIT: {pos['symbol']} at ₹{current_price:.2f} (SL: ₹{pos['stop_loss']:.2f})")
                return await self.close_position(current_price, reason="STOP_LOSS")
        else:
            # SHORT / SELL POSITION
            pos.setdefault("lowest_price", pos.get("entry_price", current_price))
            pos.setdefault("initial_stop_loss", pos.get("stop_loss", current_price + 0.75))
            pos["lowest_price"] = min(pos["lowest_price"], current_price)

            gain_per_share = pos["entry_price"] - current_price
            sl_distance = pos["initial_stop_loss"] - pos["entry_price"]

            # Ratchet Rule: Move SL to Breakeven (-0.05 buffer) once gain reaches +1R
            if not pos["breakeven_locked"] and gain_per_share >= sl_distance:
                pos["stop_loss"] = pos["entry_price"] - 0.05
                pos["breakeven_locked"] = True
                logger.info(f"🔒 SHORT RATCHET ACTIVATED: Stop-Loss moved to Breakeven- ₹{pos['stop_loss']:.2f} (+1R reached)")

            # Trail SL further if gain expands beyond +1.5R
            if pos["breakeven_locked"] and gain_per_share > 1.5 * sl_distance:
                trailing_sl = pos["lowest_price"] + (sl_distance * 0.6)
                if trailing_sl < pos["stop_loss"]:
                    pos["stop_loss"] = round(trailing_sl, 2)
                    logger.debug(f"📉 Short Trailing SL ratcheted down to ₹{pos['stop_loss']:.2f}")

            # Check Take-Profit Trigger for Short
            if current_price <= pos["take_profit"]:
                logger.info(f"🎉 SHORT TAKE-PROFIT HIT: {pos['symbol']} at ₹{current_price:.2f} (Target: ₹{pos['take_profit']:.2f})")
                return await self.close_position(current_price, reason="TAKE_PROFIT")

            # Check Stop-Loss Trigger for Short
            if current_price >= pos["stop_loss"]:
                logger.warning(f"🛑 SHORT STOP-LOSS HIT: {pos['symbol']} at ₹{current_price:.2f} (SL: ₹{pos['stop_loss']:.2f})")
                return await self.close_position(current_price, reason="STOP_LOSS")

        return None

    async def close_position(self, exit_price: float, reason: str = "MANUAL") -> dict[str, Any]:
        """Closes active position, records PnL, and progresses the Sniper Triangle stage."""
        pos = self.active_position
        if not pos:
            return {"status": "NO_ACTIVE_POSITION"}

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
            sec_info = SNIPER_UNIVERSE.get(pos["symbol"], {"security_id": pos.get("security_id", "0")})
            exit_side = "SELL" if pos.get("side", "BUY") == "BUY" else "BUY"
            exit_res = self.bridge.execute_micro_order(
                symbol=pos["symbol"],
                security_id=sec_info["security_id"],
                quantity=pos["quantity"],
                side=exit_side,
                price=exit_price,
                order_type="MARKET",
                product_type="INTRADAY",
                dry_run=self.dry_run,
            )
            logger.info(f"Broker exit order dispatched: {exit_res}")

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

        # Update SQLite WAL Ledger
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """UPDATE sniper_trades 
                   SET exit_price = ?, realized_pnl = ?, status = ?
                   WHERE cl_ord_id = ?""",
                (exit_price, net_pnl, f"CLOSED_{reason}", pos["cl_ord_id"])
            )
            conn.commit()

        logger.info(f"📋 TRADE CLOSED ({reason}): {pos['symbol']} | Qty: {pos['quantity']} | Entry: ₹{pos['entry_price']} | Exit: ₹{exit_price} | Net PnL: ₹{net_pnl:+.2f} | Balance: ₹{self.current_equity:.2f}")

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
            "symbol": pos["symbol"],
            "quantity": pos["quantity"],
            "entry_price": pos["entry_price"],
            "exit_price": exit_price,
            "net_pnl": net_pnl,
            "reason": reason,
            "new_balance": self.current_equity,
            "current_stage": self.active_stage.stage_id,
        }

        self.active_position = None
        return {"status": "POSITION_CLOSED", "details": closed_pos_info}

    def get_summary(self) -> dict[str, Any]:
        """Provides full operational telemetry."""
        return {
            "initial_capital": self.initial_capital,
            "current_equity": self.current_equity,
            "total_return_pct": round(((self.current_equity - self.initial_capital) / self.initial_capital) * 100.0, 2),
            "daily_loss": self.daily_loss,
            "circuit_breaker_active": self.circuit_breaker_tripped,
            "current_stage": self.active_stage.stage_id,
            "has_active_position": self.active_position is not None,
            "active_position": self.active_position,
            "dry_run": self.dry_run,
        }
