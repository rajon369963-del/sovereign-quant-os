# ⚡ [QUANT-SOURCE-069] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_069_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: QuantInsti_InterIIT2023 (`VAULT_IN-QUANT-119_anurag203__QuantInsti_InterIIT2023`)
- **Full Name**: `IN-QUANT-119_anurag203__QuantInsti_InterIIT2023`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Efficacy of Price Action Trading Strategies in the Context of the Indian Equities Market
## **Introduction** :
* Welcome to our project on price action trading strategies for Indian equities market! This project was born out of our participation in the Inter IIT Tech Meet 11.0 where we took up QuantInsti's intriguing problem statement. We are proud to announce that we were at Bronze Runner-up position for our hard work and dedication to the task. This project examines the effectiveness of candlestick patterns and price action trading strategies in the context of the Indian equities market. Through developing and testing three distinct hypotheses, we provide a nuanced and insightful examination of these techniques and contribute to the ongoing discourse on financial predictions.
___
## **Summary** :
### The project involves three hypotheses:

* Hypothesis 1: The combination of Mean Reversion and Engulfing or Harami patterns may provide useful signals for entering and exiting trades.

* Hypothesis 2: Doji patterns can be a valuable tool for traders in identifying potential market trends and making informed trade decisions, especially in banking and auto Indian stocks.

* Hypothesis 3: Identifying key resistance levels and buying the security when it breaks through them can be a valuable tool for capturing the potential upside in security that shows strength.
___
## **Data** :
* We collected data for a variety of large-cap and liquid Indian equities, including banks, autos, metals, and IT stocks. Our data includes daily price, volume, and technical indicators such as moving averages, Bollinger Bands, and relative strength index (RSI).
___
## **Results** :

### From our analysis, we found that:

* Mean Reversion and Candlestick Patterns can be useful technical analysis tools for trading large-cap and liquid Indian equities.
* The combination of Mean Reversion and Engulfing or Harami patterns may provide useful signals for entering and exiting trades.
* The 2nd Hypothesis works excellent for the sectors sensitive to the nation’s interest rates.
* Doji patterns can be a valuable tool for traders in identifying potential market trends and making informed trade decisions, especially in banking and auto Indian stocks.
* Hypothesis 3 can be a valuable tool for capturing the potential upside in security that shows strength.
___
## **Conclusion** :

Overall, our project suggests that technical analysis can be a useful tool for trading Indian equities. However, it is important to note that technical analysis should be used in conjunction with fundamental analysis and a comprehensive risk management strategy. We hope our findings will provide useful insights for traders and investors interested in the Indian equity market.
___
## For a more detailed analysis, click on the following link to access the full report : [QuantInsti_InterIIT2023.pdf](https://github.com/anurag203/QuantInsti_InterIIT2023/files/11185283/QuantInsti_InterIIT2023.pdf)

### Core Implementation Code & Architecture
#### File: `GoldenCross_Blueshiftcode.py`
```python
from blueshift.api import date_rules, time_rules, symbol
from blueshift.api import schedule_function, set_long_only, order_target_percent
from blueshift.library.library import alpha_function, get_history, enter_long
from blueshift.library.library import finish_prune_tracking, init_prune_tracking


def initialize(context):
    set_long_only()
    context.universe = [symbol('RELIANCE')]
    context.deathcross = {}
    context.golden_cross = {}
    context.shortterm_ma = {}
    context.longtermma = {}
    schedule_function(scheduled_func_87631, date_rules.every_day(),
        time_rules.market_open(hours=0, minutes=5))


def rule_func_87643(context, data):
    for asset in context.universe:
        if context.deathcross[asset]:
            enter_long(context, asset, order_target_percent, -0.25, None,
                'SCHEDULE')


def rule_func_87635(context, data):
    for asset in context.universe:
        if context.golden_cross[asset]:
            enter_long(context, asset, order_target_percent, 0.25, None,
                'SCHEDULE')
```

#### File: `Dow_theory_Buy_Sell.py`
```python
from blueshift.api import schedule_function, date_rules, time_rules
from blueshift.api import get_datetime, symbol, order
import pandas as pd

def initialize(context):
    context.universe=[symbol('AAPL')] # list of shares we will be trading
    # shedule funtion for keep running program in specified time interval
    schedule_function(myfunc, date_rule=date_rules.every_day(), time_rule=time_rules.every_nth_minute(minutes=30))

def myfunc(context, data):
    # stock price of last 50 days
    prev_data = data.history(context.universe[0], 'close', 50, '1d')
    df = pd.DataFrame(prev_data) # converted to panda dataframe

    # finding last maxima (it is maxima if it is maximum in window of 5 days)
    df['rolling_max'] = df['close'].rolling(window=5).max()
    previous_peak = df[df['close'] == df['rolling_max']].iloc[-2]['close']

    # finding last minima (it is maxima if it is minimum in window of 5 days)
    df['rolling_min'] = df['close'].rolling(window=5).min()
    previous_low = df[df['close'] == df['rolling_min']].iloc[-2]['close']

    # current price 
    px = data.current(context.universe[0],'close')
    # print([previous_peak,previous_low,px])

    #calculating count of share of AAPL we have
    portfolio = context.portfolio
    positions = portfolio.positions
    tot_share = 0 # assuming 0 at first

    # str(asset).split("(")[1].split(")")[0] # for getting share name and id
    
    for asset in positions:
        position = positions[asset]
        tot_share = position.quantity

    if(px > previous_peak):
        x = portfolio.cash / px # count we can buy with our cash
        x= int(x)
        if(x > 0):
            order(context.universe[0], x) # buying shares
    if(px < previous_low and tot_share > 0):
        order(context.universe[0],-tot_share) # selling shares

    # print(f'scheduled function called at {get_datetime()}')
```

