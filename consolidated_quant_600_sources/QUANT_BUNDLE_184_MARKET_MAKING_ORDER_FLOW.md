# ⚡ [QUANT-SOURCE-184] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_184_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ofi-cross-impact-analysis (`WHEEL_ofi-cross-impact-analysis`)
- **Full Name**: `ofi-cross-impact-analysis`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Order Flow Imbalance (OFI) Cross-Impact Analysis

This project evaluates the cross-impact of Order Flow Imbalance (OFI) on short-term price changes across highly liquid Nasdaq stocks. It involves computing OFI metrics, analyzing cross-impact relationships, and generating visualizations for insights.

## Project Structure
- **data/**: Contains placeholder datasets representing the format of original data.
- **notebooks/**: Includes Jupyter Notebook for exploratory analysis and methodology.
- **scripts/**: Python scripts for data processing, analysis, and visualization.
- **results/**: Stores output files, figures, and analysis results.

## Data Description
Working with high-frequency data for 4 Nasdaq stocks:
- BKR (Baker Hughes)
- NVDA (NVIDIA)
- MARA (Marathon Digital)
- TSLA (Tesla)

## How to Run the Code
1. **Set up the environment**:
   - Install Python 3.8 or higher.
   - Clone the repository: 
     ```
     git clone https://github.com/onurratarr/ofi-cross-impact-analysis.git
     cd ofi-cross-impact-analysis
     ```
   - Install the dependencies:
     ```
     pip install -r requirements.txt
     ```

2. **Execute the scripts**:
   - Preprocess data and calculate OFI metrics:
     ```
     python scripts/calculate_ofi.py
     ```
   - Perform PCA and cross-impact analysis:
     ```
     python scripts/full_analysis.py
     ```
   - Generate visualizations:
     ```
     python scripts/visualization.py
     ```

3. **Review the results**:
   - Outputs, including OFI metrics, PCA results, and visualizations, will be saved in the `results/` directory.

Summary of the Findings
OFI Metrics:

Successfully computed for four stocks: BKR, NVDA, MARA, and TSLA.
PCA reduced multi-level metrics into components, capturing ~85% variance in the first two components.
Cross-Impact Relationships:

NVDA showed the strongest contemporaneous impact on other stocks.
Significant relationships observed across all analyzed stocks.
Lagged Impact Analysis:

Moderate predictive power found for lagged OFI on price changes, with 1-minute and 5-minute horizons showing autocorrelations.
Visualizations:

Generated heatmaps, time-series plots, and boxplots to illustrate findings.
## References
- Cont, R., & Kukanov, A. (2017). Cross-Impact of Order Flow in Equity Markets.
- Databento Documentation: [https://databento.com/docs](https://databento.com/docs)

### Core Implementation Code & Architecture
#### File: `scripts/visualization.py`
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def plot_ofi_heatmap(cross_impact_matrix, symbols, save_path=None):
    '''Create heatmap of cross-impact relationships'''
    plt.figure(figsize=(10, 8))
    sns.heatmap(cross_impact_matrix, 
                xticklabels=symbols,
                yticklabels=symbols,
                cmap='coolwarm',
                center=0)
    plt.title('Cross-Impact of OFI Between Stocks')
    if save_path:
        plt.savefig(save_path)
    plt.close()
```

#### File: `scripts/utils.py`
```python
import pandas as pd
import numpy as np
from pathlib import Path

def load_data(file_path, sample_size=None):
    '''Load and preprocess order book data'''
    df = pd.read_csv(file_path, nrows=sample_size)
    df['ts_event'] = pd.to_datetime(df['ts_event'])
    return df.sort_values('ts_event')

def calculate_ofi(df, level=5):
    '''Calculate OFI metrics for multiple levels'''
    ofi_levels = []
    for i in range(level):
        bid_size = df[f'bid_sz_{i:02d}']
        ask_size = df[f'ask_sz_{i:02d}']
        ofi = bid_size - ask_size
        ofi_levels.append(ofi)
    
    return pd.DataFrame({
        'ts_event': df['ts_event'],
        'symbol': df['symbol'],
        **{f'ofi_level_{i}': ofi_levels[i] for i in range(level)}
    })
```

#### File: `scripts/analysis.py`
```python
import pandas as pd
import numpy as np
from pathlib import Path
from sklearn.decomposition import PCA
from .utils import load_data, calculate_ofi

def process_stock_data(file_path, sample_size=None):
    '''Process single stock data and calculate OFI'''
    df = load_data(file_path, sample_size)
    return calculate_ofi(df)

def calculate_cross_impact(ofi_data, price_changes):
    '''Calculate cross-impact between stocks'''
    return np.corrcoef(ofi_data.T)

def main():
    DATA_DIR = Path(__file__).parent.parent / 'data'
    files = list(DATA_DIR.glob('xnas-itch-*.csv'))
    
    # Process each stock
    all_ofi = {}
    for file in files:
        stock_ofi = process_stock_data(file)
        symbol = stock_ofi['symbol'].iloc[0]
        all_ofi[symbol] = stock_ofi

if __name__ == "__main__":
    main()
```

#### File: `scripts/test_pipeline.py`
```python
import pandas as pd
import numpy as np
from pathlib import Path
from utils import load_data, calculate_ofi
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_pipeline():
    try:
        # Set paths
        DATA_DIR = Path(__file__).parent.parent / 'data'
        
        # Test with TSLA data first
        test_file = DATA_DIR / 'xnas-itch-tsla-20241219.mbp-10.csv'
        
        # Load first 1000 rows
        logger.info("Loading test data...")
        df = load_data(test_file, sample_size=1000)
        
        # Calculate OFI
        logger.info("Calculating OFI...")
        ofi_results = calculate_ofi(df)
        
        # Basic statistics
        logger.info("\nOFI Statistics:")
        print(ofi_results.describe())
        
        return True
        
    except Exception as e:
        logger.error(f"Error in test pipeline: {str(e)}")
        return False

if __name__ == "__main__":
    test_pipeline()
```

#### File: `scripts/calculate_ofi.py`
```python
import pandas as pd
import numpy as np
from pathlib import Path

def calculate_ofi(df, level=5):
    '''
    Calculate Order Flow Imbalance for given order book data
    Parameters:
    - df: DataFrame with order book data
    - level: Number of price levels to consider (default=5)
    '''
    ofi_levels = []
    
    for i in range(level):
        # Calculate OFI for each level
        bid_size = df[f'bid_sz_{i:02d}']
        ask_size = df[f'ask_sz_{i:02d}']
        
        # Basic OFI calculation: bid size - ask size
        ofi = bid_size - ask_size
        ofi_levels.append(ofi)
    
    return pd.DataFrame({
        'ts_event': df['ts_event'],
        'symbol': df['symbol'],
        **{f'ofi_level_{i}': ofi_levels[i] for i in range(level)}
    })

# Example usage
if __name__ == "__main__":
    DATA_DIR = Path(__file__).parent.parent / 'data'
    # Process first 1000 rows as a test
    df = pd.read_csv(DATA_DIR / 'xnas-itch-tsla-20241219.mbp-10.csv', nrows=1000)
    ofi_result = calculate_ofi(df)
    print(ofi_result.head())
```

#### File: `scripts/full_analysis.py`
```python
import pandas as pd
import numpy as np
from pathlib import Path
from utils import load_data, calculate_ofi
from visualization import plot_ofi_heatmap
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def run_full_analysis():
    try:
        # Set paths
        DATA_DIR = Path(__file__).parent.parent / 'data'
        RESULTS_DIR = Path(__file__).parent.parent / 'results'
        RESULTS_DIR.mkdir(exist_ok=True)
        
        # Process all files
        all_stocks_ofi = {}
        files = list(DATA_DIR.glob('xnas-itch-*.csv'))
        
        for file in files:
            logger.info(f"Processing {file.name}")
            df = load_data(file)
            ofi_results = calculate_ofi(df)
            symbol = ofi_results['symbol'].iloc[0]
            all_stocks_ofi[symbol] = ofi_results
            
            # Save individual stock results
            output_file = RESULTS_DIR / f'ofi_results_{symbol}.csv'
            ofi_results.to_csv(output_file, index=False)
            logger.info(f"Saved results for {symbol}")
            
        # Calculate cross-impacts
        logger.info("Calculating cross-impacts...")
        symbols = list(all_stocks_ofi.keys())
        cross_impact_matrix = np.zeros((len(symbols), len(symbols)))
        
        for i, sym1 in enumerate(symbols):
            for j, sym2 in enumerate(symbols):
                corr = all_stocks_ofi[sym1]['ofi_level_0'].corr(all_stocks_ofi[sym2]['ofi_level_0'])
                cross_impact_matrix[i, j] = corr
        
        # Create and save heatmap
        plot_ofi_heatmap(cross_impact_matrix, symbols, 
                        save_path=RESULTS_DIR / 'cross_impact_heatmap.png')
        
        # Save cross-impact matrix
        pd.DataFrame(cross_impact_matrix, 
                    index=symbols, 
                    columns=symbols).to_csv(RESULTS_DIR / 'cross_impact_matrix.csv')
        
        logger.info("Analysis completed successfully")
        return True
        
    except Exception as e:
        logger.error(f"Error in full analysis: {str(e)}")
        return False

if __name__ == "__main__":
    run_full_analysis()
```


==================================================


## [2/3] Repository: order-flow-imbalance-strategy (`WHEEL_order-flow-imbalance-strategy`)
- **Full Name**: `order-flow-imbalance-strategy`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Order Flow Imbalance (OFI) Trading System

This project is a full-stack quantitative research pipeline that investigates whether Order Flow Imbalance (OFI), enhanced with machine learning, contains statistically significant predictive power in liquid crypto markets.

The system is designed end-to-end: from raw market microstructure data ingestion, through feature engineering and regime modeling, to ML-based prediction and walk-forward backtesting.

---

## Core Idea

Order Flow Imbalance captures short-term pressure between buyers and sellers in the order book. While OFI is known to have predictive power at very short horizons, it is noisy and regime-dependent.

This project builds a context-aware ML system that improves OFI using:

- Multi-horizon signal fusion (1m, 5m, 15m)
- Time-decay modeling of microstructure signals
- Market regime detection (volatility-based)
- Feature-rich order book + trade flow representation

## Goals

- Determine whether ML-enhanced OFI has predictive power in crypto markets
- Build a fully reproducible microstructure research pipeline
- Evaluate robustness across regimes and time periods

## Status

Early-stage development (Phase 1: Data Ingestion + Pipeline Foundation)

## Development

Use the dev container for a consistent environment (see [CONTRIBUTING.md](CONTRIBUTING.md)), or install locally with `pip install -e ".[dev]"`. Run `./scripts/check.sh` before opening a PR.

### Core Implementation Code & Architecture
#### File: `src/order_flow_imbalance_strategy/__init__.py`
```python

```

#### File: `tests/test_health.py`
```python
def test_imports_cleanly() -> None:
    assert True
```

#### File: `.devcontainer/devcontainer.json`
```python
{
  "name": "Order Flow Imbalance",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "charliermarsh.ruff"
      ],
      "settings": {
        "editor.formatOnSave": true,
        "[python]": {
          "editor.defaultFormatter": "charliermarsh.ruff"
        },
        "ruff.nativeServer": true,
        "python.testing.pytestEnabled": true,
        "python.testing.unittestEnabled": false
      }
    }
  },
  "postCreateCommand": "bash .devcontainer/post-create.sh",
  "remoteUser": "vscode"
}
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "order-flow-imbalance-strategy"
version = "0.1.0"
description = "ML-enhanced Order Flow Imbalance research pipeline for crypto markets"
readme = "README.md"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.30",
    "tqdm>=4.66",
    "pandas",
    "polars>=1.0",
    "pyarrow>=14.0.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0",
    "ruff>=0.9",
    "requests-mock",
]


[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]

[tool.ruff]
target-version = "py311"
line-length = 100
src = ["src", "tests"]

[tool.ruff.format]
quote-style = "double"

[tool.ruff.lint]
select = ["E", "F", "I", "UP", "B"]
```

#### File: `tests/test_normalize_klines.py`
```python
from datetime import date

import polars as pl

from order_flow_imbalance_strategy.klines import (
    LOOKBACK_BARS,
    OUTPUT_COLUMNS,
    execute_normalization,
    load_day_with_context,
    process_klines,
)

# real Binance klines CSV header (only the columns the normalizer consumes)
KLINES_CSV_HEADER = "open_time,open,high,low,close,volume\n"

DAY = date(2024, 1, 1)
DAY_START_MS = 1704067200000  # 2024-01-01 00:00:00 UTC in ms
MINUTE_MS = 60_000


def _klines_rows(n, start_ms=DAY_START_MS, base=100.0):
    """Generate n valid 1m OHLCV rows (open_time in ms) as CSV text lines."""
    lines = []
    for i in range(n):
        ts = start_ms + i * MINUTE_MS
        o = base + i * 0.1
        lines.append(f"{ts},{o:.4f},{o + 1:.4f},{o - 1:.4f},{o + 0.5:.4f},10.0\n")
    return lines


def _write_klines_csv(path, n, start_ms=DAY_START_MS, base=100.0):
    path.write_text(KLINES_CSV_HEADER + "".join(_klines_rows(n, start_ms, base)))


def _sample_lazyframe(n, start_ms=DAY_START_MS, base=100.0):
    rows = [r.strip().split(",") for r in _klines_rows(n, start_ms, base)]
    return pl.DataFrame(
        {
            "open_time": [int(r[0]) for r in rows],
            "open": [float(r[1]) for r in rows],
            "high": [float(r[2]) for r in rows],
            "low": [float(r[3]) for r in rows],
            "close": [float(r[4]) for r in rows],
            "volume": [float(r[5]) for r in rows],
        }
    ).lazy()


def test_process_klines_transformations():
    res = process_klines(_sample_lazyframe(30), "BTCUSDT", thresholds=None, keep_date=DAY).collect()

    assert list(res.columns) == list(OUTPUT_COLUMNS)
    assert res.height == 30
    assert (res["asset"] == "BTCUSDT").all()
    # first bar has no prior close -> null log_return; later bars are populated
    assert res["log_return"][0] is None
    assert res["log_return"][1] is not None
    # rolling realized_vol is populated once the window (20) is filled
    assert res["realized_vol"][-1] is not None
    # no thresholds provided -> vol_regime stays null
    assert res["vol_regime"].null_count() == res.height


def test_process_klines_filters_invalid_ohlc():
    lf = _sample_lazyframe(5)
    # corrupt one row so high < low (must be filtered out)
    df = lf.collect()
    df[2, "high"] = 1.0
    df[2, "low"] = 99999.0
    res = process_klines(df.lazy(), "BTCUSDT", thresholds=None, keep_date=DAY).collect()
    assert res.height == 4


def test_vol_regime_labeling_with_thresholds():
    thresholds = {"BTCUSDT": {"p25": 0.0, "p75": 1e-9}}
    res = process_klines(_sample_lazyframe(30), "BTCUSDT", thresholds, keep_date=DAY).collect()
    labels = set(res["vol_regime"].drop_nulls().unique().to_list())
    assert labels <= {"low", "normal", "high"}


def test_load_day_with_context_prepends_prior_tail(tmp_path):
    raw_dir = tmp_path / "raw"
    kdir = raw_dir / "BTCUSDT" / "klines"
    kdir.mkdir(parents=True)

    prev = kdir / "BTCUSDT-1m-2023-12-31.csv"
    curr = kdir / "BTCUSDT-1m-2024-01-01.csv"
    _write_klines_csv(prev, 50, start_ms=DAY_START_MS - 50 * MINUTE_MS)
    _write_klines_csv(curr, 30, start_ms=DAY_START_MS)

    lf = load_day_with_context(curr, raw_dir, "BTCUSDT", DAY)
    # current day (30) + only the last LOOKBACK_BARS of the prior day
    assert lf.collect().height == 30 + LOOKBACK_BARS


def test_execute_normalization_writes_parquet(tmp_path):
    raw_dir = tmp_path / "raw"
    out_dir = tmp_path / "processed" / "BTCUSDT" / "klines"
    kdir = raw_dir / "BTCUSDT" / "klines"
    kdir.mkdir(parents=True)
    out_dir.mkdir(parents=True)

    raw_file = kdir / "BTCUSDT-1m-2024-01-01.csv"
    out_file = out_dir / "BTCUSDT-klines-2024-01-01.parquet"
    _write_klines_csv(raw_file, 150)

    task = {
        "symbol": "BTCUSDT",
        "date_str": "2024-01-01",
        "keep_date": DAY.isoformat(),
        "raw_path": str(raw_file),
        "output_path": str(out_file),
        "output_dir": str(out_dir),
        "raw_dir": str(raw_dir),
        "thresholds": None,
    }

    assert execute_normalization(task) is True
    assert out_file.exists()

    result = pl.read_parquet(out_file)
    assert result.height == 150
    assert list(result.columns) == list(OUTPUT_COLUMNS)


def test_execute_normalization_skip_low_rowcount(tmp_path):
    raw_dir = tmp_path / "raw"
    out_dir = tmp_path / "processed"
    kdir = raw_dir / "BTCUSDT" / "klines"
    kdir.mkdir(parents=True)
    out_dir.mkdir()

    raw_file = kdir / "BTCUSDT-1m-2024-01-01.csv"
    out_file = out_dir / "out.parquet"
    _write_klines_csv(raw_file, 5)

    task = {
        "symbol": "BTCUSDT",
        "date_str": "2024-01-01",
        "keep_date": DAY.isoformat(),
        "raw_path": str(raw_file),
        "output_path": str(out_file),
        "output_dir": str(out_dir),
        "raw_dir": str(raw_dir),
        "thresholds": None,
    }

    # a low-rowcount file is an intentional skip, not a failure
    assert execute_normalization(task) is True
    assert not out_file.exists()


def test_execute_normalization_reports_failure(tmp_path):
    """A malformed/unreadable input must return False (not silently 'succeed')."""
    raw_dir = tmp_path / "raw"
    out_dir = tmp_path / "processed"
    kdir = raw_dir / "BTCUSDT" / "klines"
    kdir.mkdir(parents=True)
    out_dir.mkdir()

    raw_file = kdir / "BTCUSDT-1m-2024-01-01.csv"
    out_file = out_dir / "out.parquet"
    raw_file.write_text("foo,bar,baz\n1,2,3\n")  # wrong schema -> should fail, not skip

    task = {
        "symbol": "BTCUSDT",
        "date_str": "2024-01-01",
        "keep_date": DAY.isoformat(),
        "raw_path": str(raw_file),
        "output_path": str(out_file),
        "output_dir": str(out_dir),
        "raw_dir": str(raw_dir),
        "thresholds": None,
    }

    assert execute_normalization(task) is False
    assert not out_file.exists()
```

#### File: `tests/test_normalize_bookticker_aggtrades.py`
```python
from datetime import datetime

import polars as pl
import pytest

from order_flow_imbalance_strategy.normalize_data import (
    execute_normalization,
    generate_tasks,
    process_agg_trades,
    process_book_ticker,
)

# real Binance bookTicker CSV header row
BOOK_TICKER_CSV_HEADER = (
    "update_id,best_bid_price,best_bid_qty,best_ask_price,"
    "best_ask_qty,transaction_time,event_time\n"
)


@pytest.fixture
def sample_book_ticker_lazyframe():
    """Generates a mock LazyFrame simulating raw bookTicker CSV input
    (using the real Binance header names)."""
    data = {
        "update_id": [100, 101, 102, 103],
        "best_bid_price": [100.0, 100.5, 0.0, 101.0],  # Row 3 has 0 price (should filter)
        "best_bid_qty": [10.0, 5.0, 5.0, 10.0],
        "best_ask_price": [101.0, 101.0, 102.0, 100.5],  # Row 4 has ask < bid (should filter)
        "best_ask_qty": [10.0, 5.0, 5.0, 10.0],
        "transaction_time": [1700000000000, 1700000001000, 1700000002000, 1700000003000],
        "event_time": [1700000000000, 1700000001000, 1700000002000, 1700000003000],
    }
    return pl.DataFrame(data).lazy()


@pytest.fixture
def sample_agg_trades_lazyframe():
    """Generates a mock LazyFrame simulating raw aggTrades CSV input
    (using the real Binance header names)."""
    data = {
        "agg_trade_id": [1, 2, 3, 2],
        "price": [100.0, 101.0, -5.0, 101.0],
        "quantity": [1.5, 2.0, 1.0, 2.0],
        "first_trade_id": [10, 12, 14, 12],
        "last_trade_id": [11, 13, 15, 13],
        "transact_time": [1700000000000, 1700000001000, 1700000002000, 1700000001000],
        "is_buyer_maker": [True, False, False, False],
    }
    return pl.DataFrame(data).lazy()


# tests for process book ticker
def test_process_book_ticker_transformations(sample_book_ticker_lazyframe):
    symbol = "BTCUSDT"
    res = process_book_ticker(sample_book_ticker_lazyframe, symbol).collect()

    # Verify column layout and count
    assert len(res.columns) == 9
    expected_cols = [
        "timestamp",
        "asset",
        "bid_price",
        "ask_price",
        "bid_qty",
        "ask_qty",
        "mid_price",
        "spread",
        "queue_imbalance",
    ]
    assert res.columns == expected_cols

    # Verify invalid rows (zero prices or negative spreads) were filtered out
    assert res.height == 2  # Only rows 1 and 2 should survive

    # Verify asset name assignment
    assert (res["asset"] == symbol).all()

    # Check calculated metrics for row 1 (bid=100.0, ask=101.0, bid_qty=10.0, ask_qty=10.0)
    assert res["mid_price"][0] == 100.5
    assert res["spread"][0] == 1.0
    assert res["queue_imbalance"][0] == 0.0  # (10 - 10) / (10 + 10) = 0.0


def test_process_book_ticker_queue_imbalance_zero_division():
    """Verify queue_imbalance handles 0/0 safely with fill_nan."""
    data = {
        "update_id": [1],
        "best_bid_price": [100.0],
        "best_bid_qty": [0.001],  # Small positive to pass filter
        "best_ask_price": [101.0],
        "best_ask_qty": [0.001],
        "transaction_time": [1700000000000],
        "event_time": [1700000000000],
    }
    lf = pl.DataFrame(data).lazy()
    res = process_book_ticker(lf, "BTCUSDT").collect()

    assert not res["queue_imbalance"].is_nan().any()


# tests for process agg_trades
def test_process_agg_trades_transformations(sample_agg_trades_lazyframe):
    symbol = "ETHUSDT"
    res = process_agg_trades(sample_agg_trades_lazyframe, symbol).collect()

    # Verify column count and layout
    assert len(res.columns) == 8
    expected_cols = [
        "timestamp",
        "asset",
        "price",
        "quantity",
        "side",
        "notional",
        "buy_qty",
        "sell_qty",
    ]
    assert res.columns == expected_cols

    # verify filters & deduplication
    assert res.height == 2

    # check side derivation logic
    assert res["side"].to_list() == ["sell", "buy"]
    assert res["sell_qty"][0] == 1.5
    assert res["buy_qty"][0] == 0.0
    assert res["buy_qty"][1] == 2.0

    # check calculated notional
    assert res["notional"][0] == 100.0 * 1.5


# tests for generation


def test_generate_tasks(tmp_path):
    raw_dir = tmp_path / "raw"
    processed_dir = tmp_path / "processed"

    symbol = "BTCUSDT"
    data_type = "bookTicker"
    date_str = "2024-01-01"

    file_dir = raw_dir / f"{symbol}/{data_type}"
    file_dir.mkdir(parents=True)
    raw_file = file_dir / f"{symbol}-{data_type}-{date_str}.csv"
    raw_file.write_text("header\n")

    start_date = datetime.strptime("2024-01-01", "%Y-%m-%d")
    end_date = datetime.strptime("2024-01-01", "%Y-%m-%d")

    tasks = generate_tasks(
        [symbol], start_date, end_date, [data_type], str(raw_dir), str(processed_dir)
    )

    assert len(tasks) == 1
    assert tasks[0]["symbol"] == symbol
    assert tasks[0]["date_str"] == date_str


def test_execute_normalization_skip_low_rowcount(tmp_path):
    """Verify that execute_normalization skips saving parquet if < 100 rows survive."""
    raw_dir = tmp_path / "raw"
    out_dir = tmp_path / "processed"
    raw_dir.mkdir()
    out_dir.mkdir()

    raw_file = raw_dir / "sample.csv"
    out_file = out_dir / "sample.parquet"

    # just write 5 rows, using the real Binance bookTicker header
    lines = [BOOK_TICKER_CSV_HEADER]
    for i in range(5):
        lines.append(
            f"{i},100.0,1.0,101.0,1.0,{1700000000000 + i * 1000},{1700000000000 + i * 1000}\n"
        )
    raw_file.write_text("".join(lines))

    task = {
        "data_type": "bookTicker",
        "symbol": "BTCUSDT",
        "date_str": "2024-01-01",
        "raw_path": str(raw_file),
        "output_path": str(out_file),
        "output_dir": str(out_dir),
    }

    # a low-rowcount file is an intentional skip, not a failure
    assert execute_normalization(task) is True

    # check no output file
    assert not out_file.exists()


def test_execute_normalization_writes_parquet(tmp_path):
    """Full success path: >=100 valid rows should pass assertions and write parquet."""
    raw_dir = tmp_path / "raw"
    out_dir = tmp_path / "processed"
    raw_dir.mkdir()
    out_dir.mkdir()

    raw_file = raw_dir / "sample.csv"
    out_file = out_dir / "sample.parquet"

    lines = [BOOK_TICKER_CSV_HEADER]
    for i in range(150):
        ts = 1700000000000 + i * 1000
        lines.append(f"{i},100.0,1.0,101.0,1.0,{ts},{ts}\n")
    raw_file.write_text("".join(lines))

    task = {
        "data_type": "bookTicker",
        "symbol": "BTCUSDT",
        "date_str": "2024-01-01",
        "raw_path": str(raw_file),
        "output_path": str(out_file),
        "output_dir": str(out_dir),
    }

    assert execute_normalization(task) is True
    assert out_file.exists()

    result = pl.read_parquet(out_file)
    assert result.height == 150
    assert result.columns == [
        "timestamp",
        "asset",
        "bid_price",
        "ask_price",
        "bid_qty",
        "ask_qty",
        "mid_price",
        "spread",
        "queue_imbalance",
    ]


def test_execute_normalization_reports_failure(tmp_path):
    """A malformed/unreadable input must return False (not silently 'succeed')."""
    raw_dir = tmp_path / "raw"
    out_dir = tmp_path / "processed"
    raw_dir.mkdir()
    out_dir.mkdir()

    raw_file = raw_dir / "sample.csv"
    out_file = out_dir / "sample.parquet"

    # wrong schema: headers the normalizer does not expect -> rename should fail
    raw_file.write_text("foo,bar,baz\n1,2,3\n")

    task = {
        "data_type": "bookTicker",
        "symbol": "BTCUSDT",
        "date_str": "2024-01-01",
        "raw_path": str(raw_file),
        "output_path": str(out_file),
        "output_dir": str(out_dir),
    }

    assert execute_normalization(task) is False
    assert not out_file.exists()
```


==================================================


## [3/3] Repository: orderflow-metrics (`WHEEL_orderflow-metrics`)
- **Full Name**: `orderflow-metrics`
- **Description**: Microstructure order-flow metrics — Order Flow Imbalance (OFI), depth and trade imbalance. Dependency-free TypeScript.
- **GitHub Stars**: 10
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# orderflow-metrics

[![CI](https://github.com/twowaymind/orderflow-metrics/actions/workflows/ci.yml/badge.svg)](https://github.com/twowaymind/orderflow-metrics/actions/workflows/ci.yml)
[![npm](https://img.shields.io/npm/v/orderflow-metrics.svg?logo=npm)](https://www.npmjs.com/package/orderflow-metrics)
[![PyPI](https://img.shields.io/pypi/v/orderflow-metrics.svg?logo=pypi&logoColor=white)](https://pypi.org/project/orderflow-metrics/)
[![Python](https://img.shields.io/pypi/pyversions/orderflow-metrics.svg?logo=python&logoColor=white)](https://pypi.org/project/orderflow-metrics/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Microstructure **order-flow metrics** in dependency-free TypeScript and Python:
Order Flow Imbalance (OFI), VPIN, information-driven bars, transaction-cost /
price-impact metrics, trade-sign classification, limit-order-book reconstruction
and execution scheduling. The npm package ships as compiled ESM with type
declarations (Node ≥ 18) and has zero runtime dependencies; the TypeScript
source is also vendorable directly (Node 22+ type-stripping, no build step).

## Metrics

- **Order flow & imbalance** — [Order Flow Imbalance](#order-flow-imbalance) · [Multi-level OFI](#multi-level-ofi-deep-book) · [Imbalance](#imbalance) · [VPIN](#vpin) · [Trade-sign classification](#trade-sign-classification) · [Order-flow entropy](#order-flow-entropy)
- **Bars & sampling** — [Information-driven bars](#information-driven-bars)
- **Fair value & spreads** — [Fair value](#fair-value) · [Spread estimators (OHLC)](#spread-estimators-from-ohlc)
- **Execution & impact** — [Execution cost & price impact](#execution-cost--price-impact) · [Market impact](#market-impact) · [Adverse selection (markout profiles)](#adverse-selection-markout-profiles) · [Implementation shortfall](#implementation-shortfall) · [Execution scheduling](#execution-scheduling)
- **Order book** — [Order book](#order-book)
- **Volatility & risk** — [Volatility](#volatility) · [Range-based volatility (OHLC)](#range-based-volatility-from-ohlc) · [Realized moments](#realized-moments) · [Jumps & bipower variation](#jumps--bipower-variation) · [Lee-Mykland jump test (timing)](#lee-mykland-jump-test-timing) · [Realized semivariance](#realized-semivariance) · [HAR-RV volatility forecasting](#har-rv-volatility-forecasting) · [Value-at-Risk & Expected Shortfall](#value-at-risk--expected-shortfall) · [Risk-adjusted performance](#risk-adjusted-performance)
- **Market efficiency** — [Market efficiency](#market-efficiency) · [Hurst exponent](#hurst-exponent) · [Mean reversion (half-life & z-score)](#mean-reversion-half-life--z-score)
- **Liquidity** — [Liquidity](#liquidity) · [Pástor-Stambaugh liquidity (return reversal)](#pástor-stambaugh-liquidity-return-reversal)
- **Streaming** — [Online / streaming estimators](#online--streaming-estimators)
- **Cross-asset** — [Realized covariance, correlation & beta](#realized-covariance-correlation--beta) · [Realized semicovariance](#realized-semicovariance) · [Downside & upside beta](#downside--upside-beta) · [Downside covariance & correlation matrices](#downside-covariance--correlation-matrices) · [Realized semibetas](#realized-semibetas) · [Hayashi-Yoshida covariance (non-synchronous)](#hayashi-yoshida-covariance-non-synchronous) · [Absorption ratio (systemic risk)](#absorption-ratio-systemic-risk)

Runnable quickstarts live in [`examples/`](examples/).

## Install

```bash
npm install orderflow-metrics
# or vendor the src/ directory directly — it's tiny and dependency-free
```

## Usage

```ts
import { ofi, depthImbalance, tradeImbalance } from "orderflow-metrics";

// Order Flow Imbalance across a stream of best-quote updates
const quotes = [
  { bidPrice: 100, bidSize: 5, askPrice: 101, askSize: 4 },
  { bidPrice: 100, bidSize: 8, askPrice: 101, askSize: 1 },
  { bidPrice: 100.5, bidSize: 2, askPrice: 101, askSize: 1 },
];
ofi(quotes); // 8  (net buy-side pressure)

depthImbalance(quotes[0]); // (5 - 4) / (5 + 4) ≈ 0.111

tradeImbalance([
  { price: 100, size: 2, side: "buy" },
  { price: 100, size: 1, side: "sell" },
]); // 0.333
```

## Examples

Runnable, dependency-free quickstarts that tour the library end-to-end on
deterministic synthetic data live in [`examples/`](examples/):

```bash
node --experimental-strip-types examples/quickstart.ts   # TypeScript
python examples/quickstart.py                            # Python
```

Both use the same seeded data and print the same numbers — a quick check that
the two ports agree.

## Order Flow Imbalance

`ofi` implements the level-1 OFI of Cont, Kukanov & Stoikov (2014). For two
consecutive best-quote observations the event contribution is:

```
e_n =  q_bid_n · 1{P_bid_n ≥ P_bid_{n-1}}  −  q_bid_{n-1} · 1{P_bid_n ≤ P_bid_{n-1}}
     − q_ask_n · 1{P_ask_n ≤ P_ask_{n-1}}  +  q_ask_{n-1} · 1{P_ask_n ≥ P_ask_{n-1}}
```

OFI over a window is the sum of `e_n`. Intuitively it counts size added to the
bid and removed from the ask (buy pressure) against the reverse. Empirically it
is a strong linear predictor of short-horizon price changes.

- `ofiContribution(prev, curr)` — one transition
- `ofiSeries(quotes)` — per-step contributions (for bucketing / regression)
- `ofi(quotes)` — cumulative

## Multi-level OFI (deep-book)

Top-of-book OFI flickers in fragmented books. `mlofi` applies the same
event-flow logic at each of the top `K` levels and returns the per-level OFI
vector (Cont, Cucuringu & Zhang, 2023), then collapses it with geometric
depth-decay weights:

```ts
import { multiLevelOFI, depthWeightedOFI, type BookSnapshot } from "orderflow-metrics";

const prev: BookSnapshot = {
  bids: [{ price: 100.0, size: 200 }, { price: 99.9, size: 150 }, { price: 99.8, size: 120 }],
  asks: [{ price: 100.1, size: 180 }, { price: 100.2, size: 160 }, { price: 100.3, size: 140 }],
};
const curr: BookSnapshot = {
  bids: [{ price: 100.0, size: 260 }, { price: 99.9, size: 150 }, { price: 99.8, size: 90 }],
  asks: [{ price: 100.1, size: 120 }, { price: 100.2, size: 160 }, { price: 100.3, size: 140 }],
};

multiLevelOFI(prev, curr, 3);        // [120, 0, -30] — OFI per level
depthWeightedOFI(prev, curr, 3, 0.5); // 64.29 — near touch weighted up
```

- `multiLevelOFI(prev, curr, levels)` — the OFI vector across the top `levels`
- `multiLevelOFISeries(snapshots, levels)` — per-step vectors for a sequence
- `depthWeightedOFI(prev, curr, levels, decay)` — geometric depth-decay scalar (`decay` in (0,1]; 1 = equal weights)

Levels beyond the depth present in either snapshot contribute 0. Sides are
best-first: bids by descending price, asks by ascending price.

## Imbalance

- `depthImbalance(quote)` — `(bidSize − askSize) / (bidSize + askSize)`, in `[-1, 1]`
- `tradeImbalance(trades)` — `(buyVol − sellVol) / (buyVol + sellVol)`, in `[-1, 1]`

## VPIN

`vpin` implements Volume-Synchronized Probability of Informed Trading (Easley,
López de Prado & O'Hara, 2012). Trades are grouped into equal-volume buckets;
each bucket is split into buy/sell volume by Bulk Volume Classification (BVC)
from the standardized price change, and VPIN is the average absolute imbalance
across a rolling window.

```ts
import { bucketByVolume, vpin } from "orderflow-metrics";

const buckets = bucketByVolume(trades, 1_000); // equal-volume buckets
vpin(buckets, { window: 50 }); // flow toxicity in [0, 1]
```

- `bucketByVolume(trades, bucketSize)` — split a trade stream into equal-volume buckets
- `bvcBuyFraction(priceChange, sigma)` — BVC buy fraction Φ(ΔP/σ)
- `vpin(buckets, { window, sigma })` — VPIN over the last `window` buckets
- `standardNormalCdf(z)` — Φ, the standard normal CDF (Abramowitz & Stegun 7.1.26)

## Execution cost & price impact

Transaction-cost analysis (TCA) building blocks (buys `+1`, sells `−1`):

```ts
import { effectiveSpread, realizedSpread, priceImpact, kyleLambda } from "orderflow-metrics";

effectiveSpread(101, 100, "buy");        // 2  — cost vs the midpoint
realizedSpread(101, 100.5, "buy");       // 1  — LP revenue after reversion
priceImpact(100, 100.5, "buy");          // 1  — permanent impact (effective − realized)

kyleLambda([                             // price impact per unit signed flow
  { signedVolume: 2, priceChange: 1 },
  { signedVolume: -2, priceChange: -1 },
]);                                      // 0.5
```

- `effectiveSpread` / `effectiveHalfSpread` — realized cost vs the quote mid
- `realizedSpread` — post-trade reversion component
- `priceImpact` — permanent impact
- `kyleLambda` — OLS impact slope of ΔP on signed volume
- `rollSpread` — Roll's (1984) spread from price-change autocovariance

### Execution quality (vs the quote)

Measure a fill against the quote it faced — the SEC Rule 605 / TCA view:

```ts
import { quotedSpread, priceImprovement, effectiveToQuotedRatio } from "orderflow-metrics";

quotedSpread(99.98, 100.02);                     // 0.04 — width of the market
priceImprovement(100.01, 99.98, 100.02, "buy");  // 0.01 — filled inside the ask
effectiveToQuotedRatio(0.02, 0.04);              // 0.5  — traded at half the quoted spread
```

- `quotedSpread` / `quotedHalfSpread` — width of the market
- `priceImprovement` — how far inside the quote a fill landed (signed by side)
- `effectiveToQuotedRatio` — effective ÷ quoted; <1 = price improvement, >1 = walked the book

## Fair value

```ts
import { weightedMid, relativeSpreadBps } from "orderflow-metrics";

weightedMid({ bidPrice: 100, bidSize: 9, askPrice: 101, askSize: 1 }); // ~100.9 — heavy bid pulls toward ask
relativeSpreadBps({ bidPrice: 99.99, bidSize: 1, askPrice: 100.01, askSize: 1 }); // 2 (bps)
```

- `weightedMid` — imbalance-weighted mid (a simple micro-price)
- `mid` — arithmetic mid
- `relativeSpreadBps` — quoted spread in basis points

## Trade-sign classification

Public prints rarely say who was the aggressor. Infer it so OFI / imbalance /
VPIN inputs can be signed (+1 buyer-initiated, −1 seller-initiated, 0 unknown):

```ts
import { tickRule, leeReady } from "orderflow-metrics";

tickRule([100, 101, 101, 100]);                        // [0, 1, 1, -1]
leeReady([{ price: 101, mid: 100 }, { price: 99, mid: 100 }]); // [1, -1]
```

- `tickRule` — sign from the change vs the previous price (zero ticks carry)
- `leeReady` — Lee-Ready (1991): quote rule, with the tick rule breaking ties

## Liquidity

```ts
import { amihudIlliquidity } from "orderflow-metrics";

amihudIlliquidity([
  { ret: 0.02, volume: 100 },
  { ret: -0.01, volume: 50 },
]); // 0.0002 — price move per unit of volume; higher = thinner
```

- `amihudIlliquidity` — Amihud (2002): average |return| / volume across periods

### Pástor-Stambaugh liquidity (return reversal)

Measure liquidity from the reversal that follows order flow — the classic
return-reversal regression of Pástor & Stambaugh (2003). Dependency-free OLS:

```ts
import { pastorStambaughGamma } from "orderflow-metrics";

// aligned daily series (one month per estimate): raw returns, excess returns, volume
pastorStambaughGamma(returns, excessReturns, volumes);
// { gamma, phi, intercept } — γ is the liquidity measure (more negative = less liquid)
```

- `pastorStambaughGamma` — fits `rᵉₜ₊₁ = θ + φ·rₜ + γ·sign(rᵉₜ)·vₜ` by OLS; `gamma` is the liquidity measure (stronger post-trade reversal ⇒ more negative ⇒ less liquid); `NaN` with fewer than four usable pairs

## Volatility

```ts
import { realizedVolatility, annualizedVolatility } from "orderflow-metrics";

realizedVolatility([0.03, 0.04]);          // 0.05  — √(Σ rᵢ²)
annualizedVolatility(minuteReturns, 252 * 390); // scaled to a year
```

- `realizedVariance` — Σ rᵢ²
- `realizedVolatility` — √ of the realized variance
- `annualizedVolatility` — √( mean(rᵢ²) · periodsPerYear )

## Market efficiency

```ts
import { varianceRatio, autocorrelation } from "orderflow-metrics";

varianceRatio(returns, 2);   // <1 mean-reverting · ~1 random walk · >1 trending
autocorrelation(returns, 1); // lag-1 return autocorrelation
```

- `varianceRatio` — Lo-MacKinlay variance ratio over overlapping q-period returns
- `autocorrelation` — lag-k autocorrelation of a return series

## Order book

Reconstruct a limit order book from incremental level updates and read the
usual top-of-book / depth signals:

```ts
import { OrderBook } from "orderflow-metrics";

const ob = new OrderBook();
ob.update("bid", 100, 5);
ob.update("ask", 101, 3);

ob.bestBid();      // { price: 100, size: 5 }
ob.mid();          // 100.5
ob.spread();       // 1
ob.imbalance(1);   // 0.25  — top-of-book bid/ask size imbalance
ob.update("bid", 100, 0); // size 0 removes the level
```

- `update(side, price, size)` · `bestBid` / `bestAsk` · `mid` · `spread`
- `depth(side, n)` — top n levels · `imbalance(n)` — depth imbalance in `[-1, 1]`

### Market-order simulation

Sweep the book with a market order and see the real fill — VWAP price, slippage
and any unfilled size (read-only, the book isn't touched):

```ts
import { simulateMarketOrder } from "orderflow-metrics";

const r = simulateMarketOrder(ob, "buy", 4);
r.avgPrice;      // volume-weighted fill price
r.slippageBps;   // cost vs mid, in basis points
r.remainingSize; // > 0 if the book was too thin
```

### Book-depth liquidity

Read liquidity off a book snapshot — near-touch depth, how steeply the book
thickens away from mid, and the round-trip cost of a given size. Take plain
`Level[]` arrays sorted best-first (bids high→low, asks low→high):

```ts
import { depthWithin, orderBookSlope, costOfRoundTrip } from "orderflow-metrics";

const bids = [{ price: 99.95, size: 6 }, { price: 99.9, size: 10 }];
const asks = [{ price: 100.0, size: 5 }, { price: 100.05, size: 8 }];

depthWithin(bids, asks, 10);     // { bidDepth, askDepth, total } within ±10 bps of mid
orderBookSlope(asks, 99.975);    // cumulative size per unit of relative price move
costOfRoundTrip(bids, asks, 15); // { roundTripBps, avgBuyPrice, avgSellPrice, filledSize }
```

- `depthWithin` — resting size within ±bps of mid, split by side
- `orderBookSlope` — (Σ size) / (relative distance to the outermost level)
- `costOfRoundTrip` — basis-point liquidity tax of buying then selling `size`

## Execution scheduling

Split a parent order into child slices:

```ts
import { twap, pov } from "orderflow-metrics";

twap(100, 4);                       // [25, 25, 25, 25] — even time slices
pov(30, [100, 100, 100], 0.1);      // [10, 10, 10] — 10% of each interval's volume
```

- `twap` — time-weighted: even slices that sum exactly to the parent size
- `pov` — percentage-of-volume: participate at a fixed fraction of each interval

## Information-driven bars

Sampling trades on a fixed time grid oversamples quiet periods and produces
non-IID returns. Sampling on **activity** instead — a bar every N ticks, N
units of volume, or N units of traded value — gives bars with much better
statistical properties (López de Prado, *Advances in Financial ML*, ch. 2).
Build them first, then run the other metrics on the resulting series.

```ts
import { tickBars, volumeBars, dollarBars } from "orderflow-metrics";

const trades = [
  { price: 100, size: 3, side: "buy" },
  { price: 101, size: 4, side: "buy" },
  { price: 100, size: 2, side: "sell" },
  { price: 102, size: 5, side: "sell" },
];

tickBars(trades, 2);      // one bar per 2 trades
volumeBars(trades, 5);    // new bar each time cumulative size ≥ 5
dollarBars(trades, 500);  // new bar each time cumulative price·size ≥ 500
```

Each `Bar` carries `open`/`high`/`low`/`close`, `volume`, `dollar` (traded
value), `vwap`, `ticks`, and signed `buyVolume` / `sellVolume` (plus `start` /
`end` timestamps when the feed provides them). The trade that crosses the
threshold is included whole (never split), and a trailing partial bar is
dropped. Dollar bars are usually preferred — they are the most robust of the
three to changes in price level.

- `tickBars(trades, threshold)` — a bar every `threshold` trades
- `volumeBars(trades, threshold)` — a bar every `threshold` units of volume
- `dollarBars(trades, threshold)` — a bar every `threshold` units of traded value

## Market impact

Pre-trade cost models and post-trade markouts:

```ts
import { squareRootImpact, almgrenChrissCost, markout } from "orderflow-metrics";

squareRootImpact(0.02, 1_000, 1_000_000);   // Y·σ·√(Q/V) — empirical impact
almgrenChrissCost(10_000, 30, 1e-6, 2e-7);  // { permanent, temporary, total }
markout("buy", 100, 100.5);                 // +0.5 — price moved with the trade
```

- `squareRootImpact` — the empirical square-root law of impact
- `linearPermanentImpact` / `linearTemporaryImpact` — Almgren-Chriss impact terms
- `almgrenChrissCost` — expected TWAP cost, split into permanent vs temporary
- `markout` / `averageMarkout` — realized post-trade adverse-selection drift

## Adverse selection (markout profiles)

Toxicity has a *shape*: an informed fill keeps drifting against you, a benign one
snaps back. The markout profile is the signed post-fill move across horizons — the
standard TCA adverse-selection lens:

```ts
import { markoutProfile, adverseSelectionScore } from "orderflow-metrics";

// taker buys at mid 100.00; mids at +1s / +5s / +30s
markoutProfile("buy", 100.0, [100.02, 100.05, 100.04]); // [0.02, 0.05, 0.04]

// the 1s move in half-spread units (spread 0.02 → half 0.01)
adverseSelectionScore("buy", 100.0, 100.02, 0.02);      // 2 — toxic beyond the spread
```

- `markoutProfile(side, midAtTrade, midsAfter)` — signed markout at each horizon
- `adverseSelectionScore(side, midAtTrade, midAfter, spread)` — markout in half-spread units (>1 = toxic beyond the quoted spread)
- `averageMarkoutProfile(observations)` — the aggregate markout curve across many fills

Sign is the taker's (buy → up is positive); flip it for the liquidity provider's
toxicity. Extends the single-horizon `markout`.

## Implementation shortfall

Execution-quality analytics against a decision / arrival benchmark:

```ts
import { implementationShortfall, arrivalSlippageBps } from "orderflow-metrics";

implementationShortfall("buy", 100, 100.5, 800, 1000, 101, 5);
// { execution: 400, opportunity: 200, fees: 5, total: 605 }

arrivalSlippageBps("buy", 100, 100.5);   // 50 bps paid up vs arrival
```

- `implementationShortfall` — Perold's execution + opportunity + fees decomposition
- `arrivalSlippageBps` — signed slippage of the fill vs the arrival price

## Spread estimators (from OHLC)

Recover the effective bid-ask spread when all you have is daily high, low, and
close — no tick data required:

```ts
import { corwinSchultz, abdiRanaldo } from "orderflow-metrics";

const bars = [
  { high: 10.2, low: 9.8, close: 10.18 },
  { high: 10.25, low: 9.85, close: 9.88 },
  { high: 10.3, low: 9.9, close: 10.27 },
];

corwinSchultz(bars);   // proportional spread from the two-day high-low range
abdiRanaldo(bars);     // proportional spread from close vs high-low mid-range
```

- `corwinSchultz` — Corwin & Schultz (2012) high-low estimator
- `abdiRanaldo` — Abdi & Ranaldo (2017) close/high/low estimator

Both return a proportional spread (a fraction of price); negative estimates are
floored at 0.

## Range-based volatility (from OHLC)

Estimate volatility from the open, high, low, and close — far more efficient than
close-to-close when you have candles:

```ts
import {
  parkinsonVolatility,
  garmanKlassVolatility,
  rogersSatchellVolatility,
  yangZhangVolatility,
} from "orderflow-metrics";

const candles = [
  { open: 100, high: 105, low: 99, close: 102 },
  { open: 102, high: 106, low: 101, close: 104 },
  { open: 104, high: 104, low: 98, close: 99 },
];

parkinsonVolatility(candles);       // high-low range
garmanKlassVolatility(candles);     // adds open & close
rogersSatchellVolatility(candles);  // drift-independent
yangZhangVolatility(candles);       // + overnight jumps (needs >= 3 bars)
```

- `parkinsonVolatility` — Parkinson (1980), high-low range
- `garmanKlassVolatility` — Garman & Klass (1980), OHLC
- `rogersSatchellVolatility` — Rogers & Satchell (1991), drift-independent
- `yangZhangVolatility` — Yang & Zhang (2000), drift- and jump-robust

Each returns the volatility (standard deviation) per bar; multiply the variance
by bars-per-year to annualize.

## Hurst exponent

Detect long-memory — trending vs mean-reverting — from a return series via
rescaled-range (R/S) analysis:

```ts
import { hurstExponent } from "orderflow-metrics";

hurstExponent(returns);
// ~0.5 random walk · >0.5 persistent/trending · <0.5 mean-reverting
// NaN if the series is too short (needs ~32+ points)
```

- `hurstExponent` — R/S Hurst estimate; a companion to `varianceRatio` and
  `autocorrelation` for gauging market efficiency

## Mean reversion (half-life & z-score)

Quantify *how fast* a spread or pair residual reverts and *how far* from home it
sits right now — the Ornstein–Uhlenbeck timescale a pairs / stat-arb strategy
trades on:

```ts
import { meanReversionSpeed, halfLife, zScore } from "orderflow-metrics";

const spread = [10.0, 10.6, 10.1, 9.7, 10.2, 9.8, 10.3, 9.9];

meanReversionSpeed(spread); // κ ≈ 1.393 per step (>0 reverting · <0 trending)
halfLife(spread);           // ≈ 0.498 steps to decay halfway (Infinity if κ ≤ 0)
zScore(spread);             // ≈ -0.642 — latest point sits below the mean
```

- `meanReversionSpeed` — OU reversion speed `κ`, the negated OLS slope of the
  change `Δyₜ` on the lagged level `yₜ₋₁`
- `halfLife` — `ln 2 / κ`, the number of steps a deviation takes to revert
  halfway; `Infinity` when the series does not mean-revert
- `zScore` — the latest observation as a standardized deviation from the sample
  mean (population σ), the raw entry/exit signal

Operates on a **level / spread** series (not returns), complementing the
`varianceRatio` and `hurstExponent` regime diagnostics above.

## Realized moments

Higher moments of the intraday return distribution (Amaya et al., 2015):

```ts
import { realizedSkewness, realizedKurtosis } from "orderflow-metrics";

realizedSkewness(returns);  // √N · Σr³ / RV^1.5  — intraday asymmetry
realizedKurtosis(returns);  // N · Σr⁴ / RV²      — intraday tail heaviness
```

- `realizedSkewness` — asymmetry of the intraday return distribution
- `realizedKurtosis` — tail heaviness of the intraday return distribution

Both return 0 for an empty or zero-variance series.

## Jumps & bipower variation

Split realized variance into its continuous (diffusive) part and its jump part
(Barndorff-Nielsen & Shephard, 2004). Bipower variation is jump-robust because
multiplying adjacent absolute returns damps a lone spike:

```ts
import { bipowerVariation, jumpVariation, relativeJumpVariation } from "orderflow-metrics";

bipowerVariation(returns);       // (π/2)·Σ|rᵢ₋₁||rᵢ| — continuous variance
jumpVariation(returns);          // max(RV − BV, 0)    — variance from jumps
relativeJumpVariation(returns);  // jump share of RV, in [0, 1]
```

- `bipowerVariation` — jump-robust estimate of continuous variance
- `jumpVariation` — the realized-variance contribution of discrete jumps
- `relativeJumpVariation` — that jump contribution as a fraction of RV

All three return 0 for fewer than two returns (and a jumpless series gives a jump
variation of 0).

### Lee-Mykland jump test (timing)

Bipower variation tells you *how much* jump there was; the Lee & Mykland (2008)
test tells you *which* returns are jumps and *when*. Each return is standardized by
a local, jump-robust volatility estimate, and the maximum statistic is compared to
a Gumbel critical value that controls the family-wide false-positive rate:

```ts
import { leeMyklandStatistics, leeMyklandCriticalValue, leeMyklandJumps } from "orderflow-metrics";

// log returns; window K defaults to √n, override to match your sampling frequency
leeMyklandStatistics(returns, { windowSize: 5 });        // L(i) series (NaN before the first window)
leeMyklandCriticalValue(20, 0.01);                       // ≈ 3.8691 — the jump threshold
leeMyklandJumps(returns, { windowSize: 5 });             // [{ index, statistic, direction }]
```

- `leeMyklandStatistics` — the standardized statistics `L(i) = rᵢ / σ̂(tᵢ)`; the first `K−1` entries (and any degenerate-window entry) are `NaN`
- `leeMyklandCriticalValue` — the extreme-value threshold `Sₙ·β* + Cₙ` for a given number of test points and significance level
- `leeMyklandJumps` — the returns whose `|L(i)|` exceeds the threshold, each with its index and direction (+1 up / −1 down)

Complements the aggregate bipower split above with per-return jump *timing*.

## Realized semivariance

Realized variance treats an up-move and a down-move of equal size as identical
risk. Realized semivariance splits it by the *sign* of each return, isolating
downside ("bad") from upside ("good") volatility — Barndorff-Nielsen,
Kinnebrock & Shephard (2010) and Patton & Shephard (2015):

```ts
import {
  realizedSemivariance,
  downsideVarianceRatio,
  signedJumpVariation,
} from "orderflow-metrics";

realizedSemivariance(returns); // { upside: Σr²·1{r>0
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "allowImportingTsExtensions": true,
    "noEmit": true,
    "strict": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src", "test"]
}
```

#### File: `tsconfig.build.json`
```python
{
  "extends": "./tsconfig.json",
  "compilerOptions": {
    "noEmit": false,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "dist",
    "rootDir": "src",
    "rewriteRelativeImportExtensions": true,
    "allowImportingTsExtensions": true
  },
  "include": ["src"],
  "exclude": ["test"]
}
```

#### File: `python/tests/test_moments.py`
```python
import math

from orderflow_metrics import realized_kurtosis, realized_skewness

R = [0.01, -0.02, 0.015, -0.005, 0.03, -0.01, 0.008, -0.025]


def test_realized_skewness():
    assert math.isclose(realized_skewness(R), 0.167588027657, abs_tol=1e-9)


def test_realized_kurtosis():
    assert math.isclose(realized_kurtosis(R), 1.931132423255, abs_tol=1e-9)


def test_symmetric_zero_skew():
    assert math.isclose(realized_skewness([0.02, -0.02, 0.02, -0.02]), 0.0, abs_tol=1e-12)


def test_empty_or_zero_variance():
    assert realized_skewness([]) == 0.0
    assert realized_kurtosis([]) == 0.0
    assert realized_skewness([0, 0, 0]) == 0.0
    assert realized_kurtosis([0, 0, 0]) == 0.0
```

#### File: `python/tests/test_hurst.py`
```python
import math

from orderflow_metrics import hurst_exponent


def minstd(n):
    x = 1
    s = []
    for _ in range(n):
        x = (48271 * x) % 2147483647
        s.append(x / 2147483647)
    return s


def test_hurst_regression_value():
    assert math.isclose(hurst_exponent(minstd(128)), 0.638944060791, abs_tol=1e-9)


def test_noise_near_half_walk_higher():
    noise = minstd(128)
    h = hurst_exponent(noise)
    assert 0.3 < h < 0.7
    c = 0.0
    walk = []
    for v in noise:
        c += v - 0.5
        walk.append(c)
    assert hurst_exponent(walk) > h


def test_short_series_nan():
    assert math.isnan(hurst_exponent(list(range(1, 9))))
    assert math.isnan(hurst_exponent([]))
```

#### File: `python/src/orderflow_metrics/imbalance.py`
```python
"""Book and trade imbalance metrics.

Both return a value in [-1, 1]: positive = buy-side heavy, negative = sell-side
heavy, 0 = balanced (or empty input).
"""
from __future__ import annotations

from typing import Sequence

from .types import L1Quote, Trade


def depth_imbalance(q: L1Quote) -> float:
    """Top-of-book depth imbalance: (bid_size - ask_size) / (bid_size + ask_size)."""
    denom = q.bid_size + q.ask_size
    return 0.0 if denom == 0 else (q.bid_size - q.ask_size) / denom


def trade_imbalance(trades: Sequence[Trade]) -> float:
    """Trade imbalance: (buy_vol - sell_vol) / (buy_vol + sell_vol)."""
    buy = sum(t.size for t in trades if t.side == "buy")
    sell = sum(t.size for t in trades if t.side == "sell")
    denom = buy + sell
    return 0.0 if denom == 0 else (buy - sell) / denom
```

#### File: `python/src/orderflow_metrics/liquidity.py`
```python
"""Liquidity measures."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True)
class ReturnVolume:
    """A period return paired with the traded (or dollar) volume over it."""

    ret: float
    volume: float


def amihud_illiquidity(obs: Sequence[ReturnVolume]) -> float:
    """Amihud (2002) illiquidity: the average of |return| / volume across periods.

    Captures how much price moves per unit of volume — a high value means even
    small trades push the price a lot (thin, illiquid). Periods with zero volume
    are skipped. Returns 0 when there is no usable data.
    """
    total = 0.0
    n = 0
    for o in obs:
        if o.volume > 0:
            total += abs(o.ret) / o.volume
            n += 1
    return 0.0 if n == 0 else total / n
```


==================================================
