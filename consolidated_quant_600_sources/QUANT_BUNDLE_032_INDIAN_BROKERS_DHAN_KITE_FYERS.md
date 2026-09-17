# ⚡ [QUANT-SOURCE-032] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_032_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: dhanhq-trading-system (`PHASE4-QUANT-063`)
- **Full Name**: `PHASE4-QUANT-063_mitulpatel123__dhanhq-trading-system`
- **Description**: 
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# AI F&O Trading System

A comprehensive real-time trading system for Futures & Options (F&O) that integrates with DhanHQ API to fetch market data, calculate technical indicators, and provide trading insights.

## Features

### Real-time Data Collection
- **WebSocket Integration**: Binary packet parsing for real-time tick data
- **Market Depth**: 20-level order book data
- **Option Chain**: Complete option chain with Greeks calculation
- **Multi-timeframe Candles**: Automatic candle building (1m, 5m, 15m, 1h, 1d)

### Technical Analysis
- **Momentum Indicators**: RSI, MACD, Stochastic, MFI, CCI, Williams %R
- **Trend Indicators**: ADX, Supertrend, PSAR, Ichimoku Cloud
- **Volatility Indicators**: Bollinger Bands, ATR, Keltner Channels, Donchian Channels
- **Volume Indicators**: OBV, CMF, VWAP, Volume Profile
- **Option Greeks**: Delta, Gamma, Theta, Vega, Rho calculations
- **Implied Volatility**: IV calculation and skew analysis

### Data Processing
- **Tick Aggregation**: Efficient batch processing and storage
- **Market Analysis**: Breadth, sentiment, and sector performance
- **Option Analysis**: Max pain, support/resistance from OI
- **Pattern Recognition**: Price patterns and divergence detection

### System Monitoring
- **Health Checks**: Component status and diagnostics
- **Performance Metrics**: Latency, throughput, resource usage
- **Alert System**: Multi-level alerts with suppression rules
- **Real-time Dashboard**: Live monitoring interface

## Architecture

```
trading_system/
├── clients/              # API clients
│   ├── websocket/       # WebSocket client with binary parsing
│   └── rest/            # REST API with rate limiting
├── database/            # MongoDB models and operations
├── indicators/          # Technical indicators engine
├── data_processing/     # Real-time data processors
├── monitoring/          # Health checks and metrics
├── utils/              # Utilities and constants
└── scripts/            # Management scripts
```

## Prerequisites

- Python 3.11 or higher
- MongoDB 4.4 or higher
- DhanHQ API credentials
- 8GB RAM minimum (16GB recommended)
- SSD storage for database

## Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd trading_system
```

2. **Run setup script**
```bash
python scripts/setup.py
```

3. **Activate virtual environment**
```bash
# On Unix/MacOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

4. **Configure environment**
```bash
cp .env.template .env
# Edit .env with your credentials
```

5. **Verify installation**
```bash
python scripts/health_check.py
```

## Configuration

### Environment Variables

Create a `.env` file with the following:

```env
# DhanHQ API Credentials
DHAN_CLIENT_ID=your_client_id
DHAN_ACCESS_TOKEN=your_access_token

# MongoDB Configuration
MONGODB_URL=mongodb://localhost:27017/
MONGODB_DATABASE=trading_system

# System Configuration
LOG_LEVEL=INFO
LOG_FILE_PATH=logs/trading_system.log

# WebSocket Configuration
WEBSOCKET_HEARTBEAT_INTERVAL=30
WEBSOCKET_RECONNECT_ATTEMPTS=5
WEBSOCKET_RECONNECT_DELAY=5

# REST API Configuration
REST_API_TIMEOUT=30
REST_API_MAX_RETRIES=3
RATE_LIMIT_REQUESTS_PER_SECOND=10

# Monitoring Configuration
HEALTH_CHECK_INTERVAL=60
METRICS_COLLECTION_INTERVAL=30

# Default Instruments (comma-separated DhanHQ instrument IDs)
DEFAULT_INSTRUMENTS=13,14,15
```

### MongoDB Indexes

The system automatically creates the following indexes:
- Tick data: `symbol`, `timestamp` (compound)
- Market depth: `symbol`, `timestamp` (compound)
- Option chain: `underlying_symbol`, `expiry_date`, `timestamp`
- Indicators: `symbol`, `indicator_name`, `timeframe`, `timestamp`
- Candles: `symbol`, `timeframe`, `timestamp`

## Usage

### Starting the System

```bash
# Run the main application
python main.py

# Or use the run script
python scripts/run.py
```

### Command Line Interface

```bash
# Check system statistics
python scripts/cli.py stats

# View alerts
python scripts/cli.py alerts --hours 24

# Query tick data
python scripts/cli.py ticks --symbol NIFTY --minutes 5

# Query indicators
python scripts/cli.py indicators NIFTY --indicator RSI
```

### Monitoring