#### File: `Updated_Dow_theory_min_max_hard_coded.py`
```python
from blueshift.library.technicals.indicators import fibonacci_support, adx
from blueshift.finance import commission, slippage
from blueshift.api import symbol, order_target_percent, set_commission, set_slippage, schedule_function, date_rules, time_rules, get_datetime
import numpy as np
import pandas as pd
from math import sqrt

def initialize(context):
    # universe selection
    context.securities = [symbol('NIFTY-I'),symbol('BANKNIFTY-I')]
    # context.securities = [symbol('ADANIPOWER')]

    # define strategy parameters
    context.params = {'indicator_lookback':100,
                      'indicator_freq':'1d',
                      'buy_signal':1,
                      'sell_signal':-1,
                      'ROC_period_short':30,
                      'ROC_period_long':120,
                      'ADX_period':120,
                      'trade_freq':30,
                      'leverage':1}

    # variables to calculate support and resistance line and target portfolio
    context.stop_loss = dict((security,0) for security in context.securities)
    context.previous_peak = dict((security,0) for security in context.securities)
    context.signal = dict((security,0) for security in context.securities)
    context.target_position = dict((security,0) for security in context.securities)

    # set trading cost and slippage to zero
    set_commission(commission.PerShare(cost=0.002, min_trade_cost=0.0))
    set_slippage(slippage.FixedSlippage(0.00))
    
    freq = int(context.params['trade_freq'])
    # schedule_function(run_strategy, date_rules.every_day(), time_rules.every_nth_minute(freq))
    schedule_function(run_strategy, date_rules.every_day(), time_rules.market_close(minutes=59))
    schedule_function(stop_trading, date_rules.every_day(), time_rules.market_close(minutes=30))

def before_trading_start(context, data):
    context.trade = True
    
def stop_trading(context, data):
    context.trade = False

def run_strategy(context, data):
    if not context.trade:
        return
    
    generate_max_min(context,data)
    generate_target_position(context, data)
    rebalance(context, data)

def rebalance(context,data):
    for security in context.securities:
        order_target_percent(security, context.target_position[security])

def generate_target_position(context, data):
    num_secs = len(context.securities)
    weight = round(1.0/num_secs,2)*context.params['leverage']

    for security in context.securities:
        if context.signal[security] == context.params['buy_signal']:
            context.target_position[security] = weight
        elif context.signal[security] == context.params['sell_signal']:
            context.target_position[security] = 0

def generate_signal(context,security,points):
    curr = points[len(points)-1] #current price 
    if(curr>=context.previous_peak[security]):
        context.signal[security] = context.params['buy_signal']
    elif(curr<=context.stop_loss[security]):
        context.signal[security] = context.params['sell_signal']    
    else:
        context.signal[security] = 0



def generate_max_min(context, data):
    try:
        price_data = data.history(context.securities, ['open','high','low','close'], context.params['indicator_lookback'], context.params['indicator_freq'])
        current_price = data.current(context.securities, ['open','high','low','close'])
        price_data.append(current_price)
    except:
        return

    for security in context.securities:
        px = price_data.xs(security)
        context.previous_peak[security], context.stop_loss[security] = loc_max_min(px)
        generate_signal(context,security,px.close.values)


# Function to calculate last minima and maxima price
def loc_max_min(px):
    points=px.close.values
    i=len(points)-2
    for j in range(1,len(points)-1):
        i=len(points)-1-j
        if points[i-1] > points[i] < points[i+1]:
            mi=points[i]
            break

    for j in range(1,len(points)-1):
        i=len(points)-1-j
        if points[i-1] < points[i] > points[i+1]:
            ma=points[i]
            break                 
    return ma,mi
```

