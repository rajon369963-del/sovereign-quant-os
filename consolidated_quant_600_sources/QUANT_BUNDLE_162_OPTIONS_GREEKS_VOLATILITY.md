# ⚡ [QUANT-SOURCE-162] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_162_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: FX-Options-Dashboard (`PHASE4-QUANT-194`)
- **Full Name**: `PHASE4-QUANT-194_dmitrybudreyka__FX-Options-Dashboard`
- **Description**: A Python project for FX Options Trading and Financial Markets. It builds a synthetic EUR/USD implied volatility surface, prices European FX options with the Garman-Kohlhagen model, calculates Greeks, runs scenario analysis, and produces a simple delta-hedging recommendation in an interactive Streamlit dashboard.
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# FX Options Pricing & Risk Analytics Dashboard

A Python project for FX Options Trading and Financial Markets internship preparation. It builds a synthetic EUR/USD implied volatility surface, prices European FX options with the Garman-Kohlhagen model, calculates Greeks, runs scenario analysis, and produces a simple delta-hedging recommendation in an interactive Streamlit dashboard.

## Project Motivation

FX options desks need fast tools for pricing, risk explanation, and market scenario analysis. This project recreates a simplified analytics workflow: load market volatility data, interpolate an implied volatility, value an option, inspect Greeks, stress the market, and translate delta into a hedge action.

## Why FX Options Matter

FX options are used by banks, asset managers, corporates, and macro funds to hedge or express views on exchange rates. Unlike a forward, an option gives asymmetric payoff exposure, so traders need pricing models and risk measures to understand how option value changes with spot, volatility, time, and rates.

## Garman-Kohlhagen Model

The Garman-Kohlhagen model is the Black-Scholes framework adapted for foreign exchange. For EUR/USD, USD is the domestic currency and EUR is the foreign currency. The model discounts the strike at the domestic rate and discounts the spot exposure at the foreign rate.

For a European FX call:

```text
C = S0 * exp(-rf * T) * N(d1) - K * exp(-rd * T) * N(d2)
```

For a European FX put:

```text
P = K * exp(-rd * T) * N(-d2) - S0 * exp(-rf * T) * N(-d1)
```

## Implied Volatility Surface

An implied volatility surface maps option maturity and strike to the volatility implied by market option prices. Real FX options markets show smile and skew patterns: options away from at-the-money often trade at different implied volatilities because investors value tail protection and directional risk differently.

This project uses a synthetic but realistic EUR/USD surface across 1W, 1M, 3M, 6M, and 1Y maturities with strikes from 1.02 to 1.18.

## Greeks and Risk Management

Greeks explain how option value responds to market moves:

- Delta: directional exposure to spot.
- Gamma: sensitivity of delta to spot.
- Vega: sensitivity to implied volatility.
- Theta: time decay.
- Domestic rho: sensitivity to USD interest rates.
- Foreign rho: sensitivity to EUR interest rates.

These measures help a trader decide whether a book is mostly exposed to spot direction, volatility, time decay, or rates.

## Project Structure

```text
fx-options-dashboard/
├── README.md
├── requirements.txt
├── app.py
├── data/
│   └── sample_vol_surface.csv
├── src/
│   ├── __init__.py
│   ├── market_data.py
│   ├── volatility_surface.py
│   ├── garman_kohlhagen.py
│   ├── greeks.py
│   ├── scenario_analysis.py
│   ├── hedging.py
│   └── utils.py
└── tests/
    ├── test_garman_kohlhagen.py
    ├── test_greeks.py
    └── test_volatility_surface.py
```

## How to Run

```bash
cd fx-options-dashboard
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Run tests:

```bash
pytest
```

### Core Implementation Code & Architecture
#### File: `src/__init__.py`
```python
"""FX options pricing and risk analytics package."""
```

#### File: `tests/test_greeks.py`
```python
from __future__ import annotations

from src.greeks import calculate_greeks