```bash
# Real-time monitoring dashboard
python scripts/monitor.py --refresh 5

# Health check
python scripts/health_check.py

# Market status
python scripts/market_status.py
```

### WebSocket Subscriptions

```bash
# Subscribe to instruments
python scripts/subscribe_instruments.py 12345 67890 --mode full --duration 60
```

## API Reference

### WebSocket Client

```python
from clients.websocket import DhanWebSocketClient
from utils.constants import SUBSCRIPTION_MODE_FULL

# Initialize client
client = DhanWebSocketClient()

# Connect
await client.connect()

# Subscribe to instruments
await client.subscribe([12345, 67890], SUBSCRIPTION_MODE_FULL)

# Get status
status = client.get_status()
```

### REST API Client

```python
from clients.rest import MarketFeedClient

# Initialize client
client = MarketFeedClient()

# Get LTP
ltp_data = await client.get_ltp("NSE", ["12345"])

# Get option chain
chain = await client.get_option_chain("NIFTY", "2024-01-25")

# Get market depth
depth = await client.get_market_depth("NSE", "12345")
```

### Technical Indicators

```python
from indicators import IndicatorCalculator

# Initialize calculator
calculator = IndicatorCalculator()

# Calculate for symbol
indicators = await calculator.calculate_for_symbol("NIFTY", "5m")

# Get specific indicator
rsi = await calculator.calculate_single_indicator("NIFTY", "5m", "RSI")
```

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test categories
python scripts/run_tests.py --unit        # Unit tests only
python scripts/run_tests.py --integration # Integration tests only
python scripts/run_tests.py --fast        # Skip slow tests

# Run tests in parallel
python scripts/run_tests.py -n 4
```

## Performance Optimization

1. **Database**: Ensure MongoDB has sufficient memory and proper indexes
2. **Batch Processing**: Tick data is batched before insertion
3. **Async Operations**: All I/O operations are asynchronous
4. **Connection Pooling**: Reuses database and HTTP connections
5. **Rate Limiting**: Prevents API throttling
6. **Caching**: Frequently accessed data is cached in memory

## Troubleshooting

### Common Issues

1. **WebSocket Disconnection**
   - Check internet connection
   - Verify API credentials
   - Check WebSocket URL in logs

2. **High Memory Usage**
   - Reduce batch sizes in settings
   - Limit subscription count
   - Increase aggregation intervals

3. **MongoDB Performance**
   - Ensure indexes are created
   - Check disk I/O performance
   - Monitor connection pool

### Debug Mode

Enable debug logging:
```bash
LOG_LEVEL=DEBUG python main.py
```

## Security

- API credentials are stored in environment variables
- MongoDB connection uses authentication (if configured)
- All external data is validated using Pydantic models
- Rate limiting prevents API abuse
- No hardcoded secrets in code

## Contributing

1. Fork the repository
2. Create a feature branch
3. Write tests for new features
4. Ensure all tests pass
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This software is for educational and research purposes only. Trading in financial markets involves substantial risk of loss. The developers are not responsible for any financial losses incurred through the use of this software.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review logs in the `logs/` directory
3. Create an issue with detailed error information

## Acknowledgments

- DhanHQ for providing the trading API
- Contributors and testers
- Open source libraries used in this project

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python
"""Test suite for the trading system."""
```

#### File: `clients/auth/__init__.py`
```python
"""Authentication module for DhanHQ API."""

from .dhan_auth import DhanAuth

__all__ = ["DhanAuth"]
```

#### File: `config/__init__.py`
```python
"""Configuration module for the trading system."""

from .settings import Settings, get_settings
from .logging_config import setup_logging

__all__ = ["Settings", "get_settings", "setup_logging"]
```

#### File: `scripts/run.py`
```python
#!/usr/bin/env python
"""Run the trading system."""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio
from main import main

if __name__ == "__main__":
    asyncio.run(main())
```

#### File: `monitoring/__init__.py`
```python
"""System monitoring and health checks."""

from .health_checker import HealthChecker
from .metrics_collector import MetricsCollector
from .alerts import AlertManager

__all__ = [
    "HealthChecker",
    "MetricsCollector",
    "AlertManager",
]
```

#### File: `clients/websocket/__init__.py`
```python
"""WebSocket client module for real-time data feed."""

from .dhan_websocket import DhanWebSocketClient
from .packet_parser import PacketParser
from .reconnect_manager import ReconnectManager

__all__ = [
    "DhanWebSocketClient",
    "PacketParser",
    "ReconnectManager",
]
```


==================================================


## [2/3] Repository: intraday-algo-bot (`PHASE4-QUANT-064`)
- **Full Name**: `PHASE4-QUANT-064_intraday-algo-bot__intraday-algo-bot`
- **Description**: Algo Trading Bot (RSI + MACD + EMA with Dhan)
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
## Hi there 👋

<!--
**intraday-algo-bot/intraday-algo-bot** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
-->