#### File: `Eliot_Wave_Strategy_1.py`
```python
from blueshift.library.technicals.indicators import fibonacci_support, adx
from blueshift.finance import commission, slippage
from blueshift.api import symbol, order_target_percent, set_commission, set_slippage, schedule_function, date_rules, time_rules, get_datetime
import numpy as np
import pandas as pd
from math import sqrt
import talib as ta

def initialize(context):
    # universe selection
    # context.securities = [symbol('NIFTY-I')]
    context.securities = [symbol('BAJFINANCE'),symbol('HDFCBANK'),symbol('ICICIBANK'),symbol('KOTAKBANK'),symbol('SBIN'),symbol('BAJAJFINSV'),symbol('AXISBANK')]
    # context.securities = [symbol('JSL'),symbol('JSWSTEEL'),symbol('TATASTEEL'),symbol('TECHM'),symbol('ADANIENT'),symbol('HINDALCO'),symbol('WELCORP')]
    # context.securities = [symbol('TCS'),symbol('INFY'),symbol('WIPRO'),symbol('TECHM'),symbol('HCLTECH'),symbol('COFORGE'),symbol('MPHASIS')]
    # context.securities = [symbol('MARUTI'),symbol('TVSMOTOR'),symbol('EICHERMOT'),symbol('ESCORTS'),symbol('ASHOKLEY'),symbol('TATAMOTORS'),symbol('MOTHERSON')]

    # define strategy parameters
    context.params = {'indicator_lookback':100,
                      'indicator_freq':'1m',
                      'buy_signal':1,
                      'sell_signal':-1,
                      'ROC_period_short':30,
                      'ROC_period_long':120,
                      'ADX_period':120,
                      'trade_freq':30,
                      'leverage':1}

    # variables to calculate support and resistance line and target portfolio
    context.stop_loss = dict((security,0) for security in context.securities)
    context.previous_peak = dict((security,0) for security in context.securities)
    context.signal = dict((security,0) for security in context.securities)
    context.target_position = dict((security,0) for security in context.securities)

    # set trading cost and slippage to zero
    set_commission(commission.PerShare(cost=0.002, min_trade_cost=0.0))
    set_slippage(slippage.FixedSlippage(0.00))
    
    freq = int(context.params['trade_freq'])
    # schedule_function(run_strategy, date_rules.every_day(), time_rules.every_nth_minute(freq))
    schedule_function(run_strategy, date_rules.every_day(), time_rules.market_open(minutes=45))
    schedule_function(stop_trading, date_rules.every_day(), time_rules.market_close(minutes=30))

def before_trading_start(context, data):
    context.trade = True
    
def stop_trading(context, data):
    context.trade = False

def run_strategy(context, data):
    if not context.trade:
        return
    
    generate_max_min(context,data)
    generate_target_position(context, data)
    rebalance(context, data)

def rebalance(context,data):
    for security in context.securities:
        order_target_percent(security, context.target_position[security])

def generate_target_position(context, data):
    num_secs = len(context.securities)
    weight = round(1.0/num_secs,2)*context.params['leverage']

    for security in context.securities:
        if context.signal[security] == context.params['buy_signal']:
            context.target_position[security] = weight
        elif context.signal[security] == context.params['sell_signal']:
            context.target_position[security] = 0
        else:
            context.target_position[security] = 0


def generate_signal(context,security,points):
    curr = points[len(points)-1] #current price 
    m_avg = ta.SMA(points, 40)
    m_avg=m_avg[-1]
    if(curr>=context.previous_peak[security] or curr>= m_avg):
        context.signal[security] = context.params['buy_signal']
    elif(curr<=context.stop_loss[security] or curr<= m_avg):
        context.signal[security] = context.params['sell_signal']



def generate_max_min(context, data):
    try:
        price_data = data.history(context.securities, ['open','high','low','close'], context.params['indicator_lookback'], context.params['indicator_freq'])
    except:
        return

    for security in context.securities:
        px = price_data.xs(security)
        context.previous_peak[security], context.stop_loss[security] = loc_max_min(px)
        generate_signal(context,security,px.close.values)


# Function to calculate last minima and maxima price
def loc_max_min(px):
    points=px.close.values
    i=len(points)-2
    for j in range(1,len(points)-1):
        i=len(points)-1-j
        if points[i-1] > points[i] < points[i+1]:
            mi=points[i]
            break

    for j in range(1,len(points)-1):
        i=len(points)-1-j
        if points[i-1] < points[i] > points[i+1]:
            ma=points[i]
            break                 
    return ma,mi
```

#### File: `candlestick_engulfing.py`
```python
from blueshift.library.technicals.indicators import fibonacci_support, adx
from blueshift.finance import commission, slippage
from blueshift.api import symbol, order_target_percent, set_commission, set_slippage, schedule_function, date_rules, time_rules, get_datetime
import numpy as np
import pandas as pd
from math import sqrt

def initialize(context):
    # universe selection
    context.securities = [symbol('RELIANCE')]
    # context.securities = [symbol('ADANIPOWER')]

    # define strategy parameters
    context.params = {'indicator_lookback':100,
                      'indicator_freq':'1m',
                      'buy_signal':1,
                      'sell_signal':-1,
                      'ROC_period_short':30,
                      'ROC_period_long':120,
                      'ADX_period':120,
                      'trade_freq':5,
                      'leverage':1}

    # variables to calculate support and resistance line and target portfolio
    context.stop_loss = dict((security,0) for security in context.securities)
    context.exits = dict((security,0) for security in context.securities)
    context.signal = dict((security,0) for security in context.securities)
    context.target_position = dict((security,0) for security in context.securities)

    # set trading cost and slippage to zero
    set_commission(commission.PerShare(cost=0.002, min_trade_cost=0.0))
    set_slippage(slippage.FixedSlippage(0.00))
    
    freq = int(context.params['trade_freq'])
    schedule_function(run_strategy, date_rules.every_day(), time_rules.every_nth_minute(freq))
    # schedule_function(run_strategy, date_rules.every_day(), time_rules.market_close(minutes=59))
    schedule_function(stop_trading, date_rules.every_day(), time_rules.market_close(minutes=30))

def before_trading_start(context, data):
    context.trade = True
    
def stop_trading(context, data):
    context.trade = False

def run_strategy(context, data):
    if not context.trade:
        return
    
    generate_signal(context,data)
    generate_target_position(context, data)
    rebalance(context, data)

def rebalance(context,data):
    for security in context.securities:
        order_target_percent(security, context.target_position[security])

def generate_target_position(context, data):
    num_secs = len(context.securities)
    weight = round(1.0/num_secs,2)*context.params['leverage']

    for security in context.securities:
        if context.signal[security] == context.params['buy_signal']:
            context.target_position[security] = weight
        elif context.signal[security] == context.params['sell_signal']:
            context.target_position[security] = 0


def is_bullish_engulfing(candles):
    
        present_candle = candles.iloc[-1]
        en_candle = candles.iloc[-2]
        prev_candle = candles.iloc[-3]

        close = en_candle['close']
        openf = en_candle['open']
        high = en_candle['high']
        low = en_candle['low']

        prev_close = prev_candle['close']
        prev_open = prev_candle['open']
        prev_high = prev_candle['high']
        prev_low = prev_candle['low']

        # return (prev_close < prev_open and
        #         0.3 > abs(prev_close - prev_open) / (prev_high - prev_low) >= 0.1 and
        #         close > openf and
        #         abs(close - openf) / (high - low) >= 0.7 and
        #         prev_high < close and
        #         prev_low > openf)

        if (close >= prev_open) and (prev_open > prev_close) and (close > openf) and (prev_close >= openf) and (close - openf > prev_open - prev_close):
            if present_candle['close']>=en_candle['high']:
                return True
        return False

def generate_signal(context, data):
    try:
        price_data = data.history(context.securities, ['open','high','low','close'], context.params['indicator_lookback'], context.params['indicator_freq'])
    except:
        return

    for security in context.securities:
        px = price_data.xs(security)
        previous_candle = px.iloc[-2]
        present_candle=px.iloc[-1]
        last_to_last=px.iloc[-3]
        # check if the candle is bulish engulfing and 
        is_bullish_engulfing(px)
        if is_bullish_engulfing(px):
            context.signal[security] = context.params['buy_signal']
            context.stop_loss[security] = min(previous_candle['low'],last_to_last['low'])
            context.exits[security] = previous_candle['high']+3*(previous_candle['high']-previous_candle['low'])
        elif context.stop_loss[security]>=present_candle['close'] or context.exits[security]<=present_candle['close']:
            context.signal[security] = context.params['sell_signal']            
        # else:
        #     context.signal[security] =0
```

