import subprocess
import json
import time

prompt = """[SOVEREIGN DUAL-GRAPH 1000X HYPER-EXTENDED RAG & RECOVERY DIRECTIVE - 17 SEP 2026]

Grounded in our newly injected note 'LIVE_INGESTION_17_SEP_2026_YOUTUBE_AND_MACRO_PULSE' and the 290 Quantitative Repositories (NautilusTrader, VectorBT, Riskfolio-Lib, vollib, Order Flow Imbalance, statsmodels, ta-lib):

Founder Mandate:
"अरे ऐसा नहीं करना है कि तुम पूरा सेल ही करते रहो, फिर प्रॉफिट कब होगा? मिला के चलना है, लाइव डायनामिक अपडेट से जो चीज मिलेगा उसे डायनेमिकली अपडेट करना है, एक चीज पकड़ के नहीं बैठना है। एक हाइपर एक्सटेंडेड ग्राफ बनाओ सो दैट हमारा पुराना सब लॉस रिकवर हो जाए, टैक्स भी कवर हो जाए और प्रॉफिट भी हो जाए।"

Physical Broker Truth (Dhan v2 Live):
- Capital: ₹918.43 SOD | Available Cash: ₹370.73 (5x Margin Buying Power: ₹1,853.65).
- Active Open Positions:
  * PNB: LONG 14 shares @ ₹118.32 (Realized +₹8.82, Live +₹4.06 = Total +₹12.88 net profit). Stop Loss at ₹118.35 Breakeven Ratchet.
  * ITC: LONG 4 shares @ ₹267.00 (Live +₹1.40). Stop Loss at ₹265.80.
  * TATASTEEL: Re-entered / Scalped (Net -₹6.57).
  * Current Net Account P&L: +₹6.32 Net Profit.
- Target: Recover yesterday's -₹89.57 loss + ₹12 taxes = +₹102.00 to +₹125.00 Total Net Gain.

MANDATORY HYPER-EXTENDED GRAPH SYNTHESIS:
Synthesize the structured Hyper-Extended Knowledge Graph:
1. NODES SPECIFICATION:
   - Node 1: Macro_Sensex_0DTE_ShortGamma (Call wall unwind at 76,000 / 76,200)
   - Node 2: Macro_PSU_Credit_Dividend (PNB dividend & loan book expansion momentum)
   - Node 3: Macro_FMCG_Defensive_Hedging (ITC institutional accumulation during expiry chop)
   - Node 4: Micro_L2_OrderFlowImbalance (OFI_t > +0.25 delta surge)
   - Node 5: Micro_Chandelier_ATR_Trail (1.5 * ATR_14 trailing ratchet preserving green equity)
   - Node 6: Asset_PNB_Holding (14 shares @ 118.32, dynamic upside expansion to 121.50)
   - Node 7: Asset_ITC_Holding (4 shares @ 267.00, upside expansion to 272.20)
   - Node 8: Asset_RBLBANK_Breakout (52-week high volume breakout momentum)
   - Node 9: Risk_Variance_Shield_2.5Pct (₹22.96 circuit breaker hard stop)
   - Node 10: Target_Recovery_Plus102 (₹102 profit target lock)

2. DIRECTED EDGES & CAUSAL TRANSMISSIONS:
   - Map exact mathematical relationships (Node_A -> Edge_Type -> Node_B).
   - Explain how holding PNB and ITC with dynamic trailing prevents premature selling and allows compounding toward the +₹102 recovery target.

3. RECOVERY MATHEMATICS & EXECUTION RULES:
   - Step-by-step profit ladder to achieve +₹102.00 while capping daily trade count to <= 3 and turnover to <= ₹3,000.
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

cmd = ["osascript", "-e", f'tell application "Google Chrome" to execute active tab of front window javascript "{js_code.replace(chr(92), chr(92)+chr(92)).replace(chr(34), chr(92)+chr(34))}"']
res = subprocess.run(cmd, capture_output=True, text=True)
print("Result:", res.stdout.strip())
