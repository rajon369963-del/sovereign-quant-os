# ⚡ [QUANT-SOURCE-182] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_182_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Flow_Imbalances-AAPL- (`WHEEL_Order_Flow_Imbalances-AAPL-`)
- **Full Name**: `Order_Flow_Imbalances-AAPL-`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Order Flow Imbalance (OFI) Analysis

Hey there! Welcome to my GitHub repo for my Order Flow Imbalance (OFI) Analysis project. I had a ton of fun diving into high-frequency trading data for AAPL and building features to explore market dynamics. This project features a Jupyter Notebook with OFI calculations, some awesome visualizations, and a LaTeX report tackling key conceptual questions. I’m stoked to share this work—it’s a deep dive into how order flow shapes financial markets, and I hope you find it as exciting as I do!

## What’s This Project About?
This project analyzes Order Flow Imbalance (OFI) using a high-frequency limit order book dataset for AAPL (`first_25000_rows.csv`). I implemented three OFI features—Best-Level, Multi-Level, and Integrated OFI—and used visualizations to uncover their relationship with price movements. I also explored three conceptual questions in a LaTeX report, explaining why multi-level OFI rocks, the power of Lasso regression, and how OFI outshines trade volume for predicting short-term returns. As a bonus, I studied the paper *"Optimal Order Placement in Limit Order Markets"* by Cont and Kukanov to deepen my understanding of smart order routing (no separate deliverables for that part).

## Repository Structure
Here’s how the repo is organized:
- `data/`: Holds the input dataset (`first_25000_rows.csv`).
- `src/`: Contains my Jupyter Notebook (`ofi_analysis.ipynb`), where all the OFI calculations and plots come to life.
- `output/`: Stores the computed OFI data (`ofi_features.csv`) and visualization files (PNG plots: `ofi_time_series.png`, `ofi_returns_scatter.png`, `ofi_distribution.png`).
- `doc/`: Includes my LaTeX report (`conceptual_answers.tex`) and the compiled PDF (`conceptual_answers.pdf`) for the conceptual questions.
- `README.md`: This file, giving you the full scoop on the project!


## How to Run the Code
Getting this project up and running is a breeze. Here’s what to do:

1. **Clone the Repository**:
   ```bash
   git clone gh repo clone prashantsonibps/Order_Flow_Imbalances-AAPL-


==================================================


## [2/3] Repository: TapeFlow (`WHEEL_TapeFlow`)
- **Full Name**: `TapeFlow`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# TapeFlow

![TapeFlow v2](./docs/tapeflow_v2.png)

A trading terminal for reading order flow on crypto markets. It shows the tape, footprint charts, a DOM ladder, CVD, volume profile, open interest and liquidations, flags whale trades and spoofing, and lets you paper trade against live prices. It can run against live Binance data or against a local C++ matching engine that simulates a market, and the UI does not care which one it is talking to.

I built it because the tools I wanted to learn tape reading on were either paid or ran on a single symbol. This runs in a browser on anything.

## What is in it

- Time and Sales tape with whale trade highlighting
- Footprint charts with a volume heatmap
- DOM ladder with bid/ask imbalance detection
- Cumulative volume delta overlay
- Volume profile with point of control
- Open interest and liquidation views
- Signal detection for whale trades, velocity surges, spoofing and walls
- Sound and desktop alerts with cooldowns
- Paper trading with slippage, fees, stop loss, take profit, position and daily loss limits
- Session stats (VWAP, high/low, delta)
- Dockable layout you can rearrange and save
- A few color themes

## How it is put together

```
Binance WebSocket
    |
    v
backend/  Node proxy on :3001
    |     normalizes trades, aggregates the book, tracks OI and liquidations
    v
frontend/ React on :5173
    |
    +-- services/dataBuffer.ts   ring buffer, last 5000 trades per symbol, subscriber callbacks
    +-- components/              TapeTable, FootprintChart, DOMLadder, CVDOverlay, VolumeProfile,
    |                            OIMonitor, LiquidationHeatmap, AlgoSignals, ExecutionPanel, SessionStats
    +-- paper/                   PaperTradingEngine + risk checks
    +-- engine/                  canvas layers driven by one requestAnimationFrame loop
    +-- analytics/               OPS, CVD, spread, OBI, iceberg and liquidity-zone calculators
```

Trades go into a mutable ring buffer and components subscribe to it directly. At a few hundred trades per second, pushing every trade through React state made the UI stutter, so the hot path skips React entirely and only the canvas layers redraw.

Everything in `analytics/` is plain TypeScript with no React imports, so the calculators are easy to test on their own.

### Signals

| Signal | How it is detected | Default threshold |
| --- | --- | --- |
| Whale trade | single trade notional | > $50K (> $250K on BTC) |
| Velocity surge | trades/sec vs the 30s average | > 300% |
| Wall | large resting size at one level | > $100K |
| Spoof | large order pulled before it fills | > $50K removed |
| Imbalance | bid/ask size ratio at a level | > 3:1 |

### Paper trading

Market and limit orders, long/short positions, average entry, realized and unrealized P&L. Fills are simulated against the real L1 with configurable slippage and fees. Risk checks reject orders that would break the max order size, max position size, max open positions or daily loss limit, and positions can carry a stop loss and take profit.

## Running it

You need Node 18+.

```bash
git clone https://github.com/ianfigueroa/TapeFlow.git
cd TapeFlow

