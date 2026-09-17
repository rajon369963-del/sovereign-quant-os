import subprocess
import json
import time

prompt = """DEEP QUANTITATIVE STRATEGY & RISK HARNESS INQUIRY - 17 SEP 2026 MID-DAY EXPIRY

Context & Current State:
1. Broker Truth (Dhan v2 Live):
   - SOD Starting Capital: ₹918.43.
   - Active Live Portfolio:
     * PNB: LONG 14 shares @ ₹118.32 (Realized Profit: +₹8.82, Current LTP: ~₹118.45).
     * ITC: LONG 4 shares @ ₹267.00 (Current LTP: ~₹267.10).
     * TATASTEEL: Closed with -₹7.56.
     * Cash available: ₹370.73, Utilized Intraday Margin (5x): ₹547.00.
     * Net target recovery needed: ~₹98 to ₹102 to cover yesterday's statutory slippage/taxes and flip account fully green.

2. Macro Sentiment & Ingested Live Feeds (17 Sep 2026):
   - Nifty holding 23,100 support; Bank Nifty 55,700 base. 0-DTE Sensex expiry showing strong short-covering bias in PSU and FMCG/Banking majors.
   - PNB boosted by dividend payout announcement and credit expansion.
   - Tata Group & Banking sectors experiencing positive sector-momentum rotation.

3. Available Codebase & Quantitative Repos in this Notebook:
   - Order Flow Imbalance (OFI) & L2/L3 order book dynamics.
   - VectorBT, NautilusTrader, Riskfolio-Lib, PyPortfolioOpt, statsmodels, ta-lib, qlib, qstrader.

Questions for Quantitative Repos:
1. PNB & ITC Mid-Day Management:
   Based on volatility regimes and trailing stop algorithms (Chandelier Exit / ATR Trailing / OFI delta reversal), how should we dynamically scale out or trail stop-losses for our PNB (14 shares @ 118.32) and ITC (4 shares @ 267.00) positions during the 10:00 AM - 12:30 PM expiry session?
2. Capital Allocation & Half-Kelly Sizing:
   With ₹370 remaining available margin, what is the optimal position size and risk allocation if another 3-Gate Sniper signal triggers (e.g. RBL Bank, Yes Bank, HDFC Bank)?
3. Mathematical Variance Shield:
   How do we structure our take-profit threshold so that we hit the +₹102 target while capping maximum draw-down to < 2.5% of SOD capital?"""

escaped_prompt = json.dumps(prompt)

js_code = f"""
(() => {{
    const ta = document.querySelector('textarea.query-box-input');
    if (!ta) return 'TEXTAREA_NOT_FOUND';
    ta.focus();
    ta.value = {escaped_prompt};
    ta.dispatchEvent(new Event('input', {{ bubbles: true }}));
    ta.dispatchEvent(new Event('change', {{ bubbles: true }}));
    
    // Find submit button
    const submitBtn = document.querySelector('button[aria-label="Submit"]');
    if (!submitBtn) return 'SUBMIT_BTN_NOT_FOUND';
    if (submitBtn.disabled) {{
        submitBtn.removeAttribute('disabled');
        submitBtn.classList.remove('mat-mdc-button-disabled');
    }}
    submitBtn.click();
    return 'SUBMITTED_SUCCESSFULLY';
}})()
"""

apple_script = f'tell application "Google Chrome" to execute active tab of front window javascript "{js_code.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"'

res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
print("Result:", res.stdout.strip(), res.stderr.strip())
