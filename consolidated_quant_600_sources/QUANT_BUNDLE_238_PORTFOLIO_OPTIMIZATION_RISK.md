# ⚡ [QUANT-SOURCE-238] Consolidated Quant & Algo Trading Repositories
**Category**: `PORTFOLIO_OPTIMIZATION_RISK` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_238_PORTFOLIO_OPTIMIZATION_RISK.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: riskparity.py (`PHASE4-QUANT-095`)
- **Full Name**: `PHASE4-QUANT-095_convexfi__riskparity.py`
- **Description**: Fast and scalable construction of risk parity portfolios
- **GitHub Stars**: 325
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# riskparity.py

[![PyPI version](https://badge.fury.io/py/riskparityportfolio.svg)](https://badge.fury.io/py/riskparityportfolio)
[![Downloads](https://pepy.tech/badge/riskparityportfolio)](https://pepy.tech/project/riskparityportfolio)
[![codecov](https://codecov.io/gh/mirca/riskparity.py/branch/master/graph/badge.svg)](https://codecov.io/gh/mirca/riskparity.py)


**riskparityportfolio** provides solvers to design risk parity portfolios.
In its simplest form, we consider the convex formulation with a unique solution proposed by
[Spinu (2013)](https://dx.doi.org/10.2139/ssrn.2297383) and use cyclical methods inspired by
[Griveau-Billion et al. (2013)](https://arxiv.org/pdf/1311.4057.pdf)
and [Choi & Chen (2022)](https://www.emerald.com/insight/content/doi/10.1108/JDQS-12-2021-0031/full/pdf). For more general formulations,
which are usually nonconvex, we implement the successive convex approximation
method proposed by [Feng & Palomar (2015)](https://doi.org/10.1109/TSP.2015.2452219).

**Documentation:** [**https://mirca.github.io/riskparity.py**](https://mirca.github.io/riskparity.py)

**R version:** [**https://mirca.github.io/riskParityPortfolio**](https://mirca.github.io/riskParityPortfolio)

**Rust version:** [**https://github.com/mirca/riskparity.rs**](https://github.com/mirca/riskparity.rs)

**Talks**: [**slides HKML meetup 2020**](https://speakerdeck.com/mirca/breaking-down-risk-parity-portfolios-a-practical-open-source-implementation),
[**tutorial - Data-driven Portfolio Optimization Course (HKUST)**](https://www.youtube.com/watch?v=xb1Xxf5LQks)

## Installation

* **development version**

```
$ git clone https://github.com/dppalomar/riskparity.py.git
$ cd riskparity.py
$ pip install -e .
```

* **stable version**

```
$ pip install riskparityportfolio
```

### Windows requirements

Make sure to install [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
prior to ``riskparityportfolio``.

``riskparityportfolio`` depends on ``jaxlib`` which can be installed following these
[instructions](https://github.com/cloudhan/jax-windows-builder).


## References

* Spinu, Florin. An Algorithm for Computing Risk Parity Weights (July 30, 2013). Available at SSRN: [https://ssrn.com/abstract=2297383](https://ssrn.com/abstract=2297383).

* Griveau-Billion, Théophile et al. A Fast Algorithm for Computing High-dimensional Risk Parity Portfolios. [https://arxiv.org/abs/1311.4057](https://arxiv.org/abs/1311.4057)

* Feng, Yiyong et al. SCRIP: Successive Convex Optimization Methods for Risk Parity Portfolio Design.
IEEE Transactions on Signal Processing, 2015. [https://ieeexplore.ieee.org/document/7145485](https://ieeexplore.ieee.org/document/7145485)

* Choi, J., & Chen, R. (2022). Improved iterative methods for solving risk parity portfolio. Journal of Derivatives and Quantitative Studies 30(2), 114–124. [https://doi.org/10.1108/JDQS-12-2021-0031](https://doi.org/10.1108/JDQS-12-2021-0031)


## License

Copyright 2022 [Ze Vinicius](https://mirca.github.io) and [Daniel Palomar](https://www.danielppalomar.com)

This project is licensed under the terms of the MIT License.

## Disclaimer

The information, software, and any additional resources contained in this repository are not intended as,
and shall not be understood or construed as, financial advice. Past performance is not a reliable indicator
of future results and investors may not recover the full amount invested.
The [authors](https://github.com/dppalomar/riskParityPortfolio/blob/master/AUTHORS.md) of this repository
accept no liability whatsoever for any loss or damage you may incur.  Any opinions expressed in this repository
are from the personal research and experience of the
[authors](https://github.com/dppalomar/riskParityPortfolio/blob/master/AUTHORS.md) and are intended as
educational material.

### Core Implementation Code & Architecture
#### File: `src/riskparityportfolio/tests/__init__.py`
```python

```

#### File: `third-party/eigen_3.3.7/debug/gdb/__init__.py`
```python
# Intentionally empty
```

#### File: `src/riskparityportfolio/version.py`
```python
__version__ = "0.5.1"
```

#### File: `third-party/eigen_3.3.7/doc/snippets/MatrixBase_random_int.cpp`
```python
cout << VectorXi::Random(2) << endl;
```

#### File: `third-party/eigen_3.3.7/doc/snippets/MatrixBase_zero_int_int.cpp`
```python
cout << MatrixXi::Zero(2,3) << endl;
```

#### File: `third-party/eigen_3.3.7/doc/snippets/MatrixBase_ones_int_int.cpp`
```python
cout << MatrixXi::Ones(2,3) << endl;
```


==================================================


## [2/3] Repository: simulated-bifurcation-algorithm (`PHASE4-QUANT-097`)
- **Full Name**: `PHASE4-QUANT-097_bqth29__simulated-bifurcation-algorithm`
- **Description**: Python CPU/GPU implementation of the Simulated Bifurcation (SB) algorithm to solve quadratic optimization problems (QUBO, Ising, TSP, optimal asset allocations for a portfolio, etc.).
- **GitHub Stars**: 168
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Simulated Bifurcation for Python

[![PyTorch](https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?logo=PyTorch&logoColor=white)](https://pytorch.org/)
[![PyPI package](https://badge.fury.io/py/simulated-bifurcation.svg)](https://pypi.org/project/simulated-bifurcation/)
[![codecov](https://codecov.io/gh/bqth29/simulated-bifurcation-algorithm/branch/main/graph/badge.svg?token=J76VVHPGVS)](https://codecov.io/gh/bqth29/simulated-bifurcation-algorithm)
![Status](https://github.com/bqth29/simulated-bifurcation-algorithm/actions/workflows/test.yml/badge.svg)
[![Documentation Status](https://readthedocs.org/projects/simulated-bifurcation-algorithm/badge/?version=latest)](https://simulated-bifurcation-algorithm.readthedocs.io/en/latest/?badge=latest)
![GitHub stars](https://img.shields.io/github/stars/bqth29/simulated-bifurcation-algorithm.svg?style=social&label=Star)

The **Simulated Bifurcation** (SB) algorithm is a fast and highly parallelizable state-of-the-art algorithm for quadratic combinatorial optimization inspired by quantum physics and spins dynamics. It relies on Hamiltonian quantum mechanics to find local minima of **Ising** problems. The last accuracy tests showed a median optimality gap of less than 1% on high-dimensional instances.

This open-source package utilizes **PyTorch** to leverage GPU computations, harnessing the high potential for parallelization offered by the SB algorithm.

It also provides an API to define Ising models or other NP-hard and NP-complete problems (QUBO, Karp problems, ...) that can be solved using the SB algorithm.

## ⚙️ Install

<table>
<thead>
<tr>
<th>Compute Plateform</th>
<th>CPU</th>
<th>GPU</th>
</tr>
</thead>
<tbody>
<tr>
<th>Instructions</th>
<td>

```console
pip install simulated-bifurcation     
```

</td>
<td>

&nbsp;&nbsp;&nbsp;
Install [PyTorch](https://pytorch.org/get-started/locally/) with GPU support

```console
pip install simulated-bifurcation     
```

</td>
</tr>
</tbody>
</table>

> To use the latest package version matching the GitHub main branch status, use:
> ```
> pip install git+https://github.com/bqth29/simulated-bifurcation-algorithm.git
> ```

## 💡 Online documentation

The documentation of the package is available on [ReadTheDocs](https://simulated-bifurcation-algorithm.readthedocs.io/en/latest/?badge=latest).

## 🧪 The _Simulated Bifurcation_ (SB) algorithm

### Ising model

An Ising problem, given a null-diagonal square symmetrical matrix $J$ of size $N \times N$ and a vector $h$ of size $N$, consists in finding the spin vector $\mathbf{s} = (s_{1}, ... s_{N})$ called the _ground state_, (each $s_{i}$ being equal to either 1 or -1) such that the following value, called _Ising energy_, is minimal:

$$- \frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} J_{ij}s_{i}s_{j} + \sum_{i=1}^{N} h_{i}s_{i}$$

This problem is known to be NP-hard but is very useful since it can be used in many sectors such as finance, transportation or chemistry or derived as other well-know optimization problems (QUBO, MAXCUT, Knapsack problem, etc.).

The Simulated Bifurcation algorithm was originally introduced to solve Ising problems by simulating the adiabatic evolution of spins in a quantum Hamiltonian system, but can also be generalized to a wider range of optimization problems.

### Usage on polynomial instances

The SB algorithm can be used more broadly to minimize or maximize quadratic models which are multivariable polynomials of degree two, i.e. written as

$$\sum_{i=1}^{N} \sum_{j=1}^{N} M_{ij}x_{i}x_{j} + \sum_{i=1}^{N} v_{i}x_{i} + c$$

for which the $x_{i}$'s can be spins, binary or non-negative integer.

This can also be seen as the sum of a quadratic form, a linear form and a constant term (offset) and such a formulation is the basis of many optimization problems.

> Any quadratic model written as above can easily be converted in an equivalent Ising model, thus allowing the use of the SB algorithm for minimizing said quadratic model on a given optimization domain.

The `minimize` and `maximize` functions allow to respectively minimize and maximize the value of such quadratic models on a given optimization domain, relying on the SB algorithm. They both return the optimal polynomial value found by the SB algorithm, along with its associated input vector.

> The optimization domain is not necessarily the same for all the variables of the quadratic model.

The input types must be passed to the `domain` argument:

- `spin` (default value) for a spin optimization: the optimal vector will only have ±1 values
- `binary` for a binary optimization: the optimal vector will only have 0 or 1 values
- `intX` for a `X`-bits encoded integer optimization: the optimal vector will only have integer value encoded with `X` bits or less, i.e. belonging to the range 0 to $2^{X} - 1$.

> For instance, 9-bits integer correspond to the `int9` input type and the accepted values span from 0 to 511.

```python
import simulated_bifurcation as sb
```

```python
matrix = torch.tensor([[1, 1, 2], [0, -1, -2], [-2, 0, 2]])
vector = torch.tensor([-1, 0, 2])
constant = 2.0
```

The package provides a `polynomial` API to build quadratic multivariate polynomials from such tensors. Four options are possible.

A polynomial can be defined using coefficient tensors or SymPy expressions to define polynomials in a more natural way from mathematical equations.

> The four following code snippets all create equivalent polynomials

1. Using the `QuadraticPolynomial` class

```python
from simulated_bifurcation.core import QuadraticPolynomial
```

**With tensors**

```python
polynomial = QuadraticPolynomial(matrix, vector, constant)
```

**With a SymPy expression**

```python
from sympy import poly, symbols
x, y, z = symbols("x y z")
expression = poly(
    x**2 - y**2 + 2 * z**2
    + x * y + 2 * x * z
    - 2 * y * z
    - 2 * z * x
    - x + 2 * z
    + 2
)

polynomial = QuadraticPolynomial(expression)
```

2. Using the `sb.build_model` function

**With tensors**

```python
polynomial = sb.build_model(matrix, vector, constant)
```

**With a SymPy expression**

```python
from sympy import poly, symbols
x, y, z = symbols("x y z")
expression = poly(
    x**2 - y**2 + 2 * z**2
    + x * y + 2 * x * z
    - 2 * y * z
    - 2 * z * x
    - x + 2 * z
    + 2
)

polynomial = sb.build_model(expression)
```

The `minimize` and `maximize` functions allow to respectively minimize and maximize the value of such polynomials for a given type of input values, relying on the SB algorithm. They both return the optimal polynomial value found by the SB algorithm, along with its associated variable vector.

#### Minimization

```python
# Spin minimization
spin_value, spin_vector = sb.minimize(matrix, vector, constant, domain='spin')

# Binary minimization
binary_value, binary_vector = sb.minimize(matrix, vector, constant, domain='binary')

# 3-bits integer minimization
int_value, int_vector = sb.minimize(matrix, vector, constant, domain='int3')

# Minimization with each variable having its own domain
value, vector = sb.minimize(matrix, vector, constant, domain=['spin', 'binary', 'int3'])
```

Or, using a SymPy expression:

```python
# Spin minimization
spin_value, spin_vector = sb.minimize(expression, domain='spin')

# Binary minimization
binary_value, binary_vector = sb.minimize(expression, domain='binary')

# 3-bits integer minimization
int_value, int_vector = sb.minimize(expression, domain='int3')

# Minimization with each variable having its own domain
value, vector = sb.minimize(expression, domain=['spin', 'binary', 'int3'])
```

#### Maximization

```python
# Spin maximization
spin_value, spin_vector = sb.maximize(matrix, vector, constant, domain='spin')

# Binary maximization
binary_value, binary_vector = sb.maximize(matrix, vector, constant, domain='binary')

# 10-bits integer maximization
int_value, int_vector = sb.maximize(matrix, vector, constant, domain='int10')

# Maximization with each variable having its own domain
value, vector = sb.minimize(matrix, vector, constant, domain=['spin', 'binary', 'int10'])
```

Or, using a SymPy expression:

```python
# Spin minimization
spin_value, spin_vector = sb.maximize(expression, domain='spin')

# Binary minimization
binary_value, binary_vector = sb.maximize(expression, domain='binary')

# 3-bits integer minimization
int_value, int_vector = sb.maximize(expression, domain='int10')

# Maximization with each variable having its own domain
value, vector = sb.minimize(expression, domain=['spin', 'binary', 'int10'])
```

> For both functions, only the matrix is required, the vector and constant terms are optional.

### Parallelization (multi-agent search)

The Simulated Bifurcation algorithm is highly parallelizable since it only relies on linear matrices equations. To take advantage of this property, this implementation offers the possibility to perform a multi-agent search of the optimal solution by evolving several spin vectors in parallel (each one being called an **agent**). The number of agents is set by the `agents` parameter in the `minimize` and `maximize` functions.

> **💡 Tip:** it is faster to run once the algorithm with N agents than to run N times the algorithm with only one agent.

```python
# Efficient computation ✔️
sb.minimize(matrix, agents=100)

# Slower cumbersome computation ❌
for _ in range(100):
    sb.minimize(matrix, agents=1)
```

### GPU computation

This parallelization of the algorithm can also be utilized by performing calculations on GPUs to speed them up significantly. To do this, simply specify the calculation `device` argument to `cuda` when instantiating an Ising model:

```python
sb.minimize(matrix, device='cuda')
```

### Early stopping

The Simulated Bifurcation algorithm stops after a certain number of iterations, defined by the parameter `max_steps` of the `minimize` and `maximize` functions. However, this implementation comes with the possibility to perform early stopping and save computation time by defining convergence conditions.

At regular intervals, the energy of the agents is sampled and compared with its previous value to calculate their stability period. If an agent's stability period exceeds a convergence threshold, it is considered to have converged and its value is frozen. If all agents converge before the maximum number of iterations has been reached, the algorithm stops.

- The sampling period and the convergence threshold are respectively set using the `sampling_period` and `convergence_threshold` parameters of the `minimize` and `maximize` functions.
- To use early stopping in the SB algorithm, set the `early_stopping` parameter to `True`.
- If only some agents have converged when the maximum number of iterations is reached, the algorithm stops and only these agents are considered in the results.

```python
# Stop with maximal iterations
sb.minimize(matrix, max_steps=10000)

# Early stopping
sb.minimize(
    matrix,
    sampling_period=30,
    convergence_threshold=50,
    early_stopping=True,
)
```

### Optimization results

By default, SB returns the best vector and objective value found. However, it is also possible to configure it to so it returns all the vectors for each agent with the associated objective value. To do so, the `best_only` parameter of the `minimize` and `maximize` functions must be set to `False` (default is `True`).

```python
best_vector, best_value = sb.minimize(matrix, best_only=True)
vectors, values = sb.maximize(matrix, best_only=False)
```

## 🚀 Advanced usages

This section deals with a more complex use of the SB algorithm, as it is closer to the quantum theory from which it is derived. To better understand the significance of the subjects at stake, we recommend reading the theory behind the SB algorithm by Goto _et al._.

- Goto, H., Tatsumura, K., & Dixon, A. R. (2019). Combinatorial optimization by simulating adiabatic bifurcations in nonlinear Hamiltonian systems. _Science advances, 5_(4), eaav2372.
- Kanao, T., & Goto, H. (2022). Simulated bifurcation assisted by thermal fluctuation. _Communications Physics, 5_(1), 153.
- Goto, H., Endo, K., Suzuki, M., Sakai, Y., Kanao, T., Hamakawa, Y., ... & Tatsumura, K. (2021). High-performance combinatorial optimization based on classical mechanics. _Science Advances, 7_(6), eabe7953.

### SB Algorithm modes

The SB algorithm is available in four different versions (Goto _et al._) that result in small variations in the algorithm general operation. The four modes are:

1. **Ballistic SB (bSB)**: uses the particles' position for the SB matrix computations; usually faster but less accurate.
2. **Discrete SB (dSB)**: uses the sign of the particles' position for the SB matrix computations; usually slower but more accurate.
3. **Heated ballistic SB (HbSB)**: uses the bSB algorithm with a supplementary non-symplectic term to allow a higher solution space exploration.
4. **Heated discrete SB (HdSB)**: uses the dSB algorithm with a supplementary non-symplectic term to allow a higher solution space exploration.

These modes can be selected setting the parameters `mode` to either `"ballistic"` or `"discrete"` and `heated` to either `True` or `False` in the `minimize`/`maximize` functions.

```python
sb.minimize(matrix, mode="ballistic", heated=False)  # bSB
sb.minimize(matrix, mode="discrete", heated=True)  # HdSB

sb.maximize(matrix, mode="discrete", heated=False)  # dSB
sb.maximize(matrix, mode="ballistic", heated=True)  # HbSB
```

### SB Algorithm's hyperparameters setting

The SB algorithm has a set of hyperparameters corresponding to physical constants derived from quantum theory, which have been fine-tuned (Goto _et al._) to give the best results most of the time. Nevertheless, the relevance of specific hyperparameters may vary depending on the properties of the instances. For this purpose, the `set_env` function can be used to modify their value.

```python
# Custom hyperparameters values
sb.set_env(time_step=.1, pressure_slope=.01, heat_coefficient=.06)

# Default hyperparameters values
sb.reset_env()
```

### Derived optimization models

A lot of mathematical problems (QUBO, Travelling Salesman Problem, MAXCUT, ...) can be written as quadratic models, and thus can be solved using the Simulated Bifurcation algorithm. Some of them are already implemented in the `models` module:

**🔬 Physics**

- Ising model

**📐 Mathematics**

- Quadratic Unconstrained Binary Optimization (QUBO)
- Number partitioning

**💸 Finance**

- Markowitz model

### Custom models

You are also free to create your own models using our API. Depending on the type of model you wish to implement, you can create a subclass of the `ABCModel` class to quickly and efficiently link your custom model to an Ising problem and solve it using the SB algorithm. Such a model must have a `domain` class attribute that set the definition domain of all the instances.

For instance, here is how the QUBO model was implemented:

> The QUBO problem consists, given an upper triangular matrix $Q$, in finding the binary vector that minimizes the value
> $$\sum_{i=1}^{N} \sum_{j=1}^{N} Q_{ij}x_{i}x_{j}$$

```python
from simulated_bifurcation.models import ABCModel


class QUBO(ABCModel):

    domain = "binary"

    def __init__(
        self,
        Q: Union[torch.Tensor, np.ndarray],
        dtype: Optional[torch.dtype] = None,
        device: Optional[Union[str, torch.device]] = None,
    ) -> None:
        super().__init__(Q, dtype=dtype, device=device)
        self.Q = self[2]
```

> You can check Andrew Lucas' paper on Ising formulations of NP-complete and NP-hard problems, including all of Karp's 21 NP-complete problems.
> 
> [🔎 Lucas, A. (2014). Ising formulations of many NP problems. _Frontiers in physics, 2_, 5.](https://www.frontiersin.org/articles/10.3389/fphy.2014.00005/full)

## 🔗 Cite this work

If you are using this code for your own projects please cite our work:

```bibtex
@software{Ageron_Simulated_Bifurcation_SB_2023,
    author = {Ageron, Romain and Bouquet, Thomas and Pugliese, Lorenzo},
    month = apr,
    title = {{Simulated Bifurcation (SB) algorithm for Python}},
    url = {https://github.com/bqth29/simulated-bifurcation-algorithm},
    version = {2.1.0.dev0},
    year = {2025},
}
```

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/core/__init__.py`
```python

```

#### File: `tests/optimizer/__init__.py`
```python

```

#### File: `src/simulated_bifurcation/core/optimization_domain.py`
```python
from enum import Enum


class OptimizationDomain(Enum):
    SPIN = "spin"
    BINARY = "binary"
    INTEGER = "integer"
```

#### File: `tests/test_utils.py`
```python
import torch

BOOLEANS = [True, False]

DTYPES = [torch.float32, torch.float64]

DEVICES = (
    [torch.device("cpu"), torch.device("cuda")]
    if torch.cuda.is_available()
    else [torch.device("cpu")]
)
```

#### File: `tests/models/test_ising_model.py`
```python
import torch

from src.simulated_bifurcation.models import Ising


def test_ising():
    torch.manual_seed(42)
    J = torch.tensor([[0, -2, 3], [-2, 0, 1], [3, 1, 0]])
    h = torch.tensor([1, -4, 2])
    model = Ising(J, h, dtype=torch.float32, device=torch.device("cpu"))
    spin_vector, value = model.minimize(
        agents=10, best_only=True, mode="ballistic", verbose=False
    )
    assert torch.equal(
        torch.tensor([-1.0, 1.0, -1.0], dtype=torch.float32), spin_vector
    )
    assert -11.0 == value
```


==================================================


## [3/3] Repository: optimizer (`PHASE4-QUANT-098`)
- **Full Name**: `PHASE4-QUANT-098_SilvioBaratto__optimizer`
- **Description**: Quantitative portfolio construction and optimization platform built on skfolio and scikit-learn.
- **GitHub Stars**: 173
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# portopt

[![CI](https://github.com/SilvioBaratto/optimizer/actions/workflows/ci.yml/badge.svg)](https://github.com/SilvioBaratto/optimizer/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/portopt)](https://pypi.org/project/portopt/)
![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
[![codecov](https://codecov.io/gh/SilvioBaratto/optimizer/branch/main/graph/badge.svg)](https://codecov.io/gh/SilvioBaratto/optimizer)
![License](https://img.shields.io/badge/license-PolyForm--Noncommercial--1.0.0-green)
[![oosmetrics](https://api.oosmetrics.com/api/v1/badge/achievement/c47694dc-b34e-481e-8907-2766ff13d4cd.svg)](https://oosmetrics.com/repo/SilvioBaratto/optimizer)

Quantitative portfolio construction and optimization built on [skfolio](https://skfolio.org/) and scikit-learn. Every component follows the **frozen-config + factory** pattern and composes in standard sklearn pipelines.

The repository is a **`uv` workspace** with three packages:

- **`optimizer/`** — the pure-Python optimization library, published to PyPI as **`portopt-core`** (import package `optimizer`). DB-agnostic, no API keys, no I/O.
- **`ingestion/`** — the **`portopt`** app: a yfinance-centric ingestion daemon (PostgreSQL + SQLAlchemy + APScheduler) plus a `uv`-installable CLI and install wizard. No HTTP API.
- **`packages/portopt-db/`** — **`portopt-db`** (import package `portopt_db`): the shared database layer — SQLAlchemy models, repositories, connection manager, and the single Alembic migration tree. Consumed by `ingestion`; carries no sklearn/skfolio stack.

The optimizer library is independent of the data side: neither `ingestion/` nor `portopt-db/` imports `optimizer`, and the daemon image carries none of the sklearn/skfolio optimization stack.

## Installation

The **`portopt` CLI** (ingestion daemon + install wizard) installs via [uv](https://docs.astral.sh/uv/):

```bash
# mac/linux
curl -LsSf https://raw.githubusercontent.com/SilvioBaratto/optimizer/main/install.sh | bash
# windows
powershell -c "irm https://raw.githubusercontent.com/SilvioBaratto/optimizer/main/install.ps1 | iex"
```

The bootstrap installs `uv` (if missing), runs `uv tool install portopt`, and launches
`portopt setup` — an interactive wizard that verifies Docker, validates your API keys,
encrypts your secrets (`~/.portopt/secrets.enc`), and migrates the database. Re-run any time
with `portopt setup`; manage the stack with `portopt start` / `portopt stop` / `portopt status`.

The optimization **library** is a separate distribution, `portopt-core` (import package `optimizer`):

```bash
pip install portopt-core
```

For development (tests, linting, type checking):

```bash
git clone https://github.com/SilvioBaratto/optimizer.git
cd optimizer
pip install -e ".[dev]"
```

## Quick Start

```python
from optimizer.optimization import MeanRiskConfig, build_mean_risk
from optimizer.pre_selection import build_portfolio_pipeline
from optimizer.validation import WalkForwardConfig, build_walk_forward, run_cross_val
from skfolio.preprocessing import prices_to_returns

# Build an optimizer from a frozen config
optimizer = build_mean_risk(MeanRiskConfig.for_max_sharpe())

# Compose pre-selection + optimizer into one sklearn Pipeline
pipeline = build_portfolio_pipeline(optimizer)

# Convert prices -> linear returns OUTSIDE the pipeline (semantic change)
returns = prices_to_returns(price_df)

# In-sample fit / predict
pipeline.fit(returns)
portfolio = pipeline.predict(returns)
print(portfolio.weights)         # asset weights
print(portfolio.sharpe_ratio)

# Out-of-sample walk-forward backtest
cv = build_walk_forward(WalkForwardConfig.for_quarterly_rolling())
population = run_cross_val(pipeline, returns, cv=cv)
```

## Features

### Composable pipeline

`optimizer` is a **library of composable primitives**, not a fixed end-to-end
runner. Every stage — preprocessing, pre-selection, moment estimation, views,
optimization, validation, tuning, rebalancing — is a standalone sklearn-compatible
component. `build_portfolio_pipeline(optimizer)` flattens pre-selection + the
optimizer into a single sklearn `Pipeline`:

```
returns -> [validate -> outliers -> impute -> select -> optimize] -> Portfolio
           \_______________ sklearn Pipeline _______________/
```

Prices are converted to returns **outside** the pipeline (semantic change).
The composed `Pipeline` is a single estimator that can be cross-validated and
tuned as one object — pre-selection runs *inside* each CV fold to prevent leakage.

> Opinionated, DB-connected orchestration (FX conversion, delisting correction,
> universe/factor selection, rebalancing decisions, persistence) is **not** part
> of this library — it belongs to the separate `fund/` bridge layer, keeping
> `optimizer` DB-agnostic.

### Preprocessing

Four sklearn-compatible transformers for return data cleaning:

- **DataValidator** -- replaces `inf` and extreme returns (|r| > 10) with `NaN`
- **OutlierTreater** -- three-group z-score methodology: remove data errors (>= 10 sigma), winsorize moderate outliers (3-10 sigma), keep normal observations
- **SectorImputer** -- leave-one-out sector-average NaN imputation with global mean fallback
- **RegressionImputer** -- OLS regression from top-5 correlated assets with cold-start fallback to sector imputation

### Pre-selection

Assembles data cleaning and asset filtering into a single sklearn pipeline:

`validate -> outliers -> impute -> select_complete -> drop_zero_variance -> drop_correlated -> [select_k] -> [select_pareto] -> [select_non_expiring]`

All steps run inside CV folds to prevent data leakage. Pipeline parameters are exposed via `get_params()` for hyperparameter tuning.

### Moment Estimation

4 expected-return estimators and 11 covariance estimators:

| Expected Returns | Covariance |
|---|---|
| Empirical, Shrunk (James-Stein, Bayes-Stein, Bodnar-Okhrin), Exponentially Weighted, Equilibrium (CAPM) | Empirical, EW, Ledoit-Wolf, OAS, Shrunk, Denoised (RMT), Detoned, Gerber, Graphical Lasso CV, Implied, Regime-Adjusted EW |

**Regime-adjusted EW**: short-term volatility uplift applied on top of an exponentially weighted covariance (multiplier internal to skfolio, clipped to `(0.7, 1.6)`).

**Log-normal scaling**: multi-period moment projection with Jensen's inequality correction (`apply_lognormal_correction`, `scale_moments_to_horizon`).

Separately, `build_variance_estimator()` returns 1-D `BaseVariance` estimators (`variance_`, not `covariance_`) — not interchangeable with covariance estimators inside priors.

### View Integration

Three frameworks for incorporating forward-looking views:

- **Black-Litterman** -- Bayesian posterior combining market equilibrium with absolute/relative views. Omega from He-Litterman, Idzorek confidence, or empirical track record (`calibrate_omega_from_track_record`)
- **Entropy Pooling** -- mean, variance, correlation, skew, kurtosis, and CVaR views via KL-divergence minimization
- **Opinion Pooling** -- linear and logarithmic combination of multiple expert priors

### Optimization

13 portfolio optimization models across 4 categories:

| Category | Models |
|---|---|
| **Convex** | MeanRisk, Risk Budgeting, Maximum Diversification, Benchmark Tracker, DR-CVaR |
| **Hierarchical** | HRP, HERC, NCO, Schur Complementary |
| **Naive** | Equal Weighted, Inverse Volatility, Random |
| **Ensemble** | Stacking Optimization |

**Robust variants**: ellipsoidal/bootstrap mu and covariance uncertainty sets (`RobustMeanRisk`), distributionally robust CVaR over a Wasserstein ball, and `RegimeBlendedMeanRisk` which consumes externally-supplied regime probabilities (the library does not fit HMMs itself).

**Constraint helpers**: `build_sector_constraints()` and `build_region_linear_constraints()` emit skfolio `linear_constraints` strings for group exposure bands.

Every model uses frozen `@dataclass` configs with named presets:

```python
MeanRiskConfig.for_max_sharpe()           # maximize Sharpe ratio
MeanRiskConfig.for_min_cvar(beta=0.95)    # minimize CVaR at 95%
RobustMeanRiskConfig.for_conservative()   # 99% uncertainty-set confidence
DRCVaRConfig.for_moderate()               # Wasserstein ball radius
```

### Validation

Temporal cross-validation strategies that respect the time-series nature of financial data:

- **Walk-Forward** -- rolling or expanding window (monthly, quarterly presets)
- **Combinatorial Purged CV** -- multiple non-overlapping test paths with purging and embargoing to prevent leakage
- **Multiple Randomized CV** -- Monte Carlo evaluation with asset subsampling

Plus covariance-forecast evaluation (offline and online).

### Scoring and Tuning

Ratio measures (Sharpe, Sortino, Calmar, CVaR ratio, ...) for model selection. Grid search and randomized search with temporal CV enforced by default. Nested parameter addressing via sklearn's double-underscore syntax:

```python
param_grid = {
    "prior_estimator__mu_estimator__alpha": [0.01, 0.1],
    "risk_measure": [RiskMeasureType.CVAR, RiskMeasureType.SEMI_VARIANCE],
}
```

### Rebalancing

Three strategies for determining when to trade:

- **Calendar** -- fixed intervals (monthly, quarterly, semiannual, annual)
- **Threshold** -- drift-based (absolute or relative)
- **Hybrid** -- calendar-gated threshold (check drift only at review dates)

Plus utility functions: `compute_drifted_weights()`, `compute_turnover()`, `compute_rebalancing_cost()`.

### Factor Research

Complete factor research pipeline with 17 factors across 9 groups:

**Construction** -> **Standardization** (winsorize, z-score, sector neutralize) -> **Scoring** (equal-weight, IC-weighted, ICIR-weighted, Ridge, GBT) -> **Selection** (fixed-count or quantile with buffer hysteresis) -> **Regime Tilts** (GDP/yield-spread classification with multiplicative group tilts)

**Validation**: Information Coefficient analysis, Newey-West t-statistics, VIF collinearity, Benjamini-Hochberg FDR correction, out-of-sample rolling block validation.

**Integration**: factor exposure constraints for MeanRisk, Black-Litterman views from factor premia, net alpha after turnover costs.

### Synthetic Data

Vine copula models for scenario generation. Decomposes the multivariate return distribution into marginal distributions and bivariate copulas organized in a tree structure. Supports conditional sampling for stress testing:

```python
# What if SPY drops 10%?
prior = build_synthetic_data(
    SyntheticDataConfig.for_stress_test(),
    sample_args={"conditioning": {"SPY": -0.10}},
)
```

### Universe Screening

8 investability screens with hysteresis entry/exit thresholds to reduce universe turnover: market cap, 12m/3m average daily dollar volume, trading frequency, price floors (US/Europe), listing age, IPO seasoning, financial statement coverage, exchange-relative percentile.

### FX

Multi-currency handling: `FxPriceConverter` (sklearn transformer) converts a multi-currency price panel to a base currency (EUR/GBP/USD, optionally crossing via USD), and `decompose_fx_returns()` splits total return into stock-only and FX components.

## Design Principles

**Config + Factory**: Every module uses frozen `@dataclass` configs holding only serializable primitives and enums. Factory functions create estimator instances. Configs can be serialized, logged, and swept over; non-serializable objects (estimators, arrays, callables) are passed as factory kwargs.

**sklearn compatibility**: All transformers follow `BaseEstimator + TransformerMixin`. The full preprocessing + optimization chain composes in `sklearn.pipeline.Pipeline` and can be cross-validated, tuned, and serialized as one object.

**skfolio foundation**: Optimization models wrap [skfolio](https://skfolio.org/) estimators. portopt adds robust uncertainty sets, factor research, rebalancing, universe screening, and FX on top.

## Architecture

```
optimizer/            Pure-Python library (DB-agnostic, sklearn/skfolio-based)
  pre_selection/      Asset filtering + build_portfolio_pipeline composition
  preprocessing/      Return data cleaning (validation, outliers, imputation)
  pre_selection/      Asset filtering pipeline (completeness, variance, correlation)
  moments/            Expected return + covariance + variance estimation, prior construction
  views/              Black-Litterman, Entropy Pooling, Opinion Pooling
  optimization/       13 optimization models + robust variants + group constraints
  validation/         Walk-Forward, Combinatorial Purged CV, Randomized CV
  scoring/            Ratio measures for model selection
  tuning/             Grid/randomized search with temporal CV
  rebalancing/        Calendar, threshold, and hybrid rebalancing
  factors/            17 factors, scoring, selection, regime tilts, validation
  synthetic/          Vine copula scenario generation + stress testing
  universe/           Investability screening with hysteresis
  distance/           Distance estimators for hierarchical optimizers
  cluster/            Hierarchical clustering wrapper
  uncertainty_set/    Mu / covariance uncertainty sets for robust optimization
  linear_model/       Cross-sectional regression (factor IC)
  online/             partial_fit-based incremental workflows
  fx/                 Multi-currency conversion + FX return decomposition

ingestion/            Ingestion daemon (PostgreSQL, APScheduler) — services/scheduler/CLI
packages/portopt-db/  Shared DB layer (models, repositories, engine, single Alembic tree)
scheduler/            Shell wrappers over the daemon CLI (fetch, refetch)
scripts/              CI helpers (branch-coverage gate)
tests/                Library test suite
```

## Development

```bash
# uv workspace: one venv for all three packages
uv sync --all-packages --all-extras

# Tests (per package)
uv run --package portopt-core pytest tests/ -v       # optimizer library
uv run --package portopt-db   pytest                 # shared DB layer
uv run --package portopt      pytest                 # ingestion daemon

# Lint / type check
uv run --package portopt-core ruff check optimizer/ tests/
uv run --package portopt-core mypy optimizer/

# Everything (lint + typecheck + test)
make all
```

`pip install -e ".[dev]"` still works for the library alone if you are not on uv.

## Ingestion daemon

`ingestion/` is **yfinance-centric**: it builds its instrument universe from the yfinance
Screener and fetches market data, fundamentals, and macro series (FRED, Il Sole 24 Ore,
Trading Economics) into PostgreSQL on a schedule. APScheduler runs in-process; there is no
HTTP API. Job metrics are exposed to Prometheus, which is also the container healthcheck
target. Trading 212 is an optional add-on — when configured, its tickers are mapped onto the
yfinance universe *after* the build (it no longer sources it).

```bash
# PostgreSQL (host port 54320) + Adminer (18081) + scheduler (metrics 9000)
docker compose up -d
docker compose logs -f scheduler

# Or run the daemon directly (uv workspace)
uv sync --all-packages --all-extras
(cd packages/portopt-db && alembic upgrade head)   # migrations owned by portopt-db
uv run --package portopt python -m app.worker      # blocks until SIGTERM
```

Seven scheduled jobs: `daily_pipeline` (07:00), `midday_news` (14:00), `universe_build`
(Sun 02:00), `weekly_refetch` (Sun 03:00), `fred_monthly`, `news_refresh` (30 min), and
`orphan_reaper`. Cadence is configurable via `SCHEDULER_*` env vars.

Any step can be run by hand through the same job-slot and heartbeat path the scheduler
uses — so a manual run is refused rather than double-fetching if the scheduler is already
running that step:

```bash
docker compose exec scheduler python -m app.cli daily
docker compose exec scheduler python -m app.cli yfinance --mode full --period 5y
# also: refetch-all | universe | macro | fred | news | reference-indices
```

Run **exactly one daemon per database**: the orphan reaper fails any active job whose
worker host is not its own, so two instances will reap each other's jobs.

See `ingestion/README.md` for the full picture.

### Environment Variables

`portopt setup` collects and encrypts these; for CI / manual runs the daemon also reads them
from the environment (and Docker-compose `secrets:` at `/run/secrets/*`):

| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `FRED_API_KEY` | Federal Reserve Economic Data |
| `TRADING_212_API_KEY` / `TRADING_212_SECRET_KEY` / `TRADING_212_MODE` | Optional Trading 212 add-on — mapped onto the yfinance universe after the build |
| `METRICS_PORT` | Prometheus port (default `9000`) |
| `NOTIFICATION_WEBHOOK_URL` | Discord/Slack webhook for job-failure alerts (optional) |

Il Sole 24 Ore and Trading Economics are scraped from HTML and need no key.
Scheduler cadence is configurable via `SCHEDULER_*` env vars — see `CLAUDE.md`.

## Disclaimer

This software is provided for **educational and research purposes only**. It is not intended as, and shall not be understood or construed as, financial, investment, tax, or legal advice.

**No investment advice.** The authors and contributors are not registered investment advisors, broker-dealers, or financial planners. Nothing in this software or its documentation constitutes a recommendation to buy, sell, or hold any financial instrument.

**No liability for losses.** The authors and contributors accept no responsibility or liability whatsoever for any loss or damage arising from the use of this software. You may lose some or all of your invested capital. Use this software entirely at your own risk.

**Past performance is not indicative of future results.** Backtesting and historical analysis produced by this software do not guarantee future performance. Simulated results may not reflect the impact of real market conditions including liquidity, slippage, fees, and taxes.

**Seek professional advice.** Before making any investment decision, consult with a qualified, licensed financial advisor, accountant, or attorney.

By using this software, you acknowledge that you have read and understood this disclaimer and agree to be bound by its terms.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=SilvioBaratto/optimizer&type=Date)](https://star-history.com/#SilvioBaratto/optimizer&Date)

## License

[PolyForm Noncommercial License 1.0.0](LICENSE)

### Core Implementation Code & Architecture
#### File: `ingestion/tests/unit/setup/__init__.py`
```python

```

#### File: `ingestion/tests/unit/schemas/__init__.py`
```python

```

#### File: `ingestion/tests/unit/_shared/__init__.py`
```python

```

#### File: `ingestion/tests/unit/services/__init__.py`
```python

```

#### File: `ingestion/tests/unit/services/market_data/__init__.py`
```python

```

#### File: `ingestion/tests/unit/services/macro/__init__.py`
```python

```


==================================================
