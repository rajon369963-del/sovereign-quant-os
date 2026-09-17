# ⚡ [QUANT-SOURCE-179] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_179_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: FLOW_IMBALANCE (`WHEEL_ORDER_FLOW_IMBALANCE`)
- **Full Name**: `ORDER_FLOW_IMBALANCE`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Order Flow Imbalance
Desenvolvimento de um possível sinal para HFT/Market Making baseado no conceito de Order Flow Imbalance (OFI).
<br><br>

Baseado no artigo "The price impact of order book events - Rama Cont, Arseniy Kukanov and Sasha Stoikov", esse indicador calcula um número a cada alteração no L1 do book (best bid/ask), considerando mudanças de preço e no volume naquele nível. Assim, um aumento no volume do bid, mesmo sem um aumento de preço, representaria mais desequilíbrio e mais força do lado comprador.
<br><br>
Nesse repositório foi criado o sistema central para a geração desse feature, podendo consequentemente ser usado para diversas aplicações a depender da tese formulada. Acumula-se o fator de OFI por um tempo pré determinado.
<br><br>
Um exemplo: order flow imbalance acumulado nos últimos 15 segundos demonstrou muito mais força compradora que vendedora, e minha pressuposição é de momentum (continuação do movimento). Isso geraria um sinal para uma ordem de compra.

### Core Implementation Code & Architecture
#### File: `utils.py`
```python
import MetaTrader5 as mt5
import pandas as pd

def mt5_connect(login, password, server):
    """
    Connects to MetaTrader 5 and displays basic account information.
    """

    if not mt5.initialize(login=login, password=password, server=server):
        print("initialize() failed")
        mt5.shutdown()
    else: 
        print("Conection stablished with MetaTrader5")
        print(mt5.account_info())

def OpenTicker(ticker):
    """"
    Opens ticker in MT5, making it open for data requests.
    """
    symbol_info = mt5.symbol_info(ticker)
    if not symbol_info.visible:
        mt5.symbol_select(ticker,True)

def open_book(ticker):
    """
    Makes ticker available for book data extraction.
    """
    mt5.market_book_add(ticker)

def extract_bid_ask(ticker):
    """"
    Returns book data for the specified ticker.
    """
    book = mt5.market_book_get(ticker)
    return book

def setup_ticker(ticker):
    """
    Opens ticker for both book and other information pull.
    """
    OpenTicker(ticker)
    open_book(ticker)
```


==================================================


## [2/3] Repository: Order-Flow-Imbalance (`WHEEL_Order-Flow-Imbalance`)
- **Full Name**: `Order-Flow-Imbalance`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Order Flow Imbalance (OFI) Construction

## Objective

This program implements Order Flow Imbalance (OFI) features from high-frequency limit order book (LOB) data and evaluates their application in price impact modeling and cross-asset relationships. OFI is a microstructure-based feature that captures the net imbalance between supply and demand, considered superior to trade volume for modeling short-term returns. The implementation is based on methodologies presented in "Cross-impact of order flow imbalance in equity markets" by Rama Cont, Mihai Cucuringu & Chao Zhang.

## Code Structure & Flow

### 🔹 1. Imports and Configuration
* Standard imports: pandas, numpy, sklearn, and matplotlib
* Column suffixes for bid/ask prices and sizes (bid_px_00, ask_sz_05, etc.) defined for the top 10 levels of the order book

### 🔹 2. Data Loading and Preprocessing
* Primary dataset loaded via pd.read_csv()
* Timestamps converted using pd.to_datetime(), and dataframe sorted by ts_event to preserve chronological order
* Depth column names programmatically generated using list comprehensions

### 🔹 3. Best-Level OFI Calculation
**Function**: compute_best_ofi(row_t, row_tm1)
* Compares bid/ask prices and sizes at level 0 (best bid and best ask) between two time points
* Implements logic from research paper (Cont et al.): if price increases, the new quantity is added; if it stays the same, the change in size is used; if it decreases, the previous size is subtracted
* Applied across the dataset to produce OFI_best

### 🔹 4. Multi-Level OFI Calculation
**Function**: compute_multi_level_ofi(row_t, row_tm1)
* Loops through LOB levels 0 to 9 and applies the same logic as best-level OFI for each depth
* Aggregates across all levels to generate a single OFI_multi value per timestamp

### 🔹 5. Integrated OFI Calculation via PCA
* Constructs a list of 10-dimensional OFI vectors at each timestamp
* Applies Principal Component Analysis (PCA) using sklearn to extract the first principal component
* The first component serves as the Integrated OFI, capturing the most informative combination of depth-level OFIs

### 🔹 6. Synthetic Cross-Asset Dataset
* Creates a synthetic dataset by duplicating the AAPL data and assigning fake tickers (AAPL, GOOG, MSFT)
* Each "synthetic" asset is given slightly perturbed values to simulate distinct order book behavior
* A new symbol column is added to facilitate group-wise calculations

### 🔹 7. Cross-Asset OFI Calculation
**Logic**:
* For each asset, sum the OFI values of all other assets at each timestamp
* This represents a naive cross-asset pressure signal that approximates the influence of external order flow on the asset in question
* Note: This is a simplification of the cross-impact model described in the paper, which uses Lasso regression to formally estimate pairwise impact coefficients