def test_call_delta_is_between_zero_and_one() -> None:
    greeks = calculate_greeks(
        spot=1.10,
        strike=1.10,
        maturity=0.5,
        domestic_rate=0.05,
        foreign_rate=0.035,
        volatility=0.09,
        option_type="call",
    )

    assert 0 < greeks["delta"] < 1


def test_put_delta_is_between_minus_one_and_zero() -> None:
    greeks = calculate_greeks(
        spot=1.10,
        strike=1.10,
        maturity=0.5,
        domestic_rate=0.05,
        foreign_rate=0.035,
        volatility=0.09,
        option_type="put",
    )

    assert -1 < greeks["delta"] < 0


def test_gamma_and_vega_are_positive() -> None:
    greeks = calculate_greeks(
        spot=1.10,
        strike=1.10,
        maturity=0.5,
        domestic_rate=0.05,
        foreign_rate=0.035,
        volatility=0.09,
        option_type="call",
    )

    assert greeks["gamma"] > 0
    assert greeks["vega"] > 0
```

#### File: `tests/test_volatility_surface.py`
```python
from __future__ import annotations

from pathlib import Path

from src.scenario_analysis import run_scenario_analysis
from src.volatility_surface import VolatilitySurface


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sample_vol_surface.csv"


def test_interpolated_volatility_is_positive() -> None:
    surface = VolatilitySurface(DATA_PATH)

    volatility = surface.get_implied_volatility(strike=1.11, maturity=0.30)

    assert volatility > 0


def test_surface_grid_has_expected_shape() -> None:
    surface = VolatilitySurface(DATA_PATH)

    strike_grid, maturity_grid, vol_grid = surface.surface_grid()

    assert strike_grid.shape == maturity_grid.shape == vol_grid.shape


def test_scenario_analysis_returns_non_empty_dataframe() -> None:
    scenarios = run_scenario_analysis(
        spot=1.10,
        strike=1.10,
        maturity=0.5,
        domestic_rate=0.05,
        foreign_rate=0.035,
        volatility=0.09,
        option_type="call",
    )

    assert not scenarios.empty
    assert {"Scenario", "Option price", "P&L", "Delta", "Gamma", "Vega", "Theta"}.issubset(
        scenarios.columns
    )
```

#### File: `src/market_data.py`
```python
"""Market data loading utilities."""

from __future__ import annotations

from pathlib import Path

import pandas as pd


REQUIRED_VOL_COLUMNS = {
    "maturity",
    "time_to_maturity",
    "strike",
    "implied_volatility",
}


def load_vol_surface_data(path: str | Path) -> pd.DataFrame:
    """Load and validate an implied volatility surface CSV."""
    data = pd.read_csv(path)
    missing = REQUIRED_VOL_COLUMNS.difference(data.columns)
    if missing:
        missing_cols = ", ".join(sorted(missing))
        raise ValueError(f"Volatility data is missing required columns: {missing_cols}")

    data = data.copy()
    data["time_to_maturity"] = data["time_to_maturity"].astype(float)
    data["strike"] = data["strike"].astype(float)
    data["implied_volatility"] = data["implied_volatility"].astype(float)

    if (data["time_to_maturity"] <= 0).any():
        raise ValueError("All time_to_maturity values must be positive.")
    if (data["strike"] <= 0).any():
        raise ValueError("All strike values must be positive.")
    if (data["implied_volatility"] <= 0).any():
        raise ValueError("All implied volatility values must be positive.")

    return data.sort_values(["time_to_maturity", "strike"]).reset_index(drop=True)
```

#### File: `src/garman_kohlhagen.py`
```python
"""Garman-Kohlhagen pricing model for European FX options."""

from __future__ import annotations

from math import exp

from scipy.stats import norm

from .utils import calculate_d1_d2, validate_option_inputs


