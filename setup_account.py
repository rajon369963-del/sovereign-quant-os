#!/usr/bin/env python3
"""
SOVEREIGN 24/7 TRADING ENGINE — ACCOUNT SETUP WIZARD
Auto-validates all broker connections, paper-trades to verify flow,
then generates a readiness report.

Usage:
  python setup_account.py --check      # Check credentials + connectivity
  python setup_account.py --paper      # Run 60s paper trade simulation
  python setup_account.py --shoonya    # Test Shoonya login only
  python setup_account.py --crypto     # Test crypto exchange only
  python setup_account.py --full       # Full end-to-end setup check
"""
import os
import sys
import json
import time
import argparse
import traceback
from datetime import datetime
from pathlib import Path

# ── Load .env ────────────────────────────────────────────────
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
    print("✅ .env loaded")
except ImportError:
    print("⚠️  python-dotenv not installed, reading os.environ directly")

# ── Rich terminal output ──────────────────────────────────────
try:
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    console = Console()
    RICH = True
except ImportError:
    RICH = False
    class Console:
        def print(self, *args, **kwargs): print(*args)
    console = Console()

ENGINE_DIR = Path(__file__).parent
REPORT_PATH = ENGINE_DIR / "account_setup_report.json"

# ════════════════════════════════════════════════════════════
# CONNECTIVITY CHECKS
# ════════════════════════════════════════════════════════════

def check_internet():
    """Basic internet check."""
    import requests
    try:
        r = requests.get("https://api.ipify.org?format=json", timeout=5)
        ip = r.json()["ip"]
        console.print(f"  ✅ Internet OK — Public IP: {ip}")
        return True, ip
    except Exception as e:
        console.print(f"  ❌ No internet: {e}")
        return False, None


def check_shoonya():
    """Test Shoonya (Finvasia) connection."""
    results = {"broker": "shoonya", "status": "UNCHECKED", "notes": ""}
    try:
        from NorenRestApiPy.NorenApi import NorenApi
        import pyotp

        user = os.environ.get("SHOONYA_USER", "")
        pwd = os.environ.get("SHOONYA_PASSWORD", "")
        totp_secret = os.environ.get("SHOONYA_TOTP_SECRET", "")
        vendor_code = os.environ.get("SHOONYA_VENDOR_CODE", "")
        api_secret = os.environ.get("SHOONYA_API_SECRET", "")
        imei = os.environ.get("SHOONYA_IMEI", "867073046952132")

        if not all([user, pwd, vendor_code, api_secret]):
            results["status"] = "CREDENTIALS_MISSING"
            results["notes"] = "Fill SHOONYA_USER, SHOONYA_PASSWORD, SHOONYA_VENDOR_CODE, SHOONYA_API_SECRET in .env"
            console.print("  ⚠️  Shoonya credentials missing — see .env.template")
            return results

        api = NorenApi(
            host="https://api.shoonya.com/NorenWClientTP/",
            websocket="wss://api.shoonya.com/NorenWSTP/"
        )

        totp = pyotp.TOTP(totp_secret).now() if totp_secret else ""

        ret = api.login(
            userid=user,
            password=pwd,
            twoFA=totp,
            vendor_code=vendor_code,
            api_secret=api_secret,
            imei=imei
        )

        if ret and ret.get("stat") == "Ok":
            results["status"] = "CONNECTED"
            results["notes"] = f"Session token obtained. Account: {ret.get('uname', user)}"
            console.print(f"  ✅ Shoonya CONNECTED — {ret.get('uname', user)}")

            # Check funds
            try:
                funds = api.get_limits()
                if funds:
                    cash = funds.get("cash", "unknown")
                    results["available_cash"] = cash
                    console.print(f"  💰 Available Cash: ₹{cash}")
            except Exception:
                pass
        else:
            results["status"] = "LOGIN_FAILED"
            results["notes"] = str(ret)
            console.print(f"  ❌ Shoonya login failed: {ret}")

    except ImportError:
        results["status"] = "PACKAGE_MISSING"
        results["notes"] = "Run: pip install NorenRestApiPy"
        console.print("  ❌ NorenRestApiPy not installed")
    except Exception as e:
        results["status"] = "ERROR"
        results["notes"] = str(e)
        console.print(f"  ❌ Shoonya error: {e}")

    return results


