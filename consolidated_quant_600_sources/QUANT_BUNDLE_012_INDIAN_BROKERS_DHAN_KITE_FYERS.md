# ⚡ [QUANT-SOURCE-012] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_012_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: RRG-Sector-Rotation-India (`VAULT_IN-QUANT-114_AdroitAnandAI__RRG-Sector-Rotation-India`)
- **Full Name**: `IN-QUANT-114_AdroitAnandAI__RRG-Sector-Rotation-India`
- **Description**: Relative Rotation Graphs (RRG) for Indian stock markets (NSE, NIFTY) to track sector rotation and relative strength. Uses RS-Ratio and RS-Momentum to identify outperforming and weakening sectors, based on the Julius de Kempenaer RRG methodology, adapted for Indian equity markets
- **GitHub Stars**: 31
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# RRG Chart Visualization: Sector Rotation Analysis

This project implements a Relative Rotation Graph (RRG) computation and visualization platform for sector rotation strategies and swing trading in the Indian equity market. **The Julius de Kempenaer (JdK) Relative Rotation Graph methodology, widely used by professional traders in Western markets, is not freely available for the Indian market — this gap serves as the primary motivation behind this project.** The platform implements both the standard JdK RRG methodology and an enhanced EMA-based variant that provides earlier signals and smoother transitions for timely investment and swing-trading decisions.

---

## Why RRG Charts Matter

**Relative Rotation Graphs identifies which sectors/stocks are rotating into and out of favor** before the crowd recognizes the shift. Traditional analysis shows absolute performance, but RRG reveals **relative strength and momentum** - the two dimensions that drive sector rotation cycles.

### The Power of Two Dimensions

RRG charts plot securities in a 2D space:
- **X-axis (RS-Ratio)**: How strong is this security relative to the benchmark?
- **Y-axis (RS-Momentum)**: Is the relative strength accelerating or decelerating?

This dual-axis approach captures the **rotational dynamics** that drive market cycles. Sectors don't just move up or down - they **rotate** through predictable phases:**Improving → Leading → Weakening → Lagging → Improving**.

### Why This Matters for Swing Trading

1. **Early Entry Signals**: Identify sectors moving from "Improving" to "Leading" before they become obvious
2. **Exit Timing**: Recognize when "Leading" sectors transition to "Weakening" 
3. **Risk Management**: Avoid "Lagging" sectors with negative momentum
4. **Portfolio Rebalancing**: Systematically rotate capital from weakening to improving sectors

---

## Enhanced Formula Implementation

Our implementation uses **EMA-based ratio normalization**, a significant improvement over the standard JdK z-score methodology. This enhancement provides **2-3 periods faster signal detection** and **direct percentage interpretation** - critical advantages for swing trading.

### RS-Ratio Formula

**Enhanced Implementation:**

<!-- ![RS Ratio](imgs/rs_enhanced.png) -->

<p align="center">
  <img src="imgs/rs_enhanced.png" width="60%">
</p>

Formulas in Text:
```
RS = Stock_Close / Benchmark_Close

EMA_RS(t) = α × RS(t) + (1-α) × EMA_RS(t-1)
           where α = 2/(m+1), m = 14 (default)

RS_Ratio = 100 × (EMA_RS / Rolling_Mean(EMA_RS, m))
```

**Key Advantages:**
- **EMA weighting**: Recent data gets exponentially more weight → faster trend detection
- **Ratio normalization**: Direct interpretation (105 = 5% above recent average)
- **Reduced lag**: Responds 2-3 periods earlier than SMA-based methods

**Standard JdK (for comparison):**

<!-- ![RS Ratio](imgs/rs_standard.png) -->

<p align="center">
  <img src="imgs/rs_standard.png" width="60%">
</p>

Formulas in Text:
```
RS = Stock_Close / Benchmark_Close

JdK_RS(t) = α × RS(t) + (1-α) × JdK_RS(t-1)
           where α = 2/(m+1), m = 14 (default)

RS_Ratio = 100 + 10 × (JdK_RS - Rolling_Mean(JdK_RS, m)) / Rolling_StdDev(JdK_RS, m)
```

**Note**: Standard JdK uses EMA smoothing of RS followed by z-score normalization, providing a balance between responsiveness and statistical normalization.

### RS-Momentum Formula

**Enhanced Implementation:**

<!-- ![RS Momentum](imgs/mom_enhanced.png) -->

<p align="center">
  <img src="imgs/mom_enhanced.png" width="60%">
</p>

Formulas in Text:
```
ROC(t) = (RS_Ratio(t) - RS_Ratio(t-k)) / RS_Ratio(t-k)
        where k = 10 (default, short-term momentum)

EMA_ROC(t) = α × ROC(t) + (1-α) × EMA_ROC(t-1)
            where α = 2/(m+1), m = 14

RS_Momentum = 100 + 100 × EMA_ROC
```

**Key Advantages:**
- **Direct percentage**: Momentum of 102 = 2% positive momentum (no conversion needed)
- **Short lookback (k=10)**: Captures recent momentum relevant for current swing trade
- **Faster signals**: EMA smoothing detects acceleration/deceleration earlier

**Standard JdK (for comparison):**

<!-- ![RS Momentum](imgs/mom_standard.png) -->

<p align="center">
  <img src="imgs/mom_standard.png" width="70%">
</p>

Formulas in Text:
```
ROC(t) = (JdK_RS(t) - JdK_RS(t-k)) / JdK_RS(t-k)
        where k = 10 (default, ROC lookback period)

JdK_ROC(t) = α × ROC(t) + (1-α) × JdK_ROC(t-1)
            where α = 2/(m+1), m = 14

RS_Momentum = 100 + 10 × (JdK_ROC - Rolling_Mean(JdK_ROC, m)) / Rolling_StdDev(JdK_ROC, m)
```

**Note**: Standard JdK calculates momentum from the smoothed RS (JdK_RS) rather than RS_Ratio, then applies z-score normalization for statistical bounds.

### Why These Enhancements Matter

