# ⚡ [QUANT-SOURCE-111] Consolidated Quant & Algo Trading Repositories
**Category**: `EXECUTION_ALGORITHMS_ROUTING` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_111_EXECUTION_ALGORITHMS_ROUTING.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: quant-trading-strategies (`WHEEL_quant-trading-strategies`)
- **Full Name**: `quant-trading-strategies`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Quant-trading

&nbsp;

## Intro

&nbsp;

> We’re right 50.75 percent of the time... but we’re 100 percent right 50.75 percent of the time, you can make billions that way. <br><br>
> --- Robert Mercer, co-CEO of Renaissance Technologies

> If you trade a lot, you only need to be right 51 percent of the time, we need a smaller edge on each trade. <br><br>
> --- Elwyn Berlekamp, co-Founder of Combinatorial Game Theory

###### *The quotes above come from a book by Gregory Zuckerman, a book every quant must read, THE MAN WHO SOLVED THE MARKET.*

&nbsp;

Most scripts inside this repository are technical indicator automated trading. These scripts include various types of momentum trading, opening range breakout, reversal of support & resistance and statistical arbitrage strategies. Yet, quantitative trading is not only about technical analysis. It can refer to computational finance to exploit derivative price mismatch, pattern recognition on alternative datasets to generate alphas or low latency order execution in the market microstructure. Hence, there are a few ongoing projects inside this repository. These projects are mostly quantamental analysis on some strange ideas I come up with to beat the market (or so I thought). There is no HFT strategy simply because ultra high frequency data are very expensive to acquire (even consider platforms like Quantopian or Quandl). Additionally, please note that, all scripts are historical data backtesting/forward testing (basically via Python, not C++, maybe Julia in the near future). The assumption is that all trades are frictionless. No slippage, no surcharge, no illiquidity. Last but not least, all scripts contain a global function named main so that you can embed the scripts directly into you trading system (although too lazy to write docstring).

### Table of Contents

&nbsp;

#### Options Strategy

* <a href=https://github.com/je-suis-tm/quant-trading#12-options-straddle>Options Straddle</a>
* <a href=https://github.com/je-suis-tm/quant-trading#15-vix-calculator>VIX Calculator</a>

&nbsp;

#### Quantamental Analysis

* <a href=https://github.com/je-suis-tm/quant-trading#11-monte-carlo-project>Monte Carlo Project</a>

* <a href=https://github.com/je-suis-tm/quant-trading#6-oil-money-project>Oil Money Project</a>

* <a href=https://github.com/je-suis-tm/quant-trading#2-pair-trading>Pair Trading</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#13-portfolio-optimization-project>Portfolio Optimization Project</a>

* <a href=https://github.com/je-suis-tm/quant-trading#14-smart-farmers-project>Smart Farmers Project</a>

* <a href=https://github.com/je-suis-tm/quant-trading#16-wisdom-of-crowds-project>Wisdom of Crowd Project</a>

&nbsp;

#### Technical Indicators

* <a href=https://github.com/je-suis-tm/quant-trading#5-awesome-oscillator>Awesome Oscillator</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#9-bollinger-bands-pattern-recognition>Bollinger Bands Pattern Recognition</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#7-dual-thrust>Dual Thrust</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#3-heikin-ashi-candlestick>Heikin-Ashi Candlestick</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#4-london-breakout>London Breakout</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#1-macd-oscillator>MACD Oscillator</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#8-parabolic-sar>Parabolic SAR</a> 

* <a href=https://github.com/je-suis-tm/quant-trading#10-relative-strength-index-pattern-recognition>Relative Strength Index Pattern Recognition</a>

* <a href=https://github.com/je-suis-tm/quant-trading#17-shooting-star>Shooting Star</a>

&nbsp;

### Data Source

* Bloomberg/Eikon

* <a href=https://github.com/je-suis-tm/web-scraping/blob/master/CME3.py>CME</a>/<a href=https://github.com/je-suis-tm/web-scraping/blob/master/LME.py>LME</a>

* <a href=https://www.histdata.com/>Histdata</a>/<a href=https://fxhistoricaldata.com>FX Historical Data</a>

* <a href=https://github.com/je-suis-tm/web-scraping/blob/master/Macrotrends.py>Macrotrends</a>

* <a href=https://stooq.com>Stooq</a>/<a href=https://www.quandl.com>Quandl</a>

* <a href=https://github.com/je-suis-tm/web-scraping/blob/master/WallStreetBets.py>Reddit WallStreetBets</a>

* <a href=https://github.com/je-suis-tm/web-scraping>Web Scraping</a>

* <a href=https://finance.yahoo.com>Yahoo Finance</a>/<a href=https://pypi.org/project/fix-yahoo-finance>fix_yahoo_finance package</a>/<a href=https://pypi.org/project/yfinance>yfinance package</a> 

<br>

## Strategies:

### 1. MACD oscillator

MACD oscillator is trading strategy 101. MACD refers to Moving Average Convergence/Divergence. It is a momentum trading strategy which holds the belief that upward/downward momentum has more impact on short term moving average than long term moving average. It only takes 5 minutes for any bloke with no background in finance to trade with MACD signals. Regarding the simplicity of MACD oscillator, it is the most common strategy among the non-professionals in the market. In behavioral economics, the more people believe in the strategy, the more effective the strategy becomes (not always true, e.g. 2008). Therefore, we should not underestimate the power of MACD oscillator.

For the strategy itself, we compute long term moving average and short term moving average on the close price of a given stock. To generate the trading signal, we implement a comparison between the moving averages of different time horizons. When short term moving average is above long term moving average, we long the given stock accordingly. Vice versa.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/MACD%20Oscillator%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/macd%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/macd%20oscillator.png)

### 2. Pair trading