def check_zerodha():
    """Test Zerodha KiteConnect connection."""
    results = {"broker": "zerodha", "status": "UNCHECKED", "notes": ""}
    try:
        from kiteconnect import KiteConnect
        import pyotp

        api_key = os.environ.get("ZERODHA_API_KEY", "")
        api_secret = os.environ.get("ZERODHA_API_SECRET", "")

        if not all([api_key, api_secret]):
            results["status"] = "CREDENTIALS_MISSING"
            results["notes"] = "Fill ZERODHA_API_KEY and ZERODHA_API_SECRET in .env"
            console.print("  ⚠️  Zerodha credentials missing — see .env.template")
            return results

        kite = KiteConnect(api_key=api_key)
        login_url = kite.login_url()
        results["status"] = "CREDENTIALS_PRESENT"
        results["login_url"] = login_url
        results["notes"] = f"Visit login URL to get request_token: {login_url}"
        console.print(f"  ℹ️  Zerodha: API Key present. Manual login needed once.")
        console.print(f"  🔗 Login URL: {login_url}")
        console.print(f"  📋 After login, paste request_token in .env as ZERODHA_REQUEST_TOKEN")

    except ImportError:
        results["status"] = "PACKAGE_MISSING"
        results["notes"] = "Run: pip install kiteconnect"
    except Exception as e:
        results["status"] = "ERROR"
        results["notes"] = str(e)

    return results


def check_crypto(exchange_name="binance"):
    """Test crypto exchange via CCXT."""
    results = {"broker": f"crypto_{exchange_name}", "status": "UNCHECKED", "notes": ""}
    try:
        import ccxt

        api_key = os.environ.get(f"{exchange_name.upper()}_API_KEY", "")
        api_secret = os.environ.get(f"{exchange_name.upper()}_API_SECRET", "")
        testnet = os.environ.get(f"{exchange_name.upper()}_TESTNET", "true").lower() == "true"

        # Even without credentials, check market data connectivity
        exchange_class = getattr(ccxt, exchange_name)
        exchange = exchange_class({
            "apiKey": api_key,
            "secret": api_secret,
            "sandbox": testnet,
            "enableRateLimit": True,
        })

        # Test public API (no auth needed)
        ticker = exchange.fetch_ticker("BTC/USDT")
        btc_price = ticker["last"]
        results["btc_price_usd"] = btc_price
        console.print(f"  ✅ {exchange_name.upper()} public API OK — BTC: \${btc_price:,.0f}")

        if api_key and api_secret:
            try:
                balance = exchange.fetch_balance()
                usdt = balance.get("USDT", {}).get("free", 0)
                results["usdt_balance"] = usdt
                results["status"] = "CONNECTED_WITH_AUTH"
                console.print(f"  ✅ {exchange_name.upper()} authenticated — USDT balance: {usdt}")
            except Exception as auth_err:
                results["status"] = "PUBLIC_ONLY"
                results["notes"] = f"Public API works. Auth failed: {auth_err}"
                console.print(f"  ⚠️  {exchange_name.upper()} auth failed (add API key in .env): {str(auth_err)[:60]}")
        else:
            results["status"] = "PUBLIC_ONLY"
            results["notes"] = "No API key — public data only. Add keys for live trading."

    except ImportError:
        results["status"] = "PACKAGE_MISSING"
        results["notes"] = "Run: pip install ccxt"
    except Exception as e:
        results["status"] = "ERROR"
        results["notes"] = str(e)
        console.print(f"  ❌ {exchange_name} error: {e}")

    return results


def check_telegram():
    """Test Telegram notification bot."""
    results = {"service": "telegram", "status": "UNCHECKED"}
    try:
        import requests
        token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
        chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")

        if not token or not chat_id:
            results["status"] = "NOT_CONFIGURED"
            console.print("  ⚠️  Telegram not configured (optional — add to .env for alerts)")
            return results

        r = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            json={"chat_id": chat_id, "text": "🤖 Sovereign Trading Engine: Account setup test ✅"}
        )
        if r.ok and r.json().get("ok"):
            results["status"] = "CONNECTED"
            console.print("  ✅ Telegram bot connected — test message sent!")
        else:
            results["status"] = "ERROR"
            results["notes"] = r.text

    except Exception as e:
        results["status"] = "ERROR"
        results["notes"] = str(e)

    return results