| Feature | Enhanced | Standard JdK | Trading Impact |
|---------|----------|--------------|----------------|
| **Signal Speed** | 2-3 periods faster | Delayed | Earlier entry/exit |
| **Interpretation** | Direct percentage | Statistical units | Faster decisions |
| **Momentum Period** | 10 periods (relevant) | 52 weeks (outdated) | Current market focus |
| **Volatility Sensitivity** | Stable ratio-based | Z-score volatility-dependent | Fewer false signals |

---

## Installation & Setup

### Prerequisites

- Python 3.8+
- AngelOne SmartAPI account with API credentials
- Internet connection for real-time data

### Step-by-Step Installation

```bash
# 1. Clone or navigate to project directory
cd RRG-Chart-Visualization

# 2. Create virtual environment (recommended)
python -m venv venv

# 3. Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file for API credentials (optional, for security)
# Copy .env.example to .env and add your credentials
```

### Configuration

**Option 1: Environment Variables (Recommended)**
Create a `.env` file in the project root:
```env
ANGELONE_API_KEY=your_api_key
ANGELONE_CLIENT_ID=your_client_id
ANGELONE_PASSWORD=your_password
ANGELONE_TOTP_SECRET=your_totp_secret
```

**Option 2: Streamlit UI**
Enter credentials directly in the application sidebar (credentials are stored in session state only).

---

## Usage Guide

### Starting the Application

```bash
streamlit run app.py
```

The application opens at `http://localhost:8501`

### Step-by-Step Workflow

#### 1. **Initial Setup**
   - Enter AngelOne API credentials (if not using .env)
   - Select **Benchmark**: NIFTY 50 (default) or NIFTY Bank
   - Choose **Timeframe**: Weekly (recommended) or Daily

#### 2. **Select Securities**
   - **Index Tab**: Analyze sectoral indices (NIFTY IT, NIFTY Bank, etc.)
   - **Stock Tab**: Analyze individual stocks or entire sectors
     - **Individual Selection**: Search and select specific stocks
     - **Sector Selection**: Use "Select Sector" dropdown to add all major stocks from a sector (e.g., IT, Banking, Finance)
     - **Sub-Sector Selection**: Select sub-sectors like "Private Banks" or "PSU Banks" to analyze specific segments
   - **ETF Tab**: Analyze ETFs (NIFTYBEES, BANKBEES, etc.)
   - Use search to find securities or select from dropdown

#### 3. **Configure Parameters**
   - **Computation Method**: Choose between "Enhanced" (default) or "Standard JDK"
     - **Enhanced**: EMA-based ratio normalization (faster signals, intuitive interpretation)
     - **Standard JDK**: JdK methodology with EMA smoothing and z-score normalization
   - **EMA Window Period (m)**: 
     - Enhanced: Default 14 (fixed for all timeframes)
     - Standard JDK: Default 14 (Weekly), 20 (Daily), 6 (Monthly)
   - **ROC Shift Period (k)**: 
     - Enhanced: Default 10 (Weekly), 20 (Daily), 3 (Monthly)
     - Standard JDK: Default 10 (Weekly), 20 (Daily), 3 (Monthly)
   - **Tail Count**: Default 8 (Enhanced) or 4 (Standard JDK) - historical trail length

#### 4. **Generate Chart**
   - Chart auto-generates when securities are selected
   - Use **Time Period Slider** to view historical rotations
   - Enable **Animation** to see rotational movement over time

#### 5. **Interpret Results**
   - Identify quadrant positions (see interpretation guide below)
   - Analyze tail trajectories (direction indicates trend)
   - Use animation to observe rotation cycles

---

## Interpreting RRG Charts

### Quadrant Analysis

| Quadrant | Condition | Action | Interpretation |
|----------|-----------|--------|----------------|
| 🟢 **Leading** (Top-Right) | RS > 100, Momentum > 100 | Hold/Add | Strong outperformance with accelerating momentum |
| 🟡 **Weakening** (Bottom-Right) | RS > 100, Momentum ≤ 100 | Take Profits | Outperforming but momentum fading - early exit signal |
| 🔴 **Lagging** (Bottom-Left) | RS ≤ 100, Momentum ≤ 100 | Avoid/Exit | Weak performance with negative momentum |
| 🔵 **Improving** (Top-Left) | RS ≤ 100, Momentum > 100 | Early Entry | Weak but recovering - best risk/reward opportunity |

**Rotation Cycle**: Improving → Leading → Weakening → Lagging → Improving

### Key Visual Elements

- **Tail Direction**: Clockwise = normal rotation; Counter-clockwise = reversal; Straight = persistent trend
- **Animation**: Observe rotation speed, quadrant duration, and cyclical patterns
- **Position**: Distance from center (100, 100) indicates strength of relative performance

---

## Advanced Swing Trading Strategies

### Strategy 1: Momentum Rotation Play
**Entry**: Improving quadrant (RS: 95-100, Momentum: 101-105, upward tail)  
**Exit**: Weakening signal (Momentum < 100)  
**Hold**: 6-12 weeks | **R:R**: 1:2 to 1:3

### Strategy 2: Defensive Exit
**Signal**: Leading → Weakening transition (Momentum drops below 101)  
**Action**: Exit 30% on first signal, 40% more if Momentum < 99, full exit on Lagging  
**Benefit**: Protects gains, frees capital for new opportunities

### Strategy 3: Contrarian Entry
**Entry**: Lagging → Improving transition (Momentum crosses 100, RS: 95-100)  
**Scaling**: 25% initial, 50% when RS crosses 100, 25% on Leading entry  
**Stop**: Momentum drops below 100 | **Target**: 15-25% return

### Strategy 4: Multi-Sector Portfolio
**Allocation**: 40% Leading, 30% Improving, 20% Weakening (reducing), 10% Cash  
**Rebalance**: Weekly rotation from Weakening → Improving, maintain 2-3 Leading sectors  
**Target**: 12-18% annual returns with lower drawdowns

### Strategy 5: Cyclical Timing
**Cycle**: Improving (M1-2) → Leading (M3-6) → Weakening (M7-9) → Lagging (M10-12)  
**Execution**: Pre-position before Improving phase, scale in/out with rotation  
**Requirement**: 2+ years historical data to identify sector-specific cycles

---

## Technical Specifications

