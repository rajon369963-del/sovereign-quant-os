# TASK 018: Sovereign Quant OS Cross-Venue Arbitrage Harvester & Risk Gatekeeper

- **Task ID**: `TASK_018`
- **Priority**: Critical
- **Weight**: 40% (Trading Domain - Focus 3)
- **Target Lanes**: `Lane 08` (Security & Privacy Court), `Lane 10` (Federation Steward / Arbitration Court)
- **Primary Repository**: `rajon369963-del/sovereign-quant-os`
- **Status**: `QUEUED`
- **Created**: 2026-09-11T05:30:00+05:30

## Objective
Evaluate cross-venue pricing deltas and risk gatekeeper tripwires:
1. **Cross-Venue Triangular & Statistical Arbitrage**:
   - Verify `cross_venue_arbitrage_harvester.py` calculation of triangular spread after deducting broker commission, STT, exchange turnover, and slippage buffers.
   - Confirm negative EV trades are rejected before order packet serialization.
2. **Risk Gatekeeper Max-Drawdown Circuit Breakers**:
   - Verify that when simulated drawdowns exceed strict percentage thresholds, all open orders are immediately canceled and new entries halted.
   - Reconcile paper trading ledger against virtual broker positions to ensure zero drift.

## Deliverable & Invariants
- Run `test_wire_bridge_and_reconciliation_battery.py` and verify 100% pass rate.
- Document test outcomes with execution receipt in `tasks/completed/`.
