# ⚡ [QUANT-SOURCE-082] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_082_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: pyts (`WHEEL_pyts`)
- **Full Name**: `pyts`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
[![Build Status](https://dev.azure.com/johannfaouzi0034/johannfaouzi/_apis/build/status/johannfaouzi.pyts?branchName=main)](https://dev.azure.com/johannfaouzi0034/johannfaouzi/_build/latest?definitionId=1&branchName=main)
[![Documentation Status](https://readthedocs.org/projects/pyts/badge/?version=latest)](https://pyts.readthedocs.io/)
[![Codecov](https://codecov.io/gh/johannfaouzi/pyts/branch/main/graph/badge.svg)](https://codecov.io/gh/johannfaouzi/pyts)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyts.svg)](https://img.shields.io/pypi/pyversions/pyts.svg)
[![PyPI version](https://badge.fury.io/py/pyts.svg)](https://badge.fury.io/py/pyts)
[![Conda Version](https://img.shields.io/conda/vn/conda-forge/pyts.svg)](https://anaconda.org/conda-forge/pyts)
[![CodeQL](https://github.com/johannfaouzi/pyts/workflows/CodeQL/badge.svg)](https://github.com/johannfaouzi/pyts/actions?query=workflow%3ACodeQL)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1244152.svg)](https://doi.org/10.5281/zenodo.1244152)

## pyts: a Python package for time series classification

pyts is a Python package for time series classification. It
aims to make time series classification easily accessible by providing
preprocessing and utility tools, and implementations of
state-of-the-art algorithms. Most of these algorithms transform time series,
thus pyts provides several tools to perform these transformations.


### Installation

#### Dependencies

pyts requires:

- Python (>= 3.8)
- NumPy (>= 1.22.4)
- SciPy (>= 1.8.1)
- Scikit-Learn (>= 1.2.0)
- Joblib (>= 1.1.1)
- Numba (>= 0.55.2)

To run the examples Matplotlib (>=2.0.0) is required.


#### User installation

If you already have a working installation of numpy, scipy, scikit-learn,
joblib and numba, you can easily install pyts using ``pip``

    pip install pyts

or ``conda`` via the ``conda-forge`` channel

    conda install -c conda-forge pyts

You can also get the latest version of pyts by cloning the repository

    git clone https://github.com/johannfaouzi/pyts.git
    cd pyts
    pip install .


#### Testing

After installation, you can launch the test suite from outside the source
directory using pytest:

    pytest pyts


### Changelog

See the [changelog](https://pyts.readthedocs.io/en/stable/changelog.html)
for a history of notable changes to pyts.

### Development

The development of this package is in line with the one of the scikit-learn
community. Therefore, you can refer to their
[Development Guide](https://scikit-learn.org/stable/developers/). A slight
difference is the use of Numba instead of Cython for optimization.

### Documentation

The section below gives some information about the implemented algorithms in pyts.
For more information, please have a look at the
[HTML documentation available via ReadTheDocs](https://pyts.readthedocs.io/).

### Citation

If you use pyts in a scientific publication, we would appreciate
citations to the following [paper](http://www.jmlr.org/papers/v21/19-763.html):
```
Johann Faouzi and Hicham Janati. pyts: A python package for time series classification.
Journal of Machine Learning Research, 21(46):1−6, 2020.
```

Bibtex entry:
```
@article{JMLR:v21:19-763,
  author  = {Johann Faouzi and Hicham Janati},
  title   = {pyts: A Python Package for Time Series Classification},
  journal = {Journal of Machine Learning Research},
  year    = {2020},
  volume  = {21},
  number  = {46},
  pages   = {1-6},
  url     = {http://jmlr.org/papers/v21/19-763.html}
}
```

### Implemented features

**Note: the content described in this section corresponds to the main branch
(i.e., the latest version), and not the latest released version. You may have to
install the latest version to use some of these features.**

pyts consists of the following modules:

- `approximation`: This module provides implementations of algorithms that
approximate time series. Implemented algorithms are
[Piecewise Aggregate Approximation](https://pyts.readthedocs.io/en/latest/generated/pyts.approximation.PiecewiseAggregateApproximation.html),
[Symbolic Aggregate approXimation](https://pyts.readthedocs.io/en/latest/generated/pyts.approximation.SymbolicAggregateApproximation.html),
[Discrete Fourier Transform](https://pyts.readthedocs.io/en/latest/generated/pyts.approximation.DiscreteFourierTransform.html),
[Multiple Coefficient Binning](https://pyts.readthedocs.io/en/latest/generated/pyts.approximation.MultipleCoefficientBinning.html) and
[Symbolic Fourier Approximation](https://pyts.readthedocs.io/en/latest/generated/pyts.approximation.SymbolicFourierApproximation.html).

- `bag_of_words`: This module provide tools to transform time series into bags
of words. Implemented algorithms are
[WordExtractor](https://pyts.readthedocs.io/en/latest/generated/pyts.bag_of_words.WordExtractor.html) and
[BagOfWords](https://pyts.readthedocs.io/en/latest/generated/pyts.bag_of_words.BagOfWords.html).


- `classification`: This module provides implementations of algorithms that
can classify time series. Implemented algorithms are
[KNeighborsClassifier](https://pyts.readthedocs.io/en/latest/generated/pyts.classification.KNeighborsClassifier.html),
[SAXVSM](https://pyts.readthedocs.io/en/latest/generated/pyts.classification.SAXVSM.html),
[BOSSVS](https://pyts.readthedocs.io/en/latest/generated/pyts.classification.BOSSVS.html),
[LearningShapelets](https://pyts.readthedocs.io/en/latest/generated/pyts.classification.LearningShapelets.html),
[TimeSeriesForest](https://pyts.readthedocs.io/en/latest/generated/pyts.classification.TimeSeriesForest.html) and
[TSBF](https://pyts.readthedocs.io/en/latest/generated/pyts.classification.TSBF.html).

- `datasets`: This module provides utilities to make or load toy datasets,
as well as fetching datasets from the
[UEA & UCR Time Series Classification Repository](http://www.timeseriesclassification.com).

- `decomposition`: This module provides implementations of algorithms that
decompose a time series into several time series. The only implemented
algorithm is
[Singular Spectrum Analysis](https://pyts.readthedocs.io/en/latest/generated/pyts.decomposition.SingularSpectrumAnalysis.html).

- `image`: This module provides implementations of algorithms that transform
time series into images. Implemented algorithms are
[Recurrence Plot](https://pyts.readthedocs.io/en/latest/generated/pyts.image.RecurrencePlot.html),
[Gramian Angular Field](https://pyts.readthedocs.io/en/latest/generated/pyts.image.GramianAngularField.html) and
[Markov Transition Field](https://pyts.readthedocs.io/en/latest/generated/pyts.image.MarkovTransitionField.html).

- `metrics`: This module provides implementations of metrics that are specific
to time series. Implemented metrics are
[Dynamic Time Warping](https://pyts.readthedocs.io/en/latest/generated/pyts.metrics.dtw.html)
with several variants and the
[BOSS](https://pyts.readthedocs.io/en/latest/generated/pyts.metrics.boss.html)
metric.

- `multivariate`: This modules provides utilities to deal with multivariate
time series. Available tools are
[MultivariateTransformer](https://pyts.readthedocs.io/en/latest/generated/pyts.multivariate.transformation.MultivariateTransformer.html) and
[MultivariateClassifier](https://pyts.readthedocs.io/en/latest/generated/pyts.multivariate.classification.MultivariateClassifier.html)
to transform and classify multivariate time series using tools for univariate
time series respectively, as well as
[JointRecurrencePlot](https://pyts.readthedocs.io/en/latest/generated/pyts.multivariate.image.JointRecurrencePlot.html) and
[WEASEL+MUSE](https://pyts.readthedocs.io/en/latest/generated/pyts.multivariate.transformation.WEASELMUSE.html).

- `preprocessing`: This module provides most of the scikit-learn preprocessing
tools but applied sample-wise (i.e. to each time series independently) instead
of feature-wise, as well as an
[imputer](https://pyts.readthedocs.io/en/latest/generated/pyts.preprocessing.InterpolationImputer.html)
of missing values using interpolation. More information is available at the
[pyts.preprocessing API documentation](https://pyts.readthedocs.io/en/latest/api.html#module-pyts.preprocessing).

- `transformation`: This module provides implementations of algorithms that
transform a data set of time series with shape `(n_samples, n_timestamps)` into
a data set with shape `(n_samples, n_extracted_features)`. Implemented algorithms are
[BagOfPatterns](https://pyts.readthedocs.io/en/latest/generated/pyts.transformation.BagOfPatterns.html),
[BOSS](https://pyts.readthedocs.io/en/latest/generated/pyts.transformation.BOSS.html),
[ShapeletTransform](https://pyts.readthedocs.io/en/latest/generated/pyts.transformation.ShapeletTransform.html),
[WEASEL](https://pyts.readthedocs.io/en/latest/generated/pyts.transformation.WEASEL.html) and
[ROCKET](https://pyts.readthedocs.io/en/latest/generated/pyts.transformation.ROCKET.html).

- `utils`: a simple module with
[utility functions](https://pyts.readthedocs.io/en/latest/api.html#module-pyts.utils).

## License
The contents of this repository is under a [BSD 3-Clause License](https://github.com/johannfaouzi/pyts/blob/main/LICENSE.txt).

### Core Implementation Code & Architecture
#### File: `pyts/classification/tests/__init__.py`
```python

```

#### File: `pyts/metrics/tests/__init__.py`
```python

```

#### File: `pyts/multivariate/classification/tests/__init__.py`
```python

```

#### File: `pyts/multivariate/transformation/tests/__init__.py`
```python

```

#### File: `pyts/multivariate/tests/__init__.py`
```python

```

#### File: `pyts/multivariate/utils/tests/__init__.py`
```python

```


==================================================


## [2/3] Repository: quantaxis (`WHEEL_quantaxis`)
- **Full Name**: `quantaxis`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# QUANTAXIS 2.1.0-alpha2

<div align="center">

**⭐ 如果这个项目对您有帮助，请点击Star支持我们！**

**🔄 Fork本项目开始您的量化交易之旅！**

Made with ❤️ by [@yutiansut](https://github.com/yutiansut) and [contributors](https://github.com/QUANTAXIS/QUANTAXIS/graphs/contributors)

© 2016-2025 QUANTAXIS. Released under the MIT License.

</div>


[![Powered by OrcaRouter](https://img.shields.io/badge/Powered_by-OrcaRouter-2563eb)](https://www.orcarouter.ai/ref/ref_ce94b4f99fa4cde037ea)

> 🚀 **全新升级**: Python 3.9+、QARS2 Rust核心集成、100x性能提升
>
> **最新版本**: v2.1.0-alpha2 | **Python**: 3.9-3.12 | **更新日期**: 2025-10-25

---

## 🌟 新特性 (v2.1.0)

### ⚡ QARS2 Rust核心集成 - 性能飞跃

- **100x账户操作加速**: 创建账户从50ms降至0.5ms
- **10x回测速度提升**: 10年日线回测从30秒降至3秒
- **90%内存优化**: 大规模持仓内存占用降低90%
- **无缝集成**: 完全兼容QIFI协议，自动回退Python实现

### 🔧 Python 3.9-3.12 现代化

- **依赖升级**: 60+核心依赖现代化 (pymongo 4.10+, pandas 2.0+, pyarrow 15.0+)
- **性能优化**: 利用Python 3.11+的性能提升
- **类型安全**: 更好的类型提示支持

### 📦 QARSBridge - Rust桥接层

```python
from QUANTAXIS.QARSBridge import QARSAccount, has_qars_support

# 自动检测并使用Rust高性能版本
if has_qars_support():
    print("✨ 使用QARS2 Rust版本 (100x性能)")
account = QARSAccount("my_account", init_cash=1000000)

# API完全兼容，无需修改代码
account.buy("000001", 10.5, "2025-01-15", 1000)
```

---

## 🔗 相关项目生态

### 核心项目

- 🦀 [**QARS**](https://github.com/yutiansut/qars) - QUANTAXIS Rust核心 (高性能账户、回测引擎)
- ⚡ [**QADataSwap**](https://github.com/QUANTAXIS/qadataswap) - 跨语言零拷贝通信 (Python/Rust/C++)
- 🏛️ [**QAEXCHANGE-RS**](https://github.com/yutiansut/qaexchange-rs) - Rust交易所 + HTAP混合数据库



### 扩展实现

- 📊 [**QAUltra-cpp**](https://github.com/QUANTAXIS/qaultra-cpp) - QUANTAXIS C++实现
- 🔥 [**QAUltra-rs**](https://github.com/QUANTAXIS/qautlra-rs) - QUANTAXIS Rust实现 (部分开源)


[![Github workers](https://img.shields.io/github/watchers/quantaxis/quantaxis.svg?style=social&label=Watchers&)](https://github.com/quantaxis/quantaxis/watchers)
[![GitHub stars](https://img.shields.io/github/stars/quantaxis/quantaxis.svg?style=social&label=Star&)](https://github.com/quantaxis/quantaxis/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/quantaxis/quantaxis.svg?style=social&label=Fork&)](https://github.com/quantaxis/quantaxis/fork)

[点击右上角Star和Watch来跟踪项目进展! 点击Fork来创建属于你的QUANTAXIS!]

![QUANTAXIS_LOGO_LAST_small.jpg](./qalogo.png)

---

## 📞 联系方式

- **项目主页**: https://github.com/yutiansut/QUANTAXIS
- **作者**: yutiansut
- **Email**: yutiansut@qq.com
- **微信公众号**: QAPRO
- **微信**: quantitativeanalysis

---




更多文档在[QABook Release](https://github.com/QUANTAXIS/QUANTAXIS/releases/download/latest/quantaxis.pdf)

Quantitative Financial FrameWork

## 📚 核心模块

### 1. 🦀 QARSBridge - Rust桥接层 (v2.1新增)

**QARS2 Rust核心的Python包装器，提供100x性能提升**

- **QARSAccount**: 高性能QIFI账户系统
  - 股票交易: `buy()`, `sell()`
  - 期货交易: `buy_open()`, `sell_open()`, `buy_close()`, `sell_close()`
  - 账户查询: `get_qifi()`, `get_positions()`, `get_account_info()`
  - 完全兼容QIFI协议，跨语言一致性 (Python/Rust/C++)

- **QARSBacktest**: Rust回测引擎
  - 10x回测速度提升
  - 支持自定义策略 (`QARSStrategy`基类)
  - 内存占用降低90%

- **自动回退机制**: QARS2未安装时自动使用纯Python实现

```python
# 完整示例
from QUANTAXIS.QARSBridge import QARSAccount

account = QARSAccount("test", init_cash=1000000)
account.buy("000001", 10.5, "2025-01-15", 1000)      # 股票买入
account.buy_open("IF2512", 4500.0, "2025-01-15", 2)  # 期货开仓
positions = account.get_positions()                   # 查询持仓
```

📖 **详细文档**: [QARSBridge README](./QUANTAXIS/QARSBridge/README.md)

---

### 2. 🔄 QADataBridge - 零拷贝数据交换 (v2.1新增)

**基于QADataSwap的跨语言零拷贝数据传输，5-10x性能提升**

- **零拷贝转换**:
  - Pandas ↔ Polars (2.5x加速)
  - Pandas ↔ Arrow (零拷贝)
  - Polars ↔ Arrow (零拷贝)
  - 批量转换支持

- **共享内存通信**:
  - 跨进程数据传输 (7x加速)
  - 实时行情分发
  - 策略间数据共享

- **自动回退机制**: QADataSwap未安装时自动使用标准转换

```python
# 零拷贝转换示例
from QUANTAXIS.QADataBridge import convert_pandas_to_polars
import pandas as pd

df_pandas = pd.DataFrame({'price': [10.5, 20.3], 'volume': [1000, 2000]})
df_polars = convert_pandas_to_polars(df_pandas)  # 零拷贝，2.5x加速

# 共享内存示例
from QUANTAXIS.QADataBridge import SharedMemoryWriter, SharedMemoryReader

# 进程A：写入数据
writer = SharedMemoryWriter("market_data", size_mb=50)
writer.write(df_polars)

# 进程B：读取数据
reader = SharedMemoryReader("market_data")
df = reader.read(timeout_ms=5000)  # 零拷贝，7x加速
```

📖 **详细文档**: [QADataBridge README](./QUANTAXIS/QADataBridge/README.md)

---

### 3. 💾 QASU / QAFetch - 多市场数据

- 支持MongoDB / ClickHouse存储
- 自动运维和数据更新
- Tick / L2 Order / Transaction数据格式
- 因子化数据结构

### 4. 🕐 QAUtil - 工具函数

- 交易时间、交易日历
- 时间向前向后推算
- 市场识别、DataFrame转换

### 5. 💼 QIFI / QAMarket - 统一账户体系

**多市场、多语言统一账户协议**

- **qifiaccount**: 标准QIFI账户，与Rust/C++版本保持100%一致
- **qifimanager**: 多账户管理系统
- **qaposition**: 单标的精准仓位管理 (套利/CTA/股票)
- **marketpreset**: 市场预制基类 (tick大小/保证金/手续费)

**QIFI协议特点**:
- 跨语言兼容 (Python/Rust/C++)
- 完整账户状态 (账户/持仓/订单/成交)
- 增量更新支持 (Diff机制)
- MongoDB友好

### 6. 📊 QAFactor - 因子研究

- 单因子研究入库
- 因子管理、测试
- 因子合并
- 优化器 [开发中]

### 7. 📈 QAData - 内存数据库

多标的多市场数据结构，支持：
- 实时计算
- 回测引擎
- 高性能数据访问

### 8. 📉 QAIndicator - 自定义指标

- 支持自定义指标编写
- 批量全市场apply
- 因子表达式构建

### 9. ⚙️ QAEngine - 异步计算

- 自定义线程/进程基类
- 异步计算支持
- 局域网分布式计算agent

### 10. 📮 QAPubSub - 消息队列

基于RabbitMQ的消息系统：
- 1-1 / 1-n / n-n 消息分发
- 计算任务分发收集
- 实时订单流

### 11. 🎯 QAStrategy - 回测套件

- CTA策略回测
- 套利策略回测
- 完整QIFI模式支持

### 12. 🌐 QAWebServer - 微服务

- Tornado Web服务器
- 中台微服务构建
- RESTful API

### 13. 📅 QASchedule - 任务调度

- 后台任务调度
- 自动运维
- 远程任务调度



---

## 🆕 版本更新说明

### v2.1.0 (2025-10-25) - 重大性能升级

#### 🚀 核心升级

**1. QARS2 Rust核心集成**
- ✅ QARSBridge桥接层 - 100x性能提升
- ✅ 完全兼容QIFI协议
- ✅ 自动fallback到Python实现
- ✅ 账户操作: 50ms → 0.5ms
- ✅ 回测速度: 30s → 3s (10年日线)
- ✅ 内存优化: -90%

**2. Python现代化**
- ✅ Python版本: 3.5-3.10 → **3.9-3.12**
- ✅ 依赖升级: 60+核心依赖现代化
  - pymongo: 3.11.2 → 4.10.0+
  - pandas: 1.1.5 → 2.0.0+
  - pyarrow: 6.0.1 → 15.0.0+
  - tornado: 6.3.2 → 6.4.0+
- ✅ 移除过时依赖: delegator.py, six, pyconvert

**3. 新增模块**
- ✅ `QARSBridge/`: QARS2桥接层
  - `qars_account.py`: 高性能账户包装器
  - `qars_backtest.py`: Rust回测引擎
  - `QIFI_PROTOCOL.md`: 完整协议规范
- ✅ `examples/qarsbridge_example.py`: 完整使用示例

**4. 安装方式优化**
```bash
# 基础安装
pip install -e .

# 包含Rust组件 (推荐)
pip install -e .[rust]

# 包含性能优化包
pip install -e .[performance]

# 完整安装
pip install -e .[full]
```

#### 📝 升级文档
- ✅ [UPGRADE_PLAN.md](./UPGRADE_PLAN.md) - 完整升级计划
- ✅ [PHASE1_COMPLETE.md](./PHASE1_COMPLETE.md) - Phase 1完成报告
- ✅ [PHASE2_COMPLETE.md](./PHASE2_COMPLETE.md) - Phase 2完成报告
- ✅ [QIFI_PROTOCOL.md](./QUANTAXIS/QARSBridge/QIFI_PROTOCOL.md) - QIFI协议规范

---

### v2.0.0 - 架构重构

本版本为不兼容升级，涉及重大架构改变：

#### 数据层改进

- ✅ ClickHouse客户端集成
- ✅ Tabular数据支持
- ✅ 因子化数据结构
- ✅ Tick / L2 Order / Transaction格式

#### 微服务架构

- ✅ QAWebServer - Tornado Web服务
- ✅ QASchedule - 动态任务调度
- ✅ DAG Pipeline模型
- ✅ QAPubSub - RabbitMQ消息队列

#### 账户系统升级

- ⚠️ 移除QAARP (不再维护老版本)
- ✅ 完整QIFI模块
  - 保证金模型
  - 股票/期货支持
  - 期权 [开发中]

#### 实盘/模拟盘

- ✅ QIFI结构对接
- ✅ CTP接口 (期货/期权)
- ✅ QMT对接 (股票)
- ✅ 母子账户OMS
- ✅ OrderGateway风控

#### 多语言集成

- ✅ QUANTAXIS Rust版本通信
- ✅ Apache Arrow跨语言数据交换
  - pyarrow (Python)
  - arrow-rs (Rust)
  - libarrow (C++)
- ✅ Rust/C++账户支持
- ✅ Rust Job Worker

---

## 🚀 快速开始

### 系统要求

- **Python**: 3.9 - 3.12 (推荐3.11+)
- **操作系统**: Linux / macOS / Windows
- **内存**: 最低4GB，推荐8GB+
- **数据库**: MongoDB 4.0+ / ClickHouse 20.0+ (可选)

### 安装

#### 1. 基础安装

```bash
# 克隆仓库
git clone https://github.com/QUANTAXIS/QUANTAXIS.git
cd QUANTAXIS

# 安装依赖
pip install -e .
```

#### 2. 包含Rust组件 (推荐 - 100x性能)

```bash
# 安装QUANTAXIS + QARS2
pip install -e .[rust]

# 或手动安装QARS2
cd /home/quantaxis/qars2
pip install -e .
```

#### 3. 完整安装

```bash
# 安装所有组件
pip install -e .[full]

# 包含:
# - QARS2 Rust核心
# - QADataSwap跨语言通信
# - Polars高性能DataFrame
# - 所有可选依赖
```

#### 4. 验证安装

```python
import QUANTAXIS as QA
from QUANTAXIS.QARSBridge import has_qars_support

print(f"QUANTAXIS版本: {QA.__version__}")
print(f"QARS2支持: {has_qars_support()}")

# 预期输出:
# QUANTAXIS版本: 2.1.0.alpha2
# QARS2支持: True
```

### 快速示例

```python
from QUANTAXIS.QARSBridge import QARSAccount

# 创建高性能账户 (自动使用Rust核心)
account = QARSAccount(
    account_cookie="my_strategy",
    init_cash=1000000.0
)

# 股票交易
account.buy("000001", 10.5, "2025-01-15", 1000)
account.sell("000001", 10.8, "2025-01-16", 500)

# 期货交易
account.buy_open("IF2512", 4500.0, "2025-01-15", 2)
account.sell_close("IF2512", 4520.0, "2025-01-16", 1)

# 查询持仓
positions = account.get_positions()
print(positions)

# 获取QIFI格式账户数据
qifi = account.get_qifi()
print(f"账户权益: {qifi['accounts']['balance']}")
print(f"可用资金: {qifi['accounts']['available']}")
```

### 数据库配置

```python
# MongoDB配置
import QUANTAXIS as QA

# 设置MongoDB连接
QA.DATABASE = QA.QAUtil.QALogs.QA_Setting.MONGO_URI
# 默认: mongodb://localhost:27017/quantaxis

# ClickHouse配置
QA.CLICKHOUSE_HOST = 'localhost'
QA.CLICKHOUSE_PORT = 9000
```

---

## 📖 文档

### 📚 文档中心

完整文档请访问 **[文档中心 (Documentation Hub)](./doc/README.md)**

### 快速导航

**🚀 入门指南**
- [快速开始](./doc/getting-started/quickstart.md) - 10分钟上手教程
- [安装指南](./doc/getting-started/installation.md) - 详细安装步骤

**📘 API参考**
- [API概览](./doc/api-reference/overview.md) - 完整API文档
- [QAFetch](./doc/api-reference/qafetch.md) - 数据获取
- [QAData](./doc/api-reference/qadata.md) - 数据结构
- [QAMarket/QIFI](./doc/api-reference/qamarket.md) - 账户体系

**🔧 高级功能**
- [资源管理器](./doc/advanced/resource-manager.md) - 统一资源管理
- [Rust集成](./doc/advanced/rust-integration.md) - 高性能组件
- [数据桥接](./doc/advanced/data-bridge.md) - 零拷贝数据交换

**🐳 部署指南**
- [Docker部署](./doc/deployment/docker.md) - 容器化部署
- [Kubernetes部署](./doc/deployment/kubernetes.md) - K8s集群部署
- [部署概览](./doc/deployment/overview.md) - 完整部署指南

**📦 迁移指南**
- [2.0 → 2.1 迁移](./doc/migration/v2.0-to-v2.1.md) - 升级步骤和注意事项
- [兼容性状态](./doc/migration/COMPATIBILITY_STATUS.md) - 100%向后兼容

**👨‍💻 开发者**
- [贡献指南](./doc/development/contributing.md) - 如何参与开发
- [最佳实践](./doc/development/best-practices.md) - 生产环境建议
- [开发指南 (CLAUDE.md)](./CLAUDE.md) - AI辅助开发

**📘 其他资源**
- [完整手册 (QABook PDF)](https://github.com/QUANTAXIS/QUANTAXIS/releases/download/latest/quantaxis.pdf)
- [示例代码](./examples/) - 完整示例集合

---

## 🤝 社区与支持

### GitHub

QUANTAXIS 是一个开放的项目, 在开源的3年中有大量的小伙伴加入了我, 并提交了相关的代码, 感谢以下的同学们

<a href="https://github.com/QUANTAXIS/QUANTAXIS/graphs/contributors"><img src="https://opencollective.com/QUANTAXIS/contributors.svg?width=890&button=false" /></a>



**问题反馈**:
- 💬 [GitHub Issues](https://github.com/QUANTAXIS/QUANTAXIS/issues) - 提交Bug和功能请求
- 🌟 [GitHub Discussions](https://github.com/QUANTAXIS/QUANTAXIS/discussions) - 技术讨论

### 社群

#### QQ群

- 💬 **QUANTAXIS交流群**: 563280067 [群链接](https://jq.qq.com/?_wv=1027&k=4CEKGzn)
- 👨‍💻 **QUANTAXIS开发群**: 773602202 (贡献代码请加此群，需备注GitHub ID)
- 🔥 **期货实盘部署群**: 945822690 (仅限本地多账户部署用户)

#### Discord

- 🌍 [QUANTAXIS Discord社区](https://discord.gg/mkk5RgN)

#### 论坛

- 📝 [QUANTAXIS CLUB论坛](http://www.yutiansut.com:3000)
  - 论坛提问享有最高回复优先级

#### 公众号

- 📱 关注公众号获取最新动态和免费下单推送接口
  - 回复 `trade` 获取下单接口

![公众号](http://picx.gulizhu.com/Fr0pHbwB7-zrq_HAKsvB8g2zaP_A)

---

## 📊 性能对比

### QARS2 Rust vs Python

| 操作 | Python版本 | QARS2 Rust | 加速比 |
|------|-----------|-----------|-------|
| 创建1000个账户 | ~50秒 | ~0.5秒 | **100x** ⚡ |
| 发送10000个订单 | ~50秒 | ~0.5秒 | **100x** ⚡ |
| 账户结算 | ~200ms | ~2ms | **100x** ⚡ |
| 10年日线回测 | ~30秒 | ~3秒 | **10x** 🚀 |
| 内存占用(单账户) | ~2MB | ~200KB | **-90%** 💾 |
| 内存占用(1000持仓) | ~50MB | ~5MB | **-90%** 💾 |

### Python版本性能

| Python版本 | 性能提升 | 推荐度 |
|-----------|---------|-------|
| Python 3.9 | 基准 | ⭐⭐⭐ |
| Python 3.10 | +10% | ⭐⭐⭐⭐ |
| Python 3.11 | +25% | ⭐⭐⭐⭐⭐ 最佳 |
| Python 3.12 | +20% | ⭐⭐⭐⭐⭐ 最新 |

---

## 💰 项目支持

### 捐赠

写代码不易...请作者喝杯咖啡呗? ☕

![支付宝捐赠](config/ali.jpg)

**注**: 支付时请备注您的名字/昵称，我们会维护一个赞助列表感谢您的支持！

### 企业赞助

如需企业级支持、定制开发或技术咨询，请联系:
- 📧 Email: yutiansut@qq.com
- 💼 企业服务: 提供定制化量化交易解决方案

---

## 📜 许可证

本项目采用 **MIT License** 开源许可证。

```
Copyright (c) 2016-2025 yutiansut/QUANTAXIS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...
```

完整许可证请查看 [LICENSE](./LICENSE) 文件。

---

## 👏 致谢

### 核心贡献者

特别感谢所有为QUANTAXIS做出贡献的开发者！

### 技术栈

QUANTAXIS得以实现离不开以下优秀的开源项目:

- **Python生态**: pandas, numpy, scipy, matplotlib
- **数据库**: MongoDB, ClickHouse, Redis
- **Web框架**: Tornado, Flask
- **消息队列**: RabbitMQ (pika)
- **Rust生态**: PyO3, Polars, Arrow
- **金融数据**: tushare, pytdx

### 特别鸣谢

- **QARS2项目组**: 提供高性能Rust核心
- **社区贡献者**: 所有提交PR和Issue的朋友们
- **早期用户**: 在项目初期就给予支持和反馈的用户

---

## 🗺️ 路线图

### v2.1.x (当前)
- ✅ QARS2 Rust核心集成
- ✅ Python 3.9-3.12支持
- ✅ QARSBridge桥接层
- 🔄 QADataSwap跨语言通信 (进行中)
- 📋 完善文档和示例

### v2.2.0 (计划中)
- 📊 完整的QADataSwap集成
- 🔥 Polars全面替代pandas (可选)
- ⚡ 更多Rust加速模块
- 🧪 增强的回测引擎

### v3.0.0 (未来)
- 🤖 AI驱动的策略优化
- 🌐 分布式回测系统
- 📱 移动端支持
- ☁️ 云原生部署

### Core Implementation Code & Architecture
#### File: `QUANTAXIS/QAData/QAFeatureStruct.py`
```python

```

#### File: `QUANTAXIS/QAFetch/QAdata.py`
```python

```

#### File: `QUANTAXIS/QAStrategy/qahedgebase.py`
```python

```

#### File: `QUANTAXIS/QAStrategy/qafactorbase.py`
```python

```

#### File: `qapro-rs/src/qaportfolio/lib.rs`
```python

```

#### File: `qapro-rs/src/qaconnector/rabbitmq/mod.rs`
```python

```


==================================================


## [3/3] Repository: quantick (`WHEEL_quantick`)
- **Full Name**: `quantick`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<p align="center">
  <img src="logo/logo-dark.png" alt="quantick logo" width="480">
</p>

# quantick

**Real-time alternative bar charts for order flow trading — and one engine to take your research from chart to backtest to bot.**

<p align="center">
  <img src="img/quantick_v2.png" alt="quantick desktop chart showing live BTCUSDT tick bars over a Bookmap-style L2 liquidity heatmap, with buy/sell aggression bubbles, L2 reduction marks and a dedicated live lane for the forming bar" width="900">
</p>

<p align="center"><em>Live BTCUSDT tick bars over the Bookmap-inspired L2 liquidity heatmap, with buy/sell aggression bubbles, L2 reduction marks and a live lane where the forming bar's tape keeps moving — this is <code>cargo run -p quantick-app</code> out of the box.</em></p>

> ⚠️ Early development, but already runnable. The Rust bar engine, public Binance and Hyperliquid feeds, and the native desktop chart work today — you can clone, build and watch bars form in real time in a few minutes (see [Quick start](#quick-start--build-test-run)). APIs will still churn. Star/watch the repo to follow along.

## Why this exists

Time-based candles distort order flow. A 1-minute bar at the session open and a 1-minute bar during lunch look identical on your chart, yet one may contain fifty times more trading than the other. Every indicator you compute on top inherits that distortion: a delta of +500 contracts means one thing in a quiet bar and something completely different in a busy one.

The fix has been known for decades: sample by **activity** instead of time. Close a bar every N trades (tick bars), every N contracts (volume bars), every $N of notional (dollar bars), or whenever buying/selling pressure gets unusually one-sided (imbalance bars). The research literature — from Ané & Geman (2000) to López de Prado's *Advances in Financial Machine Learning* — documents why this works: activity-sampled bars have far better statistical properties, and they make flow metrics comparable from bar to bar.

**Quant funds and professional desks use these bar types every day.** But the tooling has stayed locked up: it lives inside proprietary platforms (Bookmap, ATAS, Sierra Chart, NinjaTrader) that don't expose an engine you can program against, or inside private codebases that never see daylight. If you want to watch these bars form live on a chart — and then hand the *exact same bars* to a backtest or a trading bot — there is essentially no open-source option today.

quantick exists to change that: **a free, open, programmable implementation of the charts professionals actually use, built for the community.**

## What quantick is for

1. **Visualize.** A native desktop app that renders tick, volume, dollar and imbalance bars from a live market feed — with per-bar delta and CVD built in. See the market the way flow traders read it.
2. **Research.** Study setups directly on the charts: how does absorption look on volume bars? Where does CVD diverge? Chart-driven analysis is where strategy ideas are born.
3. **Build.** The same engine that draws your chart feeds your backtests and your bots. The bars your strategy trades live are byte-identical to the bars you researched and backtested — parity by construction, not by discipline.
4. **Operate.** The desktop app exposes itself to an AI agent over **MCP** — read the chart, watch for the bar you point at, annotate it, attach a script — under a capability contract you grant and can revoke. See [Drive it with an agent](#drive-it-with-an-agent-mcp).

## Quick start — build, test, run

You don't need an exchange account, an API key or any credentials. Out of the box the chart connects to Binance's **public** market data and opens on `BTCUSDT`.

### 1. Install Rust

quantick is pure Rust. Install [rustup](https://rustup.rs/) — that is the only choice you have to make. The repository pins the exact toolchain it builds with in `rust-toolchain.toml`, and rustup installs and selects that version, with the components it needs, the first time you run a cargo command in the clone:

```sh
# macOS / Linux
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
# Windows: download and run rustup-init.exe from https://rustup.rs

rustup --version   # that is all you need here
```

Inside the clone, `rustc --version` will report the pinned version rather than whatever you installed — that is `rust-toolchain.toml` doing its job. CI reads the same file, so the toolchain is never the difference between your machine and a red build.

### 2. Clone and build

```sh
git clone https://github.com/milocaetano/quantick.git
cd quantick
cargo build --workspace
```

The first build compiles every dependency and takes a few minutes; later builds are incremental and fast.

### 3. Run the tests

The engine is developed test-first and guarded by golden/snapshot tests (fixed trades in → known bars out). Run the whole suite with:

```sh
cargo test --workspace
```

### 4. Run the chart

```sh
cargo run -p quantick-app
```

A native window titled **quantick** opens, recovers the factual recent trades
available from the selected source and then streams live trades, forming bars as
they happen. From the controls bar you can switch the **bar type** live — tick,
volume, dollar, time or imbalance — and tune its parameter. For the smoothest
rendering on a busy order book, build optimized:

```sh
cargo run --release -p quantick-app
```

> The chart is a native desktop app (egui) and needs a graphical display; it won't run on a headless server. CI builds the whole workspace on Linux and on Windows, runs the full test suite on Linux and the engine and guard tests on Windows; it's used daily on Windows. macOS is neither built nor tested by CI.

### 5. (Optional) Pick a different feed or symbol

Feeds and symbols are configuration, never hardcoded. For a one-off startup
selection, set `QUANTICK_DEFAULT_FEED` and `QUANTICK_DEFAULT_SYMBOL`; these
change only what opens and keep every configured feed in the selector. For
example, to open directly on Hyperliquid BTC:

```sh
QUANTICK_DEFAULT_FEED=hyperliquid \
QUANTICK_DEFAULT_SYMBOL=BTC \
cargo run --release -p quantick-app
```

For a custom catalog, point `QUANTICK_CONFIG` at a TOML file or place a
git-ignored `quantick.toml` in the working directory. These files replace the
complete built-in catalog; they are not merged with it. Start by copying
[`crates/app/config/feeds.toml`](crates/app/config/feeds.toml), then edit the
copy so Binance, Hyperliquid or MetaTrader are removed only intentionally.
The same file documents the optional MetaTrader 5 bridge, L2 heatmap toggles
and logging.

The built-in selector also includes Hyperliquid perpetuals (`BTC`, `ETH`,
`HYPE`, `SOL`, `ZEC`). They need no account or API key: select **Hyperliquid**,
pick a coin, then use the same **⚙ L2** and **⚙ bubbles** controls as Binance.
Hyperliquid's initial WebSocket response carries only a short recent-trades
recovery window, so older-history paging is disabled instead of being
reconstructed from candles.

### Contributing

Working on the code? Every change must pass the four-check verification loop (`cargo fmt --all -- --check`, `cargo clippy --workspace --all-targets`, `cargo build --workspace`, `cargo test --workspace`) before commit — the same checks CI enforces. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

## Drive it with an agent (MCP)

Quantick ships its own **MCP server**. The chart is not only something you
watch: it is something an AI agent can read, and — when you allow it —
answer on.

The design rule behind this is that a capability never ships reachable by
mouse alone. Every action gets a named call, a readable result and a registry
entry, so the assistant and the trader operate the same application through
the same contract.

### Connect one in three steps

```sh
cargo build --release -p quantick-mcp
target/release/quantick-mcp setup --client claude   # or: --client codex
```

1. **Register.** `setup` prints the exact registration command for your
   client, filled in with the binary's absolute path. It reads nothing but
   its own path, so it works before Quantick is running. Run the command it
   prints.
2. **Allow.** In Quantick, open **Tools → Local agent access**, enable
   it, and tick the scopes the connection gets.
3. **Connect.** In the client, call `quantick_describe`.

The adapter attaches to a window you already opened — it never launches
the application, never writes a client configuration file and never stores a
token. Close the window, or turn access off, and every connection is revoked.

### What an agent can do

| Tool | What it answers |
| --- | --- |
| `quantick_describe` | The live instances; then version, profile, scopes, modules, capabilities and limits for one of them |
| `quantick_get_snapshot` | One coherent capture of the requested scopes, taken in a single pass, with a capture revision |
| `quantick_get_chart_window` | A paginated, append-only page of closed bars: OHLC, volume, delta, trade count, as exact decimal strings |
| `quantick_get_scene` | Every control on screen, each with a frame-stable ID, its owner, and a coded reason when it cannot be operated |
| `quantick_get_diagnostics` | The bounded health view: frame timing, feed arrival, engine state, queue metrics |
| `quantick_read_events` | A page of the semantic event journal — tab, focus, feed, replay and market changes, and the bars you marked |
| `quantick_wait_for_change` | Parks up to 30 s until the journal moves, instead of polling |
| `quantick_capture_evidence` | A hashed, redacted investigation bundle — scopes, surrounding events, effective configuration, optionally a screenshot |
| `quantick_search_capabilities` | Capabilities and scopes by substring or module, with availability |
| `quantick_invoke` | The long tail, under exactly the same authority checks as the named tools |

Grant the **annotator** profile and the agent also gets `quantick_annotate`,
`quantick_remove_annotation`, `quantick_notify`, `quantick_attach_script` and
`quantick_detach_script` — the half of the loop that answers on the chart.
The **cockpit** profile adds the canvas layout — panes, tabs, presets, focus
— and the ability to reconnect the market feed.

### The loop this is built for

Press the mark hotkey over a bar. Quantick resolves what is under the pointer
and appends it to the event journal. An agent parked in `wait_for_change`
returns with that mark, reads the window around that bar, and answers about
*that* bar — as a label pinned next to it, if you granted the annotate
tier. It is not screenshotting your screen and guessing.

### What keeps it safe

- **Local only.** An authenticated loopback socket, discovered through a
  private per-user descriptor the running instance publishes. Nothing listens
  on the network.
- **You choose the ceiling.** Three grantable profiles, each containing the
  one below: `observer` reads, `annotator` also answers on the chart, and
  `cockpit` also rearranges the canvas and may reconnect the feed. The
  contract declares a fourth, `trader`, over order placement — its
  permission is sensitive and denied by default, the access panel filters it
  out, and the MCP adapter never asks for it, so nothing reaches it today.
  It is written down now so that the day fills are not simulated, the
  boundary is not decided in a hurry.
- **Refused at the gate.** A capability you did not grant fails with
  `control.permission_denied`, whichever tool asked for it. `quantick_invoke`
  is checked exactly like a named tool.
- **Attributed and reversible.** Anything an agent draws is visibly marked as
  the agent's wherever you see it, and it can never remove something you drew
  by hand.
- **Written down.** The catalog records 34 capabilities across 20 modules,
  with 17 snapshot scopes and 27 selectable permissions — recount them in
  [`observer-capability-catalog-v1.json`](schemas/control/observer-capability-catalog-v1.json)
  rather than trusting this sentence. The wire schemas are generated from the
  Rust contracts and committed under
  [`schemas/control/`](schemas/control/), so a snapshot test rejects
  undeclared drift. The trust boundary has a
  [threat model](docs/control-plane/observer-threat-model.md); the transport
  has an [ADR](docs/control-plane/adr-0001-local-transport-and-instance-discovery.md).

Full reference: [`crates/mcp/README.md`](crates/mcp/README.md) for the tools,
[`docs/control-plane/`](docs/control-plane/) for the contract, and
[`AGENTS.md`](AGENTS.md) for the agent's-eye view of the whole repository.

## Candle appearance

Open **🎨 candle** from the chart toolbar to tune candle rendering without
changing bars, feeds or order-book capture. The default **Order flow** preset
uses a low-opacity body and a strong directional outline so liquidity and
aggression remain visible.

- Presets: **Order flow**, **Glass**, **Outline only** and **Classic**.
- Independent bull/bear colours for the body fill and outline.
- Body fill opacity, outline opacity/thickness, body width, corner radius and
  minimum doji height.
- Optional wicks with directional or custom colour, opacity and thickness.
- A forming-candle opacity control.
- **Outline only** removes the candle body fill entirely; this is the clearest
  mode for dense heatmaps.
- Canvas background and grid can be recoloured, faded or disabled independently.

The settings window includes a live preview. Candle paint is intentionally
layered after resting liquidity and before aggression bubbles:
`heatmap → candle → aggression`. Appearance changes only trigger a redraw and
never restart the market-data pipelines.

## Market Replay

Replay a recorded session and watch the chart build it print by print, at up to
50× speed. Open it from **File → Market Replay…** (`Ctrl+R`), pick the folder
holding your sessions, choose one and press **Play session**. A transport bar
appears at the bottom of the window while a recording plays — and only then:

```
⏮ ⏸  REPLAY  WINJ26 · 2026-03-16  13:27:48   1× 2× 3× 5× 10× 20× 50×   57 650 / 86 313 prints  ✖
▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●────────────
```

`Space` toggles play/pause. Dragging or clicking the track seeks; the chart is
rebuilt from the new position, because bars that already closed cannot be
reopened. Idle stretches longer than two seconds of market time are skipped —
lunch lulls and halts do not have to be watched in real time. Playback drives
the chart through the same feed channel a live venue uses, so bars, navigation
and metrics behave exactly as they do live, and nothing is ever labelled "live"
while a recording is playing.

Replay streams trades only. Depth is not in the file, so the L2 heatmap and
aggression bubbles are unavailable during a replay and disable themselves.

### Session file format

One folder per instrument, one CSV per session day:

```text
<replay folder>/
    WINJ26/
        20260316.csv
        20260317.csv
```

Files named `SYMBOL-YYYYMMDD.csv` directly in the folder are read too. Each file
holds one executed trade per line, oldest first, preceded by `#` metadata:

```text
# quantick-replay 1
# symbol=WINJ26
# timezone=-03:00
# side_source=bid_ask
Date,Time,Price,Bid,Ask,Volume,Side
2026-03-16,10:01:08.000,182035,182030,182035,12,B
2026-03-16,10:01:09.250,182025,182025,182030,4,S
```

- **Required columns:** `Date`, `Time`, `Price`, `Volume`, `Side`.
- **Optional columns:** `Bid`, `Ask`, `Id`. Any other column is ignored and
  reported, so a file carrying extra data still loads.
- Columns are matched **by name**, so their order is free.
- `Date` is `YYYY-MM-DD`; `Time` is `HH:MM:SS` or `HH:MM:SS.mmm`, in the
  timezone declared by `# timezone=` (UTC when the line is absent).
- `Side` is the **aggressor**: `B` when the buyer lifted the offer, `S` when the
  seller hit the bid. `A`/`ASK`/`BID` are rejected by name — those spellings mean
  opposite sides at different vendors, and guessing would mirror the order flow.

The layout follows what replay-capable platforms already do (an instrument/day
folder tree, as in NinjaTrader's `db/replay/`), with the row format every
tick-data vendor ships. A folder that does not load says exactly why, per file,
with the fix and the whole format one click away in the browser.

### Importing recordings

MT5 order-flow recordings (NDJSON with `tick` and `book_update` events) convert
to sessions with:

```bash
cargo run -p quantick-replay --example import_mt5_ndjson -- \
    --in runtime/mt5_orderflow_20260316.ndjson \
    --out /path/to/replay
```

| Option | Default | Behavior |
| --- | --- | --- |
| `--in <file>` | — | Recording to read; repeat for several |
| `--out <folder>` | — | Replay folder to write into |
| `--symbol <name>` | all | Keep only this instrument |
| `--side-source <policy>` | `bid_ask` | `bid_ask` (position against the recorded quote, tick rule as fallback), `flags` (the broker's BUY/SELL tick flags) or `tick_rule` |
| `--spread-within-second` | off | Even out prints inside each recorded second |
| `--timezone <offset>` | from the data | Offset the rows are written in |

The run reports how often each rule decided the aggressor side — including how
often it disagreed with the broker's flags — and the policy is written into the
session's `# side_source=` line. Recordings that stamp trades to the second are
labelled `# time_resolution=1s`; `--spread-within-second` distributes prints
evenly across each second for smoother playback and marks the session
`1s_interpolated`, because those sub-second times are inferred.

### Replay environment variables

| Variable | Default | Behavior |
| --- | --- | --- |
| `QUANTICK_REPLAY_DIR` | the folder you last chose, else `Documents/Quantick/replay` | Folder the browser opens on, **for this run only** — what you pick in the app is stored in the workspace and is not overwritten by a run under this variable |
| `QUANTICK_REPLAY_AUTOSTART` | unset | Set to `1` to load and play the first session in that folder on startup (same code path as clicking **Play session**) |
| `QUANTICK_REPLAY_SPEED` | `1` | Speed the autostarted session opens at |

## Optional L2 liquidity map

The chart can capture Binance Spot, Hyperliquid perpetual and MetaTrader DOM
depth and render a Bookmap-inspired liquidity map. Capture starts with any feed that can stream
depth; the map itself is **hidden by default** and shown from the chart
controls. The **⚙ L2** button docks a settings panel to
the left of the chart — the chart keeps the remaining width instead of being
covered — including a deterministic preview of every visual state, so themes
and grouping can be tuned without waiting for a rare live-book event.

The order flow splits into two independent layers, each with its own toolbar
switch and its own docked panel:

- **book heatmap** (**⚙ L2**) — resting liquidity and liquidity-response
  markers, built from the synchronized L2 depth pipeline.
- **bubbles** (**⚙ bubbles**) — confirmed aggressive executions, built from the
  aggregate-trade stream the chart already consumes.

Neither switch touches the other. Bubbles render with the map hidden (and for
providers without a depth pipeline at all), and hiding the book leaves the
bubbles running.

Both switches are display-only. Recording and drawing are separate concerns:
the depth recorder runs from the moment a depth-capable feed starts, so hiding
the map never punches a hole in the recorded book — reopen it and the whole
retained window is there, without the gap that stopping capture would leave.
While the map is hidden no projection is built and no depth geometry is drawn,
so the only cost it carries is the recording itself, bounded by the same
retention budget documented below. Capture stops only when the market changes:
a feed or symbol switch, or a replay taking the chart over.

The visualization follows a few data-honesty rules:

- History begins at the first successfully synchronized live snapshot/update sequence. Neither Binance nor Hyperliquid provides historical L2 backfill through these feeds, so candles before that point are marked as unavailable instead of being reconstructed. That stretch is marked by a single dashed line where the book begins, plus a label: it can span most of the chart, and tinting it would bury candles and bubbles that are perfectly real there.
- Depth update IDs are checked continuously. A disconnect, sequence gap or resynchronization closes the current liquidity runs, marks the affected interval with a faint fill between dashed vertical boundaries, and starts again from a fresh snapshot. Stale book state is never stretched across a gap. Interior gaps keep their fill precisely because they are narrow — an untinted sliver would read as "no resting liquidity" rather than "no data".
- Heatmap quantities are resting bid/ask amounts from the snapshot plus absolute depth updates, limited to the source's declared coverage. Hyperliquid publishes complete visible images of at most 20 levels per side; Binance's requested depth is configurable. Liquidity outside either coverage is unknown.
- A displayed band records the bucket total observed when its run opened; changes smaller than ~10% merge into the open run instead of cutting a new one. This churn-merge tolerance is a disclosed granularity choice — larger moves, appearances and full removals always cut a new run at their exact value.
- Trade bubbles are confirmed market aggression (`aggTrade` on Binance and venue-side `trades` on Hyperliquid). Their area is quantity-proportional and nearby prints can be clustered without changing total volume.
- A dark **bite** and impact ring mean an aggression and an L2 reduction were compatible in passive side, displayed price range, synchronized generation and time. This is an association, not a claim that one event caused the other.
- A violet dashed tail means displayed liquidity decreased without compatible aggression. It is deliberately called an **unattributed L2 reduction**, not a cancellation: a depth reduction can be an execution, cancellation, replacement or a combination of those events.
- Window clipping, retention boundaries, snapshots and synchronization gaps never create fake reduction markers.
- Captured history is bounded and kept in memory only. Restarting the application starts a new capture.

The chart exposes these settings:

| Setting | Default | Range / behavior |
| --- | ---: | --- |
| L2 heatmap | Hidden | Display-only; the recorder runs whenever the feed can stream depth, so reopening the map shows the whole retained window |
| Retention | 30 minutes | 1–1,440 minutes |
| Display range | Auto / 128 rows | Native, `2×`, `5×`, `10×`, `25×`, `50×`, custom multiple or adaptive-to-zoom; changing it reprojects immediately without resetting history |
| Base capture bucket | auto from price | Sized to ~`price / 65000` (1/2/5·10^k) on the first snapshot; any positive value can be set by hand. Changing the base resolution requires a fresh snapshot and resets retained L2 history |
| Theme | Bookmap | Bookmap, High contrast or Color blind |
| Brightness | `0.9` | `0.05`–`1.0` |
| Quiet liquidity curve | `1.8` | `0.25`–`2.0`; above one sinks quiet liquidity into the dark canvas so only real walls glow |
| Intensity scale | Visible P99 | Automatic visible-window P99 or a fixed full-intensity quantity |
| Aggression bubbles | Off | Own toolbar switch and own panel; records and projects without L2 depth capture |
| Bubble clustering | 200 ms | Raw, 50, 100, 200 or 500 ms |
| Bubble opacity | `0.78` | `0.05`–`1.0` |
| Largest bubble | `15 px` | `4`–`48 px`; area stays quantity-proportional |
| Liquidity response | On / 250 ms | Bite or withdrawal-tail markers with a configurable 25–1,000 ms evidence window |
| Legend | On | Explains liquidity brightness, buy/sell aggression, aligned depletion, unattributed reduction and L2 gaps |

The in-memory safety budgets are 500,000 liquidity runs (approximately 64 MiB), 100,000 aggression records, 12,000 projected visible cells/events and 700 projected bubbles. Old history is pruned and excess render primitives are dropped within those limits; the associated counters are emitted in diagnostic logs. All book state lives on a dedicated thread: the UI forwards depth events and latest-wins projection requests through a channel and only draws the newest published frame, so a dense-book projection can never block a frame. Projections rebuild at the ~220 ms depth cadence, are regrouped in a deterministic sweep and submitted in batched meshes. The paint order is `gap → heatmap → liquidity response → candle → aggression → legend`.

### L2 and logging environment variables

| Variable | Default | Behavior |
| --- | --- | --- |
| `QUANTICK_BOOK_DEPTH` | `1000` | Binance snapshot depth per side. Numeric values are clamped to `1`–`5000`; a missing or invalid value uses the default. Hyperliquid's public L2 coverage is fixed by the venue at up to 20 levels per side. |
| `QUANTICK_BOOK_AUTOSTART` | 
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `crates/pine/tests/corpus/err/stray_token.pine`
```python
// expect: PINE_SYNTAX@3
//@version=5
x = )
```

#### File: `crates/pine/tests/corpus/err/non_ascii.pine`
```python
// expect: PINE_LEX@3
//@version=5
plot(close × 2)
```

#### File: `crates/pine/tests/corpus/err/unterminated_string.pine`
```python
// expect: PINE_LEX@3
//@version=5
title = "never closed
```

#### File: `crates/pine/tests/corpus/ok/cvd.pine`
```python
//@version=5
indicator("CVD")
plot(cvd, color=color.aqua, title="cvd")
```

#### File: `crates/pine/tests/corpus/err/fill_non_plots.pine`
```python
// expect: PINE_UNSUPPORTED@5
//@version=5
x = close
y = open
fill(x, y)
```

#### File: `crates/pine/tests/corpus/err/bad_dedent.pine`
```python
// expect: PINE_INDENT@5
//@version=5
if close > open
        x = 1
    y = 2
```


==================================================
