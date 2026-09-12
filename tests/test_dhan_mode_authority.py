import os

os.environ.pop("DHAN_CLIENT_ID", None)
os.environ.pop("DHAN_ACCESS_TOKEN", None)

from dhan_live_bridge import DhanLiveBridge


LIVE_SUCCESS_STATUSES = {"ORDER_PLACED", "LIVE_EXECUTED", "SUCCESS"}
LIVE_RESULT_CLASSES = {"LIVE_ORDER_SUBMISSION", "LIVE_ACCOUNT_SNAPSHOT", "LIVE_MARKET_QUOTE"}


def assert_not_live_authority(result):
    assert result["execution_mode"] == "SIMULATED"
    assert result["connection_authority"] == "ABSENT"
    assert result["is_simulated"] is True
    assert result["status"] not in LIVE_SUCCESS_STATUSES
    assert result["result_class"] not in LIVE_RESULT_CLASSES
    assert result.get("broker_order_id") is None


def test_disconnected_order_is_unrepresentable_as_live_success():
    bridge = DhanLiveBridge(client_id="", access_token="")
    result = bridge.place_canary_order("TEST", "123", quantity=1)

    assert_not_live_authority(result)
    assert result["status"] == "SIMULATED"
    assert result["result_class"] == "SIMULATED_ORDER"
    assert "PROBE_SUCCESS" not in result.values()


def test_disconnected_balance_and_quote_do_not_use_live_value_fields():
    bridge = DhanLiveBridge(client_id="", access_token="")

    balance = bridge.check_balance()
    quote = bridge.get_market_quote("123")

    assert_not_live_authority(balance)
    assert_not_live_authority(quote)
    assert balance["result_class"] == "SIMULATED_ACCOUNT_SNAPSHOT"
    assert quote["result_class"] == "SIMULATED_MARKET_QUOTE"
    assert "deposited_balance" not in balance
    assert "ltp" not in quote
    assert balance["simulated_balance_hint"] == 1.00
    assert quote["simulated_ltp_hint"] == 684.85


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


def test_stubbed_connected_authority_is_explicitly_live_without_network():
    bridge = DhanLiveBridge(client_id="offline", access_token="offline")
    bridge.dhan = FakeConnectedDhan()
    bridge.is_connected = True

    order = bridge.place_canary_order("TEST", "123", quantity=1)
    balance = bridge.check_balance()
    quote = bridge.get_market_quote("123")

    assert order["status"] == "ORDER_PLACED"
    assert order["result_class"] == "LIVE_ORDER_SUBMISSION"
    assert order["execution_mode"] == "LIVE"
    assert order["connection_authority"] == "PRESENT"
    assert order["is_simulated"] is False
    assert order["broker_order_id"] == "OFFLINE-STUB-123"

    assert balance["result_class"] == "LIVE_ACCOUNT_SNAPSHOT"
    assert quote["result_class"] == "LIVE_MARKET_QUOTE"
    assert balance["execution_mode"] == quote["execution_mode"] == "LIVE"


def test_mutant_generic_success_classifier_would_be_rejected_by_authority_contract():
    bridge = DhanLiveBridge(client_id="", access_token="")
    result = bridge.place_canary_order("TEST", "123")

    # This represents the dangerous downstream mutant: treating any truthy status as success.
    mutant_generic_success = bool(result.get("status"))
    assert mutant_generic_success is True

    # The real authority contract must still make live success impossible.
    real_live_success = (
        result.get("execution_mode") == "LIVE"
        and result.get("connection_authority") == "PRESENT"
        and result.get("is_simulated") is False
        and result.get("status") == "ORDER_PLACED"
        and bool(result.get("broker_order_id"))
    )
    assert real_live_success is False