def run_paper_trade_simulation():
    """60-second paper trading simulation to verify signal → order flow."""
    console.print("\n[bold cyan]📊 Running 60s Paper Trade Simulation...[/bold cyan]" if RICH else "\n📊 Running 60s Paper Trade Simulation...")

    try:
        import pandas as pd
        import numpy as np
        import yfinance as yf

        # Download NIFTY50 data
        console.print("  📥 Fetching NIFTY50 data from Yahoo Finance...")
        ticker = yf.Ticker("^NSEI")
        hist = ticker.history(period="5d", interval="5m")

        if hist.empty:
            console.print("  ⚠️  No data from Yahoo Finance — using synthetic data")
            np.random.seed(42)
            prices = 25000 + np.cumsum(np.random.randn(50) * 10)
            closes = pd.Series(prices)
        else:
            closes = hist["Close"].tail(50)
            console.print(f"  ✅ Got {len(closes)} candles. Last close: ₹{closes.iloc[-1]:,.2f}")

        # Simple SMA crossover strategy
        sma5 = closes.rolling(5).mean()
        sma20 = closes.rolling(20).mean()

        signals = []
        capital = float(os.environ.get("INITIAL_CAPITAL_INR", "1000"))
        daily_loss_limit = float(os.environ.get("DAILY_LOSS_LIMIT_INR", "20"))
        position = None
        pnl = 0

        for i in range(20, len(closes)):
            price = closes.iloc[i]
            fast = sma5.iloc[i]
            slow = sma20.iloc[i]
            prev_fast = sma5.iloc[i-1]
            prev_slow = sma20.iloc[i-1]

            # BUY signal: SMA5 crosses above SMA20
            if prev_fast <= prev_slow and fast > slow and position is None:
                qty = max(1, int(capital * 0.01 / price))
                position = {"entry": price, "qty": qty, "type": "BUY"}
                signals.append({"bar": i, "action": "BUY", "price": price, "qty": qty})

            # SELL signal: SMA5 crosses below SMA20
            elif prev_fast >= prev_slow and fast < slow and position:
                trade_pnl = (price - position["entry"]) * position["qty"]
                pnl += trade_pnl
                signals.append({"bar": i, "action": "SELL", "price": price, "qty": position["qty"], "pnl": trade_pnl})
                position = None

                # Circuit breaker
                if pnl < -daily_loss_limit:
                    console.print(f"  🔴 CIRCUIT BREAKER TRIGGERED at bar {i} — Daily loss ₹{pnl:.2f} > limit ₹{daily_loss_limit}")
                    break

        console.print(f"\n  📊 Paper Simulation Results:")
        console.print(f"     Signals generated: {len(signals)}")
        console.print(f"     Total P&L: ₹{pnl:.2f}")
        console.print(f"     Final capital: ₹{capital + pnl:.2f}")

        return {
            "status": "PAPER_TRADE_OK",
            "signals": len(signals),
            "pnl_inr": round(pnl, 2),
            "final_capital": round(capital + pnl, 2)
        }

    except Exception as e:
        console.print(f"  ❌ Paper trade error: {e}")
        return {"status": "PAPER_TRADE_ERROR", "error": str(e)}


