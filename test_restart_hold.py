import asyncio
import sqlite3
import tempfile
import unittest
from pathlib import Path

from live_broker_wire_bridge import LiveBrokerWireBridge, WireMode, WireOrderPayload, WireState


class RestartHoldTest(unittest.TestCase):
    def test_every_recovered_intent_holds_without_broker_evidence(self):
        for state in ('PENDING_NEW', 'SENT_TO_WIRE', 'INFLIGHT_UNKNOWN', 'OPEN', 'ACK_RECEIVED'):
            with self.subTest(state=state), tempfile.TemporaryDirectory() as tmp:
                db = Path(tmp) / 'orders.sqlite'
                first = LiveBrokerWireBridge(db, mode=WireMode.TESTNET_MOCK)
                order = WireOrderPayload('restart', 'TEST', 'MOCK', 'BUY', 10, 1, 'LIMIT',
                                         wire_state=WireState(state))
                first._sandwich_pre_commit(order)
                first._get_db().close()
                first.executor.shutdown()
                del first
                recovered = LiveBrokerWireBridge(db, mode=WireMode.TESTNET_MOCK)
                self.assertIn('restart', recovered.inflight_orders)
                asyncio.run(recovered.run_reconciliation_sweep())
                receipt = recovered.lookup_order('restart')
                self.assertEqual(receipt.wire_state.value, 'HOLD')
                self.assertIn('RECONCILE_REQUIRED', receipt.rejection_reason)
                asyncio.run(recovered.transmit_order(order))
                self.assertEqual(recovered.total_wire_sent, 0)
                with sqlite3.connect(db) as con:
                    self.assertEqual(con.execute('SELECT COUNT(*) FROM wire_state_audit_log').fetchone()[0], 1)
                recovered._get_db().close()
                recovered.executor.shutdown()
                again = LiveBrokerWireBridge(db, mode=WireMode.TESTNET_MOCK)
                self.assertTrue(again.is_halted)
                self.assertIn('restart', again.inflight_orders)
                again.executor.shutdown()


if __name__ == '__main__':
    unittest.main()