#### File: `Eliot_Wave_Strategy_2.py`
```python
from blueshift.library.technicals.indicators import fibonacci_support, adx
from blueshift.finance import commission, slippage
from blueshift.api import symbol, order_target_percent, set_commission, set_slippage, schedule_function, date_rules, time_rules, get_datetime
import numpy as np
import pandas as pd
from math import sqrt
import talib as ta

def initialize(context):
    # universe selection
    # context.securities = [symbol('NIFTY-I'),symbol('BANKNIFTY-I')]
    # context.securities = [symbol('MARUTI'),symbol('TVSMOTOR'),symbol('EICHERMOT'),symbol('ESCORTS'),symbol('ASHOKLEY'),symbol('TATAMOTORS'),symbol('MOTHERSON')]
    context.securities = [symbol('BAJFINANCE'),symbol('HDFCBANK'),symbol('ICICIBANK'),symbol('KOTAKBANK'),symbol('SBIN'),symbol('BAJAJFINSV'),symbol('AXISBANK')]
    # context.securities = [symbol('TCS'),symbol('INFY'),symbol('WIPRO'),symbol('TECHM'),symbol('HCLTECH'),symbol('COFORGE'),symbol('MPHASIS')]
    # context.securities = [symbol('JSL'),symbol('JSWSTEEL'),symbol('TATASTEEL'),symbol('TECHM'),symbol('ADANIENT'),symbol('HINDALCO'),symbol('WELCORP')]
    # context.securities = [symbol('ADANIPOWER')]

    # define strategy parameters
    context.params = {'indicator_lookback':100,
                      'indicator_freq':'1d',
                      'buy_signal':1,
                      'sell_signal':-1,
                      'ROC_period_short':30,
                      'ROC_period_long':120,
                      'ADX_period':120,
                      'trade_freq':1,
                      'leverage':2}

    # variables to calculate support and resistance line and target portfolio
    context.stop_loss = dict((security,0) for security in context.securities)
    context.previous_peak = dict((security,0) for security in context.securities)
    context.signal = dict((security,0) for security in context.securities)
    context.target_position = dict((security,0) for security in context.securities)

    # set trading cost and slippage to zero
    set_commission(commission.PerShare(cost=0.002, min_trade_cost=0.0))
    set_slippage(slippage.FixedSlippage(0.00))
    
    freq = int(context.params['trade_freq'])
    # schedule_function(run_strategy, date_rules.every_day(), time_rules.every_nth_minute(freq))
    schedule_function(run_strategy, date_rules.every_day(), time_rules.market_open(minutes=45))
    schedule_function(stop_trading, date_rules.every_day(), time_rules.market_close(minutes=30))

def before_trading_start(context, data):
    context.trade = True
    
def stop_trading(context, data):
    context.trade = False

def run_strategy(context, data):
    if not context.trade:
        return
    
    generate_max_min(context,data)
    generate_target_position(context, data)
    rebalance(context, data)

def rebalance(context,data):
    for security in context.securities:
        order_target_percent(security, context.target_position[security])

def generate_target_position(context, data):
    num_secs = len(context.securities)
    weight = round(1.0/num_secs,2)*context.params['leverage']

    for security in context.securities:
        if context.signal[security] == context.params['buy_signal']:
            context.target_position[security] = weight
        elif context.signal[security] == context.params['sell_signal']:
            context.target_position[security] = 0
        else:
            context.target_position[security] = 0


def generate_signal(context,security,points):
    curr = points[len(points)-1] #current price 
    m_avg = ta.SMA(points, 40)
    m_avg=m_avg[-1]
    if(curr>=m_avg):
        context.signal[security] = context.params['buy_signal']
    elif(curr<= m_avg):
        context.signal[security] = context.params['sell_signal']
    elif(curr>=context.previous_peak[security]):
        context.signal[security] = context.params['buy_signal']
    elif(curr<=context.stop_loss[security]):
        context.signal[security] = context.params['sell_signal']



def generate_max_min(context, data):
    try:
        price_data = data.history(context.securities, ['open','high','low','close'], context.params['indicator_lookback'], context.params['indicator_freq'])
    except:
        return

    for security in context.securities:
        px = price_data.xs(security)
        context.previous_peak[security], context.stop_loss[security] = loc_max_min(px)
        generate_signal(context,security,px.close.values)


# Function to calculate last minima and maxima price
def loc_max_min(px):
    points=px.close.values
    i=len(points)-2
    for j in range(1,len(points)-1):
        i=len(points)-1-j
        if points[i-1] > points[i] < points[i+1]:
            mi=points[i]
            break

    for j in range(1,len(points)-1):
        i=len(points)-1-j
        if points[i-1] < points[i] > points[i+1]:
            ma=points[i]
            break                 
    return ma,mi
```


