# ⚡ [QUANT-SOURCE-045] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_045_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: zerodha-algo-trader (`PHASE4-QUANT-161`)
- **Full Name**: `PHASE4-QUANT-161_anshuman-75__zerodha-algo-trader`
- **Description**: Automated NSE trading bot using Zerodha Kite API and Claude AI
- **GitHub Stars**: 5
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# AutoInvestor v3

An automated trading bot for the Indian stock market — built on Zerodha Kite API, powered by Claude AI, and managed via Telegram.

> **Status:** Live as of April 10, 2026 | Server: OneProvider France | Ubuntu 20.04

---

## What it does

AutoInvestor v3 runs fully autonomously during market hours. It scans the NSE market at key intervals, uses Claude AI to analyse signals and decide trades, places equity and F&O orders through Zerodha, and sends you a Telegram report after every run — all without any manual intervention.

**Scheduled runs:** 9:15 AM · 9:45 AM · 11:00 AM · 1:00 PM · 3:00 PM IST (Mon–Fri)

---

## Features

- **Pre-market scan** — NSE top actives, gainers, losers, VIX, PCR, FII/DII data at 9:15 AM
- **AI-driven decisions** — Claude analyses signals and picks BUY/SELL with confidence scores
- **F&O trading** — Options chain analysis, CE/PE selection, within a strict Rs. 1,500 test budget
- **Automated SIP** — Weekly NIFTYBEES (Rs. 500) and JUNIORBEES (Rs. 250) investments
- **Profit booking** — Auto-sells 50% of a position when it gains 8%
- **Stop-loss** — Auto-exits if any position loses more than 8%
- **Telegram control** — Login flow, token refresh, and reports all via Telegram
- **systemd service** — Survives SSH drops, auto-restarts on crash, starts on reboot

---

## Project structure

```
investor_v3/
├── auto_investor_v3.py     # Main runner — APScheduler, calls all modules
├── market_scanner.py       # Pre-market scan — VIX, PCR, FII/DII, watchlist builder
├── options_trader.py       # F&O brain — options chain, CE/PE selection, order placement
├── fno_tracker.py          # Tracks F&O trades — enforces 1 trade per 2 weeks limit
├── token_manager.py        # Telegram-based Zerodha token refresh
├── config.py               # All settings (API keys, limits, watchlists) — not in repo
├── config.example.py       # Template config — copy this and fill in your values
└── investor.service        # systemd service file
```

---

## Configuration

Copy the example config and fill in your credentials:

```bash
cp config.example.py config.py
nano config.py
```

Key settings:

| Setting | Default | Description |
|---|---|---|
| `MAX_ORDER_VALUE` | Rs. 5,000 | Max per single equity order |
| `MAX_DAILY_SPEND` | Rs. 5,000 | Max equity spend per day |
| `MIN_CASH_RESERVE` | Rs. 1,000 | Always kept untouched |
| `MAX_FNO_ORDER_VALUE` | Rs. 1,500 | Max per options trade |
| `MAX_FNO_TRADES_BIWEEKLY` | 1 | Max F&O trades per 2 weeks |
| `MAX_VIX_FOR_FNO` | 25 | Skip options if VIX above this |
| `PROFIT_BOOKING_PCT` | 8% | Sell 50% when position gains this |
| `STOP_LOSS_PCT` | 8% | Exit if position loses this |

---

## Setup

### Prerequisites

