# ⚡ [QUANT-SOURCE-180] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_180_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Order-Flow-Imbalance-OFI-features (`WHEEL_Order-Flow-Imbalance-OFI-features`)
- **Full Name**: `Order-Flow-Imbalance-OFI-features`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
To run the full project, please cd into ofi_project and follow the instructions in README.

### Core Implementation Code & Architecture
#### File: `ofi_project/src/__init__.py`
```python

```

#### File: `ofi_project/src/features/__init__.py`
```python

```

#### File: `ofi_project/src/utils.py`
```python
from contextlib import contextmanager
import time
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    datefmt="%H:%M:%S",
)


@contextmanager
def timer(task: str):
    """Simple timing decorator."""
    start = time.perf_counter()
    logging.info(f"[{task}] started …")
    yield
    elapsed = time.perf_counter() - start
    logging.info(f"[{task}] finished in {elapsed:.2f}s")
```

#### File: `ofi_project/src/features/ofi_best.py`
```python
import pandas as pd
import numpy as np


def ofi_best(lob: pd.DataFrame) -> pd.Series:
    """
    Compute best-level Order Flow Imbalance (OFI) from the LOB data.

    Parameters
    ----------
    lob : pd.DataFrame
        Limit order book dataframe with bid_qty_1 and ask_qty_1 columns.

    Returns
    -------
    pd.Series
        Series containing best-level OFI indexed by timestamps.
    """
    bid = lob["bid_qty_1"]
    ask = lob["ask_qty_1"]
    ofi = bid.diff().fillna(0) - ask.diff().fillna(0)
    return ofi.astype(np.float32).rename("ofi_best")
```

#### File: `ofi_project/src/features/ofi_integrated.py`
```python
from __future__ import annotations
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def ofi_integrated(ofi_levels: pd.DataFrame) -> pd.Series:
    """
    Perform PCA integration of multi-level OFI into a single integrated OFI series.

    Parameters
    ----------
    ofi_levels : pd.DataFrame
        DataFrame containing multi-level OFI features (columns = OFI at each depth level).

    Returns
    -------
    tuple[pd.Series, PCA]
        First principal component as a Series (aligned by timestamp),
        and the fitted PCA object.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(ofi_levels.fillna(0).values)
    pca = PCA(n_components=1)
    pc1 = pca.fit_transform(X_scaled)
    return pd.Series(pc1[:, 0], index=ofi_levels.index, name="ofi_integrated"), pca
```

#### File: `ofi_project/src/features/ofi_multi.py`
```python
from __future__ import annotations
import pandas as pd
import numpy as np


def ofi_multi(
    lob: pd.DataFrame,
    k: int = 10,
    decay: float = 5.0,
) -> pd.DataFrame:
    """
    Compute multi-level OFI for k depth levels, applying exponential decay weighting.

    Parameters
    ----------
    lob : pd.DataFrame
        Limit order book dataframe with bid_qty_i and ask_qty_i for i=1 to k.
    k : int, optional
        Number of depth levels to compute OFI for (default is 10).
    decay : float, optional
        Decay factor controlling how fast the weight decreases with level depth.

    Returns
    -------
    pd.DataFrame
        DataFrame with k columns ('ofi_multi_1', ..., 'ofi_multi_k') containing
        weighted OFI values for each depth level.
    """
    weights = np.exp(-np.arange(1, k + 1) / decay)

    bids = lob[[f"bid_qty_{i}" for i in range(1, k + 1)]].diff().fillna(0).values
    asks = lob[[f"ask_qty_{i}" for i in range(1, k + 1)]].diff().fillna(0).values
    diff = bids - asks  # shape (T, k)

    data = {}
    for i in range(k):
        data[f"ofi_multi_{i+1}"] = diff[:, i] * weights[i]

    return pd.DataFrame(data, index=lob.index)
```


==================================================


## [2/3] Repository: Order-Flow-Imbalance-analysis (`WHEEL_Order-Flow-Imbalance-analysis`)
- **Full Name**: `Order-Flow-Imbalance-analysis`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# OFI Factor Research Project

这是一个专注于研究**订单流失衡（Order Flow Imbalance, OFI）**因子的独立项目。

