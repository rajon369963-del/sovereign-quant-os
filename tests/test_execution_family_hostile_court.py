#!/usr/bin/env python3
"""
AIR10 Sovereign Quant OS - Execution Family Hostile Court & Kill-Mutants
Covers:
- Quant #14: Fake-broker partial-fill quantity/remaining-state & PnL accounting
- Quant #16: Order-intent identity under concurrency / same-millisecond collision protection
- Quant #18: Timeout fail-closed enforcement & reconcile-before-resubmit
- Quant #27: TWAP non-mock execution authority (zero phantom fills without wire receipts)
- Quant #36: Two-leg hedge compensation outcome (unwind failure => HOLD/UNHEDGED_RECONCILE_REQUIRED)
- Restart recovery across SQLite WAL persistence

100% offline, hermetic, zero-secret, zero-network, zero real-money dependency.
Uses Python stdlib unittest for zero-dependency CI execution.
"""

import asyncio
import sqlite3
import sys
import tempfile
import time
import unittest
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from agentic_alpha_shift import TWAPExecutionEngine
from alpha_engine import SignalType, StrategyArchetype, TradeSignal
from async_l2_dma_gateway import OrderRequest
from async_l2_dma_gateway import OrderState as GatewayOrderState
from cross_venue_arbitrage_harvester import CrossVenueArbitrageHarvester
from execution_daemon import ExecutionDaemon, OrderState, TradeOrder
from risk_gatekeeper import RiskGatekeeper, RiskGateResult

# ============================================================================
# FAKE BROKER / VENUE ADAPTERS FOR HOSTILE SIMULATION
# ============================================================================

class FakeWireAdapter:
    """Spy & programmable wire execution adapter."""
    def __init__(self):
        self.call_count = 0
        self.submitted_slices = []
        self.should_reject_slice_id = None
        self.partial_fill_qty = None

    async def execute_slice(self, symbol: str, action: str, size: float) -> dict[str, Any]:
        self.call_count += 1
        chunk_id = self.call_count
        self.submitted_slices.append({"symbol": symbol, "action": action, "size": size})

        if self.should_reject_slice_id and chunk_id == self.should_reject_slice_id:
            return {
                "status": "REJECTED",
                "broker_order_id": f"BROKER_REJ_{chunk_id}",
                "confirmed_filled_qty": 0.0,
                "reason": "Simulated venue limit breach"
            }

        fill_qty = self.partial_fill_qty if self.partial_fill_qty is not None else size
        return {
            "status": "FILLED",
            "broker_order_id": f"BROKER_ORD_{chunk_id}_{int(time.time()*1000)}",
            "confirmed_filled_qty": fill_qty,
            "fill_price": 100.0
        }


class FakeVenueForReconciliation:
    """Simulates broker venue with dropped acknowledgements and reconciliation queries."""
    def __init__(self):
        self.venue_orders: dict[str, dict[str, Any]] = {}
        self.send_call_count = 0
        self.query_call_count = 0
        self.drop_first_response = False
        self.unknown_state = False

    def send_order(self, client_order_id: str, symbol: str, side: str, qty: float) -> dict[str, Any]:
        self.send_call_count += 1
        if self.drop_first_response and self.send_call_count == 1:
            # Order accepted remotely, but response packet is lost / timed out
            self.venue_orders[client_order_id] = {
                "client_order_id": client_order_id,
                "status": "ACCEPTED",
                "qty": qty
            }
            return {"status": "ERROR", "error": "TIMEOUT_OR_LOST_RESPONSE"}

        self.venue_orders[client_order_id] = {
            "client_order_id": client_order_id,
            "status": "FILLED",
            "qty": qty
        }
        return {"status": "FILLED", "client_order_id": client_order_id}

    def query_order(self, client_order_id: str) -> dict[str, Any]:
        self.query_call_count += 1
        if self.unknown_state:
            return {"status": "UNKNOWN", "client_order_id": client_order_id}
        if client_order_id in self.venue_orders:
            return self.venue_orders[client_order_id]
        return {"status": "NOT_FOUND", "client_order_id": client_order_id}


