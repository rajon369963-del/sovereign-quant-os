# ⚡ [QUANT-SOURCE-114] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_114_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: polymarket-whales (`PHASE4-QUANT-008`)
- **Full Name**: `PHASE4-QUANT-008_al1enjesus__polymarket-whales`
- **Description**: 🐋 Real-time whale trade tracker for Polymarket — get terminal alerts + Telegram notifications when smart money moves
- **GitHub Stars**: 63
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<div align="center">

# 🐋 polymarket-whales

CLI whale tracker for Polymarket — terminal alerts when smart money moves.

[Quick Start](#-quick-start) · [Configuration](#️-configuration) · [Features](#-features) · [Contributing](#-contributing)

![demo](https://raw.githubusercontent.com/al1enjesus/polymarket-whales/main/assets/demo.gif)

</div>

---

## What is this?

`polymarket-whales` monitors the [Polymarket](https://polymarket.com) CLOB API and fires an alert the moment a trade above your threshold hits the books. Prints to terminal with color-coded output. No sign-up, no API key, no infrastructure. Just Python.

**Don't want to self-host?** Subscribe to the live whale feed on Telegram: [@polymarketwhales_ai](https://t.me/polymarketwhales_ai)

---

## 📋 Example Output

```
══════════════════════════════════════════════════
🐋  polymarket-whales
══════════════════════════════════════════════════
  Min trade size : $500
  Check interval : 30s
══════════════════════════════════════════════════

🐋 WHALE ALERT  2026-03-20 14:23:01
───────────────────────────────────────────
Market : Will Trump tweet about crypto today?
Side   : YES
Amount : $2,847.00
Price  : 0.7300  (73% YES)
───────────────────────────────────────────

🐋 WHALE ALERT  2026-03-20 14:26:44
───────────────────────────────────────────
Market : Fed rate cut in March 2026?
Side   : NO
Amount : $12,500.00
Price  : 0.3100  (69% NO)
───────────────────────────────────────────
```

---

## ⚡ Quick Start

```bash
git clone https://github.com/al1enjesus/polymarket-whales
cd polymarket-whales
pip install -r requirements.txt
python main.py
```

That's it. Terminal alerts start immediately. No config needed to get started.

---

## ⚙️ Configuration

Copy `.env.example` to `.env` and edit:

```env
MIN_TRADE_SIZE=500        # USD — only alert above this
CHECK_INTERVAL=30         # seconds between polls

# Optional — Telegram push alerts
TELEGRAM_BOT_TOKEN=...
TELEGRAM_CHAT_ID=...
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/...
```

Or edit `config.yaml` directly. Environment variables take priority.

**Telegram setup (optional):**

1. Message [@BotFather](https://t.me/BotFather) → `/newbot` → copy the token
2. Message [@userinfobot](https://t.me/userinfobot) → copy your chat ID
3. Paste both into `.env`

> **Just want alerts without setup?** → [Join @polymarketwhales_ai](https://t.me/polymarketwhales_ai)

---

## ✨ Features

- ✅ Real-time polling of the Polymarket CLOB API
- ✅ Configurable minimum trade size (USD)
- ✅ Colorized terminal output — YES in green, NO in red
- ✅ Optional Telegram push alerts to any chat or channel
- ✅ Optional Discord webhook alerts
- ✅ Export whale trades to CSV or JSON (`--export whales.csv`)
- ✅ Auto-resolves market names from condition IDs
- ✅ Trade deduplication — no double alerts
- ✅ Graceful handling of network errors and API timeouts
- ✅ No database, no Docker, no setup beyond `pip install`

---

## 🛠️ Advanced

**Run in background:**
```bash
nohup python main.py > whales.log 2>&1 &
```

**Custom config path:**
```bash
python main.py --config /path/to/config.yaml
```

**Export whale trades to CSV or JSON:**
```bash
python main.py --export whales.csv
python main.py --export whales.json
```

**24/7 on a VPS:** Any $5/month VPS works — the script uses <10MB RAM.

---

## 🤝 Contributing

Good first issues:

- [x] Discord / Slack webhook support _(merged — thanks [@Deepak8858](https://github.com/Deepak8858)!)_
- [x] Historical whale data export (CSV / JSON) _(merged — thanks [@Deepak8858](https://github.com/Deepak8858)!)_
- [ ] Filter by specific market or category
- [ ] Track and tag recurring whale wallets
- [ ] Alert cooldown per market (avoid spam)
- [ ] Web dashboard (simple Flask/Streamlit UI)

Open an issue or send a PR — both welcome.

---

## 📡 Community & Live Whale Feed

Join **[@polymarketwhales_ai](https://t.me/polymarketwhales_ai)** on Telegram:

- 🐋 Live feed of large trades — real-time, no setup required
- 💬 Community chat — discuss strategies, share setups, post your whale catches
- 🤖 AI bot connected — ask questions, get market context, analyze trades

Whether you're running the script or just lurking for signals — this is the place.

---

## 🌍 Blocked by geo-restrictions?

Polymarket is unavailable in the US and some other countries. If you can't access it, you have two options:

**Option A — Self-host with a VPN/proxy**
Point the script at a proxy by setting `HTTPS_PROXY` in `.env`:
```env
HTTPS_PROXY=http://your-proxy:port
```

**Option B — Use PolyClawster's relay (recommended)**

[PolyClawster](https://polyclawster.com) runs a transparent proxy to `clob.polymarket.com`, deployed in Tokyo (outside US geo-blocks). It routes your API calls on their behalf — your requests never touch Polymarket directly.

- 🚫 No VPN needed
- 🚫 No KYC
- ✅ Full Polymarket CLOB API access from any country
- ✅ One line of config

Set in `.env`:
```env
POLYMARKET_API_URL=https://polyclawster.com/api/clob-relay
```

Then in `main.py` the script will use this base URL for all CLOB requests instead of hitting Polymarket directly.

The relay is the same infrastructure used by [PolyClawster](https://polyclawster.com) AI agents to trade Polymarket 24/7 from any country.

---

## 🤖 Want trades executed automatically?

This tool watches. [PolyClawster](https://polyclawster.com) acts.  
AI agent that copies whale moves and trades Polymarket 24/7 — works from any country, no VPN, no KYC, start with $10.

[![PolyClawster](https://img.shields.io/badge/PolyClawster-Trade%20Automatically-8b5cf6?style=for-the-badge)](https://polyclawster.com)

---

MIT · Built by [Virixlabs](https://virixlabs.com)

### Core Implementation Code & Architecture
#### File: `whale_of_day.py`
```python
#!/usr/bin/env python3
"""
Whale of the Day — daily auto-post to @polymarketwhales_ai
Finds the market with the biggest 24h volume spike on Polymarket.
"""

import os, sys, json, datetime, urllib.request, urllib.parse
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN  = os.getenv("TELEGRAM_BOT_TOKEN", "8721816606:AAHGpKrz2qNAoXwbguAQlEzYKj1TSkZdA4k")
CHAT_ID    = os.getenv("WHALE_CHANNEL_ID", "-1003518498844")
GAMMA_API  = "https://gamma-api.polymarket.com"

def fetch(url, timeout=15):
    req = urllib.request.Request(url, headers={"User-Agent": "polymarket-whales/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)

def get_top_markets():
    url = f"{GAMMA_API}/markets?limit=50&active=true&order=volume24hr&ascending=false"
    return fetch(url)

def get_biggest_whale_market(markets):
    """Find market with biggest 24h volume and interesting price action."""
    best = None
    for m in markets:
        vol24 = float(m.get("volume24hr") or 0)
        vol_total = float(m.get("volume") or 0)
        price = float(m.get("lastTradePrice") or 0)
        # Skip extreme prices (already decided) and tiny markets
        if vol24 < 100_000:
            continue
        if price < 0.02 or price > 0.98:
            continue
        score = vol24
        if best is None or score > best["score"]:
            best = {
                "score": score,
                "question": m.get("question", "Unknown market"),
                "slug": m.get("slug", ""),
                "vol24": vol24,
                "vol_total": vol_total,
                "price": price,
                "conditionId": m.get("conditionId", ""),
                "endDate": m.get("endDate", ""),
                "outcomes": m.get("outcomes", ""),
            }
    # Fallback: just pick top by vol24 regardless of price
    if best is None and markets:
        m = markets[0]
        best = {
            "score": float(m.get("volume24hr") or 0),
            "question": m.get("question", "Unknown market"),
            "slug": m.get("slug", ""),
            "vol24": float(m.get("volume24hr") or 0),
            "vol_total": float(m.get("volume") or 0),
            "price": float(m.get("lastTradePrice") or 0),
            "conditionId": m.get("conditionId", ""),
            "endDate": m.get("endDate", ""),
        }
    return best

def format_message(market):
    vol24 = market["vol24"]
    vol_total = market["vol_total"]
    price = market["price"]
    question = market["question"]
    slug = market["slug"]
    end_date = market.get("endDate", "")

    # Format end date
    try:
        dt = datetime.datetime.fromisoformat(end_date.replace("Z", "+00:00"))
        closes = dt.strftime("%b %d, %Y")
    except:
        closes = end_date[:10] if end_date else "TBD"

    # Price interpretation
    pct = price * 100
    side = "YES" if price >= 0.5 else "NO"
    side_emoji = "🟢" if side == "YES" else "🔴"
    opp_pct = 100 - pct if side == "YES" else pct

    market_url = f"https://polymarket.com/event/{slug}" if slug else "https://polymarket.com"

    today = datetime.datetime.utcnow().strftime("%b %d, %Y")

    msg = f"""🐋 *Whale of the Day* — {today}

*{question}*

{side_emoji} Market says: *{pct:.0f}% {side}*
💰 24h Volume: *${vol24/1_000_000:.1f}M*
📊 Total Volume: ${vol_total/1_000_000:.1f}M
📅 Closes: {closes}

Whales moved *${vol24/1_000_000:.1f}M* on this market today alone.

[🔗 Trade on Polymarket]({market_url})

_Track every whale move in real time 👇_
[GitHub](https://github.com/al1enjesus/polymarket-whales) · @polymarketwhales\\_ai"""

    return msg

def send_telegram(msg):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = json.dumps({
        "chat_id": CHAT_ID,
        "text": msg,
        "parse_mode": "Markdown",
        "disable_web_page_preview": False
    }).encode()
    req = urllib.request.Request(url, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.load(r)

def main():
    print("Fetching top markets by 24h volume...")
    markets = get_top_markets()
    print(f"Got {len(markets)} markets")

    whale = get_biggest_whale_market(markets)
    if not whale:
        print("No suitable market found", file=sys.stderr)
        sys.exit(1)

    print(f"Top whale market: {whale['question'][:60]}")
    print(f"24h volume: ${whale['vol24']:,.0f}")
    print(f"Price: {whale['price']:.2%}")

    msg = format_message(whale)
    print("\n--- Message preview ---")
    print(msg)
    print("---")

    result = send_telegram(msg)
    if result.get("ok"):
        print(f"✅ Posted! msg_id={result['result']['message_id']}")
    else:
        print(f"❌ Error: {result}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```

#### File: `main.py`
```python
#!/usr/bin/env python3
"""
🐋 Polymarket Whale Tracker
Monitors Polymarket for large trades and sends Telegram alerts.
"""

import os
import sys
import time
import logging
import requests
import yaml
import csv
import json
import argparse
from datetime import datetime, timezone
from dotenv import load_dotenv
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored output
init(autoreset=True)

# Load environment variables from .env file if present
load_dotenv()

# ─────────────────────────────────────────────
# Logging setup
# ─────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)


# ─────────────────────────────────────────────
# Config loader
# ─────────────────────────────────────────────
def load_config(path: str = "config.yaml") -> dict:
    """Load configuration from YAML file, with env var overrides."""
    config = {
        "min_trade_size": 500,
        "check_interval": 30,
        "telegram": {
            "bot_token": "",
            "chat_id": "",
        },
        "discord": {
            "webhook_url": "",
        },
        "polymarket": {
            "api_url": "https://clob.polymarket.com",
        },
    }

    if os.path.exists(path):
        with open(path, "r") as f:
            loaded = yaml.safe_load(f)
            if loaded:
                # Deep merge
                for key, val in loaded.items():
                    if isinstance(val, dict) and key in config:
                        config[key].update(val)
                    else:
                        config[key] = val

    # Environment variable overrides (takes priority over YAML)
    if os.getenv("TELEGRAM_BOT_TOKEN"):
        config["telegram"]["bot_token"] = os.getenv("TELEGRAM_BOT_TOKEN")
    if os.getenv("TELEGRAM_CHAT_ID"):
        config["telegram"]["chat_id"] = os.getenv("TELEGRAM_CHAT_ID")
    if os.getenv("DISCORD_WEBHOOK_URL"):
        config["discord"]["webhook_url"] = os.getenv("DISCORD_WEBHOOK_URL")
    if os.getenv("MIN_TRADE_SIZE"):
        config["min_trade_size"] = float(os.getenv("MIN_TRADE_SIZE"))

    return config


# ─────────────────────────────────────────────
# Polymarket API
# ─────────────────────────────────────────────
def fetch_recent_trades(api_url: str, limit: int = 100) -> list:
    """Fetch recent trades from Polymarket CLOB API."""
    url = f"{api_url}/trades"
    params = {"limit": limit}
    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        # The CLOB API returns {"data": [...], "next_cursor": ...}
        if isinstance(data, dict) and "data" in data:
            return data["data"]
        # Some endpoints return a list directly
        if isinstance(data, list):
            return data
        return []
    except requests.exceptions.ConnectionError:
        logger.warning("⚠️  Network error: could not reach Polymarket API.")
        return []
    except requests.exceptions.Timeout:
        logger.warning("⚠️  Request timed out fetching trades.")
        return []
    except requests.exceptions.HTTPError as e:
        logger.warning(f"⚠️  HTTP error fetching trades: {e}")
        return []
    except Exception as e:
        logger.warning(f"⚠️  Unexpected error fetching trades: {e}")
        return []


def fetch_market_info(condition_id: str) -> dict:
    """
    Fetch market metadata (title, etc.) from Polymarket Gamma API.
    Returns a dict with at least 'question' key.
    """
    url = "https://gamma-api.polymarket.com/markets"
    params = {"condition_id": condition_id}
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        if isinstance(data, list) and len(data) > 0:
            return data[0]
        if isinstance(data, dict):
            return data
        return {}
    except Exception as e:
        logger.debug(f"Could not fetch market info for {condition_id}: {e}")
        return {}


# ─────────────────────────────────────────────
# Trade processing
# ─────────────────────────────────────────────
def parse_trade_usd_size(trade: dict) -> float:
    """
    Calculate the USD size of a trade.
    size * price gives approximate USD value for a YES trade;
    size * (1 - price) for a NO trade — but simpler: use size as USDC shares.
    Polymarket CLOB: 'size' is the number of outcome shares, 'price' is in USD.
    USD value = size * price (for market buys).
    """
    try:
        size = float(trade.get("size", 0))
        price = float(trade.get("price", 0))
        return size * price
    except (TypeError, ValueError):
        return 0.0


def format_side(side: str) -> str:
    """Normalize side string to YES/NO."""
    s = str(side).upper()
    if s in ("YES", "BUY", "1"):
        return "YES"
    if s in ("NO", "SELL", "0"):
        return "NO"
    return side.upper()


def trade_unique_id(trade: dict) -> str:
    """Generate a unique identifier for a trade to avoid duplicate alerts."""
    return trade.get("id") or trade.get("trade_id") or str(trade)


# ─────────────────────────────────────────────
# Formatting
# ─────────────────────────────────────────────
DIVIDER = "─" * 43


def format_terminal_alert(market_title: str, side: str, amount_usd: float,
                           price: float, timestamp: str) -> str:
    """Format a colorful terminal alert message."""
    ts = timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    side_color = Fore.GREEN if side == "YES" else Fore.RED
    prob_pct = int(price * 100) if side == "YES" else int((1 - price) * 100)

    lines = [
        f"\n{Fore.CYAN}🐋 WHALE ALERT{Style.RESET_ALL}  {Fore.YELLOW}{ts}{Style.RESET_ALL}",
        f"{Fore.WHITE}{DIVIDER}{Style.RESET_ALL}",
        f"{Fore.WHITE}Market:{Style.RESET_ALL} {market_title}",
        f"{Fore.WHITE}Side:  {Style.RESET_ALL} {side_color}{side}{Style.RESET_ALL}",
        f"{Fore.WHITE}Amount:{Style.RESET_ALL} {Fore.YELLOW}${amount_usd:,.2f}{Style.RESET_ALL}",
        f"{Fore.WHITE}Price: {Style.RESET_ALL} {price:.4f} ({side_color}{prob_pct}% {side}{Style.RESET_ALL})",
        f"{Fore.WHITE}{DIVIDER}{Style.RESET_ALL}",
    ]
    return "\n".join(lines)


def format_telegram_message(market_title: str, side: str, amount_usd: float,
                             price: float, timestamp: str) -> str:
    """Format a Telegram alert message (plain text, emoji-rich)."""
    ts = timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    side_emoji = "✅" if side == "YES" else "❌"
    prob_pct = int(price * 100) if side == "YES" else int((1 - price) * 100)

    return (
        f"🐋 *WHALE ALERT*  `{ts}`\n"
        f"{'─' * 30}\n"
        f"*Market:* {market_title}\n"
        f"*Side:*    {side_emoji} {side}\n"
        f"*Amount:* `${amount_usd:,.2f}`\n"
        f"*Price:*   `{price:.4f}` ({prob_pct}% {side})\n"
        f"{'─' * 30}"
    )


# ─────────────────────────────────────────────
# Telegram sender
# ─────────────────────────────────────────────
def send_telegram_alert(bot_token: str, chat_id: str, message: str) -> bool:
    """Send a message via Telegram Bot API. Returns True on success."""
    if not bot_token or not chat_id:
        logger.debug("Telegram not configured — skipping alert.")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    }
    try:
        resp = requests.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        return True
    except requests.exceptions.HTTPError as e:
        logger.warning(f"Telegram HTTP error: {e} — response: {resp.text[:200]}")
        return False
    except Exception as e:
        logger.warning(f"Failed to send Telegram alert: {e}")
        return False


def format_discord_message(market_title: str, side: str, amount_usd: float,
                            price: float, timestamp: str) -> str:
    """Format a Discord alert message."""
    ts = timestamp or datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    side_emoji = "✅" if side == "YES" else "❌"
    prob_pct = int(price * 100) if side == "YES" else int((1 - price) * 100)

    return (
        f"🐋 **WHALE ALERT**  `{ts}`\n"
        f"{'─' * 30}\n"
        f"**Market:** {market_title}\n"
        f"**Side:**    {side_emoji} {side}\n"
        f"**Amount:** `${amount_usd:,.2f}`\n"
        f"**Price:**   `{price:.4f}` ({prob_pct}% {side})\n"
        f"{'─' * 30}"
    )


def send_discord_alert(webhook_url: str, message: str) -> bool:
    """Send a message via Discord Webhook API. Returns True on success."""
    if not webhook_url:
        logger.debug("Discord not configured — skipping alert.")
        return False

    payload = {
        "content": message,
    }
    try:
        resp = requests.post(webhook_url, json=payload, timeout=10)
        resp.raise_for_status()
        return True
    except requests.exceptions.HTTPError as e:
        logger.warning(f"Discord HTTP error: {e}")
        return False
    except Exception as e:
        logger.warning(f"Failed to send Discord alert: {e}")
        return False




def export_trade(file_path: str, trade_data: dict) -> None:
    """Export trade data to a CSV or JSON file."""
    if not file_path:
        return

    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == ".csv":
        file_exists = os.path.isfile(file_path)
        with open(file_path, "a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=trade_data.keys())
            if not file_exists:
                writer.writeheader()
            writer.writerow(trade_data)
    elif ext == ".json":
        all_data = []
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r") as f:
                    all_data = json.load(f)
            except (json.JSONDecodeError, ValueError):
                all_data = []
        
        all_data.append(trade_data)
        with open(file_path, "w") as f:
            json.dump(all_data, f, indent=2)
    else:
        logger.warning(f"Unsupported export format: {ext}. Use .csv or .json.")

# ─────────────────────────────────────────────
# Market info cache (avoid hammering the API)
# ─────────────────────────────────────────────
_market_cache: dict = {}


def get_market_title(condition_id: str) -> str:
    """Return market title, using a local cache to reduce API calls."""
    if condition_id in _market_cache:
        return _market_cache[condition_id]

    info = fetch_market_info(condition_id)
    title = (
        info.get("question")
        or info.get("title")
        or info.get("name")
        or f"Market {condition_id[:10]}..."
    )
    _market_cache[condition_id] = title
    return title


# ─────────────────────────────────────────────
# Main loop
# ─────────────────────────────────────────────
def run(config: dict, export_path: str = None) -> None:
    """Main monitoring loop."""
    min_size = float(config["min_trade_size"])
    interval = int(config["check_interval"])
    # Allow env var override — useful for geo-restricted regions
    # Set POLYMARKET_API_URL=https://polyclawster.com/api/clob-relay to bypass geo-blocks
    api_url = os.getenv("POLYMARKET_API_URL", config["polymarket"]["api_url"])
    bot_token = config["telegram"]["bot_token"]
    chat_id = config["telegram"]["chat_id"]
    discord_webhook = config["discord"]["webhook_url"]

    telegram_enabled = bool(bot_token and chat_id and
                            bot_token != "YOUR_BOT_TOKEN" and
                            chat_id != "YOUR_CHAT_ID")
    discord_enabled = bool(discord_webhook and
                           discord_webhook != "YOUR_DISCORD_WEBHOOK_URL")

    print(f"\n{Fore.CYAN}{'═' * 50}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}🐋  Polymarket Whale Tracker — Starting up{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═' * 50}{Style.RESET_ALL}")
    print(f"  Min trade size : {Fore.YELLOW}${min_size:,.0f}{Style.RESET_ALL}")
    print(f"  Check interval : {Fore.YELLOW}{interval}s{Style.RESET_ALL}")
    print(f"  Telegram alerts: {Fore.GREEN+'ON' if telegram_enabled else Fore.RED+'OFF'}{Style.RESET_ALL}")
    print(f"  Discord alerts : {Fore.GREEN+'ON' if discord_enabled else Fore.RED+'OFF'}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'═' * 50}{Style.RESET_ALL}\n")

    if not (telegram_enabled or discord_enabled):
        logger.info("ℹ️  Alerts not configured — terminal-only mode.")

    seen_ids: set = set()
    first_run = True

    while True:
        try:
            trades = fetch_recent_trades(api_url)
        except KeyboardInterrupt:
            raise
        except Exception as e:
            logger.error(f"Error in fetch loop: {e}")
            trades = []

        new_seen: set = set()
        whale_count = 0

        for trade in trades:
            trade_id = trade_unique_id(trade)
            new_seen.add(trade_id)

            # On first run, just populate seen_ids (don't alert on old trades)
            if first_run:
                continue

            # Skip already-seen trades
            if trade_id in seen_ids:
                continue

            # Calculate USD size and filter
            amount_usd = parse_trade_usd_size(trade)
            if amount_usd < min_size:
                continue

            whale_count += 1

            # Get trade details
            condition_id = trade.get("market") or trade.get("condition_id", "")
            side_raw = trade.get("side", trade.get("outcome", ""))
            side = format_side(side_raw)
            price = float(trade.get("price", 0))
            ts_raw = trade.get("timestamp") or trade.get("created_at", "")

            # Parse timestamp
            if ts_raw:
                try:
                    if isinstance(ts_raw, (int, float)):
                        ts = datetime.fromtimestamp(ts_raw, tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        ts = str(ts_raw)[:19].replace("T", " ")
                except Exception:
                    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
            else:
                ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

            # Fetch market title
            market_title = get_market_title(condition_id) if condition_id else "Unknown Market"

            # Print terminal alert
            print(format_terminal_alert(market_title, side, amount_usd, price, ts))

            # Send Telegram alert
            if telegram_enabled:
                tg_msg = format_telegram_message(market_title, side, amount_usd, price, ts)
                ok = send_telegram_alert(bot_token, chat_id, tg_msg)
     
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: pybroker (`PHASE4-QUANT-040`)
- **Full Name**: `PHASE4-QUANT-040_edtechre__pybroker`
- **Description**: Algorithmic Trading in Python with Machine Learning
- **GitHub Stars**: 3542
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<img src="https://github.com/edtechre/pybroker/blob/master/docs/_static/pybroker-logo.png?raw=true" alt="PyBroker">

[![python](https://img.shields.io/badge/python-v3-brightgreen.svg)](https://www.python.org/)
[![Apache 2.0 with Commons Clause](https://img.shields.io/badge/license-Apache%202.0%20Clause-green)](https://www.pybroker.com/en/latest/license.html)
[![Documentation Status](https://readthedocs.org/projects/pybroker/badge/?version=latest)](https://www.pybroker.com/en/latest/?badge=latest)
[![Package status](https://github.com/edtechre/pybroker/actions/workflows/main.yml/badge.svg?event=push)](https://github.com/edtechre/pybroker/actions)
[![Downloads](https://static.pepy.tech/badge/lib-pybroker)](https://pepy.tech/project/lib-pybroker)
[![Github stars](https://img.shields.io/github/stars/edtechre/pybroker?style=social)](https://github.com/edtechre/pybroker/)
[![Twitter](https://img.shields.io/twitter/follow/libpybroker?style=social)](https://twitter.com/intent/follow?screen_name=libpybroker)

## Algorithmic Trading in Python with Machine Learning

Are you looking to enhance your trading strategies with the power of Python and
machine learning? **PyBroker** is a Python framework
designed for developing algorithmic trading strategies, with a focus on
strategies that use machine learning. With PyBroker, you can easily create and
fine-tune trading rules, build powerful models, and gain valuable insights into
your strategy’s performance.

## Key Features

* A super-fast backtesting engine built in [NumPy](https://numpy.org/) and accelerated with [Numba](https://numba.pydata.org/).
* Easy creation of trading rules and models for executing across multiple instruments.
* Integration of trading signals across [multiple time intervals](https://www.pybroker.com/en/latest/notebooks/15.%20Multiple%20Time%20Intervals.html), including daily, weekly, and monthly.
* Access to historical data from [Alpaca](https://alpaca.markets/), [Yahoo Finance](https://finance.yahoo.com/), [AKShare](https://github.com/akfamily/akshare), or from [your own data provider](https://www.pybroker.com/en/latest/notebooks/7.%20Creating%20a%20Custom%20Data%20Source.html).
* Model training and backtesting using [Walkforward Analysis](https://www.pybroker.com/en/latest/notebooks/6.%20Training%20a%20Model.html#Walkforward-Analysis), which simulates how the strategy would perform during actual trading.
* Reliable trading metrics that use randomized [bootstrapping](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)) to provide more accurate results.
* [Parameter optimization](https://www.pybroker.com/en/latest/notebooks/12.%20Parameter%20Optimization.html) with [Optuna](https://optuna.org/) to select the best strategy parameters.
* [Caching](https://www.pybroker.com/en/latest/notebooks/1.%20Getting%20Started%20with%20Data%20Sources.html#Caching-Data) of downloaded data, indicators, and models to speed up your development process.
* [Parallelized](https://www.pybroker.com/en/latest/notebooks/11.%20Configuring%20Parallelization.html) computation and training for faster performance.
* [Agent Skills](https://www.pybroker.com/en/latest/agent-skills.html) that help AI agents write trading strategies and backtests using PyBroker.

PyBroker provides you with the tools to build, test, and evaluate algorithmic trading strategies backed by machine learning.

## Installation

PyBroker supports Python 3.11+ on Windows, Mac, and Linux. You can install
PyBroker using ``pip``:

```bash
   pip install -U lib-pybroker
```

Or you can clone the Git repository with:

```bash
   git clone https://github.com/edtechre/pybroker
```

## A Quick Example

Here's a glimpse of what backtesting with PyBroker looks like with these code
snippets:

**Rule-based Strategy**:

```python
   from pybroker import Strategy, YFinance, highest

   def exec_fn(ctx):
      # Get the rolling 10 day high.
      high_10d = ctx.indicator('high_10d')
      # Buy on a new 10 day high.
      if not ctx.long_pos() and high_10d[-1] > high_10d[-2]:
         ctx.buy_shares = 100
         # Hold the position for 5 days.
         ctx.hold_bars = 5
         # Set a stop loss of 2%.
         ctx.stop_loss_pct = 2

   strategy = Strategy(YFinance(), start_date='1/1/2025', end_date='8/1/2026')
   strategy.add_execution(
      exec_fn, ['AAPL', 'MSFT'], indicators=highest('high_10d', 'close', period=10))
   # Run the backtest after 20 days have passed.
   result = strategy.backtest(warmup=20)
```

**Model-based Strategy**:

```python
   import pybroker
   from pybroker import Alpaca, Strategy

   def train_fn(symbol, train_data, test_data):
      # Train the model using indicators stored in train_data.
      ...
      return trained_model

   # Register the model and its training function with PyBroker.
   my_model = pybroker.model('my_model', train_fn, indicators=[...])

   def exec_fn(ctx):
      preds = ctx.preds('my_model')
      if not ctx.long_pos() and preds[-1] > buy_threshold:
         ctx.buy_shares = 100
      elif ctx.long_pos() and preds[-1] < sell_threshold:
         ctx.sell_all_shares()

   alpaca = Alpaca(api_key=..., api_secret=...)
   strategy = Strategy(alpaca, start_date='1/1/2025', end_date='8/1/2026')
   strategy.add_execution(exec_fn, ['AAPL', 'MSFT'], models=my_model)
   # Run Walkforward Analysis on 1 minute data using 5 windows with 50/50 train/test data.
   result = strategy.walkforward(timeframe='1m', windows=5, train_size=0.5)
```

## User Guide

- [Getting Started with Data Sources](https://www.pybroker.com/en/latest/notebooks/1.%20Getting%20Started%20with%20Data%20Sources.html)
- [Backtesting a Strategy](https://www.pybroker.com/en/latest/notebooks/2.%20Backtesting%20a%20Strategy.html)
- [Evaluating with Bootstrap Metrics](https://www.pybroker.com/en/latest/notebooks/3.%20Evaluating%20with%20Bootstrap%20Metrics.html)
- [Ranking Long and Short Signals](https://www.pybroker.com/en/latest/notebooks/4.%20Ranking%20Long%20and%20Short%20Signals.html)
- [Writing Indicators](https://www.pybroker.com/en/latest/notebooks/5.%20Writing%20Indicators.html)
- [Training a Model](https://www.pybroker.com/en/latest/notebooks/6.%20Training%20a%20Model.html)
- [Creating a Custom Data Source](https://www.pybroker.com/en/latest/notebooks/7.%20Creating%20a%20Custom%20Data%20Source.html)
- [Applying Stops](https://www.pybroker.com/en/latest/notebooks/8.%20Applying%20Stops.html)
- [Rebalancing Positions](https://www.pybroker.com/en/latest/notebooks/9.%20Rebalancing%20Positions.html)
- [Rotational Trading](https://www.pybroker.com/en/latest/notebooks/10.%20Rotational%20Trading.html)
- [Configuring Parallelization](https://www.pybroker.com/en/latest/notebooks/11.%20Configuring%20Parallelization.html)
- [Parameter Optimization](https://www.pybroker.com/en/latest/notebooks/12.%20Parameter%20Optimization.html)
- [Margin Trading](https://www.pybroker.com/en/latest/notebooks/13.%20Margin%20Trading.html)
- [Modeling Slippage](https://www.pybroker.com/en/latest/notebooks/14.%20Modeling%20Slippage.html)
- [Multiple Time Intervals](https://www.pybroker.com/en/latest/notebooks/15.%20Multiple%20Time%20Intervals.html)
- [Time Series Models](https://www.pybroker.com/en/latest/notebooks/16.%20Time%20Series%20Models.html)
- [Multi-Symbol Models](https://www.pybroker.com/en/latest/notebooks/17.%20Multi-Symbol%20Models.html)
- [Dynamic Symbol Selection](https://www.pybroker.com/en/latest/notebooks/18.%20Dynamic%20Symbol%20Selection.html)
- [Agent Skills](https://www.pybroker.com/en/latest/agent-skills.html)
- [FAQs](https://www.pybroker.com/en/latest/notebooks/FAQs.html)

## AI Agent Skills

PyBroker v2 now includes [AI agent skills](https://www.pybroker.com/en/latest/agent-skills.html) for coding agents:

- [Strategy Creator](https://www.pybroker.com/en/latest/agent-skills.html#skill-pybroker-strategy-creator)
- [Indicator Creator](https://www.pybroker.com/en/latest/agent-skills.html#skill-pybroker-indicator-creator)
- [Model Trainer](https://www.pybroker.com/en/latest/agent-skills.html#skill-pybroker-model-trainer)
- [Parameter Optimization](https://www.pybroker.com/en/latest/agent-skills.html#skill-pybroker-optimize)
- [Multi-Interval Strategies](https://www.pybroker.com/en/latest/agent-skills.html#skill-pybroker-multi-interval)
- [Rotational Trading](https://www.pybroker.com/en/latest/agent-skills.html#skill-pybroker-rotational-trading)

## Online Documentation

[The full reference documentation is hosted at **www.pybroker.com**.](https://www.pybroker.com)

(For Chinese users: [中文文档](https://www.pybroker.com/zh_CN/latest/), courtesy of [Albert King](https://github.com/albertandking).)

## Contact

<img src="https://github.com/edtechre/pybroker/blob/master/docs/_static/email-image.png?raw=true">

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `src/pybroker/ext/__init__.py`
```python

```

#### File: `.bench/timeframe-baseline.json`
```python
{
  "metrics": {
    "compress_5m_390": 12.99227587878704,
    "compress_5m_large": 3356.1703376471996,
    "compress_every5_large": 3293.883642181754,
    "compress_symbol_df_weekly_252": 590.3713218867779,
    "compress_timeframes_multi": 9920.406504534185,
    "compress_weekly_252": 9.008278138935566
  }
}
```

#### File: `benchmarks/__init__.py`
```python
"""asv benchmark suite for pybroker.

Run locally with::

    asv run HEAD^!                  # benchmark current commit
    asv continuous master HEAD      # diff master vs current branch
    asv publish && asv preview      # HTML dashboard

CI runs ``asv continuous origin/master HEAD`` on every PR and posts a
sticky comment (``.github/workflows/asv-pr.yml``).
"""
```

#### File: `asv.conf.json`
```python
{
  "version": 1,
  "project": "pybroker",
  "project_url": "https://www.pybroker.com",
  "repo": ".",
  "branches": ["dev"],
  "dvcs": "git",
  "environment_type": "virtualenv",
  "install_timeout": 600,
  "show_commit_url": "https://github.com/edtechre/pybroker/commit/",
  "pythons": ["3.11", "3.12", "3.13", "3.14"],
  "install_command": [
    "in-dir={build_dir} python -mpip install -e ."
  ],
  "uninstall_command": [
    "return-code=any python -mpip uninstall -y {project}"
  ],
  "build_command": [],
  "benchmark_dir": "benchmarks",
  "env_dir": ".asv/env",
  "results_dir": ".asv/results",
  "html_dir": ".asv/html",
  "build_cache_size": 8
}
```

#### File: `.github/python-versions.json`
```python
{
  "//": [
    "Single source of truth for the Python versions CI uses.",
    "'versions' drives the test matrix, the asv PR gate and the asv nightly",
    "matrix; 'tooling' is the one interpreter for format, lint, typecheck,",
    "docs and the sdist build. Workflows read this file with fromJSON();",
    "declaration sites that cannot (setup.cfg, asv.conf.json, pyproject.toml,",
    ".readthedocs.yml) are held to it by",
    ".github/scripts/check_python_versions.py, which CI runs on every push.",
    "Adding a version is one entry here plus whatever that check reports."
  ],
  "versions": ["3.11", "3.12", "3.13", "3.14"],
  "tooling": "3.12"
}
```


==================================================


## [3/3] Repository: EPAT (`PHASE4-QUANT-056`)
- **Full Name**: `PHASE4-QUANT-056_sjdKRM__EPAT`
- **Description**: Executive Programme in Algorithmic Trading by QuantInsti
- **GitHub Stars**: 11
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
This repository showcases my journey through the prestigious **Executive Program in Algorithmic Trading (EPAT)**, a globally recognized certification program offered by **QuantInsti**. EPAT focuses on empowering professionals with the knowledge and skills required to excel in the field of algorithmic and quantitative trading.

### About EPAT
EPAT is a comprehensive program designed for individuals aiming to specialize in financial markets, data analysis, and quantitative strategies. The program combines cutting-edge tools, theoretical foundations, and practical applications across various domains of trading and quantitative finance. It covers:

- **Programming and Data Analysis**: Python, R, Excel, and other essential tools for financial data modeling.
- **Mathematical and Statistical Techniques**: Probability, regression, time-series analysis, and machine learning for strategy building.
- **Algorithmic Trading Strategies**: Momentum, mean-reversion, statistical arbitrage, and options trading.
- **Risk Management and Execution**: Techniques for portfolio optimization, risk control, and market impact minimization.
- **Market Microstructure**: Understanding trading systems, order types, and high-frequency trading dynamics.

### About This Repository
This repository contains projects I have completed during the program, guided by the EPAT curriculum. It is a demonstration of the practical application of the knowledge gained, covering topics such as:

- Quantitative finance concepts
- Algorithmic strategy development
- Backtesting and optimization techniques
- Risk assessment and portfolio management

The repository is a work-in-progress as I continue to refine and add new projects while progressing through the EPAT program. Each project reflects the use of real-world tools, industry-best practices, and advanced financial modeling techniques.


==================================================
