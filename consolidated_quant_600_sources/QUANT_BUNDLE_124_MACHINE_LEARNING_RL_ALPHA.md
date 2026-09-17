# ⚡ [QUANT-SOURCE-124] Consolidated Quant & Algo Trading Repositories
**Category**: `MACHINE_LEARNING_RL_ALPHA` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_124_MACHINE_LEARNING_RL_ALPHA.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: airflow (`VAULT_IN-QUANT-037_apache__airflow`)
- **Full Name**: `IN-QUANT-037_apache__airflow`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<!--
 Licensed to the Apache Software Foundation (ASF) under one
 or more contributor license agreements.  See the NOTICE file
 distributed with this work for additional information
 regarding copyright ownership.  The ASF licenses this file
 to you under the Apache License, Version 2.0 (the
 "License"); you may not use this file except in compliance
 with the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing,
 software distributed under the License is distributed on an
 "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 KIND, either express or implied.  See the License for the
 specific language governing permissions and limitations
 under the License.
-->

<!-- START Apache Airflow, please keep comment here to allow auto update of PyPI readme.md -->
# Apache Airflow

| Category   | Badges                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| License    | [![License](https://img.shields.io/:license-Apache%202-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.txt)                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PyPI       | [![PyPI version](https://badge.fury.io/py/apache-airflow.svg)](https://badge.fury.io/py/apache-airflow) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/apache-airflow.svg)](https://pypi.org/project/apache-airflow/) [![PyPI - Downloads](https://img.shields.io/pypi/dm/apache-airflow)](https://pypi.org/project/apache-airflow/)                                                                                                                                                                               |
| Containers | [![Docker Pulls](https://img.shields.io/docker/pulls/apache/airflow.svg)](https://hub.docker.com/r/apache/airflow) [![Docker Stars](https://img.shields.io/docker/stars/apache/airflow.svg)](https://hub.docker.com/r/apache/airflow) [![Artifact HUB](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/apache-airflow)](https://artifacthub.io/packages/search?repo=apache-airflow)                                                                                                                      |
| Community  | [![Contributors](https://img.shields.io/github/contributors/apache/airflow)](https://github.com/apache/airflow/graphs/contributors) [![Slack Status](https://img.shields.io/badge/slack-join_chat-white.svg?logo=slack&style=social)](https://s.apache.org/airflow-slack) ![Commit Activity](https://img.shields.io/github/commit-activity/m/apache/airflow) [![LFX Health Score](https://insights.linuxfoundation.org/api/badge/health-score?project=apache-airflow)](https://insights.linuxfoundation.org/project/apache-airflow)  |
| Dev tools  | [![prek](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/j178/prek/master/docs/assets/badge-v0.json)](https://github.com/j178/prek)                                                                                                                                                                                                                                                                                                                                                                            |

| Version | Build Status                                                                                                                                                    |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Main    | [![Tests AMD main](https://github.com/apache/airflow/actions/workflows/ci-amd.yml/badge.svg)](https://github.com/apache/airflow/actions/workflows/ci-amd.yml) [![Tests ARM main](https://github.com/apache/airflow/actions/workflows/ci-arm.yml/badge.svg)](https://github.com/apache/airflow/actions/workflows/ci-arm.yml) |
| 3.x     | [![Tests AMD 3.2](https://github.com/apache/airflow/actions/workflows/ci-amd.yml/badge.svg?branch=v3-2-test)](https://github.com/apache/airflow/actions/workflows/ci-amd.yml) [![Tests ARM 3.2](https://github.com/apache/airflow/actions/workflows/ci-arm.yml/badge.svg?branch=v3-2-test)](https://github.com/apache/airflow/actions/workflows/ci-arm.yml) |



<picture width="500">
  <img
    src="https://github.com/apache/airflow/blob/19ebcac2395ef9a6b6ded3a2faa29dc960c1e635/docs/apache-airflow/img/logos/wordmark_1.png?raw=true"
    alt="Apache Airflow logo"
  />
</picture>

[Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/) (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.

When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

Use Airflow to author workflows (Dags) that orchestrate tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on Dags a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.

<!-- END Apache Airflow, please keep comment here to allow auto update of PyPI readme.md -->
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of contents**

- [Project Focus](#project-focus)
- [Principles](#principles)
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [Installing from PyPI](#installing-from-pypi)
- [Installation](#installation)
- [Official source code](#official-source-code)
- [Convenience packages](#convenience-packages)
- [User Interface](#user-interface)
- [Semantic versioning](#semantic-versioning)
- [Version Life Cycle](#version-life-cycle)
- [Support for Python and Kubernetes versions](#support-for-python-and-kubernetes-versions)
- [Base OS support for reference Airflow images](#base-os-support-for-reference-airflow-images)
- [Approach to dependencies of Airflow](#approach-to-dependencies-of-airflow)
- [Contributing](#contributing)
- [Community standards](#community-standards)
- [Agent-assisted contribution (apache-magpie)](#agent-assisted-contribution-apache-magpie)
- [Voting Policy](#voting-policy)
- [Who uses Apache Airflow?](#who-uses-apache-airflow)
- [Who maintains Apache Airflow?](#who-maintains-apache-airflow)
- [What goes into the next release?](#what-goes-into-the-next-release)
- [Can I use the Apache Airflow logo in my presentation?](#can-i-use-the-apache-airflow-logo-in-my-presentation)
- [Links](#links)
- [Sponsors](#sponsors)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Project Focus

Airflow works best with workflows that are mostly static and slowly changing. When the Dag structure is similar from one run to the next, it clarifies the unit of work and continuity. Other similar projects include [Luigi](https://github.com/spotify/luigi), [Oozie](https://oozie.apache.org/) and [Azkaban](https://azkaban.github.io/).

Beyond traditional data pipelines, Airflow is widely used to orchestrate machine learning workflows — training, retraining, evaluation, and deployment — and increasingly to orchestrate agentic and LLM-based workloads, coordinating the steps of an AI pipeline (data prep, tool calls, model invocation, evaluation) rather than acting as the agent itself. This isn't a new direction: teams have run ML and AI workloads on Airflow for years, and the ecosystem of providers supporting these use cases (see the [AI & ML section of the Airflow registry](https://airflow.apache.org/registry/providers/?category=ai-ml)) continues to grow.

Airflow is commonly used to process data, but has the opinion that tasks should ideally be idempotent (i.e., results of the task will be the same, and will not create duplicated data in a destination system), and should not pass large quantities of data from one task to the next (though tasks can pass metadata using Airflow's [XCom feature](https://airflow.apache.org/docs/apache-airflow/stable/concepts/xcoms.html)). For high-volume, data-intensive tasks, a best practice is to delegate to external services specializing in that type of work.

Airflow is not a streaming solution, but it is often used to process real-time data, pulling data off streams in batches.

## Principles

- **Dynamic**: Pipelines are defined in code, enabling dynamic dag generation and parameterization.
- **Extensible**: The Airflow framework includes a wide range of built-in operators and can be extended to fit your needs.
- **Flexible**: Airflow leverages the [**Jinja**](https://jinja.palletsprojects.com) templating engine, allowing rich customizations.

<!-- START Requirements, please keep comment here to allow auto update of PyPI readme.md -->
## Requirements

Apache Airflow is tested with:

|            | Main version (dev)                 | Stable version (3.3.0)              | Deprecate version (2.11.2)   |
|------------|------------------------------------|-------------------------------------|------------------------------|
| Python     | 3.10, 3.11, 3.12, 3.13, 3.14       | 3.10, 3.11, 3.12, 3.13, 3.14        | 3.10, 3.11, 3.12             |
| Platform   | AMD64/ARM64                        | AMD64/ARM64                         | AMD64/ARM64(\*)              |
| Kubernetes | 1.30, 1.31, 1.32, 1.33, 1.34, 1.35 | 1.30, 1.31, 1.32, 1.33, 1.34, 1.35  | 1.26, 1.27, 1.28, 1.29, 1.30 |
| PostgreSQL | 14, 15, 16, 17, 18                 | 14, 15, 16, 17, 18                  | 12, 13, 14, 15, 16           |
| MySQL      | 8.0, 8.4, Innovation               | 8.0, 8.4, Innovation                | 8.0, Innovation              |
| SQLite     | 3.15.0+                            | 3.15.0+                             | 3.15.0+                      |

\* Experimental

**Note**: MariaDB is not tested/recommended.

**Note**: SQLite is used in Airflow tests. Do not use it in production. We recommend
using the latest stable version of SQLite for local development.

**Note**: Airflow currently can be run on POSIX-compliant Operating Systems. For development, it is regularly
tested on fairly modern Linux Distros and recent versions of macOS.
On Windows you can run it via WSL2 (Windows Subsystem for Linux 2) or via Linux Containers.
The work to add Windows support is tracked via [#10388](https://github.com/apache/airflow/issues/10388), but
it is not a high priority. You should only use Linux-based distros as "Production" execution environment
as this is the only environment that is supported. The only distro that is used in our CI tests and that
is used in the [Community managed DockerHub image](https://hub.docker.com/p/apache/airflow) is
`Debian Bookworm`.

<!-- END Requirements, please keep comment here to allow auto update of PyPI readme.md -->
<!-- START Getting started, please keep comment here to allow auto update of PyPI readme.md -->
## Getting started

Visit the official Airflow website documentation (latest **stable** release) for help with
[installing Airflow](https://airflow.apache.org/docs/apache-airflow/stable/installation/),
[getting started](https://airflow.apache.org/docs/apache-airflow/stable/start.html), or walking
through a more complete [tutorial](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/).

> Note: If you're looking for documentation for the main branch (latest development branch): you can find it on [s.apache.org/airflow-docs](https://s.apache.org/airflow-docs/).

For more information on Airflow Improvement Proposals (AIPs), visit
the [Airflow Wiki](https://cwiki.apache.org/confluence/display/AIRFLOW/Airflow+Improvement+Proposals).

Documentation for dependent projects like provider distributions, Docker image, Helm Chart, you'll find it in [the documentation index](https://airflow.apache.org/docs/).

<!-- END Getting started, please keep comment here to allow auto update of PyPI readme.md -->
<!-- START Installing from PyPI, please keep comment here to allow auto update of PyPI readme.md -->

## Installing from PyPI

We publish Apache Airflow as `apache-airflow` package in PyPI. Installing it however might be sometimes tricky
because Airflow is a bit of both a library and application. Libraries usually keep their dependencies open, and
applications usually pin them, but we should do neither and both simultaneously. We decided to keep
our dependencies as open as possible (in `pyproject.toml`) so users can install different versions of libraries
if needed. This means that `pip install apache-airflow` will not work from time to time or will
produce unusable Airflow installation.

To have repeatable installation, however, we keep a set of "known-to-be-working" constraint
files in the orphan `constraints-main` and `constraints-2-0` branches. We keep those "known-to-be-working"
constraints files separately per major/minor Python version.
You can use them as constraint files when installing Airflow from PyPI. Note that you have to specify
correct Airflow tag/version/branch and Python versions in the URL.

1. Installing just Airflow:

> Note: Only `pip` and `uv` installation is currently officially supported.

While it is possible to install Airflow with tools like [Poetry](https://python-poetry.org) or
[pip-tools](https://pypi.org/project/pip-tools), they do not share the same workflow as
`pip` - especially when it comes to constraint vs. requirements management.
Installing via `Poetry` or `pip-tools` is not currently supported.

If you wish to install Airflow using those tools, you should use the constraint files and convert
them to the appropriate format and workflow that your tool requires.


```bash
pip install 'apache-airflow==3.3.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.3.0/constraints-3.10.txt"
```

2. Installing with extras (i.e., postgres, google)

```bash
pip install 'apache-airflow[postgres,google]==3.3.0' \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-3.3.0/constraints-3.10.txt"
```

For information on installing provider distributions, check
[providers](https://airflow.apache.org/docs/apache-airflow-providers/index.html).

<!-- END Installing from PyPI, please keep comment here to allow auto update of PyPI readme.md -->

## Installation

For comprehensive instructions on setting up your local development environment and installing Apache Airflow, please refer to the [INSTALLING.md](INSTALLING.md) file.

<!-- START Official source code, please keep comment here to allow auto update of PyPI readme.md -->
## Official source code

Apache Airflow is an [Apache Software Foundation](https://www.apache.org) (ASF) project,
and our official source code releases:

- Follow the [ASF Release Policy](https://www.apache.org/legal/release-policy.html)
- Can be downloaded from [the ASF Distribution Directory](https://downloads.apache.org/airflow)
- Are cryptographically signed by the release manager
- Are officially voted on by the PMC members during the
  [Release Approval Process](https://www.apache.org/legal/release-policy.html#release-approval)

Following the ASF rules, the source packages released must be sufficient for a user to build and test the
release provided they have access to the appropriate platform and tools.

<!-- END Official source code, please keep comment here to allow auto update of PyPI readme.md -->
## Convenience packages

There are other ways of installing and using Airflow. Those are "convenience" methods - they are
not "official releases" as stated by the `ASF Release Policy`, but they can be used by the users
who do not want to build the software themselves.

Those are - in the order of most common ways people install Airflow:

- [PyPI releases](https://pypi.org/project/apache-airflow/) to install Airflow using standard `pip` tool
- [Docker Images](https://hub.docker.com/r/apache/airflow) to install airflow via
  `docker` tool, use them in Kubernetes, Helm Charts, `docker-compose`, `docker swarm`, etc. You can
  read more about using, customizing, and extending the images in the
  [Latest docs](https://airflow.apache.org/docs/docker-stack/index.html), and
  learn details on the internals in the [images](https://airflow.apache.org/docs/docker-stack/index.html) document.
- [Tags in GitHub](https://github.com/apache/airflow/tags) to retrieve the git project sources that
  were used to generate official source packages via git

All those artifacts are not official releases, but they are prepared using officially released sources.
Some of those artifacts are "development" or "pre-release" ones, and they are clearly marked as such
following the ASF Policy.

## User Interface

- **Dags**: Overview of all Dags in your environment.

  ![Dags](https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/dags.png)

- **Assets**: Overview of Assets with dependencies.

  ![Asset Dependencies](https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/assets_graph.png)

- **Grid**: Grid representation of a Dag that spans across time.

  ![Grid](https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/grid.png)

- **Graph**: Visualization of a Dag's dependencies and their current status for a specific run.

  ![Graph](https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/graph.png)

- **Home**: Summary statistics of your Airflow environment.

  ![Home](https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/home.png)

- **Backfill**: Backfilling a Dag for a specific date range.

  ![Backfill](https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/backfill.png)

- **Code**: Quick way to view source code of a Dag.

  ![Code](https://raw.githubusercontent.com/apache/airflow/main/airflow-core/docs/img/ui-dark/code.png)

## Semantic versioning

As of Airflow 2.0.0, we support a strict [SemVer](https://semver.org/) approach for all packages released.

There are few specific rules that we agreed to that define details of versioning of the different
packages:

* **Airflow**: SemVer rules apply to core airflow only (excludes any changes to providers).
  Changing limits for versions of Airflow dependencies is not a breaking change on its own.
* **Airflow Providers**: SemVer rules apply to changes in the particular provider's code only.
  SemVer MAJOR and MINOR versions for the packages are independent of the Airflow version.
  For example, `google 4.1.0` and `amazon 3.1.1` providers can happily be installed
  with `Airflow 2.1.2`. If there are limits of cross-dependencies between providers and Airflow packages,
  they are present in providers as `install_requires` limitations. We aim to keep backwards
  compatibility of providers with all previously released Airflow 2 versions but
  there will sometimes be breaking changes that might make some, or all
  providers, have minimum Airflow version specified.
* **Airflow Helm Chart**: SemVer rules apply to changes in the chart only. SemVer MAJOR and MINOR
  versions for the chart are independent of the Airflow version. We aim to keep backwards
  compatibility of the Helm Chart with all released Airflow 2 versions, but some new features might
  only work starting from specific Airflow releases. We might however limit the Helm
  Chart to depend on minimal Airflow version.
* **Airflow API clients**: Their versioning is independent from Airflow versions. They follow their own
  SemVer rules for breaking changes and new features - which for example allows to change the way we generate
  the clients.

## Version Life Cycle

Apache Airflow version life cycle:

<!-- This table is automatically updated by prek scripts/ci/prek/supported_versions.py -->
<!-- Beginning of auto-generated table -->

| Version   | Current Patch/Minor   | State       | First Release   | Limited Maintenance   | EOL/Terminated   |
|-----------|-----------------------|-------------|-----------------|-----------------------|------------------|
| 3         | 3.3.1                 | Maintenance | Apr 22, 2025    | TBD                   | TBD              |
| 2         | 2.11.2                | EOL         | Dec 17, 2020    | Oct 22, 2025          | Apr 22, 2026     |
| 1.10      | 1.10.15               | EOL         | Aug 27, 2018    | Dec 17, 2020          | June 17, 2021    |
| 1.9       | 1.9.0                 | EOL         | Jan 03, 2018    | Aug 27, 2018          | Aug 27, 2018     |
| 1.8       | 1.8.2                 | EOL         | Mar 19, 2017    | Jan 03, 2018          | Jan 03, 2018     |
| 1.7       | 1.7.1.2               | EOL         | Mar 28, 2016    | Mar 19, 2017          | Mar 19, 2017     |

<!-- End of auto-generated table -->

Limited support versions will be supported with security and critical bug fix only.
EOL versions will not get any fixes nor support.
We always recommend that all users run the latest available minor release for whatever major version is in use.
We **highly** recommend upgrading to the latest Airflow major release at the earliest convenient time and before the EOL date.

## Support for Python and Kubernetes versions

As of Airflow 2.0, we agreed to certain rules we follow for Python and Kubernetes support.
They are based on the official release schedule of Python and Kubernetes, nicely summarized in the
[Python Developer's Guide](https://devguide.python.org/#status-of-python-branches) and
[Kubernetes version skew policy](https://kubernetes.io/docs/setup/release/version-skew-policy/).

1. We drop support for Python and Kubernetes versions when they reach EOL. Except for Kubernetes, a
   version stays supported by Airflow if two major cloud providers still provide support for it. We drop
   support for those EOL versions in main right after EOL date, and it is effectively removed when we release
   the first new MINOR (Or MAJOR if there is no new MINOR version) of Airflow. For example, for Python 3.10 it
   means that we will drop support in main right after 27.06.2023, and the first MAJOR or MINOR version of
   Airflow released after will not have it.

2. We support a new version of Python/Kubernetes in main after they are officially released, as soon as we
   make them work in our CI pipeline (which might not be immediate due to dependencies catching up with
   new versions of Python mostly) we release new images/support in Airflow based on the working CI setup.

3. This policy is best-effort which means there may be situations where we might terminate support earlier
   if circumstances require it.

## Base OS support for reference Airflow images

The Airflow Community provides conveniently packaged container images that are published whenever
we publish an Apache Airflow release. Those images contain:

* Base OS with necessary packages to install Airflow (stable Debian OS)
* Base Python installation in versions supported at the time of release for the MINOR version of
  Airflow released (so there could be different versions for 2.3 and 2.2 line for example)
* Libraries required to connect to supported Databases (again the set of databases supported depends
  on the MINOR version of Airflow)
* Predefined set of popular providers (for details see the [Dockerfile](https://raw.githubusercontent.com/apache/airflow/main/Dockerfile)).
* Possibility of building your own, custom image where the user can choose their own set of providers
  and libraries (see [Building the image](ht
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `providers/google/src/airflow/providers/google/_vendor/__init__.py`
```python

```

#### File: `airflow-core/src/airflow/_vendor/__init__.py`
```python

```

#### File: `providers/openlineage/tests/system/openlineage/expected_events/openlineage_schedule_list_complex_assets_dag__af2.json`
```python
[]
```

#### File: `providers/openlineage/tests/system/openlineage/expected_events/openlineage_versioned_dag__af2.json`
```python
[]
```

#### File: `providers/amazon/tests/unit/amazon/aws/config_templates/args.json`
```python
[
  "/usr/lib/spark/bin/run-example1"
]
```

#### File: `dev/breeze/src/airflow_breeze/files/simple_auth_manager_passwords.json`
```python
{"admin": "admin", "viewer": "viewer", "user": "user", "op": "op"}
```


==================================================


## [2/3] Repository: stock-market-analysis-with-sql (`VAULT_IN-QUANT-075_sahidul-shaikh__stock-market-analysis-with-sql`)
- **Full Name**: `IN-QUANT-075_sahidul-shaikh__stock-market-analysis-with-sql`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Stock Market Analysis 

# Problem Statement 

Two of India's biggest stock exchanges BSE and NSE, collectively clear trades combining to greater than 40,000 crores every day. As you might already be aware, a lot of trading happens on the basis of technical and fundamental analysis.

One of the most basic technical analysis used by a lot of stock traders is the Moving Average Method. 
Consider the following price trend of a particular stock.

Week 1: 13,14,11,17,19
Week 2: 26,23,22,22,14
Week 3: 17,19,13,16,17

![Alt Itext](https://github.com/sahidul-shaikh/stock-market-analysis-with-sql/blob/main/MA-Image.png?raw=True)

As We can see, Moving average use the past data to smoothen the price curve. For the purpose of this assignment, we will be using 20 Day and 50 Day moving averages.

Now that we know about the concept of Moving average, we shall be wondering how to use it to determine whether to buy or sell a stock.

When the shorter-term moving average crosses above the longer-term moving average, it is a signal to **BUY**, as it indicates that the trend is shifting up. This is known as a Golden Cross.

On the opposite when the shorter term moving average crosses below the longer term moving average, it is a signal to **SELL**, as it indicates the trend is shifting down. It is sometimes referred to as the Death Cross.

Please note that it is important that the Moving Averages Cross each other in order to generate a signal. Merely being above or below is not sufficient to generate a signal.

When the signal is neither buy nor sell, it is classified as hold. If we already own the stock, keep it and if we don't then don't buy it now.

## Data Set

The dataset provided here has been extracted from the NSE website. The Stock price data provided is from 1-Jan-2015 to 31-July-2018 for six stocks Eicher Motors, Hero, Bajaj Auto, TVS Motors, Infosys and TCS.

Please note that for the days where it is not possible to calculate the required Moving Averages, it is better to ignore these rows rather than trying to deal with NULL by filling it with average value as that would make no practical sense.

Create a new schema named 'Assignment'
Import the CSV files in MySQL, naming the tables as the name of the stocks. 

## Results Expected

1. Create a new table named 'bajaj1' containing the date, close price, 20 Day MA and 50 Day MA. (This has to be done for all 6 stocks)
The table header should appear as below:
Data - Close Price - 20 Day MA - 50 Day MA
2. Create a master table containing the date and close price of all the six stocks. (Column header for the price is the name of the stock)
The table header should appear as below:
Data - Bajaj - TCS - TVS - Infosys - Eicher - Hero
3. Use the table created in Part(1) to generate buy and sell signal. Store this in another table named 'bajaj2'. Perform this operation for all stocks.
The table header should appear as below:
Date - Close Price - Signal
4. Create a User defined function, that takes the date as input and returns the signal for that particular day (Buy/Sell/Hold) for the Bajaj stock.
5. Write a brief summary of the results obtained and what inferences we can draw from the analysis performed.


==================================================


## [3/3] Repository: TradeBrain_api (`VAULT_IN-QUANT-080_sudama011__TradeBrain_api`)
- **Full Name**: `IN-QUANT-080_sudama011__TradeBrain_api`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# 🧠 TradeBrain API

**TradeBrain** is an autonomous, AI-powered trading intelligence platform that identifies high-probability swing trading opportunities in the Indian Market (NSE/BSE) using a "Triple Confirmation" logic engine.

Unlike simple screeners, TradeBrain acts as a disciplined analyst: checking Technicals, Fundamentals, and News Catalysts before generating a signal. It combines real-time market data, AI-driven analysis, and automated risk management to deliver actionable trading setups.

---

## 📚 Documentation Hub

* **[🏛️ System Architecture](docs/architecture.md)**
    * The "Brain" of the system. Explains the Discovery → Analysis → Validation → Audit pipeline.
* **[🗄️ Domain Models & Database](docs/domain_models.md)**
    * The Source of Truth for the DB Schema, Enums, Indexes, and Integrity Rules.
* **[🔌 API Specification](docs/api_spec.md)**
    * Detailed Endpoint definitions with **Request/Response JSON examples**.

---

## 🚀 Core Features

* **24/7 Market Scanning**: Autonomous background workers monitor watchlists and "Stocks in Play".
* **Triple Confirmation**: AI Analysis based on Technicals + Fundamentals + Catalysts.
* **Optimization Engine**: Smart caching prevents redundant AI calls (checks price variance < 0.5%).
* **Risk Management**: "Math Police" validation (e.g., Risk/Reward ≥ 1:2) enforced before DB entry.
* **Signal Auditing**: Automated "The Truth" checks against live prices to update signal status.
* **Paper Trading**: Virtual portfolio management to track signal performance.

---

## 🏗️ Project Structure

The project follows a strict "Engine vs. API" separation of concerns:

```bash
TradeBrain_api/
├── app/
│   ├── api/            # The Face: REST API Endpoints (FastAPI)
│   ├── engine/         # The Brain: Background Intelligence (Scanner, Validator)
│   ├── models/         # Database Schemas (SQLAlchemy)
│   ├── repositories/   # Data Access Layer
│   ├── services/       # Business Logic & Orchestration
│   └── core/           # Config, Logging, Security
└── tests/              # Unit and Integration Tests
```

---

## 🚀 Tech Stack

| Component | Technology |
| --- | --- |
| **Core Framework** | Python 3.13+, FastAPI |
| **Database** | PostgreSQL (Async via SQLAlchemy 2.0) |
| **AI Engine** | Google Gemini Flash (1.5/2.0) |
| **Data Sources** | yfinance, Tavily Search API |
| **Scheduling** | APScheduler (Cron Jobs) |
| **Authentication** | JWT (PyJWT) with Session Tracking |
| **Validation** | Pydantic v2 |

---

## 🔧 Installation & Setup

### Prerequisites

* Python 3.13+
* PostgreSQL 14+
* Docker & Docker Compose (optional)

### Local Development

1. **Clone the repository**
```bash
git clone https://github.com/sudama011/tradebrain.git
cd tradebrain

```


2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

```


3. **Install dependencies**
```bash
pip install -r requirements-dev.txt

```


4. **Configure environment**
```bash
cp .env.example .env
# Edit .env with your API keys (Gemini, Tavily) and Database URL

```


5. **Initialize database**
```bash
make db-migrate
make db-seed

```


6. **Run the server**
```bash
make run
# Or: uvicorn app.main:app --reload

```



The API will be available at `http://localhost:8000`

* **API Docs**: http://localhost:8000/docs
* **ReDoc**: http://localhost:8000/redoc

### Docker Setup

```bash
docker-compose up -d
# Database will be available at localhost:5432
# API will be available at localhost:8000

```

### Core Implementation Code & Architecture
#### File: `app/__init__.py`
```python

```

#### File: `app/core/__init__.py`
```python

```

#### File: `app/repositories/trade.py`
```python

```

#### File: `app/db/__init__.py`
```python

```

#### File: `app/api/__init__.py`
```python

```

#### File: `app/services/portfolio.py`
```python

```


==================================================
