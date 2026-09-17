import subprocess
import json
import time

prompt = """QUANTITATIVE AUDIT: OVERTRADING, TURNOVER EXPLOSION & FRICTION DRAG ON MICRO-CAPITAL (₹1,008)

Rajon (Account Owner) noted:
"कल हमने ज्यादा शेयर्स ले लिए? मैं देख रहा हूँ कि ₹40,000 का ट्रेड (टर्नओवर) किया है हमने कल। थोड़ा ज्यादा हो गया था क्या? मुझे तो पता ही नहीं कल ज्यादा क्यों हुआ था, मैं तो नहीं लिया था। मेरे को पता नहीं ज्यादा हुआ था या कम हुआ था या और ज्यादा लेता तो अच्छा होता।"

Mathematical & Microstructure Facts:
1. Account SOD Starting Capital: ₹1,008.00.
2. Yesterday's Executed Turnover: ~₹40,000.00 (Buy Turnover ~₹20,000 + Sell Turnover ~₹20,000 across multiple high-frequency intraday trades).
3. P&L Breakdown:
   - Screen Gross Trading P&L: -₹42.00 (Loss from stock price movement).
   - Statutory Slippage & Brokerage Drag: -₹47.57 (STT, Exchange transaction charges, SEBI turnover fees, GST, Stamp duty).
   - Total Net Account Debit: -₹89.57 (8.88% of total account evaporated!).
   - Crucial Revelation: Taxes and friction (-₹47.57) were HIGHER than the actual market loss (-₹42.00)!

Inquiry for the 200+ Quant Repos (NautilusTrader, VectorBT, Riskfolio-Lib, Transaction Cost Models, PyPortfolioOpt):
1. Was ₹40,000 turnover "too much" (ज्यादा हो गया था क्या)? Explain the mathematical concept of Turnover-to-Capital Ratio (40x Churn Rate) and why a 40x churn on a ₹1,000 account guarantees mathematical bankruptcy due to fixed/proportional friction.
2. Why did the user feel "मैं तो नहीं लिया था, मुझे तो पता ही नहीं चला"? (Explain automated micro-scalping churning vs algorithmic trade frequency limits).
3. If the user asks: "या फिर और ज्यादा लेता तो अच्छा होता?", explain why increasing trade size or churning more under high friction would have accelerated capital death exponentially.
4. Hard Quantitative Solution: What is the strictly optimal Maximum Daily Turnover and Maximum Daily Trade Count (e.g., max 2-3 high-conviction trades, max 2x-3x turnover = ₹2,000-₹3,000 total turnover) to keep statutory friction strictly under 0.5% of capital?"""

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