### Core Implementation Code & Architecture
#### File: `symbols.py`
```python
# List of symbols to monitor
stock_list = ['RELIANCE', 'TCS', 'INFY', 'HDFCBANK', 'ICICIBANK']
```

#### File: `indicators.py`
```python
# Dummy logic to simulate signals
def calculate_indicators(df, rsi_period=14, ema_period=50):
    # Add real indicator logic later
    return "BUY" if df['close'].iloc[-1] % 2 == 0 else "SELL"
```

#### File: `dhan_api.py`
```python
# Handles placing orders via Dhan API (mock or real)
def place_order(dhan, symbol, capital, signal, sl_price=None, target_price=None):
    try:
        ltp = dhan.get_ltp(symbol)
        quantity = int(capital / ltp)

        order = {
            "symbol": symbol,
            "side": signal,
            "qty": quantity,
            "entry_price": round(ltp, 2),
            "stop_loss": round(sl_price, 2) if sl_price else None,
            "target": round(target_price, 2) if target_price else None
        }

        print(f"✅ Order Placed: {order}")
        return order

    except Exception as e:
        print(f"❌ Order placement failed for {symbol}: {e}")
```

#### File: `telegram_alert.py`
```python
import requests

TELEGRAM_TOKEN = "your_telegram_bot_token"
CHAT_ID = "your_chat_id"

def send_telegram_alert(symbol, signal, df, sl=None, target=None):
    entry = df['close'].iloc[-1]
    message = f"""
🔔 *{signal} Signal*
📈 *{symbol}* at ₹{entry:.2f}
🎯 Target: ₹{target:.2f}
🛑 Stop Loss: ₹{sl:.2f}
🔗 [Chart](https://www.tradingview.com/symbols/NSE-{symbol})
"""
    try:
        requests.post(
            f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
        )
        print(f"📩 Telegram alert sent for {symbol}.")
    except Exception as e:
        print(f"❌ Telegram alert failed: {e}")
```

#### File: `dhan.py`
```python
class DhanClient:
    def __init__(self, client_id, access_token):
        self.client_id = client_id
        self.access_token = access_token

    def get_ohlc(self, symbol, interval):
        import pandas as pd
        from datetime import datetime, timedelta
        import random

        # Generate dummy OHLC data for 20 candles
        end = datetime.now()
        start = end - timedelta(minutes=15*20)
        data = {
            "timestamp": pd.date_range(start, periods=20, freq="15T"),
            "open": [random.uniform(1000, 2000) for _ in range(20)],
            "high": [random.uniform(1000, 2000) for _ in range(20)],
            "low": [random.uniform(1000, 2000) for _ in range(20)],
            "close": [random.uniform(1000, 2000) for _ in range(20)],
        }
        return pd.DataFrame(data)
```

#### File: `main.py`
```python
# Algo Trading Bot using RSI + MACD + EMA with Telegram Alerts and Dhan API + SL/TP
import time
import requests
from dhan import DhanClient
from indicators import calculate_indicators
from telegram_alert import send_telegram_alert
from symbols import stock_list
from dhan_api import place_order

# Dhan Credentials
DHAN_CLIENT_ID = "1000675006"
DHAN_ACCESS_TOKEN = "your_dhan_access_token_here"

dhan = DhanClient(DHAN_CLIENT_ID, DHAN_ACCESS_TOKEN)

# Strategy Configuration
TIMEFRAME = "15m"  # 15-minute candles
RSI_PERIOD = 14
EMA_PERIOD = 50
MAX_TRADES = 3
TRADE_CAPITAL = 10000

# Risk Management
SL_PCT = 0.005  # 0.5%
TARGET_PCT = 0.01  # 1%

def run_strategy():
    trade_count = 0
    for symbol in stock_list:
        try:
            df = dhan.get_ohlc(symbol, interval=TIMEFRAME)
            signal = calculate_indicators(df, rsi_period=RSI_PERIOD, ema_period=EMA_PERIOD)

            if signal in ["BUY", "SELL"]:
                entry_price = df['close'].iloc[-1]

                sl = entry_price * (1 - SL_PCT) if signal == "BUY" else entry_price * (1 + SL_PCT)
                target = entry_price * (1 + TARGET_PCT) if signal == "BUY" else entry_price * (1 - TARGET_PCT)

                send_telegram_alert(symbol, signal, df, sl, target)
                place_order(dhan, symbol, TRADE_CAPITAL, signal, sl, target)

                trade_count += 1

            if trade_count >= MAX_TRADES:
                break
        except Exception as e:
            print(f"Error with {symbol}: {e}")

while True:
    run_strategy()
    time.sleep(900)  # wait for 15 minutes
```


==================================================


## [3/3] Repository: dhan-trading-engine (`PHASE4-QUANT-065`)
- **Full Name**: `PHASE4-QUANT-065_NDZCorp__dhan-trading-engine`
- **Description**: Production-grade algorithmic trading engine for Dhan broker
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# dhan-trading-engine
Production-grade algorithmic trading engine for Dhan broker


==================================================