cd backend && npm install && npm run dev      # terminal 1
cd frontend && npm install && npm run dev     # terminal 2
```

Open http://localhost:5173.

`npm run build` in either folder produces a production build. `docker-compose up -d` runs the backend, an nginx-served frontend and Titan together.

### Titan

The backend can pull VWAP, book imbalance and whale alerts from [Titan](https://github.com/ianfigueroa/Titan), a C++ market data engine, instead of computing them in JavaScript. Set `TITAN_WS_URL=ws://titan:9001` (or run `docker pull ghcr.io/ianfigueroa/titan:latest`). The header shows "Titan Connected" when it is up; if it is not, TapeFlow falls back to its own calculators.

### Backend proxy routes

The backend proxies a few Binance Futures REST calls so the browser does not hit CORS:

- `/api/binance/openInterest`
- `/api/binance/longShortRatio`
- `/api/binance/premiumIndex`

## Keyboard

| Key | Action |
| --- | --- |
| Space | pause/resume the tape |
| S | focus symbol search |
| A | toggle alerts panel |
| ? | shortcut list |
| R | clear trades |
| 1-9 | switch symbol tab |
| Ctrl+W | close tab |

## The C++ engine (cpp-engine/)

`cpp-engine/` is a small matching engine plus a market simulator that TapeFlow can use instead of a live feed. The order book is price-time priority and is guarded by a mutex (it is not lock-free). The simulator drives it with an Ornstein-Uhlenbeck price process and a mix of trader types, and there is a header-only RFC 6455 WebSocket server (hand-written SHA-1 and Base64 for the handshake, no dependencies) that streams book telemetry to the frontend.

```bash
cd cpp-engine
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release
./build/hyperion            # demo, then the built-in 1M orders/sec simulator benchmark, then the telemetry server
```

The built-in benchmark is paced by the simulator and tops out around 1M orders/sec by design. To measure the order book itself:

```bash
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DHYPERION_BUILD_BENCHMARKS=ON
cmake --build build --target bench_orderbook
./build/bench_orderbook
```

On a Ryzen 9 8945HS with MinGW g++ 15 `-O3 -march=native`, run with nothing else on the machine, that gives roughly 2.1 to 2.3M mixed add/cancel/match ops per second and about 4.3M add-only inserts per second. Numbers move with the CPU and with whatever else is running; treat them as a ballpark, not a spec.

See `cpp-engine/README.md` for the simulator parameters.

## Stack

React 18, TypeScript, Vite, Zustand, Tailwind, flexlayout-react, @tanstack/react-virtual, TradingView lightweight-charts, Node + Express + ws, C++20 for the engine.

## License

MIT

### Core Implementation Code & Architecture
#### File: `frontend/tsconfig.node.json`
```python
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
```

#### File: `backend/tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "lib": ["ES2020"],
    "outDir": "./dist",
    "rootDir": ".",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "moduleResolution": "node"
  },
  "include": ["./**/*.ts"],
  "exclude": ["node_modules", "dist"]
}
```

#### File: `frontend/tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2020",
    "useDefineForClassFields": true,
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx",
    "strict": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noFallthroughCasesInSwitch": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["src"],
  "exclude": ["src/**/__tests__/**", "src/**/*.test.ts", "src/**/*.test.tsx"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
```

#### File: `backend/package.json`
```python
{
  "name": "market-dashboard-backend",
  "version": "1.0.0",
  "description": "Real-time market data backend server",
  "main": "dist/server.js",
  "scripts": {
    "dev": "tsx watch server.ts",
    "build": "tsc",
    "start": "node dist/server.js",
    "lint": "eslint . --ext .ts"
  },
  "dependencies": {
    "axios": "^1.6.2",
    "cors": "^2.8.5",
    "dotenv": "^16.3.1",
    "express": "^4.18.2",
    "ws": "^8.14.2"
  },
  "devDependencies": {
    "@types/cors": "^2.8.17",
    "@types/express": "^4.17.21",
    "@types/node": "^20.10.4",
    "@types/ws": "^8.5.10",
    "@typescript-eslint/eslint-plugin": "^6.14.0",
    "@typescript-eslint/parser": "^6.14.0",
    "eslint": "^8.55.0",
    "tsx": "^4.6.2",
    "typescript": "^5.3.3"
  }
}
```

#### File: `frontend/package.json`
```python
{
  "name": "market-dashboard-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "lint": "eslint . --ext ts,tsx --report-unused-disable-directives --max-warnings 0",
    "preview": "vite preview"
  },
  "dependencies": {
    "@tanstack/react-virtual": "^3.13.18",
    "clsx": "^2.0.0",
    "flexlayout-react": "^0.8.18",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "tailwind-merge": "^2.1.0",
    "zustand": "^4.4.7"
  },
  "devDependencies": {
    "@types/react": "^18.2.43",
    "@types/react-dom": "^18.2.17",
    "@typescript-eslint/eslint-plugin": "^6.14.0",
    "@typescript-eslint/parser": "^6.14.0",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.16",
    "eslint": "^8.55.0",
    "eslint-plugin-react-hooks": "^4.6.0",
    "eslint-plugin-react-refresh": "^0.4.5",
    "postcss": "^8.4.32",
    "tailwindcss": "^3.3.6",
    "typescript": "^5.3.3",
    "vite": "^5.0.8"
  }
}
```

#### File: `cpp-engine/include/order.hpp`
```python
// Order struct - optimized for cache efficiency (32 bytes)

#pragma once

#include <cstdint>

