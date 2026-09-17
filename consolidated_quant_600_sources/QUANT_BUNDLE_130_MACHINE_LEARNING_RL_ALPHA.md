# ⚡ [QUANT-SOURCE-130] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_130_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: AIAlpha (`PHASE4-QUANT-005`)
- **Full Name**: `PHASE4-QUANT-005_VivekPa__AIAlpha`
- **Description**: Use unsupervised and supervised learning to predict stocks
- **GitHub Stars**: 1959
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# AIAlpha: Multilayer neural network architecture for stock return prediction
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![GitHub license](https://img.shields.io/badge/License-MIT-brightgreen.svg?style=flat-square)](https://github.com/VivekPa/AIAlpha/blob/master/LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)

This project is meant to be an **advanced** implementation of **stacked neural networks** to predict the return of stocks. My goal for the viewer is to understand the core principles that go behind the development of such a multilayer model and the nuances of training the individual components for optimal predictive ability. Once the core principles are understood, the various components of the model can be replaced with the state of the art models available at time of usage. 

The workflow is similar to the approach in the excellent text Advances in Financial Machine Learning by Marcos Lopez de Prado, which I recommend to anyone who wants to learn about applying machine learning techniques to financial data. The data that was used for this project is not in the repository due to size constraints in GitHub, but the raw data was open sourced from Tick Data LLC, but now I believe is not available. 

In essense, we will be making bars (tick, volume or dollar) based on the tick data, apply feature engineering, reduce the dimensions using an **autoencoder** and finally use a machine learing model to make predictions. I have implemented both a **LSTM** regression model and a **Random Forest** classification model to classify the direction of the move. 

This model is not meant to be used to live trade without modifications. However, an extended version of this model can very well be profitable with the right strategies. 

I truly hope you find this project informative and useful in developing your own trading strategies or machine learning models.

*This project illustrates how to use machine learning to predict the future prices of stocks. In order to efficiently allocate the capital to those stocks, check out [OptimalPortfolio](https://github.com/VivekPa/OptimalPortfolio)*

*Disclaimer, this is purely an educational project. Any backtesting performance do not guarentee live trading results. Trade at your own risk.*
*This is only a guide on the usage of the model. If you want to delve into the reasoning behind the model and the theory, please check out my blog: [Engineer Quant](https://medium.com/engineer-quant)*

## Contents
- [Contents](#contents)
- [Overview](#overview)
- [Quickstart](#quickstart)
- [Bar Sampling](#bar-sampling)
- [Feature Engineering](#feature-engineering)
- [Stacked Autoencoder](#stacked-autoencoder)
- [Neural Network Model](#neural-network-model)
- [Random Forest Model](#random-forest-model)
- [Results](#results)
- [Online Learning](#online-learning)
- [What next?](#what-next?)
- [Contributing](#contributing)

## Overview

Those who have done some form of machine learning would know that the workflow follows this format: acquire data, preprocess, train, test, monitor model. However, given the complexity of this task, the workflow has been modified to the following:

1. Acquire the tick data - this is the primary data for our model.
2. Preprocess the data - we need to sample the data using some method. Subsequently, we make the train-test splits.
3. Train the stacked autoencoder - this will give us our feature extractor.
4. Process the data - this will give us the *features* of our model, along with train, test datasets.
5. Use the neural network/random forest to learn from the training data.
6. Test the model with the testing set - this gives us a gauge of how good our model is.

Now let me elaborate the various parts of the pipeline.

## Quickstart

For those who just want to see the model work, run the following code (make sure you are on Python 3 to prevent any bugs or errors):

```bash
pip install -r requirements.txt
python run.py
```

*Note: Due to GitHub file size restrictions, I have only uploaded part of the data (1 million rows), so the model results may vary from the one shown below.*

## Bar Sampling

Running machine learning algorithms, or any other statistical models, directly on tick level data often leads to poor results, due to the high level of noise caused by the bid-ask bounce, and the high nonlinearity in the nature of the data. Therefore, we need to sample the data at some interval (which can be decided depending on the frequency of the predictive model). The sampling that we are used to seeing is time sampled (we get bars every 1min), but this is known to exhibit non stationarities and the returns are not normally distributed. So, as explained in Advances in Financial Machine Learning, we are going to sample it according to the number of ticks, or the amount of volume or the amount of dollars traded. These bars show better statistical properties and are preferable for machine learning applications.

## Feature Engineering

Given our OHLCV data from our sampling procedure, we can go ahead and create features that we feel might add information to the forecast. I have constructed a set of features that are based on moving averages and rolling volatilities of the various prices and volumes. This set of features can be extended accordingly. 

## Stacked Autoencoder

Given our features, we notice that the dimension of the dataset is huge (185 for my configuration). This can pose a lot of problems when we run machine learning algorithms due to the curse of dimensionality. However, we can attempt to overcome this by using neural networks that are able to decompress the data given into smaller number of neurons than the input number. When we train such a neural network, it becomes able to extract the 'important sections' of the data so to speak. Hence, this compressed version of the data can be considered as *features*. Although this method is useful, the downside is that we do not know what the various compressed data points mean and hence cannot extract methods to achieve them in differnt datasets. 

## Neural Network Model

Using neural networks for the prediction of time series has become widespread and the power of neural networks is well known. I have used a LSTM model for its memory property. However, an issue I faced with the training of the neural network model is that there was a tendency for the model to fit to a constant, as it turned out to be a local minima for the loss function. One way to overcome this is using different initialisations for the weights, and tuning the hyperparameters. 

## Random Forest Model

Sometimes, it might be better to use a simpler model as apposed to a sophisticated neural network. This is especially true when the amount of data available is not enough for deep models. Even though I used tick level data, the dataset was only around 5 million rows. After sampling, the number of rows drops and it is not enough for deep learning models to learn effectively from. So, I wanted to use a random forest classification model that classified the direction of the next bar.

## Results

Using this stacked neural network model, I was able to achieve decent results. The following are graphs of my predictions vs the actual market prices for various securities.

EURUSD

![alt text][EURUSD]

[EURUSD]: https://engfinance.files.wordpress.com/2018/11/figure_1-4.png "Prediction 1"

EURUSD prices - R^2: 0.90

![alt text][EURUSD2]

[EURUSD2]: https://engfinance.files.wordpress.com/2018/11/figure_1-5.png "Prediction 2"

For the random forest classification model, the results were better. I used tick bars for this simulation. 

The base case used is merely predicting no moves in the market. The out of sample results were:

```bash
Tick bars:
    Model log loss: 2.78
    Base log loss: 4.81

Volume bars:
    Model log loss: 1.69
    Base log loss: 5.06

Dollar bars:
    Model log loss: 2.56
    Base log loss: 2.94
```

It is also useful to understand how much of an impact the autoencoders made, so I ran the model without autoencoders and the results were:

```bash
Tick bars:
    Model log loss: 5.12
    Base log loss: 4.81

Volume bars:
    Model log loss: 3.25
    Base log loss: 5.06

Dollar bars:
    Model log loss: 3.62
    Base log loss: 2.94
```


## Online Learning

The training normally stops after the model has trained on historic data and merely predicts future data. However, I believe that it might be a waste of data if the model does not also learn from the predictions. This is done by training the model on the new (prediction, actual) pairs to continually improve the model. 

## What's next?

The beauty of this model is the once the construction is understood, the individual models can be swapped out for the best model there is. So over time the actual models used here will be different but the core framework will still be the same. I am also working on improving the current model with ideas from Advanced in Financial Machine Learning, such as adding sample weights, cross-validation and ensemble techniques. 

## Contributing

I am always grateful for feedback and modifications that would help! 

Hope you have enjoyed that! To see more content like this, please visit: [Engineer Quant](https://medium.com/engineer-quant)

### Core Implementation Code & Architecture
#### File: `.vs/ProjectSettings.json`
```python
{
  "CurrentProjectSetting": null
}
```

#### File: `.vs/VSWorkspaceState.json`
```python
{
  "ExpandedNodes": [
    ""
  ],
  "PreviewInSolutionExplorer": false
}
```

#### File: `__init__.py`
```python
"A package to build a machine learning model for trading and stock price prediction"

import aialpha.data_processor as data_processor
import aialpha.models as models
```

#### File: `test.py`
```python
import pandas as pd 
import numpy as np 

df = pd.read_csv('data/raw_data/price_vol.csv', index_col=0)
print(df.shape)

sample_data = df.iloc[:1000000, :]
sample_data.to_csv('sample_data/raw_data/price_vol.csv')
```

#### File: `twitter_scrubbing/twitter.py`
```python
import os

os.environ['R_HOME'] = r'C:\Program Files\R\R-3.5.1' 
os.environ['R_USER'] = r'C:\Users\Xue Yao\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\rpy2' 

import rpy2.robjects as robjects

directory = r'C:\Users\Xue Yao\Documents\News Scrubbing\Twitter Scrubbing\twitter.R'
r_source = robjects.r['source']
r_source(directory)
print ('r script finished running')
```

#### File: `twitter_scrubbing/twittersentimentcalculator.py`
```python
import pandas as pd
import numpy as np
from textblob import TextBlob

pd.options.mode.chained_assignment = None

df = pd.read_csv('twitter.csv')
n = 0
sentiment = 0
df['New sentiment'] = pd.Series(np.random.randn(len(df['sentiment'])), index=df.index)
print(df)
for i in range(len(df)):
	text = TextBlob(df.iloc[i][2])
	newsentiment = text.sentiment.polarity
	sentiment += df.iloc[i][3]
	n += 1
	df['New sentiment'][i] = newsentiment
df.to_csv("twitter.csv")
print(sentiment/n)
```


==================================================


## [2/3] Repository: tributary (`PHASE4-QUANT-010`)
- **Full Name**: `PHASE4-QUANT-010_timkpaine__tributary`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# <img src="https://raw.githubusercontent.com/1kbgz/tributary/main/docs/img/icon.png" width="300">
Python Data Streams

[![Build Status](https://github.com/1kbgz/tributary/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/1kbgz/tributary/actions?query=workflow%3A%22Build+Status%22)
[![Coverage](https://codecov.io/gh/1kbgz/tributary/branch/main/graph/badge.svg)](https://codecov.io/gh/1kbgz/tributary)
[![PyPI](https://img.shields.io/pypi/l/tributary.svg)](https://pypi.python.org/pypi/tributary)
[![PyPI](https://img.shields.io/pypi/v/tributary.svg)](https://pypi.python.org/pypi/tributary)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/1kbgz/tributary/main?urlpath=lab)


Tributary is a library for constructing dataflow graphs in python. Unlike many other DAG libraries in python ([airflow](https://airflow.apache.org), [luigi](https://luigi.readthedocs.io/en/stable/), [prefect](https://docs.prefect.io), [dagster](https://docs.dagster.io), [dask](https://dask.org), [kedro](https://github.com/quantumblacklabs/kedro), etc), tributary is not designed with data/etl pipelines or scheduling in mind. Instead, tributary is more similar to libraries like [mdf](https://github.com/man-group/mdf), [loman](https://github.com/janushendersonassetallocation/loman), [pyungo](https://github.com/cedricleroy/pyungo), [streamz](https://streamz.readthedocs.io/en/latest/), or [pyfunctional](https://github.com/EntilZha/PyFunctional), in that it is designed to be used as the implementation for a data model. One such example is the [greeks](https://github.com/1kbgz/greeks) library, which leverages tributary to build data models for [options pricing](https://www.investopedia.com/articles/optioninvestor/07/options_beat_market.asp).

![](https://raw.githubusercontent.com/1kbgz/tributary/main/docs/img/example.gif)


# Installation
Install with pip:

`pip install tributary`

or with conda:

`conda install -c conda-forge tributary`

or from source:

`python setup.py install`

Note: If installing from source or with pip, you'll also need [Graphviz itself](https://www.graphviz.org/download/) if you want to visualize the graph using the `.graphviz()` method.

# Stream Types
Tributary offers several kinds of streams:

## Streaming
These are synchronous, reactive data streams, built using asynchronous python generators. They are designed to mimic complex event processors in terms of event ordering.

## Functional
These are functional streams, built by currying python functions (callbacks).

## Lazy
These are lazily-evaluated python streams, where outputs are propogated only as inputs change. They are implemented as directed acyclic graphs.

# Examples
- [Streaming](docs/examples/streaming/streaming.md): In this example, we construct a variety of forward propogating reactive graphs.
- [Lazy](docs/examples/lazy/lazy.md): In this example, we construct a variety of lazily-evaluated directed acyclic computation graphs.
- [Automatic Differentiation](docs/examples/autodiff/autodiff.md): In this example, we use `tributary` to perform automatic differentiation on both lazy and streaming graphs.

# Graph Visualization
You can visualize the graph with Graphviz. All streaming and lazy nodes support a `graphviz` method.

Streaming and lazy nodes also support [ipydagred3](https://github.com/timkpaine/ipydagred3) for live update monitoring.

## Streaming
![](https://raw.githubusercontent.com/1kbgz/tributary/main/docs/img/streaming/dagred3.gif)

Here green indicates executing, yellow indicates stalled for backpressure, and red indicates that `StreamEnd` has been propogated (e.g. stream has ended).

## Lazy
![](https://raw.githubusercontent.com/1kbgz/tributary/main/docs/img/lazy/dagred3.gif)

Here green indicates executing, and red indicates that the node is dirty. Note the the determination if a node is dirty is also done lazily (we can check with `isDirty` whcih will update the node's graph state.

## Catalog
See the [CATALOG](CATALOG.md) for a full list of functions, transforms, sources, and sinks.

## Support / Contributors
Thanks to the following organizations for providing code or financial support.


<a href="https://nemoulous.com"><img src="https://raw.githubusercontent.com/1kbgz/tributary/main/docs/img/nem.png" width="50"></a>

<a href="https://nemoulous.com">Nemoulous</a>

## License
This software is licensed under the Apache 2.0 license. See the [LICENSE](LICENSE) file for details.

## Alternatives
Here is an incomplete list of libraries which implement similar/overlapping functionality

- [man-group/mdf](https://github.com/man-group/mdf)
- [janushendersonassetallocation/loman](https://github.com/janushendersonassetallocation/loman)
- [cedricleroy/pyungo](https://github.com/cedricleroy/pyungo)
- [python-streamz/streamz](https://github.com/python-streamz/streamz)
- [EntilZha/pyfunctional](https://github.com/EntilZha/PyFunctional)
- [stitchfix/hamilton](https://github.com/stitchfix/hamilton)

### Core Implementation Code & Architecture
#### File: `tributary/incubating/__init__.py`
```python

```

#### File: `tributary/tests/__init__.py`
```python

```

#### File: `tributary/tests/utils/__init__.py`
```python

```

#### File: `tributary/tests/streaming/__init__.py`
```python

```

#### File: `tributary/tests/streaming/input/__init__.py`
```python

```

#### File: `tributary/tests/streaming/input/test_sse_streaming.py`
```python

```


==================================================


## [3/3] Repository: financial-machine-learning (`PHASE4-QUANT-014`)
- **Full Name**: `PHASE4-QUANT-014_firmai__financial-machine-learning`
- **Description**: A curated list of practical financial machine learning tools and applications.
- **GitHub Stars**: 8785
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
[![Repo-Updater](https://github.com/firmai/financial-machine-learning/actions/workflows/repo_status.yml/badge.svg)](https://github.com/firmai/financial-machine-learning/actions/workflows/repo_status.yml)
[![Wiki-Generator](https://github.com/firmai/financial-machine-learning/actions/workflows/wiki_gen.yml/badge.svg)](https://github.com/firmai/financial-machine-learning/actions/workflows/wiki_gen.yml)
[![Repo-Search](https://github.com/firmai/financial-machine-learning/actions/workflows/repo_search.yml/badge.svg)](https://github.com/firmai/financial-machine-learning/actions/workflows/repo_search.yml)
[![Gitter](https://badges.gitter.im/financial-machine-learning/community.svg)](https://gitter.im/financial-machine-learning/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

---

## 🌟 We Are Growing!

We're seeking to collaborate with motivated, independent PhD graduates or doctoral students on approximately seven new projects in 2024. If you’re interested in contributing to cutting-edge investment insights and data analysis, please get in touch! This could be in colaboration with a university or as independent study. 

![image](https://github.com/user-attachments/assets/da97663a-b63f-4286-94cc-fcd168905109)


### 🚀 About Sov.ai

Sov.ai is at the forefront of integrating advanced machine learning techniques with financial data analysis to revolutionize investment strategies. We are working with **3 of the top 10** quantitative hedge funds, and with many mid-sized and boutique firms. 

Our platform leverages diverse data sources and innovative algorithms to deliver actionable insights that drive smarter investment decisions. 

By joining Sov.ai, you'll be part of a dynamic research team dedicated to pushing the boundaries of what's possible in finance through technology. Before expressing your interest, please be aware that the research will be predominantly challenging and experimental in nature.


### 🔍 Research and Project Opportunities

We offer a wide range of projects that cater to various interests and expertise within machine learning and finance. Some of the exciting recent projects include:

- **Predictive Modeling with GitHub Logs:** Develop models to predict market trends and investment opportunities using GitHub activity and developer data.
- **Satallite Data Analysis:** Explore non-traditional data sources such as social media sentiment, satellite imagery, or web traffic to enhance financial forecasting.
- **Data Imputation Techniques:** Investigate new methods for handling missing or incomplete data to improve the robustness and accuracy of our models.

Please visit [docs.sov.ai](https://docs.sov.ai) for more information on public projects that have made it into the subscription product. If you already have a corporate sponsor, we are also happy to work with them. 

### 🌐 Why Join Sov.ai?

- **Innovative Environment:** Engage with the latest technologies and methodologies in machine learning and finance.
- **Collaborative Team:** Work alongside a team of experts passionate about driving innovation in investment insights.
- **Flexible Projects:** Tailor your research to align with your interests and expertise, with the freedom to explore new ideas.
- **Experienced Researchers:** Experts previously from NYU, Columbia, Oxford-Man Institute, Alan Turing Institute, and Cambridge.
- **Post Research:** Connect with alumni that has moved on to DRW, Citadel Securities, Virtu Financial, Akuna Capital, HRT.


### 🤝 How to Apply

If you’re excited about leveraging your expertise in machine learning and finance to drive impactful research and projects, we’d love to hear from you! Please reach out to us at [research@sov.ai](mailto:research@sov.ai) with your resume and a brief description of your research interests.

Join us in shaping the future of investment insights and making a meaningful impact in the world of finance!



## So what is [ML-Quant.com](https://ml-quant.com) then?


It is our firehose of daily research, serving as an internal knowledge base and client resource while also acting as a marketing channel to showcase our expertise and attract potential clients in the machine learning and quantitative finance space.


![Screenshot 2024-10-04 at 08-30-53 ML-Quant - Machine Learning and Quantitative Finance](https://github.com/user-attachments/assets/37911503-1277-4eec-b856-bb801ca9b45b)



# Financial Machine Learning and Data Science


- All repos/links status including last commit date is updated daily
- Only 15 Highest ranked repos/links for each section are displayed on main README.md and full list is available within the wiki page
- Both Wikis/README.md is updated in realtime as soon as new information are pushed to the repo 
___

# Trading
## Deep Learning & Reinforcement Learning ([Wiki](https://github.com/firmai/financial-machine-learning/wiki/deep_learning_and_reinforcement_learning))
<!-- [PLACEHOLDER_START:deep_learning_and_reinforcement_learning] --> 
| <sub>repo</sub>                                                                                                                                                                                                           | <sub>comment</sub>                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | <sub>created_at</sub>          | <sub>last_commit</sub>         | <sub>star_count</sub>   | <sub>repo_status</sub>              | <sub>rating</sub>   |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|:-------------------------------|:------------------------|:------------------------------------|:--------------------|
| <sub>[FinRL-Library](https://github.com/AI4Finance-LLC/FinRL-Library)</sub>                                                                                                                                               | <sub>started by Columbia university engineering students and designed as an end to end deep reinforcement learning library for automated trading platform. Implementation of DQN DDQN DDPG etc using PyTorch and [gym](https://gym.openai.com/) use [pyfolio](https://github.com/quantopian/pyfolio) for showing backtesting stats. Big contributions on Proximal Policy Optimization (PPO) advantage actor critic (A2C) and Deep Deterministic Policy Gradient (DDPG) agents for trading</sub> | <sub>2020-07-26 13:18:16</sub> | <sub>2024-09-28 02:56:03</sub> | <sub>9697.0</sub>       | <sub>:heavy_check_mark:</sub>       | <sub>:star:x5</sub> |
| <sub>[Stock-Prediction-Models](https://github.com/huseinzol05/Stock-Prediction-Models)</sub>                                                                                                                              | <sub>very good curated list of notebooks showing deep learning + reinforcement learning models. Also contain topics on outlier detections/overbought oversold study/monte carlo simulartions/sentiment analysis from text (text storage/parsing is not detailed but it mentioned using [BERT](https://github.com/google-research/bert))</sub>                                                                                                                                                   | <sub>2017-12-18 10:49:59</sub> | <sub>2021-01-05 10:31:50</sub> | <sub>7924.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x5</sub> |
| <sub>[AI Trading](https://github.com/borisbanushev/stockpredictionai/blob/master/readme2.md)</sub>                                                                                                                        | <sub>AI to predict stock market movements.</sub>                                                                                                                                                                                                                                                                                                                                                                                                                                                | <sub>2019-01-09 08:02:47</sub> | <sub>2019-02-11 16:32:47</sub> | <sub>4094.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x5</sub> |
| <sub>[Deep Learning IV](https://github.com/achillesrasquinha/bulbea)</sub>                                                                                                                                                | <sub>Bulbea: Deep Learning based Python Library.</sub>                                                                                                                                                                                                                                                                                                                                                                                                                                          | <sub>2017-03-09 06:11:06</sub> | <sub>2017-03-19 07:42:49</sub> | <sub>2032.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x5</sub> |
| <sub>[RLTrader](https://github.com/notadamking/RLTrader)</sub>                                                                                                                                                            | <sub>predecessor to [tensortrade](https://github.com/tensortrade-org/tensortrade) uses open api [gym](https://gym.openai.com/) and neat way to render matplotlib plots in real time. Also explains LSTM/data stationarity/Bayesian optimization using [Optuna](https://github.com/optuna/optuna) etc.</sub>                                                                                                                                                                                     | <sub>2019-04-27 18:35:15</sub> | <sub>2019-10-17 16:25:49</sub> | <sub>1731.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x5</sub> |
| <sub>[Deep Learning III](https://github.com/Rachnog/Deep-Trading)</sub>                                                                                                                                                   | <sub>Algorithmic trading with deep learning experiments.</sub>                                                                                                                                                                                                                                                                                                                                                                                                                                  | <sub>2016-06-18 18:23:06</sub> | <sub>2018-08-07 15:24:45</sub> | <sub>1429.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x5</sub> |
| <sub>[Personae](https://github.com/Ceruleanacg/Personae)</sub>                                                                                                                                                            | <sub>implementation of deep reinforcement learning and supervised learnings covering areas: deep deterministic policy gradient (DDPG) and DDQN etc. Data are being pulled from [rqalpha](https://github.com/ricequant/rqalpha) which is a python backtest engine and have a nice docker image to run training/testing</sub>                                                                                                                                                                     | <sub>2018-03-10 11:22:00</sub> | <sub>2018-09-02 17:21:38</sub> | <sub>1340.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x5</sub> |
| <sub>[RL Trading](https://colab.research.google.com/drive/1FzLCI0AO3c7A4bp9Fi01UwXeoc7BN8sW)</sub>                                                                                                                        | <sub>A collection of 25+ Reinforcement Learning Trading Strategies -Google Colab.</sub>                                                                                                                                                                                                                                                                                                                                                                                                         | <sub>nan</sub>                 | <sub>nan</sub>                 | <sub>nan</sub>          | <sub>:heavy_check_mark:</sub>       | <sub>:star:x4</sub> |
| <sub>[Neural Network](https://github.com/VivekPa/IntroNeuralNetworks)</sub>                                                                                                                                               | <sub>Neural networks to predict stock prices.</sub>                                                                                                                                                                                                                                                                                                                                                                                                                                             | <sub>2018-09-10 06:34:53</sub> | <sub>2018-11-21 07:39:31</sub> | <sub>734.0</sub>        | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x4</sub> |
| <sub>[Deep Learning](https://github.com/keon/deepstock)</sub>                                                                                                                                                             | <sub>Technical experimentations to beat the stock market using deep learning.</sub>                                                                                                                                                                                                                                                                                                                                                                                                             | <sub>2016-12-12 02:15:12</sub> | <sub>2017-03-04 08:37:29</sub> | <sub>470.0</sub>        | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x4</sub> |
| <sub>[Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020](https://github.com/AI4Finance-LLC/Deep-Reinforcement-Learning-for-Automated-Stock-Trading-Ensemble-Strategy-ICAIF-2020)</sub> | <sub>Part of FinRL and provided code for paper [deep reinformacement learning for automated stock trading](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3690996) focuses on ensemble.</sub>                                                                                                                                                                                                                                                                                              | <sub>2020-07-26 13:12:53</sub> | <sub>2024-07-01 08:09:06</sub> | <sub>2019.0</sub>       | <sub>:heavy_check_mark:</sub>       | <sub>:star:x4</sub> |
| <sub>[LTSM Recurrent](https://github.com/VivekPa/AIAlpha)</sub>                                                                                                                                                           | <sub>OHLC Average Prediction of Apple Inc. Using LSTM Recurrent Neural Network.</sub>                                                                                                                                                                                                                                                                                                                                                                                                           | <sub>2018-10-07 03:58:26</sub> | <sub>2019-08-03 09:00:44</sub> | <sub>1711.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x4</sub> |
| <sub>[awesome-deep-trading](https://github.com/cbailes/awesome-deep-trading)</sub>                                                                                                                                        | <sub>curated list of papers/repos on topics like CNN/LSTM/GAN/Reinforcement Learning etc. Categorized as deep learning for now but there are other topics here. Manually maintained by cbailes</sub>                                                                                                                                                                                                                                                                                            | <sub>2018-11-26 03:23:04</sub> | <sub>2021-01-01 09:41:21</sub> | <sub>1482.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x4</sub> |
| <sub>[trading-bot](https://github.com/pskrunner14/trading-bot)</sub>                                                                                                                                                      | <sub>Implementation of deep reinforcement learning using Deep Q Network (DQN). Only supports single security at the moment. Idea is roughly based [here](https://keon.github.io/deep-q-learning/) and uses tensorflow/keras. Interesting helper python libraries used here are [tqdm](https://tqdm.github.io/) for console based progress bar and [altair](https://altair-viz.github.io/) for declarative visualization in python </sub>                                                        | <sub>2018-08-13 10:44:08</sub> | <sub>2020-01-23 04:41:20</sub> | <sub>952.0</sub>        | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x3</sub> |
| <sub>[crypto-rl](https://github.com/sadighian/crypto-rl)</sub>                                                                                                                                                            | <sub>Retrieve limit order book level data from coinbase pro and bitfinex -> record in [arctic](https://github.com/man-group/arctic) timeseries database then implemented trend following strategies (market orders) and market making (limit orders). Uses reinforcement learning (DQN) [keras-rl](https://github.com/keras-rl/keras-rl) to create agents and uses [openai gym](https://gym.openai.com/) to implement POMDP (partially observable markov decision process)</sub>                | <sub>2018-06-21 01:06:01</sub> | <sub>2021-11-30 13:52:18</sub> | <sub>849.0</sub>        | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x3</sub> |<!-- [PLACEHOLDER_END:deep_learning_and_reinforcement_learning] --> 
 

## Other Models ([Wiki](https://github.com/firmai/financial-machine-learning/wiki/other_models))
<!-- [PLACEHOLDER_START:other_models] --> 
| <sub>repo</sub>                                                                                                                                                                    | <sub>comment</sub>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | <sub>created_at</sub>          | <sub>last_commit</sub>         | <sub>star_count</sub>   | <sub>repo_status</sub>              | <sub>rating</sub>   |
|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------|:-------------------------------|:------------------------|:------------------------------------|:--------------------|
| <sub>[Microservices-Based-Algorithmic-Trading-System](https://github.com/saeed349/Microservices-Based-Algorithmic-Trading-System)</sub>                                            | <sub>docker based platfrom for developing algo trading strategies. Very interesting combinations of open source components were used including [backtrader](https://www.backtrader.com/) for backtest strategies / [mlflow](https://mlflow.org/) for managing the machine learning model life cycle  (i.e. training and developing machine learning models) / [airflow](https://airflow.apache.org/) used as workflow management including schedule data download etc. / [superset](https://superset.apache.org/) web data visualization tool similar to tableau / [minio](https://min.io/) for fast object storage (i.e. storing saved models and model artifacts) / postgresql used to store security master and daily and minute data. Also contains some details on deployment on cloud</sub> | <sub>2020-01-06 00:21:58</sub> | <sub>2024-04-08 19:33:16</sub> | <sub>443.0</sub>        | <sub>:heavy_check_mark:</sub>       | <sub>:star:x5</sub> |
| <sub>[Awesome-Quant-Machine-Learning-Trading](https://github.com/grananqvist/Awesome-Quant-Machine-Learning-Trading)</sub>                                                         | <sub>curated list of books/online courses/youtube videos/blogs/interviews/papers/code etc. Updates are pretty infrequent</sub>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | <sub>2018-11-05 21:09:06</sub> | <sub>2020-10-08 16:48:18</sub> | <sub>2675.0</sub>       | <sub>:heavy_multiplication_x:</sub> | <sub>:star:x5</sub> |
| <sub>[Hands-On-Machine-Learning-for-Algorithmic-Trading](https://github.com/PacktPublishing/Hands-On-Machine-Learning-for-Algorithmic-Trading)</sub>                               | <sub>repo for book [hands-on-machine learning for algorithmic trading](https://www.packtpub.com/product/hands-on-machine-learning-for-algorithmic-trading/9781789346411) covering topic from data/unsupervised learning/NPL/RNN & CNN/reinforcement learning etc. Leverage zipline/alphalens/sklearn/openai-gym etc as well. Good references to have</sub>                                                                                                                                                                                                                                                                                                            
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `raw_data/__init__.py`
```python

```

#### File: `generated_wiki/__init__.py`
```python

```

#### File: `conf.py`
```python
import os
PROJECT_ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
```

#### File: `git_util.py`
```python
from github import Github, Repository, GithubException
import os
import datetime


def get_github_client():
    # search for app_client and client secrets first, since this allow higher api request limit
    github_app = os.environ.get('GIT_APP_ID')
    if github_app is None:
        github_token = os.environ.get('GIT_TOKEN')
        g = Github(github_token)
    else:
        github_app_secret = os.environ.get('GIT_APP_SECRET')
        g = Github(
            client_id=github_app,
            client_secret=github_app_secret)
    return g


# *******
# repo specific information
# *******
def get_repo_path(in_url):
    repo_path = None
    if 'https://github.com/' in in_url:
        url_query = in_url.replace('https://github.com/', '')
        repo_path = '/'.join(url_query.split('/')[:2])
    return repo_path


def get_last_commit_date(input_repo: Repository):
    """
    get latest commit from repo
    :param input_repo:
    :return:
    """
    page = input_repo.get_commits().get_page(0)[0]
    return page.commit.author.date


def get_repo_attributes_dict(input_repo: Repository, last_commit_within_years: int = 2):
    result_dict = {}
    try:
        result_dict = {
            'repo_path': input_repo.full_name,
            'created_at': input_repo.created_at,
            'last_commit': get_last_commit_date(input_repo),
            'last_update': input_repo.updated_at,
            'star_count': input_repo.stargazers_count,
            'fork_count': input_repo.forks_count,
            'contributors_count': input_repo.get_contributors().totalCount

        }
        today = datetime.datetime.today()
        check_start_date = datetime.datetime(today.year - last_commit_within_years,
                                             today.month,
                                             today.day)

        if result_dict['last_commit'] >= check_start_date:
            repo_status = 'active'
        else:
            repo_status = 'inactive'
        result_dict['repo_status'] = repo_status
    except Exception as e:
        print(e)

    return result_dict
```

#### File: `git_status.py`
```python
import os
from conf import PROJECT_ROOT_DIR
import re
import pandas as pd

from git_util import get_repo_attributes_dict, get_github_client, get_repo_path


def get_repo_list():
    repo_df = pd.read_csv(os.path.join(PROJECT_ROOT_DIR, 'raw_data', 'url_list.csv'))
    if 'repo_path' not in repo_df.columns:
        repo_df['repo_path'] = repo_df['url'].apply(get_repo_path)
    return repo_df


def get_repo_status():
    g = get_github_client()
    repo_df = get_repo_list()
    for idx, row in repo_df.iterrows():
        repo_path = row['repo_path']
        if not pd.isna(repo_path):
            try:
                print('processing [{}]'.format(repo_path))
                repo = g.get_repo(repo_path)

                repo_attr_dict = get_repo_attributes_dict(repo)
            except Exception as ex:
                print(ex)
                repo_attr_dict = {}

            for k, v in iter(repo_attr_dict.items()):
                repo_df.loc[idx, k] = v
    repo_df.to_csv(os.path.join(PROJECT_ROOT_DIR, 'raw_data', 'url_list.csv'), index=False)


@DeprecationWarning
def parse_readme_md():
    """

    :return:
    usage:
    >>> df = parse_readme_md()
    >>> df.to_csv(os.path.join(PROJECT_ROOT_DIR, 'raw_data', 'url_list.csv'), index=False)
    """
    file_path = os.path.join(PROJECT_ROOT_DIR, 'README.md')
    with open(file_path) as f:
        lines = f.readlines()[11:]  # skip heading
        all_df_list = []
        for line_num in range(len(lines)):
            line = lines[line_num]
            if line.strip().startswith('#'):
                # find a heading
                heading = line.strip().replace('#', '').replace('\n', '').strip()
                # parse until next # or eof
                parsed_list = []
                line_num += 1
                while line_num < len(lines) and not lines[line_num].strip().startswith('#'):
                    link_line = lines[line_num].replace('\n', '').strip()
                    if len(link_line) > 0:
                        # usually in the format of '- [NAME](link) - comment
                        split_sections = link_line.split('- ')
                        if len(split_sections) == 2:
                            comment_str = None
                        elif len(split_sections) >= 3:
                            comment_str = '-'.join(split_sections[2:]).strip()
                        else:
                            raise Exception('link_line [{}] not supported'.format(link_line))

                        title_and_link = split_sections[1].strip()
                        title = re.search(r'\[(.*?)\]', title_and_link)
                        title_str = None
                        if title is not None:
                            title_str = title.group(1)
                            title_and_link = title_and_link.replace('[{}]'.format(title_str), '')
                        m_link = re.search(r'\((.*?)\)', title_and_link)
                        link_str = None
                        if m_link is not None:
                            link_str = m_link.group(1)
                        parsed_set = (title_str, link_str, comment_str)
                        parsed_list.append(parsed_set)
                    line_num += 1
                parsed_df = pd.DataFrame(parsed_list, columns=['name', 'url', 'comment'])
                parsed_df['category'] = heading
                all_df_list.append(parsed_df)
    final_df = pd.concat(all_df_list).reset_index(drop=True)
    return final_df


if __name__ == '__main__':
    get_repo_status()
```

#### File: `wiki_gen.py`
```python
from conf import PROJECT_ROOT_DIR
import os
import pandas as pd
import numpy as np
import re

from git_status import get_repo_list


def get_wiki_status_color(input_text):
    if input_text is None or input_text == 'inactive':
        result_text = ":heavy_multiplication_x:"
    else:
        result_text = ":heavy_check_mark:"
    return '<sub>{}</sub>'.format(result_text)


def get_wiki_rating(input_rating):
    result_text = ''
    if input_rating is not None and not np.isnan(input_rating):
        rating = int(input_rating)
        result_text = ':star:x{}'.format(rating)
    return '<sub>{}</sub>'.format(result_text)


def generate_wiki_per_category(output_path, update_readme: bool = True):
    """

    :param update_readme:
    :param output_path:
    """
    repo_df = get_repo_list()
    for category in repo_df['category'].unique():
        category_df = repo_df[repo_df['category'] == category].copy()
        url_md_list = []
        for idx, irow in category_df[['name', 'url']].iterrows():
            url_md_list.append('<sub>[{}]({})</sub>'.format(irow['name'], irow['url']))

        formatted_df = pd.DataFrame({
            'repo': url_md_list,
            'comment': category_df['comment'].apply(lambda x: '<sub>{}</sub>'.format(x)),
            'created_at': category_df['created_at'].apply(lambda x: '<sub>{}</sub>'.format(x)),
            'last_commit': category_df['last_commit'].apply(lambda x: '<sub>{}</sub>'.format(x)),
            'star_count': category_df['star_count'].apply(lambda x: '<sub>{}</sub>'.format(x)),
            'repo_status': category_df['repo_status'],
            'rating': category_df['rating']
        })
        # add color for the status
        formatted_df = formatted_df.sort_values(by=['rating', 'star_count'], ascending=False).reset_index(drop=True)
        formatted_df['repo_status'] = formatted_df['repo_status'].apply(lambda x: get_wiki_status_color(x))
        formatted_df['rating'] = formatted_df['rating'].apply(lambda x: get_wiki_rating(x))
        formatted_df.columns = ['<sub>{}</sub>'.format(x) for x in formatted_df.columns]

        clean_category_name = category.lower().replace(' ', '_')
        output_path_full = os.path.join(output_path, '{}.md'.format(clean_category_name))
        with open(output_path_full, 'w') as f:
            f.write(formatted_df.to_markdown(index=False))
        print('wiki generated in [{}]'.format(output_path_full))

        if update_readme:
            check_str = '[PLACEHOLDER_START:{}]'.format(clean_category_name)
            with open(os.path.join(PROJECT_ROOT_DIR, 'README.md')) as f:
                all_read_me = f.read()
                if check_str not in all_read_me:
                    print(f'section {check_str} not found')
                    continue

            # only display top 5, then expandable for extra 5
            with open(os.path.join(PROJECT_ROOT_DIR, 'README.md'), 'w') as f:

                table_str = formatted_df.iloc[:15].to_markdown(index=False)
                new_str = f"<!-- [PLACEHOLDER_START:{clean_category_name}] --> \n"
                new_str += table_str
                new_str += f"<!-- [PLACEHOLDER_END:{clean_category_name}] -->"

                search_start = re.escape('<!-- [PLACEHOLDER_START:{}] -->'.format(clean_category_name))
                search_end = re.escape('<!-- [PLACEHOLDER_END:{}] -->'.format(clean_category_name))
                pattern_s = re.compile(r'{}.*?{}'.format(search_start, search_end), re.DOTALL)
                write_str = re.sub(pattern_s, new_str, all_read_me)
                f.write(write_str)


if __name__ == '__main__':
    local_path = os.path.join(PROJECT_ROOT_DIR, 'generated_wiki')
    generate_wiki_per_category(local_path)
```


==================================================