## 🎉 项目状态：Phase 4 已完成

**最新更新**: 2025-11-19
**当前阶段**: Phase 4 - 交易路径分析 ✅

### Phase 3 核心发现（单因子诊断）
- ✅ 6个品种（BTCUSD, ETHUSD, EURUSD, USDJPY, XAGUSD, XAUUSD）
- ✅ 8个时间周期（5min, 15min, 30min, 1H, 2H, 4H, 8H, 1D）
- ✅ 48个合并文件，9,247,557行数据

**Phase 3 Top 3**:
- 🥇 **ETHUSD 1D**: Q5-Q1收益差 4.09%, Sharpe 1.89
- 🥈 **BTCUSD 8H**: Q5-Q1收益差 0.80%, Sharpe 2.32
- 🥉 **ETHUSD 8H**: Q5-Q1收益差 1.09%, Sharpe 1.15

详见 [FINAL_ANALYSIS_COMPLETE.md](FINAL_ANALYSIS_COMPLETE.md)

### Phase 4 核心发现（交易路径分析）
- ✅ 4个品种（BTCUSD, ETHUSD, XAUUSD, XAGUSD）- 仅加密货币和贵金属
- ✅ 32个配置，311,720笔交易
- ✅ 完整交易路径统计（MFE, MAE, t_MFE, 出场原因等）

**Phase 4 Top 3**:
- 🥇 **BTCUSD 8H**: 期望值R 1.503, Sharpe 0.142, MFE_R 4.103
- 🥈 **BTCUSD 4H**: 期望值R 1.273, Sharpe 0.132, MFE_R 3.307
- 🥉 **ETHUSD 1D**: 期望值R 1.208, Sharpe 0.136, MFE_R 3.493

详见 [PHASE4_FINAL_RESULTS.md](PHASE4_FINAL_RESULTS.md)

## 项目概述

本项目从原始tick数据出发，构建OFI因子并进行单因子分析。项目设计模块化、可扩展，便于后续添加其他因子、交易路径分析或实盘交易集成。

## 研究阶段

### ✅ Phase 0 – 理论基础与项目框架（已完成）
- ✅ 文档化OFI因子的理论动机
- ✅ 定义研究假设
- ✅ 创建项目骨架

### ✅ Phase 1 – 数据加载与K线聚合（已完成）
- ✅ 从tick数据加载和清洗
- ✅ 支持Parquet格式（Hive分区）
- ✅ 支持多种时间周期（5min-1D）
- ✅ 支持bid/ask和单一价格两种tick格式

### ✅ Phase 2 – OFI因子构建（已完成）
- ✅ 使用tick规则标记买卖方向
- ✅ 计算原始OFI（OFI_raw）
- ✅ 计算标准化OFI（OFI_z）
- ✅ 批处理大规模数据

### ✅ Phase 3 – OFI单因子诊断（已完成）
- ✅ OFI分布和统计特性检查
- ✅ 条件未来收益分析
- ✅ 分位数分析（Q1-Q5）
- ✅ 相关性分析
- ✅ Sharpe比率计算

### ✅ Phase 4 – 交易路径分析（已完成 2025-11-19）
- ✅ 基于OFI_z的信号生成（趋势/反转模式）
- ✅ 交易路径模拟（MFE, MAE, t_MFE跟踪）
- ✅ 动态出场规则（从峰值回撤止损）
- ✅ R倍数统计（期望值、Sharpe、胜率）
- ✅ 32个配置完整分析（311,720笔交易）
- ✅ 跨资产汇总和排名

**关键成果**:
- BTCUSD 8H: 期望值R 1.503（最高）
- BTCUSD 4H: 期望值R 1.273
- ETHUSD 1D: 期望值R 1.208
- 详细交易路径特征分析
- 止盈/止损策略设计依据

详见 [PHASE4_FINAL_RESULTS.md](PHASE4_FINAL_RESULTS.md) 和 [PHASE4_QUICKSTART.md](PHASE4_QUICKSTART.md)

## 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 配置

编辑 `config/settings.yaml` 设置：
- 交易品种列表
- 数据路径
- K线周期
- 分析参数