namespace hyperion {

enum class Side : uint8_t {
    BID = 0,
    ASK = 1
};

// Packed struct for memory efficiency
// Total: 32 bytes (cache-line friendly)
struct Order {
    uint64_t id;           // Unique order ID
    uint64_t timestamp;    // Nanosecond timestamp
    double   price;        // Limit price
    double   quantity;     // Remaining quantity
    Side     side;         // Bid or Ask
    uint8_t  padding[7];   // Align to 32 bytes
    
    Order() = default;
    
    Order(uint64_t id_, Side side_, double price_, double qty_, uint64_t ts_)
        : id(id_), timestamp(ts_), price(price_), quantity(qty_), side(side_) {}
    
    bool isBid() const { return side == Side::BID; }
    bool isAsk() const { return side == Side::ASK; }
    bool isFilled() const { return quantity <= 0.0; }
};

// Trade result from matching
struct Trade {
    uint64_t bidOrderId;
    uint64_t askOrderId;
    double   price;
    double   quantity;
    uint64_t timestamp;
};

} // namespace hyperion
```


==================================================


## [3/3] Repository: Work-Trial-Task-Cross-Impact-Analysis-of-Order-Flow-Imbalance-OFI- (`WHEEL_Work-Trial-Task-Cross-Impact-Analysis-of-Order-Flow-Imbalance-OFI-`)
- **Full Name**: `Work-Trial-Task-Cross-Impact-Analysis-of-Order-Flow-Imbalance-OFI-`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Work-Trial-Task-Cross-Impact-Analysis-of-Order-Flow-Imbalance-OFI-

python package: pandas  numpy statsmodels sklearn.linear_model  warnings
I create a ofi.py file which implements the caculation method of OFI, plz import it as a package when you run the script

Run the contemporaneous.py and future.py scripts you can get the refression results and the ofi data(stockname_combined.csv)

There is no data prepossessing file and you can find that in each scripts, there are the input data to load the data. 

Since the data file is quite large, I would show the example of original data file that may be used in this project

example dataname: AAPL20241230.csv
and you can download the data from the Databento




> reference:  Rama Cont, Mihai Cucuringu & Chao Zhang (2023) Cross-impact of
 order flow imbalance in equity markets, Quantitative Finance, 23:10, 1373-1393, DOI:10.1080/14697688.2023.2236159

### Core Implementation Code & Architecture
#### File: `scripts/ofi.py`
```python
import pandas as pd 
import numpy as np 
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler

class OFI_implement:
    def __init__(self, level: int, freq: str):
        self.level = level
        self.freq = freq
    def ofi_implement(data: pd.DataFrame, level: int, freq: str):
        ## compute OFI
        
        ask_sz = [f'ask_sz_{i:02}' for i in range(1, level+1)]
        bid_sz = [f'bid_sz_{i:02}' for i in range(1, level+1)]
        ask_px = [f'ask_px_{i:02}' for i in range(1, level+1)]
        bid_px = [f'bid_px_{i:02}' for i in range(1, level+1)]

        # Create columns to store bOF and aOF
        for i in range(1, level + 1):
            data[f'bOF{i}'] = 0
            data[f'aOF{i}'] = 0

        # Calculate the bid and ask price difference matrix
        bid_px_diff = data[bid_px].diff().values  # bid_price differ value
        ask_px_diff = data[ask_px].diff().values  # ask_price differ value

        bid_sz_matrix = data[bid_sz].values
        ask_sz_matrix = data[ask_sz].values
        bid_sz_matrix_prev = np.roll(bid_sz_matrix, 1, axis=0)  # Previous values of the sliding window
        ask_sz_matrix_prev = np.roll(ask_sz_matrix, 1, axis=0)

        # Initialize bOF and aOF matrices
        bOF_matrix = np.zeros_like(bid_px_diff)
        aOF_matrix = np.zeros_like(ask_px_diff)

        # Calculate bOF (Order Flow Imbalance for buy orders)
        bOF_matrix[bid_px_diff > 0] = bid_sz_matrix[bid_px_diff > 0]  # bid price up
        bOF_matrix[bid_px_diff == 0] = bid_sz_matrix[bid_px_diff == 0] - bid_sz_matrix_prev[bid_px_diff == 0]  # bid pricve no change
        bOF_matrix[bid_px_diff < 0] = -bid_sz_matrix_prev[bid_px_diff < 0]  # bid price down

        # Calculate aOF (Order Flow Imbalance for sell orders)
        aOF_matrix[ask_px_diff > 0] = -ask_sz_matrix_prev[ask_px_diff > 0]  # ask price up
        aOF_matrix[ask_px_diff == 0] = ask_sz_matrix[ask_px_diff == 0] - ask_sz_matrix_prev[ask_px_diff == 0]  # ask price no change
        aOF_matrix[ask_px_diff < 0] = ask_sz_matrix[ask_px_diff < 0]  # ask price down

        # Update the DataFrame with the bOF and aOF matrix results
        for j in range(level):
            data[f'bOF{j + 1}'] = bOF_matrix[:, j]
            data[f'aOF{j + 1}'] = aOF_matrix[:, j]

        ## compute misprice
        data['midprice'] = (data['ask_px_01'] + data['bid_px_01']) / 2

        ## comupte size change in each time, for later agg operation, th sum of last_size before time t sould be equal to the size value at time t
        data['last_size'] = data['size'].diff().values
        data['last_size'][0] = data['size'][0]

        ## Integrated OFI, with PCA
        #freq = freq
        data['event_num'] = 1
        data_th = data.resample(freq).agg(
            {'action': 'last', 
             'side': 'last', 
             'depth': 'last', 
             'price': 'last', 
             'midprice': 'last',
             'last_size': 'sum',
             'aOF1': 'sum', 'aOF2': 'sum', 'aOF3': 'sum', 'aOF4': 'sum', 'aOF5': 'sum',
             'bOF1': 'sum', 'bOF2': 'sum', 'bOF3': 'sum', 'bOF4': 'sum', 'bOF5': 'sum',

            'ask_sz_01': 'sum', 'ask_sz_02': 'sum', 'ask_sz_03': 'sum', 'ask_sz_04': 'sum', 'ask_sz_05': 'sum',
            'bid_sz_01': 'sum', 'bid_sz_02': 'sum', 'bid_sz_03': 'sum', 'bid_sz_04': 'sum', 'bid_sz_05': 'sum',

            'event_num': 'sum', 'symbol': 'last', 'midprice': 'last'
                                    }).rename(columns={'last_size': 'size'})

        # x = x.loc[~(x == 0).all(axis=1)]
        data_th.dropna(inplace=True)
        data_th['returns'] = np.log(data_th['midprice']) - np.log(data_th['midprice'].shift(1))
        data_th['midprice_delta'] = data_th['midprice'] - data_th['midprice'].shift(1)

        ## Best-level OFI
        for i in range(1, level + 1): data_th[f'OFI{i}'] = data_th[f'bOF{i}'] - data_th[f'aOF{i}']

        ## Deeper-level OFI
        M = level
        Q = []
        for i in range(1, level+1): Q.append((data_th[f'ask_sz_{i:02}'] + data_th[f'bid_sz_{i:02}']) / 2 / data_th['event_num'])
        QM = sum(Q) / M
        for i in range(1, level + 1): data_th[f'ofi{i}'] = data_th[f'OFI{i}'] / QM

        ## Integrated OFI
        # data_th = data_th.replace([np.inf, -np.inf], np.nan).dropna()
        # X = data_th[[f'ofi{i}' for i in range(1, level+1)]]
        # pca = PCA(n_components=1)
        # X_pca = pca.fit_transform(X)
        # ofiI = pd.Series(X_pca.flatten(), index=X.index)
        # standard_scaler = StandardScaler()
        # ofiI_standard = standard_scaler.fit_transform(np.array(ofiI).reshape(-1, 1))
        # data_th['ofiI'] = pd.Series(ofiI_standard.flatten(), index=X.index)

        ## Integrated OFI
        data_th = data_th.replace([np.inf, -np.inf], np.nan).dropna()
        X = data_th[[f'ofi{i}' for i in range(1, level + 1)]]
        X_standardized = (X - X.mean()) / X.std() 
        pca = PCA(n_components=1)  
        X_pca = pca.fit_transform(X_standardized)  
        w1 = pca.components_[0]  
        w1_normalized = w1 / np.sum(np.abs(w1))  
        ofiI = np.dot(X, w1_normalized)  
        standard_scaler = StandardScaler()
        ofiI_standard = standard_scaler.fit_transform(np.array(ofiI).reshape(-1, 1))
        data_th['ofiI'] = pd.Series(ofiI_standard.flatten(), index=X.index)

        return data_th, X_pca