==================================================


## [2/3] Repository: price-action-lib (`VAULT_IN-QUANT-123_nashit8421__price-action-lib`)
- **Full Name**: `IN-QUANT-123_nashit8421__price-action-lib`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Price Action Library

A comprehensive Python library for pure price action analysis, specifically optimized for the Indian stock market. Generate **95+ columns** of price action analysis with a single function call!

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Key Features

- **30+ Candlestick Patterns** - From basic doji to complex triple formations
- **15+ Chart Patterns** - Head & shoulders, triangles, wedges, flags, and more
- **Advanced Market Structure** - BOS, ChoCh, Fair Value Gaps, Order Blocks
- **Support & Resistance** - Multiple detection methods with confluence analysis
- **Volume Analysis** - Volume Spread Analysis (VSA) and volume patterns
- **Price Action Setups** - Pin bars, inside bars, fakey patterns, springs
- **Gap Analysis** - All gap types with classification and tracking
- **Session Analysis** - Indian market hours optimization (9:15 AM - 3:30 PM IST)
- **Multi-Timeframe** - Analyze across different time horizons
- **Machine Learning Ready** - Structured output perfect for ML models

## 🎯 Perfect For

- **Systematic Trading** - Algorithm development and backtesting
- **Market Research** - Comprehensive price action studies  
- **Machine Learning** - Feature engineering for ML models
- **Professional Trading** - Real-time pattern recognition
- **Education** - Learning price action concepts

## ⚡ Quick Start

### Installation

```bash
# Install dependencies
pip install pandas numpy scipy

# Install the library
pip install .
```

### Basic Usage

```python
from price_action_lib import PriceActionAnalyzer
import pandas as pd

# Initialize analyzer
analyzer = PriceActionAnalyzer()

# Load your OHLCV data (1-minute timeframe recommended)
# df should have columns: open, high, low, close, volume with DateTime index

# Get comprehensive analysis - 95+ columns!
result = analyzer.fetch_all(df)

print(f"Generated {result.shape[1]} columns of analysis!")
print(f"Analyzed {result.shape[0]} time periods")

# Individual analysis methods also available
patterns = analyzer.detect_candlestick_patterns(df)
structure = analyzer.analyze_market_structure(df)
levels = analyzer.find_support_resistance(df)
```

### Sample Output

The `fetch_all()` method returns a DataFrame with 95+ columns including:

- **Original OHLCV** (optional)
- **44+ Candlestick patterns** (`pattern_doji`, `pattern_hammer`, etc.)
- **14+ Chart patterns** (`chart_head_and_shoulders`, `chart_triangle`, etc.)
- **Market structure** (`structure_trend`, `structure_bos`, etc.)
- **Fair Value Gaps** (`fvg_bullish`, `fvg_bearish`)
- **Order Blocks** (`order_block_bullish`, `order_block_bearish`)
- **Price Action Setups** (`setup_pin_bar`, `setup_inside_bar`, etc.)
- **Support/Resistance** (`near_support`, `near_resistance`)
- **Volume Analysis** (`volume_spike`, `volume_climax`, etc.)
- **Gap Analysis** (`gap_breakaway`, `gap_exhaustion`, etc.)
- **Metadata** (ATR, volatility, trend classification, price zones)

## 📊 Example Analysis

```python
# Find high-probability trading setups
strong_signals = result[
    (result['near_support'] == True) &      # At key support level
    (result['setup_pin_bar'] == True) &     # Pin bar setup
    (result['volume_spike'] == True) &      # Volume confirmation
    (result['pattern_hammer'] != '')        # Hammer pattern
]

print(f"Found {len(strong_signals)} high-probability setups!")

# Analyze market structure
current_trend = result['structure_trend'].iloc[-1]
trend_strength = result['structure_trend_strength'].iloc[-1]
print(f"Current trend: {current_trend} (strength: {trend_strength:.2f})")
```

## 🇮🇳 Indian Market Optimization

- **Market Hours**: 9:15 AM - 3:30 PM IST
- **Session Analysis**: Pre-open, opening, regular, closing sessions
- **Holiday Handling**: Automatic weekend and holiday filtering
- **NSE/BSE Compatible**: Optimized for Indian stock exchanges

## 📈 Performance

- **Fast Processing**: 400+ bars/second on typical hardware
- **Memory Efficient**: Only 308KB package size
- **Vectorized Operations**: Optimized pandas/numpy operations
- **Scalable**: Handles datasets from 100 to 10,000+ bars

## 📚 Comprehensive Documentation

For detailed documentation, see **[DOCUMENTATION.md](DOCUMENTATION.md)** which includes:

- **Complete API Reference** - All methods with parameters and examples
- **Pattern Recognition Guide** - Details on all 30+ candlestick patterns
- **Market Structure Analysis** - BOS, ChoCh, FVGs, Order Blocks explained
- **Advanced Features** - Multi-timeframe, volume analysis, gap analysis
- **Best Practices** - Data preparation, performance optimization
- **Troubleshooting** - Common issues and solutions
- **Real-world Examples** - Complete trading workflows