def price_fx_option(
    spot: float,
    strike: float,
    maturity: float,
    domestic_rate: float,
    foreign_rate: float,
    volatility: float,
    option_type: str,
) -> float:
    """Price a European FX option using the Garman-Kohlhagen model.

    For EUR/USD, USD is the domestic currency and EUR is the foreign currency.
    The foreign discount factor captures the yield earned by holding the base
    currency instead of the option.
    """
    option_type = validate_option_inputs(spot, strike, maturity, volatility, option_type)

    if maturity == 0 or volatility == 0:
        intrinsic = max(spot - strike, 0.0) if option_type == "call" else max(strike - spot, 0.0)
        return intrinsic

    d1, d2 = calculate_d1_d2(
        spot=spot,
        strike=strike,
        maturity=maturity,
        domestic_rate=domestic_rate,
        foreign_rate=foreign_rate,
        volatility=volatility,
    )
    foreign_df = exp(-foreign_rate * maturity)
    domestic_df = exp(-domestic_rate * maturity)

    if option_type == "call":
        return spot * foreign_df * norm.cdf(d1) - strike * domestic_df * norm.cdf(d2)
    return strike * domestic_df * norm.cdf(-d2) - spot * foreign_df * norm.cdf(-d1)
```

#### File: `src/hedging.py`
```python
"""Simple delta-hedging recommendations for FX option positions."""

from __future__ import annotations


def generate_delta_hedge_recommendation(delta: float, notional: float) -> dict[str, float | str]:
    """Generate a rule-based EUR/USD forward hedge recommendation.

    Delta is expressed per one unit of base currency notional. Multiplying by
    option notional gives the EUR exposure that should be offset with forwards.
    """
    if notional <= 0:
        raise ValueError("notional must be positive.")

    portfolio_delta = delta * notional
    if abs(portfolio_delta) < 1e-8:
        direction = "No hedge"
        hedge_amount = 0.0
        recommendation = "The position is already approximately delta-neutral."
    elif portfolio_delta > 0:
        direction = "Sell EUR/USD forward"
        hedge_amount = abs(portfolio_delta)
        recommendation = (
            "The position has positive EUR delta exposure. "
            f"Sell EUR/USD forward with EUR {hedge_amount:,.0f} notional to become approximately delta-neutral."
        )
    else:
        direction = "Buy EUR/USD forward"
        hedge_amount = abs(portfolio_delta)
        recommendation = (
            "The position has negative EUR delta exposure. "
            f"Buy EUR/USD forward with EUR {hedge_amount:,.0f} notional to become approximately delta-neutral."
        )

    return {
        "portfolio_delta": portfolio_delta,
        "hedge_direction": direction,
        "hedge_amount": hedge_amount,
        "recommendation": recommendation,
    }
```


==================================================


## [2/3] Repository: theta-reaper-template (`PHASE4-QUANT-195`)
- **Full Name**: `PHASE4-QUANT-195_socials-zanskar__theta-reaper-template`
- **Description**: A defined-risk Iron Condor template for the Nubra Python SDK. Delta-based strike selection, Greeks, margin check before trading, and 4-leg multi-leg execution in one order.
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Theta Reaper Iron Condor Template (Nubra Python SDK)

A defined-risk **option selling** template for the **Nubra Python SDK** (`nubra-sdk`): sell an OTM call spread and an OTM put spread at once, collect premium from both sides, and let time decay (theta) work for you.

## What it demonstrates

- **Greeks from the option chain** - delta, theta, IV per strike via `market.option_chain()`
- **Delta-based strike selection** - sells the ~0.20-delta call and put, buys wings further out
- **Margin check before trading** - `trader.get_margin()` shows required margin and estimated charges *before* any order goes out
- **4-leg multi-leg order** - the whole condor placed as one `create_order()` call with `isMultiLeg: True`

## The position

```
BUY  call  (wing)      ← caps loss on the upside
SELL call  (~0.20 Δ)   ← collects premium
        …spot stays here = profit…
