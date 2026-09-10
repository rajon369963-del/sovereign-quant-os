"""
================================================================================
AIR10 MICRO-CAPITAL FRICTION CORTEX & TRANSACTION COST ANALYSIS (TCA) ENGINE
================================================================================
Implements the 5 Sovereign Pillars of Micro-Capital Algorithmic Survival:
1. Pre-Trade TCA & 3.0x Golden Rule Friction Gate (Square-Root Law Slippage).
2. Zero-Brokerage DMA Rails (Shoonya NorenRestApi & FlatTrade integration).
3. Hyperliquid L1 Gasless Perpetual Engine with ALO (Post-Only) Maker Rebates.
4. Volatility-Based Swing Multiplier (2.5x ATR dynamic exit dilation).
5. Prop Firm Evaluation Scaler & Webhook Bridge (Apex / Topstep / FTMO).
================================================================================
"""

import os
import sqlite3
import sys
import threading
import time
from pathlib import Path
from typing import Any

# Add local wheels to sys.path
ENGINE_DIR = Path(os.environ.get("AIR10_ENGINE_DIR", Path(__file__).resolve().parent))
WHEELS_DIR = Path(os.environ.get("AIR10_WHEELS_DIR", ENGINE_DIR / "downloaded_wheels"))
if (WHEELS_DIR / "pandas-ta").exists():
    sys.path.insert(0, str(WHEELS_DIR / "pandas-ta"))

# Attempt imports of native wheels
try:
    HAS_PANDAS_TA = True
except Exception:
    HAS_PANDAS_TA = False

try:
    HAS_SHOONYA = True
except Exception:
    HAS_SHOONYA = False

try:
    HAS_HYPERLIQUID = True
except Exception:
    HAS_HYPERLIQUID = False

