"""
Sovereign Quant OS - Real-Time Risk Gatekeeper v2.
Enforces drawdown limits, max position sizing, and circuit breaker halts.
"""
from typing import Tuple

class QuantRiskGatekeeper:
    def __init__(self, max_drawdown_pct: float = 0.05, max_position_size: float = 1_000_000.0):
        self.max_drawdown_pct = max_drawdown_pct
        self.max_position_size = max_position_size
        self.circuit_broken = False

    def evaluate_order(self, symbol: str, side: str, qty: float, price: float, current_dd_pct: float) -> Tuple[bool, str]:
        if self.circuit_broken:
            return False, "CIRCUIT_BREAKER_ACTIVE"
        if current_dd_pct > self.max_drawdown_pct:
            self.circuit_broken = True
            return False, f"MAX_DRAWDOWN_EXCEEDED: {current_dd_pct:.2%} > {self.max_drawdown_pct:.2%}"
        order_val = qty * price
        if order_val > self.max_position_size:
            return False, f"POSITION_LIMIT_EXCEEDED: {order_val} > {self.max_position_size}"
        return True, "ORDER_APPROVED"
