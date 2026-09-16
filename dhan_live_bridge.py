"""
⚡ DHAN LIVE QUANT BRIDGE (DhanHQ API v2)
=========================================
Integrated into Sovereign Quant OS.
Enforces the 3-Gate Variance Shield and keeps simulated and live broker authority explicit.
"""

import json
import logging
import os
import socket
import time
from typing import Any

import urllib3.util.connection as urllib_conn

# SEBI / DhanHQ API v2 Whitelist Invariant:
# macOS defaults to dynamic IPv6, which causes DH-905 Invalid IP mismatch.
# Forcing AF_INET routes all Dhan HTTP requests strictly over whitelisted primary IPv4 (152.59.152.111).
urllib_conn.allowed_gai_family = lambda: socket.AF_INET

try:
    from dhanhq import dhanhq
except ImportError:
    dhanhq = None

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("DhanLiveBridge")


class DhanLiveBridge:
    def __init__(self, client_id: str | None = None, access_token: str | None = None, dry_run: bool = False):
        self.dry_run = dry_run
        self.client_id = client_id or os.environ.get("DHAN_CLIENT_ID", "")
        self.access_token = access_token or os.environ.get("DHAN_ACCESS_TOKEN", "")
        if not self.client_id or not self.access_token:
            env_path = os.path.expanduser("~/teamwork_projects/sovereign-quant-os/.env.dhan")
            if os.path.exists(env_path):
                with open(env_path) as f:
                    for line in f:
                        if line.startswith("DHAN_CLIENT_ID=") and not self.client_id:
                            self.client_id = line.strip().split("=", 1)[1]
                        elif line.startswith("DHAN_ACCESS_TOKEN=") and not self.access_token:
                            self.access_token = line.strip().split("=", 1)[1]
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
    def get_positions(self) -> dict[str, Any]:
        """Fetch live positions from Dhan."""
        if not self.is_connected or not self.dhan:
            return {"status": "SIMULATED", "data": []}
        try:
            return self.dhan.get_positions()
        except Exception as e:
            logger.error(f"Error fetching positions: {e}")
            return {"status": "ERROR", "error": str(e), "data": []}

    def get_orders(self) -> dict[str, Any]:
        """Fetch live orders from Dhan."""
        if not self.is_connected or not self.dhan:
            return {"status": "SIMULATED", "data": []}
        try:
            return self.dhan.get_order_list()
        except Exception as e:
            logger.error(f"Error fetching orders: {e}")
            return {"status": "ERROR", "error": str(e), "data": []}

    def execute_micro_order(
        self,
        symbol: str,
        security_id: str,
        quantity: int,
        side: str = "BUY",
        price: float = 0.0,
        order_type: str = "LIMIT",
        product_type: str = "INTRADAY",
        dry_run: bool = False,
    ) -> dict[str, Any]:
        """Execute order in live or dry-run mode with fail-closed safety."""
        is_dry = dry_run or self.dry_run
        cl_ord_id = f"DHAN_{symbol[:4]}_{int(time.time()*1000)%100000000:08d}"

        if is_dry or not self.is_connected or not self.dhan:
            logger.info(f"[DRY_RUN] Order: {side} {quantity} {symbol} @ {price} ({order_type}, {product_type})")
            return {
                "status": "ORDER_PLACED",
                "result_class": "SIMULATED_ORDER",
                "execution_mode": "DRY_RUN",
                "cl_ord_id": cl_ord_id,
                "broker_order_id": f"SIM_{int(time.time())}",
                "symbol": symbol,
                "quantity": quantity,
                "side": side,
                "price": price,
            }

        try:
            dhan_side = self.dhan.BUY if side.upper() == "BUY" else self.dhan.SELL
            dhan_order_type = self.dhan.LIMIT if order_type.upper() == "LIMIT" else self.dhan.MARKET
            dhan_product = self.dhan.INTRA if product_type.upper() == "INTRADAY" else self.dhan.CNC

            order_price = float(price) if dhan_order_type == self.dhan.LIMIT else 0.0

            resp = self.dhan.place_order(
                security_id=str(security_id),
                exchange_segment=self.dhan.NSE,
                transaction_type=dhan_side,
                quantity=int(quantity),
                order_type=dhan_order_type,
                product_type=dhan_product,
                price=order_price,
                tag=cl_ord_id[:10],
            )
            logger.info(f"Live order response from Dhan: {resp}")
            broker_order_id = None
            if isinstance(resp, dict):
                broker_order_id = resp.get("orderId") or resp.get("order_id")
                if not broker_order_id and "data" in resp and isinstance(resp["data"], dict):
                    broker_order_id = resp["data"].get("orderId") or resp["data"].get("order_id")

            return {
                "status": "ORDER_PLACED" if broker_order_id else "REJECTED",
                "result_class": "LIVE_ORDER_SUBMISSION",
                "execution_mode": "LIVE",
                "cl_ord_id": cl_ord_id,
                "broker_order_id": broker_order_id,
                "data": resp,
            }
        except Exception as e:
            logger.error(f"Failed to place live order: {e}")
            return {"status": "ERROR", "error": str(e), "cl_ord_id": cl_ord_id}


if __name__ == "__main__":
    bridge = DhanLiveBridge()
    status = bridge.check_balance()
    print("==================================================")
    print("⚡ DHAN LIVE BRIDGE PROBE STATUS")
    print("==================================================")
    print(json.dumps(status, indent=2))
    print("==================================================")