SELL put   (~0.20 Δ)   ← collects premium
BUY  put   (wing)      ← caps loss on the downside
```

The script prints net credit, **defined max loss**, and the net theta you're collecting.

## Safety switch

The script is a **dry run by default** — it selects strikes, prints the position, and checks margin, but places nothing until you set:

```python
PLACE_ORDER = True
```

Multi-leg convention used: `unitQty > 0` = buy leg, `unitQty < 0` = sell leg. Verify with the margin check output and a 1-lot test before trading size.

## Settings

```python
UNDERLYING = "NIFTY"
SHORT_DELTA = 0.20     # short strike selection
WING_STRIKES = 2       # wings this many strikes further out
LOTS = 1
```

## Run it

```bash
pip install -r requirements.txt
python theta_reaper.py
```

Greeks are live-market data — run during market hours.

## ⚠️ Disclaimer

Educational example only — not investment advice. Option selling carries significant risk; the risk is defined **only while all four legs stay on**. Trade at your own risk.

### Core Implementation Code & Architecture
#### File: `theta_reaper.py`
```python
"""
Theta Reaper - a defined-risk Iron Condor template for the Nubra Python SDK.

An Iron Condor sells an OTM call spread AND an OTM put spread at the
same time. You collect premium from both sides and profit if the market
stays inside your short strikes until expiry. The long wings cap your
maximum loss -- this is a DEFINED-RISK way to sell options.

This template demonstrates:
    - reading Greeks (delta, theta, IV) from the option chain
    - selecting strikes by delta
    - checking required margin BEFORE placing the trade
    - placing a 4-leg multi-leg order in one shot

DISCLAIMER: Educational example only. Not investment advice.
Option selling can lose more than the premium collected if legs are
removed or modified. Trade at your own risk.
"""

from nubra_python_sdk.start_sdk import InitNubraSdk, NubraEnv
from nubra_python_sdk.trading.trading_data import NubraTrader
from nubra_python_sdk.marketdata.market_data import MarketData
from nubra_python_sdk.interceptor.errors import NubraHttpError, NubraValidationError

# ---------------- Settings ----------------

UNDERLYING = "NIFTY"
SHORT_DELTA = 0.20      # sell the strike whose |delta| is closest to this
WING_STRIKES = 2        # buy protection this many strikes further out
LOTS = 1
PLACE_ORDER = False     # safety switch: set True to actually trade


def strike_by_delta(options, target_delta):
    """Find the option whose |delta| is closest to target_delta."""
    with_delta = [o for o in options if o.delta is not None]
    if not with_delta:
        return None
    return min(with_delta, key=lambda o: abs(abs(o.delta) - target_delta))


def strikes_away(options, from_strike, count, direction):
    """Return the option `count` strikes above (+1) or below (-1) from_strike."""
    ladder = sorted(options, key=lambda o: o.strike_price)
    strikes = [o.strike_price for o in ladder]
    if from_strike not in strikes:
        return None
    idx = strikes.index(from_strike) + count * direction
    if 0 <= idx < len(ladder):
        return ladder[idx]
    return None


def rupees(paise):
    return f"Rs {paise / 100:.2f}" if paise is not None else "n/a"