### Data Requirements
- **Minimum**: 200+ periods for reliable calculations
- **Recommended**: 300+ periods for weekly charts
- **Real-time**: Fetches live data from AngelOne SmartAPI

### Performance Characteristics
- **Signal Latency**: 2-3 periods faster than standard JdK
- **Calculation Speed**: < 2 seconds for 20 securities
- **Update Frequency**: Real-time on data refresh

### Supported Markets
- **Primary**: NSE (National Stock Exchange, India)
- **Indices**: NIFTY 50, NIFTY Bank, Sectoral Indices
- **Stocks**: All NSE-listed equities
- **ETFs**: NIFTYBEES, BANKBEES, GOLDBEES, etc.

---

## Project Structure

```
RRG-Chart-Visualization/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .env                           # API credentials (create from .env.example)
├── README.md                      # This file
├── RRG_IMPLEMENTATION_COMPARISON.md  # Detailed formula comparison
│
└── src/
    ├── rrg_calculator.py          # Enhanced RRG calculation engine
    ├── sectors.py                 # Sector and stock definitions
    ├── token_fetcher.py           # Symbol-to-token mapping
    ├── scrip_master_search.py     # Security search functionality
    │
    └── loaders/
        └── AngelOneLoader.py      # Real-time data fetcher
```

---

## Key Features

- ✅ **Dual Computation Methods**: Enhanced (EMA-based) and Standard JDK (JdK methodology)
- ✅ **Enhanced EMA-based formulas** for faster signal detection
- ✅ **Real-time data** from AngelOne SmartAPI
- ✅ **Interactive charts** with Plotly (zoom, pan, hover)
- ✅ **Animation mode** to visualize rotation cycles
- ✅ **Multi-timeframe** analysis (daily, weekly, monthly)
- ✅ **Customizable parameters** (EMA span, ROC period, tail count)
- ✅ **Index, Stock, and ETF** analysis
- ✅ **Sector-based selection**: Quickly add all major stocks from a sector or sub-sector
- ✅ **Time period slider** for historical analysis

---

## Limitations & Considerations

1. **API Dependency**: Requires active AngelOne SmartAPI connection
2. **Data Quality**: Calculations depend on clean, complete historical data
3. **Market Hours**: Real-time data available only during market hours
4. **Lookback Period**: Short-term momentum (k=10) may miss longer cycles
5. **Volatility**: Extreme market conditions may produce temporary anomalies

---

## Contributing & Extending

### Adding Custom Strategies

The modular architecture allows easy extension:

```python
# Example: Custom strategy function
def momentum_crossover_strategy(rrg_data):
    leading_sectors = [s for s in rrg_data 
                      if s.rs_ratio > 100 and s.momentum > 102]
    improving_sectors = [s for s in rrg_data 
                        if s.rs_ratio < 100 and s.momentum > 101]
    return {
        'buy': improving_sectors,
        'hold': leading_sectors,
        'sell': [s for s in rrg_data if s.momentum < 99]
    }
```

### Integrating with Trading Systems

- **API Integration**: Export RRG signals to trading platforms
- **Alert System**: Set up notifications for quadrant transitions
- **Backtesting**: Use historical RRG data to test strategies
- **Portfolio Optimization**: Combine RRG signals with risk models

---

## References & Further Reading

- **RRG Methodology**: Julius de Kempenaer's Relative Rotation Graphs
- **Sector Rotation Theory**: Market cycle analysis and sector rotation patterns
- **EMA vs SMA**: Exponential vs Simple Moving Averages in technical analysis
- **Momentum Investing**: Using relative strength for portfolio construction

---

## License

This project is for educational and personal use. Ensure compliance with AngelOne API terms of service.

---

## Acknowledgments

- Data integration with AngelOne SmartAPI
- Visualization framework inspired by https://github.com/An0n1mity/RRGPy

---

**Built for investors and swing traders who understand that markets rotate, not just move. Identify the rotation before it becomes obvious.**

### Core Implementation Code & Architecture
#### File: `src/loaders/__init__.py`
```python
# Loaders package
```

#### File: `.streamlit/config.toml`
```python
[global]
# Disable widget state duplication warning
# This prevents UI warning messages about session state values being set for widgets
disableWidgetStateDuplicationWarning = true
```

#### File: `kite_login.py`
```python
"""
Helper to generate a Zerodha Kite Connect access token.

Kite access tokens expire every day, so you need to run this once per day
(after market login) to refresh KITE_ACCESS_TOKEN in your .env file.

Prerequisites in .env (or environment):
    KITE_API_KEY=...
    KITE_API_SECRET=...

Usage:
    python kite_login.py

Steps it walks you through:
    1. Opens (prints) the Kite login URL.
    2. You log in; Kite redirects to your app's redirect URL with a
       `request_token=...` query parameter.
    3. Paste that request_token back here.
    4. The script prints the access_token and, if a .env file exists, offers
       to update KITE_ACCESS_TOKEN in it automatically.
"""
import os
import re
import sys
from pathlib import Path

from dotenv import load_dotenv
from kiteconnect import KiteConnect

load_dotenv()

ENV_PATH = Path(__file__).with_name(".env")


def update_env_access_token(token: str) -> bool:
    """Write/replace KITE_ACCESS_TOKEN in the local .env file. Returns True on success."""
    if not ENV_PATH.exists():
        return False
    text = ENV_PATH.read_text(encoding="utf-8")
    line = f"KITE_ACCESS_TOKEN={token}"
    if re.search(r"^KITE_ACCESS_TOKEN=.*$", text, flags=re.MULTILINE):
        text = re.sub(r"^KITE_ACCESS_TOKEN=.*$", line, text, flags=re.MULTILINE)
    else:
        if text and not text.endswith("\n"):
            text += "\n"
        text += line + "\n"
    ENV_PATH.write_text(text, encoding="utf-8")
    return True


def main():
    api_key = os.getenv("KITE_API_KEY", "").strip()
    api_secret = os.getenv("KITE_API_SECRET", "").strip()

    if not api_key or not api_secret:
        print("ERROR: Set KITE_API_KEY and KITE_API_SECRET in your .env file first.")
        sys.exit(1)

    kite = KiteConnect(api_key=api_key)

    print("\n1) Open this URL in your browser and log in:\n")
    print("   " + kite.login_url())
    print("\n2) After login you'll be redirected to your app's redirect URL, e.g.:")
    print("   https://your-redirect-url/?request_token=XXXXXX&action=login&status=success")
    print("\n3) Copy the value of request_token from that URL.\n")

    request_token = input("Paste request_token here: ").strip()
    if not request_token:
        print("ERROR: No request_token provided.")
        sys.exit(1)

    try:
        data = kite.generate_session(request_token, api_secret=api_secret)
    except Exception as e:
        print(f"ERROR: Failed to generate session: {e}")
        sys.exit(1)

    access_token = data["access_token"]
    print("\nSUCCESS! Your access token is:\n")
    print("   " + access_token + "\n")

    if update_env_access_token(access_token):
        print(f"Updated KITE_ACCESS_TOKEN in {ENV_PATH}")
    else:
        print("No .env file found to update. Add this line to your .env manually:")
        print(f"   KITE_ACCESS_TOKEN={access_token}")


if __name__ == "__main__":
    main()
```