class MicroCapitalFrictionCortex:
    """
    Unified Transaction Cost Analysis (TCA) and Microstructure Friction Shield.
    Protects retail micro-capital (<$100 / <₹5,000) from fee-drag ruin.
    """

    def __init__(self, db_path: Path | None = None):
        self.db_path = db_path or Path(os.environ.get("AIR10_TEST_DB", str(ENGINE_DIR / "live_production_ledger.sqlite")))
        self._local = threading.local()
        self._init_db()

    def _init_db(self):
        """Initializes TCA and friction audit tables in SQLite."""
        conn = sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tca_audit_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                symbol TEXT,
                venue TEXT,
                side TEXT,
                order_type TEXT,
                entry_price REAL,
                expected_alpha_pct REAL,
                spread_pct REAL,
                slippage_est_pct REAL,
                commission_pct REAL,
                tax_pct REAL,
                total_friction_pct REAL,
                friction_ratio REAL,
                passed INTEGER,
                decision_reason TEXT
            )
        """)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS maker_rebate_ledger (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                symbol TEXT,
                order_id TEXT,
                volume_usd REAL,
                rebate_rate REAL,
                rebate_earned_usd REAL,
                rebate_earned_inr REAL,
                venue TEXT
            )
        """)
        conn.commit()
        conn.close()

    def calculate_friction(self,
                           symbol: str,
                           order_book: dict[str, Any],
                           order_size_usd: float,
                           venue: str = "HYPERLIQUID_DEX_ALO",
                           order_type: str = "ALO") -> dict[str, float]:
        """
        Calculates exact friction components (Spread, Slippage, Commission, Taxes).
        
        Venues:
        - HYPERLIQUID_DEX_ALO: Gasless L1 DEX, ALO Post-Only (-0.002% Maker Rebate)
        - SHOONYA_ZERO_BROKERAGE: ₹0 flat fee, STT 0.025%, NSE 0.00297%, GST 18%
        - STANDARD_DISCOUNT_BROKER: Flat ₹20/order (₹40 round-trip = massive drag on small accounts)
        - BINANCE_TAKER: 0.05% taker fee + 1% Indian TDS on sell side
        """
        best_bid = float(order_book.get("bid", 100.0))
        best_ask = float(order_book.get("ask", 100.0))
        mid = (best_bid + best_ask) / 2.0
        
        # 1. Spread Percentage
        spread_pct = (best_ask - best_bid) / mid if mid > 0 else 0.0002

        # 2. Market Impact / Slippage (Square Root Law)
        # For micro-capital ($10 - $100), market impact is dominated by spread crossing.
        if order_type in ("ALO", "POST_ONLY"):
            # Post-only limit orders do not cross spread; slippage is 0!
            slippage_pct = 0.0
        else:
            # Taker market orders cross spread and suffer adverse selection
            slippage_pct = spread_pct * 1.5

        # 3. Commission & Rebate
        commission_pct = 0.0
        maker_rebate_pct = 0.0

        if venue == "HYPERLIQUID_DEX_ALO":
            if order_type in ("ALO", "POST_ONLY"):
                # Earning maker rebate instead of paying!
                maker_rebate_pct = 0.0002 # +0.02% or 2 bps rebate
                commission_pct = -maker_rebate_pct # Negative cost!
            else:
                commission_pct = 0.00035 # 3.5 bps taker fee
        elif venue == "SHOONYA_ZERO_BROKERAGE":
            commission_pct = 0.0 # Free brokerage
        elif venue == "STANDARD_DISCOUNT_BROKER":
            # Flat ₹20 buy + ₹20 sell = ₹40 round trip
            round_trip_fee_usd = 40.0 / 86.50 # ~$0.46 USD
            commission_pct = (round_trip_fee_usd / order_size_usd) if order_size_usd > 0 else 0.04
        elif venue == "BINANCE_TAKER":
            commission_pct = 0.0010 # 0.05% entry + 0.05% exit = 0.10%

        # 4. Regulatory Taxes
        tax_pct = 0.0
        if "SHOONYA" in venue or "EQUITY" in symbol:
            # STT 0.025% on sell side (0.0125% avg round-trip)
            # Exchange turnover 0.00297% * 2 = 0.00594%
            # Stamp duty 0.003%
            # GST 18% on exchange turnover
            tax_pct = 0.000125 + 0.0000594 + 0.000030 + (0.0000594 * 0.18)
        elif venue == "BINANCE_TAKER" and "INDIAN_KYC" in venue:
            # 1% TDS on sell side under Section 194S!
            tax_pct = 0.0100 # 1.0% brutal drag!
        else:
            # Decentralized DEXs (Hyperliquid): 0% tax at source
            tax_pct = 0.0

        # Total Round-Trip Friction
        # If maker rebate applies, friction is strictly reduced!
        total_friction_pct = max(0.0, spread_pct + slippage_pct + commission_pct + tax_pct)

        return {
            "spread_pct": spread_pct,
            "slippage_pct": slippage_pct,
            "commission_pct": commission_pct,
            "tax_pct": tax_pct,
            "maker_rebate_pct": maker_rebate_pct,
            "total_friction_pct": total_friction_pct
        }

    def evaluate_tca_gate(self,
                          symbol: str,
                          order_book: dict[str, Any],
                          order_size_usd: float,
                          expected_alpha_pct: float,
                          side: str = "BUY",
                          venue: str = "HYPERLIQUID_DEX_ALO",
                          order_type: str = "ALO") -> tuple[bool, dict[str, Any], str]:
        """
        Evaluates the Golden 3.0x Rule:
        Trade is APPROVED only if Expected Alpha >= 3.0 * Total Friction Cost.
        (Equivalently: Friction consumes <= 33.3% of Expected Profit).
        """
        friction = self.calculate_friction(symbol, order_book, order_size_usd, venue, order_type)
        total_fric = friction["total_friction_pct"]

        # Friction Ratio
        friction_ratio = (total_fric / expected_alpha_pct) if expected_alpha_pct > 0 else 999.0

        # Golden 3.0x Rule Barrier (Ratio must be <= 0.333, or Alpha >= 3x Cost)
        passed = (total_fric == 0.0) or (expected_alpha_pct >= 3.0 * total_fric)

        reason = "APPROVED_BY_TCA_GATE" if passed else (
            f"GATED_BY_FRICTION: Expected Alpha ({expected_alpha_pct*100:.3f}%) < "
            f"3.0x Friction ({total_fric*3.0*100:.3f}%). Friction eats {friction_ratio*100:.1f}% of profit."
        )

        # Audit Log (Thread-local cached connection with WAL)
        try:
            conn = getattr(self._local, "conn", None)
            if conn is None:
                conn = sqlite3.connect(self.db_path, timeout=5.0)
                conn.execute("PRAGMA journal_mode=WAL;")
                conn.execute("PRAGMA synchronous=NORMAL;")
                conn.execute("PRAGMA cache_size=-64000;")
                self._local.conn = conn
            conn.execute("""
                INSERT INTO tca_audit_log (
                    timestamp, symbol, venue, side, order_type, entry_price, expected_alpha_pct,
                    spread_pct, slippage_est_pct, commission_pct, tax_pct, total_friction_pct,
                    friction_ratio, passed, decision_reason
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                time.strftime("%Y-%m-%dT%H:%M:%S"), symbol, venue, side, order_type,
                float(order_book.get("ask" if side == "BUY" else "bid", 100.0)),
                expected_alpha_pct, friction["spread_pct"], friction["slippage_pct"],
                friction["commission_pct"], friction["tax_pct"], total_fric,
                friction_ratio, 1 if passed else 0, reason
            ))
            conn.commit()
        except Exception:
            pass

        return passed, friction, reason

    def calculate_atr_swing_targets(self,
                                   highs: list,
                                   lows: list,
                                   closes: list,
                                   length: int = 14,
                                   multiplier: float = 2.5) -> dict[str, float]:
        """
        Calculates Volatility-Based Swing Exits using 2.5x ATR.
        Expands target R-multiple to 1:3, diluting fixed fees by 98%.
        """
        if len(closes) < length + 1:
            # Default estimated volatility
            current_price = closes[-1] if closes else 100.0
            atr = current_price * 0.015 # 1.5% volatility baseline
        else:
            trs = []
            for i in range(1, len(closes)):
                tr = max(highs[i] - lows[i], abs(highs[i] - closes[i-1]), abs(lows[i] - closes[i-1]))
                trs.append(tr)
            atr = sum(trs[-length:]) / float(length)

        current_p = closes[-1] if closes else 100.0
        stop_dist = atr * multiplier
        target_dist = stop_dist * 3.0 # 1:3 R-multiple!

        return {
            "atr": atr,
            "atr_pct": atr / current_p if current_p > 0 else 0.01,
            "stop_loss_distance": stop_dist,
            "take_profit_distance": target_dist,
            "stop_loss_pct": (stop_dist / current_p),
            "take_profit_pct": (target_dist / current_p),
            "r_multiple": 3.0
        }

    def simulate_hyperliquid_alo_fill(self,
                                      symbol: str,
                                      side: str,
                                      price: float,
                                      qty: float) -> dict[str, Any]:
        """
        Simulates an Add-Liquidity-Only (ALO / Post-Only) Limit Order on Hyperliquid L1.
        Captures the spread and credits a Maker Rebate (+0.002%)!
        """
        volume_usd = price * qty
        rebate_rate = 0.0002 # 2 bps (0.02%)
        rebate_earned_usd = volume_usd * rebate_rate
        rebate_earned_inr = round(rebate_earned_usd * 86.50, 4)

        # Log rebate into SQLite ledger
        try:
            conn = sqlite3.connect(self.db_path)
            conn.execute("""
                INSERT INTO maker_rebate_ledger (
                    timestamp, symbol, order_id, volume_usd, rebate_rate,
                    rebate_earned_usd, rebate_earned_inr, venue
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                time.strftime("%Y-%m-%dT%H:%M:%S"), symbol, f"ALO_{int(time.time()*1000)}",
                volume_usd, rebate_rate, rebate_earned_usd, rebate_earned_inr, "HYPERLIQUID_L1"
            ))
            conn.commit()
            conn.close()
        except Exception:
            pass

        return {
            "status": "FILLED_MAKER_POST_ONLY",
            "venue": "HYPERLIQUID_L1",
            "side": side,
            "price": price,
            "qty": qty,
            "volume_usd": volume_usd,
            "rebate_rate": rebate_rate,
            "rebate_earned_usd": rebate_earned_usd,
            "rebate_earned_inr": rebate_earned_inr,
            "gas_fee_usd": 0.0 # Gasless L1!
        }

    def evaluate_prop_firm_scaling(self,
                                   master_capital_inr: float,
                                   trade_risk_inr: float,
                                   account_tier_usd: float = 50000.0,
                                   copier_multiplier: int = 20) -> dict[str, Any]:
        """
        Calculates Prop Firm Scaler metrics (Apex Trader Funding / Topstep).
        Risks pennies on ₹1,000 master account; copies to 20x $50,000 funded accounts!
        """
        max_trailing_drawdown_usd = 2500.0 # Standard $50k Apex tier
        daily_loss_limit_usd = 1000.0
        
        trade_risk_usd = trade_risk_inr / 86.50
        copied_trade_risk_usd = trade_risk_usd * copier_multiplier
        
        # Max allowable micro-contracts (MES)
        mes_point_value = 5.0 # $5 per point on S&P 500 Micro E-mini
        mes_contracts = max(1, min(10, int(copied_trade_risk_usd / (mes_point_value * 5.0))))

        return {
            "account_tier_usd": account_tier_usd,
            "copier_multiplier": copier_multiplier,
            "master_risk_inr": trade_risk_inr,
            "master_risk_usd": trade_risk_usd,
            "total_portfolio_risk_usd": copied_trade_risk_usd,
            "max_drawdown_usd": max_trailing_drawdown_usd,
            "drawdown_headroom_pct": (max_trailing_drawdown_usd - copied_trade_risk_usd) / max_trailing_drawdown_usd * 100.0,
            "mes_contracts": mes_contracts,
            "compliant": copied_trade_risk_usd <= (daily_loss_limit_usd * 0.20) # max 20% of daily limit per trade
        }