```

#### File: `scripts/contemporaneous.py`
```python
#%%Import libraries
import pandas as pd 
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from datetime import *
import matplotlib.ticker as mtk
from ofi import OFI_implement
import warnings
warnings.filterwarnings("ignore") 

#%% Function
## Price impact of best-level OFIs
def PI(data, object, window_length='30min'):
    #object = OFI1/ ofiI
    regression_results = []
    # get the data for each window
    grouped_data = data.resample(window_length)
    # run regression for each window
    for window_start, window_data in grouped_data:
        
        if len(window_data) < 2:
            continue
        
        X = window_data[f'{object}']
        y = window_data['returns']
        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        # store the regression results
        regression_results.append({
            'window_start': window_start,
            'window_end': window_start + pd.Timedelta(window_length),
            'params': model.params,            # model parameters
            'r_squared': model.rsquared,       # R^2 value
            'p_values': model.pvalues,         # Pvalues
            'summary': model.summary().as_text()  # regression summary
        })

    results_df = pd.DataFrame(regression_results)
    return results_df




 ##Cross-impact of best-level OFI

def CI(data, object, stock_list,stock_name, window_length='30min'):
    #object = 'OFI'/ 'ofiI'
    data = data[['returns', f'{object}','symbol']]
    data = data.set_index('symbol', append = True).unstack(level='symbol')
    #since the number of event in one 
    
    #data.dropna(inplace=True)
    #print(data.isnull().sum())
    data = data.fillna(0)
    regression_results = []
    # get the data for each window
    grouped_data = data.resample(window_length)
    # run regression for each window
    for window_start, window_data in grouped_data:
        
        if len(window_data) < 2:
            continue
        #window_data = window_data.set_index('symbol', append = True).unstack(level='symbol')
        return_col = [f'returns_{i}' for i in stock_list]
        ofi_col = [f'{object}_{i}' for i in stock_list]
        window_data.columns = return_col + ofi_col
        ofi_col_copy = ofi_col.copy()
        # ofi_col_copy.remove(f'{object}_{stock_name}')

        y = window_data[f'returns_{stock_name}']
        X = window_data[ofi_col_copy]
        
        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        # store the regression results
        regression_results.append({
            'window_start': window_start,
            'window_end': window_start + pd.Timedelta(window_length),
            'params': model.params,            # model parameters
            'r_squared': model.rsquared,       # R^2 value
            'p_values': model.pvalues,         # Pvalues
            'summary': model.summary().as_text()  # regression summary
        })

    results_df = pd.DataFrame(regression_results)
    return results_df

 