#### File: `src/token_fetcher.py`
```python
"""
Utility to fetch stock tokens from AngelOne Scrip Master JSON
"""
import requests
import logging

logger = logging.getLogger(__name__)

SCRIP_MASTER_URL = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"

# Cache for scrip master data
_scrip_master_cache = None


def fetch_scrip_master():
    """Fetch and cache scrip master JSON"""
    global _scrip_master_cache
    if _scrip_master_cache is None:
        try:
            response = requests.get(SCRIP_MASTER_URL, timeout=10)
            response.raise_for_status()
            _scrip_master_cache = response.json()
            logger.info("Scrip master JSON fetched successfully")
        except Exception as e:
            logger.error(f"Failed to fetch scrip master: {e}")
            return None
    return _scrip_master_cache


# Hardcoded benchmark tokens (fallback if not found in scrip master)
# These match the exact symbols from OpenAPIScripMaster.json
BENCHMARK_TOKENS = {
    # Exact symbols from scrip master
    "Nifty 50": "99926000",
    "Nifty Bank": "99926009",
    "Nifty IT": "99926008",
    "Nifty Pharma": "99926023",
    "Nifty Auto": "99926029",
    "Nifty FMCG": "99926021",
    "Nifty Energy": "99926020",
    "Nifty Metal": "99926030",
    # Legacy formats for backward compatibility
    "NIFTY50-EQ": "99926000",
    "NIFTYBANK-EQ": "99926009",
    "NIFTYIT-EQ": "99926008",
    "NIFTYPHARMA-EQ": "99926023",
    "NIFTYAUTO-EQ": "99926029",
    "NIFTYFMCG-EQ": "99926021",
    "NIFTYENERGY-EQ": "99926020",
    "NIFTYMETAL-EQ": "99926030",
    # Also try without -EQ suffix
    "NIFTY50": "99926000",
    "NIFTYBANK": "99926009",
    "NIFTYIT": "99926008",
    "NIFTYPHARMA": "99926023",
    "NIFTYAUTO": "99926029",
    "NIFTYFMCG": "99926021",
    "NIFTYENERGY": "99926020",
    "NIFTYMETAL": "99926030",
}


def get_token_from_symbol(symbol, exchange="NSE"):
    """
    Get token for a given symbol from scrip master
    
    :param symbol: Stock symbol (e.g., "HDFCBANK-EQ")
    :param exchange: Exchange (NSE or BSE)
    :return: Token string or None
    """
    # First check hardcoded benchmark tokens
    if symbol in BENCHMARK_TOKENS:
        return BENCHMARK_TOKENS[symbol]
    
    scrip_data = fetch_scrip_master()
    if scrip_data is None:
        # If scrip master fetch fails, try benchmark tokens as fallback
        if symbol in BENCHMARK_TOKENS:
            return BENCHMARK_TOKENS[symbol]
        return None
    
    # Try exact match
    for item in scrip_data:
        if item.get("symbol") == symbol and item.get("exch_seg") == exchange:
            return str(item.get("token"))
    
    # If exact match not found, try without -EQ suffix
    if symbol.endswith("-EQ"):
        base_symbol = symbol[:-3]
        for item in scrip_data:
            if item.get("symbol") == base_symbol and item.get("exch_seg") == exchange:
                return str(item.get("token"))
        
        # Also try with "name" field for NSE (as per jsonReader.py)
        for item in scrip_data:
            if item.get("name") == base_symbol and item.get("exch_seg") == exchange:
                return str(item.get("token"))
    
    # Try fuzzy match on name field for benchmarks (case-insensitive)
    if "NIFTY" in symbol.upper() or "NIFTY" in symbol:
        # Try exact match first (case-insensitive)
        symbol_upper = symbol.upper()
        symbol_lower = symbol.lower()
        symbol_title = symbol.title()  # "Nifty Pharma" format
        
        for item in scrip_data:
            item_name = item.get("name", "")
            item_symbol = item.get("symbol", "")
            # Try multiple case variations
            if ((symbol_upper == item_name.upper() or symbol_upper == item_symbol.upper() or
                 symbol_lower == item_name.lower() or symbol_lower == item_symbol.lower() or
                 symbol_title == item_name or symbol_title == item_symbol or
                 symbol == item_name or symbol == item_symbol) and 
                item.get("exch_seg") == exchange):
                return str(item.get("token"))
        
        # If still not found, try substring match
        symbol_upper_clean = symbol_upper.replace("-EQ", "").replace(" ", "")
        for item in scrip_data:
            item_name = item.get("name", "").upper().replace(" ", "")
            item_symbol = item.get("symbol", "").upper().replace(" ", "")
            if (symbol_upper_clean in item_name or symbol_upper_clean in item_symbol or
                item_name in symbol_upper_clean or item_symbol in symbol_upper_clean) and item.get("exch_seg") == exchange:
                return str(item.get("token"))
    
    logger.warning(f"Token not found for {symbol} on {exchange}")
    return None
```