### 3. 准备数据

**推荐格式：Parquet（Hive分区）**

```
data/ticks/
├── symbol=BTCUSD/
│   ├── date=2017-05-07/
│   │   └── part-0.parquet
│   ├── date=2017-05-08/
│   │   └── part-0.parquet
│   └── ...
├── symbol=ETHUSD/
│   └── ...
```

**Parquet文件字段**：
- `timestamp` (datetime64)
- `bid` (float64)
- `ask` (float64)
- `bid_vol` (float64)
- `ask_vol` (float64)

**传统CSV格式也支持**：

选项A（bid/ask格式）：
```
timestamp,bid,ask,volume
2024-01-01 00:00:00,42000.5,42001.0,1.5
```

选项B（单一价格格式）：
```
timestamp,price,volume
2024-01-01 00:00:00,42000.75,1.5
```

### 4. 运行分析

**单品种分析**：
```bash
# 构建K线 + OFI因子
python scripts/build_bars_with_ofi.py

# 运行单因子分析
python scripts/run_ofi_single_factor.py
```

**批量分析（推荐）**：
```bash
# 单品种批处理（适合大数据）
python run_single_symbol_batch.py

# 所有品种顺序处理
python run_all_symbols_sequential.py

# 分析结果汇总
python analyze_ofi_results.py
```

## 输出结果

### 数据输出

**批次文件**：
- `results/{SYMBOL}_{TIMEFRAME}_{BATCH}_bars_with_ofi.csv`

**合并文件**（推荐使用）：
- `results/{SYMBOL}_{TIMEFRAME}_merged_bars_with_ofi.csv`

**字段说明**：
- `open`, `high`, `low`, `close` - OHLC价格
- `volume` - 成交量
- `OFI` - 原始订单流失衡
- `OFI_z` - 标准化OFI（滚动窗口200）
- `fut_ret_2`, `fut_ret_5`, `fut_ret_10` - 未来2/5/10期收益率

### 分析报告

**完整分析**：
- `results/analysis_summary.csv` - 所有品种和周期的统计汇总

**单品种报告**：
- `results/sanity/ofi_R0_sanity_{symbol}.md` - OFI因子健全性检查
- `results/single_factor/ofi_R1_single_factor_{symbol}.csv` - 条件收益分析
- `results/single_factor/ofi_R1_bins_{symbol}.csv` - 分位数分析

## 项目结构

```
ofi_factor_project/
├── config/              # 配置文件
├── data/                # 数据目录
│   ├── ticks/          # 原始tick数据（用户提供）
│   └── bars/           # K线数据输出
├── results/            # 分析结果
│   ├── sanity/         # 健全性检查
│   └── single_factor/  # 单因子分析
├── docs/               # 文档
├── src/                # 源代码
│   ├── config_loader.py
│   ├── data/           # 数据处理模块
│   ├── factors/        # 因子计算模块
│   ├── research/       # 研究分析模块
│   └── utils/          # 工具函数
└── scripts/            # 可执行脚本
```

## 扩展性

项目设计支持未来扩展：
- 添加更多因子（如ManipScore）并在K线级别合并
- 添加交易路径和退出规则分析
- 集成简单回测框架
- 连接实盘交易系统

## 技术栈

- Python 3.10+
- pandas - 数据处理
- numpy - 数值计算
- matplotlib - 可视化
- pyyaml - 配置管理

## 核心发现

### Top 3 最佳配置

1. **ETHUSD + 1D（日线）** ⭐⭐⭐⭐⭐
   - Q5-Q1收益差: 4.09%
   - OFI相关性: 0.0804
   - Sharpe比率: 1.89
   - 推荐策略: 做多Q5组，做空Q1组，持仓10天

2. **BTCUSD + 8H** ⭐⭐⭐⭐⭐
   - Q5-Q1收益差: 0.80%
   - OFI相关性: 0.0417
   - Sharpe比率: 2.32（最高！）
   - 推荐策略: 做多Q5组，做空Q1组，持仓80小时

3. **ETHUSD + 8H** ⭐⭐⭐⭐
   - Q5-Q1收益差: 1.09%
   - OFI相关性: 0.0360
   - Sharpe比率: 1.15