# ════════════════════════════════════════════════════════════
# MAIN SETUP WIZARD
# ════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description="Sovereign Trading Engine Account Setup")
    parser.add_argument("--check", action="store_true", help="Check all credentials")
    parser.add_argument("--paper", action="store_true", help="Run paper trade simulation")
    parser.add_argument("--shoonya", action="store_true", help="Test Shoonya only")
    parser.add_argument("--crypto", action="store_true", help="Test crypto only")
    parser.add_argument("--full", action="store_true", help="Full setup check")
    args = parser.parse_args()

    if not any(vars(args).values()):
        args.full = True  # Default to full

    console.print("\n" + "="*60)
    console.print("⚡ SOVEREIGN TRADING ENGINE — ACCOUNT SETUP WIZARD")
    console.print(f"   {datetime.now().strftime('%Y-%m-%d %H:%M:%S IST')}")
    console.print("="*60 + "\n")

    report = {
        "timestamp": datetime.now().isoformat(),
        "checks": {}
    }

    # 1. Internet
    console.print("🌐 [1/6] Internet Connectivity")
    ok, ip = check_internet()
    report["checks"]["internet"] = {"ok": ok, "ip": ip}

    # 2. .env file check
    console.print("\n📄 [2/6] .env File Status")
    env_path = ENGINE_DIR / ".env"
    if env_path.exists():
        console.print("  ✅ .env file exists")
        report["checks"]["env_file"] = "EXISTS"
    else:
        console.print("  ⚠️  .env file missing — copying from .env.template")
        import shutil
        template = ENGINE_DIR / ".env.template"
        if template.exists():
            shutil.copy(template, env_path)
            console.print("  ✅ .env created from template — FILL IN YOUR CREDENTIALS")
        report["checks"]["env_file"] = "CREATED_FROM_TEMPLATE"

    # 3. Shoonya
    if args.shoonya or args.full or args.check:
        console.print("\n🏦 [3/6] Shoonya (MCX + NSE Broker)")
        shoonya_result = check_shoonya()
        report["checks"]["shoonya"] = shoonya_result

    # 4. Zerodha
    if args.full or args.check:
        console.print("\n🏦 [4/6] Zerodha KiteConnect")
        zerodha_result = check_zerodha()
        report["checks"]["zerodha"] = zerodha_result

    # 5. Crypto
    if args.crypto or args.full or args.check:
        exchange = os.environ.get("CRYPTO_EXCHANGE", "binance")
        console.print(f"\n₿ [5/6] Crypto Exchange ({exchange.upper()})")
        crypto_result = check_crypto(exchange)
        report["checks"]["crypto"] = crypto_result

    # 6. Telegram
    if args.full or args.check:
        console.print("\n📱 [6/6] Telegram Notifications")
        tg_result = check_telegram()
        report["checks"]["telegram"] = tg_result

    # Paper trade
    if args.paper or args.full:
        paper_result = run_paper_trade_simulation()
        report["checks"]["paper_trade"] = paper_result

    # ── Summary ─────────────────────────────────────────────
    console.print("\n" + "="*60)
    console.print("📋 SETUP READINESS SUMMARY")
    console.print("="*60)

    ready = []
    needs_action = []

    for check_name, result in report["checks"].items():
        if isinstance(result, dict):
            status = result.get("status", "")
            if status in ("CONNECTED", "CONNECTED_WITH_AUTH", "PAPER_TRADE_OK"):
                ready.append(f"✅ {check_name}: {status}")
            elif status in ("CREDENTIALS_MISSING", "NOT_CONFIGURED", "CREDENTIALS_PRESENT"):
                needs_action.append(f"⚠️  {check_name}: {result.get('notes', status)[:80]}")
            elif status == "PUBLIC_ONLY":
                needs_action.append(f"🔑 {check_name}: Add API keys to .env for live trading")
            else:
                needs_action.append(f"❌ {check_name}: {status} — {result.get('notes', '')[:60]}")
        elif result in (True, "EXISTS"):
            ready.append(f"✅ {check_name}")

    for r in ready:
        console.print(f"  {r}")
    for n in needs_action:
        console.print(f"  {n}")

    # Paper mode status
    paper_mode = os.environ.get("PAPER_TRADING_MODE", "true").lower()
    if paper_mode == "true":
        console.print("\n  🧪 MODE: PAPER TRADING (safe — no real money)")
        console.print("     Set PAPER_TRADING_MODE=false in .env to go LIVE")
    else:
        console.print("\n  🔴 MODE: LIVE TRADING — Real money at stake!")

    # Save report
    with open(REPORT_PATH, "w") as f:
        json.dump(report, f, indent=2, default=str)
    console.print(f"\n✅ Full report saved: {REPORT_PATH}")
    console.print("\n" + "="*60)
    console.print("NEXT STEP: Fill credentials in .env, then run:")
    console.print("  python setup_account.py --shoonya   # Test broker")
    console.print("  python setup_account.py --paper     # Paper trade")
    console.print("  python sovereign_master_120_hacks_120_wheels_engine.py --paper")
    console.print("="*60 + "\n")

    return report


if __name__ == "__main__":
    main()