#### File: `src/sectors.py`
```python
"""
Sector definitions for Indian stock market
Stock symbols for different sectors
Tokens will be fetched automatically from scrip master JSON
"""
# Format: {sector_name: [symbol, ...]}

SECTORS = {
    "Banking": [
        "HDFCBANK-EQ",
        "ICICIBANK-EQ",
        "SBIN-EQ",
        "KOTAKBANK-EQ",
        "AXISBANK-EQ",
        "INDUSINDBK-EQ",
        "FEDERALBNK-EQ",
        "PNB-EQ",
        "BANKBARODA-EQ",
        "UNIONBANK-EQ",
    ],
    "IT": [
        "TCS-EQ",
        "INFY-EQ",
        "HCLTECH-EQ",
        "TECHM-EQ",
        "WIPRO-EQ",
        "LTIM-EQ",
        "MPHASIS-EQ",
        "PERSISTENT-EQ",
        "COFORGE-EQ",
        "ZENSARTECH-EQ",
    ],
    "Pharma": [
        "SUNPHARMA-EQ",
        "DRREDDY-EQ",
        "CIPLA-EQ",
        "LUPIN-EQ",
        "TORNTPHARM-EQ",
        "GLENMARK-EQ",
        "ZYDUSLIFE-EQ",
        "DIVISLAB-EQ",
        "AUROPHARMA-EQ",
        "BIOCON-EQ",
    ],
    "Auto": [
        "MARUTI-EQ",
        "M&M-EQ",
        "TATAMOTORS-EQ",
        "BAJAJ-AUTO-EQ",
        "HEROMOTOCO-EQ",
        "EICHERMOT-EQ",
        "ASHOKLEY-EQ",
        "TVSMOTOR-EQ",
        "BHARATFORG-EQ",
        "MRF-EQ",
    ],
    "FMCG": [
        "HINDUNILVR-EQ",
        "ITC-EQ",
        "NESTLEIND-EQ",
        "BRITANNIA-EQ",
        "DABUR-EQ",
        "MARICO-EQ",
        "GODREJCP-EQ",
        "COLPAL-EQ",
        "TATACONSUM-EQ",
        "EMAMILTD-EQ",
    ],
    "Energy": [
        "RELIANCE-EQ",
        "ONGC-EQ",
        "IOC-EQ",
        "BPCL-EQ",
        "HINDPETRO-EQ",
        "GAIL-EQ",
        "ADANIENT-EQ",
        "ADANIGREEN-EQ",
        "TATAPOWER-EQ",
        "NTPC-EQ",
    ],
    "Metals": [
        "TATASTEEL-EQ",
        "JSWSTEEL-EQ",
        "SAIL-EQ",
        "VEDL-EQ",
        "HINDALCO-EQ",
        "NMDC-EQ",
        "NATIONALUM-EQ",
        "HINDZINC-EQ",
        "JINDALSAW-EQ",
        "RATNAMANI-EQ",
    ],
    "Telecom": [
        "BHARTIARTL-EQ",
        "RELIANCE-EQ",
        "IDEA-EQ",
    ],
    "Cement": [
        "ULTRACEMCO-EQ",
        "SHREECEM-EQ",
        "ACC-EQ",
        "AMBUJACEM-EQ",
        "DALMIABHA-EQ",
        "RAMCOCEM-EQ",
        "JKLAKSHMI-EQ",
        "ORIENTCEM-EQ",
    ],
    "Real Estate": [
        "DLF-EQ",
        "GODREJPROP-EQ",
        "OBEROIRLTY-EQ",
        "PRESTIGE-EQ",
        "SOBHA-EQ",
        "BRIGADE-EQ",
        "MAHLIFE-EQ",
        "PHOENIXLTD-EQ",
    ],
    "Finance": [
        "HDFCBANK-EQ",
        "ICICIBANK-EQ",
        "SBIN-EQ",
        "KOTAKBANK-EQ",
        "AXISBANK-EQ",
        "HDFC-EQ",
        "ICICIPRULI-EQ",
        "BAJFINANCE-EQ",
        "SBILIFE-EQ",
        "HDFCLIFE-EQ",
    ],
}

# Sub-sectors for each major sector
SUB_SECTORS = {
    # Banking sub-sectors
    "Private Banks": [
        "HDFCBANK-EQ",
        "ICICIBANK-EQ",
        "KOTAKBANK-EQ",
        "AXISBANK-EQ",
        "INDUSINDBK-EQ",
        "FEDERALBNK-EQ",
        "YESBANK-EQ",
        "IDFCFIRSTB-EQ",
    ],
    "PSU Banks": [
        "SBIN-EQ",
        "PNB-EQ",
        "BANKBARODA-EQ",
        "UNIONBANK-EQ",
        "CANBK-EQ",
        "INDIANB-EQ",
        "CENTRALBK-EQ",
        "IOB-EQ",
    ],
    # IT sub-sectors
    "IT Services": [
        "TCS-EQ",
        "INFY-EQ",
        "HCLTECH-EQ",
        "TECHM-EQ",
        "WIPRO-EQ",
        "LTIM-EQ",
        "MPHASIS-EQ",
        "PERSISTENT-EQ",
    ],
    "IT Products": [
        "COFORGE-EQ",
        "ZENSARTECH-EQ",
        "MINDTREE-EQ",
        "LTI-EQ",
    ],
    # Pharma sub-sectors
    "Pharma - Large Cap": [
        "SUNPHARMA-EQ",
        "DRREDDY-EQ",
        "CIPLA-EQ",
        "LUPIN-EQ",
        "TORNTPHARM-EQ",
    ],
    "Pharma - Mid Cap": [
        "GLENMARK-EQ",
        "ZYDUSLIFE-EQ",
        "DIVISLAB-EQ",
        "AUROPHARMA-EQ",
        "BIOCON-EQ",
    ],
    # Auto sub-sectors
    "Passenger Vehicles": [
        "MARUTI-EQ",
        "M&M-EQ",
        "TATAMOTORS-EQ",
        "BAJAJ-AUTO-EQ",
    ],
    "Two Wheelers": [
        "HEROMOTOCO-EQ",
        "EICHERMOT-EQ",
        "TVSMOTOR-EQ",
        "BAJAJ-AUTO-EQ",
    ],
    "Auto Ancillaries": [
        "ASHOKLEY-EQ",
        "BHARATFORG-EQ",
        "MRF-EQ",
        "APOLLOTYRE-EQ",
    ],
    # FMCG sub-sectors
    "FMCG - Personal Care": [
        "HINDUNILVR-EQ",
        "DABUR-EQ",
        "MARICO-EQ",
        "GODREJCP-EQ",
        "COLPAL-EQ",
    ],
    "FMCG - Food & Beverages": [
        "ITC-EQ",
        "NESTLEIND-EQ",
        "BRITANNIA-EQ",
        "TATACONSUM-EQ",
        "EMAMILTD-EQ",
    ],
    # Energy sub-sectors
    "Oil & Gas - Refining": [
        "RELIANCE-EQ",
        "IOC-EQ",
        "BPCL-EQ",
        "HINDPETRO-EQ",
    ],
    "Oil & Gas - Exploration": [
        "ONGC-EQ",
        "GAIL-EQ",
        "OIL-EQ",
    ],
    "Power": [
        "TATAPOWER-EQ",
        "NTPC-EQ",
        "ADANIENT-EQ",
        "ADANIGREEN-EQ",
    ],
    # Metals sub-sectors
    "Steel": [
        "TATASTEEL-EQ",
        "JSWSTEEL-EQ",
        "SAIL-EQ",
        "JINDALSTEL-EQ",
    ],
    "Non-Ferrous Metals": [
        "VEDL-EQ",
        "HINDALCO-EQ",
        "HINDZINC-EQ",
        "NATIONALUM-EQ",
    ],
    "Mining": [
        "NMDC-EQ",
        "COALINDIA-EQ",
    ],
    # Finance sub-sectors
    "Finance - Private Banks": [
        "HDFCBANK-EQ",
        "ICICIBANK-EQ",
        "KOTAKBANK-EQ",
        "AXISBANK-EQ",
    ],
    "Finance - PSU Banks": [
        "SBIN-EQ",
        "PNB-EQ",
        "BANKBARODA-EQ",
        "UNIONBANK-EQ",
    ],
    "Finance - NBFCs": [
        "BAJFINANCE-EQ",
        "HDFC-EQ",
        "M&MFIN-EQ",
        "POWERGRID-EQ",
    ],
    "Finance - Insurance": [
        "SBILIFE-EQ",
        "HDFCLIFE-EQ",
        "ICICIPRULI-EQ",
        "LICI-EQ",
    ],
}

# Benchmark indices
# Format: {name: symbol}
# Tokens will be fetched automatically from scrip master JSON or use hardcoded fallback
# Note: Benchmarks may not have -EQ suffix in scrip master, so we try both formats
BENCHMARKS = {
    "NIFTY 50": "Nifty 50",  # Token: 99926000
    "NIFTY BANK": "Nifty Bank",  # Token: 99926009
    "NIFTY IT": "Nifty IT",  # Token: 99926008
    "NIFTY PHARMA": "Nifty Pharma",  # Token: 99926023
    "NIFTY AUTO": "Nifty Auto",  # Token: 99926029
    "NIFTY FMCG": "Nifty FMCG",  # Token: 99926021
    "NIFTY ENERGY": "Nifty Energy",  # Token: 99926020
    "NIFTY METAL": "Nifty Metal",  # Token: 99926030
}
```

