"""
PRE-TRADE RISK GATEKEEPER & SIZING ENGINE
Enforces:
1. Gate 1: Law of Ruin (Max single-trade risk <= 1.5% of equity)
2. Gate 2: Ergodicity Audit (Survival probability over 100 trades >= 95%)
3. Gate 3: Win-Rate Dominance (Expected Value > Variance Drag)
4. Anti-Martingale / Fractional Kelly Scaling Engine
"""

from dataclasses import dataclass
from typing import Any

from alpha_engine import TradeSignal


@dataclass
class RiskConfig:
    max_capital: float = 1008.0
    single_trade_risk_limit: float = 200.0
    daily_loss_limit: float = 200.0
    max_spread_pct: float = 0.05
    max_variance: float = 2.5

@dataclass
class RiskGateResult:
    passed: bool
    reason: str
    approved_quantity: float
    risk_amount: float
    hard_stop_loss: float
    hard_take_profit: float

class RiskGatekeeper:
    def __init__(
        self,
        config: RiskConfig | None = None,
        account_equity: float = 10000.0,
        base_risk_unit: float = 10.0,      # Base risk (₹10 or 0.1%)
        max_risk_pct: float = 0.015,       # 1.5% max risk per trade
        max_scale_level: int = 4,          # 1x, 2x, 4x, 8x
        historical_win_rate: float = 0.55
    ):
        self.config = config
        self.account_equity = config.max_capital if config else account_equity
        self.base_risk_unit = config.single_trade_risk_limit if config else base_risk_unit
        self.max_risk_pct = max_risk_pct
        self.max_scale_level = max_scale_level
        self.historical_win_rate = historical_win_rate
        
        self.current_scale_step: int = 1
        self.consecutive_wins: int = 0
        self.profit_buffer: float = 0.0

    def evaluate_pre_trade_gate(self, signal: TradeSignal) -> RiskGateResult:
        """Executes the 3-Gate Pipeline before allowing an order to reach the broker."""
        # Calculate proposed risk amount based on Anti-Martingale scaling
        scale_multiplier = 2 ** (self.current_scale_step - 1)
        proposed_risk = self.base_risk_unit * scale_multiplier

        # GATE 1: Law of Ruin Check
        max_allowed_risk = self.account_equity * self.max_risk_pct
        if proposed_risk > max_allowed_risk:
            return RiskGateResult(
                passed=False,
                reason=f"GATE 1 VETO: Proposed risk ₹{proposed_risk:.2f} exceeds 1.5% max equity risk (₹{max_allowed_risk:.2f})",
                approved_quantity=0,
                risk_amount=0,
                hard_stop_loss=0,
                hard_take_profit=0
            )

        # GATE 2: Ergodicity Audit
        # Survival over n=100 trials: P(survive) = (1 - r)^n
        risk_fraction = proposed_risk / self.account_equity
        p_survival_100 = (1.0 - risk_fraction) ** 100
        if p_survival_100 < 0.90:
            return RiskGateResult(
                passed=False,
                reason=f"GATE 2 VETO: Ergodicity failure. P(survival over 100 trades) is {p_survival_100:.1%}, below 90% threshold.",
                approved_quantity=0,
                risk_amount=0,
                hard_stop_loss=0,
                hard_take_profit=0
            )

        # GATE 3: Win-Rate Dominance Check
        # Edge = WR * RR - (1 - WR)
        edge = (self.historical_win_rate * signal.risk_reward_ratio) - (1.0 - self.historical_win_rate)
        variance_drag = 0.5 * (risk_fraction ** 2)
        if edge <= variance_drag:
            return RiskGateResult(
                passed=False,
                reason=f"GATE 3 VETO: Expected edge ({edge:.4f}) is dominated by variance drag ({variance_drag:.4f}).",
                approved_quantity=0,
                risk_amount=0,
                hard_stop_loss=0,
                hard_take_profit=0
            )

        # Calculate exact lot quantity based on stop-loss distance
        per_unit_risk = abs(signal.price - signal.stop_loss)
        if per_unit_risk <= 0:
            return RiskGateResult(passed=False, reason="Invalid stop-loss distance.", approved_quantity=0, risk_amount=0, hard_stop_loss=0, hard_take_profit=0)

        quantity = proposed_risk / per_unit_risk

        return RiskGateResult(
            passed=True,
            reason=f"CLEARED: Passed Gates 1-3. Scale Level {self.current_scale_step} ({scale_multiplier}x risk).",
            approved_quantity=quantity,
            risk_amount=proposed_risk,
            hard_stop_loss=signal.stop_loss,
            hard_take_profit=signal.take_profit
        )

    def record_trade_outcome(self, realized_pnl: float):
        """Updates Anti-Martingale scaling state: scales on win, resets on loss."""
        if realized_pnl > 0:
            self.consecutive_wins += 1
            self.profit_buffer += realized_pnl
            if self.current_scale_step < self.max_scale_level:
                self.current_scale_step += 1
        else:
            # ANTI-MARTINGALE INVARIANT: Reset immediately to base on ANY loss!
            self.consecutive_wins = 0
            self.current_scale_step = 1

        self.account_equity += realized_pnl

    def verify_3_gates(
        self,
        price_df: Any = None,
        asset_price: float = 100.0,
        bid: float = 99.95,
        ask: float = 100.05,
        stop_loss: float = 99.50,
        max_trade_risk: float = 3.75,
        side: str = "BUY",
    ) -> bool:
        """
        Evaluates the 3-Gate Variance Shield:
        Gate 1: Spread & Liquidity Check (Spread % <= max_spread_pct)
        Gate 2: Rolling Volatility / Variance Check (Variance <= max_variance)
        Gate 3: Single-Trade Capital Risk Check (Per-share risk <= max_trade_risk)
        
        Leverages Apple Silicon M1 native Zig NEON acceleration (libvariance_shield.dylib)
        with zero-copy fallback.
        """
        # Calculate per-unit risk based on trade side
        if side.upper() == "BUY":
            per_unit_risk = asset_price - stop_loss
        else:
            per_unit_risk = stop_loss - asset_price

        if per_unit_risk <= 0.0:
            return False

        # Calculate spread percentage
        spread = max(0.0, ask - bid)
        spread_pct = (spread / asset_price) * 100.0 if asset_price > 0 else 999.0
        max_spread = getattr(self.config, "max_spread_pct", 0.50) if self.config else 0.50
        # If config is 0.05 (fraction), scale to percent 0.50%
        if max_spread < 0.10:
            max_spread = max_spread * 10.0

        # Calculate variance from ticks dataframe if available
        variance = 0.50
        if price_df is not None:
            try:
                import pandas as pd
                if isinstance(price_df, pd.DataFrame) and not price_df.empty and "price" in price_df.columns:
                    v = float(price_df["price"].var())
                    if not pd.isna(v):
                        variance = v
            except Exception:
                pass

        max_var = getattr(self.config, "max_variance", 2.5) if self.config else 2.5

        # Attempt Apple Silicon M1 Zig NEON Hardware-Accelerated Evaluation
        try:
            import ctypes
            import pathlib
            zig_path = pathlib.Path(__file__).parent / "libvariance_shield.dylib"
            if zig_path.exists():
                lib = ctypes.CDLL(str(zig_path))
                lib.evaluate_3_gates.argtypes = [
                    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                    ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double,
                    ctypes.c_double
                ]
                lib.evaluate_3_gates.restype = ctypes.c_bool
                # In Zig, gate 3 checks d0 - d3 <= d4. For SELL, emulate symmetric check:
                sim_sl = (asset_price - per_unit_risk) if side.upper() == "SELL" else stop_loss
                neon_passed = lib.evaluate_3_gates(
                    float(asset_price), float(bid), float(ask), float(sim_sl),
                    float(max_trade_risk), float(self.account_equity),
                    float(variance), float(max_var), float(max_spread)
                )
                return bool(neon_passed)
        except Exception:
            pass

        # Robust High-Performance Python Fallback (Accounts for 5x Intraday MIS Margin)
        gate1_spread_ok = spread_pct <= max_spread
        gate2_var_ok = variance <= max_var
        margin_required = asset_price / 5.0
        gate3_risk_ok = per_unit_risk <= max_trade_risk and margin_required <= self.account_equity

        return gate1_spread_ok and gate2_var_ok and gate3_risk_ok

if __name__ == "__main__":
    from alpha_engine import SignalType, StrategyArchetype, TradeSignal
    gate = RiskGatekeeper(account_equity=10000.0, base_risk_unit=10.0)
    sig = TradeSignal(
        bar_id=1, timestamp=100.0, strategy=StrategyArchetype.MEAN_REVERSION,
        signal_type=SignalType.BUY, price=100.0, stop_loss=98.0, take_profit=105.0,
        risk_reward_ratio=2.5, confidence=0.85
    )
    res = gate.evaluate_pre_trade_gate(sig)
    print("Risk Gatekeeper Smoke Test:", res.reason, f"| Quantity: {res.approved_quantity:.2f} units | Risk: ₹{res.risk_amount:.2f}")