def decorateAx(ax, xs, ys):

    def x_fmt_func(x, pos=None):
        idx = np.clip(int(x + 0.5), 0, len(xs) - 1)
        return xs[idx]
    idx_pxy = np.arange(len(xs))
    ax.plot(idx_pxy, ys, linewidth=1, linestyle="-")
    ax.plot(ax.get_xlim(), [0, 0], color="blue", linewidth=0.5, linestyle="--")
    ax.xaxis.set_major_formatter(mtk.FuncFormatter(x_fmt_func))
    ax.grid(True)
    return







#%%Load data
time_range = ['20241230', '20241231', '20250102', '20250103', '20250106', '20250107']
stock_list = ['JPM', 'TSLA', 'XOM', 'AMGN', 'AAPL']


alldata = {}

for stock in stock_list:
    combined_data = pd.DataFrame()  
    for date in time_range:
        
        file_name = f"../data/{stock}{date}.csv"
        try:
           
            chunks = pd.read_csv(file_name, chunksize=100000)
            for chunk in chunks:
                
                chunk = chunk.drop(columns=['ts_recv', 'rtype', 'publisher_id', 'instrument_id', 'flags'], errors='ignore')
                
                chunk = chunk.drop(columns=[col for col in chunk.columns 
                                             if any(char.isdigit() for char in col) 
                                             and (int(''.join(filter(str.isdigit, col))) > 5 
                                                  or int(''.join(filter(str.isdigit, col))) == 0)], errors='ignore')
                
                chunk.fillna(0, inplace=True)
                chunk.set_index('ts_event', inplace=True)  
                print(chunk.head())
                chunk.index = pd.to_datetime(chunk.index) 
                chunk, X_pac = OFI_implement.ofi_implement(chunk, 5, '1min')
                
                
                combined_data = pd.concat([combined_data, chunk])
        except Exception as e:
            print(f"Cannot read the {file_name}: {e}")
    
    combined_data.to_csv(f"../results/{stock}_combined.csv")
    alldata[stock] = combined_data
    print(combined_data.head(5))

datapool = alldata.copy()  


#%% PI and PII
PI_result = {}
PII_result = {}

for stock_name in stock_list:
  result1 = PI(datapool[stock_name], 'OFI1',window_length='30min')
  result2 = PI(datapool[stock_name], 'ofiI',window_length='30min')
  result1.to_csv(f"../results/{stock_name}_PI_result.csv")
  result2.to_csv(f"../results/{stock_name}_PII_result.csv")
  PI_result[stock_name] = result1
  PII_result[stock_name] = result2

#%% CI and CII
combined_data = []
for stock_name, data in datapool.items():
    data['symbol'] = stock_name
    combined_data.append(data)
combined_data = pd.concat(combined_data, axis=0)

CI_result = {}
for stock_name in stock_list:
  result = CI(combined_data, 'OFI1', stock_list, stock_name, window_length='30min')
  result.to_csv(f"../results/{stock_name}_CI_result.csv")
  CI_result[stock_name] = result

CII_result = {}
for stock_name in stock_list:
  result = CI(combined_data, 'ofiI',stock_list, stock_name, window_length='30min')
  result.to_csv(f"../results/{stock_name}_CII_result.csv")
  CII_result[stock_name] = result

# %%
PImean = []
for stock_name in stock_list:
    PImean.append(PI_result[stock_name]['r_squared'].mean())
PImean
# %%
```

#### File: `scripts/Contemporaneous cross-impact of OFI.py`
```python
#%%Import libraries
import pandas as pd 
import numpy as np
import statsmodels.api as sm
from ofi import OFI_implement
import warnings
warnings.filterwarnings("ignore") 

#%% Function
## Price impact of best-level OFIs
def PI(data, window_length='30min'):
    regression_results = []
    # get the data for each window
    grouped_data = data.resample(window_length)
    # run regression for each window
    for window_start, window_data in grouped_data:
        
        if len(window_data) < 2:
            continue
        
        X = window_data['OFI1']
        y = window_data['returns']
        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        # store the regression results
        regression_results.append({
            'window_start': window_start,
            'window_end': window_start + pd.Timedelta(window_length),
            'params': model.params,            # model parameters
            'r_squared': model.rsquared,       # R^2 value
            'p_values': model.pvalues,         # Pvalues
            'summary': model.summary().as_text()  # regression summary
        })

    results_df = pd.DataFrame(regression_results)
    return results_df


#Price impact of integrated OFIs
def PII(data, window_length='30min'):
    regression_results = []
    # get the data for each window
    grouped_data = data.resample(window_length)
    # run regression for each window
    for window_start, window_data in grouped_data:
        
        if len(window_data) < 2:
            continue
        
        X = window_data['ofiI']
        y = window_data['returns']
        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        # store the regression results
        regression_results.append({
            'window_start': window_start,
            'window_end': window_start + pd.Timedelta(window_length),
            'params': model.params,            # model parameters
            'r_squared': model.rsquared,       # R^2 value
            'p_values': model.pvalues,         # Pvalues
            'summary': model.summary().as_text()  # regression summary
        })

    results_df = pd.DataFrame(regression_results)
    return results_df


 ##Cross-impact of best-level OFI

