import os
import unittest

os.environ.pop("DHAN_CLIENT_ID", None)
os.environ.pop("DHAN_ACCESS_TOKEN", None)

from dhan_live_bridge import DhanLiveBridge


LIVE_SUCCESS_STATUSES = {"ORDER_PLACED", "LIVE_EXECUTED", "SUCCESS"}
LIVE_RESULT_CLASSES = {"LIVE_ORDER_SUBMISSION", "LIVE_ACCOUNT_SNAPSHOT", "LIVE_MARKET_QUOTE"}


class FakeConnectedDhan:
    NSE = "NSE"
    BUY = "BUY"
    MARKET = "MARKET"
    CNC = "CNC"

    def place_order(self, **kwargs):
        return {"orderId": "OFFLINE-STUB-123", "status": "stubbed"}

    def get_fund_limits(self):
        return {"availabelBalance": 1000.0}

    def quote_data(self, **kwargs):
        return {"ltp": 123.45}


class DhanModeAuthorityCourt(unittest.TestCase):
    def assert_not_live_authority(self, result):
        self.assertEqual(result["execution_mode"], "SIMULATED")
        self.assertEqual(result["connection_authority"], "ABSENT")
        self.assertIs(result["is_simulated"], True)
        self.assertNotIn(result["status"], LIVE_SUCCESS_STATUSES)
        self.assertNotIn(result["result_class"], LIVE_RESULT_CLASSES)
        self.assertIsNone(result.get("broker_order_id"))

    def test_disconnected_order_is_unrepresentable_as_live_success(self):
        bridge = DhanLiveBridge(client_id="", access_token="")
        result = bridge.place_canary_order("TEST", "123", quantity=1)

        self.assert_not_live_authority(result)
        self.assertEqual(result["status"], "SIMULATED")
        self.assertEqual(result["result_class"], "SIMULATED_ORDER")
        self.assertNotIn("PROBE_SUCCESS", result.values())

    def test_disconnected_balance_and_quote_do_not_use_live_value_fields(self):
        bridge = DhanLiveBridge(client_id="", access_token="")
        balance = bridge.check_balance()
        quote = bridge.get_market_quote("123")

        self.assert_not_live_authority(balance)
        self.assert_not_live_authority(quote)
        self.assertEqual(balance["result_class"], "SIMULATED_ACCOUNT_SNAPSHOT")
        self.assertEqual(quote["result_class"], "SIMULATED_MARKET_QUOTE")
        self.assertNotIn("deposited_balance", balance)
        self.assertNotIn("ltp", quote)
        self.assertEqual(balance["simulated_balance_hint"], 1.00)
        self.assertEqual(quote["simulated_ltp_hint"], 684.85)

    def test_stubbed_connected_authority_is_explicitly_live_without_network(self):
        bridge = DhanLiveBridge(client_id="", access_token="")
        bridge.dhan = FakeConnectedDhan()
        bridge.is_connected = True

        order = bridge.place_canary_order("TEST", "123", quantity=1)
        balance = bridge.check_balance()
        quote = bridge.get_market_quote("123")

        self.assertEqual(order["status"], "ORDER_PLACED")
        self.assertEqual(order["result_class"], "LIVE_ORDER_SUBMISSION")
        self.assertEqual(order["execution_mode"], "LIVE")
        self.assertEqual(order["connection_authority"], "PRESENT")
        self.assertIs(order["is_simulated"], False)
        self.assertEqual(order["broker_order_id"], "OFFLINE-STUB-123")
        self.assertEqual(balance["result_class"], "LIVE_ACCOUNT_SNAPSHOT")
        self.assertEqual(quote["result_class"], "LIVE_MARKET_QUOTE")
        self.assertEqual(balance["execution_mode"], "LIVE")
        self.assertEqual(quote["execution_mode"], "LIVE")

    def test_generic_status_truthiness_does_not_grant_live_authority(self):
        bridge = DhanLiveBridge(client_id="", access_token="")
        result = bridge.place_canary_order("TEST", "123")

        # Deliberately model the dangerous downstream mutant: any non-empty status is "success".
        self.assertTrue(bool(result.get("status")))

        real_live_success = (
            result.get("execution_mode") == "LIVE"
            and result.get("connection_authority") == "PRESENT"
            and result.get("is_simulated") is False
            and result.get("status") == "ORDER_PLACED"
            and bool(result.get("broker_order_id"))
        )
        self.assertFalse(real_live_success)


if __name__ == "__main__":
    unittest.main(verbosity=2)