## 🔧 Requirements

- **Python**: 3.7 or higher
- **pandas**: >= 1.3.0
- **numpy**: >= 1.21.0  
- **scipy**: >= 1.7.0

## 📋 Data Format

Your DataFrame should have:

```python
                     open    high     low   close  volume
2024-01-15 09:15:00  1000.0  1002.5   999.0  1001.5  25000
2024-01-15 09:16:00  1001.5  1003.0  1000.5  1002.0  18000
# ... with DateTime index and proper OHLC relationships
```

## 🚦 Quick Test

Verify your installation:

```python
from price_action_lib import PriceActionAnalyzer
analyzer = PriceActionAnalyzer()
print("✅ Price Action Library installed successfully!")
```

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🎉 Ready to Get Started?

1. **Install** the library following the instructions above
2. **Read** the comprehensive [DOCUMENTATION.md](DOCUMENTATION.md)
3. **Load** your OHLCV data into a pandas DataFrame
4. **Run** `analyzer.fetch_all(df)` and get 95+ columns of analysis!

**Happy Trading!** 📈💰

### Core Implementation Code & Architecture
#### File: `price_action_lib/core/__init__.py`
```python
"""Core modules for price action library"""

from .timeframe import TimeFrameManager
from .base import BaseAnalyzer

__all__ = ["TimeFrameManager", "BaseAnalyzer"]
```

#### File: `price_action_lib/patterns/__init__.py`
```python
"""Pattern recognition modules"""

from .candlestick import CandlestickPatterns
from .chart_patterns import ChartPatterns

__all__ = ["CandlestickPatterns", "ChartPatterns"]
```

#### File: `price_action_lib/structures/__init__.py`
```python
"""Market structure analysis modules"""

from .support_resistance import SupportResistance
from .market_structure import MarketStructure

__all__ = ["SupportResistance", "MarketStructure"]
```

#### File: `price_action_lib/analysis/__init__.py`
```python
"""Analysis modules for price action"""

from .volume_analysis import VolumeAnalysis
from .gap_analysis import GapAnalysis
from .session_analysis import SessionAnalysis
from .multi_timeframe import MultiTimeframeAnalysis

__all__ = ["VolumeAnalysis", "GapAnalysis", "SessionAnalysis", "MultiTimeframeAnalysis"]
```

#### File: `price_action_lib/__init__.py`
```python
"""
Price Action Library for Indian Stock Market
A comprehensive library for price action analysis
"""

from .core.timeframe import TimeFrameManager
from .patterns.candlestick import CandlestickPatterns
from .structures.support_resistance import SupportResistance
from .structures.market_structure import MarketStructure
from .analysis.volume_analysis import VolumeAnalysis
from .patterns.chart_patterns import ChartPatterns
from .analysis.gap_analysis import GapAnalysis
from .analysis.session_analysis import SessionAnalysis
from .analysis.multi_timeframe import MultiTimeframeAnalysis
from .main import PriceActionAnalyzer

__version__ = "1.0.1"
__all__ = [
    "PriceActionAnalyzer",
    "TimeFrameManager",
    "CandlestickPatterns",
    "SupportResistance",
    "MarketStructure",
    "VolumeAnalysis",
    "ChartPatterns",
    "GapAnalysis",
    "SessionAnalysis",
    "MultiTimeframeAnalysis"
]
```

#### File: `pyproject.toml`
```python
[build-system]
requires = ["setuptools>=45", "wheel", "setuptools_scm[toml]>=6.2"]
build-backend = "setuptools.build_meta"

[project]
name = "price-action-lib"
dynamic = ["version"]
description = "A comprehensive price action analysis library for Indian stock market"
readme = "README.md"
license = {file = "LICENSE"}
authors = [
    {name = "Nashit", email = "nashit8421@gmail.com"}
]
keywords = ["price action", "trading", "stock market", "candlestick patterns", "technical analysis", "indian stocks", "NSE", "BSE"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Financial and Insurance Industry",
    "Intended Audience :: Developers",
    "Topic :: Office/Business :: Financial :: Investment",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Operating System :: OS Independent",
]
requires-python = ">=3.7"
dependencies = [
    "pandas>=1.3.0",
    "numpy>=1.21.0",
    "scipy>=1.7.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-cov>=3.0.0",
    "black>=22.0.0",
    "flake8>=4.0.0",
]

[project.urls]
Homepage = "https://github.com/nashit8421/price-action-lib"
Documentation = "https://github.com/nashit8421/price-action-lib#readme"
Repository = "https://github.com/nashit8421/price-action-lib.git"
Issues = "https://github.com/nashit8421/price-action-lib/issues"

[tool.setuptools.packages.find]
where = ["."]
include = ["price_action_lib*"]

[tool.setuptools_scm]
write_to = "price_action_lib/_version.py"
```


==================================================


## [3/3] Repository: kha-ching (`VAULT_IN-QUANT-125_aakashlpin__kha-ching`)
- **Full Name**: `IN-QUANT-125_aakashlpin__kha-ching`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# SignalX

SignalX is a trading app for anyone looking to diversify their funds into systematic and algorithmic intraday trading strategies.