### 关键洞察

- ✅ **加密货币**（BTCUSD, ETHUSD）OFI因子效果显著
- ✅ **中长周期**（4H-1D）表现最佳
- ⚠️ **外汇品种**（EURUSD, USDJPY）OFI因子效果很弱
- ❌ **短周期**（5min）噪音太大，不推荐

## 文档

详细文档请参阅：
- `FINAL_ANALYSIS_COMPLETE.md` - 最终完成报告（推荐阅读）
- `analysis_summary_complete.csv` - 完整统计数据
- `docs/OFI_DESIGN_NOTES.md` - OFI因子设计说明
- `docs/PHASE0_3_PROGRESS_LOG.md` - 开发进度日志
- `使用Parquet数据指南.md` - Parquet数据使用说明
- `批量分析使用指南.md` - 批量分析指南

### Core Implementation Code & Architecture
#### File: `src/utils/__init__.py`
```python
"""Utility modules."""
```

#### File: `src/factors/__init__.py`
```python
"""Factor calculation modules."""
```

#### File: `src/research/__init__.py`
```python
"""Research and analysis modules."""
```

#### File: `src/data/__init__.py`
```python
"""Data processing modules for OFI factor research."""
```

#### File: `src/__init__.py`
```python
"""OFI Factor Research Project - Core Package"""

__version__ = "0.1.0"
```

#### File: `src/trading/__init__.py`
```python
"""
Trading module for OFI-based signal generation and trade path simulation.
"""

from .ofi_signals import generate_ofi_signals
from .trade_path_simulator import simulate_trade_paths

__all__ = [
    'generate_ofi_signals',
    'simulate_trade_paths',
]
```


==================================================


## [3/3] Repository: Order-Flow-Imbalances (`WHEEL_Order-Flow-Imbalances`)
- **Full Name**: `Order-Flow-Imbalances`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Order-Flow-Imbalances
OFI construction

