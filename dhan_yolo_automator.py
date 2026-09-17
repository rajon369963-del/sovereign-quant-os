#!/usr/bin/env python3
"""
⚡ DHAN YOLO AUTOMATOR
=====================
Zero-friction setup for Rajon:
Antigravity launches Chrome to https://web.dhan.co for instant QR scan login.
Validates credentials, tests live ₹1 balance, and connects to the Quant OS engine.
"""

import argparse
import os
import subprocess

ENV_FILE = os.path.expanduser("~/teamwork_projects/sovereign-quant-os/.env.dhan")

def open_dhan_web():
    """Launch Chrome directly to Dhan Web login page."""
    url = "https://web.dhan.co"
    print(f"🚀 Opening Google Chrome to: {url}...")
    try:
        subprocess.run(["open", "-a", "Google Chrome", url], check=True)
        print("✅ Chrome opened! Simply scan the QR code using your Dhan mobile app to log in.")
    except Exception as e:
        print(f"⚠️ Could not open Chrome via 'open': {e}")
        subprocess.run(["open", url])

def save_credentials(client_id: str, access_token: str):
    """Save Dhan credentials to secure local file."""
    content = f"DHAN_CLIENT_ID={client_id.strip()}\nDHAN_ACCESS_TOKEN={access_token.strip()}\n"
    os.makedirs(os.path.dirname(ENV_FILE), exist_ok=True)
    with open(ENV_FILE, "w") as f:
        f.write(content)
    print(f"✅ Credentials securely saved to {ENV_FILE}")

def load_credentials():
    """Load Dhan credentials from local file or env."""
    client_id = os.environ.get("DHAN_CLIENT_ID", "")
    access_token = os.environ.get("DHAN_ACCESS_TOKEN", "")
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, "r") as f:
            for line in f:
                if line.startswith("DHAN_CLIENT_ID="):
                    client_id = line.strip().split("=", 1)[1]
                elif line.startswith("DHAN_ACCESS_TOKEN="):
                    access_token = line.strip().split("=", 1)[1]
    return client_id, access_token

def verify_dhan_connection():
    """Ping DhanHQ API to verify live balance and connectivity."""
    client_id, access_token = load_credentials()
    if not client_id or not access_token:
        print("⚠️ DHAN_CLIENT_ID or DHAN_ACCESS_TOKEN missing.")
        print("Run with --save <client_id> <access_token> or provide them via .env.dhan.")
        return False

    try:
        from dhanhq import DhanContext, dhanhq
        dhan = dhanhq(DhanContext(client_id, access_token))
        limits = dhan.get_fund_limits()
        print("==================================================")
        print("⚡ DHANHQ LIVE ACCOUNT CONNECTION VERIFIED")
        print("==================================================")
        print(f"Client ID     : {client_id}")
        print(f"Funds Status  : {orjson.dumps(limits, option=orjson.OPT_INDENT_2).decode('utf-8')}")
        print("==================================================")
        return True
    except Exception as e:
        print(f"❌ Failed to connect to DhanHQ: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Dhan YOLO Automator")
    parser.add_argument("--open", action="store_true", help="Open Chrome to Dhan Web for QR login")
    parser.add_argument("--save", nargs=2, metavar=("CLIENT_ID", "ACCESS_TOKEN"), help="Save credentials")
    parser.add_argument("--verify", action="store_true", help="Verify live balance via DhanHQ API")
    args = parser.parse_args()

    if args.open:
        open_dhan_web()
    elif args.save:
        save_credentials(args.save[0], args.save[1])
        verify_dhan_connection()
    elif args.verify:
        verify_dhan_connection()
    else:
        print("⚡ Dhan YOLO Automator Status:")
        cid, tok = load_credentials()
        print(f"Configured Client ID: {'*****' + cid[-4:] if cid else 'NOT_CONFIGURED'}")
        print(f"Access Token Status : {'SET' if tok else 'NOT_CONFIGURED'}")
        print("\nCommands:")
        print("  python3 dhan_yolo_automator.py --open")
        print("  python3 dhan_yolo_automator.py --save <CLIENT_ID> <ACCESS_TOKEN>")
        print("  python3 dhan_yolo_automator.py --verify")

if __name__ == "__main__":
    main()
