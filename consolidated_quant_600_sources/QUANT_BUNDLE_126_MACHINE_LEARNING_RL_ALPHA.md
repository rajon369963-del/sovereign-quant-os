# ⚡ [QUANT-SOURCE-126] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_126_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Flow_Imbalance_Strategy (`WHEEL_MicrostructureAlphaEngine-Order_Flow_Imbalance_Strategy`)
- **Full Name**: `MicrostructureAlphaEngine-Order_Flow_Imbalance_Strategy`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)


### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `scripts/train_model.py`
```python

```

#### File: `scripts/generate_report.py`
```python

```

#### File: `scripts/collect_data.py`
```python

```

#### File: `src/__init__.py`
```python

```

#### File: `src/features/book_features.py`
```python

```


==================================================


## [2/3] Repository: StockPredictionAI (`WHEEL_StockPredictionAI`)
- **Full Name**: `StockPredictionAI`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Using the latest advancements in AI to predict stock market movements

 


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;In this notebook I will create a complete process for predicting stock price movements. Follow along and we will achieve some pretty good results. For that purpose we will use a **Generative Adversarial Network** (GAN) with **LSTM**, a type of Recurrent Neural Network, as generator, and a Convolutional Neural Network, **CNN**, as a discriminator. We use LSTM for the obvious reason that we are trying to predict time series data. Why we use GAN and specifically CNN as a discriminator? That is a good question: there are special sections on that later.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will go into greater details for each step, of course, but the most difficult part is the GAN: very tricky part of successfully training a GAN is getting the right set of hyperparameters. For that reason we will use **Bayesian optimisation** (along with Gaussian processes) and **Reinforcement learning** (RL) for deciding when and how to change the GAN's hyperparameters (the exploration vs. exploitation dilemma). In creating the reinforcement learning we will use the most recent advancements in the field, such as **Rainbow** and **PPO**.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will use a lot of different types of input data. Along with the stock's historical trading data and technical indicators, we will use the newest advancements in **NLP** (using 'Bidirectional Embedding Representations from Transformers', **BERT**, sort of a transfer learning for NLP) to create sentiment analysis (as a source for fundamental analysis), **Fourier transforms** for extracting overall trend directions, **Stacked autoencoders** for identifying other high-level features, **Eigen portfolios** for finding correlated assets, autoregressive integrated moving average (**ARIMA**) for the stock function approximation, and many more, in order to capture as much information, patterns, dependencies, etc, as possible about the stock. As we all know, the more (data) the merrier. Predicting stock price movements is an extremely complex task, so the more we know about the stock (from different perspectives) the higher our changes are.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For the purpose of creating all neural nets we will use MXNet and its high-level API - Gluon, and train them on multiple GPUs.

**Note:** _Although I try to get into details of the math and the mechanisms behind almost all algorithms and techniques, this notebook is not explicitly intended to explain how machine/deep learning, or the stock markets, work. The purpose is rather to show how we can use different techniques and algorithms for the purpose of accurately predicting stock price movements, and to also give rationale behind the reason and usefulness of using each technique at each step._

_Notebook created: January 9, 2019_.


**Figure 1 - The overall architecture of our work**

<center><img src='imgs/main.jpg' width=1060></img></center>