def main():
    nubra = InitNubraSdk(env=NubraEnv.PROD)
    trader = NubraTrader(nubra)
    market = MarketData(nubra)

    # ---- 1. Fetch the chain and pick the four legs by delta ----
    try:
        chain = market.option_chain(UNDERLYING).chain
    except NubraHttpError as e:
        print(f"Could not fetch option chain: {e}")
        return

    print(f"{UNDERLYING} spot {rupees(chain.current_price)}, expiry {chain.expiry}")

    short_call = strike_by_delta(chain.ce, SHORT_DELTA)
    short_put = strike_by_delta(chain.pe, SHORT_DELTA)
    if not short_call or not short_put:
        print("Chain has no Greeks right now (market closed?). Try during market hours.")
        return

    long_call = strikes_away(chain.ce, short_call.strike_price, WING_STRIKES, +1)
    long_put = strikes_away(chain.pe, short_put.strike_price, WING_STRIKES, -1)
    if not long_call or not long_put:
        print("Could not find wing strikes far enough out.")
        return

    lot = short_call.lot_size or 1
    qty = LOTS  # multi-leg qty is the multiplier; unitQty below is per-lot units

    # ---- 2. Show the position and its Greeks ----
    legs_info = [
        ("SELL CALL", short_call), ("BUY  CALL", long_call),
        ("SELL PUT ", short_put), ("BUY  PUT ", long_put),
    ]
    credit = 0
    total_theta = 0.0
    print("\nIron Condor legs:")
    for action, o in legs_info:
        sign = 1 if action.startswith("SELL") else -1
        credit += sign * (o.last_traded_price or 0)
        total_theta += -sign * (o.theta or 0)  # short options collect theta
        print(f"  {action} {o.strike_price:>7}  ltp {rupees(o.last_traded_price):>12}  "
              f"delta {o.delta:+.2f}  theta {o.theta:+.2f}  iv {o.iv}")

    width = (long_call.strike_price - short_call.strike_price)  # paise-scale strike gap
    print(f"\nNet credit per lot:  {rupees(credit * lot)}")
    print(f"Max loss per lot:    {rupees((width - credit) * lot)} (defined risk)")
    print(f"Net theta (per unit): {total_theta:+.2f}  <- this is what the reaper collects daily")

    # ---- 3. Multi-leg order: positive unitQty = BUY leg, negative = SELL leg ----
    # Verify the sign convention with the margin check below (and a 1-lot
    # test trade) before running with size.
    condor = {
        "qty": qty,
        "side": "BUY",              # multi-leg orders are always entered as BUY
        "deliveryType": "IDAY",
        "priceType": "MARKET",
        "validityType": "DAY",
        "isMultiLeg": True,
        "legs": [
            {"refId": short_call.ref_id, "unitQty": -lot},
            {"refId": long_call.ref_id, "unitQty": lot},
            {"refId": short_put.ref_id, "unitQty": -lot},
            {"refId": long_put.ref_id, "unitQty": lot},
        ],
    }

    # ---- 4. Margin check BEFORE trading ----
    try:
        funds = trader.get_margin({"orders": [condor], "requestType": "margin"})
        if funds.marginInfo:
            print(f"\nMargin required: {rupees(funds.marginInfo.totalMargin)}")
        if funds.brokerageInfo:
            print(f"Est. charges:    Rs {funds.brokerageInfo.totalChargesFloat}")
    except (NubraHttpError, NubraValidationError) as e:
        print(f"\nMargin check failed: {e}")
        return

    # ---- 5. Place it (only if you flipped the safety switch) ----
    if not PLACE_ORDER:
        print("\nDry run only. Set PLACE_ORDER = True to actually place the condor.")
        return

    try:
        result = trader.create_order(condor)
        print("Condor placed:", result)
    except NubraValidationError as e:
        print("Order payload invalid:", e.validation_error)
    except NubraHttpError as e:
        print("Order failed:", e)


if __name__ == "__main__":
    main()
```


==================================================


## [3/3] Repository: options-trading-strategy (`PHASE4-QUANT-198`)
- **Full Name**: `PHASE4-QUANT-198_Preeti15-github__options-trading-strategy`
- **Description**: "A Python-based Options Trading Strategy using Greeks (Delta, Gamma, Theta, Vega) with a web dashboard built in Streamlit."
- **GitHub Stars**: 0
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# options-trading-strategy
"A Python-based Options Trading Strategy using Greeks (Delta, Gamma, Theta, Vega) with a web dashboard built in Streamlit."

### Core Implementation Code & Architecture
#### File: `app.py`
```python
from flask import Flask, request, jsonify
import numpy as np
from scipy.stats import norm

app = Flask(__name__)

