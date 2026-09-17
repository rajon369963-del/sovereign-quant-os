# ⚡ [QUANT-SOURCE-065] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_065_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: ipo-data-scraper-python (`VAULT_IN-QUANT-063_agrimgoyal__ipo-data-scraper-python`)
- **Full Name**: `IN-QUANT-063_agrimgoyal__ipo-data-scraper-python`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# IPO Scraper

A robust web scraper that collects and tracks Initial Public Offering (IPO) data from [Screener.in](https://www.screener.in). This tool automates the process of gathering IPO information, including listing dates, market capitalizations, price history, and performance metrics.

## Overview

The IPO Scraper is designed to:
- Extract comprehensive IPO data from Screener.in
- Track listing dates, IPO prices, current prices, and performance metrics
- Maintain a record of processed IPOs to avoid duplication
- Export collected data to Excel for easy analysis
- Implement error handling and retry mechanisms for reliable data collection

## Features

- **Automated Data Collection**: Scrapes IPO data from multiple pages automatically
- **Duplicate Prevention**: Maintains a record of processed IPOs to avoid duplication
- **Comprehensive Data**: Collects company name, listing date, market cap, IPO price, current price, and performance metrics
- **Persistent Storage**: Exports data to Excel for easy analysis and record-keeping
- **Error Handling**: Implements robust error handling and retry logic
- **Logging**: Provides detailed logging for monitoring and debugging

## Technologies Used

- **Python 3.7+**: Core programming language
- **Requests**: HTTP library for making web requests
- **BeautifulSoup4**: HTML parsing and navigation
- **Pandas**: Data manipulation and Excel export
- **Logging**: Standard library for application logging
- **Pathlib**: Object-oriented filesystem paths
- **JSON**: Data serialization for tracking processed IPOs

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/ipo-scraper.git
   cd ipo-scraper
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Run the script to start scraping IPO data:

```bash
python ipo_scraper.py
```

### Output

The script generates:
- `ipo_data.xlsx`: Excel file containing all the scraped IPO data
- `processed_ipos.json`: JSON file tracking already processed IPOs to avoid duplication

### Example Output

The Excel file will contain the following columns:
- Company: Name of the company
- Company Link: URL to the company's page on Screener.in
- Listing Date: Date when the company was listed
- IPO MCap (Rs. Cr): Market capitalization at IPO
- IPO Price: Initial offering price
- Current Price: Current trading price
- Percent Change: Performance since IPO

## 🔍 How It Works

1. The scraper starts by loading previously processed IPOs from the JSON file.
2. It then navigates to the recent IPO page on Screener.in.
3. The scraper determines the total number of pages to process.
4. For each page, it extracts data from the IPO table, including:
   - Company name and link
   - Listing date
   - Market capitalization
   - IPO price
   - Current price
   - Performance metrics
5. New IPO data is appended to the Excel file.
6. The list of processed IPOs is updated to avoid duplication in future runs.

## Development Challenges

- **Handling Pagination**: Implementing a robust solution to navigate through multiple pages of IPO listings.
- **Preventing Duplication**: Creating a system to track already processed IPOs across multiple runs.
- **Error Handling**: Building resilient error handling and retry mechanisms to deal with potential network issues.
- **Rate Limiting**: Implementing reasonable delays between requests to respect the website's servers.

## Future Enhancements

- Add command-line arguments for customization (e.g., output file path, base URL)
- Implement email notifications for new IPO listings
- Add data visualization capabilities
- Expand to scrape additional financial metrics
- Implement parallel processing for faster scraping
- Add support for additional data sources


## Contact

For questions or feedback, please reach out to agrim.goyal@gmail.com.

### Core Implementation Code & Architecture
#### File: `screener_recentIPOs.py`
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import logging
from pathlib import Path
import json
from datetime import datetime

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

class IPOScraper:
    def __init__(self, base_url: str = "https://www.screener.in"):
        """
        Initialize the IPO scraper with base URL and settings.
        
        Args:
            base_url: The base URL for screener.in
        """
        self.base_url = base_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        # Store processed IPOs in a set for quick lookup
        self.processed_ipos = self._load_processed_ipos()
        self.output_file = "ipo_data.xlsx"
        self.processed_file = "processed_ipos.json"
        
    def _load_processed_ipos(self) -> set:
        """
        Load previously processed IPOs from JSON file.
        
        Returns:
            Set of processed IPO identifiers
        """
        try:
            if Path(self.processed_file).exists():
                with open(self.processed_file, 'r') as f:
                    return set(json.load(f))
        except Exception as e:
            logger.error(f"Error loading processed IPOs: {str(e)}")
        return set()

    def _save_processed_ipos(self):
        """Save processed IPOs to JSON file."""
        try:
            with open(self.processed_file, 'w') as f:
                json.dump(list(self.processed_ipos), f)
        except Exception as e:
            logger.error(f"Error saving processed IPOs: {str(e)}")

    def _extract_pagination_info(self, soup: BeautifulSoup) -> int:
        """
        Extract total number of pages from pagination div.
        
        Args:
            soup: BeautifulSoup object of the page
            
        Returns:
            Total number of pages
        """
        pagination = soup.find('div', class_='pagination')
        if not pagination:
            return 1
            
        # Find all page links
        page_links = pagination.find_all('a')
        max_page = 1
        
        for link in page_links:
            # Extract page number from href
            if 'page=' in link.get('href', ''):
                try:
                    page_num = int(link['href'].split('page=')[1])
                    max_page = max(max_page, page_num)
                except ValueError:
                    continue
                    
        return max_page

    def _extract_ipo_data(self, row) -> dict:
        """
        Extract IPO information from a table row.
        
        Args:
            row: BeautifulSoup table row object
            
        Returns:
            Dictionary containing IPO data
        """
        cells = row.find_all('td')
        if not cells:
            return None
            
        # Extract company name and link
        name_cell = cells[0].find('a')
        if not name_cell:
            return None
            
        company_name = name_cell.text.strip()
        company_link = name_cell['href']
        
        # Create unique identifier for IPO
        ipo_id = f"{company_name}_{cells[1].text.strip()}"
        
        # Extract other data
        ipo_data = {
            'Company': company_name,
            'Company Link': f"{self.base_url}{company_link}",
            'Listing Date': cells[1].text.strip(),
            'IPO MCap (Rs. Cr)': cells[2].text.strip(),
            'IPO Price': cells[3].text.replace('₹', '').strip(),
            'Current Price': cells[4].text.replace('₹', '').strip(),
            'Percent Change': cells[5].text.strip().replace('⇣', '-').replace('⇡', '+')
        }
        
        return ipo_id, ipo_data

    def _make_request(self, url: str) -> requests.Response:
        """
        Make an HTTP request with error handling and retry logic.
        
        Args:
            url: URL to request
            
        Returns:
            Response object or None if failed
        """
        max_retries = 3
        
        for attempt in range(max_retries):
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                return response
            except requests.RequestException as e:
                logger.error(f"Error fetching {url}: {str(e)}")
                
            if attempt < max_retries - 1:
                delay = (2 ** attempt) + (time.random() * 0.1)
                time.sleep(delay)
            
        return None

    def scrape_ipo_data(self):
        """Scrape IPO data from all pages and save to Excel."""
        all_ipo_data = []
        url = f"{self.base_url}/ipo/recent/"
        
        # Get initial page
        response = self._make_request(url)
        if not response:
            logger.error("Failed to fetch initial page")
            return
            
        soup = BeautifulSoup(response.text, 'html.parser')
        total_pages = self._extract_pagination_info(soup)
        
        logger.info(f"Found {total_pages} pages to process")
        
        # Process all pages
        for page in range(1, total_pages + 1):
            page_url = f"{url}?page={page}"
            response = self._make_request(page_url)
            
            if not response:
                continue
                
            soup = BeautifulSoup(response.text, 'html.parser')
            table = soup.find('table', class_='data-table')
            
            if not table:
                continue
                
            # Process each row
            for row in table.find('tbody').find_all('tr'):
                ipo_id, ipo_data = self._extract_ipo_data(row)
                
                if ipo_id in self.processed_ipos:
                    logger.info(f"IPO {ipo_data['Company']} already processed, skipping...")
                    continue
                    
                all_ipo_data.append(ipo_data)
                self.processed_ipos.add(ipo_id)
                
            logger.info(f"Processed page {page}/{total_pages}")
            time.sleep(2)  # Be nice to the server
            
        # Save data if we found new IPOs
        if all_ipo_data:
            # Load existing data if file exists
            if Path(self.output_file).exists():
                existing_df = pd.read_excel(self.output_file)
                new_df = pd.DataFrame(all_ipo_data)
                final_df = pd.concat([existing_df, new_df], ignore_index=True)
            else:
                final_df = pd.DataFrame(all_ipo_data)
                
            final_df.to_excel(self.output_file, index=False)
            self._save_processed_ipos()
            logger.info(f"Added {len(all_ipo_data)} new IPOs to {self.output_file}")
        else:
            logger.info("No new IPOs found")

def main():
    """Main function to run the IPO scraper."""
    scraper = IPOScraper()
    scraper.scrape_ipo_data()

if __name__ == "__main__":
    main()
```


==================================================


## [2/3] Repository: XTS_MasterInstruments (`VAULT_IN-QUANT-065_TechfaneTechnologies__XTS_MasterInstruments`)
- **Full Name**: `IN-QUANT-065_TechfaneTechnologies__XTS_MasterInstruments`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
[![Deploy static content to Pages](https://github.com/TechfaneTechnologies/XTS_MasterInstruments/actions/workflows/static.yml/badge.svg)](https://github.com/TechfaneTechnologies/XTS_MasterInstruments/actions/workflows/static.yml)      [![Update XTS Master Instruments](https://github.com/TechfaneTechnologies/XTS_MasterInstruments/actions/workflows/main.yml/badge.svg)](https://github.com/TechfaneTechnologies/XTS_MasterInstruments/actions/workflows/main.yml)
# XTS Master Instruments / Contracts
Symphony Fintech XTS API Instrument / Contract Masters CSV's. It allows to download master contract as CSV Files. The master contract contains all necessary information about all available contracts. Gets all contracts or filter contracts by exchange segment.


## Update Frequency
Check for updates daily at 08:00 AM IST and 09:00 PM IST.


## ExchangeSegment Wise CSV Files.
- [NSECM_INDEX.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/NSECM_INDEX.csv)
- [NSECM.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/NSECM.csv)
- [NSEFO.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/NSEFO.csv)
- [NSECD.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/NSECD.csv)
- [BSECM_INDEX.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/BSECM_INDEX.csv)
- [BSECM.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/BSECM.csv)
- [BSEFO.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/BSEFO.csv)
- [BSECO.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/BSECO.csv)
- [BSECD.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/BSECD.csv)
- [NCDEX.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/NCDEX.csv)
- [MCXFO.csv](https://techfanetechnologies.github.io/XTS_MasterInstruments/csv/MCXFO.csv)

## _If You have liked the work, Do Star This Repository and Stay-Up-To-Date_
<p align="center">
  <img src="https://user-images.githubusercontent.com/96371033/180197157-aabda812-828b-4cf7-97a6-a4b9bdd8b151.gif" alt="How To Star A Repository">
</p>

### Core Implementation Code & Architecture
#### File: `main.py`
```python
# -*- coding: utf-8 -*-
"""
    :description: A Python Script To Fetch and Save Symphony Fintech XTS API's Instrument/Contract Masters as CSV Files.
    :license: MIT.
    :author: Dr June Moone
    :created: On Monday March 27, 2023 01:30:30 GMT+05:30
"""
__author__ = "Dr June Moone"
__webpage__ = "https://github.com/MooneDrJune"
__license__ = "MIT"


import os

import requests

from json import JSONDecodeError

HEADERS = {"Content-Type": "application/json"}
BASE_URL = "https://developers.symphonyfintech.in/apimarketdata/instruments"
MASTER = "/master"
INDEXLIST = "/indexlist"
IL_PARAMS_NSE = {"exchangeSegment": 1}
IL_PARAMS_BSE = {"exchangeSegment": 11}

CM_HDR = "ExchangeSegment|ExchangeInstrumentID|InstrumentType|Name|Description|Series|NameWithSeries|InstrumentID|PriceBandHigh|PriceBandLow| FreezeQty|TickSize|LotSize|Multiplier|displayName|ISIN|PriceNumerator|PriceDenominator|FullDescription\n"
FO_HDR = "ExchangeSegment|ExchangeInstrumentID|InstrumentType|Name|Description|Series|NameWithSeries|InstrumentID|PriceBandHigh|PriceBandLow|FreezeQty|TickSize|LotSize|Multiplier|UnderlyingInstrumentId|UnderlyingIndexName|ContractExpiration|StrikePrice|OptionType|displayName|PriceNumerator|PriceDenominator|FullDescription\n"

exchangeSegmentList = [
    "NSECM",
    "NSEFO",
    "NSECD",
    "NSECO",
    "BSECM",
    "BSEFO",
    "BSECD",
    "BSECO",
    "NCDEX",
    "MSECM",
    "MSEFO",
    "MSECD",
    "MCXFO",
]


def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start + len(needle))
        n -= 1
    return start