✅ Read everything about SignalX [here](https://signalx.club).

Once you've gone through the Notion doc above, come back here for instructions to setup SignalX!

## Setup Prerequisites:

1. [Sign up on DigitalOcean using this link](https://m.do.co/c/d9db955b428e). You'd receive $100 in new signup credits valid for 2 months. Running this app costs $10/month. So you'd be able to run it FREE for first 2 months.

2) Goto https://kite.trade and sign up for Kite Connect. Create an app and pay Zerodha the ₹2000/month fee.

   - Ignore the `Redirect URL` and `Postback URL` fields for now.
   - Copy `API Key` and `API Secret` fields and keep them handy somewhere.

3) Goto https://redislabs.com/try-free/ and sign up for a "Cloud" redis account.

   - Activate your database and name it `signalx`
   - Copy the `Endpoint` and `User Password` fields to construct the following Redis URL - `redis://:{User Password}@{Endpoint}`. Keep this handy. (remove the curly braces)

_Update - Redislabs free tier drops connections very often. Recommend upgrading to a paid tier for a seamless trading experience._

## 1-click Installation

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

or, deploy the application on DigitalOcean's (DO) apps platform.

[![Deploy to DO](https://www.deploytodo.com/do-btn-blue.svg)](https://cloud.digitalocean.com/apps/new?repo=https://github.com/aakashlpin/kha-ching/tree/master&refcode=d9db955b428e)

## Environment variables

> Environment variables are private setting variables that configures this application to run on your Zerodha account.

#### `KITE_API_KEY`

Paste the Kite API key that you copied from Step #1. Ensure to tick `Encrypt`.

#### `KITE_API_SECRET`

Paste the Kite Secret key that you copied from Step #1. Ensure to tick `Encrypt`.

#### `SECRET_COOKIE_PASSWORD`

This **must** be a 32 digit alphanumeric string. Generate a 32 digit password from here - https://1password.com/password-generator/. Ensure to tick `Encrypt`.

#### `REDIS_URL`

Paste the Redis URL generated from Step #2. Ensure to tick `Encrypt`.

#### `MOCK_ORDERS`

Set it to `true` if you'd simulate orders but not actually place them on Zerodha. Comes in handy if you're looking to develop this application locally. Ignore it otherwise.

#### `NEXT_PUBLIC_DEFAULT_LOTS`

Default lots that you trade on a regular basis. This is only the default initial value in the form and is changeable before taking the trade.

for e.g. If you regularly trade `150` quantity of Nifty Options, you'd enter `2` lots here.

#### `NEXT_PUBLIC_DEFAULT_SKEW_PERCENT`

Default skew that you're okay with when selling straddles. Anywhere between 5-15 is a good value. The value here only serves as a default and can be changed before setting up daily trades.

#### `NEXT_PUBLIC_DEFAULT_SQUARE_OFF_TIME`

Default square off time of the strategy. The value here only serves as a default and can be changed per strategy during the strategy setup when taking daily trades. Format is 24 hours hh:mm. i.e. enter `15:20` as value if you mean 3.20pm.

#### `NEXT_PUBLIC_APP_URL`

Enter `${APP_URL}` here or leave this value as it is if you're doing a fresh setup as the value will be correctly prefilled for you.

#### `SIGNALX_API_KEY`

Upgrade to [SignalX Premium](https://imjo.in/q6g7cB) to receive your API key. SignalX Premium gives you access to technical indicators required to trade certain strategies.

#### `DATABASE_HOST_URL`

#### `DATABASE_USER_KEY`

#### `DATABASE_API_KEY`

[Follow the upgrade guide here](https://www.notion.so/Release-notes-20-06-2021-84859083abca4f5bb2ed229eea8642f2#7a05ef9737904c148ea299177f1de8f0) to get values for all these 3 variables.

#### `NEXT_PUBLIC_DEFAULT_SLM_PERCENT`

Default percent of SLM BUY orders to be placed after initial order goes through. The value here only serves as a default and can be changed before setting up daily trades.

#### `NEXT_PUBLIC_GIT_HASH`

Leave the value in this field as it-is. This'll inform if there's an app update available in the app UI. If there's an update available, you can hit the "Deploy" button in your DigitalOcean app to install the new build for yourself.

## Next Steps

- DigitalOcean Step 2: After entering all environment variables in setup Step 1, proceed to the next step and select `Bangalore` as region.
- DigitalOcean Step 3: Select `$5/mo` container size from the `Basic size` dropdown. Ensure you see `$5` as the `Monthy App Cost`.
- Click on `Launch Basic App`.
- Give it 5mins, let the application get build.
- Once successfully built, Goto `Settings` of this app, and copy the URL where DigitalOcean hosted this application for you.
- Go back to the [kite app](https://kite.trade/), and now enter Redirect URL as follows: `{url_from_digitalocean}/api/redirect_url_kite`. It should look something like this https://qwe-qwerty-gex5y.ondigitalocean.app/api/redirect_url_kite (only an example - yours will differ). Press `Save`!

## Using the application

- Bookmark the URL, or save it to your homescreen. You'd need it every trading day!
- Zerodha automatically expires the authentication token required to access the APIs at around 7.35am. You're required to login to this app every day after 7.45am to generate a new access token.
- Once logged in, you'd need to setup your trades for the day. **This needs to be done everyday!**. _Trades setup after market hours will fail the next day as the API access token would have expired._

## Data and Security

- All access tokens are saved via a first-party cookie in your browser and are encrypted via the `SECRET_COOKIE_PASSWORD` environment variable. Whatever you do, **DO NOT** share this with anyone!
- Redis is used for scheduling the tasks or running them on spot. **DO NOT** share your redis URL with anyone as it contains your Zerodha profile details alongwith API access tokens.

## Develop locally

In case you'd like to contribute, you can run the development server like so

```bash
yarn
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

## License

SignalX is [MIT licensed](https://github.com/aakashlpin/kha-ching/blob/master/LICENSE.md).

### Core Implementation Code & Architecture
#### File: `.vscode/settings.json`
```python
{
  "standard.enable": false
}
```

#### File: `.vscode/launch.json`
```python
{
  "version": "0.2.0",
  "configurations": [
    {
      "type": "node",
      "request": "attach",
      "name": "Launch Program",
      "skipFiles": [
        "${workspaceFolder}/node_modules/**/*.js",
        "<node_internals>/**"
      ],
      "port": 9229
    }
  ]
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": false,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "strictNullChecks": true
  },
  "include": ["next-env.d.ts", "**/*.js", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
```

#### File: `public/manifest.json`
```python
{
  "name": "SignalX",
  "short_name": "SignalX",
  "theme_color": "#ffffff",
  "background_color": "#19857b",
  "display": "fullscreen",
  "orientation": "portrait",
  "scope": "/",
  "start_url": "/",
  "icons": [
    {
      "src": "icons/icon-72x72.png",
      "sizes": "72x72",
      "type": "image/png"
    },
    {
      "src": "icons/icon-96x96.png",
      "sizes": "96x96",
      "type": "image/png"
    },
    {
      "src": "icons/icon-128x128.png",
      "sizes": "128x128",
      "type": "image/png"
    },
    {
      "src": "icons/icon-144x144.png",
      "sizes": "144x144",
      "type": "image/png"
    },
    {
      "src": "icons/icon-152x152.png",
      "sizes": "152x152",
      "type": "image/png"
    },
    {
      "src": "icons/icon-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "icons/icon-384x384.png",
      "sizes": "384x384",
      "type": "image/png"
    },
    {
      "src": "icons/icon-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "splash_pages": null
}
```

#### File: `package.json`
```python
{
  "name": "kha-ching",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "NODE_OPTIONS='--inspect' next dev",
    "build": "next build",
    "start": "node ./bootup.js & NODE_OPTIONS=--max-old-space-size=1024 TZ=Asia/Kolkata next start -H 0.0.0.0 -p ${PORT:-8080}",
    "lint": "next lint --quiet",
    "test": "jest ./__tests__ --testPathIgnorePatterns support/*",
    "unit-test": "jest ./__tests__/unit --detectOpenHandles",
    "int-test": "jest ./__tests__/integration",
    "format": "prettier-standard --format"
  },
  "lint-staged": {
    "*": ["prettier-standard --lint"]
  },
  "dependencies": {
    "@date-io/date-fns": "^1.3.13",
    "@material-ui/core": "^4.11.3",
    "@material-ui/icons": "^4.11.2",
    "@material-ui/lab": "^4.0.0-alpha.58",
    "@material-ui/pickers": "^3.2.10",
    "@types/styled-jsx": "^3.4.4",
    "axios": "^0.21.1",
    "bluebird": "^3.7.2",
    "bullmq": "^1.48.2",
    "csvtojson": "^2.0.10",
    "date-fns": "^2.19.0",
    "dayjs": "^1.10.4",
    "esm": "^3.2.25",
    "fyers-api": "^1.1.0",
    "ioredis": "^4.22.0",
    "kiteconnect": "^3.2.0",
    "lodash": "^4.17.21",
    "memoizee": "^0.4.15",
    "nanoid": "^3.1.23",
    "next": "^11.1.0",
    "next-iron-session": "^4.1.11",
    "next-pwa": "5.2.24",
    "qs": "^6.10.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-swipeable-views": "^0.14.0",
    "react-timeago": "^5.2.0",
    "react-toastify": "^7.0.4",
    "redis": "^3.1.2",
    "redis-memoizer": "^1.0.2",
    "request": "^2.88.2",
    "swr": "^0.4.2",
    "trace-unhandled": "^2.0.1",
    "uuid": "^8.3.2"
  },
  "devDependencies": {
    "@types/bluebird": "^3.5.36",
    "@types/react": "^17.0.16",
    "@typescript-eslint/eslint-plugin": "4",
    "@typescript-eslint/parser": "^4.29.0",
    "axios-mock-adapter": "^1.19.0",
    "babel-eslint": "^10.1.0",
    "babel-jest": "^27.0.6",
    "dotenv": "^10.0.0",
    "enzyme": "^3.11.0",
    "eslint": "7",
    "eslint-config-next": "^11.0.1",
    "eslint-config-prettier": "^8.3.0",
    "eslint-config-standard-with-typescript": "^20.0.0",
    "eslint-plugin-import": "2",
    "eslint-plugin-jsx-a11y": "^6.4.1",
    "eslint-plugin-node": "11",
    "eslint-plugin-prettier": "^3.3.1",
    "eslint-plugin-promise": "4",
    "eslint-plugin-react": "^7.24.0",
    "eslint-plugin-react-hooks": "^4.2.0",
    "eslint-plugin-simple-import-sort": "^7.0.0",
    "husky": "^5.0.9",
    "identity-obj-proxy": "^3.0.0",
    "jest": "^27.0.6",
    "jest-when": "^3.3.1",
    "lint-staged": "^10.5.4",
    "mockserver": "^3.1.1",
    "prettier-standard": "^16.4.1",
    "react-test-renderer": "^17.0.2",
    "typescript": "^4.3.5"
  },
  "husky": {
    "hooks": {
      "pre-commit": "lint-staged"
    }
  },
  "cacheDirectories": [".next/cache"]
}
```


==================================================