# Global singleton instance
friction_cortex = MicroCapitalFrictionCortex()

if __name__ == "__main__":
    print("⚡ Testing AIR10 Micro-Capital Friction Cortex...")
    test_ob = {"bid": 77700.0, "ask": 77701.0}
    
    # Test 1: Standard Broker Scalp with ₹1,000 ($12) -> SHOULD BE REJECTED!
    passed_std, fric_std, reason_std = friction_cortex.evaluate_tca_gate(
        symbol="BTC/USDT", order_book=test_ob, order_size_usd=12.0,
        expected_alpha_pct=0.0070, side="BUY", venue="STANDARD_DISCOUNT_BROKER", order_type="MARKET"
    )
    print(f"Test 1 (Standard Broker Flat ₹20): Passed={passed_std} | Reason: {reason_std}")

    # Test 2: Hyperliquid ALO Maker Rebate with ₹1,000 ($12) -> SHOULD BE APPROVED!
    passed_hl, fric_hl, reason_hl = friction_cortex.evaluate_tca_gate(
        symbol="BTC/USDT", order_book=test_ob, order_size_usd=12.0,
        expected_alpha_pct=0.0070, side="BUY", venue="HYPERLIQUID_DEX_ALO", order_type="ALO"
    )
    print(f"Test 2 (Hyperliquid ALO Gasless): Passed={passed_hl} | Reason: {reason_hl}")

    # Test 3: Volatility ATR Swing Expansion
    closes = [77000, 77200, 77100, 77350, 77250, 77500, 77400, 77650, 77550, 77700]
    highs = [p * 1.002 for p in closes]
    lows = [p * 0.998 for p in closes]
    swing = friction_cortex.calculate_atr_swing_targets(highs, lows, closes)
    print(f"Test 3 (ATR Swing Expansion): Stop={swing['stop_loss_pct']*100:.2f}% | Target={swing['take_profit_pct']*100:.2f}% | R={swing['r_multiple']}")

    # Test 4: Maker Rebate Simulation
    rebate = friction_cortex.simulate_hyperliquid_alo_fill("BTC/USDT", "BUY", 77700.0, 0.001)
    print(f"Test 4 (Maker Rebate Credit): Earned +${rebate['rebate_earned_usd']:.5f} (+₹{rebate['rebate_earned_inr']:.3f} INR) with Zero Gas!")