Pair trading is the basic form of statistics arbitrage. It relies on the assumption that two cointegrated stocks would not drift too far away from each other. First step, we select two stocks and run <a href=https://en.wikipedia.org/wiki/Error_correction_model#Engle_and_Granger_2-step_approach>Engle-Granger two step analysis</a>. Once the criteria of cointegration is met, we standardize the residual and set one sigma away (two tailed) as the threshold. After that, we compute the current standardized residual of the selected stocks accordingly. When the standardized residual exceeds the threshold, it generates the trading signal. The simple rule is we always long the cheap stock and short the expensive stock. 

The core idea of pair trading is <a href=https://en.wikipedia.org/wiki/Cointegration>cointegration</a>. Metaphorically speaking, cointegration is like a couple in a clingy relationship where two parties are crazy-glued together. Yet, most relationships break sooner or later, and only the very few can make it to the marriage (from a statistics perspective, not being pessimistic). Hence, it is important to frequently check on the status quo of cointegration before any pair trading order execution (the same applies to relationships).

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Pair%20trading%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/pair%20trading%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/pair%20trading%20asset.png)

### 3. Heikin-Ashi candlestick

Heikin-Ashi, the exotic name actually referring to 'Average Bar' in Japanese, is an alternative style of candlestick chart. The sophisticated rules of Heiki-Ashi are designed to filter out the noise for momentum trading. Hence, Heikin-Ashi shows more consecutive bars in contrast to the standard candlestick, which makes price momentum and reverse points more distinguishable in figures. Arguably it should outperform the standard candlestick in sideways and choppy markets. 

For the strategy itself, initially we make a few transformations on four vital benchmarks - Open, Close, High, Low. The next step is to apply unique Heikin-Ashi rules on Heikin-Ashi Open, Close, High, Low to generate trading signals. The downside of Heikin-Ashi (or any momentum trading strategies) is the slow response. Thus, we should set up the stop loss position accordingly so that we don't get caught up in any flash crash.

The rules of Heikin-Ashi can be found in <a href=https://quantiacs.com/Blog/Intro-to-Algorithmic-Trading-with-Heikin-Ashi.aspx>Quantiacs</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Heikin-Ashi%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/heikin-ashi%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/heikin-ashi%20asset%20value.png)

### 4. London Breakout

To one of my favourite cities in the world! Proud to be a Londoner!

London Breakout is an intra daily opening range breakout strategy. Basically, it is a fascinating information arbitrage across different markets in different time zones. FX market runs 24/7 globally. For instance, you cannot long the stock of Ford in ASX simply because Ford is listed in NYSE. As FX market is decentralised, you can long any currency pair in any market as long as the market is open. That leaves a door to take a peek at the activity in a closed foreign FX market before the opening of domestic FX market.

Back to London Breakout, London and Tokyo are two of the largest FX markets in the world. Tokyo FX trading hour is GMT 0:00 a.m. - GMT 8:59am. London FX trading hour (no summer daylight saving) begins at GMT 8:00 a.m. Even though there is an hour of overlap, the crucial timeframe of London Breakout is GMT 7:00 a.m. - GMT 7:59 a.m. a.k.a. the last trading hour before the opening of London market. The price movement of the crucial timeframe incorporates the information of all the overnight activities of financial market (from the perspective of the current time zone).

For the strategy itself, we establish upper and lower thresholds prior to the high and low of the crucial timeframe. Once London FX market opens, we spend the first couple of minutes to check if the price would breach the preset boundaries. If it is above threshold, we long the currency pair accordingly. Vice versa. Nevertheless, we should set up a limit to prevent us from trading in the case of abnormal opening volatility. Normally, we clear our positions based on our target stop loss or stop profit respectively. By the end of the trading hour (still from the perspective of the current time zone), if there are any open positions, we clear them out.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/London%20Breakout%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/london%20breakout%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/london%20breakout%20thresholds.png)

### 5. Awesome oscillator

Awesome oscillator is an upgraded version of MACD oscillator. It is one of those momentum strategies focusing on the game of moving average. Instead of taking simple moving average on close price, awesome moving average is derived from the mean of high and low price. Similar to MACD oscillator, it takes both short term and long term moving averages to construct the oscillator.

There are various strategies for awesome oscillator to generate signals, such as traditional moving average divergence, twin peaks and saucer. Twin peaks is just one of the many names of bottom W pattern. The pattern recognition will be covered in another chapter so the main focus of this chapter is saucer. Saucer is slightly more complex to implement than the traditional divergence. In return, saucer has the power to beat the slow response of the traditional divergence. Generally speaking, a faster response may sound awesome, but it does not guarantee a less risky outcome or a more profitable outcome. Hence, we will take MACD oscillator as a control group, to test if awesome oscillator can actually outperform MACD oscillator.

The rules of awesome oscillator could be found in <a href=https://www.tradingview.com/wiki/Awesome_Oscillator_(AO)>TradingView</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Awesome%20Oscillator%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/awesome%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/awesome%20oscillator.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/awesome%20ma.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/awesome%20asset.png)

### 6. Oil Money project

This project is inspired by an <a href=https://www.bloomberg.com/news/articles/2018-05-20/crude-oil-s-surge-is-putting-the-petro-back-in-petrocurrencies>article</a> on oil-backed foreign exchange. Amid the bullish outlook for crude oil, the currency exchange of oil producing countries would also bounce back. Does this statement really hold? 

According to the article by Bloomberg (or many other similar research), researchers examine the correlation between petrocurrency and oil price, instead of the causality. But correlation does not equal to causality. Correlation could be a coincidence of a math game. We simply cannot draw the conclusion that oil price moves the currency. Some researchers even use bootstrapping which greatly destroys the autocorrelation of a time series. Thus, it is vital to apply academic analysis and computer simulation on some petrocurrencies to test the causality of oil.