def calculate_greeks(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    vega = S * np.sqrt(T) * norm.pdf(d1)

    return {"Delta": delta, "Gamma": gamma, "Theta": theta, "Vega": vega}

@app.route('/trade', methods=['GET'])
def trade():
    S = float(request.args.get('S', 150))
    K = float(request.args.get('K', 155))
    T = float(request.args.get('T', 30)) / 365
    r = float(request.args.get('r', 0.05))
    sigma = float(request.args.get('sigma', 0.2))

    greeks = calculate_greeks(S, K, T, r, sigma)
    return jsonify(greeks)

if __name__ == '__main__':
    app.run(debug=True)
```

#### File: `dashboard.py`
```python
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def calculate_greeks(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = norm.cdf(d1)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
    theta = - (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    vega = S * np.sqrt(T) * norm.pdf(d1)

    return delta, gamma, theta, vega


def calculate_profit_loss(S, K, premium):
    return max(S - K, 0) - premium


st.title("📈 Options Trading Strategy")

S = st.number_input("Stock Price", value=150.0)
K = st.number_input("Strike Price", value=155.0)
T = st.number_input("Days to Expiry", value=30) / 365
r = st.number_input("Risk-Free Rate", value=0.05)
sigma = st.number_input("Volatility", value=0.2)
premium = st.number_input("Option Premium", value=5.0)

delta, gamma, theta, vega = calculate_greeks(S, K, T, r, sigma)

st.subheader("📊 Option Greeks")
st.write(f"**Delta:** {delta:.4f}")
st.write(f"**Gamma:** {gamma:.4f}")
st.write(f"**Theta:** {theta:.4f}")
st.write(f"**Vega:** {vega:.4f}")

profit_loss = calculate_profit_loss(S, K, premium)
st.subheader("💰 Potential Profit/Loss")
st.write(f"Profit/Loss: ${profit_loss:.2f}")

st.subheader("📉 Greeks Visualization")
fig, ax = plt.subplots()
labels = ["Delta", "Gamma", "Theta", "Vega"]
values = [delta, gamma, theta, vega]
ax.bar(labels, values, color=['blue', 'red', 'green', 'orange'])
st.pyplot(fig)
```

#### File: `import_data.py`
```python
import pandas as pd

# File Paths
file_1 = r"C:\Users\Preeti\stock project\aapl_2016_2020.csv"
file_2 = r"C:\Users\Preeti\stock project\aapl_2021_2023.csv"

# Define Correct Data Types
dtype_dict = {
    "C_DELTA": "float64",
    "C_GAMMA": "float64",
    "C_VEGA": "float64",
    "C_THETA": "float64",
    "C_RHO": "float64",
    "C_IV": "float64",
    "C_VOLUME": "float64",
    "C_LAST": "float64",
    "C_BID": "float64",
    "C_ASK": "float64",
    "P_BID": "float64",
    "P_ASK": "float64",
    "P_LAST": "float64",
    "P_DELTA": "float64",
    "P_GAMMA": "float64",
    "P_VEGA": "float64",
    "P_THETA": "float64",
    "P_RHO": "float64",
    "P_IV": "float64",
    "P_VOLUME": "float64",
}

# Read CSV with dtype and low_memory=False
df1 = pd.read_csv(file_1, dtype=dtype_dict, low_memory=False)
df2 = pd.read_csv(file_2, dtype=dtype_dict, low_memory=False)

# Combine Both DataFrames
df = pd.concat([df1, df2], ignore_index=True)

# Check Data
print(df.head())
print(df.info())


import numpy as np
import scipy.stats as si

def calculate_greeks(S, K, T, r, sigma):
    """
    Calculate option Greeks: Delta, Gamma, Theta, Vega using Black-Scholes Model.
    S: Current stock price
    K: Strike price
    T: Time to expiry (in years)
    r: Risk-free interest rate
    sigma: Volatility
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    delta = si.norm.cdf(d1)  # N(d1)
    gamma = si.norm.pdf(d1) / (S * sigma * np.sqrt(T))  # N'(d1)
    vega = S * si.norm.pdf(d1) * np.sqrt(T)  # Vega
    theta = (-S * si.norm.pdf(d1) * sigma / (2 * np.sqrt(T)))  # Theta

    return delta, gamma, theta, vega


def trading_strategy(S, K, T, r, sigma):
    """
    Define an options trading strategy based on Greeks.
    """
    delta, gamma, theta, vega = calculate_greeks(S, K, T, r, sigma)

    if delta > 0.5 and vega > 20:
        return "BUY CALL OPTION"
    elif delta < -0.5 and vega > 20:
        return "BUY PUT OPTION"
    else:
        return "NO TRADE"

    # Example Test


decision = trading_strategy(150, 155, 30 / 365, 0.05, 0.2)
print("Trading Decision:", decision)
```


==================================================