def CI(data, stock_list,stock_name, window_length='30min'):
    data = data[['returns', 'OFI1','symbol']]
    data = data.set_index('symbol', append = True).unstack(level='symbol')
    #since the number of event in one 
    
    #data.dropna(inplace=True)
    #print(data.isnull().sum())
    data = data.fillna(0)
    regression_results = []
    # get the data for each window
    grouped_data = data.resample(window_length)
    # run regression for each window
    for window_start, window_data in grouped_data:
        
        if len(window_data) < 2:
            continue
        #window_data = window_data.set_index('symbol', append = True).unstack(level='symbol')
        return_col = [f'returns_{i}' for i in stock_list]
        ofi_col = [f'OFI_{i}' for i in stock_list]
        window_data.columns = return_col + ofi_col
        ofi_col_copy = ofi_col.copy()
        ofi_col_copy.remove(f'OFI_{stock_name}')

        y = window_data[f'returns_{stock_name}']
        X = window_data[ofi_col_copy]
        
        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        # store the regression results
        regression_results.append({
            'window_start': window_start,
            'window_end': window_start + pd.Timedelta(window_length),
            'params': model.params,            # model parameters
            'r_squared': model.rsquared,       # R^2 value
            'p_values': model.pvalues,         # Pvalues
            'summary': model.summary().as_text()  # regression summary
        })

    results_df = pd.DataFrame(regression_results)
    return results_df

 ##Cross-impact of integrated OFIs

def CII(data, stock_list,stock_name, window_length='30min'):
    data = data[['returns', 'OFI1','symbol']]
    data = data.set_index('symbol', append = True).unstack(level='symbol')
    #since the number of event in one 
    #print(data.isnull().sum())
    data = data.fillna(0)
    regression_results = []
    # get the data for each window
    grouped_data = data.resample(window_length)
    # run regression for each window
    for window_start, window_data in grouped_data:
        
        if len(window_data) < 2:
            continue
        #window_data = window_data.set_index('symbol', append = True).unstack(level='symbol')
        return_col = [f'returns_{i}' for i in stock_list]
        ofiI_col = [f'ofiI_{i}' for i in stock_list]
        window_data.columns = return_col + ofiI_col
        ofiI_col_copy = ofiI_col.copy()
        ofiI_col_copy.remove(f'ofiI_{stock_name}')

        y = window_data[f'returns_{stock_name}']
        X = window_data[ofiI_col_copy]
        
        X = sm.add_constant(X)

        model = sm.OLS(y, X).fit()

        # store the regression results
        regression_results.append({
            'window_start': window_start,
            'window_end': window_start + pd.Timedelta(window_length),
            'params': model.params,            # model parameters
            'r_squared': model.rsquared,       # R^2 value
            'p_values': model.pvalues,         # Pvalues
            'summary': model.summary().as_text()  # regression summary
        })

    results_df = pd.DataFrame(regression_results)
    return results_df






#%%Load data
stock_list = ["AAPL","MSFT","NVDA","AMGN","GILD","TSLA","PEP","JPM", "V", "XOM"]
datapool = {}

# Loop through each stock's data and store it in the data pool
for stock_name in stock_list:
    file_path = f'../data/{stock_name}20250102_after.csv'  # file path
    data = pd.read_csv(file_path, index_col=0)            
    data.index = pd.to_datetime(data.index)              
    datapool[stock_name] = data

# Get the OFI data for each stock
for stock_name in stock_list:
    data, X_pac = OFI_implement.ofi_implement(datapool[stock_name], 5, '1min')
    datapool[stock_name] = data      


#%% PI and PII
PI_result = {}
PII_result = {}

for stock_name in stock_list:
  result1 = PI(datapool[stock_name], window_length='30min')
  result2 = PII(datapool[stock_name], window_length='30min')
  PI_result[stock_name] = result1
  PII_result[stock_name] = result2

#%% CI and CII
combined_data = []
for stock_name, data in datapool.items():
    data['symbol'] = stock_name
    combined_data.append(data)
combined_data = pd.concat(combined_data, axis=0)

CI_result = {}
for stock_name in stock_list:
  result = CI(combined_data, stock_list, stock_name, window_length='30min')
  CI_result[stock_name] = result

CII_result = {}
for stock_name in stock_list:
  result = CII(combined_data, stock_list, stock_name, window_length='30min')
  CII_result[stock_name] = result
# %%
```

#### File: `scripts/future.py`
```python
#%% import library
import pandas as pd 
import numpy as np
import statsmodels.api as sm
from ofi import OFI_implement
from sklearn.linear_model import LinearRegression
import warnings
warnings.filterwarnings("ignore")