### 🔹 8. Output
* Final features (OFI_best, OFI_multi, OFI_integrated, OFI_cross) are stored in the dataframe for export or further analysis

## Testing Cross-Asset OFI Using Synthetic Data

Since real multi-asset LOB data was unavailable, we:
* Replicated AAPL data into multiple "assets"
* Applied noise or transformations to simulate realistic asset-specific behavior
* Evaluated how well cross-asset OFI aligns with or diverges from asset-specific OFIs

This approach allows testing the cross-impact logic without needing real cross-asset LOB feeds.

## Summary of Outputs

| Feature | Description |
|---------|-------------|
| OFI_best | Order flow imbalance at the best (top) LOB level |
| OFI_multi | Aggregated OFI from top 10 levels of LOB |
| OFI_integrated | PCA-based integrated OFI signal |
| OFI_cross | Sum of OFIs from other synthetic assets at timestamp |


==================================================


## [3/3] Repository: Order-Flow-Imbalance-OFI- (`WHEEL_Order-Flow-Imbalance-OFI-`)
- **Full Name**: `Order-Flow-Imbalance-OFI-`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# OFI Feature Computation Notebook

This Jupyter Notebook processes event-level LOB snapshots, aggregates them into regular time intervals (with an option to implement without aggreation), and outputs various OFI-related features (best-level OFI, multi-level OFI sum, integrated OFI via PCA, and cross-asset OFI). 

## Order Flow Imbalance (OFI)

Order Flow Imbalance (OFI) is a market microstructure indicator that measures the net difference between buying pressure and selling pressure in the order book.  Intuitively, if there is more liquidity (depth) on the bid side than the ask side, price is more likely to move upward, and vice versa.  By quantifying this supply/demand imbalance, OFI provides insight into short-term price dynamics.  

Empirically, OFI has been shown to correlate with price changes. For example, Cont *et al.* demonstrate that, over short intervals, price movements are largely driven by the order flow imbalance at the best bid and ask. More generally, OFI models “quantify the imbalance between buying and selling pressure in financial markets”, helping predict short-term price movements. These properties make the OFI feature useful as a quantitative signal in market microstructure analysis.

## Input Data Format

The notebook expects a CSV file containing LOB snapshots at each event (e.g., each row is a snapshot after a trade or order book update). The file should have at least the following columns:  
- `ts_event`: Timestamp of the event (datetime format).  
- `symbol`: Asset symbol (e.g., stock ticker).  
- Bid price and size columns for each depth level (e.g. `bid_px_00, bid_sz_00, bid_px_01, bid_sz_01, ..., bid_px_09, bid_sz_09`).  
- Ask price and size columns (e.g. `ask_px_00, ask_sz_00, ask_px_01, ask_sz_01, ..., ask_px_09, ask_sz_09`).  

Set `BOOK_DEPTH` in the notebook to match the number of levels in your data (for example, 10 if you have levels 00–09). The data should be sorted by `symbol` and `ts_event`; the notebook does this automatically after loading.

## Usage

1. **Set parameters** at the top of the notebook:
   - `CSV_FILE`: Path to your CSV data file.  
   - `TIME_INTERVAL`: Time bin size (e.g., `'1S'` for 1 second, `'5S'`, `'1Min'`, etc.).  
   - `BOOK_DEPTH`: Number of LOB levels present in the data.  

3. **Run all cells** in order. The notebook workflow:
    - Loads the CSV and sorts by symbol and timestamp.  
    - For each symbol, computes event-level OFI at each book level with `compute_event_ofi_one_stock`.  
    - Aggregates the OFI values into the specified time intervals (`time_bin`).  
    - Computes additional features:  
      - **Best_Level_OFI**: OFI at the best bid/ask (level 1).  
      - **Multi_Level_Sum**: Sum of OFI across all levels.  
      - **Integrated_OFI**: A single OFI value (per symbol per bin) obtained by PCA on the multi-level OFIs (captures the main imbalance direction).  
      - **Cross_Asset_OFI**: For each symbol, the sum of other symbols’ integrated OFI at the same time (market-wide pressure).  

After running, the final result is a pandas DataFrame named `agg`, with one row per time bin per symbol. Columns include:  
```
time_bin, symbol, Best_Level_OFI, Multi_Level_Sum, Integrated_OFI, Cross_Asset_OFI, OFI_L1, ..., OFI_L<BOOK_DEPTH>
```
You can save this DataFrame (e.g. `agg.to_csv('ofi_features.csv')`) or use it for further analysis.

## Further Exploration

- **Adjust parameters**: Try different `TIME_INTERVAL` or `BOOK_DEPTH` settings to see how the OFI features change.    
- **Broaden assets**: Run the notebook on additional symbols or asset classes and examine cross-asset imbalances.  
- **Backtesting**: Use the computed OFI features in a trading strategy or machine-learning model.  
- **Real-time deployment**: Adapt the logic for live data feeds to compute OFI on the fly.


==================================================