if __name__ == "__main__":
    os.makedirs(os.path.join(os.getcwd(), "csv"), exist_ok=True)
    exchange_wise_MC = dict.fromkeys(exchangeSegmentList, "")
    exchange_wise_MC_Idx = dict.fromkeys(["NSECM", "BSECM"], "")
    with requests.session() as session:
        for exchange, params in (
            ("NSECM", IL_PARAMS_NSE),
            ("BSECM", IL_PARAMS_BSE),
        ):  # noqa E501
            try:
                response = session.get(
                    BASE_URL + INDEXLIST,
                    params=params,  # noqa E501
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as _exception:
                print(str(_exception))
            else:
                try:
                    data = response.json()
                except JSONDecodeError:
                    print(
                        f"Failed to Decode Response Json for params: {params}",  # noqa E501
                        f"Respose was: {response.content.decode('utf-8')}",
                        "Continuing Loop to fetch other exchange...",
                        sep="\n",
                        end="\n\n",
                    )
                    continue
                else:
                    exchange_wise_MC_Idx[exchange] = data
        for exchange in exchangeSegmentList:
            try:
                response = session.post(
                    BASE_URL + MASTER,
                    headers=HEADERS,
                    json=dict(exchangeSegmentList=[exchange]),  # noqa E501
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as _exception:
                print(str(_exception))
            else:
                try:
                    data = response.json()
                except JSONDecodeError:
                    print(
                        f"Failed to Decode Response Json for Exchange: {exchange}",  # noqa E501
                        f"Respose was: {response.content.decode('utf-8')}",
                        "Continuing Loop to fetch other exchange...",
                        sep="\n",
                        end="\n\n",
                    )
                    continue
                else:
                    exchange_wise_MC[exchange] = data

    for exchange, data in exchange_wise_MC.items():
        if (
            data != ""
            and isinstance(data, dict)
            and data.get("type")
            and data.get("code")
            and data.get("description")
            and data.get("result")
            and data.get("type").find("success") != -1
            and data.get("description").find("instrument data") != -1
        ):
            with open(f"csv/{exchange}.csv", "w") as file:
                if exchange[-2:].find("CM") != -1:
                    file.write((CM_HDR + data["result"]).replace("|", ","))  # noqa E501
                else:
                    file.write(
                        FO_HDR.replace("|", ",")
                        + "\n".join(
                            lines[: find_nth(lines, ",", 17)]
                            + ",0,0"
                            + lines[find_nth(lines, ",", 17) :]
                            if lines.count(",") == 20
                            else lines[: find_nth(lines, ",", 14)]  # noqa E501
                            + ",-1,,,0,0"
                            + lines[find_nth(lines, ",", 14) :]
                            if lines.count(",") == 17
                            else lines
                            for lines in data["result"].replace("|", ",").split("\n")
                        )
                    )
    for exchange, data in exchange_wise_MC_Idx.items():
        if (
            data != ""
            and isinstance(data, dict)
            and data.get("type")
            and data.get("code")
            and data.get("description")
            and data.get("result")
            and data.get("type").find("success") != -1
            and data.get("description").find("Index List successfully")  # noqa E501
            != -1
        ):
            with open(f"csv/{exchange}_INDEX.csv", "w") as file:
                file.write(
                    (
                        "Name,InstrumentID\n"
                        + "\n".join(
                            index.replace("_", ",")
                            for index in data.get("result").get(
                                "indexList"
                            )  # noqa E501
                        )
                    )
                )  # noqa E501
```


==================================================


## [3/3] Repository: Bharat-SM-Data (`VAULT_IN-QUANT-066_Sampad-Hegde__Bharat-SM-Data`)
- **Full Name**: `IN-QUANT-066_Sampad-Hegde__Bharat-SM-Data`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Bharat (India) Stock Market Data Collection / Fetch Library

Bharat_SM_Data stands for Bharat(India) Stock Market Data.

```shell
pip install Bharat-sm-data
```

<p align="center">
  <img src="https://github.com/Sampad-Hegde/Bharat-SM-Data/raw/master/Logo.png" alt="Logo" width="500" height="400">
</p>

## !!! Disclaimer !!!
**Disclaimer: Use Caution and Consider Legal Implications**
  This project employs third-party private APIs and deals with stock market investing,
both of which come with inherent risks and legal considerations.
Users must ensure
they have the appropriate permissions to use the data obtained from these APIs to avoid potential copyright issues.
Additionally, stock market investing carries financial risks, and users should exercise caution,
conduct thorough research, and seek professional advice before making investment decisions.
The accuracy of third-party data cannot be guaranteed, and this project does not offer financial advice.
Users are responsible for complying with all applicable laws and regulations,
and any unauthorized or illegal use may lead to legal consequences.
This package is strictly for educational purposes,
and any practical applications should be done with careful consideration of the aforementioned risks.
By using this project, users acknowledge and accept these risks and responsibilities,
with the project developers and contributors not liable for any damages,
legal issues, or financial losses resulting from its use.
It is essential to exercise caution and seek legal and financial advice when necessary.


## Library Description
📈 Explore the dynamic world of the Indian Stock Market with our powerful open-source stock market scraping library. 
Effortlessly access real-time and historical data for derivatives, equities, currencies, commodities, ETFs, and more, 
enabling you to make informed investment decisions, develop trading strategies, and stay ahead of market trends.
Our user-friendly API facilitates seamless integration,
making it a valuable tool for traders, investors, and data enthusiasts.
Join Me in harnessing the power of data
to unlock new opportunities in the ever-evolving landscape of the Indian financial markets.
Start scraping today and gain a competitive edge in your financial ventures!
💼📊🚀

### Documentation : [Readthedoc](https://bharat-sm-data.readthedocs.io/en/latest/index.html)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Important Note:
```text
Pass  `is_index=true` whenever calling get_ohlc function for any Indices, Future Contracts and Options Contracts
```

## Installation
Install the package using this command

```bash
pip install Bharat-sm-data
```

## Usage

### Read the Documentation here: [Readthedoc](https://bharat-sm-data.readthedocs.io/en/latest/index.html)

Refer below example Jupyter Notebooks to get know how to use this library :
- [NSE Technical](https://github.com/Sampad-Hegde/Bharat-SM-Data/blob/master/examples/Technical_NSE.ipynb)
- [NSE Derivatives](https://github.com/Sampad-Hegde/Bharat-SM-Data/blob/master/examples/Derivatives_NSE.ipynb)
- [Sensibull  Derivatives](https://github.com/Sampad-Hegde/Bharat-SM-Data/blob/master/examples/Derivatives_Sensibull.ipynb)
- [Tickertape Fundamentals](https://github.com/Sampad-Hegde/Bharat-SM-Data/blob/master/examples/Fundementals_Tickertape.ipynb)
- [Moneycontrol Fundamentals](https://github.com/Sampad-Hegde/Bharat-SM-Data/blob/master/examples/Fundementals_Moneycontrol.ipynb)
 

## Features

- Some basic NSE Data:
  - Last Traded date of Exchange
  - Current Market Status (open/close) and a Nifty 50 current value.
  - Equity Meta data
  - NSE turn-over for the day
  - OHLC data

- Technical Data:
  - Important NSE Reports   
  - All indices data
  - Indices composites
  - OHLC of Indices & Equities
  - Trade Info of Equity
  - Corporate Disclosures
  - SME Data
  - SGB Data
  - ETF
  - Block Deals
  - VIX

- Derivatives (Applicable for both Index and Equity options):
  - Options Expiry Dates
  - Option Chain
  - OHLC of Option contracts
  - PCR (Put Call Ratio)
  - List all Equities allowed for Derivative trading.
  - Option Trade info (Equities Only)
  - Trade Info of Futures
  - OHLC of Future Contracts
  - Currency and commodities Futures
  - Currency and commodities Future contracts OHLC
  - Option Chain with Greeks (From Sensibull)

- Fundamentals :
  - Moneycontrol :
    - Mini Statements from Moneycontrol (some commonly used data out of `annual reports` of few timeframes)
      - overview
      - Income
      - Balance sheet
      - Cash flow
      - Ratios
    - Complete Statements (you get complete data of common reports of all annual/quarter reports)
      - Balance Sheet
      - P & L
      - Quarterly results (25th Percentile)
      - Half-Yearly results (50th Percentile)
      - Nine months (75th Percentile)
      - Yearly results (100th percentile)
      - Cash Flow Statement
      - Ratios
      - Capital Structure
  - Tickertape
    - Index Constituents (Tickertape)
    - Annual Report/ Quarterly Results extracted data
      - Income
      - Balance Sheet
      - Cash flow
    - Peers Comparison (Technical Bsed and Valuation Based)
    - Tickertape Scorecard
    - Share Holding Pattern
    - Mutual Fund Holdings
    - Small Case Holdings
    - Dividend History (paid out + Upcoming which is confirmed)
    - Key Ratios of Stocks and Indices
    - All ETFs under an Index
    - Tickertape Screeners
  - BSE :
    - Download Annual Reports in PDF format

## License

This project is licensed under the Apache License.
See the [LICENSE](https://github.com/Sampad-Hegde/Bharat-SM-Data/blob/master/LICENSE) for more details.

## Acknowledgments
- Pandas
- Requests
- All the websites I used for collecting data
- pydash
- BS4

## Contact
Connect Me over: 
- Email: [me@sampadhegde.in | sampadhegde@gmail.com]
- LinkedIn [sampad-hegde](https://www.linkedin.com/in/sampad-hegde)
- Instagram [@sampad_hegde](https://www.instagram.com/sampad_hegde)
- Facebook [sampad.hegde](https://www.facebook.com/sampad.hegde)

### Core Implementation Code & Architecture
#### File: `Bharat_sm_data/Technical/__init__.py`
```python
from Technical.NSE import NSE
```

#### File: `Bharat_sm_data/Derivatives/__init__.py`
```python
from Derivatives.NSE import NSE
from Derivatives.Sensibull import Sensibull
```

#### File: `Bharat_sm_data/__init__.py`
```python
from Technical import *
from Derivatives import *
from Fundamentals import *
```

#### File: `Bharat_sm_data/Base/__init__.py`
```python
from Base.CustomRequest import CustomSession
from Base.NSEBase import NSEBase
```

#### File: `Bharat_sm_data/Fundamentals/__init__.py`
```python
from Fundamentals.MoneyControl import MoneyControl
from Fundamentals.TickerTape import Tickertape
from Fundamentals.BSE import BSE
from Fundamentals.Screener import Screener
```

#### File: `docs/conf.py`
```python
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath('../Bharat_sm_data/Base'))

project = 'Bharat (INDIA) Stock market Data Collection Library'
copyright = '2025, Sampad Hegde'
author = 'Sampad Hegde'
release = '4.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
```


==================================================