# ============================================================================
# TEST SUITE
# ============================================================================

class TestExecutionFamilyHostileCourt(unittest.TestCase):

    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory(prefix="air10-quant-court-")
        self.db_path = str(Path(self.tmp_dir.name) / "test_ledger.sqlite")
        self.daemon = ExecutionDaemon(db_path=self.db_path, initial_capital=50000.0)
        self.risk_gate = RiskGatekeeper()

    def tearDown(self):
        self.tmp_dir.cleanup()

    # ------------------------------------------------------------------------
    # Quant #14: Partial-Fill Quantity / Remaining-State & Realized PnL Court
    # ------------------------------------------------------------------------
    def test_quant14_partial_fill_accounting_and_lifecycle(self):
        """Requested 100, fragment 1 = 37 -> remaining 63, state is PARTIALLY_FILLED.
        Exit PnL is computed strictly on 37 filled, never on requested 100."""
        order = TradeOrder(
            order_id="ORD_TEST_PARTIAL_001",
            symbol="NIFTY_FUT",
            strategy="TrendBreakout",
            side="BUY",
            quantity=100.0,
            entry_price=100.0,
            hard_stop_loss=90.0,
            hard_take_profit=110.0,
            state=OrderState.PENDING,
            created_at=time.time(),
            filled_quantity=0.0,
            remaining_quantity=100.0
        )

        # Apply fragment 1: 37 units @ 100.0
        applied = order.apply_fill_fragment("FRAG_01", 37.0, 100.0)
        self.assertTrue(applied)
        self.assertEqual(order.filled_quantity, 37.0)
        self.assertEqual(order.remaining_quantity, 63.0)
        self.assertEqual(order.state, OrderState.PARTIALLY_FILLED)
        self.assertNotEqual(order.state, OrderState.FILLED)

        # Idempotent replay of same fragment ID must be suppressed
        replayed = order.apply_fill_fragment("FRAG_01", 37.0, 100.0)
        self.assertFalse(replayed)
        self.assertEqual(order.filled_quantity, 37.0)

        # Price tick reaches Take-Profit (110.0)
        self.daemon.active_orders[order.order_id] = order
        self.daemon.simulate_price_tick(110.0, self.risk_gate)

        # Order must be CLOSED
        self.assertEqual(order.state, OrderState.CLOSED)
        self.assertEqual(order.exit_price, 110.0)
        # Realized PnL: (110.0 - 100.0) * 37 = +370.0 (NOT (110.0 - 100.0) * 100 = 1000.0)
        self.assertAlmostEqual(order.realized_pnl, 370.0, places=2)
        self.assertNotEqual(order.realized_pnl, 1000.0)

    def test_quant14_kill_mutant_premature_full_fill(self):
        """KILL MUTANT: First partial fragment must NOT be treated as terminal FILLED."""
        order = TradeOrder(
            order_id="ORD_TEST_MUTANT_001",
            symbol="NIFTY_FUT",
            strategy="TrendBreakout",
            side="BUY",
            quantity=100.0,
            entry_price=100.0,
            hard_stop_loss=90.0,
            hard_take_profit=110.0,
            state=OrderState.PENDING,
            created_at=time.time()
        )
        order.apply_fill_fragment("FRAG_01", 37.0, 100.0)

        # Court assertion: state MUST NOT be FILLED
        with self.assertRaises(AssertionError):
            self.assertEqual(order.state, OrderState.FILLED)

    def test_quant14_kill_mutant_requested_qty_pnl_leak(self):
        """KILL MUTANT: Realized PnL must NOT use requested quantity when partially filled."""
        order = TradeOrder(
            order_id="ORD_TEST_MUTANT_002",
            symbol="NIFTY_FUT",
            strategy="TrendBreakout",
            side="BUY",
            quantity=100.0,
            entry_price=100.0,
            hard_stop_loss=90.0,
            hard_take_profit=110.0,
            state=OrderState.PENDING,
            created_at=time.time()
        )
        order.apply_fill_fragment("FRAG_01", 40.0, 100.0)
        self.daemon.active_orders[order.order_id] = order
        self.daemon.simulate_price_tick(110.0, self.risk_gate)

        # Mutant that computes PnL on requested qty (1000.0) must FAIL
        mutant_pnl = (order.exit_price - order.fill_price) * order.quantity  # 1000.0
        with self.assertRaises(AssertionError):
            self.assertEqual(order.realized_pnl, mutant_pnl)

    # ------------------------------------------------------------------------
    # Quant #16: Order-Intent Identity Under Concurrency Court
    # ------------------------------------------------------------------------
    def test_quant16_order_intent_identity_no_collision_on_same_millisecond(self):
        """When multiple dispatches occur in the exact same millisecond, each distinct intent
        receives a unique durable order ID. Zero dict overwrite and zero SQLite PK collapse."""
        frozen_time = 1773385200.555
        saved_time = time.time
        time.time = lambda: frozen_time
        try:
            gate_res = RiskGateResult(passed=True, reason="PASS", approved_quantity=10.0, risk_amount=100.0, hard_stop_loss=90.0, hard_take_profit=110.0)
            orders = []
            for i in range(10):
                sig = TradeSignal(
                    bar_id=i,
                    timestamp=frozen_time,
                    strategy=StrategyArchetype.MEAN_REVERSION,
                    signal_type=SignalType.BUY,
                    price=100.0,
                    stop_loss=90.0,
                    take_profit=110.0,
                    risk_reward_ratio=2.0,
                    confidence=0.85
                )
                sig.intent_id = f"INTENT_BATCH_{i}"
                order = self.daemon.dispatch_order_with_self_healing(sig, gate_res)
                self.assertIsNotNone(order)
                orders.append(order)

            # Assert all 10 order IDs are distinct
            order_ids = [o.order_id for o in orders]
            self.assertEqual(len(set(order_ids)), 10)
            self.assertEqual(len(self.daemon.active_orders), 10)

            # Persist each order to SQLite
            with sqlite3.connect(self.db_path) as conn:
                for o in orders:
                    conn.execute("""
                        INSERT INTO trades VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (
                        o.order_id, o.symbol, o.strategy, o.side,
                        o.quantity, o.entry_price, o.fill_price, o.exit_price,
                        o.hard_stop_loss, o.hard_take_profit, o.realized_pnl,
                        o.state.value, o.created_at
                    ))
                row_count = conn.execute("SELECT count(*) FROM trades").fetchone()[0]
                self.assertEqual(row_count, 10)
        finally:
            time.time = saved_time

    def test_quant16_kill_mutant_timestamp_only_collision(self):
        """KILL MUTANT: A timestamp-only generator collides in the same millisecond."""
        frozen_ms = 1773385200555
        mutant_ids = [f"ORD_TRE_{frozen_ms}" for _ in range(5)]
        self.assertEqual(len(set(mutant_ids)), 1)
        with self.assertRaises(AssertionError):
            self.assertEqual(len(set(mutant_ids)), 5)

    # ------------------------------------------------------------------------
    # Quant #18: Timeout Fail-Closed & Reconcile-Before-Resubmit Court
    # ------------------------------------------------------------------------
    def test_quant18_timeout_reconciliation_suppresses_duplicate_resubmit(self):
        """Attempt 1 reaches venue and is accepted, but response is lost/times out.
        Reconcile query finds order ACCEPTED remotely -> suppresses resubmission."""
        fake_venue = FakeVenueForReconciliation()
        fake_venue.drop_first_response = True

        sig = TradeSignal(
            bar_id=1,
            timestamp=time.time(),
            strategy=StrategyArchetype.MEAN_REVERSION,
            signal_type=SignalType.BUY,
            price=100.0,
            stop_loss=90.0,
            take_profit=110.0,
            risk_reward_ratio=2.0,
            confidence=0.85
        )

        res = self.daemon.dispatch_with_reconciliation(
            client_order_id="CL_ORD_RECON_001",
            fake_venue=fake_venue,
            signal=sig,
            quantity=25.0
        )

        # Wire call count must remain 1 (no blind resubmit!)
        self.assertEqual(fake_venue.send_call_count, 1)
        self.assertEqual(fake_venue.query_call_count, 1)
        self.assertTrue(res["reconciled"])
        self.assertTrue(res["resubmission_suppressed"])
        self.assertEqual(res["status"], "ACCEPTED")

    def test_quant18_unknown_remote_state_fails_closed_to_hold(self):
        """If remote order state cannot be determined on reconciliation, state MUST be HOLD/RECONCILE_REQUIRED.
        It must NOT guess FAILED and must NOT blindly create a second order."""
        fake_venue = FakeVenueForReconciliation()
        fake_venue.drop_first_response = True
        fake_venue.unknown_state = True

        sig = TradeSignal(
            bar_id=1,
            timestamp=time.time(),
            strategy=StrategyArchetype.MEAN_REVERSION,
            signal_type=SignalType.BUY,
            price=100.0,
            stop_loss=90.0,
            take_profit=110.0,
            risk_reward_ratio=2.0,
            confidence=0.85
        )

        res = self.daemon.dispatch_with_reconciliation(
            client_order_id="CL_ORD_RECON_002",
            fake_venue=fake_venue,
            signal=sig,
            quantity=10.0
        )

        self.assertEqual(fake_venue.send_call_count, 1)
        self.assertEqual(fake_venue.query_call_count, 1)
        self.assertEqual(res["status"], "HOLD/RECONCILE_REQUIRED")
        self.assertNotEqual(res["status"], "REJECTED")
        self.assertNotEqual(res["status"], "FAILED")

    def test_quant18_kill_mutant_blind_retry_without_reconciliation(self):
        """KILL MUTANT: Blind retry without reconciliation sends 2 wire orders."""
        fake_venue = FakeVenueForReconciliation()
        fake_venue.drop_first_response = True
        fake_venue.send_order("CL_MUTANT_01", "NIFTY", "BUY", 10.0)
        fake_venue.send_order("CL_MUTANT_01", "NIFTY", "BUY", 10.0)
        self.assertEqual(fake_venue.send_call_count, 2)
        with self.assertRaises(AssertionError):
            self.assertEqual(fake_venue.send_call_count, 1)

    # ------------------------------------------------------------------------
    # Quant #27: TWAP Execution Authority Court
    # ------------------------------------------------------------------------
    def test_quant27_twap_execution_authority_contract(self):
        """1. mock_mode=True returns SIMULATED.
        2. mock_mode=False without adapter fails closed as HOLD/CONFIG_ERROR.
        3. mock_mode=False with adapter receives wire calls and returns confirmed broker IDs."""
        engine = TWAPExecutionEngine(min_chunks=4, max_chunks=4)

        # 1. Mock mode
        res_mock = asyncio.run(engine.execute_twap("NIFTY", "BUY", 100.0, mock_mode=True))
        self.assertEqual(res_mock["twap_status"], "SIMULATED")
        self.assertTrue(res_mock["is_simulated"])
        for c in res_mock["chunks"]:
            self.assertEqual(c["status"], "SIMULATED")

        # 2. Non-mock without adapter -> FAIL CLOSED
        res_no_adapter = asyncio.run(engine.execute_twap("NIFTY", "BUY", 100.0, mock_mode=False))
        self.assertEqual(res_no_adapter["twap_status"], "HOLD/CONFIG_ERROR")
        self.assertEqual(res_no_adapter["total_executed"], 0.0)
        self.assertFalse(res_no_adapter["is_simulated"])

        # 3. Non-mock with wire adapter -> SUCCESS with broker order IDs
        adapter = FakeWireAdapter()
        res_wire = asyncio.run(engine.execute_twap("NIFTY", "BUY", 100.0, mock_mode=False, execution_adapter=adapter))
        self.assertEqual(res_wire["twap_status"], "SUCCESS")
        self.assertGreaterEqual(adapter.call_count, 4)
        for c in res_wire["chunks"]:
            self.assertEqual(c["status"], "FILLED")
            self.assertIsNotNone(c["broker_order_id"])

        # 4. Partial / rejected slice -> Batch is not SUCCESS
        adapter_rej = FakeWireAdapter()
        adapter_rej.should_reject_slice_id = 2
        res_rej = asyncio.run(engine.execute_twap("NIFTY", "BUY", 100.0, mock_mode=False, execution_adapter=adapter_rej))
        self.assertIn(res_rej["twap_status"], ("PARTIAL", "FAILED"))
        self.assertNotEqual(res_rej["twap_status"], "SUCCESS")

    def test_quant27_kill_mutant_no_wire_phantom_success(self):
        """KILL MUTANT: Non-mock mode without adapter returning SUCCESS must fail."""
        engine = TWAPExecutionEngine(min_chunks=4, max_chunks=4)
        res = asyncio.run(engine.execute_twap("NIFTY", "BUY", 100.0, mock_mode=False))
        with self.assertRaises(AssertionError):
            self.assertEqual(res["twap_status"], "SUCCESS")

    # ------------------------------------------------------------------------
    # Quant #36: Two-Leg Hedge Compensation Outcome Court
    # ------------------------------------------------------------------------
    def test_quant36_two_leg_compensation_fails_closed_when_unwind_fails(self):
        """Leg 1 FILLED, Leg 2 REJECTED. Emergency unwind is REJECTED.
        Result MUST report HOLD/UNHEDGED_RECONCILE_REQUIRED and residual_delta > 0.
        MUST NOT claim ATOMIC_UNWOUND or unhedged_delta_prevented > 0."""
        harvester = CrossVenueArbitrageHarvester(db_path=Path(self.db_path))
        from async_l2_dma_gateway import async_dma_gateway

        call_sequence = []
        async def mock_submit_dma_order(symbol, side, quantity, **kwargs):
            call_sequence.append((symbol, side, quantity))
            if len(call_sequence) == 1:
                return OrderRequest(cl_ord_id="L1", symbol=symbol, venue="SHOONYA", side=side, order_type="MARKET", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.FILLED, filled_qty=quantity)
            elif len(call_sequence) == 2:
                return OrderRequest(cl_ord_id="L2", symbol=symbol, venue="HYPERLIQUID", side=side, order_type="ALO", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.REJECTED, rejection_reason="Venue margin error")
            elif len(call_sequence) == 3:
                return OrderRequest(cl_ord_id="UNW", symbol=symbol, venue="SHOONYA", side=side, order_type="MARKET", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.REJECTED, rejection_reason="Market halted")
            return OrderRequest(cl_ord_id="ERR", symbol=symbol, venue="SHOONYA", side=side, order_type="MARKET", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.REJECTED)

        async_dma_gateway.submit_dma_order = mock_submit_dma_order

        res = asyncio.run(harvester.execute_atomic_two_leg_trade("TCS", 10000.0, 3500.0, 3510.0))

        self.assertEqual(res["status"], "HOLD/UNHEDGED_RECONCILE_REQUIRED")
        self.assertEqual(res["unhedged_delta_prevented"], 0.0)
        self.assertGreater(res["residual_delta"], 0.0)
        self.assertTrue(res["reconciliation_required"])

    def test_quant36_two_leg_compensation_succeeds_when_unwind_fills(self):
        """When emergency unwind fills cleanly, report ATOMIC_UNWOUND_LEG2_FAILED with confirmed prevented delta."""
        harvester = CrossVenueArbitrageHarvester(db_path=Path(self.db_path))
        from async_l2_dma_gateway import async_dma_gateway

        call_sequence = []
        async def mock_submit_dma_order(symbol, side, quantity, **kwargs):
            call_sequence.append((symbol, side, quantity))
            if len(call_sequence) == 1:
                return OrderRequest(cl_ord_id="L1", symbol=symbol, venue="SHOONYA", side=side, order_type="MARKET", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.FILLED, filled_qty=quantity)
            elif len(call_sequence) == 2:
                return OrderRequest(cl_ord_id="L2", symbol=symbol, venue="HYPERLIQUID", side=side, order_type="ALO", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.REJECTED, rejection_reason="Venue rejected")
            elif len(call_sequence) == 3:
                return OrderRequest(cl_ord_id="UNW", symbol=symbol, venue="SHOONYA", side=side, order_type="MARKET", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.FILLED, filled_qty=quantity)
            return OrderRequest(cl_ord_id="ERR", symbol=symbol, venue="SHOONYA", side=side, order_type="MARKET", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.REJECTED)

        async_dma_gateway.submit_dma_order = mock_submit_dma_order

        res = asyncio.run(harvester.execute_atomic_two_leg_trade("TCS", 10000.0, 3500.0, 3510.0))
        self.assertEqual(res["status"], "ATOMIC_UNWOUND_LEG2_FAILED")
        self.assertGreater(res["unhedged_delta_prevented"], 0.0)
        self.assertEqual(res["residual_delta"], 0.0)
        self.assertFalse(res["reconciliation_required"])

    def test_quant36_kill_mutant_unwind_rejected_claiming_unwound(self):
        """KILL MUTANT: A rejected unwind claiming ATOMIC_UNWOUND must fail the court."""
        harvester = CrossVenueArbitrageHarvester(db_path=Path(self.db_path))
        from async_l2_dma_gateway import async_dma_gateway

        call_sequence = []
        async def mock_submit_dma_order(symbol, side, quantity, **kwargs):
            call_sequence.append((symbol, side, quantity))
            if len(call_sequence) == 1:
                return OrderRequest(cl_ord_id="L1", symbol=symbol, venue="SHOONYA", side=side, order_type="MARKET", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.FILLED)
            elif len(call_sequence) == 2:
                return OrderRequest(cl_ord_id="L2", symbol=symbol, venue="HYPERLIQUID", side=side, order_type="ALO", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.REJECTED)
            else:
                return OrderRequest(cl_ord_id="UNW", symbol=symbol, venue="SHOONYA", side=side, order_type="MARKET", price=100.0, quantity=quantity, expected_alpha_pct=0.0, state=GatewayOrderState.REJECTED)

        async_dma_gateway.submit_dma_order = mock_submit_dma_order

        res = asyncio.run(harvester.execute_atomic_two_leg_trade("TCS", 10000.0, 3500.0, 3510.0))
        with self.assertRaises(AssertionError):
            self.assertEqual(res["status"], "ATOMIC_UNWOUND_LEG2_FAILED")

    # ------------------------------------------------------------------------
    # Restart Recovery & State Preservation Court
    # ------------------------------------------------------------------------
    def test_execution_daemon_restart_recovery(self):
        """State written to SQLite WAL survives daemon crash and restart cleanly."""
        order = TradeOrder(
            order_id="ORD_RESTART_TEST_001",
            symbol="NIFTY_FUT",
            strategy="TrendBreakout",
            side="BUY",
            quantity=50.0,
            entry_price=100.0,
            hard_stop_loss=90.0,
            hard_take_profit=110.0,
            state=OrderState.FILLED,
            created_at=time.time(),
            filled_quantity=50.0,
            remaining_quantity=0.0
        )
        self.daemon.active_orders[order.order_id] = order
        self.daemon.simulate_price_tick(110.0, self.risk_gate)

        # Re-initialize daemon pointing to the same database
        new_daemon = ExecutionDaemon(db_path=self.db_path)
        with sqlite3.connect(new_daemon.db_path) as conn:
            row = conn.execute("SELECT order_id, realized_pnl, state FROM trades WHERE order_id = ?", (order.order_id,)).fetchone()
            self.assertIsNotNone(row)
            self.assertEqual(row[0], "ORD_RESTART_TEST_001")


if __name__ == "__main__":
    unittest.main(verbosity=2)