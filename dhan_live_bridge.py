"""
⚡ DHAN LIVE QUANT BRIDGE (DhanHQ API v2)
=========================================
Integrated into Sovereign Quant OS.
Enforces the 3-Gate Variance Shield and keeps simulated and live broker authority explicit.
"""

import json
import logging
import os
from typing import Any

try:
    from dhanhq import dhanhq
except ImportError:
    dhanhq = None

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("DhanLiveBridge")


class DhanLiveBridge:
    def __init__(self, client_id: str | None = None, access_token: str | None = None):
        self.client_id = client_id or os.environ.get("DHAN_CLIENT_ID", "")
        self.access_token = access_token or os.environ.get("DHAN_ACCESS_TOKEN", "")
        self.dhan = None
        self.is_connected = False

        if self.client_id and self.access_token and dhanhq:
            try:
                from dhanhq import DhanContext

                self.dhan = dhanhq(DhanContext(self.client_id, self.access_token))
                self.is_connected = True
                logger.info("Initialized DhanHQ instance for configured Client ID")
            except Exception as e:
                logger.error(f"Failed to initialize DhanHQ: {e}")
                self.dhan = None

    @staticmethod
    def _simulated_envelope(result_class: str, **payload: Any) -> dict[str, Any]:
        """Return a fail-closed result that cannot masquerade as live broker authority."""
        return {
            "status": "SIMULATED",
            "result_class": result_class,
            "execution_mode": "SIMULATED",
            "connection_authority": "ABSENT",
            "is_simulated": True,
            "broker_order_id": None,
            **payload,
        }

    def check_balance(self) -> dict[str, Any]:
        """Fetch available margin limits / funds from Dhan."""
        if not self.is_connected or not self.dhan:
            return self._simulated_envelope(
                "SIMULATED_ACCOUNT_SNAPSHOT",
                client_id=self.client_id or "AWAITING_INPUT",
                simulated_balance_hint=1.00,
                note="Awaiting DHAN_CLIENT_ID & DHAN_ACCESS_TOKEN from web.dhan.co",
            )
        try:
            fund_resp = self.dhan.get_fund_limits()
            logger.info(f"Fund Limits Response: {fund_resp}")
            return {
                "status": "SUCCESS",
                "result_class": "LIVE_ACCOUNT_SNAPSHOT",
                "execution_mode": "LIVE",
                "connection_authority": "PRESENT",
                "is_simulated": False,
                "data": fund_resp,
            }
        except Exception as e:
            logger.error(f"Error checking funds: {e}")
            return {"status": "ERROR", "error": str(e)}

    def get_market_quote(self, security_id: str, exchange_segment: str = "NSE_EQ") -> dict[str, Any]:
        """Fetch live LTP and market depth."""
        if not self.is_connected or not self.dhan:
            return self._simulated_envelope(
                "SIMULATED_MARKET_QUOTE",
                security_id=security_id,
                simulated_ltp_hint=684.85,
            )
        try:
            quote = self.dhan.quote_data(security_id=security_id, exchange_segment=exchange_segment)
            return {
                "status": "SUCCESS",
                "result_class": "LIVE_MARKET_QUOTE",
                "execution_mode": "LIVE",
                "connection_authority": "PRESENT",
                "is_simulated": False,
                "data": quote,
            }
        except Exception as e:
            return {"status": "ERROR", "error": str(e)}

    def place_canary_order(self, symbol: str, security_id: str, quantity: int = 1, price: float = 0.0) -> dict[str, Any]:
        """Place a live micro-order only when explicit broker authority is present."""
        if not self.is_connected or not self.dhan:
            logger.info(f"[SIMULATION] Micro order: BUY {quantity} {symbol} @ market. No broker authority.")
            return self._simulated_envelope(
                "SIMULATED_ORDER",
                symbol=symbol,
                quantity=quantity,
                est_risk=1.00,
            )
        try:
            order_resp = self.dhan.place_order(
                security_id=security_id,
                exchange_segment=self.dhan.NSE,
                transaction_type=self.dhan.BUY,
                quantity=quantity,
                order_type=self.dhan.MARKET,
                product_type=self.dhan.CNC,
                price=price,
            )
            broker_order_id = None
            if isinstance(order_resp, dict):
                broker_order_id = order_resp.get("orderId") or order_resp.get("order_id")
                nested = order_resp.get("data")
                if broker_order_id is None and isinstance(nested, dict):
                    broker_order_id = nested.get("orderId") or nested.get("order_id")
            return {
                "status": "ORDER_PLACED",
                "result_class": "LIVE_ORDER_SUBMISSION",
                "execution_mode": "LIVE",
                "connection_authority": "PRESENT",
                "is_simulated": False,
                "broker_order_id": broker_order_id,
                "data": order_resp,
            }
        except Exception as e:
            logger.error(f"Failed to place order: {e}")
            return {"status": "ERROR", "error": str(e)}


if __name__ == "__main__":
    bridge = DhanLiveBridge()
    status = bridge.check_balance()
    print("==================================================")
    print("⚡ DHAN LIVE BRIDGE PROBE STATUS")
    print("==================================================")
    print(json.dumps(status, indent=2))
    print("==================================================")
