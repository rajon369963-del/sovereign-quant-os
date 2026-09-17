# ⚡ [QUANT-SOURCE-009] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_009_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: indian-share-market (`VAULT_IN-QUANT-077_abuhurairalakdawala__indian-share-market`)
- **Full Name**: `IN-QUANT-077_abuhurairalakdawala__indian-share-market`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Indian Share Market

[![Latest Stable Version](https://img.shields.io/packagist/v/abuhurairalakdawala/indian-share-market.svg)](https://packagist.org/packages/abuhurairalakdawala/indian-share-market)

### Introduction
This package helps you get latest data from National and Bombay Stock Exchange.

You can also use it for REST API's.

You can get the data in JSON, CSV or Array formats.

> The stock market is filled with individuals who know the price of everything, but the value of nothing.

### Requirement

This is a PHP library, it require PHP7.

### Installation
```sh
$ composer require abuhurairalakdawala/indian-share-market
```

### Documentation
For documentation visit [[here]](https://abuhurairalakdawala.github.io/ism/) or [[@github]](https://github.com/abuhurairalakdawala/ism).

### Features!

  - Retrieve latest stocks from NSE & BSE.
  - List of NSE & BSE Sectors.
  - List of NSE & BSE Industries.
  - Real time stock quotes

### Todos

We have to fetch the following data

 - Top Gainers
 - Top Loosers
 - Future and option data
 - Historical Data
 - more to come...

### Development

Want to contribute? Great!

License
----

MIT

### Core Implementation Code & Architecture
#### File: `composer.json`
```python
{
    "name": "abuhurairalakdawala/indian-share-market",
    "type": "library",
    "authors": [
        {
            "name": "Abuhuraira Lakdawala",
            "email": "abu2602@gmail.com"
        }
    ],
    "keywords": [
        "nifty",
        "sensex",
        "nse",
        "bse"
    ],
    "license": "MIT",
    "minimum-stability": "stable",
    "prefer-stable": true,
    "require": {},
    "autoload": {
        "psr-4": {
            "IndianShareMarket\\": "src/"
        }
    }
}
```


==================================================


## [2/3] Repository: IndianStockMarketData (`VAULT_IN-QUANT-078_emanivinay__IndianStockMarketData`)
- **Full Name**: `IN-QUANT-078_emanivinay__IndianStockMarketData`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# stock-market-app

Stock market App allows users to view and track stock prices on their smart phones.


==================================================


## [3/3] Repository: bulk_dwd_yfinanance_indian_market_data (`VAULT_IN-QUANT-081_RaiAnk__bulk_dwd_yfinanance_indian_market_data`)
- **Full Name**: `IN-QUANT-081_RaiAnk__bulk_dwd_yfinanance_indian_market_data`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Bulk YFinance Indian Market Data Downloader

A Python-based tool for downloading historical stock market data from NSE and BSE exchanges. Retrieves 10 years of daily OHLCV data for Nifty 50, Sensex 30 constituent stocks, and major market indices.

## Overview

This tool automates the process of downloading and organizing historical stock data from Yahoo Finance API for Indian equity markets. It's designed for data analysts, quantitative researchers, and developers building financial models or backtesting strategies.

## Features

- Downloads historical data for all Nifty 50 constituent stocks (NSE)
- Downloads historical data for all Sensex 30 constituent stocks (BSE)
- Includes major indices: Nifty 50, Sensex, Bank Nifty
- Automatic retry logic and error handling
- Organized directory structure for easy data access
- Comprehensive logging to file and console
- Rate limiting to prevent API throttling
- Auto-adjusted data for stock splits and dividends

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Dependencies

Install required packages:
```bash
pip install yfinance pandas
```

Or use requirements file:
```bash
pip install -r requirements.txt
```

**requirements.txt:**
```
yfinance>=0.2.28
pandas>=1.5.0
```

## Usage

### Basic Usage

Run the script directly to download all data:
```bash
python bulk_download.py
```

This will download 10 years of historical data for all stocks and save to the `data/` directory.

### Advanced Usage

Import as a module for custom workflows:
```python
from bulk_download import StockDataDownloader

# Initialize downloader
downloader = StockDataDownloader(base_path="my_data")

# Download last 5 years of data
stats = downloader.run_full_download(years=5)

# Check download statistics
print(f"Downloaded {stats['nifty_success']} Nifty stocks")
print(f"Downloaded {stats['sensex_success']} Sensex stocks")
```

### Download Specific Components
```python
from datetime import datetime, timedelta
from bulk_download import StockDataDownloader

downloader = StockDataDownloader()

# Set custom date range
end_date = datetime.now()
start_date = end_date - timedelta(days=365*3)  # 3 years

# Download only indices
downloader.download_market_indices(start_date, end_date)

# Download only Nifty 50 stocks
nifty_stocks = downloader.get_nifty50_stocks()
downloader.bulk_download_stocks(nifty_stocks, "data/nifty50", start_date, end_date)
```

## Output Structure

After execution, data is organized as follows:
```
data/
├── NIFTY50_index.csv       # Nifty 50 index historical data
├── SENSEX_index.csv        # Sensex index historical data
├── BANKNIFTY_index.csv     # Bank Nifty index historical data
├── nifty50/                # Individual Nifty 50 stocks
│   ├── RELIANCE.csv
│   ├── TCS.csv
│   ├── INFY.csv
│   └── ... (50 files)
└── sensex30/               # Individual Sensex 30 stocks
    ├── RELIANCE.csv
    ├── TCS.csv
    ├── HDFCBANK.csv
    └── ... (30 files)
```

### CSV Format

Each CSV file contains the following columns:
```
Date, Open, High, Low, Close, Volume
```

Example:
```csv
Date,Open,High,Low,Close,Volume
2020-01-01,1234.50,1245.00,1230.00,1240.00,5000000
2020-01-02,1241.00,1250.00,1238.00,1248.00,4800000
```

## Configuration

### Modify Historical Data Range

Edit the `years` parameter in the `main()` function:
```python
def main():
    downloader = StockDataDownloader(base_path="data")
    stats = downloader.run_full_download(years=15)  # Download 15 years
    return stats
```

### Change Output Directory

Specify custom path when initializing:
```python
downloader = StockDataDownloader(base_path="custom_folder")
```

### Adjust Rate Limiting

Modify the sleep delay in `bulk_download_stocks()`:
```python
time.sleep(0.5)  # Change to 1.0 for slower, safer requests
```

## Logging

The script generates two types of logs:

1. **Console output**: Real-time progress displayed in terminal
2. **Log file**: Detailed logs saved to `stock_downloader.log`

Log format:
```
2024-11-18 10:30:45 - INFO - Downloading data for RELIANCE.NS
2024-11-18 10:30:47 - INFO - Successfully saved: data/nifty50/RELIANCE.csv (2518 rows)
```

## Troubleshooting

### Connection Errors

If downloads fail due to network issues:
- Check internet connectivity
- Verify Yahoo Finance service status
- Increase rate limiting delay (change `time.sleep()` value)

### Missing Data

Some stocks may have limited historical data:
- Check if stock was recently listed
- Verify stock symbol is correct
- Review log file for specific error messages

### API Rate Limiting

If receiving HTTP 429 errors:
- Increase delay between requests in `bulk_download_stocks()`
- Run script during off-peak hours
- Download in smaller batches

## Notes

- Data is adjusted for stock splits and dividends automatically
- Nifty 50 constituent list is fetched dynamically from NSE
- If NSE API fails, fallback to hardcoded list (may be outdated)
- Downloads only trading day data (weekends/holidays excluded)
- First run may take 30-45 minutes depending on network speed

## Use Cases

- Building stock price prediction models (LSTM, ARIMA)
- Backtesting trading strategies
- Portfolio optimization research
- Statistical arbitrage analysis
- Market correlation studies
- Technical indicator development

## License

MIT License - Free for commercial and personal use

## Contributing

Contributions welcome. Please ensure code follows existing style and includes appropriate documentation.

## Disclaimer

This tool is for educational and research purposes. Market data accuracy depends on Yahoo Finance API. Always verify critical data from official sources. Not financial advice.

## Support

For issues or questions:
- Check the log file for detailed error messages
- Review Yahoo Finance API documentation
- Verify all dependencies are correctly installed

---

Last Updated: November 2024

### Core Implementation Code & Architecture
#### File: `downloadfullfinancedata.py`
```python
"""
Indian Stock Market Data Downloader
===================================
A production-ready script for downloading historical stock data from NSE and BSE.
Supports Nifty 50, Sensex 30, and major indices with comprehensive error handling.

Author: Market Data Analytics Team
Version: 1.0.0
Dependencies: yfinance, pandas
"""

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os
import time
import logging
from typing import List, Dict, Tuple

# Configure logging for production environment
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('stock_downloader.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class StockDataDownloader:
    """
    Handles bulk downloading of Indian stock market data from NSE and BSE exchanges.
    Implements rate limiting and retry logic for robust data acquisition.
    """
    
    def __init__(self, base_path: str = "data"):
        """
        Initialize the downloader with directory structure.
        
        Args:
            base_path: Root directory for storing downloaded data
        """
        self.base_path = base_path
        self.nifty_path = os.path.join(base_path, "nifty50")
        self.sensex_path = os.path.join(base_path, "sensex30")
        
        # Create directory structure if it doesn't exist
        self._setup_directories()
        
    def _setup_directories(self) -> None:
        """Create necessary directory structure for data storage."""
        directories = [self.base_path, self.nifty_path, self.sensex_path]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        logger.info(f"Directory structure initialized at: {self.base_path}")
    
    def get_nifty50_stocks(self) -> List[str]:
        """
        Fetch the current list of Nifty 50 constituent stocks from NSE.
        Falls back to hardcoded list if API call fails.
        
        Returns:
            List of stock symbols with .NS suffix for NSE exchange
        """
        try:
            # Attempt to fetch live data from NSE official source
            nse_url = 'https://www.nseindia.com/content/indices/ind_nifty50list.csv'
            df = pd.read_csv(nse_url)
            symbols = [f"{symbol}.NS" for symbol in df['Symbol'].tolist()]
            logger.info(f"Successfully fetched {len(symbols)} Nifty 50 stocks from NSE")
            return symbols
        except Exception as e:
            # Fallback to static list if API fails
            logger.warning(f"Failed to fetch live Nifty 50 list: {e}. Using fallback list.")
            return self._get_fallback_nifty50()
    
    def _get_fallback_nifty50(self) -> List[str]:
        """
        Provides a hardcoded fallback list of Nifty 50 constituents.
        This list should be periodically updated to reflect index changes.
        
        Returns:
            Static list of Nifty 50 stock symbols
        """
        return [
            'ADANIPORTS.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS',
            'BAJFINANCE.NS', 'BAJAJFINSV.NS', 'BPCL.NS', 'BHARTIARTL.NS',
            'CIPLA.NS', 'COALINDIA.NS', 'DRREDDY.NS', 'EICHERMOT.NS',
            'GRASIM.NS', 'HCLTECH.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS',
            'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS',
            'INDUSINDBK.NS', 'INFY.NS', 'ITC.NS', 'JSWSTEEL.NS',
            'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NESTLEIND.NS',
            'NTPC.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBIN.NS',
            'SUNPHARMA.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TCS.NS',
            'TECHM.NS', 'TITAN.NS', 'ULTRACEMCO.NS', 'WIPRO.NS',
            'ADANIENT.NS', 'APOLLOHOSP.NS', 'BRITANNIA.NS', 'DIVISLAB.NS',
            'HDFCLIFE.NS', 'LTIM.NS', 'SBILIFE.NS', 'TATACONSUM.NS'
        ]
    
    def get_sensex30_stocks(self) -> List[str]:
        """
        Get the list of Sensex 30 constituent stocks for BSE exchange.
        
        Returns:
            List of stock symbols with .BO suffix for BSE exchange
        """
        sensex_constituents = [
            'RELIANCE.BO', 'TCS.BO', 'HDFCBANK.BO', 'INFY.BO', 'ICICIBANK.BO',
            'HINDUNILVR.BO', 'ITC.BO', 'SBIN.BO', 'BHARTIARTL.BO', 'BAJFINANCE.BO',
            'KOTAKBANK.BO', 'LT.BO', 'AXISBANK.BO', 'ASIANPAINT.BO', 'MARUTI.BO',
            'SUNPHARMA.BO', 'TITAN.BO', 'ULTRACEMCO.BO', 'NESTLEIND.BO',
            'TATAMOTORS.BO', 'M&M.BO', 'HCLTECH.BO', 'POWERGRID.BO', 'NTPC.BO',
            'WIPRO.BO', 'TATASTEEL.BO', 'BAJAJFINSV.BO', 'TECHM.BO',
            'INDUSINDBK.BO', 'JSWSTEEL.BO'
        ]
        logger.info(f"Loaded {len(sensex_constituents)} Sensex 30 stocks")
        return sensex_constituents
    
    def download_single_stock(self, symbol: str, start_date: datetime, 
                             end_date: datetime, save_path: str) -> bool:
        """
        Download historical OHLCV data for a single stock symbol.
        
        Args:
            symbol: Stock ticker symbol (e.g., 'RELIANCE.NS')
            start_date: Start date for historical data
            end_date: End date for historical data
            save_path: Directory path to save the CSV file
            
        Returns:
            True if download successful, False otherwise
        """
        try:
            logger.info(f"Downloading data for {symbol}")
            
            # Fetch data from Yahoo Finance API
            data = yf.download(
                symbol, 
                start=start_date, 
                end=end_date, 
                progress=False,
                auto_adjust=True  # Adjust for splits and dividends
            )
            
            if not data.empty:
                # Clean symbol name for filename (remove exchange suffix)
                clean_symbol = symbol.replace('.NS', '').replace('.BO', '')
                filename = os.path.join(save_path, f"{clean_symbol}.csv")
                
                # Save to CSV with proper formatting
                data.to_csv(filename)
                logger.info(f"Successfully saved: {filename} ({len(data)} rows)")
                return True
            else:
                logger.warning(f"No data available for {symbol}")
                return False
                
        except Exception as e:
            logger.error(f"Failed to download {symbol}: {str(e)}")
            return False
    
    def bulk_download_stocks(self, stock_list: List[str], save_path: str, 
                            start_date: datetime, end_date: datetime) -> Tuple[int, int]:
        """
        Download historical data for multiple stocks with rate limiting.
        
        Args:
            stock_list: List of stock symbols to download
            save_path: Directory to save CSV files
            start_date: Start date for historical data
            end_date: End date for historical data
            
        Returns:
            Tuple of (successful_downloads, total_stocks)
        """
        success_count = 0
        total_stocks = len(stock_list)
        
        logger.info(f"Starting bulk download of {total_stocks} stocks")
        
        for idx, stock in enumerate(stock_list, 1):
            logger.info(f"Processing {idx}/{total_stocks}: {stock}")
            
            if self.download_single_stock(stock, start_date, end_date, save_path):
                success_count += 1
            
            # Rate limiting: Add delay between requests to avoid API throttling
            time.sleep(0.5)
        
        logger.info(f"Bulk download complete: {success_count}/{total_stocks} successful")
        return success_count, total_stocks
    
    def download_market_indices(self, start_date: datetime, end_date: datetime) -> None:
        """
        Download historical data for major Indian market indices.
        
        Args:
            start_date: Start date for historical data
            end_date: End date for historical data
        """
        # Define major indices with their Yahoo Finance symbols
        indices_config = {
            '^NSEI': 'NIFTY50',        # Nifty 50 Index
            '^BSESN': 'SENSEX',        # BSE Sensex Index
            '^NSEBANK': 'BANKNIFTY'    # Bank Nifty Index
        }
        
        logger.info("Starting download of market indices")
        
        for symbol, name in indices_config.items():
            try:
                logger.info(f"Downloading {name} index data")
                data = yf.download(symbol, start=start_date, end=end_date, progress=False)
                
                if not data.empty:
                    filename = os.path.join(self.base_path, f"{name}_index.csv")
                    data.to_csv(filename)
                    logger.info(f"Index saved: {filename} ({len(data)} rows)")
                else:
                    logger.warning(f"No data available for {name}")
                    
            except Exception as e:
                logger.error(f"Failed to download {name} index: {str(e)}")
    
    def run_full_download(self, years: int = 10) -> Dict[str, any]:
        """
        Execute complete download workflow for all indices and stocks.
        
        Args:
            years: Number of years of historical data to download
            
        Returns:
            Dictionary containing download statistics
        """
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=years * 365)
        
        logger.info("=" * 70)
        logger.info("INDIAN STOCK MARKET DATA DOWNLOADER - FULL EXECUTION")
        logger.info("=" * 70)
        logger.info(f"Date range: {start_date.date()} to {end_date.date()}")
        logger.info(f"Data path: {os.path.abspath(self.base_path)}")
        
        stats = {
            'start_date': start_date,
            'end_date': end_date,
            'indices_downloaded': 0,
            'nifty_success': 0,
            'nifty_total': 0,
            'sensex_success': 0,
            'sensex_total': 0
        }
        
        # Step 1: Download market indices
        logger.info("\n" + "=" * 70)
        logger.info("PHASE 1: Downloading Market Indices")
        logger.info("=" * 70)
        self.download_market_indices(start_date, end_date)
        stats['indices_downloaded'] = 3
        
        # Step 2: Download Nifty 50 constituent stocks
        logger.info("\n" + "=" * 70)
        logger.info("PHASE 2: Downloading Nifty 50 Stocks")
        logger.info("=" * 70)
        nifty_stocks = self.get_nifty50_stocks()
        nifty_success, nifty_total = self.bulk_download_stocks(
            nifty_stocks, self.nifty_path, start_date, end_date
        )
        stats['nifty_success'] = nifty_success
        stats['nifty_total'] = nifty_total
        
        # Step 3: Download Sensex 30 constituent stocks
        logger.info("\n" + "=" * 70)
        logger.info("PHASE 3: Downloading Sensex 30 Stocks")
        logger.info("=" * 70)
        sensex_stocks = self.get_sensex30_stocks()
        sensex_success, sensex_total = self.bulk_download_stocks(
            sensex_stocks, self.sensex_path, start_date, end_date
        )
        stats['sensex_success'] = sensex_success
        stats['sensex_total'] = sensex_total
        
        # Display final summary
        self._print_summary(stats)
        
        return stats
    
    def _print_summary(self, stats: Dict[str, any]) -> None:
        """
        Print comprehensive download summary report.
        
        Args:
            stats: Dictionary containing download statistics
        """
        logger.info("\n" + "=" * 70)
        logger.info("DOWNLOAD SUMMARY REPORT")
        logger.info("=" * 70)
        logger.info(f"Date Range: {stats['start_date'].date()} to {stats['end_date'].date()}")
        logger.info(f"Indices Downloaded: {stats['indices_downloaded']}")
        logger.info(f"Nifty 50: {stats['nifty_success']}/{stats['nifty_total']} stocks")
        logger.info(f"Sensex 30: {stats['sensex_success']}/{stats['sensex_total']} stocks")
        logger.info("\nData Location:")
        logger.info(f"  - Indices: {self.base_path}/")
        logger.info(f"  - Nifty 50: {self.nifty_path}/")
        logger.info(f"  - Sensex 30: {self.sensex_path}/")
        logger.info("=" * 70)


def main():
    """
    Main entry point for the stock data downloader application.
    Initializes the downloader and executes full download workflow.
    """
    # Initialize downloader with default data directory
    downloader = StockDataDownloader(base_path="data")
    
    # Execute full download for last 10 years
    # Modify the 'years' parameter to adjust historical data range
    stats = downloader.run_full_download(years=10)
    
    # Optional: Return stats for further processing or logging
    return stats


if __name__ == "__main__":
    """
    Script execution entry point.
    Runs when script is executed directly (not imported as module).
    """
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("\nDownload interrupted by user")
    except Exception as e:
        logger.error(f"Critical error during execution: {str(e)}", exc_info=True)
```


==================================================