- Python 3.11+
- A [Zerodha](https://zerodha.com) account with Kite API access
- An [Anthropic](https://anthropic.com) API key (for Claude)
- A Telegram bot token

### Install dependencies

```bash
cd ~/investor_v3
pip3.11 install -r requirements.txt
```

### Enable the systemd service

```bash
sudo cp investor.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable investor
sudo systemctl start investor
```

### Zerodha token setup

On first run (or after the daily 6 AM token expiry), send `/login` to your Telegram bot. It will send you a login link — open it in an **incognito window**, complete the login, paste the `request_token` back to the bot within 2 minutes.

---

## Daily management

```bash
# Check if bot is running
sudo systemctl status investor

# Follow live logs
journalctl -u investor -f

# Attach to screen session
screen -r investor_v3   # Ctrl+A then D to detach

# Restart bot
sudo systemctl restart investor

# Check F&O trade history
python3.11 fno_tracker.py

# View logs
cat ~/investor_v3/investor_log.txt
```

---

## Watchlist

- **Equity:** 22 stocks (large-cap NSE)
- **F&O:** 15 stocks (options-eligible)

Dynamic additions from the morning scan (NSE top actives, unusual movers).

---

## Safety limits

The bot is designed to be conservative by default:

- Never spends below the `MIN_CASH_RESERVE` threshold
- F&O trades capped at 1 per day and 1 per 2 weeks
- F&O only trades on HIGH confidence signals
- F&O skipped entirely if VIX > 25
- All orders go through a final Claude review before placement

---

## Known quirks

| Issue | Fix |
|---|---|
| `request_token` expires fast | Paste it within 2 minutes |
| Zerodha login fails | Always use incognito window |
| Token expires at 6 AM | Telegram login flow handles this automatically |
| pip `--break-system-packages` error | Use `pip3.11 install` without that flag on this server |

---

## Disclaimer

This bot places real trades with real money. Use it at your own risk. Past performance of any algorithm is not a guarantee of future results. Always monitor your positions and maintain a sufficient cash buffer.

---

*Built by Anshuman · April 2026*

### Core Implementation Code & Architecture
#### File: `logger.py`
```python
"""
logger.py — Logs all decisions, orders, and errors to a file and console.
"""

import datetime
import config


def _timestamp():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")


def _write(tag, message):
    line = f"[{_timestamp()}] [{tag}] {message}"
    print(line)
    with open(config.LOG_FILE, "a") as f:
        f.write(line + "\n")


def info(msg):    _write("INFO ", msg)
def success(msg): _write("✅ OK", msg)
def warning(msg): _write("⚠️  WARN", msg)
def error(msg):   _write("❌ ERR", msg)


def log_decision(decision):
    info(f"Market sentiment: {decision.get('market_sentiment', '?').upper()}")
    info(f"Claude reasoning: {decision.get('reasoning', '')}")
    for a in decision.get("actions", []):
        if a["action"] == "hold":
            info(f"Action: HOLD — {a['reason']}")
        elif a["action"] == "buy":
            info(f"Action: BUY {a['symbol']} ₹{a['amount_inr']} — {a['reason']}")
        elif a["action"] == "sell":
            info(f"Action: SELL {a['quantity']} x {a['symbol']} — {a['reason']}")


def log_order(action, symbol, quantity, order_id):
    success(f"Order placed | {action.upper()} {quantity} x {symbol} | Order ID: {order_id}")


def log_order_skipped(symbol, reason):
    warning(f"Order skipped | {symbol} | Reason: {reason}")


def log_scheduled(symbol, quantity, order_id):
    success(f"Scheduled order | BUY {quantity} x {symbol} | Order ID: {order_id}")


def log_daily_summary(spent, orders):
    info(f"Daily summary: ₹{spent:,.2f} invested across {orders} order(s).")
    info("─" * 50)
```

#### File: `daily_orders.py`
```python
"""
daily_orders.py — AutoInvestor v3
Tracks orders placed within the current trading day.
Prevents Claude from double-buying the same stock across multiple daily runs.
File: ~/investor_v3/daily_orders.json  (auto-created, auto-reset each new day)
"""

import json
import os
from datetime import date

ORDERS_FILE = os.path.join(os.path.dirname(__file__), "daily_orders.json")


def _load():
    """Load today's orders file. Returns empty structure if missing or stale."""
    today = str(date.today())
    if os.path.exists(ORDERS_FILE):
        try:
            with open(ORDERS_FILE, "r") as f:
                data = json.load(f)
            if data.get("date") == today:
                return data
        except Exception:
            pass
    return {"date": today, "orders": [], "symbols_bought": [], "total_spent": 0, "fno_trades": []}


def _save(data):
    with open(ORDERS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def record_order(symbol, action, quantity, price, order_id, reason=""):
    """Call this immediately after every successful order placement."""
    data = _load()
    entry = {
        "symbol": symbol,
        "action": action,
        "quantity": quantity,
        "price": price,
        "value": round(quantity * price, 2),
        "order_id": order_id,
        "reason": reason,
    }
    data["orders"].append(entry)
    if action == "BUY" and symbol not in data["symbols_bought"]:
        data["symbols_bought"].append(symbol)
    if action == "BUY":
        data["total_spent"] += entry["value"]
    _save(data)


def get_todays_summary():
    """Returns a dict with today's orders for injection into Claude's prompt."""
    data = _load()
    return {
        "orders_placed_today": data["orders"],
        "symbols_bought_today": data["symbols_bought"],
        "total_spent_today": round(data["total_spent"], 2),
    }


def already_bought_today(symbol):
    """Quick check — returns True if this symbol was already bought today."""
    data = _load()
    return symbol in data["symbols_bought"]


def get_symbols_bought_today():
    return _load().get("symbols_bought", [])


def get_total_spent_today():
    return _load().get("total_spent", 0)


def record_fno_trade(symbol, tradingsymbol, cost, order_id):
    """Record an F&O trade placed today."""
    data = _load()
    data.setdefault("fno_trades", [])
    data["fno_trades"].append({
        "symbol": symbol,
        "tradingsymbol": tradingsymbol,
        "cost": cost,
        "order_id": order_id,
    })
    _save(data)


def get_fno_trades_today():
    """Returns number of F&O trades placed today."""
    return len(_load().get("fno_trades", []))


if __name__ == "__main__":
    summary = get_todays_summary()
    print(f"Date: {_load()['date']}")
    print(f"Symbols bought today: {summary['symbols_bought_today']}")
    print(f"Total spent today: ₹{summary['total_spent_today']}")
    print(f"F&O trades today: {get_fno_trades_today()}")
    print(f"Orders:")
    for o in summary["orders_placed_today"]:
        print(f"  {o['action']} {o['symbol']} x{o['quantity']} @ ₹{o['price']} = ₹{o['value']} | ID: {o['order_id']}")
```

#### File: `claude_investor.py`
```python
"""
claude_investor.py (v2) — Upgraded AI brain with full technical analysis.
Claude now makes decisions based on:
- 50/200 Day Moving Averages
- RSI (momentum)
- MACD (trend direction)
- 52 Week High/Low context
- Volume trends
- Support & Resistance levels
"""

import json
import anthropic
import config


client = anthropic.Anthropic(api_key=config.ANTHROPIC_API_KEY)


SYSTEM_PROMPT = """You are an experienced AI investment manager for a retail investor in India.
You manage a real Zerodha portfolio with moderate risk appetite (mix of growth + stable).

Your investment philosophy:
- 60% stable (index ETFs like NIFTYBEES, JUNIORBEES, blue-chip large caps)
- 40% growth (high-quality large-cap growth stocks on NSE)
- Always invest for medium-long term (CNC delivery), never intraday
- Never speculate or chase momentum blindly

The investor's personal rules you MUST always follow:
{rules}

SAFETY LIMITS (never exceed):
- Max single order: ₹{max_order}
- Max daily spend: ₹{max_daily}
- Always keep ₹{min_reserve} cash untouched

TECHNICAL ANALYSIS GUIDELINES:
- STRONG BUY signals: Price above 50 & 200 DMA, RSI 40-60, MACD bullish, high volume
- BUY signals: Price above 200 DMA, RSI not overbought (<70), MACD neutral/bullish
- AVOID: RSI > 70 (overbought), price far above resistance, MACD strongly bearish
- SELL signals: RSI > 75, price breaks below 50 DMA with high volume, MACD crossover bearish
- HOLD: Mixed signals or insufficient data

DECISION RULES:
1. Never buy a stock showing STRONG DOWNTREND
2. Prefer stocks with RSI between 40-60 (not overbought, not oversold)
3. Prefer stocks trading above their 200 DMA (long term uptrend)
4. High volume on up days = strong conviction, prefer these
5. Never buy near resistance, prefer buying near support
6. If unsure on any stock, action = hold

Output FORMAT — respond ONLY with valid JSON, nothing else:
{{
  "reasoning": "2-3 sentence analysis summary",
  "market_sentiment": "bullish|neutral|bearish",
  "actions": [
    {{
      "action": "buy|sell|hold",
      "symbol": "STOCKNAME",
      "amount_inr": 2000,
      "quantity": 0,
      "reason": "One line technical reason"
    }}
  ]
}}

If action is "buy": set amount_inr, leave quantity as 0.
If action is "sell": set quantity, leave amount_inr as 0.
If no trades: return [{{"action": "hold", "symbol": "", "amount_inr": 0, "quantity": 0, "reason": "No strong signals today"}}]
Max 3 actions per day.
""".format(
    rules    = config.INVESTMENT_RULES,
    max_order = config.MAX_ORDER_VALUE,
    max_daily = config.MAX_DAILY_SPEND,
    min_reserve = config.MIN_CASH_RESERVE,
)


def analyse_and_decide(portfolio_summary, technical_analysis_str):
    """
    Asks Claude to analyse portfolio + technical data and return trade decisions.
    """
    user_message = f"""Today's portfolio:
{portfolio_summary}

Technical analysis for watchlist:
{technical_analysis_str}

Based on the technical analysis above, what should I do today?
Only buy stocks with clear technical justification.
Respond only in the JSON format specified."""

    response = client.messages.create(
        model      = "claude-sonnet-4-6",
        max_tokens = 1000,
        system     = SYSTEM_PROMPT,
        messages   = [{"role": "user", "content": user_message}],
    )

    raw = response.content[0].text.strip()

    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    raw = raw.strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        return {
            "reasoning": "Claude returned unparseable response. Holding today.",
            "market_sentiment": "neutral",
            "actions": [{"action": "hold", "symbol": "", "amount_inr": 0, "quantity": 0, "reason": "Parse error"}],
        }
```

#### File: `telegram_reporter.py`
```python
"""
telegram_reporter.py — Sends daily investment reports to Telegram.

Sends a beautiful report every morning after Claude's analysis showing:
- Portfolio summary
- Market sentiment
- Claude's reasoning
- Orders placed
- Daily P&L
"""

import requests
import datetime
import config


def send_message(text):
    """Sends a message to Telegram."""
    url = f"https://api.telegram.org/bot{config.TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id":    config.TELEGRAM_CHAT_ID,
        "text":       text,
        "parse_mode": "HTML",
    }
    try:
        response = requests.post(url, json=payload, timeout=10)
        return response.ok
    except Exception as e:
        print(f"Telegram error: {e}")
        return False


def send_daily_report(portfolio, decision, orders_placed, daily_spent):
    """
    Sends a full daily report to Telegram after Claude's analysis.
    """
    now = datetime.datetime.now().strftime("%d %b %Y, %I:%M %p IST")

    # Sentiment emoji
    sentiment = decision.get("market_sentiment", "neutral").lower()
    if sentiment == "bullish":
        sentiment_emoji = "🟢 BULLISH"
    elif sentiment == "bearish":
        sentiment_emoji = "🔴 BEARISH"
    else:
        sentiment_emoji = "🟡 NEUTRAL"

    # Portfolio stats
    cash      = portfolio.get("cash", 0)
    holdings  = portfolio.get("holdings", [])
    total_pnl = sum(h.get("pnl", 0) for h in holdings)
    pnl_emoji = "📈" if total_pnl >= 0 else "📉"
    pnl_sign  = "+" if total_pnl >= 0 else ""

    # Build orders section
    actions = decision.get("actions", [])
    orders_text = ""
    for a in actions:
        if a["action"] == "buy":
            orders_text += f"\n  🛒 BUY {a['symbol']} — {a['reason']}"
        elif a["action"] == "sell":
            orders_text += f"\n  💰 SELL {a['symbol']} — {a['reason']}"
        elif a["action"] == "hold":
            orders_text += f"\n  ⏸ HOLD — {a['reason']}"

    # Build holdings section
    holdings_text = ""
    if holdings:
        for h in holdings[:5]:  # show max 5
            pnl   = h.get("pnl", 0)
            sign  = "+" if pnl >= 0 else ""
            emoji = "📈" if pnl >= 0 else "📉"
            holdings_text += f"\n  {emoji} {h['tradingsymbol']}: {sign}₹{pnl:,.0f}"
        if len(holdings) > 5:
            holdings_text += f"\n  ... and {len(holdings)-5} more"
    else:
        holdings_text = "\n  No holdings yet"

    message = f"""🤖 <b>Claude Investor — Daily Report</b>
📅 {now}

━━━━━━━━━━━━━━━━━━━━━
📊 <b>MARKET SENTIMENT</b>
{sentiment_emoji}

🧠 <b>CLAUDE'S REASONING</b>
{decision.get('reasoning', 'No reasoning provided')}

━━━━━━━━━━━━━━━━━━━━━
⚡ <b>TODAY'S ACTIONS</b>{orders_text}

💸 <b>Amount Invested Today:</b> ₹{daily_spent:,.0f}
📦 <b>Orders Placed:</b> {orders_placed}

━━━━━━━━━━━━━━━━━━━━━
💼 <b>PORTFOLIO</b>
💵 Cash Available: ₹{cash:,.0f}
{pnl_emoji} Overall P&L: {pnl_sign}₹{total_pnl:,.0f}

<b>Holdings:</b>{holdings_text}

━━━━━━━━━━━━━━━━━━━━━
<i>Next run: Tomorrow 9:45 AM IST</i>"""

    return send_message(message)


def send_order_alert(action, symbol, quantity, order_id, reason):
    """Sends instant alert when an order is placed."""
    emoji = "🛒" if action.upper() == "BUY" else "💰"
    message = f"""{emoji} <b>Order Placed</b>

<b>Action:</b> {action.upper()}
<b>Stock:</b> {symbol}
<b>Quantity:</b> {quantity} shares
<b>Order ID:</b> {order_id}
<b>Reason:</b> {reason}

<i>Check Kite app for execution status</i>"""
    return send_message(message)


def send_error_alert(error_msg):
    """Sends alert if something goes wrong."""
    message = f"""⚠️ <b>Investor Bot Error</b>

{error_msg}

<i>Please check the server logs</i>"""
    return send_message(message)


def send_startup_message():
    """Sends a message when the bot starts up."""
    message = f"""🚀 <b>Claude Investor Bot Started</b>

✅ Connected to Zerodha
✅ Technical analysis ready
✅ Scheduler running

<b>Next analysis:</b> 9:45 AM IST on market days
<i>You'll receive a report after each daily run</i>"""
    return send_message(message)
```

#### File: `zerodha.py`
```python
"""
zerodha.py — Handles Zerodha login, portfolio data, and order placement.
"""

import json
import datetime
from kiteconnect import KiteConnect
import config


def get_kite():
    """Returns an authenticated KiteConnect instance."""
    kite = KiteConnect(api_key=config.ZERODHA_API_KEY)
    if config.ZERODHA_ACCESS_TOKEN:
        kite.set_access_token(config.ZERODHA_ACCESS_TOKEN)
    return kite


def login(kite):
    """Interactive browser-based Zerodha login."""
    print("\n" + "="*55)
    print("  ZERODHA LOGIN")
    print("="*55)
    print(f"\n1. Open this URL in your browser:\n\n   {kite.login_url()}\n")
    print("2. Log in and copy the 'request_token' from the redirect URL.\n")
    request_token = input("Paste request_token here: ").strip()
    data = kite.generate_session(request_token, api_secret=config.ZERODHA_API_SECRET)
    kite.set_access_token(data["access_token"])
    config.ZERODHA_ACCESS_TOKEN = data["access_token"]

    # Save access token permanently to config file
    with open('config.py', 'r') as f:
        content = f.read()
    import re
    content = re.sub(
        r'ZERODHA_ACCESS_TOKEN = ".*?"',
        f'ZERODHA_ACCESS_TOKEN = "{data["access_token"]}"',
        content
    )
    with open('config.py', 'w') as f:
        f.write(content)

    print("✅ Logged in successfully!\n")
    return kite


def get_portfolio(kite):
    """Returns holdings, positions, and available cash."""
    holdings  = kite.holdings()
    margins   = kite.margins()["equity"]
    available = margins.get("available", {})
    cash = available.get("cash", 0) + available.get("intraday_payin", 0)
    positions = kite.positions().get("net", [])
    return {
        "holdings":  holdings,
        "positions": positions,
        "cash":      cash,
    }


def get_portfolio_summary(portfolio):
    """Returns a plain-English string summary of the portfolio."""
    lines = [f"Available cash: ₹{portfolio['cash']:,.2f}"]

    if portfolio["holdings"]:
        lines.append(f"\nHoldings ({len(portfolio['holdings'])} stocks):")
        total_invested = 0
        total_current  = 0
        for h in portfolio["holdings"]:
            invested = h["average_price"] * h["quantity"]
            current  = h["last_price"]   * h["quantity"]
            pnl      = h["pnl"]
            pct      = ((current - invested) / invested * 100) if invested else 0
            sign     = "+" if pnl >= 0 else ""
            total_invested += invested
            total_current  += current
            lines.append(
                f"  • {h['tradingsymbol']:15s} | Qty: {h['quantity']:5d} "
                f"| Avg: ₹{h['average_price']:8.2f} | LTP: ₹{h['last_price']:8.2f} "
                f"| P&L: {sign}₹{pnl:,.2f} ({sign}{pct:.1f}%)"
            )
        overall_pnl = total_current - total_invested
        overall_pct = (overall_pnl / total_invested * 100) if total_invested else 0
        sign = "+" if overall_pnl >= 0 else ""
        lines.append(
            f"\nTotal invested: ₹{total_invested:,.2f} | "
            f"Current value: ₹{total_current:,.2f} | "
            f"Overall P&L: {sign}₹{overall_pnl:,.2f} ({sign}{overall_pct:.1f}%)"
        )
    else:
        lines.append("\nNo holdings yet.")

    return "\n".join(lines)


def get_quote(kite, symbols):
    """Returns latest quotes for a list of NSE symbols."""
    instruments = [f"NSE:{s}" for s in symbols]
    try:
        quotes = kite.quote(instruments)
        result = {}
        for sym in symbols:
            key = f"NSE:{sym}"
            if key in quotes:
                q = quotes[key]
                result[sym] = {
                    "ltp":    q["last_price"],
                    "open":   q["ohlc"]["open"],
                    "high":   q["ohlc"]["high"],
                    "low":    q["ohlc"]["low"],
                    "close":  q["ohlc"]["close"],
                    "volume": q["volume"],
                    "change": q.get("net_change", 0),
                }
        return result
    except Exception as e:
        return {}


def place_market_order(kite, symbol, quantity, transaction_type):
    return kite.place_order(
        variety          = kite.VARIETY_REGULAR,
        exchange         = kite.EXCHANGE_NSE,
        tradingsymbol    = symbol.upper(),
        transaction_type = transaction_type.upper(),
        quantity         = int(quantity),
        order_type       = kite.ORDER_TYPE_MARKET,
        product          = kite.PRODUCT_CNC,
        market_protection = -1,  # ← add this line
    )

def is_market_open():
    """Returns True if current IST time is within market hours on a weekday."""
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=5, minutes=30)))
    if now.weekday() >= 5:  # Saturday/Sunday
        return False
    market_open  = now.replace(hour=9,  minute=15, second=0, microsecond=0)
    market_close = now.replace(hour=15, minute=30, second=0, microsecond=0)
    return market_open <= now <= market_close
```

#### File: `fno_tracker.py`
```python
"""
fno_tracker.py — Tracks F&O trade count across days
Enforces the biweekly limit (MAX_FNO_TRADES_BIWEEKLY in config.py)

Uses a simple JSON file: fno_tracker.json
{
    "trades": [
        {"date": "2026-04-10", "symbol": "NIFTY24417CE", "cost": 1125}
    ]
}
"""

import json
import os
import datetime
import config

TRACKER_FILE = "fno_tracker.json"


# ─────────────────────────────────────────────────────────────
#  LOAD / SAVE
# ─────────────────────────────────────────────────────────────

def _load():
    if not os.path.exists(TRACKER_FILE):
        return {"trades": []}
    try:
        with open(TRACKER_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return {"trades": []}


def _save(data):
    try:
        with open(TRACKER_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[FNO Tracker] Save failed: {e}")


# ─────────────────────────────────────────────────────────────
#  CORE FUNCTIONS
# ─────────────────────────────────────────────────────────────

def get_biweekly_trade_count():
    """
    Returns number of F&O trades placed in the last 14 days.
    """
    data   = _load()
    today  = datetime.date.today()
    cutoff = today - datetime.timedelta(days=14)

    recent = [
        t for t in data["trades"]
        if datetime.date.fromisoformat(t["date"]) > cutoff
    ]
    return len(recent)


def can_trade_fno():
    """
    Returns (True, message) if allowed to trade F&O today.
    Returns (False, reason) if biweekly limit reached.
    """
    count = get_biweekly_trade_count()
    limit = config.MAX_FNO_TRADES_BIWEEKLY

    if count >= limit:
        next_available = _next_available_date()
        return False, (
            f"Biweekly F&O limit reached ({count}/{limit} trades in last 14 days). "
            f"Next trade allowed after {next_available}."
        )

    remaining = limit - count
    return True, f"{remaining} F&O trade(s) remaining in this 2-week window."


def record_fno_trade(symbol, cost):
    """
    Records a completed F&O trade.
    Call this after a successful options order placement.
    """
    data = _load()
    data["trades"].append({
        "date":   datetime.date.today().isoformat(),
        "symbol": symbol,
        "cost":   cost,
    })
    _save(data)
    print(f"[FNO Tracker] Recorded trade: {symbol} @ ₹{cost}")


def get_trade_history(days=30):
    """Returns trade history for the last N days."""
    data   = _load()
    today  = datetime.date.today()
    cutoff = today - datetime.timedelta(days=days)

    return [
        t for t in data["trades"]
        if datetime.date.fromisoformat(t["date"]) > cutoff
    ]


def _next_available_date():
    """Returns the date when next F&O trade will be allowed."""
    data = _load()
    if not data["trades"]:
        return datetime.date.today().isoformat()

    # Find oldest trade in current 14-day window
    today  = datetime.date.today()
    cutoff = today - datetime.timedelta(days=14)

    recent_dates = sorted([
        datetime.date.fromisoformat(t["date"])
        for t in data["trades"]
        if datetime.date.fromisoformat(t["date"]) > cutoff
    ])

    if not recent_dates:
        return today.isoformat()

    # Next available = oldest trade date + 15 days
    oldest = recent_dates[0]
    return (oldest + datetime.timedelta(days=15)).isoformat()


def summary():
    """Returns a plain-English summary for Telegram reports."""
    count          = get_biweekly_trade_count()
    limit          = config.MAX_FNO_TRADES_BIWEEKLY
    allowed, msg   = can_trade_fno()
    history        = get_trade_history(days=14)

    lines = [f"⚡ F&O Tracker: {count}/{limit} trades in last 14 days"]
    if history:
        for t in history:
            lines.append(f"  • {t['date']} | {t['symbol']} | ₹{t['cost']:,}")
    if not allowed:
        lines.append(f"  🔒 {msg}")
    else:
        lines.append(f"  ✅ {msg}")

    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────
#  STANDALONE TEST
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("F&O Tracker Status:")
    print(summary())
    allowed, msg = can_trade_fno()
    print(f"\nCan trade today: {'✅ Yes' if allowed else '❌ No'}")
    print(f"Reason: {msg}")
```


==================================================


## [2/3] Repository: nse_scrap (`PHASE4-QUANT-167`)
- **Full Name**: `PHASE4-QUANT-167_singhanuj620__nse_scrap`
- **Description**: NSE Stock Data Scraper - Full-stack web app for downloading Indian stock market data. Features Node.js/Express backend with direct NSE API integration (10x faster than web scraping) and React frontend. Provides real-time progress tracking, configurable stock lists, and automated CSV export. Perfect for financial analysis and algorithmic trading.
- **GitHub Stars**: 6
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# NSE Stock Data Downloader (API-Based)

Fast and reliable downloader for NSE India stock data using direct API calls. No browser automation required!

## 🚀 Features

- ⚡ **Lightning Fast** - Direct API calls to NSE (10x faster than browser scraping)
- � **Complete Data** - Historical price, volume, and delivery data
- �️ **Auto Organization** - Files saved as `STOCK_YEAR.csv` in organized folders
- ⚙️ **Easy Configuration** - JSON-based settings for stocks and date ranges
- �️ **Reliable** - No browser dependencies or UI changes to break
- 📈 **Scalable** - Download hundreds of stocks effortlessly

## � Data Fields

Each CSV file contains comprehensive trading data:
- **Price Data**: Open, High, Low, Close, Previous Close, Last Traded Price, VWAP
- **Volume Data**: Total Traded Quantity, Total Traded Value, Number of Trades  
- **Delivery Data**: Delivery Quantity, Delivery Percentage
- **Metadata**: Symbol, Series, Timestamps

## 🎯 Quick Start

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Test with one stock:**
   ```bash
   npm test
   ```

3. **Download all configured stocks:**
   ```bash
   npm start
   ```

## ⚙️ Configuration

### View Current Settings
```bash
npm run config:list
```

### Manage Stock List
```bash
# Add a stock
node config-manager.js add WIPRO

# Remove a stock  
node config-manager.js remove ITC

# Set year range
node config-manager.js years 2020 2024
```

### Configuration File
Edit `config.json` directly:

```json
{
  "stocks": [
    "RELIANCE", "TCS", "HDFCBANK", "ICICIBANK", 
    "HINDUNILVR", "INFY", "ITC", "SBIN"
  ],
  "years": {
    "start": 2014,
    "end": 2024
  },
  "settings": {
    "maxRetries": 1,
    "retryDelay": 3000,
    "waitBetweenStocks": 2000,
    "waitBetweenYears": 1000
  }
}
```

### Retry Configuration
- **maxRetries**: Number of retry attempts for failed downloads (default: 1)
- **retryDelay**: Wait time in milliseconds before retrying (default: 3000ms)
- **waitBetweenStocks**: Delay between processing different stocks (default: 2000ms)
- **waitBetweenYears**: Delay between years for same stock (default: 1000ms)

## 🎮 Available Commands

| Command | Description |
|---------|-------------|
| `npm start` | Download all configured stocks/years |
| `npm test` | Test with single stock (HDFCBANK 2024) |
| `npm run config:list` | Show current configuration |
| `node api-scraper.js single RELIANCE 2023` | Download specific stock/year |

## 📁 Output Structure

```
data/
├── RELIANCE/
│   ├── RELIANCE_2014.csv
│   ├── RELIANCE_2015.csv
│   └── ... (through 2024)
├── TCS/
│   ├── TCS_2014.csv
│   └── ...
└── ...
```

## 🔧 Advanced Usage

### Download Specific Stock/Year
```bash
node api-scraper.js single RELIANCE 2023
node api-scraper.js single TCS 2022
```

### Download All Configured Data
```bash
node api-scraper.js all
# or simply
npm start
```

### Configuration Management
```bash
# View help
node config-manager.js

# Examples
node config-manager.js add WIPRO
node config-manager.js remove ITC  
node config-manager.js years 2020 2024
node config-manager.js reset
```

## 📊 Example Output

Sample data from HDFCBANK_2024.csv:
```csv
CH_SYMBOL,CH_SERIES,mTIMESTAMP,CH_PREVIOUS_CLS_PRICE,CH_OPENING_PRICE,CH_TRADE_HIGH_PRICE,CH_TRADE_LOW_PRICE,CH_LAST_TRADED_PRICE,CH_CLOSING_PRICE,VWAP,CH_TOT_TRADED_QTY,CH_TOT_TRADED_VAL,CH_TOTAL_TRADES,CH_TIMESTAMP,COP_DELIV_QTY,COP_DELIV_PERC
HDFCBANK,EQ,01-Jan-2024,1709.25,1706,1709.15,1692,1692.9,1698.1,1701.52,7119843,12114568489.3,258349,2023-12-31T18:30:00.000+00:00,4416670,62.03
```

## 🚀 Performance

- **Speed**: Downloads complete year data in ~2 seconds per stock
- **Reliability**: Direct API access, no browser dependencies
- **Data Quality**: Raw NSE data with all original fields
- **Scalability**: Handle 100+ stocks easily

## 🛠️ Technical Details

### API Endpoint
Uses NSE's official API:
```
https://www.nseindia.com/api/historicalOR/generateSecurityWiseHistoricalData
```

### Session Management
- Automatically handles NSE session cookies
- Proper request headers and compression
- Rate limiting to respect server resources

### Error Handling
- **Automatic Retries**: Failed downloads are automatically retried (default: 1 retry)
- **Configurable Retry Settings**: Customize retry count and delay in config.json
- **Progress Tracking**: Retry attempts are clearly shown in progress counters
- **Detailed Error Reporting**: See exactly what failed and after how many attempts
- **Graceful Handling**: Continues processing other stocks if some fail
- **Retry Statistics**: Summary shows which items needed retries

## ❓ Troubleshooting

### Common Issues

1. **Network Errors**: Check internet connection
2. **No Data**: Verify stock symbol is correct and listed on NSE
3. **Empty Response**: Stock may not have traded during specified period

### Success Indicators
```
✅ Session cookies obtained
🔄 Processing HDFCBANK - 2024 (1/33)
✅ Success: HDFCBANK - 2024 (1/33)
📊 Records: 70
📁 Saved: ./data/HDFCBANK/01-01-2024-TO-31-12-2024-HDFCBANK-ALL-N.csv
```

### Retry Process
```
⚠️  Failed: SOMESTOCK - 2024 (5/33) - Network timeout
🔄 Retrying in 3 seconds... (1/1)
🔄 Processing SOMESTOCK - 2024 (5/33) (Retry 1/1)
✅ Success: SOMESTOCK - 2024 (5/33) (Retry 1/1)
```

### Download Summary
```
🎉 Download Summary
==================
✅ Successful: 32
❌ Failed: 1
📊 Total: 33
🔄 Items that needed retry: 3
```

## 📄 File Naming Convention

Files are automatically named as: `{SYMBOL}_{YEAR}.csv`

Examples:
- `RELIANCE_2024.csv`
- `TCS_2023.csv`  
- `HDFCBANK_2022.csv`

## 🎯 Use Cases

Perfect for:
- 📈 **Financial Analysis** - Historical price and volume analysis
- 🤖 **Algorithmic Trading** - Backtesting strategies
- 📊 **Research** - Academic and professional research
- 💼 **Portfolio Management** - Performance analysis
- 📉 **Technical Analysis** - Chart pattern analysis

## 🔒 Legal & Ethical

- Uses publicly available NSE data
- Respects rate limits and server resources
- No unauthorized access or data modification
- Intended for legitimate research and analysis

## 🆚 Why API over Web Scraping?

| Aspect | API Approach | Web Scraping |
|--------|-------------|--------------|
| **Speed** | ⚡ ~2 sec/stock | 🐌 ~30 sec/stock |
| **Reliability** | ✅ Stable | ❌ Breaks with UI changes |
| **Data Quality** | ✅ Raw JSON data | ⚠️ Parsed HTML |
| **Maintenance** | ✅ Minimal | ❌ High |
| **Resources** | ✅ Light | ❌ Heavy (browser) |

## 📜 License

MIT License - Free for personal and commercial use.

---

**⭐ Star this repo if it helped you download NSE data efficiently!**

### Core Implementation Code & Architecture
#### File: `railway.json`
```python
{
  "build": {
    "commands": [
      "npm run install-all",
      "npm run build"
    ]
  },
  "deploy": {
    "startCommand": "npm run server"
  }
}
```

#### File: `vercel.json`
```python
{
  "builds": [
    {
      "src": "frontend/package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "dist"
      }
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/frontend/dist/$1"
    }
  ]
}
```

#### File: `config.json`
```python
{
  "stocks": [
    "RELIANCE",
    "TCS",
    "HDFCBANK"
  ],
  "years": {
    "start": 2014,
    "end": 2024
  },
  "settings": {
    "headless": false,
    "downloadTimeout": 5000,
    "pageTimeout": 10000,
    "waitBetweenStocks": 2000,
    "waitBetweenYears": 1000,
    "maxRetries": 1,
    "retryDelay": 3000
  }
}
```

#### File: `vercel-frontend.json`
```python
{
  "builds": [
    {
      "src": "frontend/package.json",
      "use": "@vercel/static-build",
      "config": {
        "distDir": "dist"
      }
    }
  ],
  "installCommand": "cd frontend && npm install",
  "buildCommand": "cd frontend && npm run build",
  "outputDirectory": "frontend/dist",
  "routes": [
    {
      "src": "/(.*)",
      "dest": "/index.html"
    }
  ]
}
```

#### File: `frontend/package.json`
```python
{
  "name": "frontend",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "lint": "eslint .",
    "preview": "vite preview"
  },
  "dependencies": {
    "axios": "^1.11.0",
    "file-saver": "^2.0.5",
    "jszip": "^3.10.1",
    "lucide-react": "^0.542.0",
    "react": "^19.1.1",
    "react-dom": "^19.1.1"
  },
  "devDependencies": {
    "@eslint/js": "^9.33.0",
    "@types/react": "^19.1.10",
    "@types/react-dom": "^19.1.7",
    "@vitejs/plugin-react": "^5.0.0",
    "eslint": "^9.33.0",
    "eslint-plugin-react-hooks": "^5.2.0",
    "eslint-plugin-react-refresh": "^0.4.20",
    "globals": "^16.3.0",
    "vite": "^7.1.2"
  }
}
```

#### File: `package.json`
```python
{
  "name": "nse-api-scraper",
  "version": "1.0.0",
  "description": "Fast NSE India stock data downloader using direct API calls",
  "main": "api-scraper.js",
  "scripts": {
    "start": "node api-scraper.js all",
    "test": "node api-scraper.js test",
    "single": "node api-scraper.js single",
    "config": "node config-manager.js",
    "config:list": "node config-manager.js list",
    "config:reset": "node config-manager.js reset",
    "server": "node server.js",
    "frontend": "cd frontend && npm run dev",
    "build": "cd frontend && npm run build",
    "dev": "concurrently \"npm run server\" \"npm run frontend\"",
    "install-all": "npm install && cd frontend && npm install"
  },
  "keywords": [
    "nse",
    "api",
    "stocks",
    "india",
    "data",
    "historical"
  ],
  "author": "",
  "license": "ISC",
  "dependencies": {
    "archiver": "^7.0.1",
    "cors": "^2.8.5",
    "express": "^4.21.2",
    "fs-extra": "^11.1.1",
    "multer": "^2.0.2"
  },
  "devDependencies": {
    "concurrently": "^9.2.1"
  }
}
```


==================================================


## [3/3] Repository: Finvasia (`PHASE4-QUANT-168`)
- **Full Name**: `PHASE4-QUANT-168_Indian-Algorithmic-Trading-Community__Finvasia`
- **Description**: All Codes Which Will Help You Do Algorithmic Trading With Finvasia Broker
- **GitHub Stars**: 4
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Finvasia
All Codes Which Will Help You Do Algorithmic Trading With Finvasia Broker


#### License

<sup>
Licensed under either of <a href="LICENSE-APACHE">Apache License, Version
2.0</a> or <a href="LICENSE-MIT">MIT license</a> at your option.
</sup>

<br>

<sub>
Unless you explicitly state otherwise, any contribution intent

### Core Implementation Code & Architecture
#### File: `resample/resample_shoonya.py`
```python
import polars as pl
from typing import Literal

def prepare_data(dataframe: pl.DataFrame(), 
                 filtered: bool=True,
                 ) -> pl.DataFrame():

    df = dataframe.drop(
        ["stat", "time", "v", "oi"]
        ).rename(
            mapping={
            "ssboe" : "Timestamp", 
            "into" : "Open", 
            "inth" : "High",
            "intl" : "Low",
            "intc" : "Close",
            "intvwap" : "VWAP",
            "intv" : "Volume",
            "intoi" : "OI"
            }
        ).with_columns(
          pl.from_epoch(
              "Timestamp", time_unit="s").dt.replace_time_zone(
                  time_zone="UTC").dt.convert_time_zone(
                    time_zone="Asia/Kolkata")
                )
    
    if filtered:
        df_market = df.filter(
            pl.col("Timestamp").dt.time().is_between(
                    lower_bound=pl.time(9,15,00),
                    upper_bound=pl.time(15,30,00)
                )
            )
        return df_market
    return df

def resample_data(dataframe: pl.DataFrame(),
                  timeframe: Literal['3m', '5m', '15m', '30m', '1h', '4h', '1d', '1w', '1mo', '1y']='5m'
                  ) -> pl.DataFrame():
    df_resampled = dataframe.sort("Timestamp").group_by_dynamic(
        "Timestamp",every=timeframe).agg(
            pl.col("Open").first(), 
            pl.col("High").max(), 
            pl.col("Low").min(), 
            pl.col("Close").last(),
            pl.col("VWAP").mean(), 
            pl.col("Volume").sum(), 
            pl.col("OI").sum()
        )
    return df_resampled

if __name__ == '__main__':

    df = pl.read_csv("Sample.csv")
    prepared_df = prepare_data(df)
    resampled_df = resample_data(dataframe=prepared_df, timeframe='1mo')
    print(resampled_df)
    #resampled_df.write_csv("resampled_data.csv")

'''
We can use day volume and day oi columns by taking the last() value when resampling 
'''
```


==================================================
