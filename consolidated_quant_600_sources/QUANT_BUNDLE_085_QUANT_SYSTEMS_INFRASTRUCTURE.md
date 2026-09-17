# ⚡ [QUANT-SOURCE-085] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_085_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: tradeapp (`WHEEL_tradeapp`)
- **Full Name**: `tradeapp`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# tradeapp

### Core Implementation Code & Architecture
#### File: `__init__.py`
```python

```

#### File: `src/__init__.py`
```python

```

#### File: `src/Dependencies/__init__.py`
```python

```

#### File: `src/utils/__init__.py`
```python

```

#### File: `src/models/__init__.py`
```python

```

#### File: `src/schemas/__init__.py`
```python

```


==================================================


## [2/3] Repository: tsfresh (`WHEEL_tsfresh`)
- **Full Name**: `tsfresh`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<div align="center">
  <img width="70%" src="./docs/images/tsfresh_logo.svg">
</div>

-----------------

# tsfresh

[![Documentation Status](https://readthedocs.org/projects/tsfresh/badge/?version=latest)](https://tsfresh.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://github.com/blue-yonder/tsfresh/workflows/Test%20Default%20Branch/badge.svg)](https://github.com/blue-yonder/tsfresh/actions)
[![codecov](https://codecov.io/gh/blue-yonder/tsfresh/branch/main/graph/badge.svg)](https://codecov.io/gh/blue-yonder/tsfresh)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg)](https://github.com/blue-yonder/tsfresh/blob/main/LICENSE.txt)
[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/blue-yonder/tsfresh/main?filepath=notebooks)
[![Downloads](https://pepy.tech/badge/tsfresh)](https://pepy.tech/project/tsfresh)

This repository contains the *TSFRESH* python package. The abbreviation stands for

*"Time Series Feature extraction based on scalable hypothesis tests"*.

The package provides systematic time-series feature extraction by combining established algorithms from statistics, time-series analysis, signal processing, and nonlinear dynamics with a robust feature selection algorithm. In this context, the term *time-series* is interpreted in the broadest possible sense, such that any types of sampled data or even event sequences can be characterised.

## Spend less time on feature engineering

Data Scientists often spend most of their time either cleaning data or building features.
While we cannot change the first thing, the second can be automated.
*TSFRESH* frees your time spent on building features by extracting them automatically.
Hence, you have more time to study the newest deep learning paper, read hacker news or build better models.


## Automatic extraction of 100s of features

*TSFRESH* automatically extracts 100s of features from time series.
Those features describe basic characteristics of the time series such as the number of peaks, the average or maximal value or more complex features such as the time reversal symmetry statistic.

![The features extracted from a exemplary time series](docs/images/introduction_ts_exa_features.png)

The set of features can then be used to construct statistical or machine learning models on the time series to be used for example in regression or
classification tasks.

## Forget irrelevant features

Time series often contain noise, redundancies or irrelevant information.
As a result most of the extracted features will not be useful for the machine learning task at hand.

To avoid extracting irrelevant features, the *TSFRESH* package has a built-in filtering procedure.
This filtering procedure evaluates the explaining power and importance of each characteristic for the regression or classification tasks at hand.

It is based on the well developed theory of hypothesis testing and uses a multiple test procedure.
As a result the filtering process mathematically controls the percentage of irrelevant extracted features.

The  *TSFRESH* package is described in the following open access paper:

* Christ, M., Braun, N., Neuffer, J., and Kempa-Liehr A.W. (2018).
   _Time Series FeatuRe Extraction on basis of Scalable Hypothesis tests (tsfresh -- A Python package)._
   Neurocomputing 307, p. 72-77, [doi: 10.1016/j.neucom.2018.03.067](https://doi.org/10.1016/j.neucom.2018.03.067).

The FRESH algorithm is described in the following whitepaper:

* Christ, M., Kempa-Liehr, A.W., and Feindt, M. (2017).
    _Distributed and parallel time series feature extraction for industrial big data applications._
    ArXiv e-print 1610.07717,  [https://arxiv.org/abs/1610.07717](https://arxiv.org/abs/1610.07717).

Normality models simulate how humans detect time-series anomalies:

* Teh, H.Y., Wang, K.I-K., Kempa-Liehr, A.W. (2021).
    _Expect the Unexpected: Unsupervised feature selection for automated sensor anomaly detection._
    IEEE Sensors Journal 15.16, p. 18033-18046, [doi: 10.1109/JSEN.2021.3084970](https://doi.org/10.1109/JSEN.2021.3084970).

* Teh, H.Y., Wang, K.I-K., Kempa-Liehr, A.W. (2025).
    _Feature-based normality models for anomaly detection._
    Sensors 25.4757, p. 1-25, [doi: 10.3390/s25154757](https://doi.org/10.3390/s25154757).
  
Systematic time-series feature extraction even works for unsupervised problems:

* Abrasaldo, P.M., Zarrouk, S.J., Kempa-Liehr, A.W. (2026).
  _Feature-Based Time Series Clustering for Efficient Labeling of Geothermal Data._
  Geothermics 138.103656, p. 1–13, [doi: 10.1016/j.geothermics.2026.103656](https://doi.org/10.1016/j.geothermics.2026.103656)

Due to the fact that tsfresh basically provides time-series feature extraction for free, you can now concentrate on engineering new time-series,
like e.g. differences of signals from synchronous measurements, which provide even better time-series features:

* Kempa-Liehr, A.W., Oram, J., Wong, A., Finch, M., Besier, T. (2020).
    _Feature engineering workflow for activity recognition from synchronized inertial measurement units._
    In: Pattern Recognition. ACPR 2019. Ed. by M. Cree et al. Vol. 1180. Communications in Computer and Information Science (CCIS).
    Singapore: Springer, p. 223–231. [doi: 10.1007/978-981-15-3651-9_20](https://doi.org/10.1007/978-981-15-3651-9_20).

* Simmons, S., Jarvis, L., Dempsey, D., Kempa-Liehr, A.W. (2021).
    _Data Mining on Extremely Long Time-Series._
    In: 2021 International Conference on Data Mining Workshops (ICDMW). Ed. by B. Xue et al.
    Los Alamitos: IEEE, p. 1057-1066. [doi: 10.1109/ICDMW53433.2021.00137](https://doi.org/10.1109/ICDMW53433.2021.00137).

Systematic time-series features engineering allows to work with time-series samples of different lengths, because every time-series is projected
into a well-defined feature space. This approach allows the design of robust machine learning algorithms in applications with missing data.

* Kennedy, A., Gemma, N., Rattenbury, N., Kempa-Liehr, A.W. (2021).
    _Modelling the projected separation of microlensing events using systematic time-series feature engineering._
    Astronomy and Computing 35.100460, p. 1–14, [doi: 10.1016/j.ascom.2021.100460](https://doi.org/10.1016/j.ascom.2021.100460)

Is your time-series classification problem imbalanced? There is a good chance that undersampling of time-series feature matrices
might solve your problem:

* Dempsey, D.E., Cronin, S.J., Mei, S., Kempa-Liehr, A.W. (2020).
    _Automatic precursor recognition and real-time forecasting of sudden explosive volcanic eruptions at Whakaari, New Zealand_.
    Nature Communications 11.3562, p. 1-8, [doi: 10.1038/s41467-020-17375-2](https://doi.org/10.1038/s41467-020-17375-2).

You are not working with time-series, but with 2D and 3D images? Spatial variation sequences (SVS) are an excellent application for tsfresh:

* Jeune, H., Pechan, N., Reitsma, S., Kempa-Liehr, A.W. (2021).
    _Spatial Variation Sequences for Remote Sensing Applications with Small Sample Sizes._
    In: 2024 Image and Video Technology. 11th Pacific-Rim Symposium, Ed. by W.Q. Yan et al.,
    Lecture Notes in Computer Science (14403). Springer Nature: Singapore, p. 153-166. [doi: {10.1007/978-981-97-0376-0_12](https://doi.org/{10.1007/978-981-97-0376-0_12).

* Koptev, I., Tian, J., Peel, E., Parker, R., Walker, C., Kempa-Liehr, A.W. (2025).
    _Interpretable Dimensionality Reduction in 3D Image Recognition with Small Sample Sizes_.
    Journal of Nondestructive Evaluation 44.44, p. 1-12, [doi: 10.1007/s10921-025-01183-z](https://doi.org/10.1007/s10921-025-01183-z).

Natural language processing of written texts is an example of applying systematic time-series feature engineering to event sequences,
which is described in the following open access paper:

* Tang, Y., Blincoe, K., Kempa-Liehr, A.W. (2020).
    _Enriching Feature Engineering for Short Text Samples by Language Time Series Analysis._
    EPJ Data Science 9.26, p. 1–59. [doi: 10.1140/epjds/s13688-020-00244-9](https://doi.org/10.1140/epjds/s13688-020-00244-9)



## Advantages of tsfresh

*TSFRESH* has several selling points, for example

1. it is field tested
2. it is unit tested
3. the filtering process is statistically/mathematically correct
4. it has a comprehensive documentation
5. it is compatible with sklearn, pandas and numpy
6. it allows anyone to easily add their favorite features
7. it both runs on your local machine or even on a cluster

## Next steps

If you are interested in the technical workings, go to see our comprehensive Read-The-Docs documentation at [http://tsfresh.readthedocs.io](http://tsfresh.readthedocs.io).

The algorithm, especially the filtering part are also described in the paper mentioned above.

We appreciate any contributions, if you are interested in helping us to make *TSFRESH* the biggest archive of feature extraction methods in python, just head over to our [How-To-Contribute](http://tsfresh.readthedocs.io/en/latest/text/how_to_contribute.html) instructions.

If you want to try out `tsfresh` quickly or if you want to integrate it into your workflow, we also have a docker image available:

    docker pull nbraun/tsfresh


## Backwards compatibility

If you need to reproduce or update time-series features, which were computed with the `matrixprofile` feature calculators, you need to create a Python 3.8 environment:

    conda create --name tsfresh__py_3.8 python=3.8
    conda activate tsfresh__py_3.8
    pip install tsfresh[matrixprofile]

## Acknowledgements

The research and development of *TSFRESH* was funded in part by the German Federal Ministry of Education and Research under grant number 01IS14004 (project iPRODICT).

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python

```

#### File: `tests/units/__init__.py`
```python

```

#### File: `tests/units/feature_extraction/__init__.py`
```python

```

#### File: `tests/units/feature_selection/__init__.py`
```python

```

#### File: `tests/units/utilities/__init__.py`
```python

```

#### File: `tests/units/transformers/__init__.py`
```python

```


==================================================


## [3/3] Repository: usearch (`WHEEL_usearch`)
- **Full Name**: `usearch`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<h1 align="center">USearch</h1>
<h3 align="center">
Smaller & <a href="https://www.unum.cloud/blog/2023-11-07-scaling-vector-search-with-intel">Faster</a> Single-File<br/>
Similarity Search & Clustering Engine for <a href="https://github.com/ashvardanian/numkong">Vectors</a> & 🔜 <a href="https://github.com/ashvardanian/stringzilla">Texts</a>
</h3>
<br/>

<p align="center">
<a href="https://discord.gg/A6wxt6dS9j"><img height="25" src="https://github.com/unum-cloud/.github/raw/main/assets/discord.svg" alt="Discord"></a>
&nbsp;&nbsp;&nbsp;
<a href="https://www.linkedin.com/company/unum-cloud/"><img height="25" src="https://github.com/unum-cloud/.github/raw/main/assets/linkedin.svg" alt="LinkedIn"></a>
&nbsp;&nbsp;&nbsp;
<a href="https://twitter.com/unum_cloud"><img height="25" src="https://github.com/unum-cloud/.github/raw/main/assets/twitter.svg" alt="Twitter"></a>
&nbsp;&nbsp;&nbsp;
<a href="https://unum.cloud/post"><img height="25" src="https://github.com/unum-cloud/.github/raw/main/assets/blog.svg" alt="Blog"></a>
&nbsp;&nbsp;&nbsp;
<a href="https://github.com/unum-cloud/USearch"><img height="25" src="https://github.com/unum-cloud/.github/raw/main/assets/github.svg" alt="GitHub"></a>
</p>

<p align="center">
Spatial • Binary • Probabilistic • User-Defined Metrics
<br/>
<a href="https://unum-cloud.github.io/USearch/cpp">C++11</a> •
<a href="https://unum-cloud.github.io/USearch/python">Python 3</a> •
<a href="https://unum-cloud.github.io/USearch/javascript">JavaScript</a> •
<a href="https://unum-cloud.github.io/USearch/java">Java</a> •
<a href="https://unum-cloud.github.io/USearch/rust">Rust</a> •
<a href="https://unum-cloud.github.io/USearch/c">C99</a> •
<a href="https://unum-cloud.github.io/USearch/objective-c">Objective-C</a> •
<a href="https://unum-cloud.github.io/USearch/swift">Swift</a> •
<a href="https://unum-cloud.github.io/USearch/csharp">C#</a> •
<a href="https://unum-cloud.github.io/USearch/golang">Go</a> •
<a href="https://unum-cloud.github.io/USearch/wolfram">Wolfram</a>
<br/>
Linux • macOS • Windows • iOS • Android • WebAssembly •
<a href="https://unum-cloud.github.io/USearch/sqlite">SQLite</a>
</p>

<div align="center">
<a href="https://pepy.tech/project/usearch"> <img alt="PyPI" src="https://static.pepy.tech/personalized-badge/usearch?period=total&units=abbreviation&left_color=black&right_color=blue&left_text=Python%20PyPI%20installs"> </a>
<a href="https://www.npmjs.com/package/usearch"> <img alt="NPM" src="https://img.shields.io/npm/dy/usearch?label=JavaScript%20NPM%20installs"> </a>
<a href="https://crates.io/crates/usearch"> <img alt="Crate" src="https://img.shields.io/crates/d/usearch?label=Rust%20Crate%20installs"> </a>
<a href="https://www.nuget.org/packages/Cloud.Unum.USearch"> <img alt="NuGet" src="https://img.shields.io/nuget/dt/Cloud.Unum.USearch?label=CSharp%20NuGet%20installs"> </a>
<!-- Maven Central publishing is deprecated for now; fat-JAR download is the supported path. -->
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/unum-cloud/USearch?label=Repo%20size">
</div>

---

- ✅ __[10x faster][faster-than-faiss]__ [HNSW][hnsw-algorithm] implementation than [FAISS][faiss].
- ✅ Simple and extensible [single C++11 header][usearch-header] __library__.
- ✅ [Trusted](#integrations) by giants like Google and DBs like [ClickHouse][clickhouse-docs] & [DuckDB][duckdb-docs].
- ✅ [SIMD][simd]-optimized and [user-defined metrics](#user-defined-functions) with JIT compilation.
- ✅ Hardware-agnostic `bf16`, `e5m2`, & `i8` - [half-precision & quarter-precision support](#memory-efficiency-downcasting-and-quantization).
- ✅ [View large indexes from disk](#serialization--serving-index-from-disk) without loading into RAM.
- ✅ Heterogeneous lookups, renaming/relabeling, and on-the-fly deletions.
- ✅ Binary Tanimoto and Sorensen coefficients for [Genomics and Chemistry applications](#usearch--rdkit--molecular-search).
- ✅ Space-efficient point-clouds with `uint40_t`, accommodating 4B+ size.
- ✅ Compatible with OpenMP and custom "executors" for fine-grained parallelism.
- ✅ [Semantic Search](#usearch--uform--ucall--multimodal-semantic-search) and [Joins](#joins-one-to-one-one-to-many-and-many-to-many-mappings).
- 🔄 Near-real-time [clustering and sub-clustering](#clustering) for Tens or Millions of clusters.

[faiss]: https://github.com/facebookresearch/faiss
[usearch-header]: https://github.com/unum-cloud/USearch/blob/main/include/usearch/index.hpp
[obscure-use-cases]: https://ashvardanian.com/posts/abusing-vector-search
[hnsw-algorithm]: https://arxiv.org/abs/1603.09320
[simd]: https://en.wikipedia.org/wiki/Single_instruction,_multiple_data
[faster-than-faiss]: https://www.unum.cloud/blog/2023-11-07-scaling-vector-search-with-intel
[clickhouse-docs]: https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/annindexes#usearch
[duckdb-docs]: https://duckdb.org/2024/05/03/vector-similarity-search-vss.html

__Technical Insights__ and related articles:

- [Uses Arm SVE and x86 AVX-512's masked loads to eliminate tail `for`-loops](https://ashvardanian.com/posts/simsimd-faster-scipy/#tails-of-the-past-the-significance-of-masked-loads).
- [Uses Horner's method for polynomial approximations, beating GCC 12 by 119x](https://ashvardanian.com/posts/gcc-12-vs-avx512fp16/).
- [For every language implements a custom separate binding](https://ashvardanian.com/posts/porting-cpp-library-to-ten-languages/).


## Comparison with FAISS

FAISS is a widely recognized standard for high-performance vector search engines.
USearch and FAISS both employ the same HNSW algorithm, but they differ significantly in their design principles.
USearch is compact and broadly compatible without sacrificing performance, primarily focusing on user-defined metrics and fewer dependencies.

|                                              |                   FAISS |                  USearch |             Improvement |
| :------------------------------------------- | ----------------------: | -----------------------: | ----------------------: |
| Indexing time ⁰                              |                         |                          |                         |
| 100 Million 96d `f32`, `f16`, `i8` vectors   |       2.6 · 2.6 · 2.6 h |        0.3 · 0.2 · 0.2 h | __9.6 · 10.4 · 10.7 x__ |
| 100 Million 1536d `f32`, `f16`, `i8` vectors |       5.0 · 4.1 · 3.8 h |        2.1 · 1.1 · 0.8 h |   __2.3 · 3.6 · 4.4 x__ |
|                                              |                         |                          |                         |
| Codebase length ¹                            |       84 K [SLOC][sloc] |         3 K [SLOC][sloc] |            maintainable |
| Supported metrics ²                          |         9 fixed metrics |               any metric |              extendible |
| Supported languages ³                        |             C++, Python |             10 languages |                portable |
| Supported ID types ⁴                         |          32-bit, 64-bit |   32-bit, 40-bit, 64-bit |               efficient |
| Filtering ⁵                                  |               ban-lists |           any predicates |              composable |
| Required dependencies ⁶                      |            BLAS, OpenMP |                        - |            light-weight |
| Bindings ⁷                                   |                    SWIG |                   Native |             low-latency |
| Python binding size ⁸                        | [~ 10 MB][faiss-weight] | [< 1 MB][usearch-weight] |              deployable |

[sloc]: https://en.wikipedia.org/wiki/Source_lines_of_code
[faiss-weight]: https://pypi.org/project/faiss-cpu/#files
[usearch-weight]: https://pypi.org/project/usearch/#files

> ⁰ [Tested][intel-benchmarks] on Intel Sapphire Rapids, with the simplest inner-product distance, equivalent recall, and memory consumption while also providing far superior search speed.
> ¹ A shorter codebase of `usearch/` over `faiss/` makes the project easier to maintain and audit.
> ² User-defined metrics allow you to customize your search for various applications, from GIS to creating custom metrics for composite embeddings from multiple AI models or hybrid full-text and semantic search.
> ³ With USearch, you can reuse the same preconstructed index in various programming languages.
> ⁴ The 40-bit integer allows you to store 4B+ vectors without allocating 8 bytes for every neighbor reference in the proximity graph.
> ⁵ With USearch the index can be combined with arbitrary external containers, like Bloom filters or third-party databases, to filter out irrelevant keys during index traversal.
> ⁶ Lack of obligatory dependencies makes USearch much more portable.
> ⁷ Native bindings introduce lower call latencies than more straightforward approaches.
> ⁸ Lighter bindings make downloads and deployments faster.

[intel-benchmarks]: https://www.unum.cloud/blog/2023-11-07-scaling-vector-search-with-intel

Base functionality is identical to FAISS, and the interface must be familiar if you have ever investigated Approximate Nearest Neighbors search:

```py
# pip install usearch

import numpy as np
from usearch.index import Index

index = Index(ndim=3)               # Default settings for 3D vectors
vector = np.array([0.2, 0.6, 0.4])  # Can be a matrix for batch operations
index.add(42, vector)               # Add one or many vectors in parallel
matches = index.search(vector, 10)  # Find 10 nearest neighbors

assert matches[0].key == 42
assert matches[0].distance <= 0.001
assert np.allclose(index[42], vector, atol=0.1) # Ensure high tolerance in mixed-precision comparisons
```

More settings are always available, and the API is designed to be as flexible as possible.
The default storage/quantization level is hardware-dependant for efficiency, but `bf16` is recommended for most modern CPUs.

```py
index = Index(
    ndim=3, # Define the number of dimensions in input vectors
    metric='cos', # Choose 'l2sq', 'ip', 'haversine' or other metric, default = 'cos'
    dtype='bf16', # Store as 'f64', 'f32', 'bf16', 'f16', 'e5m2', 'e4m3', 'e3m2', 'e2m3', 'u8', 'i8', 'b1'..., default = None
    connectivity=16, # Optional: Limit number of neighbors per graph node
    expansion_add=128, # Optional: Control the recall of indexing
    expansion_search=64, # Optional: Control the quality of the search
    multi=False, # Optional: Allow multiple vectors per key, default = False
)
```

## Serialization & Serving `Index` from Disk

USearch supports multiple forms of serialization:

- Into a __file__ defined with a path.
- Into a __stream__ defined with a callback, serializing or reconstructing incrementally.
- Into a __buffer__ of fixed length or a memory-mapped file that supports random access.

The latter allows you to serve indexes from external memory, enabling you to optimize your server choices for indexing speed and serving costs.
This can result in __20x cost reduction__ on AWS and other public clouds.

```py
index.save("index.usearch")

index.load("index.usearch")
view = Index.restore("index.usearch", view=True, ...)

other_view = Index(ndim=..., metric=...)
other_view.view("index.usearch")
```

## Exact vs. Approximate Search

Approximate search methods, such as HNSW, are predominantly used when an exact brute-force search becomes too resource-intensive.
This typically occurs when you have millions of entries in a collection.
For smaller collections, we offer a more direct approach with the `search` method.

```py
from usearch.index import search, MetricKind, Matches, BatchMatches
import numpy as np

# Generate 10'000 random vectors with 1024 dimensions
vectors = np.random.rand(10_000, 1024).astype(np.float32)
vector = np.random.rand(1024).astype(np.float32)

one_in_many: Matches = search(vectors, vector, 50, MetricKind.L2sq, exact=True)
many_in_many: BatchMatches = search(vectors, vectors, 50, MetricKind.L2sq, exact=True)
```

If you pass the `exact=True` argument, the system bypasses indexing altogether and performs a brute-force search through the entire dataset using SIMD-optimized similarity metrics from [NumKong](https://github.com/ashvardanian/numkong).
When compared to FAISS's `IndexFlatL2` in Google Colab, __[USearch may offer up to a 20x performance improvement](https://github.com/unum-cloud/USearch/issues/176#issuecomment-1666650778)__:

- `faiss.IndexFlatL2`: __55.3 ms__.
- `usearch.index.search`: __2.54 ms__.

## User-Defined Metrics

While most vector search packages concentrate on just two metrics, "Inner Product distance" and "Euclidean distance", USearch allows arbitrary user-defined metrics.
This flexibility allows you to customize your search for various applications, from computing geospatial coordinates with the rare [Haversine][haversine] distance to creating custom metrics for composite embeddings from multiple AI models, like joint image-text embeddings.
You can use [Numba][numba], [Cppyy][cppyy], or [PeachPy][peachpy] to define your [custom metric even in Python](https://unum-cloud.github.io/USearch/python#user-defined-metrics-and-jit-in-python):

```py
from numba import cfunc, types, carray
from usearch.index import Index, MetricKind, MetricSignature, CompiledMetric

ndim = 256

@cfunc(types.float32(types.CPointer(types.float32), types.CPointer(types.float32)))
def python_inner_product(a, b):
    a_array = carray(a, ndim)
    b_array = carray(b, ndim)
    c = 0.0
    for i in range(ndim):
        c += a_array[i] * b_array[i]
    return 1 - c

metric = CompiledMetric(pointer=python_inner_product.address, kind=MetricKind.IP, signature=MetricSignature.ArrayArray)
index = Index(ndim=ndim, metric=metric, dtype=np.float32)
```

Similar effect is even easier to achieve in C, C++, and Rust interfaces.
Moreover, unlike older approaches indexing high-dimensional spaces, like KD-Trees and Locality Sensitive Hashing, HNSW doesn't require vectors to be identical in length.
They only have to be comparable.
So you can apply it in [obscure][obscure] applications, like searching for similar sets or fuzzy text matching, using [GZip][gzip-similarity] compression-ratio as a distance function.

[haversine]: https://ashvardanian.com/posts/abusing-vector-search#geo-spatial-indexing
[obscure]: https://ashvardanian.com/posts/abusing-vector-search
[gzip-similarity]: https://twitter.com/LukeGessler/status/1679211291292889100?s=20

[numba]: https://numba.readthedocs.io/en/stable/reference/jit-compilation.html#c-callbacks
[cppyy]: https://cppyy.readthedocs.io/en/latest/
[peachpy]: https://github.com/Maratyszcza/PeachPy

## Filtering and Predicate Functions

Sometimes you may want to cross-reference search-results against some external database or filter them based on some criteria.
In most engines, you'd have to manually perform paging requests, successively filtering the results.
In USearch you can simply pass a predicate function to the search method, which will be applied directly during graph traversal.
In Rust that would look like this:

```rust
let is_odd = |key: Key| key % 2 == 1;
let query = vec![0.2, 0.1, 0.2, 0.1, 0.3];
let results = index.filtered_search(&query, 10, is_odd).unwrap();
assert!(
    results.keys.iter().all(|&key| key % 2 == 1),
    "All keys must be odd"
);
```

## Memory Efficiency, Downcasting, and Quantization

Training a quantization model and dimension-reduction is a common approach to accelerate vector search.
Those, however, are only sometimes reliable, can significantly affect the statistical properties of your data, and require regular adjustments if your distribution shifts.
Instead, we have focused on high-precision arithmetic over low-precision downcasted vectors.
The same index, and `add` and `search` operations will automatically down-cast or up-cast between `f64_t`, `f32_t`, `bf16_t`, `f16_t`, `e5m2_t`, `e4m3_t`, `e3m2_t`, `e2m3_t`, `u8_t`, `i8_t`, and single-bit `b1x8_t` representations.
You can use the following command to check, if hardware acceleration is enabled:

```sh
$ python -c 'from usearch.index import Index; print(Index(ndim=768, metric="cos", dtype="f16").hardware_acceleration)'
> sapphire
$ python -c 'from usearch.index import Index; print(Index(ndim=166, metric="tanimoto").hardware_acceleration)'
> ice
```

In most cases, `bf16` is recommended for modern CPUs.
For even smaller footprints, USearch supports IEEE & MX-compatible Float8 (`e5m2` and `e4m3`) and Float6 (`e3m2` and `e2m3`) formats.
You can pass pre-quantized buffers from [NumKong](https://github.com/ashvardanian/numkong) with the explicit `dtype=` parameter on `add` and `search`, or let USearch handle the quantization internally from higher-precision inputs.
When quantization is enabled, the "get"-like functions won't be able to recover the original data, so you may want to replicate the original vectors elsewhere.
When quantizing to `i8_t` integers, note that it's only valid for cosine-like metrics.
As part of the quantization process, the vectors are normalized to unit length and later scaled to [-127, 127] range to occupy the full 8-bit range.
When quantizing to `b1x8_t` single-bit representations, note that it's only valid for binary metrics like Jaccard, Hamming, etc.
As part of the quantization process, the scalar components greater than zero are set to `true`, and the rest to `false`.

![USearch uint40_t support](https://github.com/unum-cloud/USearch/blob/main/assets/usearch-neighbor-types.png?raw=true)

Using smaller numeric types will save you RAM needed to store the vectors, but you can also compress the neighbors lists forming our proximity graphs.
By default, 32-bit `uint32_t` is used to enumerate those, which is not enough if you need to address over 4 Billion entries.
For such cases we provide a custom `uint40_t` type, that will still be 37.5% more space-efficient than the commonly used 8-byte integers, and will scale up to 1 Trillion entries.


## `Indexes` for Multi-Index Lookups

For larger workloads targeting billions or even trillions of vectors, parallel multi-index lookups become invaluable.
Instead of constructing one extensive index, you can build multiple smaller ones and view them together.

```py
from usearch.index import Indexes

multi_index = Indexes(
    indexes: Iterable[usearch.index.Index] = [...],
    paths: Iterable[os.PathLike] = [...],
    view: bool = False,
    threads: int = 0,
)
multi_index.search(...)
```

## Clustering

Once the index is constructed, USearch can perform K-Nearest Neighbors Clustering much faster than standalone clustering libraries, like SciPy, 
UMap, and tSNE.
Same for dimensionality reduction with PCA. 
Essentially, the `Index` itself can be seen as a clustering, allowing iterative deepening.

```py
clustering = index.cluster(
    min_count=10, # Optional
    max_count=15, # Optional
    threads=..., # Optional
)

# Get the clusters and their sizes
centroid_keys, sizes = clustering.centroids_popularity

# Use Matplotlib to draw a histogram
clustering.plot_centroids_popularity()

# Export a NetworkX graph of the clusters
g = clustering.network

# Get members of a specific cluster
first_members = clustering.members_of(centroid_keys[0])

# Deepen into that cluster, splitting it into more parts, all the same arguments supported
sub_clustering = clustering.subcluster(min_count=..., max_count=...)
```

The resulting clustering isn't identical to K-Means or other conventional approaches but serves the same purpose.
Alternatively, using Scikit-Learn on a 1 Million point dataset, one may expect queries to take anywhere from minutes to hours, depending on the number of clusters you want to highlight.
For 50'000 clusters, the performance difference between USearch and conventional clustering methods may easily reach 100x.

## Joins, One-to-One, One-to-Many, and Many-to-Many Mappings

One of the big questions these days is how AI will change the world of databases and data management.
Most databases are still struggling to implement high-quality fuzzy search, and the only kind of joins they know are deterministic.
A `join` differs from searching for every entry, requiring a one-to-one mapping banning collisions among separate search results.

| Exact Search | Fuzzy Search | Semantic Search ? |
| :----------: | :----------: | :---------------: |
|  Exact Join  | Fuzzy Join ? | Semantic Join ??  |

Using USearch, one can implement sub-quadratic complexity approximate, fuzzy, and semantic joins.
This can be useful in any fuzzy-matching tasks common to Database Management Software.

```py
men = Index(...)
women = Index(...)
pairs: dict = men.join(women, max_proposals=0, exact=False)
```

> Read more in the post: [Combinatorial Stable Marriages for Semantic Search 💍](https://ashvardanian.com/posts/searching-stable-marriages)


## Functionality

By now, the core functionality is supported across all bindings.
Broader functionality is ported per request.
In some cases, like Batch operations, feature parity is meaningless, as the host language has full multi-threading capabilities and the USearch index structure is concurrent by design, so the users can implement batching/scheduling/load-balancing in the most optimal way for their applications.

|                         | C++ 11 | Python 3 | C 99  | Java  | JavaScript | Rust  |  Go   | Swift |
| :---------------------- | :----: | :------: | :---: | :---: | :--------: | :---: | :---: | :---: |
| Add, search, remove     |   ✅    |    ✅     |   ✅   |   ✅   |     ✅      |   ✅   |   ✅   |   ✅   |
| Save, load, view        |   ✅    |    ✅     |   ✅   |   ✅   |     ✅      |   ✅   |   ✅   |   ✅   |
| User-defined metrics    |   ✅    |    ✅     |   ✅   |   ❌   |     ❌      |   ✅   |   ❌   |   ❌   |
| Batch operations        |   ❌    |    ✅     |   ❌   |   ✅   |     ✅      |   ❌   |   ❌   |   ❌   |
| Filter predicates       |   ✅    |    ❌     |   ✅   |   ❌   |     ❌      |   ✅   |   ❌   |   ✅   |
| Joins                   |   ✅    |    ✅     |   ❌   |   ❌   |     ❌      |   ❌   |   ❌   |   ❌   |
| Variable-length vectors |   ✅    |    ❌     |   ❌   |   ❌   |     ❌      |   ❌   |   ❌   |   ❌   |
| 4B+ capacities          |   ✅    |    ❌     |   ❌   |   ❌   |     ❌      |   ❌   |   ❌   |   ❌   |

## Application Examples

### USearch + UForm + UCall = Multimodal Semantic Search

AI has a growing number of applications, but one of the coolest classic ideas is to use it for Semantic Search.
One can take an encoder model, like the multi-modal [UForm](https://github.com/unum-cloud/uform), and a web-programming framework, like [UCall](https://github.com/unum-cloud/ucall), and build a text-to-image search platform in just 20 lines of Python.

```python
from ucall import Server
from uform import get_model, Modality
from usearch.index import Index

import numpy as np
import PIL as pil

processors, models = get_model('unum-cloud/uform3-image-text-english-small')
model_text = models[Modality.TEXT_ENCODER]
model_image = models[Modality.IMAGE_ENCODER]
processor_text = processors[Modality.TEXT_ENCODER]
processor_image = processors[Modality.IMAGE_ENCODER]

server = Server()
index = Index(ndim=256)

@server
def add(key: int, photo: pil.Image.Image):
    image = processor_image(photo)
    vector = model_image(image)
    index.add(key, vector.flatten(), copy=True)

@server
def search(query: str) -> np.ndarray:
    tokens = processor_text(query)
    vector = model_text(tokens)
    matches = index.search(vector.flatten(), 3)
    return matches.keys

server.run()
```

Similar experiences can also be implemented in other languages and on the client side, removing the network latency.
For Swift and iOS, check out the [`ashvardanian/SwiftSemanticSearch`](https://github.com/ashvardanian/SwiftSemanticSearch) repository.

<table>
  <tr>
    <td>
      <img src="https://github.com/ashvardanian/ashvardanian/blob/master/demos/SwiftSemanticSearch-Dog.gif?raw=true" alt="SwiftSemanticSearch demo Dog">
    </td>
    <td>
      <img src="https://github.com/ashvardanian/ashvardanian/blob/master/demos/SwiftSemanticSearch-Flowers.gif?raw=true" alt="SwiftSemanticSearch demo with Flowers">
    </td>
  </tr>
</table>

A more complete [demo with Streamlit is available on GitHub](https://github.com/ashvardanian/usearch-images).
We have pre-processed some commonly used datasets, cleaned the images, produced the vectors, and pre-built the index.

| Dataset                             |            Modalities | Images |                              Download |
| :---------------------------------- | --------------------: | -----: | ------------------------------------: |
| [Unsplash][unsplash-25k-origin]     | Images & Descriptions |   25 K | [HuggingFace / Unum][unsplash-25k-hf] |
| [Conceptual Captions][cc-3m-origin] | Images & Descriptions |    3 M |        [HuggingFace / Unum][cc-3m-hf] |
| [Arxiv][arxiv-2m-origin]            |    Titles & Abstracts |    2 M |     [HuggingFace / Unum][arxiv-2m-hf] |

[unsplash-25k-origin]: https://github.com/u
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `javascript/dist-package-esm.json`
```python
{
    "type": "module"
}
```

#### File: `javascript/dist-package-cjs.json`
```python
{
    "type": "commonjs"
}
```

#### File: `wasm/lib.cpp`
```python
#define USEARCH_EXPORT EMSCRIPTEN_KEEPALIVE

#include <emscripten/emscripten.h>

#include <../c/lib.cpp>
```

#### File: `javascript/tsconfig-cjs.json`
```python
{
    "extends": "./tsconfig-base.json",
    "compilerOptions": {
        "module": "commonjs",
        "outDir": "dist/cjs",
        "target": "es2015"
    }
}
```

#### File: `javascript/tsconfig-esm.json`
```python
{
    "extends": "./tsconfig-base.json",
    "compilerOptions": {
        "module": "esnext",
        "outDir": "dist/esm",
        "target": "esnext",
        "esModuleInterop": true,
    }
}
```

#### File: `.vscode/extensions.json`
```python
{
    "recommendations": [
        "vknabel.vscode-apple-swift-format",
        "sswg.swift-lang",
        "ms-python.black-formatter",
        "ms-vscode.cpptools-extension-pack",
        "xaver.clang-format",
        "swellaby.rust-pack"
    ]
}
```


==================================================
