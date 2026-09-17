import subprocess
import json
import time

# Read the live feed pulse
with open("/Users/rajondas/teamwork_projects/sovereign-quant-os/LIVE_INGESTION_FEED_PULSE_17SEP.txt", "r") as f:
    feed_digest = f.read()

prompt = f"""[LIVE REAL-TIME INGESTION & DUAL-GRAPH HYPER-EXTENDED RAG DIRECTIVE - 17 SEP 2026]

PART 1: REAL-TIME INGESTED DATA INJECTION (YOUTUBE STREAMS & GOOGLE NEWS FEED)
{feed_digest[:3500]}

PART 2: CURRENT PHYSICAL BROKER TRUTH (DHAN v2 DMA)
- Account SOD Limit: ₹918.43. Cash Available: ₹370.73 (5x Intraday Buying Power: ₹1,853.65).
- Active Open Positions:
  * PNB: LONG 14 shares @ ₹118.32 (Realized +₹8.82, Live Unrealized +₹4.06 -> Total +₹12.88). Stop Loss at ₹118.35 Breakeven Ratchet.
  * ITC: LONG 4 shares @ ₹267.00 (Live Unrealized +₹1.00). Stop Loss at ₹265.80.
  * TATASTEEL: Closed with -₹7.56.
  * Current Net P&L: +₹6.32 Net Profit.
- Target: Full recovery of yesterday's -₹89.57 loss + ₹12 statutory taxes = +₹102.00 to +₹125.00 Total Net Session Profit.
- Founder Invariant: Do NOT rigidly just "sell and sit". Maintain dynamic, live updates from incoming news. Capture maximum upside on winners (PNB & ITC) without overtrading or excessive churning.

PART 3: HYPER-EXTENDED GRAPH SYNTHESIS MANDATE
Grounded in this notebook's 200+ Quantitative Repositories (NautilusTrader, VectorBT, Riskfolio-Lib, Order Flow Imbalance, vollib, statsmodels, ta-lib, qstrader):

Construct a comprehensive, multi-layer HYPER-EXTENDED KNOWLEDGE GRAPH for our mid-day session:
1. NODES (Define at least 8 key nodes):
   - Macro Driver Nodes (0-DTE Sensex Short Covering, PSU Credit Expansion, NSE IPO Liquidity Inflow)
   - Microstructure Nodes (Level-2 Order Flow Imbalance OFI_t, Ornstein-Uhlenbeck Drift, ATR Chandelier Exit)
   - Asset Nodes (PNB_Equity, ITC_Defensive, RBLBANK_Breakout, YESBANK_Support)
2. EDGES & CAUSAL TRANSMISSION (Define explicit directional relationships):
   - How incoming macro/news events transmit directly into L2 order queue imbalances.
   - Asymmetric profit ladder: How PNB & ITC trailing stops expand upside while keeping downside locked at ₹0.00.
3. DYNAMIC REBALANCING & EXECUTION HARNESS:
   - Specific thresholds to add or scale without exceeding 2-3 total high-conviction trades and ₹2,500-₹3,000 turnover cap.
   - Exact mathematical formula for achieving the +₹102 target while capping risk at < 1.25% per trade.
"""

escaped_prompt = json.dumps(prompt)

js_code = f"""
(() => {{
    const ta = document.querySelector('textarea.query-box-input');
    if (!ta) return 'TEXTAREA_NOT_FOUND';
    ta.focus();
    ta.value = {escaped_prompt};
    ta.dispatchEvent(new Event('input', {{ bubbles: true }}));
    ta.dispatchEvent(new Event('change', {{ bubbles: true }}));
    
    // Simulate Enter key press
    const event = new KeyboardEvent('keydown', {{
        bubbles: true,
        cancelable: true,
        key: 'Enter',
        code: 'Enter',
        keyCode: 13,
        which: 13
    }});
    ta.dispatchEvent(event);
    
    const submitBtn = document.querySelector('button[aria-label="Submit"]');
    if (submitBtn) {{
        if (submitBtn.disabled) {{
            submitBtn.removeAttribute('disabled');
            submitBtn.classList.remove('mat-mdc-button-disabled');
        }}
        submitBtn.click();
        return 'SUBMITTED_SUCCESSFULLY';
    }}
    return 'SUBMIT_BTN_NOT_FOUND';
}})()
"""

apple_script = f'tell application "Google Chrome" to execute active tab of front window javascript "{js_code.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"'

res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
print("Result:", res.stdout.strip())
