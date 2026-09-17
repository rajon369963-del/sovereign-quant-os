# ⚡ [QUANT-SOURCE-239] Consolidated Quant & Algo Trading Repositories
**Category**: `PORTFOLIO_OPTIMIZATION_RISK` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_239_PORTFOLIO_OPTIMIZATION_RISK.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: poptimizer (`PHASE4-QUANT-099`)
- **Full Name**: `PHASE4-QUANT-099_WLM1ke__poptimizer`
- **Description**: Оптимизация долгосрочного портфеля акций
- **GitHub Stars**: 163
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# <picture><img src="docs/favicon.svg" height="32px"/></picture> Оптимизация долгосрочного портфеля акций

[![Test](https://github.com/WLM1ke/poptimizer/actions/workflows/test.yml/badge.svg)](https://github.com/WLM1ke/poptimizer/actions/workflows/test.yml)

## Описание

Целью проекта является автоматизация процесса управления портфелем акций.
Используемый подход не предполагает огромных доходностей, а нацелен
на получение результата чуть лучше рынка при рисках чуть меньше рынка
при относительно небольшом обороте. Портфель ценных бумаг должен быть
достаточно сбалансированным, чтобы его нестрашно было оставить без
наблюдения на продолжительное время

Большинство частных инвесторов стремиться к быстрому обогащению и,
согласно известному афоризму Баффета, \"мало кто хочет разбогатеть
медленно\", поэтому проект является открытым. Стараюсь по возможности
исправлять ошибки, выявленные другими пользователями, и буду рад разумным PR(-ам).
Особенно приветствуются вопросы и предложения по усовершенствованию содержательной части подхода к
управлению портфелем и UI/UX web-интерфейса

Проект находится в стадии развития и постоянно модифицируется (не всегда
удачно), поэтому может быть использован на свой страх и риск

## Установка

Установка описана для `MacOS`. Готов принять PR с описанием установки для `Linux` или `Windows`.
`POptimizer` представляет собой приложение на `Python`. Для его сборки и установки нужны базовые инструменты разработчика, которые требуется установить, если они не установлены ранее:

- пакетный менеджер [Homebrew](https://brew.sh)
- современный аналог `Make` [Task](https://taskfile.dev/installation/#homebrew)
- клонируйте `POptimizer`

```bash
git clone --filter=blob:none https://github.com/WLM1ke/poptimizer.git && cd poptimizer
```

- запустите команду установки необходимых инструментов и зависимостей

```bash
task install
```

## Обновление

Данная команда предназначена для неопытных пользователей, которые не меняют сами код программы:

- проверьте, что последняя версия проходит тесты (зеленый банер в начала этого файла)
- остановите программу `Ctrl-C`
- запустите команду обновления

```bash
task update_ver
```

- так же можно обновить данные о дивидендах по наиболее ликвидным акциям из актуальной версии (лучше вводить дивиденды самому, если в портфеле много малоликвидных позиций)

```bash
task task reset_div
```

## Откат обновления

При возникновении ошибок во время обновления можно откатить на предыдущую версию с помощью команды

```bash
task revert_ver
```

## Настройка

### Работа с секретами

Для работы `POptimizer` могут потребоваться секретные токены, которые необходимо внести в конфигурационный файл.
Чтобы не хранить секреты в открытом виде:

- сохраните их в хранилище секретных ключей операционной системы

```bash
uv run poptimizer keychain save YOUR_SECRET_KEY YOUR_SECRET_VALUE
```

- в конфигурационном файле вместо `YOUR_SECRET_VALUE` используйте специальную заглушку `keychain:YOUR_SECRET_KEY`, которая в момент загрузки будет заменять на `YOUR_SECRET_VALUE` из хранилища секретов операционной системы
- при необходимости можно удалить секрет из хранилища секретов

```bash
uv run poptimizer keychain delete YOUR_SECRET_KEY
```

- посмотреть текущее значение

```bash
uv run poptimizer keychain get YOUR_SECRET_KEY
```

- так же можно зайти в интерфейс хранилища напрямую - секреты сохраняются для приложения `poptimizer`

### Создание конфигурационного файла

Настройки приложения хранятся в `cfg/cfg.yaml` и носят опциональный характер - приложение будет работать без заполнения конфигурационного файла.
При первом запуске будет создан пустой конфигурационный файл, который можно заполнить по мере необходимости на основе шаблона `cfg/cfg.yaml.template`.
При необходимости можно создать `cfg/cfg.yaml` самому и выборочно заполнить нужные секции

### Настройка `Gmail`

`POptimizer` может отправлять оповещения об ошибках, ключевых событиях в работе, изменении стоимости портфеля и рекомендациях по его оптимизации на почтовый ящик `Gmail`.
Этот функционал опционален, а для его настройки:

- создайте [пароль](https://myaccount.google.com/apppasswords) для приложения
- сохраните пароль в хранилище секретов (смотри выше) 
- внесите почту и заглушку для пароля в конфиг

### Интеграция с `Tinkoff`

В программе реализовано автоматическое обновление позиций на счетах в `Tinkoff`, для этого:

- Создайте [Read-only token](https://developer.tbank.ru/invest/intro/intro/token#получить-токен)
- Выполните команду для получения id счетов

```bash
uv run poptimizer tinkoff YOUR_TOKEN
```

- сохраните токен в хранилище секретов (смотри выше) и внесите заглушку для него в конфиг. Название счета из конфигурационного файла используется для отображения в web-интерфейсе `POptimizer` и может состоять из любых английских букв и цифр. При необходимости могут быть внесены несколько счетов для одного токена или разные токены и счета для них
- после запуска программы будут созданы соответствующие счета внутри `POptimizer`, если они не созданы ранее. По ним подтянутся актуальные данные об открытых позициях и в последствии будут регулярно обновляться

При желании подобный функционал можно поддержать для других брокеров - готов принять ПРы и помочь с доработкой

## Использование

### Первый запуск и начало использования

- запустите `MongoDB`, которая указана в `cfg.yaml` или воспользуйтесь командой для локального запуска с настройками по умолчанию. Данную команду достаточно выполнить один раз. Она зарегистрирует сервис, которые будет запускать `MongoDB` при перезапуске системы

```bash
task mongo
```

- запустите программу

```bash
task run
```

- перейдите по адресу, указанному `cfg.yaml` файле или [http://localhost:5000](http://localhost:5000) по умолчанию
- создайте в настройках хотя бы один брокерский счет или дождитесь автоматического создания для счетов `Tinkoff`, если они были внесены в `cfg.yaml`
- заполните счета актуальной информацией по имеющимся акциям и денежным средствам
- опционально в настройках можно добавить тикеры в список исключений (например, недоступные у вашего брокера, по которым ожидается делистинг и т.д.)
- дождитесь первого ночного обновления данных (1:00 MSK). Программа удалит из списка доступных малоликвидные бумаги с короткой историей и нулевой позицией на всех счетах, а так же внесенные в список исключений
- следуйте рекомендациям в разделе `Optimization`

### Разделы `Portfolio` и `Accounts`

При первом запуске в портфеле будут доступны все акции и фонды торгуемые на `MOEX` с достаточной для построения моделей историей. В дальнейшем список доступных бумаг будет меняться на основании следующих факторов:

- включения и исключения ценных бумаг из перечня торгуемых на `MOEX`
- изменения требования к минимальной истории котировок для построения моделей
- изменения требования к минимальной ликвидности ценных бумаг в зависимости от размера портфеля - чем крупнее портфель, тем меньше бумаг будет доступно

Бумаги, которые не удовлетворяют одному из требований будут автоматически исключаться при ежедневном обновлении данных, если по ним отсутствует позиция на всех счетах

На уровне портфеля отслеживается информация о характерной частоте сделок, которая используется для построения моделей и учета издержек в предложениях по оптимизации - первоначально 1 день

Агрегированные данные по всем счетам выводятся на вкладке `Portfolio`, а данные по отдельным счетам с возможностью редактирования в разделах соответствующих счетов

### Раздел `Dividends`

При первоначальном запуске формируется база с дивидендами для наиболее ликвидных бумаг, которые реально торговать при портфеле от 200М.
Если у вас менее крупный портфель, необходимо заполнить информацию по остальным акциям. При дальнейшей работе будут поступать сообщения на почту `Gmail` о необходимости обновления дивидендов и появится возможность их редактирования разделе `Dividends`

### Разделы `Forecast` и `Optimization`

Используемые для построения прогнозов модели формируются автоматически с помощью эволюционного алгоритма:

- модели с большей доходностью и лучшими статистическими свойствами на тестовой выборке выживают и создают новые модели с похожими характеристиками
- модели с меньшей доходностью и худшими статистическими свойствами на тестовой выборке удаляются

В качестве тестовой выборки используются последние торговые дни, а их количество меняется в зависимости от рыночной конъюнктуры. В результате бумаги с короткой историей могут быть исключены из портфеля.
Для тренировки моделей используются все ценные бумаги из текущего портфеля, а прогноз строится на несколько дней вперед в соответствии с актуальной частотой сделок

Прогнозы по всем моделям агрегируюся и выводятся на вкладке `Forecast` в пересчете в годовое выражение, при этом используется портфельная теория для расчета риска и доходности портфеля на основе характеристик отдельных позиций

На вкладке `Optimization` выводятся рекомендации о покупке и продаже ценных бумаг. При этом учитывается разброс в прогнозах - нижняя граница доверительного интервала в предложениях на покупку должна быть больше верхней границы доверительного интервала предложений на продажу с учетом транзакционных издержек

В некоторых случаях может сложиться ситуация, когда предложений по оптимизации не будет:

- при малом количестве прогнозов или большом их расхождении - большая ширина доверительных интервалов
- большой частоте сделок - больших транзакционных издержках, которые учитываются при расчете доверительных интервалов
- близости портфеля к оптимальному - все малодоходные и рискованные бумаги проданы, а у остальных не достаточно сильно различаются прогнозные метрики, чтобы перекрыть транзакционные издержки

В этом случае будет выведена одна бумага с максимальной нижней границей доверительного интервала, которую следует покупать при наличии свободных денежных средств

Прогноз и предложение по оптимизации пересчитывается при появлении достаточно большого количества новых моделей и с некоторой задержкой при изменении портфеля. В интерфейсе будет отображаться надпись `outdated`, если расчеты пока не обновились после последнего изменения портфеля

## Используемые подходы

Оптимизация портфеля построена на базе [Modern portfolio theory](https://en.wikipedia.org/wiki/Modern_portfolio_theory) с учетом неточности имеющихся прогнозов вместо классической mean-variance оптимизации:

- При построении портфеля учитываются все акций и ETF, обращающихся на MOEX, с достаточной ликвидностью и длинной истории для построения прогнозов
- Для оценки корреляционных матриц для большого числа активов используется сжатие [Ledoit-Wolf](http://www.ledoit.net/honey.pdf)
- Для прогнозирования риска и доходности используются ансамбль нейронных сетей, который формируется с помощью эволюционного алгоритма

## Техническая информация

Frontend сделан на `htmx`, а Backend на `asyncio` `Python`, в том числе:

- HTTP клиент и сервер `aiohttp`
- хранение данных `async` `PyMongo`
- валидация и сериализация данных `Pydantic`
- обучения моделей `PyTorch`
- статистические тесты и оптимизация `SciPy`

Backend использует конечные, которые обмениваются событиями. Примерная схема изображена на диаграмме 

![Схема событий](docs/fsm.excalidraw.svg)

### Core Implementation Code & Architecture
#### File: `poptimizer/__init__.py`
```python

```

#### File: `poptimizer/forecast/__init__.py`
```python

```

#### File: `poptimizer/forecast/models/__init__.py`
```python

```

#### File: `poptimizer/clients/__init__.py`
```python

```

#### File: `poptimizer/core/__init__.py`
```python

```

#### File: `poptimizer/cli/__init__.py`
```python

```


==================================================


## [2/3] Repository: pyrb (`PHASE4-QUANT-100`)
- **Full Name**: `PHASE4-QUANT-100_jcrichard__pyrb`
- **Description**: Constrained and Unconstrained Risk Budgeting / Risk Parity Allocation in Python
- **GitHub Stars**: 131
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
Constrained and Unconstrained Risk Budgeting Allocation in Python
================

[![Actions Status](https://github.com/jcrichard/pyrb/workflows/Python%20application/badge.svg)](https://github.com/jcrichard/pyrb/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This repository contains the code for solving constrained risk budgeting
with generalized standard deviation-based risk measure:

<a href="https://www.codecogs.com/eqnedit.php?latex=R(x)&space;=&space;-&space;\pi^T&space;x&space;&plus;&space;c&space;\sqrt{&space;x^T&space;\Sigma&space;x}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?R(x)&space;=&space;-&space;\pi^T&space;x&space;&plus;&space;c&space;\sqrt{&space;x^T&space;\Sigma&space;x}" title="R(x) = - \pi^T x + c \sqrt{ x^T \Sigma x}" /></a>


This formulation encompasses Gaussian value-at-risk and Gaussian expected shortfall and the volatility. The algorithm supports bounds constraints and inequality constraints. It is is efficient for large dimension and suitable for backtesting. 

A description can be found in [*Constrained Risk Budgeting Portfolios: Theory, Algorithms, Applications & Puzzles*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3331184)
by Jean-Charles Richard and Thierry Roncalli.

You can solve
------------------

- Equally risk contribution
- Risk budgeting
- Risk parity with expected return
- Constrained Risk parity

Installation
------------------
 Can be done using ``pip``: 

    pip install git+https://github.com/jcrichard/pyrb


Usage
------------------

    from pyrb import EqualRiskContribution

    ERC = EqualRiskContribution(cov)
    ERC.solve()
    ERC.get_risk_contributions()
    ERC.get_volatility()


References
------------------

>Griveau-Billion, T., Richard, J-C., and Roncalli, T. (2013), A Fast Algorithm for Computing High-dimensional Risk Parity Portfolios, SSRN.

>Maillard, S., Roncalli, T. and
    Teiletche, J. (2010), The Properties of Equally Weighted Risk Contribution Portfolios,
    Journal of Portfolio Management, 36(4), pp. 60-70.
    
>Richard, J-C., and Roncalli, T. (2015), Smart
    Beta: Managing Diversification of Minimum Variance Portfolios, in Jurczenko, E. (Ed.),
    Risk-based and Factor Investing, ISTE Press -- Elsevier.
    
>Richard, J-C., and Roncalli, T. (2019), Constrained Risk Budgeting Portfolios: Theory, Algorithms, Applications & Puzzles, SSRN.
    
>Roncalli, T. (2015), Introducing Expected Returns into Risk Parity Portfolios: A New Framework for Asset Allocation,
    Bankers, Markets & Investors, 138, pp. 18-28.

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `pyrb/__init__.py`
```python
from .allocation import (
    EqualRiskContribution,
    RiskBudgeting,
    RiskBudgetAllocation,
    RiskBudgetingWithER,
    ConstrainedRiskBudgeting,
)
```

#### File: `pyrb/settings.py`
```python
# algorithm tolerance
CCD_COVERGENCE_TOL = 1e-10
BISECTION_TOL = 1e-5
ADMM_TOL = 1e-10
MAX_ITER = 5000
BISECTION_UPPER_BOUND = 10
MAXITER_BISECTION = 5000

# bounds
MIN_WEIGHT = 0
MAX_WEIGHT = 1e3
RISK_BUDGET_TOL = 0.00001
```

#### File: `setup.py`
```python
from setuptools import setup, find_packages

DISTNAME = "pyrb"
VERSION = "1.0.1"
DESCRIPTION = (
    """pyrb is a Python library to solve constrained risk budgeting problem."""
)
LONG_DESCRIPTION = (
    """pyrb is a Python library to solve constrained risk budgeting problem."""
)
AUTHOR = "Jean-Charles Richard"
AUTHOR_EMAIL = "jcharles.richard@gmail.com"
URL = "https://github.com/jcrichard/pyrb"
LICENSE = "Apache License, Version 2.0"

REQUIREMENTS = ["pandas>=0.19", "numba>=0.4", "quadprog>=0.1.0"]

if __name__ == "__main__":
    setup(
        name=DISTNAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        url=URL,
        license=LICENSE,
        packages=find_packages(),
        package_data={"docs": ["*"]},
        include_package_data=True,
        zip_safe=False,
        install_requires=REQUIREMENTS,
        classifiers=["Programming Language :: Python :: 3.4"],
    )
```

#### File: `pyrb/tools.py`
```python
import quadprog

import numpy as np


def to_column_matrix(x):
    """Return x as a matrix columns."""
    x = np.matrix(x)
    if x.shape[1] != 1:
        x = x.T
    if x.shape[1] == 1:
        return x
    else:
        raise ValueError("x is not a vector")


def to_array(x):
    """Turn a columns or row matrix to an array."""
    if x is None:
        return None
    elif (len(x.shape)) == 1:
        return x

    if x.shape[1] != 1:
        x = x.T
    return np.squeeze(np.asarray(x))


def quadprog_solve_qp(P, q, G=None, h=None, A=None, b=None, bounds=None):
    """Quadprog helper."""
    n = P.shape[0]
    if bounds is not None:
        I = np.eye(n)
        LB = -I
        UB = I
        if G is None:
            G = np.vstack([LB, UB])
            h = np.array(np.hstack([-to_array(bounds[:, 0]), to_array(bounds[:, 1])]))
        else:
            G = np.vstack([G, LB, UB])
            h = np.array(
                np.hstack([h, -to_array(bounds[:, 0]), to_array(bounds[:, 1])])
            )

    qp_a = q  # because  1/2 x^T G x - a^T x
    qp_G = P
    if A is not None:
        qp_C = -np.vstack([A, G]).T
        qp_b = -np.hstack([b, h])
        meq = A.shape[0]
    else:  # no equality constraints
        qp_C = -G.T
        qp_b = -h
        meq = 0
    return quadprog.solve_qp(qp_G, qp_a, qp_C, qp_b, meq)[0]


def proximal_polyhedra(y, C, d, bound, A=None, b=None):
    """Wrapper for projecting a vector on the constrained set."""
    n = len(y)
    return quadprog_solve_qp(
        np.eye(n), np.array(y), np.array(C), np.array(d), A=A, b=b, bounds=bound
    )
```

#### File: `tests/test_risk_budgeting.py`
```python
import numpy as np
from pyrb.allocation import (
    EqualRiskContribution,
    RiskBudgeting,
    ConstrainedRiskBudgeting,
)


CORRELATIONMATRIX = np.array(
    [
        [1, 0.1, 0.4, 0.5, 0.5],
        [0.1, 1, 0.7, 0.4, 0.4],
        [0.4, 0.7, 1, 0.8, 0.05],
        [0.5, 0.4, 0.8, 1, 0.1],
        [0.5, 0.4, 0.05, 0.1, 1],
    ]
)
vol = [0.15, 0.20, 0.25, 0.3, 0.1]
NUMBEROFASSET = len(vol)
COVARIANCEMATRIX = CORRELATIONMATRIX * np.outer(vol, vol)
RISKBUDGET = [0.2, 0.2, 0.3, 0.1, 0.2]
BOUNDS = np.array([[0.2, 0.3], [0.2, 0.3], [0.05, 0.15], [0.05, 0.15], [0.25, 0.35]])


def test_erc():
    ERC = EqualRiskContribution(COVARIANCEMATRIX)
    ERC.solve()
    np.testing.assert_almost_equal(np.sum(ERC.x), 1)
    np.testing.assert_almost_equal(
        np.dot(np.dot(ERC.x, COVARIANCEMATRIX), ERC.x) ** 0.5,
        ERC.get_risk_contributions(scale=False).sum(),
        decimal=10,
    )
    np.testing.assert_equal(
        abs(ERC.get_risk_contributions().mean() - 1.0 / NUMBEROFASSET) < 1e-5, True
    )


def test_rb():
    RB = RiskBudgeting(COVARIANCEMATRIX, RISKBUDGET)
    RB.solve()
    np.testing.assert_almost_equal(np.sum(RB.x), 1, decimal=5)
    np.testing.assert_almost_equal(
        np.dot(np.dot(RB.x, COVARIANCEMATRIX), RB.x) ** 0.5,
        RB.get_risk_contributions(scale=False).sum(),
        decimal=10,
    )
    np.testing.assert_equal(
        abs(RB.get_risk_contributions() - RISKBUDGET).sum() < 1e-5, True
    )


def test_cerb():
    CRB = ConstrainedRiskBudgeting(
        COVARIANCEMATRIX, budgets=None, pi=None, bounds=BOUNDS
    )
    CRB.solve()
    np.testing.assert_almost_equal(np.sum(CRB.x), 1)
    np.testing.assert_almost_equal(CRB.get_risk_contributions()[1], 0.2455, decimal=5)
    np.testing.assert_almost_equal(np.sum(CRB.x[1]), 0.2)
```


==================================================


## [3/3] Repository: Finance-World (`PHASE4-QUANT-113`)
- **Full Name**: `PHASE4-QUANT-113_coorung__Finance-World`
- **Description**: Optimization techniques on the financial area for the hedging, investment starategies, and risk measures
- **GitHub Stars**: 43
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Finance World
Optimization techniques on the financial area for the hedging, investment strategies, and risk measures.
Codes are categorized to Basic & Advanced, as the Financial engineering or Market microstructure concept are included or not. I am trying to visualize it to grasp well but recommend that check the reference paper before you give yourself over to code, especially in Advanced folder.

This repository will be added & fixed continuously

## Basic
### 1. Modern Portfolio Theory
![MPT](./Basic/fig/1_MPT.png)
### 2. Return Distribution Analysis with Risk Measure
![2. Return Distribution Analysis with Risk Measure](./Basic/fig/2_Distribution_Analysis.png)
### 3. Naive Classification Procedure for ML Trading
![3. Naive Classification Procedure for ML Trading](./Basic/fig/3_Classification.png)
### 4. ELS Pricing(Kor)
(The figure below is only intended to show the structure of the ELS. Code result is just a price of ELS)
![4. ELS Pricing](./Basic/fig/4_ELS.jpg)
### 5. Volatility Surface
![5. Volatility Surface](./Basic/fig/5_Volsurface.png)

## Advanced

### 1. Hedging Option with Replicating Portfolio(Kor)
![1. Hedging Option with Replicating Portfolio](./Advanced/fig/1_ReplicatingPF.gif)
### 2. Pension Planning using HJB eqn
![2. Pension Planning using HJB eqn](./Advanced/fig/2_PensionPlan1.png)
![2. Pension Planning using HJB eqn](./Advanced/fig/2_PensionPlan2.png)
### 3. Pension Planning with RL
![3. Pension Planning with RL](./Advanced/fig/3_PensionPlanRL.png)
### 4. High Frequency Trading with RL
![4. High Frequency Trading with RL](./Advanced/fig/4_HFT_RL.png)


(*cont'd*)

MIT License

Copyright (c) 2019 U. Jang


==================================================