#### File: `src/loaders/KiteLoader.py`
```python
"""
Zerodha Kite Connect Data Loader for RRG Charts

Mirrors the interface of AngelOneLoader so the rest of the app does not need to
know which broker is supplying the data:

    loader = KiteLoader(config, tf="weekly", period=200)
    df = loader.get(symbol, token)   # returns OHLC DataFrame (token is ignored)
    loader.close()

The AngelOne `token` argument is accepted for signature compatibility but is NOT
used -- Kite has its own `instrument_token` namespace, so this loader resolves
the symbol to a Kite instrument token internally using the Kite instrument dump.

Requires a Kite Connect app with the historical-data add-on and a valid
(daily) access token. See `kite_login.py` to generate one.
"""
import logging
import re
from datetime import datetime, timedelta
from typing import Optional

import pandas as pd

from .ohlc_utils import resample_ohlc

logger = logging.getLogger(__name__)


def _norm(text: str) -> str:
    """Normalise an index name for matching: uppercase, alphanumerics only."""
    return re.sub(r"[^A-Z0-9]", "", (text or "").upper())


# Maps an AngelOne-style index name (normalised) to the Kite index tradingsymbol
# (normalised). Only entries that genuinely differ between the two providers
# need to be listed here; everything else matches after normalisation.
INDEX_ALIASES = {
    _norm("Nifty Financial Services"): _norm("NIFTY FIN SERVICE"),
    _norm("Nifty Fin Service"): _norm("NIFTY FIN SERVICE"),
    _norm("Nifty Infrastructure"): _norm("NIFTY INFRA"),
    _norm("Nifty Midcap 50"): _norm("NIFTY MIDCAP 50"),
    _norm("Nifty Next 50"): _norm("NIFTY NEXT 50"),
}


class KiteLoader:
    """Load Daily/Weekly/Monthly OHLC data from Zerodha Kite Connect."""

    # Kite only exposes a "day" historical interval; weekly/monthly are resampled.
    KITE_INTERVAL = "day"
    # Kite caps a single "day" request at ~2000 candles.
    MAX_DAYS_PER_REQUEST = 2000

    def __init__(
        self,
        config: dict,
        tf: Optional[str] = "daily",
        end_date: Optional[datetime] = None,
        period: int = 160,
    ):
        self.closed = False
        self.tf = tf if tf else "daily"
        self.end_date = end_date if end_date else datetime.now()
        self.period = period

        self.api_key = config.get("KITE_API_KEY") or config.get("API_KEY")
        self.access_token = config.get("KITE_ACCESS_TOKEN") or config.get("ACCESS_TOKEN")
        self.exchange = config.get("EXCHANGE", "NSE")

        if not self.api_key or not self.access_token:
            raise ValueError(
                "Missing Kite credentials: KITE_API_KEY and KITE_ACCESS_TOKEN are required"
            )

        # Imported lazily so AngelOne-only users don't need kiteconnect installed.
        try:
            from kiteconnect import KiteConnect
        except ImportError as e:
            raise ImportError(
                "The 'kiteconnect' package is required to use the Kite data provider. "
                "Install it with: pip install kiteconnect"
            ) from e

        self.kite = KiteConnect(api_key=self.api_key)
        self.kite.set_access_token(self.access_token)

        # symbol/name -> Kite instrument_token
        self._eq_map = {}
        self._idx_map = {}
        self._token_cache = {}
        self._load_instruments()

    def _load_instruments(self):
        """Build equity and index lookup tables from the Kite instrument dump."""
        try:
            instruments = self.kite.instruments(self.exchange)
        except Exception as e:
            logger.error(f"Failed to fetch Kite instruments for {self.exchange}: {e}")
            raise

        for inst in instruments:
            seg = inst.get("segment", "")
            tsym = inst.get("tradingsymbol", "")
            name = inst.get("name", "")
            token = inst.get("instrument_token")
            itype = inst.get("instrument_type", "")

            if seg == "INDICES":
                self._idx_map[_norm(tsym)] = token
                if name:
                    self._idx_map[_norm(name)] = token
            elif itype == "EQ":
                # ETFs are also instrument_type "EQ" on Kite, which is what we want.
                self._eq_map[tsym.upper()] = token

        logger.info(
            f"Kite instruments loaded: {len(self._eq_map)} equities, "
            f"{len(self._idx_map)} index keys ({self.exchange})"
        )

    def _resolve_token(self, symbol: str) -> Optional[int]:
        """Resolve an AngelOne-style symbol to a Kite instrument_token."""
        if symbol in self._token_cache:
            return self._token_cache[symbol]

        token = None
        s = (symbol or "").strip()

        if s.upper().endswith("-EQ"):
            # Equity / ETF: "RELIANCE-EQ" -> Kite tradingsymbol "RELIANCE"
            base = s[:-3].upper()
            token = self._eq_map.get(base)
        else:
            # Treat as an index name.
            key = _norm(s)
            key = INDEX_ALIASES.get(key, key)
            token = self._idx_map.get(key)
            if token is None:
                # Fall back to a contains match (shortest candidate wins).
                candidates = [
                    (k, v) for k, v in self._idx_map.items()
                    if key and (key in k or k in key)
                ]
                if candidates:
                    candidates.sort(key=lambda kv: len(kv[0]))
                    token = candidates[0][1]

        if token is None:
            # Last resort: maybe it is an equity passed without the -EQ suffix.
            token = self._eq_map.get(s.upper())

        if token is None:
            logger.warning(f"Could not resolve Kite instrument token for '{symbol}'")
        else:
            self._token_cache[symbol] = token
        return token

    def get(self, symbol: str, token: str = None) -> Optional[pd.DataFrame]:
        """
        Returns OHLC data for `symbol` as a DataFrame.

        The `token` argument is the AngelOne token and is ignored; the Kite
        instrument token is resolved from `symbol` internally.
        """
        instrument_token = self._resolve_token(symbol)
        if instrument_token is None:
            return None

        try:
            if self.tf == "daily":
                days_back = self.period + 50
            elif self.tf == "weekly":
                days_back = (self.period + 10) * 7
            else:  # monthly
                days_back = (self.period + 10) * 30

            # Kite caps a single daily request, so clamp the lookback window.
            days_back = min(days_back, self.MAX_DAYS_PER_REQUEST)
            start_date = self.end_date - timedelta(days=days_back)

            candles = self.kite.historical_data(
                instrument_token=instrument_token,
                from_date=start_date,
                to_date=self.end_date,
                interval=self.KITE_INTERVAL,
            )

            if not candles:
                logger.warning(f"No data returned for {symbol}")
                return None

            df_data = []
            for c in candles:
                df_data.append({
                    'Date': pd.to_datetime(c['date']),
                    'Open': float(c['open']),
                    'High': float(c['high']),
                    'Low': float(c['low']),
                    'Close': float(c['close']),
                    'Volume': float(c.get('volume', 0) or 0),
                })

            df = pd.DataFrame(df_data)
            df.set_index('Date', inplace=True)
            # Kite returns tz-aware timestamps; drop tz to match AngelOne output.
            try:
                df.index = df.index.tz_localize(None)
            except (TypeError, AttributeError):
                pass
            df.sort_index(inplace=True)

            return resample_ohlc(df, self.tf, self.period, symbol)

        except Exception as e:
            logger.error(f"Error loading data for {symbol}: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return None

    def close(self):
        """No persistent session to tear down for Kite; kept for interface parity."""
        self.closed = True
```


