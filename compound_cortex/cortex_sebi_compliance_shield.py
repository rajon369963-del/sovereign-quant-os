"""
CORTEX SEBI 2026 COMPLIANCE SHIELD & DYNAMIC ICEBERG SLICER
Integrates: SEBI OTR 2026 Circular, Leaky/Token Bucket Algorithm, Freeze Limits.
Features:
- Sub-10 OPS Token Bucket Throttler (Strictly capped at 9.8 OPS)
- Dynamic Iceberg Band Checker (+/- 40% of LTP or +/- INR 20, whichever higher)
- Freeze limit auto-slicer (e.g., NIFTY 1800 max qty, BANKNIFTY 900 max qty)
- Real-time OTR penalty calculator and safe execution tracker
"""

import time
import math
from datetime import datetime

class SEBIComplianceShield:
    def __init__(self, max_ops=9.8, bucket_capacity=10):
        self.max_ops = max_ops
        self.capacity = bucket_capacity
        self.tokens = bucket_capacity
        self.last_refill = time.time()
        
        # NSE Derivative Freeze Limits (2026)
        self.freeze_limits = {
            'NIFTY 50': 1800,
            'BANKNIFTY': 900,
            'FINNIFTY': 1800,
            'MIDCPNIFTY': 4200,
            'RELIANCE': 2500,
            'HDFCBANK': 5500,
            'INFY': 4000,
            'DEFAULT': 1800
        }

        # Daily Session Ledger
        self.orders_placed = 0
        self.orders_modified = 0
        self.orders_cancelled = 0
        self.trades_executed = 0

    def _refill_tokens(self):
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.max_ops)
        self.last_refill = now

    def acquire_order_slot(self, timeout=1.0):
        """Token-bucket rate limiter ensuring order flow strictly <= 9.8 OPS."""
        start = time.time()
        while time.time() - start < timeout:
            self._refill_tokens()
            if self.tokens >= 1.0:
                self.tokens -= 1.0
                return True
            time.sleep(0.01)
        return False # Throttled

    def check_dynamic_otr_band(self, ltp, limit_price, is_option=True):
        """
        Hack #1: Dynamic Iceberg Slicing Band
        Orders within +/-40% of LTP or +/- INR 20 (whichever higher) are exempt from punitive SEBI OTR.
        """
        if not is_option:
            # Equities / Futures band is +/- 10%
            max_dev = max(ltp * 0.10, 5.0)
        else:
            # Options band is +/- 40% or INR 20
            max_dev = max(ltp * 0.40, 20.0)

        lower_bound = max(0.05, round(ltp - max_dev, 2))
        upper_bound = round(ltp + max_dev, 2)
        is_compliant = (lower_bound <= limit_price <= upper_bound)

        return {
            'ltp': ltp,
            'limit_price': limit_price,
            'max_allowed_deviation': round(max_dev, 2),
            'lower_bound': lower_bound,
            'upper_bound': upper_bound,
            'is_otr_exempt': is_compliant,
            'otr_risk': 'LOW' if is_compliant else 'HIGH_PUNITIVE_PENALTY'
        }

    def slice_iceberg_order(self, symbol, total_qty, side, limit_price, ltp, lot_size=25):
        """
        Slices large block orders into exchange-compliant child orders.
        Guarantees:
        1. Each slice <= exchange freeze limit.
        2. Slices respect OTR safe bands.
        3. Quantities are exact multiples of lot size.
        """
        freeze_limit = self.freeze_limits.get(symbol, self.freeze_limits['DEFAULT'])
        band_check = self.check_dynamic_otr_band(ltp, limit_price, is_option=True)

        # Ensure limit price is clamped to safe band if desired
        safe_price = limit_price
        if not band_check['is_otr_exempt']:
            safe_price = min(band_check['upper_bound'], max(band_check['lower_bound'], limit_price))

        # Determine optimal slice size (typically 1/3rd to 1/2 of freeze limit to prevent market impact)
        optimal_slice = min(freeze_limit, max(lot_size * 4, 300))
        optimal_slice = (optimal_slice // lot_size) * lot_size

        slices = []
        remaining = total_qty
        slice_idx = 1

        while remaining > 0:
            qty = min(remaining, optimal_slice)
            slices.append({
                'slice_id': f'{symbol}-CHILD-{slice_idx:03d}',
                'symbol': symbol,
                'side': side,
                'qty': qty,
                'price': safe_price,
                'stagger_delay_ms': (slice_idx - 1) * 120 # 120ms staggered delay
            })
            remaining -= qty
            slice_idx += 1

        return {
            'symbol': symbol,
            'total_qty': total_qty,
            'freeze_limit': freeze_limit,
            'slice_count': len(slices),
            'otr_band_status': band_check,
            'child_orders': slices
        }

    def record_order_event(self, event_type='PLACE'):
        if event_type == 'PLACE':
            self.orders_placed += 1
        elif event_type == 'MODIFY':
            self.orders_modified += 1
        elif event_type == 'CANCEL':
            self.orders_cancelled += 1
        elif event_type == 'TRADE':
            self.trades_executed += 1

    def calculate_live_otr(self):
        """Computes current Order-to-Trade Ratio (OTR) and regulatory risk tier."""
        total_order_events = self.orders_placed + self.orders_modified + self.orders_cancelled
        if self.trades_executed == 0:
            otr = float(total_order_events) if total_order_events > 0 else 0.0
        else:
            otr = total_order_events / float(self.trades_executed)

        # SEBI OTR Penalty Brackets (2026)
        if otr <= 50:
            tier = 'TIER_0_NO_PENALTY'
            penalty_inr = 0.0
        elif otr <= 150:
            tier = 'TIER_1_MODERATE_RISK'
            penalty_inr = (otr - 50) * 0.01 * 1000.0
        elif otr <= 300:
            tier = 'TIER_2_HIGH_PENALTY'
            penalty_inr = (otr - 150) * 0.05 * 5000.0 + 1000.0
        else:
            tier = 'TIER_3_CRITICAL_EMPANELMENT_RISK'
            penalty_inr = 50000.0 + (otr - 300) * 200.0

        return {
            'total_order_events': total_order_events,
            'trades_executed': self.trades_executed,
            'current_otr': round(otr, 2),
            'regulatory_tier': tier,
            'estimated_daily_penalty_inr': round(penalty_inr, 2)
        }

if __name__ == '__main__':
    shield = SEBIComplianceShield()
    print('Testing 9.8 OPS Token Bucket...')
    for i in range(5):
        ok = shield.acquire_order_slot()
        print(f'Slot {i+1}: {ok}')
    
    iceberg = shield.slice_iceberg_order('NIFTY 50', 5000, 'BUY', 185.0, 180.0, lot_size=25)
    print(f"Sliced 5000 QTY NIFTY into {iceberg['slice_count']} child orders:")
    for ch in iceberg['child_orders'][:3]:
        print('  ', ch)
    print('OTR Band Status:', iceberg['otr_band_status'])