### Core Implementation Code & Architecture
#### File: `ofi.py`
```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

h = pd.Timedelta(seconds=20) #Set 20 seconds as the given time interval. This can be set to any value, and will have no effect on the time complexity

m = 10 #count of levels
bid_px = [0] * m
ask_px = [0] * m
bid_sz = [0] * m
ask_sz = [0] * m
bid_order_flow, ask_order_flow = None, None
pre_bof, pre_aof = None, None #prefix sums of bid and ask order flows
n = 0 #count of the number of rows
pre_bid_sz, pre_ask_sz = None, None

def load_data(filepath):
    return pd.read_csv(filepath)

def compute_order_flows(df):
    global n, bid_order_flow, ask_order_flow, pre_bof, pre_aof, pre_bid_sz, pre_ask_sz
    '''Precomputes all order flows'''
    for i in range(m):
        bid_px[i] = df['bid_px_' + f"{i:02}"]
        ask_px[i] = df['ask_px_' + f"{i:02}"]
        bid_sz[i] = df['bid_sz_' + f"{i:02}"]
        ask_sz[i] = df['ask_sz_' + f"{i:02}"]
    n = len(bid_px[0])
    bid_order_flow, ask_order_flow = [[0] * n] * m, [[0] * n] * m
    pre_bof, pre_aof = [[0] * n] * m, [[0] * n] * m
    pre_bid_sz, pre_ask_sz = [[0] * (n+1)] * m,  [[0] * (n+1)] * m
    for i in range(m):
        for j in range(1, n):
            if bid_px[i][j] == bid_px[i][j-1]:
                bid_order_flow[i][j] = bid_sz[i][j] - bid_sz[i][j-1]
            elif bid_px[i][j] > bid_px[i][j-1]:
                bid_order_flow[i][j] = bid_sz[i][j]
            else:
                bid_order_flow[i][j] = -bid_sz[i][j]
            pre_bof[i][j] = pre_bof[i][j-1] + bid_order_flow[i][j]

            if ask_px[i][j] == ask_px[i][j-1]:
                ask_order_flow[i][j] = ask_sz[i][j] - ask_sz[i][j-1]
            elif ask_px[i][j] > ask_px[i][j-1]:
                ask_order_flow[i][j] = -ask_sz[i][j]
            else:
                ask_order_flow[i][j] = ask_sz[i][j]

            pre_aof[i][j] = pre_aof[i][j-1] + ask_order_flow[i][j]

            pre_bid_sz[i][j] = pre_bid_sz[i][j-1] + bid_sz[i][j-1]
            pre_ask_sz[i][j] = pre_ask_sz[i][j-1] + ask_sz[i][j-1]

def compute_best_level_ofi(df, h):
    '''Computes ofi of the best level of i for each interval, and adds/updates it to df, using h as the time interval'''

    df['ofi_best_level'] = df['symbol']
    df.at[0, 'ofi_best_level'] = None
    prev = 0
    for i in range(1, n):
        cur_time = pd.Timestamp(df['ts_event'][i], tz='UTC')
        while cur_time > h+pd.Timestamp(df['ts_event'][prev+1], tz='UTC'):
            prev += 1
        cur_best_level_ofi = pre_bof[0][i] - pre_bof[0][prev] - pre_aof[0][i] + pre_aof[0][prev]
        df.at[i, 'ofi_best_level'] = cur_best_level_ofi
    return df

def compute_deep_level_ofi(df, h):
    '''Computes ofi of using multiple levels of i for each interval, and adds/updates it to df, using h as the time interval'''
    prev = 0
    avg_order_book_depth = [0] * n
    for i in range(1, n):
        cur_time = pd.Timestamp(df['ts_event'][i], tz='UTC')
        while cur_time > h+pd.Timestamp(df['ts_event'][prev+1], tz='UTC'):
            prev += 1
        div = i - prev
        if cur_time <= h+pd.Timestamp(df['ts_event'][prev], tz='UTC'):
            div += 1
        div *= 2
        for j in range(0, m):
            num = pre_bid_sz[j][i+1] - pre_bid_sz[j][prev+1] + pre_ask_sz[j][i+1] - pre_ask_sz[j][prev+1]
            avg_order_book_depth[i] += num
        avg_order_book_depth[i] /= m * div
    cur = 'multi_level_ofi'
    df[cur] = df['symbol']
    df.at[0, cur] = None
    prev = 0
    for i in range(1, n):
        cur_time = pd.Timestamp(df['ts_event'][i], tz='UTC')
        while cur_time > h+pd.Timestamp(df['ts_event'][prev+1], tz='UTC'):
            prev += 1
        cur_ofi = pre_bof[0][i] - pre_bof[0][prev] - pre_aof[0][i] + pre_aof[0][prev]
        df.at[i, cur] = cur_ofi / avg_order_book_depth[i]
    return df

def compute_integrated_ofi(df, h):
    '''Computes integrated ofi and adds/updates it to df, using h as the time interval. Assumes deep ofi is in df'''
    features = []
    for i in range(10):
        features += [
            f'bid_px_0{i}', f'ask_px_0{i}',
            f'bid_sz_0{i}', f'ask_sz_0{i}',
            f'bid_ct_0{i}', f'ask_ct_0{i}'
        ]
    X = df[features].dropna()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=1)
    pca.fit(X_scaled)
    first_principal_vector = pca.components_[0]
    norm = 0
    for x in first_principal_vector:
        norm += abs(x)
    df['integrated_ofi'] = df['symbol']
    df.at[0, 'integrated_ofi'] = None
    for i in range(1, n):
        integrated_ofi = 0
        for j in range(m):
            integrated_ofi = first_principal_vector[j] * df.at[i, 'multi_level_ofi']
        df.at[i, 'integrated_ofi'] = integrated_ofi / norm
    return df

def save_results(df, output_filepath):
    df.to_csv(output_filepath, index=False)

if __name__ == "__main__":
    df = load_data('first_25000_rows.csv')
    compute_order_flows(df)
    df = compute_best_level_ofi(df, h) #adds best level ofi
    df = compute_deep_level_ofi(df, h) #adds multi level ofi
    df = compute_integrated_ofi(df, h) #adds integrated ofi
    save_results(df, 'first_25000_rows_with_ofi.csv')
```


==================================================