==================================================


## [2/3] Repository: small-trading-indian-stock-market-survival-kit (`VAULT_IN-QUANT-117_sumeetkbhardwaj__small-trading-indian-stock-market-survival-kit`)
- **Full Name**: `IN-QUANT-117_sumeetkbhardwaj__small-trading-indian-stock-market-survival-kit`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# small-trading-indian-stock-market-survival-kit

A survival-first, evidence-based decision-support kit for Indian equity markets, usable with any LLM agent and **any Indian broker — or none at all**.

> **Disclaimer.** For research and educational purposes only. Decision-support, advisory-only — **not investment advice**, and the author is **not a SEBI-registered Investment Adviser (IA) or Research Analyst (RA)**. Provided with no warranty (see [LICENSE](LICENSE)); use entirely at your own risk. **Live order execution is out of scope for this repository** — everything here is read-only research and monitoring. You are solely responsible for your own decisions and regulatory compliance.

## Philosophy

The prime directive is **capital preservation first, profit second**. No-trade is the default and always acceptable — the burden of proof sits on the trade, not the refusal. This is grounded in SEBI's own retail-loss data (across FY22–24, ~93% of individual F&O traders net-lose after costs). An unconditional retail trade is negative-EV, so the kit says no until a stack of gates — regime, exclusion, technical, sizing, cost/tax, **exit/2R asymmetry**, and behavioral (overtrading) — is cleared.

Design axiom: **the LLM proposes, the deterministic gate disposes.** All consequential math (sizing, cost/tax, exit contract, 2R gate, freshness, frequency) lives in plain Python, not in model reasoning — and it **fails closed to NO-TRADE / STAND-DOWN** whenever the gate could not run or the data is stale. The model never asserts a number the code did not compute.