## Table of content
* [Introduction](#overview)
* [Acknowledgement](#acknowledgement)
* [The data](#thedata)
    * [Correlated assets](#corrassets)
    * [Technical indicators](#technicalind)
    * [Fundamental analysis](#fundamental)
        - [Bidirectional Embedding Representations from Transformers - BERT](#bidirnlp)
    * [Fourier transforms for trend analysis](#fouriertransform)
    * [ARIMA as a feature](#arimafeature)
    * [Statistical checks](#statchecks)
        - [Heteroskedasticity, multicollinearity, serial correlation](#hetemultiser)
    * [Feature Engineering](#featureeng)
        * [Feature importance with XGBoost](#xgboost)
    * [Extracting high-level features with Stacked Autoencoders](#stacked_ae)
        * [Activation function - GELU (Gaussian Error)](#gelu)
        * [Eigen portfolio with PCA](#pca)
    * [Deep Unsupervised Learning for anomaly detection in derivatives pricing](#dulfaddp)
* [Generative Adversarial Network - GAN](#qgan)
    * [Why GAN for stock market prediction?](#whygan)
    * [Metropolis-Hastings GAN and Wasserstein GAN](#mhganwgan)
    * [The Generator - One layer RNN](#thegenerator)
        - [LSTM or GRU](#lstmorgru)
        - [The LSTM architecture](#lstmarchitecture)
        - [Learning rate scheduler](#lrscheduler)
        - [How to prevent overfitting and the bias-variance trade-off](#preventoverfitting)
        - [Custom weights initializers and custom loss metric](#customfns)
    * [The Discriminator - 1D CNN](#thediscriminator)
        - [Why CNN as a discriminator?](#why_cnn_architecture)
        - [The CNN architecture](#the_cnn_architecture)
    * [Hyperparameters](#hyperparams)
* [Hyperparameters optimization](#hyperparams_optim)
    * [Reinforcement learning for hyperparameters optimization](#reinforcementlearning)
        - [Theory](#reinforcementlearning_theory)
            - [Rainbow](#rl_rainbow)
            - [PPO](#rl_ppo)
        - [Further work on Reinforcement learning](#reinforcementlearning_further)
    * [Bayesian optimization](#bayesian_opt)
        - [Gaussian process](#gaussprocess)
* [The result](#theresult)
* [What is next?](#whatisnext)
* [Disclaimer](#disclaimer)

# 1. Introduction <a class="anchor" id="overview"></a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Accurately predicting the stock markets is a complex task as there are millions of events and pre-conditions for a particilar stock to move in a particular direction. So we need to be able to capture as many of these pre-conditions as possible. We also need make several important assumptions: 1) markets are not 100% random, 2) history repeats, 3) markets follow people's rational behavior, and 4) the markets are '_perfect_'. And, please, do read the **Disclaimer** at the <a href="#disclaimer">bottom</a>.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will try to predict the price movements of **Goldman Sachs** (NYSE: GS). For the purpose, we will use daily closing price from January 1st, 2010 to December 31st, 2018 (seven years for training purposes and two years for validation purposes). _We will use the terms 'Goldman Sachs' and 'GS' interchangeably_.

# 2. Acknowledgement <a class="anchor" id="acknowledgement"></a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Before we continue, I'd like to thank my friends <a href="https://github.com/manganganath">Nuwan</a> and <a href="https://github.com/Q4living">Thomas</a> without whose ideas and support I wouldn't have been able to create this work.

# 3. The Data <a class="anchor" id="thedata"></a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We need to understand what affects whether GS's stock price will move up or down. It is what people as a whole think. Hence, we need to incorporate as much information (depicting the stock from different aspects and angles) as possible. (We will use daily data - 1,585 days to train the various algorithms (70% of the data we have) and predict the next 680 days (test data). Then we will compare the predicted results with a test (hold-out) data. Each type of data (we will refer to it as _feature_) is explained in greater detail in later sections, but, as a high level overview, the features we will use are:

1. **Correlated assets** - these are other assets (any type, not necessarily stocks, such as commodities, FX, indices, or even fixed income securities). A big company, such as Goldman Sachs, obviously doesn't 'live' in an isolated world - it depends on, and interacts with, many external factors, including its competitors, clients, the global economy, the geo-political situation, fiscal and monetary policies, access to capital, etc. The details are listed later.
2. **Technical indicators** - a lot of investors follow technical indicators. We will include the most popular indicators as independent features. Among them - 7 and 21 days moving average, exponential moving average, momentum, Bollinger bands, MACD.
3. **Fundamental analysis** - A very important feature indicating whether a stock might move up or down. There are two features that can be used in fundamental analysis: 1) Analysing the company performance using 10-K and 10-Q reports, analysing ROE and P/E, etc (we will not use this), and 2) **News** - potentially news can indicate upcoming events that can potentially move the stock in certain direction. We will read all daily news for Goldman Sachs and extract whether the total sentiment about Goldman Sachs on that day is positive, neutral, or negative (as a score from 0 to 1). As many investors closely read the news and make investment decisions based (partially of course) on news, there is a somewhat high chance that if, say, the news for Goldman Sachs today are extremely positive the stock will surge tomorrow. _One crucial point, we will perform feature importance (meaning how indicative it is for the movement of GS) on absolutely every feature (including this one) later on and decide whether we will use it. More on that later_.<br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For the purpose of creating accurate sentiment prediction we will use Neural Language Processing (**NLP**). We will use **BERT** - Google's recently announced NLP approach for transfer learning for sentiment classification stock news sentiment extraction.
4. **Fourier transforms** - Along with the daily closing price, we will create Fourier transforms in order to generalize several long- and short-term trends. Using these transforms we will eliminate a lot of noise (random walks) and create approximations of the real stock movement. Having trend approximations can help the LSTM network pick its prediction trends more accurately.
5. **Autoregressive Integrated Moving Average** (ARIMA) - This was one of the most popular techniques for predicting future values of time series data (in the pre-neural networks ages). Let's add it and see if it comes off as an important predictive feature.
6. **Stacked autoencoders** - most of the aforementioned features (fundamental analysis, technical analysis, etc) were found by people after decades of research. But maybe we have missed something. Maybe there are hidden correlations that people cannot comprehend due to the enormous amount of data points, events, assets, charts, etc. With stacked autoencoders (type of neural networks) we can use the power of computers and probably find new types of features that affect stock movements. Even though we will not be able to understand these features in human language, we will use them in the GAN.
7. **Deep Unsupervised learning for anomaly detection in options pricing**. We will use one more feature - for every day we will add the price for 90-days call option on Goldman Sachs stock. Options pricing itself combines a lot of data. The price for options contract depends on the future value of the stock (analysts try to also predict the price in order to come up with the most accurate price for the call option). Using deep unsupervised learning (**Self-organized Maps**) we will try to spot anomalies in every day's pricing. Anomaly (such as a drastic change in pricing) might indicate an event that might be useful for the LSTM to learn the overall stock pattern.

Next, having so many features, we need to perform a couple of important steps:
1. Perform statistical checks for the 'quality' of the data. If the data we create is flawed, then no matter how sophisticated our algorithms are, the results will not be positive. The checks include making sure the data does not suffer from heteroskedasticity, multicollinearity, or serial correlation.
2. Create feature importance. If a feature (e.g. another stock or a technical indicator) has no explanatory power to the stock we want to predict, then there is no need for us to use it in the training of the neural nets. We will using **XGBoost** (eXtreme Gradient Boosting), a type of boosted tree regression algorithms.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As a final step of our data preparation, we will also create **Eigen portfolios** using Principal Component Analysis (**PCA**) in order to reduce the dimensionality of the features created from the autoencoders.


```python
from utils import *

import time
import numpy as np

from mxnet import nd, autograd, gluon
from mxnet.gluon import nn, rnn
import mxnet as mx
import datetime
import seaborn as sns

import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.decomposition import PCA

import math

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

import xgboost as xgb
from sklearn.metrics import accuracy_score
```


```python
import warnings
warnings.filterwarnings("ignore")
```


```python
context = mx.cpu(); model_ctx=mx.cpu()
mx.random.seed(1719)
```

**Note**: The purpose of this section (3. The Data) is to show the data preprocessing and to give rationale for using different sources of data, hence I will only use a subset of the full data (that is used for training).


```python
def parser(x):
    return datetime.datetime.strptime(x,'%Y-%m-%d')
```


```python
dataset_ex_df = pd.read_csv('data/panel_data_close.csv', header=0, parse_dates=[0], date_parser=parser)
```


```python
dataset_ex_df[['Date', 'GS']].head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>GS</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2009-12-31</td>
      <td>168.839996</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2010-01-04</td>
      <td>173.080002</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2010-01-05</td>
      <td>176.139999</td>
    </tr>
  </tbody>
</table>
</div>




```python
print('There are {} number of days in the dataset.'.format(dataset_ex_df.shape[0]))
```

    There are 2265 number of days in the dataset.


Let's visualize the stock for the last nine years. The dashed vertical line represents the separation between training and test data.


```python
plt.figure(figsize=(14, 5), dpi=100)
plt.plot(dataset_ex_df['Date'], dataset_ex_df['GS'], label='Goldman Sachs stock')
plt.vlines(datetime.date(2016,4, 20), 0, 270, linestyles='--', colors='gray', label='Train/Test data cut-off')
plt.xlabel('Date')
plt.ylabel('USD')
plt.title('Figure 2: Goldman Sachs stock price')
plt.legend()
plt.show()
```


![png](output_21_0.png)



```python
num_training_days = int(dataset_ex_df.shape[0]*.7)
print('Number of training days: {}. Number of test days: {}.'.format(num_training_days, \
                                                                    dataset_ex_df.shape[0]-num_training_days))
```

    Number of training days: 1585. Number of test days: 680.


## 3.1. Correlated assets <a class="anchor" id="corrassets"></a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As explained earlier we will use other assets as features, not only GS.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;So what other assets would affect GS's stock movements? Good understanding of the company, its lines of businesses, competitive landscape, dependencies, suppliers and client type, etc is very important for picking the right set of correlated assets:
- First are the **companies** similar to GS. We will add JPMorgan Chase and Morgan Stanley, among others, to the dataset.
- As an investment bank, Goldman Sachs depends on the **global economy**. Bad or volatile economy means no M&As or IPOs, and possibly limited proprietary trading earnings. That is why we will include global economy indices. Also, we will include LIBOR (USD and GBP denominated) rate, as possibly shocks in the economy might be accounted for by analysts to set these rates, and other **FI** securities.
- Daily volatility index (**VIX**) - for the reason described in the previous point.
- **Composite indices** - such as NASDAQ and NYSE (from USA), FTSE100 (UK), Nikkei225 (Japan), Hang Seng and BSE Sensex (APAC) indices.
- **Currencies** - global trade is many times reflected into how currencies move, ergo we'll use a basket of currencies (such as USDJPY, GBPUSD, etc) as features.

#### Overall, we have 72 other assets in the dataset - daily price for every asset.

## 3.2. Technical indicators <a class="anchor" id="technicalind"></a>

We already covered what are technical indicators and why we use them so let's jump straight to the code. We will create technical indicators only for GS.


```python
def get_technical_indicators(dataset):
    # Create 7 and 21 days Moving Average
    dataset['ma7'] = dataset['price'].rolling(window=7).mean()
    dataset['ma21'] = dataset['price'].rolling(window=21).mean()
    
    # Create MACD
    dataset['26ema'] = pd.ewma(dataset['price'], span=26)
    dataset['12ema'] = pd.ewma(dataset['price'], span=12)
    dataset['MACD'] = (dataset['12ema']-dataset['26ema'])

    # Create Bollinger Bands
    dataset['20sd'] = pd.stats.moments.rolling_std(dataset['price'],20)
    dataset['upper_band'] = dataset['ma21'] + (dataset['20sd']*2)
    dataset['lower_band'] = dataset['ma21'] - (dataset['20sd']*2)
    
    # Create Exponential moving average
    dataset['ema'] = dataset['price'].ewm(com=0.5).mean()
    
    # Create Momentum
    dataset['momentum'] = dataset['price']-1
    
    return dataset
```


```python
dataset_TI_df = get_technical_indicators(dataset_ex_df[['GS']])
```


```python
dataset_TI_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>price</th>
      <th>ma7</th>
      <th>ma21</th>
      <th>26ema</th>
      <th>12ema</th>
      <th>MACD</th>
      <th>20sd</th>
      <th>upper_band</th>
      <th>lower_band</th>
      <th>ema</th>
      <th>momentum</th>
      <th>log_momentum</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2010-02-01</td>
      <td>153.130005</td>
      <td>152.374285</td>
      <td>164.220476</td>
      <td>160.321839</td>
      <td>156.655072</td>
      <td>-3.666767</td>
      <td>9.607375</td>
      <td>183.435226</td>
      <td>145.005726</td>
      <td>152.113609</td>
      <td>152.130005</td>
      <td>5.024735</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2010-02-02</td>
      <td>156.940002</td>
      <td>152.777143</td>
      <td>163.653809</td>
      <td>160.014868</td>
      <td>156.700048</td>
      <td>-3.314821</td>
      <td>9.480630</td>
      <td>182.615070</td>
      <td>144.692549</td>
      <td>155.331205</td>
      <td>155.940002</td>
      <td>5.049471</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2010-02-03</td>
      <td>157.229996</td>
      <td>153.098572</td>
      <td>162.899047</td>
      <td>159.766235</td>
      <td>156.783365</td>
      <td>-2.982871</td>
      <td>9.053702</td>
      <td>181.006450</td>
      <td>144.791644</td>
      <td>156.597065</td>
      <td>156.229996</td>
      <td>5.051329</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2010-02-04</td>
      <td>150.679993</td>
      <td>153.069999</td>
      <td>161.686666</td>
      <td>158.967168</td>
      <td>155.827031</td>
      <td>-3.140137</td>
      <td>8.940246</td>
      <td>179.567157</td>
      <td>143.806174</td>
      <td>152.652350</td>
      <td>149.679993</td>
      <td>5.008500</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2010-02-05</td>
      <td>154.160004</td>
      <td>153.449999</td>
      <td>160.729523</td>
      <td>158.550196</td>
      <td>155.566566</td>
      <td>-2.983631</td>
      <td>8.151912</td>
      <td>177.033348</td>
      <td>144.425699</td>
      <td>153.657453</td>
      <td>153.160004</td>
      <td>5.031483</td>
    </tr>
  </tbody>
</table>
</div>



So we have the technical indicators (including MACD, Bollinger bands, etc) for every trading day. We have in total 12 technical indicators.

Let's visualize the last 400 days of these indicators.


```python
def plot_technical_indicators(dataset, last_days):
    plt.figure(figsize=(16, 10), dpi=100)
    shape_0 = dataset.shape[0]
    xmacd_ = shape_0-last_days
    
    dataset = dataset.iloc[-last_days:, :]
    x_ = range(3, dataset.shape[0])
    x_ =list(dataset.index)
    
    # Plot first subplot
    plt.subplot(2, 1, 1)
    plt.plot(dataset['ma7'],label='MA 7', color='g',linestyle='--')
    plt.plot(dataset['price'],label='Closing Price', color='b')
    plt.plot(dataset['ma21'],label='MA 21', color='r',linestyle='--')
    plt.plot(dataset['upper_band'],label='Upper Band', color='c')
    plt.plot(dataset['lower_band'],label='Lower Band', color='c')
    plt.fill_between(x_, dataset['lower_band'], dataset['upper_band'], alpha=0.35)
    plt.title('Technical indicators for Goldman Sachs - last {} days.'.format(last_days))
    plt.ylabel('USD')
    plt.legend()

    # Plot second subplot
    plt.subplot(2, 1, 2)
    plt.title('MACD')
    plt.plot(dataset['MACD'],label='MACD', linestyle='-.')
    plt.hlines(15, xmacd_, shape_0, colors='g', linestyles='--')
    plt.hlines(-15, xmacd_, shape_0, colors='g', linestyles='--')
    plt.plot(dataset['log_momentum'],label='Momentum', color='b',linestyle='-')

    plt.legend()
    plt.show()
```


```python
plot_technical_indicators(dataset_TI_df, 400)
```


![png](output_32_0.png)


## 3.3. Fundamental analysis <a class="anchor" id="fundamental"></a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For fundamental analysis we will perform sentiment analysis on all daily news about GS. Using sigmoid at the end, result will be between 0 and 1. The closer the score is to 0 - the more negative the news is (closer to 1 indicates positive sentiment). For each day, we will create the average daily score (as a number between 0 and 1) and add it as a feature.

### 3.3.1. Bidirectional Embedding Representations from Transformers - BERT <a class="anchor" id="bidirnlp"></a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;For the purpose of classifying news as positive or negative (or neutral) we will use <a href="https://arxiv.org/abs/1810.04805">BERT</a>, which is a pre-trained language representation.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pretrained BERT models are already available in MXNet/Gluon. We just need to instantiated them and add two (arbitrary number) ```Dense``` layers, going to softmax - the score is from 0 to 1.


```python
# just import bert
import bert
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Going into the details of BERT and the NLP part is not in the scope of this notebook, but you have interest, do let me know - I will create a new repo only for BERT as it definitely is quite promissing when it comes to language processing tasks.

## 3.4. Fourier transforms for trend analysis <a class="anchor" id="fouriertransform"></a>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Fourier transforms** take a function and create a series of sine waves (with different amplitudes and frames). When combined, these sine waves approximate the original function. Mathematically speaking, the transforms look like this:

$$G(f) = \int_{-\infty}^\infty g(t) e^{-i 2 \pi f t} dt$$

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;We will use Fourier transforms to extract global and local trends in the GS stock, and to also denoise it a little. So let's see how it works.


```python
data_FT = dataset_ex_df[['Date', 'GS']]
```


```python
close_fft = np.fft.fft(np.asarray(data_FT['GS'].tolist()))
fft_df = pd.DataFrame({'fft':close_fft})
fft_df['absolute'] = fft_df['fft'].apply(lambda x: np.abs(x))
fft_df['angle'] = fft_df['fft'].apply(lambda x: np.angle(x))
```


```python
plt.figure(figsize=(14, 7), dpi=100)
fft_list = np.asarray(fft_df['fft'].tolist())
for num_ in [3, 6, 9, 100]:
    fft_list_m10= np.copy(fft_list); fft_list_m10[num_:-num_]=0
    plt.plot(np.fft.ifft(fft_list_m10), label='Fourier transform with {} components'.format(num_))
plt.plot(data_FT['GS'],  label='Real')
plt.xlabel('Days')
plt.ylabel('USD')
plt.title('Figure 3: Goldman Sachs (close) stock prices & Fourier transforms')
plt.legend()
plt.show()
```


![png](output_45_0.png)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;As you see in Figure 3 the more components from the Fourier transform we use the closer the approximation function is to the real stock price (the 100 components transform is almost identical to the original function - the red and the purple lines almost overlap). We use Fourier transforms for the purpose of extracting long- and short-term trends so we will use the transforms with 3, 6, and 9 component
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `package-lock.json`
```python
{
  "name": "project",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {}
}
```

#### File: `package.json`
```python
{
  "name": "trading-ai-pro",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "devDependencies": {
    "vite": "^5.0.0"
  }
}
```


==================================================


## [3/3] Repository: trading_bot (`WHEEL_ai_trading_bot`)
- **Full Name**: `ai_trading_bot`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# AI Trading Bot

A fully automated **options & stock trading system** for the Indian market, built with Python.  
It predicts market direction, selects strikes, executes orders via [Dhan HQ API](https://dhan.co/), and logs every trade — all in real time.

---

## 🚀 Features
- **Signal Generation**  
  - Machine-learning models trained on live & historical data  
  - Predicts direction for NIFTY / BANKNIFTY and equities  
- **Strike Selection**  
  - Automatically picks optimal CE/PE options based on LTP, delta, and strategy rules  
- **Order Execution**  
  - Places trades via Dhan API (market / limit)  
  - Supports straddle, strangle, and directional plays  
- **Automation & Scheduling**  
  - Cron-style scheduler to start/stop strategies at set times  
- **Risk & Logging**  
  - PnL calculation, trade history, Telegram alerts, daily summaries  
- **Backtesting Mode**  
  - Replay historical data to validate strategies before going live

---

## 🛠 Tech Stack
- **Python 3** (core language)  
- `pandas`, `numpy`, `scikit-learn`, `matplotlib`  
- Dhan HQ REST API  
- Cron / shell scripts for automation  
- Git & GitHub for version control

---

## 📂 Project Structure

### Core Implementation Code & Architecture
#### File: `config.json`
```python
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzUyNTA0NDQxLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiaHR0cHM6Ly9leGFtcGxlLmNvbSAiLCJkaGFuQ2xpZW50SWQiOiIxMTA3NDAwMjU0In0._pc2IfNHPgZLphXFxS-IQhJX5kpZiHzXVZax_N_R_5exMmmmj3YcutJo6MRTDJh9NKKH7LPFm8F-GKn6pMFBDA",
  "dry_run": true,
  "underlying": "BANKNIFTY"
}
```

#### File: `get_ltp.py`
```python
from dhan_api import get_ltp

# Example from symbol lookup: Replace this with real values you searched
security_id = "95123"           # Replace with a working ID
exchange_segment = "NFO"        # NFO = NSE Futures & Options
instrument_type = "OPTIDX"      # Options on index

ltp = get_ltp(security_id, exchange_segment, instrument_type)

if ltp:
    print(f"✅ LTP: ₹{ltp}")
else:
    print("❌ LTP fetch failed.")
```

#### File: `auto_scheduler.py`
```python
# 📁 auto_scheduler.py
# Schedule your trading bot to run at specific times

import schedule
import time
import subprocess
from datetime import datetime

# Define your time triggers (24-hour format)
TRADE_TIME = "09:20"
EXIT_TIME = "15:15"


def run_main_trade():
    print(f"\n🚀 Running main.py at {datetime.now().strftime('%H:%M:%S')}...")
    subprocess.call(["python3", "main.py"])

def run_exit_logger():
    print(f"\n💼 Running exit_trades.py at {datetime.now().strftime('%H:%M:%S')}...")
    subprocess.call(["python3", "exit_trades.py"])


# Schedule jobs
schedule.every().day.at(TRADE_TIME).do(run_main_trade)
schedule.every().day.at(EXIT_TIME).do(run_exit_logger)

print("🕒 Auto Scheduler Started")
print(f"📆 Will run main.py at {TRADE_TIME} and exit_trades.py at {EXIT_TIME} each day.")

# Keep script running
while True:
    schedule.run_pending()
    time.sleep(30)
```

#### File: `log_trades.py`
```python
# 📁 log_trades.py
# Append trade logs to CSV with profit/loss calculation

import pandas as pd
import datetime
import os


def log_trade(symbol, strike, type_, entry_price, exit_price, quantity, security_id):
    timestamp = datetime.datetime.now()
    pnl = (exit_price - entry_price) * quantity if type_ == "CE" else (entry_price - exit_price) * quantity

    log = pd.DataFrame([{
        "timestamp": timestamp,
        "symbol": symbol,
        "type": type_,
        "strike": strike,
        "entry_price": entry_price,
        "exit_price": exit_price,
        "quantity": quantity,
        "pnl": round(pnl, 2),
        "security_id": security_id
    }])

    log_file = "trade_logs.csv"
    write_header = not os.path.exists(log_file)
    log.to_csv(log_file, mode="a", index=False, header=write_header)
    print(f"📊 Logged trade: {symbol} {type_} | P&L: ₹{round(pnl, 2)}")


if __name__ == "__main__":
    # Test log
    log_trade("NIFTY 20JUN24 23500CE", 23500, "CE", 120, 132.5, 50, "95123")
```

#### File: `train_model.py`
```python
# 📁 train_model.py — Retrain AI model on labeled signals (Fixed NaN issue)

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# 📄 Load labeled data
df = pd.read_csv("training_data.csv")

# ✅ Drop rows with NaN (missing values)
df.dropna(inplace=True)

# 🧠 Features & Labels
X = df[["return", "EMA5", "EMA20", "RSI"]]
y = df["label"]

# 🔀 Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 🎓 Train Model
model = RandomForestClassifier(n_estimators=100, max_depth=6, random_state=42)
model.fit(X_train, y_train)

# 📊 Evaluation
y_pred = model.predict(X_test)
print("\n✅ Model Evaluation:")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

# 💾 Save Model
joblib.dump(model, "option_signal_model.pkl")
print("\n📦 Model saved as option_signal_model.pkl")
```

#### File: `trade_engine.py`
```python
# 📁 trade_engine.py
# Basic signal engine using moving averages (can plug into main.py or ML)

import pandas as pd
import yfinance as yf


def fetch_historical_data(symbol="^NSEI", interval="15m", period="5d"):
    """Fetch historical index data (default: NIFTY 50)"""
    print(f"📥 Downloading historical data for {symbol}...")
    df = yf.download(tickers=symbol, interval=interval, period=period)
    if df.empty:
        print("❌ No data fetched.")
        return None
    df = df[['Close']]
    df.dropna(inplace=True)
    return df


def generate_signal(df, short_window=5, long_window=20):
    """Generates basic crossover signal"""
    df['SMA5'] = df['Close'].rolling(window=short_window).mean()
    df['SMA20'] = df['Close'].rolling(window=long_window).mean()
    df.dropna(inplace=True)

    if df.iloc[-1]['SMA5'] > df.iloc[-1]['SMA20']:
        return "BUY CALL"
    elif df.iloc[-1]['SMA5'] < df.iloc[-1]['SMA20']:
        return "BUY PUT"
    else:
        return "HOLD"


if __name__ == "__main__":
    df = fetch_historical_data()
    if df is not None:
        signal = generate_signal(df)
        print(f"🧠 Signal Generated: {signal}")
```


==================================================