*For more details, please refer to the <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Oil%20Money%20project/README.md>read me page</a> of a separate directory or <a href=https://je-suis-tm.github.io/quant-trading/oil-money>quant trading section</a> on my personal blog.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/Oil%20Money%20project/preview/oil%20production%20bubble%20map.png)

### 7. Dual Thrust

If you search dual thrust on google, you will end up with results of rocket engine. Don't panic yet, you can rest assured that dual thrust strategy is nowhere near rocket science. It is just an opening range breakout strategy developed by the founder of Universal Technical Systems. The mathematics involved in this strategy is merely primary school level.

Initially we establish upper and lower thresholds based on previous days' open, close, high and low. When the market opens and the price exceeds certain thresholds, we would take long/short positions prior to upper/lower thresholds. The strategy is quite useful in intra daily trading. However, there is no stop loss/profit position in this strategy. We reverse our positions when the price goes from one threshold to the other. We need to clear all positions by the end of the day.

Rules of dual thrust can be found in <a href=https://www.quantconnect.com/tutorials/dual-thrust-trading-algorithm>QuantConnect</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Dual%20Thrust%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/dual%20thrust%20positions.png)

### 8. Parabolic SAR

Parabolic SAR is an indicator to identify stop and reverse of a trend. Usually, Parabolic SAR is presented as dotted line either above or below the price in charts. When the price is an uptrend, SAR curve would sit below the price. When the price is downtrend, SAR curve would rise above the price. Parabolic SAR is always considered as a symbol of resistance to the price momentum. When SAR curve and the price curve cross over, it is when trade orders are supposed to be executed. 

The building of this strategy seems very simple, but the construction of the indicator is extremely painful due to the involvement of recursive calculation. Illustration on how to compute Parabolic SAR can be found in <a href=https://en.wikipedia.org/wiki/Parabolic_SAR>Wikipedia</a> but it is not very well explained. To get a clear idea of the calculation, my personal recommendation is to take a look at the <a href=https://www.box.com/s/gbtrjuoktgyag56j6lv0>spreadsheet</a> made by joeu2004.

It is worth mentioning that SAR and RSI (which will be featured in a later chapter) shares the same founder, Welles Wilder. The guy is a real legend who used to work as mechanical engineer and real estate developer and later became a technical analyst. His book on technical trading system is a must-read for anyone that wants to elevate quant trading system to the next level.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Parabolic%20SAR%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/parabolic%20sar%20positions.png)

### 9. Bollinger Bands Pattern Recognition

Bollinger Bands is a very simple but powerful indicator. There are three bands of this indicator. The mid band is the moving average on the price series (usually takes 20 lags). The upper and lower bands are two moving standard deviations away from the mid band. Bollinger Bands can be used to test for various types of strategies. 

For volatility trading, contraction and expansion of the band width are crucial elements. Any distinct momentum clustering (it can take form of either upward or downward) would result in a Bollinger Bands expansion. And the oscillation in a horizontal channel would result in a Bollinger Bands contraction. 

For momentum trading, the phenomenon of 'walking the band' indicates the resistance and support level of the underlying asset. In a strong trend, the price constantly attempts to touch or break through the upper/lower band along with Bollinger Bands moving towards the same direction.

For pattern recognition, Bollinger Bands has the capability of testing bottom W, top M, head-shoulder patterns, etc. With upper and lower bands served as an interval, it is easier to identify the hidden pattern in the historical data.

More details of Bollinger Bands can be found in <a href=https://www.tradingview.com/wiki/Bollinger_Bands_(BB)>TradingView</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Bollinger%20Bands%20Pattern%20Recognition%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/bollinger%20bands%20positions.png)

### 10. Relative Strength Index Pattern Recognition

RSI (Relative Strength Index) is also a popular indicator. It reflects the current strength/weakness of the stock price momentum. The calculation is pretty straight forward. We use 14 days of smoothed moving average (or other moving average methods) to separately calculate the intra daily uptrend and downtrend. We denote uptrend moving average divided by downtrend moving average as the relative strength. We normalize the relative strength by 100 which becomes an index called RSI. It is commonly believed that RSI above 70 is overbought and RSI below 30 is oversold. This is the simplest way to trade on RSI (as shown in the pictures below). Nonetheless, there could be divergence between RSI momentum and price momentum which will not be covered in the script. The effectiveness of any divergence strategy on RSI is rather debatable.

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/rsi%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/rsi%20oscillator.png)

If you are looking for something slightly more complex, well, we can apply pattern recognition technique to RSI as well. Unlike strategy No.9 Bollinger Bands, we can directly look at the patterns of RSI itself instead of the price. Since we have tested double bottom pattern in Bollinger Bands, we would test head-shoulder pattern on RSI this time.

For details of head-shoulder pattern, please refer to <a href=https://www.investopedia.com/terms/h/head-shoulders.asp>Investopedia</a>.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/RSI%20Pattern%20Recognition%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/rsi%20pattern%20positions.png)

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/rsi%20pattern%20oscillator.png)

### 11. Monte Carlo project

Monte Carlo, my first thought on these two words is the grand casino, where you meet Famke Janssen in tuxedo and introduce yourself, 'Bond, James Bond'. Indeed, the simulation is named after the infamous casino. It actually refers to the computer simulation of massive amount of random events. This unconventional mathematical method is extremely powerful in the study of stochastic process. 

Here comes the argument on Linkedin that caught my eyes the other day. "Stock price can be seemed as a Wiener Process. Hence, we can use Monte Carlo simulation to predict the stock price." said a data science blog. Well, in order to be a Wiener Process, we have to assume the stock price is continuous in time. In reality, the market closes. The overnight volatility exists. But that is not the biggest issue here. The biggest issue is, can we really use Monte Carlo simulation to predict the stock price, even a range or its direction?