## The capability lattice — works on every surface, fails closed at each rung

The kit is **broker-agnostic** and **surface-agnostic**, degrading honestly (never to confident prose):

- **Data — a broker-agnostic `MarketData` port.** Baseline needs **no broker**: free public web (**screener.in** fundamentals + **Yahoo `.NS`/`.BO`** delayed quotes) + **manual-paste** holdings, every reading stamped `{value, source, as_of, delay_class}`. A **read-only broker MCP** (Upstox/Kotak read-only by construction preferred; any broker equal opt-in) is optional enrichment for live private state — and **every broker order/GTT write tool is structurally denied** by a PreToolUse hook (the kit never places, modifies, or cancels an order).
- **Gate — a self-identifying resolver.** A connected **Gate MCP** → the **`kit.py` CLI** (Claude Code / Cloud Routine / paid-tier chat) → a client-side **JS-paise gate Artifact** (plain chat, model out of the loop) → else **REFUSE** and default to NO-TRADE. Never free-LLM gate math.

## What it does

A **read-only advisory** pipeline that screens, shortlists, and turns each idea into a signal — with a machine-computed **exit contract** (stop · R-target · trailing rule) and a hard **2R asymmetry** requirement — and evaluates/monitors existing positions. Where the surface supports it, reports render as **beautiful, self-contained Artifacts** (theme-aware, provenance-labeled, disclaimer-footed). It never places an order; every output ends with the SEBI-safe disclaimer; the default answer is no-trade.

## Skills & commands

- `/small-trader:check TICKER` — full survival-gate stack on one name (TRADE / NO-TRADE + dominant reason + counterfactual cost).
- `/small-trader:screen` — screen a universe; return only the few that pass, with a beautiful shortlist Artifact.
- `/small-trader:research` — deep, cited, survival-first brief on a stock or theme (risks first).
- `/small-trader:portfolio-watch` — daily hold/trim/exit alerts on your holdings.
- `/small-trader:portfolio-eval` — deeper portfolio health: weight, P&L, concentration, per-name quality.
- `/small-trader:watchlist` — ageing setups (armed / triggered / extended / invalidated / aged-out).
- `/small-trader:premarket`, `/small-trader:eod`, `/small-trader:autopilot` — scheduled, unattended, **broker-free** Cloud-Routine reviews that notify you.

## How it works

- **Layer A — deterministic core** (`scripts/`): pure, unit-tested functions for cost/tax, sizing, portfolio heat, freshness, the signal gate, the **exit contract + 2R gate**, the **frequency governor**, the **MarketData port**, manual-paste, and portfolio/watchlist helpers. Every number the kit surfaces comes from here. Golden-fixture parity harness locks the output byte-for-byte (and is the reference the JS-paise Artifact port must reproduce).
- **Layer B — skills** (`skills/`, `commands/`): LLM-orchestrated, broker-agnostic, fail-closed pipelines that fetch data through the port, call Layer A via the resolver, and render the report (text or Artifact).
- **Structural safety**: a PreToolUse deny hook (`hooks/`) blocks every broker write tool; unattended routines carry no broker connector at all.

## Install & usage

Follow [SETUP.md](SETUP.md). Requirements: **Python 3.11+**; the deterministic core has **no third-party dependencies**; `pytest` for the test suite.

```
/small-trader:check RELIANCE
/small-trader:portfolio-eval
```

## Why the thresholds are trustworthy

Every threshold traces to a cited primary source (official exchange, CBDT, and broker schedules; published SEBI research), never an assumption. The design was hardened through refute-first verification and an adversarial multi-reviewer review.

## Scope & compliance

**Advisory-only.** Order execution is out of scope for this repository. If you build an execution layer on top, that is your own responsibility, including any SEBI algo-provider empanelment and static-IP/approval-gating that applies. Not a SEBI IA/RA; nothing output is personalised investment advice.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

[MIT](LICENSE)

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python
# (empty)
```

#### File: `scripts/__init__.py`
```python
# (empty)
```

#### File: `pyproject.toml`
```python
[project]
name = "small-trading-indian-stock-market-survival-kit"
version = "0.1.0"
requires-python = ">=3.11"

[tool.pytest.ini_options]
pythonpath = ["."]
testpaths = ["tests"]
```

#### File: `hooks/hooks.json`
```python
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__.*|.*(?:order|gtt|position).*",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"${CLAUDE_PLUGIN_ROOT}/hooks/deny_write_tools.py\""
          }
        ]
      }
    ]
  }
}
```

#### File: `config/watchlist.example.json`
```python
{
  "_comment": "Copy this to config/watchlist.json and edit. These are the symbols the autopilot skill scans each run. Keep to liquid Nifty-500 names; the exclusion + liquidity gates will drop anything unsafe, and most names will be rejected on any given day (that is the design).",
  "universe": [
    "RELIANCE",
    "HDFCBANK",
    "INFY",
    "TCS",
    "ICICIBANK"
  ]
}
```

#### File: `tests/fixtures/gate_parity_cases.json`
```python
[
  {"price": "1000", "qty": 100, "segment": "delivery", "brokerage": "0", "dp": "15.34"},
  {"price": "100", "qty": 300, "segment": "delivery", "brokerage": "0", "dp": "15.34"},
  {"price": "500", "qty": 50, "segment": "intraday", "brokerage": "20", "dp": "0"},
  {"price": "250.5", "qty": 40, "segment": "delivery", "brokerage": "0", "dp": "13.5"},
  {"price": "37.85", "qty": 260, "segment": "delivery", "brokerage": "0", "dp": "15.34"}
]
```


==================================================


## [3/3] Repository: Pairs-Trading-Indian-IT-Stocks (`VAULT_IN-QUANT-118_anirudhjayaraman__Pairs-Trading-Indian-IT-Stocks`)
- **Full Name**: `IN-QUANT-118_anirudhjayaraman__Pairs-Trading-Indian-IT-Stocks`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Pairs-Trading-Indian-IT-Stocks
Term Paper on Pairs Trading using Cointegration as a market neutral strategy to make almost riskless profits.


==================================================
