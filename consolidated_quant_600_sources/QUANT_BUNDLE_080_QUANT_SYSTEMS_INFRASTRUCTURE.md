# ⚡ [QUANT-SOURCE-080] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_080_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: optuna (`WHEEL_optuna`)
- **Full Name**: `optuna`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<div align="center"><img src="https://raw.githubusercontent.com/optuna/optuna/master/docs/image/optuna-logo.png" width="800"/></div>

# Optuna: A hyperparameter optimization framework

[![Python](https://img.shields.io/badge/python-3.9%20%7C%203.10%20%7C%203.11%20%7C%203.12%20%7C%203.13%20%7C%203.14-blue)](https://www.python.org)
[![pypi](https://img.shields.io/pypi/v/optuna.svg)](https://pypi.python.org/pypi/optuna)
[![conda](https://img.shields.io/conda/vn/conda-forge/optuna.svg)](https://anaconda.org/conda-forge/optuna)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/optuna/optuna)
[![Read the Docs](https://readthedocs.org/projects/optuna/badge/?version=stable)](https://optuna.readthedocs.io/en/stable/)

:link: [**Website**](https://optuna.org/)
| :page_with_curl: [**Docs**](https://optuna.readthedocs.io/en/stable/)
| :gear: [**Install Guide**](https://optuna.readthedocs.io/en/stable/installation.html)
| :pencil: [**Tutorial**](https://optuna.readthedocs.io/en/stable/tutorial/index.html)
| :bulb: [**Examples**](https://github.com/optuna/optuna-examples)
| [**Twitter**](https://twitter.com/OptunaAutoML)
| [**LinkedIn**](https://www.linkedin.com/showcase/optuna/)
| [**Medium**](https://medium.com/optuna)

*Optuna* is an automatic hyperparameter optimization software framework, particularly designed
for machine learning. It features an imperative, *define-by-run* style user API. Thanks to our
*define-by-run* API, the code written with Optuna enjoys high modularity, and the user of
Optuna can dynamically construct the search spaces for the hyperparameters.

## :loudspeaker: News

<!-- TODO: when you add a new line, please delete the oldest line -->
* **Sep 7, 2026**: Optuna v5 and [Rustuna](https://github.com/optuna/rustuna/) v0.1.0 have been released! Check out the release blog posts.
  * [Optuna v5.0.0 release blog post](https://medium.com/optuna/releasing-optuna-v5-0-an-open-source-black-box-optimization-library-9bff8b4587ba)
  * [Rustuna v0.1.0 release blog post](https://medium.com/optuna/announcing-rustuna-cc82a6815bf7)
* **Aug 3, 2026**: Release candidate of Optuna v5 is available! Check out [the release note](https://github.com/optuna/optuna/releases/tag/v5.0.0-rc1) for details.
* **Jun 1, 2026**: Optuna 4.9.0 is out! Check out [the release note](https://github.com/optuna/optuna/releases/tag/v4.9.0) for details.
* **Mar 16, 2026**: Optuna 4.8.0 is out! Check out [the release note](https://github.com/optuna/optuna/releases/tag/v4.8.0) for details.
* **Jan 19, 2026**: Optuna 4.7.0 is out! Check out [the release note](https://github.com/optuna/optuna/releases/tag/v4.7.0) for details.
* **Nov 10, 2025**: A new article [Announcing Optuna 4.6](https://medium.com/optuna/announcing-optuna-4-6-a9e82183ab07) has been published.

## :fire: Key Features

Optuna has modern functionalities as follows:

- [Lightweight, versatile, and platform agnostic architecture](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/001_first.html)
  - Handle a wide variety of tasks with a simple installation that has few requirements.
- [Pythonic search spaces](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/002_configurations.html)
  - Define search spaces using familiar Python syntax including conditionals and loops.
- [Efficient optimization algorithms](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/003_efficient_optimization_algorithms.html)
  - Adopt state-of-the-art algorithms for sampling hyperparameters and efficiently pruning unpromising trials.
- [Easy parallelization](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/004_distributed.html)
  - Scale studies to tens or hundreds of workers with little or no changes to the code.
- [Quick visualization](https://optuna.readthedocs.io/en/stable/tutorial/10_key_features/005_visualization.html)
  - Inspect optimization histories from a variety of plotting functions.


## Basic Concepts

We use the terms *study* and *trial* as follows:

- Study: optimization based on an objective function
- Trial: a single execution of the objective function

Please refer to the sample code below. The goal of a *study* is to find out the optimal set of
hyperparameter values (e.g., `regressor` and `svr_c`) through multiple *trials* (e.g.,
`n_trials=100`). Optuna is a framework designed for automation and acceleration of
optimization *studies*.

<details open>
<summary>Sample code with scikit-learn</summary>

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](http://colab.research.google.com/github/optuna/optuna-examples/blob/main/quickstart.ipynb)

```python
import optuna
import sklearn


# Define an objective function to be minimized.
def objective(trial):

    # Invoke suggest methods of a Trial object to generate hyperparameters.
    regressor_name = trial.suggest_categorical("regressor", ["SVR", "RandomForest"])
    if regressor_name == "SVR":
        svr_c = trial.suggest_float("svr_c", 1e-10, 1e10, log=True)
        regressor_obj = sklearn.svm.SVR(C=svr_c)
    else:
        rf_max_depth = trial.suggest_int("rf_max_depth", 2, 32)
        regressor_obj = sklearn.ensemble.RandomForestRegressor(max_depth=rf_max_depth)

    X, y = sklearn.datasets.fetch_california_housing(return_X_y=True)
    X_train, X_val, y_train, y_val = sklearn.model_selection.train_test_split(X, y, random_state=0)

    regressor_obj.fit(X_train, y_train)
    y_pred = regressor_obj.predict(X_val)

    error = sklearn.metrics.mean_squared_error(y_val, y_pred)

    return error  # An objective value linked with the Trial object.


study = optuna.create_study()  # Create a new study.
study.optimize(objective, n_trials=100)  # Invoke optimization of the objective function.
```
</details>

> [!NOTE]
> More examples can be found in [optuna/optuna-examples](https://github.com/optuna/optuna-examples).
>
> The examples cover diverse problem setups such as multi-objective optimization, constrained optimization, pruning, and distributed optimization.

## Installation

Optuna is available at [the Python Package Index](https://pypi.org/project/optuna/) and on [Anaconda Cloud](https://anaconda.org/conda-forge/optuna).

```bash
# PyPI
$ pip install optuna
```

```bash
# Anaconda Cloud
$ conda install -c conda-forge optuna
```

> [!IMPORTANT]
> Optuna supports Python 3.9 or newer.

## Rustuna

[Rustuna](https://github.com/optuna/rustuna) is a faster implementation of Optuna written in Rust.
It keeps the API you already know, and rewrites the parts that start to hurt at scale: sampling speed and memory efficiency.

1. **Faster sampler implementations**: Rustuna supports TPE, MOTPE, NSGA-II, and CMA-ES, and finishes the same study several times to several hundred times faster for cheap objective functions.
2. **Memory-efficient storage**: Several design choices to make Rustuna's storage memory-efficient. Furthermore, discarding unnecessary trial history prevents memory usage and runtime from increasing as the number of trials grows.
3. **Zero Python runtime dependencies**: No Python runtime dependencies by default ー dramatically faster imports, and far less exposure to supply chain attacks.

> [!NOTE]
> Rustuna is currently experimental. Compared with Optuna, it still lacks some features and APIs, and it has not yet been optimized enough to deliver better performance for every use case. Since the project has not had the same level of maturity as Optuna, bugs and rough edges likely remain. We appreciate your understanding when using it.

## Web Dashboard

[Optuna Dashboard](https://github.com/optuna/optuna-dashboard) is a real-time web dashboard for Optuna.
You can check the optimization history, hyperparameter importance, etc. in graphs and tables.
You don't need to create a Python script to call [Optuna's visualization](https://optuna.readthedocs.io/en/stable/reference/visualization/index.html) functions.
Feature requests and bug reports are welcome!

![optuna-dashboard](https://user-images.githubusercontent.com/5564044/204975098-95c2cb8c-0fb5-4388-abc4-da32f56cb4e5.gif)

`optuna-dashboard` can be installed via pip:

```shell
$ pip install optuna-dashboard
```

> [!TIP]
> Please check out the convenience of Optuna Dashboard using the sample code below.

<details>
<summary>Sample code to launch Optuna Dashboard</summary>

Save the following code as `optimize_toy.py`.

```python
import optuna


def objective(trial):
    x1 = trial.suggest_float("x1", -100, 100)
    x2 = trial.suggest_float("x2", -100, 100)
    return x1**2 + 0.01 * x2**2


study = optuna.create_study(storage="sqlite:///db.sqlite3")  # Create a new study with database.
study.optimize(objective, n_trials=100)
```

Then try the commands below:

```shell
# Run the study specified above
$ python optimize_toy.py

# Launch the dashboard based on the storage `sqlite:///db.sqlite3`
$ optuna-dashboard sqlite:///db.sqlite3
...
Listening on http://localhost:8080/
Hit Ctrl-C to quit.
```

</details>


## OptunaHub

[OptunaHub](https://hub.optuna.org/) is a feature-sharing platform for Optuna.
You can use the registered features and publish your packages.

### Use registered features

`optunahub` can be installed via pip:

```shell
$ pip install optunahub
# Install AutoSampler dependencies (CPU only is sufficient for PyTorch)
$ pip install cmaes scipy torch --extra-index-url https://download.pytorch.org/whl/cpu
```

You can load registered module with `optunahub.load_module`.

```python
import optuna
import optunahub


def objective(trial: optuna.Trial) -> float:
    x = trial.suggest_float("x", -5, 5)
    y = trial.suggest_float("y", -5, 5)
    return x**2 + y**2


module = optunahub.load_module(package="samplers/auto_sampler")
# See https://hub.optuna.org/samplers/auto_sampler/ to know the ``AutoSampler`` API.
study = optuna.create_study(sampler=module.AutoSampler())
study.optimize(objective, n_trials=10)

print(study.best_trial.value, study.best_trial.params)
```

For more details, please refer to [the optunahub documentation](https://optuna.github.io/optunahub/).

### Publish your packages

You can publish your package via [optunahub-registry](https://github.com/optuna/optunahub-registry).
See the [Tutorials for Contributors](https://optuna.github.io/optunahub/tutorials_for_contributors.html) in OptunaHub.


## Communication

- [GitHub Discussions] for questions.
- [GitHub Issues] for bug reports and feature requests.

[GitHub Discussions]: https://github.com/optuna/optuna/discussions
[GitHub issues]: https://github.com/optuna/optuna/issues


## Contribution

Any contributions to Optuna are more than welcome!

If you are new to Optuna, please check the [good first issues](https://github.com/optuna/optuna/labels/good%20first%20issue). They are relatively simple, well-defined, and often good starting points for you to get familiar with the contribution workflow and other developers.

If you already have contributed to Optuna, we recommend the other [contribution-welcome issues](https://github.com/optuna/optuna/labels/contribution-welcome).

For general guidelines on how to contribute to the project, take a look at [CONTRIBUTING.md](./CONTRIBUTING.md).


## Reference

If you use Optuna in one of your research projects, please cite [our KDD paper](https://doi.org/10.1145/3292500.3330701) "Optuna: A Next-generation Hyperparameter Optimization Framework":

<details open>
<summary>BibTeX</summary>

```bibtex
@inproceedings{akiba2019optuna,
  title={{O}ptuna: A Next-Generation Hyperparameter Optimization Framework},
  author={Akiba, Takuya and Sano, Shotaro and Yanase, Toshihiko and Ohta, Takeru and Koyama, Masanori},
  booktitle={The 25th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
  pages={2623--2631},
  year={2019}
}
```
</details>


## License

MIT License (see [LICENSE](./LICENSE)).

Optuna uses the codes from SciPy and fdlibm projects (see [LICENSE_THIRD_PARTY](./LICENSE_THIRD_PARTY)).

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/trial_tests/__init__.py`
```python

```

#### File: `tests/pruners_tests/__init__.py`
```python

```

#### File: `tests/study_tests/__init__.py`
```python

```

#### File: `tests/hypervolume_tests/__init__.py`
```python

```

#### File: `tests/importance_tests/__init__.py`
```python

```


==================================================


## [2/3] Repository: orjson (`WHEEL_orjson`)
- **Full Name**: `orjson`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# orjson

orjson is a fast, correct JSON library for Python. It
[benchmarks](https://github.com/ijl/orjson?tab=readme-ov-file#performance) as the fastest Python
library for JSON and is more correct than the standard json library or other
third-party libraries. It serializes
[dataclass](https://github.com/ijl/orjson?tab=readme-ov-file#dataclass),
[datetime](https://github.com/ijl/orjson?tab=readme-ov-file#datetime),
[numpy](https://github.com/ijl/orjson?tab=readme-ov-file#numpy), and
[UUID](https://github.com/ijl/orjson?tab=readme-ov-file#uuid) instances natively.

[orjson.dumps()](https://github.com/ijl/orjson?tab=readme-ov-file#serialize) is
something like 10x as fast as `json`, serializes
common types and subtypes, has a `default` parameter for the caller to specify
how to serialize arbitrary types, and has a number of flags controlling output.

[orjson.loads()](https://github.com/ijl/orjson?tab=readme-ov-file#deserialize)
is something like 2x as fast as `json`, and is strictly compliant with UTF-8 and
RFC 8259 ("The JavaScript Object Notation (JSON) Data Interchange Format").

Reading from and writing to files, line-delimited JSON files, and so on is
not provided by the library.

orjson supports CPython 3.10, 3.11, 3.12, 3.13, 3.14, and 3.15.

It distributes amd64/x86_64/x64, i686/x86, aarch64/arm64/armv8, and armv7 wheels
for Linux, amd64 and aarch64 wheels
for macOS, and amd64, i686, and aarch64 wheels for Windows.

Wheels published to PyPI for amd64 run on x86-64-v1 (2003)
or later, but will at runtime use AVX-512 if available for a
significant performance benefit; aarch64 wheels run on ARMv8-A (2011) or
later.

orjson does not and will not support PyPy, embedded Python builds for
Android/iOS, or PEP 554 subinterpreters.

orjson may support PEP 703 free-threading when it is stable.

Releases follow semantic versioning and serializing a new object type
without an opt-in flag is considered a breaking change.

orjson contains source code licensed under the Mozilla Public License 2.0,
Apache 2.0, and MIT licenses. The repository from which PyPI artifacts are
published is [github.com/ijl/orjson](https://github.com/ijl/orjson) and an
alternative repository is [codeberg.org/ijl/orjson](https://codeberg.org/ijl/orjson).
There is no open issue tracker or pull requests due to signal-to-noise ratio.
There is a [CHANGELOG](https://github.com/ijl/orjson/blob/master/CHANGELOG.md)
available in the repository.

1. [Usage](https://github.com/ijl/orjson?tab=readme-ov-file#usage)
    1. [Install](https://github.com/ijl/orjson?tab=readme-ov-file#install)
    2. [Quickstart](https://github.com/ijl/orjson?tab=readme-ov-file#quickstart)
    3. [Migrating](https://github.com/ijl/orjson?tab=readme-ov-file#migrating)
    4. [Serialize](https://github.com/ijl/orjson?tab=readme-ov-file#serialize)
        1. [default](https://github.com/ijl/orjson?tab=readme-ov-file#default)
        2. [option](https://github.com/ijl/orjson?tab=readme-ov-file#option)
        3. [Fragment](https://github.com/ijl/orjson?tab=readme-ov-file#fragment)
    5. [Deserialize](https://github.com/ijl/orjson?tab=readme-ov-file#deserialize)
2. [Types](https://github.com/ijl/orjson?tab=readme-ov-file#types)
    1. [dataclass](https://github.com/ijl/orjson?tab=readme-ov-file#dataclass)
    2. [datetime](https://github.com/ijl/orjson?tab=readme-ov-file#datetime)
    3. [enum](https://github.com/ijl/orjson?tab=readme-ov-file#enum)
    4. [float](https://github.com/ijl/orjson?tab=readme-ov-file#float)
    5. [int](https://github.com/ijl/orjson?tab=readme-ov-file#int)
    6. [numpy](https://github.com/ijl/orjson?tab=readme-ov-file#numpy)
    7. [str](https://github.com/ijl/orjson?tab=readme-ov-file#str)
    8. [uuid](https://github.com/ijl/orjson?tab=readme-ov-file#uuid)
3. [Testing](https://github.com/ijl/orjson?tab=readme-ov-file#testing)
4. [Performance](https://github.com/ijl/orjson?tab=readme-ov-file#performance)
    1. [Latency](https://github.com/ijl/orjson?tab=readme-ov-file#latency)
    2. [Reproducing](https://github.com/ijl/orjson?tab=readme-ov-file#reproducing)
5. [Questions](https://github.com/ijl/orjson?tab=readme-ov-file#questions)
6. [Packaging](https://github.com/ijl/orjson?tab=readme-ov-file#packaging)
7. [License](https://github.com/ijl/orjson?tab=readme-ov-file#license)

## Usage

### Install

To install a wheel from PyPI, install the `orjson` package.

In `requirements.in` or `requirements.txt` format, specify:

```txt
orjson >= 3.10,<4
```

In `pyproject.toml` format, specify:

```toml
orjson = "^3.10"
```

To build a wheel, see [packaging](https://github.com/ijl/orjson?tab=readme-ov-file#packaging).

### Quickstart

This is an example of serializing, with options specified, and deserializing:

```python
>>> import orjson, datetime, numpy
>>> data = {
    "type": "job",
    "created_at": datetime.datetime(1970, 1, 1),
    "status": "🆗",
    "payload": numpy.array([[1, 2], [3, 4]]),
}
>>> orjson.dumps(data, option=orjson.OPT_NAIVE_UTC | orjson.OPT_SERIALIZE_NUMPY)
b'{"type":"job","created_at":"1970-01-01T00:00:00+00:00","status":"\xf0\x9f\x86\x97","payload":[[1,2],[3,4]]}'
>>> orjson.loads(_)
{'type': 'job', 'created_at': '1970-01-01T00:00:00+00:00', 'status': '🆗', 'payload': [[1, 2], [3, 4]]}
```

### Migrating

orjson version 3 serializes more types than version 2. Subclasses of `str`,
`int`, `dict`, and `list` are now serialized. This is faster and more similar
to the standard library. It can be disabled with
`orjson.OPT_PASSTHROUGH_SUBCLASS`.`dataclasses.dataclass` instances
are now serialized by default and cannot be customized in a
`default` function unless `option=orjson.OPT_PASSTHROUGH_DATACLASS` is
specified. `uuid.UUID` instances are serialized by default.
For any type that is now serialized,
implementations in a `default` function and options enabling them can be
removed but do not need to be. There was no change in deserialization.

To migrate from the standard library, the largest difference is that
`orjson.dumps` returns `bytes` and `json.dumps` returns a `str`.

Users with `dict` objects using non-`str` keys should specify `option=orjson.OPT_NON_STR_KEYS`.

`sort_keys` is replaced by `option=orjson.OPT_SORT_KEYS`.

`indent` is replaced by `option=orjson.OPT_INDENT_2` and other levels of indentation are not
supported.

`ensure_ascii` is probably not relevant today and UTF-8 characters cannot be
escaped to ASCII.

### Serialize

```python
def dumps(
    __obj: Any,
    default: Optional[Callable[[Any], Any]] = ...,
    option: Optional[int] = ...,
) -> bytes: ...
```

`dumps()` serializes Python objects to JSON.

It natively serializes
`str`, `dict`, `list`, `tuple`, `int`, `float`, `bool`, `None`,
`dataclasses.dataclass`, `typing.TypedDict`, `datetime.datetime`,
`datetime.date`, `datetime.time`, `uuid.UUID`, `numpy.ndarray`, and
`orjson.Fragment` instances. It supports arbitrary types through `default`. It
serializes subclasses of `str`, `int`, `dict`, `list`,
`dataclasses.dataclass`, and `enum.Enum`. It does not serialize subclasses
of `tuple` to avoid serializing `namedtuple` objects as arrays. To avoid
serializing subclasses, specify the option `orjson.OPT_PASSTHROUGH_SUBCLASS`.

The output is a `bytes` object containing UTF-8.

The global interpreter lock (GIL) is held for the duration of the call.

It raises `JSONEncodeError` on an unsupported type. This exception message
describes the invalid object with the error message
`Type is not JSON serializable: ...`. To fix this, specify
[default](https://github.com/ijl/orjson?tab=readme-ov-file#default).

It raises `JSONEncodeError` on a `str` that contains invalid UTF-8.

It raises `JSONEncodeError` on an integer that exceeds 64 bits by default or,
with `OPT_STRICT_INTEGER`, 53 bits.

It raises `JSONEncodeError` if a `dict` has a key of a type other than `str`,
unless `OPT_NON_STR_KEYS` is specified.

It raises `JSONEncodeError` if the output of `default` recurses to handling by
`default` more than 254 levels deep.

It raises `JSONEncodeError` on circular references.

It raises `JSONEncodeError`  if a `tzinfo` on a datetime object is
unsupported.

`JSONEncodeError` is a subclass of `TypeError`. This is for compatibility
with the standard library.

If the failure was caused by an exception in `default` then
`JSONEncodeError` chains the original exception as `__cause__`.

#### default

To serialize a subclass or arbitrary types, specify `default` as a
callable that returns a supported type. `default` may be a function,
lambda, or callable class instance. To specify that a type was not
handled by `default`, raise an exception such as `TypeError`.

```python
>>> import orjson, decimal
>>>
def default(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)
    raise TypeError

>>> orjson.dumps(decimal.Decimal("0.0842389659712649442845"))
JSONEncodeError: Type is not JSON serializable: decimal.Decimal
>>> orjson.dumps(decimal.Decimal("0.0842389659712649442845"), default=default)
b'"0.0842389659712649442845"'
>>> orjson.dumps({1, 2}, default=default)
orjson.JSONEncodeError: Type is not JSON serializable: set
```

The `default` callable may return an object that itself
must be handled by `default` up to 254 times before an exception
is raised.

It is important that `default` raise an exception if a type cannot be handled.
Python otherwise implicitly returns `None`, which appears to the caller
like a legitimate value and is serialized:

```python
>>> import orjson, json
>>>
def default(obj):
    if isinstance(obj, decimal.Decimal):
        return str(obj)

>>> orjson.dumps({"set":{1, 2}}, default=default)
b'{"set":null}'
>>> json.dumps({"set":{1, 2}}, default=default)
'{"set":null}'
```

#### option

To modify how data is serialized, specify `option`. Each `option` is an integer
constant in `orjson`. To specify multiple options, mask them together, e.g.,
`option=orjson.OPT_STRICT_INTEGER | orjson.OPT_NAIVE_UTC`.

##### OPT_APPEND_NEWLINE

Append `\n` to the output. This is a convenience and optimization for the
pattern of `dumps(...) + "\n"`. `bytes` objects are immutable and this
pattern copies the original contents.

```python
>>> import orjson
>>> orjson.dumps([])
b"[]"
>>> orjson.dumps([], option=orjson.OPT_APPEND_NEWLINE)
b"[]\n"
```

##### OPT_INDENT_2

Pretty-print output with an indent of two spaces. This is equivalent to
`indent=2` in the standard library. Pretty printing is slower and the output
larger. This option is compatible with all other options.

```python
>>> import orjson
>>> orjson.dumps({"a": "b", "c": {"d": True}, "e": [1, 2]})
b'{"a":"b","c":{"d":true},"e":[1,2]}'
>>> orjson.dumps(
    {"a": "b", "c": {"d": True}, "e": [1, 2]},
    option=orjson.OPT_INDENT_2
)
b'{\n  "a": "b",\n  "c": {\n    "d": true\n  },\n  "e": [\n    1,\n    2\n  ]\n}'
```

If displayed, the indentation and linebreaks appear like this:

```json
{
  "a": "b",
  "c": {
    "d": true
  },
  "e": [
    1,
    2
  ]
}
```

This measures serializing the github.json fixture as compact (52KiB) or
pretty (64KiB):

| Library   |   compact (ms) |   pretty (ms) |   vs. orjson |
|-----------|----------------|---------------|--------------|
| orjson    |           0.01 |          0.02 |            1 |
| json      |           0.13 |          0.54 |           34 |

This measures serializing the citm_catalog.json fixture, more of a worst
case due to the amount of nesting and newlines, as compact (489KiB) or
pretty (1.1MiB):

| Library   |   compact (ms) |   pretty (ms) |   vs. orjson |
|-----------|----------------|---------------|--------------|
| orjson    |           0.25 |          0.45 |          1   |
| json      |           3.01 |         24.42 |         54.4 |

This can be reproduced using the `pyindent` script.

##### OPT_NAIVE_UTC

Serialize `datetime.datetime` objects without a `tzinfo` as UTC. This
has no effect on `datetime.datetime` objects that have `tzinfo` set.

```python
>>> import orjson, datetime
>>> orjson.dumps(
        datetime.datetime(1970, 1, 1, 0, 0, 0),
    )
b'"1970-01-01T00:00:00"'
>>> orjson.dumps(
        datetime.datetime(1970, 1, 1, 0, 0, 0),
        option=orjson.OPT_NAIVE_UTC,
    )
b'"1970-01-01T00:00:00+00:00"'
```

##### OPT_NON_STR_KEYS

Serialize `dict` keys of type other than `str`. This allows `dict` keys
to be one of `str`, `int`, `float`, `bool`, `None`, `datetime.datetime`,
`datetime.date`, `datetime.time`, `enum.Enum`, and `uuid.UUID`. For comparison,
the standard library serializes `str`, `int`, `float`, `bool` or `None` by
default. orjson benchmarks as being faster at serializing non-`str` keys
than other libraries. This option is slower for `str` keys than the default.

```python
>>> import orjson, datetime, uuid
>>> orjson.dumps(
        {uuid.UUID("7202d115-7ff3-4c81-a7c1-2a1f067b1ece"): [1, 2, 3]},
        option=orjson.OPT_NON_STR_KEYS,
    )
b'{"7202d115-7ff3-4c81-a7c1-2a1f067b1ece":[1,2,3]}'
>>> orjson.dumps(
        {datetime.datetime(1970, 1, 1, 0, 0, 0): [1, 2, 3]},
        option=orjson.OPT_NON_STR_KEYS | orjson.OPT_NAIVE_UTC,
    )
b'{"1970-01-01T00:00:00+00:00":[1,2,3]}'
```

These types are generally serialized how they would be as
values, e.g., `datetime.datetime` is still an RFC 3339 string and respects
options affecting it. The exception is that `int` serialization does not
respect `OPT_STRICT_INTEGER`.

This option has the risk of creating duplicate keys. This is because non-`str`
objects may serialize to the same `str` as an existing key, e.g.,
`{"1": true, 1: false}`. The last key to be inserted to the `dict` will be
serialized last and a JSON deserializer will presumably take the last
occurrence of a key (in the above, `false`). The first value will be lost.

This option is compatible with `orjson.OPT_SORT_KEYS`. If sorting is used,
note the sort is unstable and will be unpredictable for duplicate keys.

```python
>>> import orjson, datetime
>>> orjson.dumps(
    {"other": 1, datetime.date(1970, 1, 5): 2, datetime.date(1970, 1, 3): 3},
    option=orjson.OPT_NON_STR_KEYS | orjson.OPT_SORT_KEYS
)
b'{"1970-01-03":3,"1970-01-05":2,"other":1}'
```

This measures serializing 589KiB of JSON comprising a `list` of 100 `dict`
in which each `dict` has both 365 randomly-sorted `int` keys representing epoch
timestamps as well as one `str` key and the value for each key is a
single integer. In "str keys", the keys were converted to `str` before
serialization, and orjson still specifes `option=orjson.OPT_NON_STR_KEYS`
(which is always somewhat slower).

| Library   |   str keys (ms) |   int keys (ms) | int keys sorted (ms)   |
|-----------|-----------------|-----------------|------------------------|
| orjson    |            0.5  |            0.93 | 2.08                   |
| json      |            2.72 |            3.59 |                        |

json is blank because it
raises `TypeError` on attempting to sort before converting all keys to `str`.
This can be reproduced using the `pynonstr` script.

##### OPT_OMIT_MICROSECONDS

Do not serialize the `microsecond` field on `datetime.datetime` and
`datetime.time` instances.

```python
>>> import orjson, datetime
>>> orjson.dumps(
        datetime.datetime(1970, 1, 1, 0, 0, 0, 1),
    )
b'"1970-01-01T00:00:00.000001"'
>>> orjson.dumps(
        datetime.datetime(1970, 1, 1, 0, 0, 0, 1),
        option=orjson.OPT_OMIT_MICROSECONDS,
    )
b'"1970-01-01T00:00:00"'
```

##### OPT_PASSTHROUGH_DATACLASS

Passthrough `dataclasses.dataclass` instances to `default`. This allows
customizing their output but is much slower.


```python
>>> import orjson, dataclasses
>>>
@dataclasses.dataclass
class User:
    id: str
    name: str
    password: str

def default(obj):
    if isinstance(obj, User):
        return {"id": obj.id, "name": obj.name}
    raise TypeError

>>> orjson.dumps(User("3b1", "asd", "zxc"))
b'{"id":"3b1","name":"asd","password":"zxc"}'
>>> orjson.dumps(User("3b1", "asd", "zxc"), option=orjson.OPT_PASSTHROUGH_DATACLASS)
TypeError: Type is not JSON serializable: User
>>> orjson.dumps(
        User("3b1", "asd", "zxc"),
        option=orjson.OPT_PASSTHROUGH_DATACLASS,
        default=default,
    )
b'{"id":"3b1","name":"asd"}'
```

##### OPT_PASSTHROUGH_DATETIME

Passthrough `datetime.datetime`, `datetime.date`, and `datetime.time` instances
to `default`. This allows serializing datetimes to a custom format, e.g.,
HTTP dates:

```python
>>> import orjson, datetime
>>>
def default(obj):
    if isinstance(obj, datetime.datetime):
        return obj.strftime("%a, %d %b %Y %H:%M:%S GMT")
    raise TypeError

>>> orjson.dumps({"created_at": datetime.datetime(1970, 1, 1)})
b'{"created_at":"1970-01-01T00:00:00"}'
>>> orjson.dumps({"created_at": datetime.datetime(1970, 1, 1)}, option=orjson.OPT_PASSTHROUGH_DATETIME)
TypeError: Type is not JSON serializable: datetime.datetime
>>> orjson.dumps(
        {"created_at": datetime.datetime(1970, 1, 1)},
        option=orjson.OPT_PASSTHROUGH_DATETIME,
        default=default,
    )
b'{"created_at":"Thu, 01 Jan 1970 00:00:00 GMT"}'
```

This does not affect datetimes in `dict` keys if using OPT_NON_STR_KEYS.

##### OPT_PASSTHROUGH_SUBCLASS

Passthrough subclasses of builtin types to `default`.

```python
>>> import orjson
>>>
class Secret(str):
    pass

def default(obj):
    if isinstance(obj, Secret):
        return "******"
    raise TypeError

>>> orjson.dumps(Secret("zxc"))
b'"zxc"'
>>> orjson.dumps(Secret("zxc"), option=orjson.OPT_PASSTHROUGH_SUBCLASS)
TypeError: Type is not JSON serializable: Secret
>>> orjson.dumps(Secret("zxc"), option=orjson.OPT_PASSTHROUGH_SUBCLASS, default=default)
b'"******"'
```

This does not affect serializing subclasses as `dict` keys if using
OPT_NON_STR_KEYS.

##### OPT_SERIALIZE_DATACLASS

This is deprecated and has no effect in version 3. In version 2 this was
required to serialize  `dataclasses.dataclass` instances. For more, see
[dataclass](https://github.com/ijl/orjson?tab=readme-ov-file#dataclass).

##### OPT_SERIALIZE_NUMPY

Serialize `numpy.ndarray` instances. For more, see
[numpy](https://github.com/ijl/orjson?tab=readme-ov-file#numpy).

##### OPT_SERIALIZE_UUID

This is deprecated and has no effect in version 3. In version 2 this was
required to serialize `uuid.UUID` instances. For more, see
[UUID](https://github.com/ijl/orjson?tab=readme-ov-file#UUID).

##### OPT_SORT_KEYS

Serialize `dict` keys in sorted order. The default is to serialize in an
unspecified order. This is equivalent to `sort_keys=True` in the standard
library.

This can be used to ensure the order is deterministic for hashing or tests.
It has a substantial performance penalty and is not recommended in general.

```python
>>> import orjson
>>> orjson.dumps({"b": 1, "c": 2, "a": 3})
b'{"b":1,"c":2,"a":3}'
>>> orjson.dumps({"b": 1, "c": 2, "a": 3}, option=orjson.OPT_SORT_KEYS)
b'{"a":3,"b":1,"c":2}'
```

This measures serializing the twitter.json fixture unsorted and sorted:

| Library   |   unsorted (ms) |   sorted (ms) |   vs. orjson |
|-----------|-----------------|---------------|--------------|
| orjson    |            0.11 |          0.3  |          1   |
| json      |            1.36 |          1.93 |          6.4 |

The benchmark can be reproduced using the `pysort` script.

The sorting is not collation/locale-aware:

```python
>>> import orjson
>>> orjson.dumps({"a": 1, "ä": 2, "A": 3}, option=orjson.OPT_SORT_KEYS)
b'{"A":3,"a":1,"\xc3\xa4":2}'
```

This is the same sorting behavior as the standard library.

`dataclass` also serialize as maps but this has no effect on them.

##### OPT_STRICT_INTEGER

Enforce 53-bit limit on integers. The limit is otherwise 64 bits, the same as
the Python standard library. For more, see [int](https://github.com/ijl/orjson?tab=readme-ov-file#int).

##### OPT_UTC_Z

Serialize a UTC timezone on `datetime.datetime` instances as `Z` instead
of `+00:00`.

```python
>>> import orjson, datetime, zoneinfo
>>> orjson.dumps(
        datetime.datetime(1970, 1, 1, 0, 0, 0, tzinfo=zoneinfo.ZoneInfo("UTC")),
    )
b'"1970-01-01T00:00:00+00:00"'
>>> orjson.dumps(
        datetime.datetime(1970, 1, 1, 0, 0, 0, tzinfo=zoneinfo.ZoneInfo("UTC")),
        option=orjson.OPT_UTC_Z
    )
b'"1970-01-01T00:00:00Z"'
```

#### Fragment

`orjson.Fragment` includes already-serialized JSON in a document. This is an
efficient way to include JSON blobs from a cache, JSONB field, or separately
serialized object without first deserializing to Python objects via `loads()`.

```python
>>> import orjson
>>> orjson.dumps({"key": "zxc", "data": orjson.Fragment(b'{"a": "b", "c": 1}')})
b'{"key":"zxc","data":{"a": "b", "c": 1}}'
```

It does no reformatting: `orjson.OPT_INDENT_2` will not affect a
compact blob nor will a pretty-printed JSON blob be rewritten as compact.

The input must be `bytes` or `str` and given as a positional argument.

This raises `orjson.JSONEncodeError` if a `str` is given and the input is
not valid UTF-8. It otherwise does no validation and it is possible to
write invalid JSON. This does not escape characters. The implementation is
tested to not crash if given invalid strings or invalid JSON.

### Deserialize

```python
def loads(__obj: Union[bytes, bytearray, memoryview, str]) -> Any: ...
```

`loads()` deserializes JSON to Python objects. It deserializes to `dict`,
`list`, `int`, `float`, `str`, `bool`, and `None` objects.

`bytes`, `bytearray`, `memoryview`, and `str` input are accepted. If the input
exists as a `memoryview`, `bytearray`, or `bytes` object, it is recommended to
pass these directly rather than creating an unnecessary `str` object. That is,
`orjson.loads(b"{}")` instead of `orjson.loads(b"{}".decode("utf-8"))`. This
has lower memory usage and lower latency.

The input must be valid UTF-8.

orjson maintains a cache of map keys for the duration of the process. This
causes a net reduction in memory usage by avoiding duplicate strings. The
keys must be at most 64 bytes to be cached and 2048 entries are stored.

The global interpreter lock (GIL) is held for the duration of the call.

It raises `JSONDecodeError` if given an invalid type or invalid
JSON. This includes if the input contains `NaN`, `Infinity`, or `-Infinity`,
which the standard library allows, but is not valid JSON.

It raises `JSONDecodeError` if a combination of array or object recurses
1024 levels deep.

It raises `JSONDecodeError` if unable to allocate a buffer large enough
to parse the document.

`JSONDecodeError` is a subclass of `json.JSONDecodeError` and `ValueError`.
This is for compatibility with the standard library.

## Types

### dataclass

orjson serializes instances of `dataclasses.dataclass` natively. It serializes
instances 40-50x as fast as other libraries and avoids a severe slowdown seen
in other libraries compared to serializing `dict`.

It is supported to pass all variants of dataclasses, including dataclasses
using `__slots__`, frozen dataclasses, those with optional or default
attributes, and subclasses. There is a performance benefit to not
using `__slots__`.

| Library   |   dict (ms) |   dataclass (ms) |   vs. orjson |
|-----------|-------------|------------------|--------------|
| orjson    |        0.43 |             0.95 |            1 |
| json      |        5.81 |            38.32 |           40 |

This measures serializing 555KiB of JSON, orjson natively and other libraries
using `default` to serialize the output of `dataclasses.asdict()`. This can be
reproduced using the `pydataclass` script.

Dataclasses are serialized as maps, with every attribute serialized and in
the order given on class definition:

```python
>>> import dataclasses, orjson, typing

@dataclasses.dataclass
class Member:
    id: int
    active: bool = dataclasses.field(default=False)

@dataclasses.dataclass
class Object:
    id: int
    name: str
    members: typing.List[Member]

>>> orjson.dumps(Object(1, "a", [Member(1, True), Member(2)]))
b'{"id":1,"name":"a","members":[{"id":1,"active":true},{"id":2,"active":false}]}'
```

### datetime

orjson serializes `datetime.datetime` objects to
[RFC 3339](https://tools.ietf.org/html/rfc3339) format,
e.g., "1970-01-01T00:00:00+00:00". This is a subset of ISO 8601 and is
compatible with `isoformat()` in the standard library.

```python
>>> import orjson, datetime, zoneinfo
>>> orjson.dumps(
    datetime.datetime(2018, 12, 1, 2, 3, 4, 9, tzinfo=zoneinfo.ZoneInfo("Australia/Adelaide"))
)
b'"2018-12-01T02:03:04.000009+10:30"'
>>> orjson.dumps(
    datetime.datetime(2100, 9, 1, 21, 55, 2).replace(tzinfo=zoneinfo.ZoneInfo("UTC"))
)
b'"2100-09-01T21:55:02+00:00"'
>>> orjson.dumps(
    datetime.datetime(2100, 9, 1, 21, 55, 2)
)
b'"2100-09-01T21:55:02"'
```

`datetime.datetime` supports instances with a `tzinfo` that is `None`,
`datetime.timezone.utc`, a timezone instance from the standard library `zoneinfo`
module, or a timezone instance from the third-party `pendulum`, `pytz`, or
`dateutil`/`arrow` libraries.

It is fastest to use the standard library's `zoneinfo.ZoneInfo` for timezones.

`datetime.time` objects must no
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `bench/__init__.py`
```python

```

#### File: `test/__init__.py`
```python

```

#### File: `data/parsing/n_structure_no_data.json`
```python

```

#### File: `data/parsing/n_single_space.json`
```python

```

#### File: `data/parsing/n_structure_single_eacute.json`
```python

```

#### File: `data/parsing/n_structure_single_star.json`
```python
*
```


==================================================


## [3/3] Repository: pandas-market-calendars (`WHEEL_pandas-market-calendars`)
- **Full Name**: `pandas-market-calendars`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
pandas_market_calendars
=======================
Market calendars to use with pandas for trading applications.

.. image:: https://badge.fury.io/py/pandas-market-calendars.svg
    :target: https://badge.fury.io/py/pandas-market-calendars

.. image:: https://readthedocs.org/projects/pandas-market-calendars/badge/?version=latest
   :target: http://pandas-market-calendars.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://coveralls.io/repos/github/rsheftel/pandas_market_calendars/badge.svg?branch=master
    :target: https://coveralls.io/github/rsheftel/pandas_market_calendars?branch=master

Documentation
-------------
http://pandas-market-calendars.readthedocs.io/en/latest/

Overview
--------
The Pandas package is widely used in finance and specifically for time series analysis. It includes excellent
functionality for generating sequences of dates and capabilities for custom holiday calendars, but as an explicit
design choice it does not include the actual holiday calendars for specific exchanges or OTC markets.

The pandas_market_calendars package looks to fill that role with the holiday, late open and early close calendars
for specific exchanges and OTC conventions. pandas_market_calendars also adds several functions to manipulate the
market calendars and includes a date_range function to create a pandas DatetimeIndex including only the datetimes
when the markets are open. Additionally the package contains product specific calendars for future exchanges which
have different market open, closes, breaks and holidays based on product type.

This package provides access to over 50+ unique exchange calendars for global equity and futures markets.

Calendar Data and Updates
~~~~~~~~~~~~~~~~~~~~~~~~~
Calendars and their rules are shipped as package code. pandas_market_calendars does not request market hours from a
server at runtime. To receive corrected or updated market hours, install a newer package release or update the source
code. Calendars mirrored from ``exchange_calendars`` likewise use the version installed in the local Python environment,
not a live data feed.

This package is a fork of the Zipline package from Quantopian and extracts just the relevant parts. All credit for
their excellent work to Quantopian.

Major Releases
~~~~~~~~~~~~~~
As of v1.0 this package only works with Python3. This is consistent with Pandas dropping support for Python2.

As of v1.4 this package now has the concept of a break during the trading day. For example this can accommodate Asian
markets that have a lunch break, or futures markets that are open 24 hours with a break in the day for trade processing.

As of v2.0 this package provides a mirror of all the calendars from the `exchange_calendars <https://github.com/gerrymanoim/exchange_calendars>`_
package, which itself is the now maintained fork of the original trading_calendars package. This adds over 50 calendars.

As of v3.0, the function date_range() is more complete and consistent, for more discussion on the topic refer to PR #142 and Issue #138.

As of v4.0, this package provides the framework to add interruptions to calendars. These can also be added to a schedule and viewed using
the new interruptions_df property. A full list of changes can be found in PR #210.

As of v5.0, this package uses the new zoneinfo standard to timezones and depricates and removes pytz. Minimum python version is now 3.9

Source location
~~~~~~~~~~~~~~~
Hosted on GitHub: https://github.com/rsheftel/pandas_market_calendars

Installation
~~~~~~~~~~~~
``pip install pandas_market_calendars``

Arch Linux package available here: https://aur.archlinux.org/packages/python-pandas_market_calendars/

Calendars
---------
The list of `available calendars <https://pandas-market-calendars.readthedocs.io/en/latest/calendars.html>`_

Quick Start
-----------
.. code:: python

    import pandas_market_calendars as mcal
    
    # Create a calendar
    nyse = mcal.get_calendar('NYSE')

    # Show available calendars
    print(mcal.get_calendar_names())

.. code:: python

    early = nyse.schedule(start_date='2012-07-01', end_date='2012-07-10')
    early

    
.. parsed-literal::

                      market_open             market_close
    =========== ========================= =========================
     2012-07-02 2012-07-02 13:30:00+00:00 2012-07-02 20:00:00+00:00
     2012-07-03 2012-07-03 13:30:00+00:00 2012-07-03 17:00:00+00:00
     2012-07-05 2012-07-05 13:30:00+00:00 2012-07-05 20:00:00+00:00
     2012-07-06 2012-07-06 13:30:00+00:00 2012-07-06 20:00:00+00:00
     2012-07-09 2012-07-09 13:30:00+00:00 2012-07-09 20:00:00+00:00
     2012-07-10 2012-07-10 13:30:00+00:00 2012-07-10 20:00:00+00:00

    
.. code:: python

    mcal.date_range(early, frequency='1D')




.. parsed-literal::

    DatetimeIndex(['2012-07-02 20:00:00+00:00', '2012-07-03 17:00:00+00:00',
                   '2012-07-05 20:00:00+00:00', '2012-07-06 20:00:00+00:00',
                   '2012-07-09 20:00:00+00:00', '2012-07-10 20:00:00+00:00'],
                  dtype='datetime64[ns, UTC]', freq=None)



.. code:: python

    mcal.date_range(early, frequency='1H')




.. parsed-literal::

    DatetimeIndex(['2012-07-02 14:30:00+00:00', '2012-07-02 15:30:00+00:00',
                   '2012-07-02 16:30:00+00:00', '2012-07-02 17:30:00+00:00',
                   '2012-07-02 18:30:00+00:00', '2012-07-02 19:30:00+00:00',
                   '2012-07-02 20:00:00+00:00', '2012-07-03 14:30:00+00:00',
                   '2012-07-03 15:30:00+00:00', '2012-07-03 16:30:00+00:00',
                   '2012-07-03 17:00:00+00:00', '2012-07-05 14:30:00+00:00',
                   '2012-07-05 15:30:00+00:00', '2012-07-05 16:30:00+00:00',
                   '2012-07-05 17:30:00+00:00', '2012-07-05 18:30:00+00:00',
                   '2012-07-05 19:30:00+00:00', '2012-07-05 20:00:00+00:00',
                   '2012-07-06 14:30:00+00:00', '2012-07-06 15:30:00+00:00',
                   '2012-07-06 16:30:00+00:00', '2012-07-06 17:30:00+00:00',
                   '2012-07-06 18:30:00+00:00', '2012-07-06 19:30:00+00:00',
                   '2012-07-06 20:00:00+00:00', '2012-07-09 14:30:00+00:00',
                   '2012-07-09 15:30:00+00:00', '2012-07-09 16:30:00+00:00',
                   '2012-07-09 17:30:00+00:00', '2012-07-09 18:30:00+00:00',
                   '2012-07-09 19:30:00+00:00', '2012-07-09 20:00:00+00:00',
                   '2012-07-10 14:30:00+00:00', '2012-07-10 15:30:00+00:00',
                   '2012-07-10 16:30:00+00:00', '2012-07-10 17:30:00+00:00',
                   '2012-07-10 18:30:00+00:00', '2012-07-10 19:30:00+00:00',
                   '2012-07-10 20:00:00+00:00'],
                  dtype='datetime64[ns, UTC]', freq=None)

Contributing
------------
All improvements and additional (and corrections) in the form of pull requests are welcome. This package will grow in
value and correctness the more eyes are on it.

To add new functionality please include tests which are in standard pytest format. 

Use pytest to run the test suite.

Use black for formatting.

For complete information on contributing see CONTRIBUTING.md_

.. _CONTRIBUTING.md: https://github.com/rsheftel/pandas_market_calendars/blob/master/CONTRIBUTING.md

Future
------
This package is open sourced under the MIT license. Everyone is welcome to add more exchanges or OTC markets, confirm
or correct the existing calendars, and generally do whatever they desire with this code.

### Core Implementation Code & Architecture
#### File: `pandas_market_calendars/calendars/__init__.py`
```python

```

#### File: `pandas_market_calendars/holidays/__init__.py`
```python

```

#### File: `tests/__init__.py`
```python

```

#### File: `pandas_market_calendars/calendars/cme_market_times.py`
```python
from datetime import time


GRAINS_AND_OILSEEDS_MARKET_TIMES = {
    "market_open": ((None, time(19), -1),),  # offset by -1 day
    "market_close": ((None, time(13, 20)),),
    "break_start": ((None, time(7, 45)),),
    "break_end": ((None, time(8, 30)),),
}
```

#### File: `tests/test_24_7_calendar.py`
```python
import pandas as pd
from pandas.testing import assert_index_equal

import pandas_market_calendars as mcal


def test_weekends():
    actual = mcal.get_calendar("24/7").schedule("2012-07-01", "2012-07-10").index

    expected = pd.DatetimeIndex(
        [
            pd.Timestamp("2012-07-01"),
            pd.Timestamp("2012-07-02"),
            pd.Timestamp("2012-07-03"),
            pd.Timestamp("2012-07-04"),
            pd.Timestamp("2012-07-05"),
            pd.Timestamp("2012-07-06"),
            pd.Timestamp("2012-07-07"),
            pd.Timestamp("2012-07-08"),
            pd.Timestamp("2012-07-09"),
            pd.Timestamp("2012-07-10"),
        ]
    )

    assert_index_equal(actual, expected)
```

#### File: `tests/test_exchange_calendar_cme_globex_grains.py`
```python
from zoneinfo import ZoneInfo

from pandas_market_calendars.calendars.cme_globex_agriculture import (
    CMEGlobexGrainsAndOilseedsExchangeCalendar,
)


cal = CMEGlobexGrainsAndOilseedsExchangeCalendar()


def test_time_zone():
    assert cal.tz == ZoneInfo("America/Chicago")
    assert cal.name == "CMEGlobex_GrainsAndOilseeds"


def test_x():
    schedule = cal.schedule("2023-01-01", "2023-01-10", tz="America/New_York")

    good_dates = cal.valid_days("2023-01-01", "2023-12-31")

    assert all(d not in good_dates for d in {"2023-01-01", "2023-12-24", "2023-12-25", "2023-12-30", "2023-12-31"})

    assert all(d in good_dates for d in {"2023-01-03", "2023-01-05", "2023-12-26", "2023-12-27", "2023-12-28"})
```


==================================================
