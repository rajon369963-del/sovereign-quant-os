import asyncio
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from dhan_live_autonomous_bot import DhanAutonomousSniperBot, QuoteAuthorityError
from dhan_sniper_momentum_engine import SNIPER_UNIVERSE

SYMBOL = next(iter(SNIPER_UNIVERSE))


class SimulatedBridge:
    def get_market_quote(self, security_id, exchange_segment="NSE_EQ"):
        return {
            "status": "SIMULATED",
            "result_class": "SIMULATED_MARKET_QUOTE",
            "execution_mode": "SIMULATED",
            "connection_authority": "ABSENT",
            "is_simulated": True,
            "simulated_ltp_hint": 100.0,
        }


class MalformedAuthorityBridge:
    def get_market_quote(self, security_id, exchange_segment="NSE_EQ"):
        return {
            "status": "SUCCESS",
            "result_class": "LIVE_MARKET_QUOTE",
            "execution_mode": "LIVE",
            "connection_authority": "PRESENT",
            "is_simulated": False,
            "data": {"last_price": 101.25, "depth": {"buy": [], "sell": []}},
        }


class AuthoritativeBridge:
    def __init__(self):
        self.calls = 0

    def get_market_quote(self, security_id, exchange_segment="NSE_EQ"):
        self.calls += 1
        return {
            "status": "SUCCESS",
            "result_class": "LIVE_MARKET_QUOTE",
            "execution_mode": "LIVE",
            "connection_authority": "PRESENT",
            "is_simulated": False,
            "data": {
                "last_price": 101.25,
                "timestamp": "2026-09-16T09:30:00+05:30",
                "depth": {
                    "buy": [{"price": 101.20, "quantity": 10}],
                    "sell": [{"price": 101.30, "quantity": 12}],
                },
            },
        }


class SquareOffEngine:
    def __init__(self):
        self.active_position = {"symbol": SYMBOL, "status": "OPEN"}
        self.close_calls = 0

    def is_square_off_time(self):
        return True

    async def close_position(self, price, reason):
        self.close_calls += 1
        return {"status": "POSITION_CLOSED"}


def make_bot(*, dry_run, bridge):
    bot = DhanAutonomousSniperBot.__new__(DhanAutonomousSniperBot)
    bot.dry_run = dry_run
    bot.bridge = bridge
    bot._quote_cache = {}
    bot._quote_authority = {}
    return bot


class DhanLiveQuoteAuthorityCourt(unittest.TestCase):
    def test_live_mode_rejects_simulated_fallback(self):
        bot = make_bot(dry_run=False, bridge=SimulatedBridge())
        with self.assertRaises(QuoteAuthorityError):
            bot.fetch_live_quote(SYMBOL)
        state = bot._quote_authority[SYMBOL]
        self.assertEqual(state["source"], "UNAVAILABLE")
        self.assertIs(state["decision_eligible"], False)

    def test_live_mode_rejects_malformed_authoritative_envelope(self):
        bot = make_bot(dry_run=False, bridge=MalformedAuthorityBridge())
        with self.assertRaises(QuoteAuthorityError):
            bot.fetch_live_quote(SYMBOL)
        self.assertIs(bot._quote_authority[SYMBOL]["decision_eligible"], False)

    def test_dry_run_keeps_synthetic_fallback_truth_labelled(self):
        bot = make_bot(dry_run=True, bridge=SimulatedBridge())
        quote = bot.fetch_live_quote(SYMBOL)
        self.assertEqual(quote["source"], "SYNTHETIC_FALLBACK")
        self.assertIs(quote["decision_eligible"], True)
        self.assertIsNone(quote["provider_timestamp"])

    def test_authoritative_live_quote_remains_decision_eligible_and_cache_is_typed(self):
        bridge = AuthoritativeBridge()
        bot = make_bot(dry_run=False, bridge=bridge)
        first = bot.fetch_live_quote(SYMBOL)
        second = bot.fetch_live_quote(SYMBOL)
        self.assertEqual(first["source"], "LIVE_PROVIDER")
        self.assertEqual(second["source"], "CACHE_LIVE_PROVIDER")
        self.assertIs(first["decision_eligible"], True)
        self.assertIs(second["decision_eligible"], True)
        self.assertEqual(first["symbol"], SYMBOL)
        self.assertEqual(first["security_id"], str(SNIPER_UNIVERSE[SYMBOL]["security_id"]))
        self.assertEqual(bridge.calls, 1)

    def test_live_square_off_makes_zero_close_calls_without_quote_authority(self):
        bot = make_bot(dry_run=False, bridge=SimulatedBridge())
        bot.engine = SquareOffEngine()
        with self.assertRaises(QuoteAuthorityError):
            asyncio.run(bot.run_single_iteration())
        self.assertEqual(bot.engine.close_calls, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
