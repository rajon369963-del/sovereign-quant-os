#!/usr/bin/env python3
"""
upload_200_repos_to_notebooklm.py
=================================
Automated deployer for the 200+ Quant GitHub Repositories into NotebookLM.
Uploads the 10 consolidated domain volumes into a dedicated notebook:
'200+ QUANT & ALGO TRADING GITHUB REPOS - SOVEREIGN CODE BRAIN'
"""

from pathlib import Path

SOURCE_DIR = Path("/Users/rajondas/teamwork_projects/sovereign-quant-os/notebooklm_200_quant_repos_sources")
VOLUMES = [
    "01_HFT_EVENT_DRIVEN.md",
    "02_OPTIONS_GREEKS_VOL.md",
    "03_INDIAN_DERIVATIVES_BROKERS.md",
    "04_VECTOR_BACKTEST_PORTFOLIO.md",
    "05_STAT_ARB_FIN_ML.md",
    "06_MICROSTRUCTURE_ORDERFLOW.md",
    "07_FINANCIAL_NLP_SENTIMENT.md",
    "08_MULTI_AGENT_QUANT_LLM.md",
    "09_INFRA_ENGINEERING.md",
    "10_CLONED_PHYSICAL_WHEELS.md"
]

NOTEBOOK_TITLE = "200+ QUANT & ALGO TRADING GITHUB REPOS - SOVEREIGN CODE BRAIN"

def print_summary():
    print("=" * 80)
    print(f"🚀 NOTEBOOKLM DEPLOYMENT READY: {NOTEBOOK_TITLE}")
    print("=" * 80)
    print(f"Source Directory: {SOURCE_DIR}")
    print(f"Total Volumes to Upload: {len(VOLUMES)}")
    total_bytes = 0
    for v in VOLUMES:
        p = SOURCE_DIR / v
        if p.exists():
            sz = p.stat().st_size
            total_bytes += sz
            print(f"  • {v:45s} : {sz:>8,d} bytes")
    print("-" * 80)
    print(f"Total Source Size: {total_bytes:,d} bytes (~{total_bytes/(1024*1024):.2f} MB)")
    print("=" * 80)

def main():
    print_summary()
    print("\n💡 Options for Uploading to NotebookLM:")
    print("1. Drag & drop the 10 markdown files from:")
    print(f"   file://{SOURCE_DIR}")
    print(f"   directly into a new notebook named '{NOTEBOOK_TITLE}'.")
    print("2. Use Google Chrome automation with your active session (lakhidas168@gmail.com).")
    print("3. Use `notebooklm source add` once session auth is active.")

if __name__ == "__main__":
    main()