#%% Function
def FPI(data, object, forecast_horizon, lags):
    # object = OFI1 or ofiI
    # Rolling window setup
    train_window = 30  # Length of the training set: 30 minutes
    test_window = forecast_horizon  # Test set length equals the future horizon
    step = 1  # Rolling step size: 1 minute

    # Initialize storage for results
    time_ranges = []
    actuals = []
    predictions = []
    r2_out_values = []

    # Rolling window loop
    for start in range(0, len(data) - train_window - test_window, step):
        # Define the range for training and testing
        train_start = start
        train_end = start + train_window
        test_start = train_end
        test_end = train_end + test_window

        # Split into training and testing sets
        train = data.iloc[train_start:train_end]
        test = data.iloc[test_start:test_end]

        # Define features and target variables
        X_train = train[[f'{object}_lag_{lag}' for lag in lags]]
        y_train = train[f'freturns_{forecast_horizon}']
        X_test = test[[f'{object}_lag_{lag}' for lag in lags]]
        y_test = test[f'freturns_{forecast_horizon}']

        # Train the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Calculate out-of-sample R^2
        historical_mean = np.mean(train[f'freturns_{forecast_horizon}'])  # Baseline model: historical mean
        r2_out = 1 - np.sum((y_test - y_pred) ** 2) / np.sum((y_test - historical_mean) ** 2)

        # Store results
        time_ranges.append({
            "train_start": train.index[0],
            "train_end": train.index[-1],
            "test_start": test.index[0],
            "test_end": test.index[-1]
        })
        actuals.append(list(y_test.values))  # Store as a list for each test window
        predictions.append(list(y_pred))  # Store as a list for each test window
        r2_out_values.append(r2_out)

    # Flatten actuals and predictions for evaluation
    actuals_flat = [val for sublist in actuals for val in sublist]
    predictions_flat = [val for sublist in predictions for val in sublist]

    # Convert results into a DataFrame
    results = pd.DataFrame({
        'Train_Start': [time_range['train_start'] for time_range in time_ranges],
        'Train_End': [time_range['train_end'] for time_range in time_ranges],
        'Test_Start': [time_range['test_start'] for time_range in time_ranges],
        'Test_End': [time_range['test_end'] for time_range in time_ranges],
        'Out_of_Sample_R2': r2_out_values
    })

    # Add actuals and predictions (as lists) for each test window
    results['Actual'] = actuals
    results['Predicted'] = predictions

    # Print the first 10 rows of results
    return results




def FCI(inputdata, stock_list, object, train_window = 30, test_window = 5, step_window = 1, target_stock = 'AAPL'): 
    # object = OFI1 or ofiI
    data = inputdata
    # Set MultiIndex on 'ts_event' and 'symbol', and sort it
    data = data.set_index('symbol', append = True).sort_index()
    #data = data.set_index(['ts_event', 'symbol']).sort_index()
    # print(data.head(10))
    lags = [1,2,3,5,10,20,30]
    # for lag in lags:
    #     data[f'OFI1_lag_{lag}'] = data.groupby('symbol')['OFI1'].shift(lag)
    # data.fillna(0, inplace=True)
    #data.dropna(inplace=True)
    #lags = [1,2,3,5]
    # Rolling window setup

    train_window = train_window  # Training set size (number of minutes)
    test_window = test_window  # Test set size (number of minutes)
    step = step_window  # Rolling step size (1 minute)

    # Initialize storage for results
    time_ranges = []
    actuals = []
    predictions = []
    r2_out_values = []
    models = []
    # Rolling window loop
    for start in range(0, len(data.index.levels[0]) - train_window - test_window, step):
        # Define the training and testing time ranges
        train_start = data.index.levels[0][start]
        train_end = data.index.levels[0][start + train_window]
        test_start = data.index.levels[0][start + train_window]
        test_end = data.index.levels[0][start + train_window + test_window]

        # Select training and testing sets
        train = data.loc[train_start:train_end]
        test = data.loc[test_start:test_end]

        # Define the target stock (e.g., 'AAPL')
        target_stock = 'AAPL'

        # Check if the target stock is in both the training and testing sets
        if target_stock not in train.index.get_level_values('symbol') or target_stock not in test.index.get_level_values('symbol'):
            print(f"Target stock '{target_stock}' not found in train or test set. Skipping this window.")
            continue

        # Dependent variable: Future returns of the target stock
        # y_train = train.xs(target_stock, level='symbol')['Future_Returns']
        # y_test = test.xs(target_stock, level='symbol')['Future_Returns']
        y_train = train.xs(target_stock, level='symbol')[f'freturns_{test_window}']
        y_test = test.xs(target_stock, level='symbol')[f'freturns_{test_window}']

        # Independent variables: Lagged OFI values of all stocks
        # Include both AAPL and MSFT lagged features explicitly
        X_train = train[[f'{object}_lag_{lag}' for lag in lags]].xs(target_stock, level='symbol')
        X_test = test[[f'{object}_lag_{lag}' for lag in lags]].xs(target_stock, level='symbol')

        # Add cross-stock lags (e.g., MSFT lags for predicting AAPL)
        # other_stock = 'MSFT' if target_stock == 'AAPL' else 'AAPL'
        # for lag in lags:
        #     X_train[f'{other_stock}_OFI_lag_{lag}'] = train[[f'OFI_lag_{lag}']].xs(other_stock, level='symbol')
        #     X_test[f'{other_stock}_OFI_lag_{lag}'] = test[[f'OFI_lag_{lag}']].xs(other_stock, level='symbol')


         # 获取其他股票列表（除去 target_stock）
        other_stocks = [stock for stock in stock_list if stock != target_stock]

        # 添加其他股票的滞后特征
        for other_stock in other_stocks:
            if other_stock in train.index.get_level_values('symbol'):
                for lag in lags:
                    X_train[f'{other_stock}_{object}_lag_{lag}'] = train[[f'{object}_lag_{lag}']].xs(other_stock, level='symbol')
            if other_stock in test.index.get_level_values('symbol'):
                for lag in lags:
                    X_test[f'{other_stock}_{object}_lag_{lag}'] = test[[f'{object}_lag_{lag}']].xs(other_stock, level='symbol')
        


        # Handle missing values
        X_train = X_train.dropna()  # Drop rows with NaN in X_train
        y_train = y_train.loc[X_train.index]  # Align y_train with X_train

        X_test = X_test.dropna()  # Drop rows with NaN in X_test
        y_test = y_test.loc[X_test.index]  # Align y_test with X_test

        # X_train = sm.add_constant(X_train)
        # X_test = sm.add_constant(X_test)


        print("X_train shape:", X_train.shape)
        print("X_test shape:", X_test.shape)
        
        # Train the model
        if len(X_train) == 0 or len(X_test) == 0:  # Ensure no empty datasets
            print(f"Empty train or test set after handling NaNs. Skipping this window.")
            continue
        #print(y_train)

        model = LinearRegression()
        model.fit(X_train, y_train)
        # model = sm.OLS(y_train, X_train).fit()
        #print(model.summary())
        # Predict future returns on the test set
        if X_train.shape[1] != X_test.shape[1]: break
        y_pred = model.predict(X_test)

        # Out-of-sample R^2 calculation
        historical_mean = np.mean(y_train)  # Baseline: Historical mean
        r2_out = 1 - np.sum((y_test - y_pred) ** 2) / np.sum((y_test - historical_mean) ** 2)

        # Store time ranges
        time_ranges.append({
            "train_start": train.index.get_level_values('ts_event')[0],
            "train_end": train.index.get_level_values('ts_event')[-1],
            "test_start": test.index.get_level_values('ts_event')[0],
            "test_end": test.index.get_level_values('ts_event')[-1]
        })

        # Store actual and predicted values
        actuals.append(list(y_test.values))
        predictions.append(list(y_pred))
        r2_out_values.append(r2_out)
        models.append(model)
    # Convert results to a DataFrame
    results = pd.DataFrame({
        'Train_Start': [time_range['train_start'] for time_range in time_ranges],
        'Train_End': [time_range['train_end'] for time_range in time_ranges],
        'Test_Start': [time_range['test_start'] for time_range in time_ranges],
        'Test_End': [time_range['test_end'] for time_range in time_ranges],
        # 'model_summary': [model.summary() for model in models],
        'Out_of_Sample_R2': r2_out_values,
        'Target_Stock': target_stock
    })

    # Add actuals and predictions (as lists)
    results['Actual'] = actuals
    results['Predicted'] = predictions

    # Display results
    return results