*For more details, please refer to the <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Monte%20Carlo%20project/README.md>read me</a> page of a separate directory or <a href=https://je-suis-tm.github.io/quant-trading/monte-carlo>quant trading</a> section on my personal blog.*

![alt text](https://raw.githubusercontent.com/je-suis-tm/quant-trading/master/Monte%20Carlo%20project/preview/ge%20simulation2.png)

### 12. Options Straddle

Here marks the debut of options strategy in this repository. Straddle refers to the shape of compasses in the payoff diagram of the strategy. A long straddle involves buying a call option and a put option at the same strike price, the same expiration date and preferably the same price. In reality, the same price is not always feasible (call options price higher implies higher upside risk, vice versa). It is recommended to trade when the price disparity between call and put options is converging.

Long straddle is commonly seen in event driven strategy, e.g. political referendum, company earning release. It profits from the uncertainty of both-side risk. For upside risk, the potential profit is unlimited. The potential loss does not come from the downside risk (there is limited gain from downside risk). Instead, it comes from the stagnant price due to insufficient volatility. In this case, short straddle is more suitable for sideways choppy market.

The crucial element of options straddle is the selection of the strike price. As the price of options contains the market consensus, the only way to maximize the profit is to find the optimal strike price to shrink the loss bandwidth. This is where the economists kick in and offer base case outlook plus best/worst scenarios. In contrast to the common misunderstanding of quantitative trading, Option Greeks are no silver bullet. Quantitative combined with fundamental in one, so-called quantamental, makes the portfolio impeccable.

*Click <a href=https://github.com/je-suis-tm/quant-trading/blob/master/Options%20Straddle%20backtest.py>here</a> to be redirected to the script.*

![alt text](https://github.com/je-suis-tm/quant-trading/blob/master/preview/options%20straddle%20payoff%20diagram.png)

### 13. Portfolio Optimization project

Modern portfolio theory was introduced in 1952 by Nobel laureate Harry Markowitz. It is part of investment class 101. But I watched a video by <a href=https://www.wolfram.com/training/videos/FIN015>Wolfram</a> recently. It challenged the traditional approach and introduced graph theory to asset diversification. There are plenty of quant shops deploying fancy mathematic tools to solve the market. The real question for us is, as fancy as it sounds, does graph theory work on portfolio optimization?

![alt text](https://github.com/je-suis-tm/graph-theory/blob/master/Portfolio%20Optimization%20project/preview/outta%20sample%20mean%20variance.png)

*This project is documented in the repository of <a href=https://github.com/je-suis-tm/graph-theory>Graph Theory</a>. For more details, please refer to the <a href=https://github.com/je-suis-t
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `Ore Money project/iron ore production/iron ore production bubble map.py`
```python
# coding: utf-8

# In[1]:


#installing basemap is pretty painful for anaconda
#try conda install -c conda-forge basemap
#if there is filenotfounderror
#try conda install -c conda-forge proj4
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import os
os.chdir('d:/')


# In[2]:


#need data with value and coordinates to plot
#the iron ore production data of 2015 comes from wikipedia
# https://en.wikipedia.org/wiki/List_of_countries_by_iron_ore_production
#the coordinates of each country's capital come from someone's personal blog
# https://lab.lmnixon.org/4th/worldcapitals.html
#note that the capital doesnt necessarily locate at the centre of a country
#to make the figure look better, i slightly change the coordinates
df=pd.read_csv('iron ore production bubble map.csv')


# In[3]:


ax=plt.figure(figsize=(50,20)).add_subplot(111)

#draw up a world map
#fill continents, lakes and country boundaries
m = Basemap()
m.drawmapboundary(fill_color='white', linewidth=0)
m.fillcontinents(color='#c0c0c0',alpha=0.5, lake_color='white')
m.drawcountries(linewidth=1,color='#a79c93')

size=df['iron ore production']/max(df['iron ore production'])*40000

#this is crucial if we use a different map projection
x,y=m(df['longitude'].tolist(),df['latitude'].tolist())

m.scatter(x,y, s=size, linewidths=2, edgecolors="#6c6b74",           
          alpha=0.8,c=df['iron ore production'],cmap='autumn_r')

for i in range(len(x)):
    plt.text(x[i],y[i],               
             '%s '%(df['region'][i]),              
             horizontalalignment='center', 
            verticalalignment='center', 
             size=25)

cb=plt.colorbar(ticks=[10000,800000])
cb.ax.set_yticklabels(cb.ax.get_yticklabels(), fontsize=20)
cb.ax.set_ylabel('Iron Ore Production 1000 Tonnes per Year',fontsize=20,rotation=270)
plt.title('Iron Ore Production by Countries', fontsize=42)

plt.show()
```

#### File: `Oil Money project/oil production/oil production choropleth.py`
```python
# coding: utf-8

# In[1]:


import folium
import os
os.chdir('h:/')
import pandas as pd


# In[2]:


#this table comes from wikipedia
# https://en.wikipedia.org/wiki/List_of_countries_by_oil_production
#but i have changed the names of some countries
#try to keep names consistent with geojson file
df=pd.read_csv('oil production choropleth.csv')


# In[3]:


df['Oil Production']=df['Oil Production'].apply(lambda x: x/1000)


# In[4]:


#location takes two arguments, latitude and longitude
#zoom_start implies zoom level
#1 is world map, 2 is continent map, 3 is region map
#4 is country map, 5 is county map etc
m=folium.Map(location=(30,50), zoom_start=4)

#geo_data is a geojson file
#its a file that indicates country shape on a map
#we can download country and even more detailed level from the first link
#the second link converts all the files in first link to geojson
#https://gadm.org/download_country_v3.html
#https://mapshaper.org/
#here i found the map shape from github
#i just cannot find the original link
#so i just upload it to the repo

#data is the dataframe
#columns would be the columns we use in that dataframe
#we need one column for the region name and the other one for value
#the region name should be consistent with the region name in geojson
#and key_on denotes the key in geojson for region names
#fill_color is just matplotlib cmap
#fill_opacity,line_opacity are plotting options
#legend_name is just the name of the label in matplotlib
#threshold_scale can only take up to six values in a list
#for simplicity, we can use from branca.utilities import split_six
#to get the quantile data equally divided into six parts
m.choropleth(
 geo_data=(open("worldmapshape.json",encoding = "utf_8_sig").read()),
 name='choropleth',
 data=df,
 columns=['Country', 'Oil Production'],
 key_on='properties.name',
 fill_color='YlOrRd',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Oil Production Thousand Barrels/Day',
 threshold_scale=[0.0,1.0, 150.0, 800.0, 2000.0, 4000.0]
)

#layout control is just a map filter
#we can unselect choropleth any time
folium.LayerControl().add_to(m)
display(m)

#in general, folium is a really good wrap up for leaflet.js
#it saves me a lot of time from learning javascript
#it is very straight forward, a very flat learning curve
#there is only one thing i hate about it
#which is the location name is always in local language
#at least google map provides english plus local language
#this is quite annoying, other than that, its pretty cool
```

#### File: `Smart Farmers project/check consistency.py`
```python
# coding: utf-8

# In[1]:


import os
os.chdir('H:/')
import pandas as pd


# In[2]:


prod=pd.read_csv('Production_Crops_E_All_Data_(Normalized).csv',
                 encoding='latin-1')

prix=pd.read_csv('Prices_E_All_Data_(Normalized).csv',
                 encoding='latin-1')

land=pd.read_csv('Inputs_LandUse_E_All_Data_(Normalized).csv',
                 encoding='latin-1')


# In[3]:


global beginyear,endyear
beginyear=2012;
endyear=2019


# In[4]:


mapping=pd.read_csv('mapping.csv')


# In[5]:


#select malaysia from 2012-2018
malay_land=land[land['Year'].isin(range(beginyear,endyear))][land['Area']=='Malaysia'][land['Element'].isin(['Area'])][land['Item'].isin(['Cropland'])]

malay_prod=prod[prod['Year'].isin(range(beginyear,endyear))][prod['Area']=='Malaysia'][prod['Element'].isin(['Area harvested','Production'])]

malay_prod=malay_prod.merge(mapping,on=['Item Code', 'Item'],how='left')


# In[6]:


#remove redundant cols
for i in ['Area Code','Element Code','Year Code',
         'Flag','COMMODITY','Item Code',
          'subclass code','class code',
          'DEFINITIONS, COVERAGE, REMARKS',]:
    del malay_prod[i]


# In[7]:


#select crops with available data
a=set(malay_prod['Item'][malay_prod['Element']=='Area harvested'])

b=set(malay_prod['Item'][malay_prod['Element']=='Production'])

target_crops=a.intersection(b)


# In[8]:


#exclude land usage<1% without price data
exclude=['Areca nuts',
 'Bastfibres, other',
 'Cashew nuts, with shell',
 'Cereals, Total',
 'Chillies and peppers, dry',
 'Citrus Fruit, Total',
 'Cloves',
 'Coarse Grain, Total',
 'Coffee, green',
 'Coir',
 'Fibre Crops Primary',
 'Fruit Primary',
 'Fruit, citrus nes',
 'Fruit, fresh nes',
 'Fruit, tropical fresh nes',
 'Groundnuts, with shell',
 'Manila fibre (abaca)',
 'Nutmeg, mace and cardamoms',
 'Oilcrops',
 'Oilcrops, Cake Equivalent',
 'Oilcrops, Oil Equivalent',
 'Roots and Tubers, Total',
 'Roots and tubers nes',
 'Soybeans',
 'Spices nes',
 'Tea',
 'Treenuts, Total',
 'Vegetables Primary',
 'Vegetables, fresh nes']


# In[9]:


#finalize the target
targets=[i for i in target_crops if i not in exclude]


# In[10]:


#cleanse
malay_crops=malay_prod[malay_prod['Item'].isin(targets)]


# In[11]:


#subtotal
total=malay_prod[malay_prod['class'].isnull()]


# In[12]:


#compare sum of area by crops with sum of area by subclass
sss=total[total['Element']=='Area harvested'].groupby(['Item','Year']).sum()

ttt=malay_crops[malay_crops['Element']=='Area harvested'].groupby(['class','Year']).sum()


# In[13]:


#compare sum of area by crops
malay_crops[malay_crops['Element']=='Area harvested'].groupby(['Year']).sum()


# In[14]:


#with cropland
malay_land
```

#### File: `Smart Farmers project/country selection.py`
```python
# coding: utf-8

# In[1]:


target_country=['Australia','Spain',
 'Morocco',
 'United Kingdom',
 'Poland',
 'France',
 'Mexico',
 'Bangladesh',
 'Canada',
 'Viet Nam',
 'Thailand',
 'Guatemala',
 'Colombia',
 'Germany',
 'China',
 'Brazil',
 'India',
 'United States of America',
 'Malaysia',
 'Indonesia']


# In[2]:


target_year=[2000,
 2001,
 2002,
 2003,
 2004,
 2005,
 2006,
 2007,
 2008,
 2009,
 2010,
 2011,
 2012,
 2013,
 2014,
 2015,
 2016,
 2017]


# In[3]:


import pandas as pd
import numpy as np
import os
os.chdir('H:/')


# In[4]:


prod=pd.read_csv('Production_Crops_E_All_Data_(Normalized).csv',encoding='latin-1')


# In[5]:


prix=pd.read_csv('Prices_E_All_Data_(Normalized).csv',encoding='latin-1')


# In[6]:


echanger=pd.read_csv('Trade_Crops_Livestock_E_All_Data_(Normalized).csv',encoding='latin-1')


# In[7]:


#only compare crops with available data
target_crops=set(prod['Item']).intersection(set(prix['Item'])).intersection(set(echanger['Item']))


# # volume

# In[8]:


#extract export volume
trade=echanger[echanger['Element']=='Export Quantity']


# In[9]:


#cleanse
trade=trade[trade['Item'].isin(target_crops)]

trade=trade[trade['Area'].isin(target_country)]

trade=trade[trade['Year'].isin(target_year)]

trade=trade[['Area','Year','Item','Value']]


# In[10]:


#extract production data
prod=prod[prod['Element']=='Production']


# In[11]:


#cleanse
prod=prod[prod['Item'].isin(target_crops)]

prod=prod[prod['Area'].isin(target_country)]

prod=prod[prod['Year'].isin(target_year)]

prod=prod[['Area','Year','Item','Value']]


# In[12]:


#group by sum
export=trade.groupby(['Area','Year']).sum()


# In[13]:


#group by sum
supply=prod.groupby(['Area','Year']).sum()


# In[14]:


#create new dataframe to compute export volume percentage
pourcent=pd.DataFrame(index=export.index)


# In[15]:


#compute percentage
pourcent['value']=np.divide(export['Value'].tolist(),supply['Value'].tolist())


# In[16]:


#clean up index
pourcent.reset_index(inplace=True)


# In[17]:


#historical average
mean_pourcent=pourcent[['Area','value']].groupby('Area').mean()


# In[18]:


#sort by percentage
mean_pourcent=mean_pourcent.sort_values('value')


# In[19]:


#export percentage for a particular year
pourcent[pourcent['Year'].isin([2017])].sort_values('value')


# # price

# In[20]:


#get usd price
prix=prix[prix['Element']=='Producer Price (USD/tonne)']


# In[21]:


#cleanse
prix=prix[prix['Item'].isin(target_crops)]

prix=prix[prix['Area'].isin(target_country)]

prix=prix[prix['Year'].isin(target_year)]

prix=prix[['Area','Year','Item','Value']]


# In[22]:


#previously we examine the volume
#now we focus on value
value=prod.merge(prix,on=['Area','Year','Item'],how='inner')


# In[23]:


#volume times unit price equals to total value
value['Value']=np.multiply(value['Value_x'],value['Value_y'])


# In[24]:


#cleanse
value=value[['Area','Year','Item','Value']]


# In[25]:


#get export price
exchange=echanger[echanger['Element']=='Export Value']


# In[26]:


#cleanse
exchange=exchange[exchange['Item'].isin(target_crops)]

exchange=exchange[exchange['Area'].isin(target_country)]

exchange=exchange[exchange['Year'].isin(target_year)]

exchange=exchange[['Area','Year','Item','Value']]


# In[27]:


#group by sum
temp1=exchange.groupby(['Area','Year']).sum()


# In[28]:


#group by sum
temp2=value.groupby(['Area','Year']).sum()


# In[29]:


#inner join
temp=temp1.merge(temp2,on=['Area','Year'],how='inner')


# In[30]:


#create dataframe to compute export value percentage
percentage=pd.DataFrame(index=temp.index)


# In[31]:


#compute export value percentage
percentage['value']=np.divide(temp['Value_x'],temp['Value_y'])


# In[32]:


#clean up
percentage.reset_index(inplace=True)


# In[33]:


#historical average
mean_percentage=percentage[['Area','value']].groupby('Area').mean()


# In[34]:


#sort by percentage
mean_percentage=mean_percentage.sort_values('value')


# In[35]:


#export percentage for a particular year
percentage[percentage['Year'].isin([2016])].sort_values('value')
```

#### File: `MACD Oscillator backtest.py`
```python
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 11:57:46 2018

@author: Administrator
"""

# In[1]:

#need to get fix yahoo finance package first

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import fix_yahoo_finance as yf



# In[2]:

#simple moving average
def macd(signals):
    
    
    signals['ma1']=signals['Close'].rolling(window=ma1,min_periods=1,center=False).mean()
    signals['ma2']=signals['Close'].rolling(window=ma2,min_periods=1,center=False).mean()
    
    return signals



# In[3]:

#signal generation
#when the short moving average is larger than long moving average, we long and hold
#when the short moving average is smaller than long moving average, we clear positions
#the logic behind this is that the momentum has more impact on short moving average
#we can subtract short moving average from long moving average
#the difference between is sometimes positive, it sometimes becomes negative
#thats why it is named as moving average converge/diverge oscillator
def signal_generation(df,method):
    
    signals=method(df)
    signals['positions']=0

    #positions becomes and stays one once the short moving average is above long moving average
    signals['positions'][ma1:]=np.where(signals['ma1'][ma1:]>=signals['ma2'][ma1:],1,0)

    #as positions only imply the holding
    #we take the difference to generate real trade signal
    signals['signals']=signals['positions'].diff()

    #oscillator is the difference between two moving average
    #when it is positive, we long, vice versa
    signals['oscillator']=signals['ma1']-signals['ma2']

    return signals



# In[4]:

#plotting the backtesting result
def plot(new, ticker):
    
    #the first plot is the actual close price with long/short positions
    fig=plt.figure()
    ax=fig.add_subplot(111)
    
    new['Close'].plot(label=ticker)
    ax.plot(new.loc[new['signals']==1].index,new['Close'][new['signals']==1],label='LONG',lw=0,marker='^',c='g')
    ax.plot(new.loc[new['signals']==-1].index,new['Close'][new['signals']==-1],label='SHORT',lw=0,marker='v',c='r')

    plt.legend(loc='best')
    plt.grid(True)
    plt.title('Positions')
    
    plt.show()
    
    #the second plot is long/short moving average with oscillator
    #note that i use bar chart for oscillator
    fig=plt.figure()
    cx=fig.add_subplot(211)

    new['oscillator'].plot(kind='bar',color='r')

    plt.legend(loc='best')
    plt.grid(True)
    plt.xticks([])
    plt.xlabel('')
    plt.title('MACD Oscillator')

    bx=fig.add_subplot(212)

    new['ma1'].plot(label='ma1')
    new['ma2'].plot(label='ma2',linestyle=':')
    
    plt.legend(loc='best')
    plt.grid(True)
    plt.show()

    
# In[5]:

def main():
    
    #input the long moving average and short moving average period
    #for the classic MACD, it is 12 and 26
    #once a upon a time you got six trading days in a week
    #so it is two week moving average versus one month moving average
    #for now, the ideal choice would be 10 and 21
    
    global ma1,ma2,stdate,eddate,ticker,slicer

    #macd is easy and effective
    #there is just one issue
    #entry signal is always late
    #watch out for downward EMA spirals!
    ma1=int(input('ma1:'))
    ma2=int(input('ma2:'))
    stdate=input('start date in format yyyy-mm-dd:')
    eddate=input('end date in format yyyy-mm-dd:')
    ticker=input('ticker:')

    #slicing the downloaded dataset
    #if the dataset is too large, backtesting plot would look messy
    #you get too many markers cluster together
    slicer=int(input('slicing:'))

    #downloading data
    df=yf.download(ticker,start=stdate,end=eddate)
    
    new=signal_generation(df,macd)
    new=new[slicer:]
    plot(new, ticker)


#how to calculate stats could be found from my other code called Heikin-Ashi
# https://github.com/je-suis-tm/quant-trading/blob/master/heikin%20ashi%20backtest.py


if __name__ == '__main__':
    main()
```

#### File: `Oil Money project/oil production/oil production cost curve.py`
```python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('d:/')
import pandas as pd


# In[2]:


#traditional commodity cost curve
#input two pandas series, the third one is optional
def cost_curve(x,y1,y2=None,
               hline_var=0,hline_color='k',hline_name='',
               colormap='tab20c',legends=None,notes=None,
               ylabel='',xlabel='',title='',fig_size=(10,5)):
    y2 = [] if y2 is None else y2
    legends = [] if legends is None else legends
    notes = [] if notes is None else notes
    
    ax=plt.figure(figsize=fig_size).add_subplot(111)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    #set bar location on x axis
    wid=x
    cumwid=[0]
    for i in range(1,len(wid)):
        cumwid.append(wid[i-1]+cumwid[-1])

    #assign colors to different bars from cmap
    cmap=plt.cm.get_cmap(colormap)
    colors=[cmap(i) for i in np.linspace(0,1,len(y1))]
    colors2=[tuple([i/1.3 for i in j if i!=1]+[1.0]) for j in colors]
    
    for i in range(len(y1)):
        plt.bar(cumwid[i],            
                y1[i],width=wid[i],label=legends[i] if len(legends)>0 else '',
                   color=colors[i],align='edge')
        
        if len(y2)>0:
            plt.bar(cumwid[i],            
                    y2[i],width=wid[i],
                   color=colors2[i],bottom=y1[i],align='edge'
                   )
    
    #plot percentile line if needed
    plt.axhline(y=hline_var, linestyle='--',
                c=hline_color,label=hline_name)

    plt.title(title,pad=20)
    ax.yaxis.labelpad=10
    ax.xaxis.labelpad=10
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    
    #slightly expand x axis to look nicer
    plt.xlim(min(cumwid),max(cumwid)+list(wid)[-1])
    plt.xticks([min(cumwid),
                np.mean([min(cumwid),
                         max(cumwid)+list(wid)[-1]]),
                1.01*max(cumwid)+list(wid)[-1]])
    
    #if cost curve breakdown is provided
    #add legends to the right
    if len(y2)>0:
        plt.text(1.1*max(cumwid)+list(wid)[-1],
             list(y1)[-1]/2,notes[0],
                 verticalalignment='center', horizontalalignment='center')
        plt.text(1.1*max(cumwid)+list(wid)[-1],
             list(y1)[-1]+list(y2)[-1]/2,notes[1],
                verticalalignment='center', horizontalalignment='center')
    
    #legends of cost curve for different entities is plotted below the chart
    plt.legend(loc=6,bbox_to_anchor=(0.12, -0.4), ncol=4)    
    
    plt.show()
    


# In[3]:

#why there is only 2015 data?
#well, they said data is the new oil
#especially true when it comes to oil data

#i can only find oil production cost data of 2015 from the below address
# https://www.statista.com/statistics/597669/cost-breakdown-of-producing-one-barrel-of-oil-in-the-worlds-leading-oil-producing-countries/
#and i have to do some scraping to actually get the data
#if u dont know scraping, that will be a problem
#data scientists cant wait for engineers to feed you data
#maybe its time for you to learn
# https://github.com/je-suis-tm/web-scraping

#also you can use oil breakeven price to replace cost data
#the following two links contain quite a lot of information
#sadly, fiscal breakeven price is widely used by opec countries
#if u have other countries in mind, you will be disappointed
# https://www.cfr.org/report/interactive-oil-exporters-external-breakeven-prices
# http://graphics.wsj.com/oil-barrel-breakdown/

#daily production data and proven reserve comes from bp
# https://www.bp.com/en/global/corporate/energy-economics/statistical-review-of-world-energy.html
#production capacity is a typical x axis for cost curve
#you can find them from imf or eia, but again, only for opec countries
#therefore, i used daily production data as alternative
# https://www.imf.org/~/media/Files/Publications/REO/MCD-CCA/2018/May/English/mreo0518-statisticalappendix-elsx.ashx
# https://www.eia.gov/opendata/qb.php?sdid=STEO.COPC_AG.A

df=pd.read_csv('global oil cost curve.csv')


# In[4]:


cost_curve(df['Daily production mil barrels'],
           df['Operational cost dollar per barrel'],
           df['Capital cost dollar per barrel'],
           legends=df['Country'],
           notes=['Operational Cost','Capital Cost'],
           hline_var=np.percentile(df['Total cost dollar per barrel'],90),
           hline_color='#e08314',
           hline_name='90% Percentile',
           xlabel='Daily Production, Million Barrels',
           ylabel='US Dollar per Barrel',
           title='2015 Global Oil Cost Curve')
```


==================================================


## [2/3] Repository: rda-stock-trading (`WHEEL_rda-stock-trading`)
- **Full Name**: `rda-stock-trading`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# RDA Stock Trading Bot

Algorithmic trading system for Indian equities (Nifty 500) using Dhan API.

## Project Configuration

| Setting | Value |
|---|---|
| **Broker** | Dhan (free API + paper trading) |
| **Capital (Phase 1)** | ₹1,00,000 |
| **Universe** | Nifty 500 |
| **Hosting (Phase 1)** | Home PC during market hours (09:15 – 15:30 IST) |
| **Hosting (Phase 2)** | Oracle Cloud Always Free VPS |
| **Risk per trade** | 2% of capital (₹2,000 max) |
| **Max open positions** | 5 |

## Architecture — Multi-Agent System

The system is split into 6 specialized agents, each with a single responsibility:

```
agents/
├── research/        News, earnings calendar, corporate actions, sector signals
├── fundamental/     Screener filters (P/E, ROE, debt, growth), F&O ban check
├── technical/       Indicators (RSI, MACD, EMA), patterns, entry/exit signals
├── risk/            Position sizing, stop-loss placement, exposure limits
├── execution/       Dhan API integration — order placement, status, fills
└── portfolio/       P&L tracking, daily MTM, STCG/LTCG bookkeeping
```

## Folder Structure

```
stock-trading/
├── agents/             Trading agents (see above)
├── strategies/         Strategy implementations (momentum, mean-reversion, etc.)
├── backtests/          Backtest scripts and results
├── data/               Historical data, instrument lists, cache
├── logs/               Trade logs, error logs, daily snapshots
├── config/             config.yaml — all tunable parameters
├── utils/              Logger, helpers, common utilities
├── tests/              Unit tests for each agent
├── notebooks/          Jupyter notebooks for analysis
├── main.py             Orchestrator — runs the daily cycle
├── requirements.txt    Python dependencies
├── .env.example        Template for API keys (copy to .env)
└── .gitignore          Excludes .env, logs, data, __pycache__
```

## Setup (Week 1)

1. **Install Python 3.10+**
2. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate    # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure credentials**
   ```bash
   copy .env.example .env
   # Edit .env with your Dhan client_id and access_token
   ```
5. **Initialize git + GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial scaffold"
   git remote add origin https://github.com/<your-username>/rda-stock-trading.git
   git push -u origin main
   ```

## Roadmap

- **Week 1** — Scaffold + Dhan API connectivity test (paper account)
- **Week 2** — Technical agent + 1 strategy on paper trading
- **Week 3** — Risk + execution layer
- **Week 4** — Portfolio tracking + daily reports
- **Phase 2** — Migrate to Oracle Cloud, add fundamental + research agents
- **Phase 3** — Go live with ₹1L capital after 4+ weeks of profitable paper trading

## Key Principles

1. **Paper trade first** — never go live without 4 weeks of profitable paper results.
2. **Risk first, returns second** — every trade must have stop-loss before entry.
3. **Log everything** — every signal, order, fill, error. Critical for debugging.
4. **Version control everything** — commit working code, tag releases for production.

## Disclaimer

Algorithmic trading involves financial risk. Past backtest performance does not guarantee future returns. Use paper trading to validate strategies before deploying real capital.

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `agents/strategies_v2/__init__.py`
```python

```

#### File: `dashboard/__init__.py`
```python

```

#### File: `dashboard_web/earnings.json`
```python
{"events":[]}
```

#### File: `data/_watchdog_state.json`
```python
{"date": "2026-05-25", "restarts": 5}
```

#### File: `agents/learning/__init__.py`
```python
"""Learning agents — daily reviews + parameter adaptation."""
```


==================================================


## [3/3] Repository: shark-bot (`WHEEL_shark-bot`)
- **Full Name**: `shark-bot`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Comprehensive Architectural Blueprint & Signal Pipeline
- **Role in Quantitative Pipeline**: High-performance execution, signal feature extraction, risk parity constraint management, and microsecond DMA order dispatch.
- **Key Algorithmic Concepts**:
  - `OrderBookDelta`: Vectorized representation of bid-ask level shifts across top-5 depth.
  - `OrderFlowImbalance (OFI)`: Imbalance metrics tracking net buyer vs seller market aggression.
  - `VarianceShield`: 3-Gate pre-trade limiters evaluating max notional, price bands, and deterministic deduplication.
- **Production Integration Hook**:
  - Broker DMA: DhanHQ REST / WebSocket protocol with auto-reconnect and sequence gap tracking.
  - Risk Governor: SEBI 2026 Order-to-Trade Ratio limiter maintaining OTR <= 1.0.


==================================================