#%% Data Preparation
time_range = ['20241230', '20241231', '20250102', '20250103', '20250106', '20250107']
stock_list = ['JPM', 'TSLA', 'XOM', 'AMGN', 'AAPL']


alldata = {}

for stock in stock_list:
    combined_data = pd.DataFrame()  
    for date in time_range:
        
        file_name = f"../data/{stock}{date}.csv"
        try:
           
            chunks = pd.read_csv(file_name, chunksize=100000)
            for chunk in chunks:
                
                chunk = chunk.drop(columns=['ts_recv', 'rtype', 'publisher_id', 'instrument_id', 'flags'], errors='ignore')
                
                chunk = chunk.drop(columns=[col for col in chunk.columns 
                                             if any(char.isdigit() for char in col) 
                                             and (int(''.join(filter(str.isdigit, col))) > 5 
                                                  or int(''.join(filter(str.isdigit, col))) == 0)], errors='ignore')
                
                chunk.fillna(0, inplace=True)
                chunk.set_index('ts_event', inplace=True)  
                print(chunk.head())
                chunk.index = pd.to_datetime(chunk.index) 
                chunk, X_pac = OFI_implement.ofi_implement(chunk, 5, '1min')
                
                
                combined_data = pd.concat([combined_data, chunk])
        except Exception as e:
            print(f"Cannot read the {file_name}: {e}")
    
    
    alldata[stock] = combined_data
    print(combined_data.head(5))

datapool = alldata.copy()


Lags = [1,2,3,5,10,20,30]
forecast_horizon = 5
for stock_name in stock_list:
    datapool[stock_name][f'freturns_{forecast_horizon}'] = (
    np.log(datapool[stock_name]['midprice'].shift(-forecast_horizon)) - np.log(datapool[stock_name]['midprice'])
)
    # define lag OFI
    L = Lags
    for l in L:
        datapool[stock_name][f'OFI1_lag_{l}'] = datapool[stock_name]['OFI1'].shift(l)  
        datapool[stock_name][f'ofiI_lag_{l}'] = datapool[stock_name]['ofiI'].shift(l) 
    datapool[stock_name] = datapool[stock_name].dropna()

combined_data = []


for stock_name, data in datapool.items():

    data['symbol'] = stock_name
 
    combined_data.append(data)

combined_data = pd.concat(combined_data, axis=0)
combined_data.head(10)


#%% FPI, and FPII

FPI_result = {}
for stock_name in stock_list:
    result = FPI(datapool[stock_name], 'OFI1',forecast_horizon, lags=Lags)
    result.to_csv(f"../results/{stock_name}_FPI_result.csv")
    FPI_result[stock_name] = result

FPII_result = {}
for stock_name in stock_list:
    result = FPI(datapool[stock_name], 'ofiI', forecast_horizon, lags=Lags)
    result.to_csv(f"../results/{stock_name}_FPII_result.csv")
    FPII_result[stock_name] = result
FPII_result['AAPL'].head(10)



#%% FCI, and FCII
FCI_result = {}
for stock_name in stock_list:
    result = FCI(combined_data, stock_list, 'OFI1',train_window = 30, test_window = forecast_horizon, step_window = 1, target_stock = stock_name)
    result.to_csv(f"../results/{stock_name}_FCI_result.csv")
    FCI_result[stock_name] = result
FCII_result = {}
for stock_name in stock_list:
    result = FCI(combined_data, stock_list, 'ofiI',train_window = 30, test_window = forecast_horizon, step_window = 1, target_stock = stock_name)
    result.to_csv(f"../results/{stock_name}_FCII_result.csv")
    FCII_result[stock_name] = result



# %%
```


==================================================
