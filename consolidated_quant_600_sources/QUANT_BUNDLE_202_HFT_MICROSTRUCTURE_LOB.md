# ⚡ [QUANT-SOURCE-202] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_202_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: crypto-lob-data-pipeline (`WHEEL_crypto-lob-data-pipeline`)
- **Full Name**: `crypto-lob-data-pipeline`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
  <h3 align="center">Order Flow Imbalance Data Pipeline</h3>

  <p align="center">
    A real-time streaming data pipeline built using Kafka and Docker. Consumes Bitcoin data from Deribit's API v2.1.1 and transforms limit order book market data to net order flow imbalance and the mid-price.
    <br />
    <a href="https://github.com/kostyafarber/crypto-lob-data-pipeline"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/kostyafarber/crypto-lob-data-pipeline">View Demo</a>
    ·
    <a href="https://github.com/kostyafarber/crypto-lob-data-pipeline/issues">Report Bug</a>
    ·
    <a href="https://github.com/kostyafarber/crypto-lob-data-pipeline/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][project-image]](https://example.com)

Intially this project was intended as a starting point to build an algorithmic trading system. I decided to explore HFT (High Frequency Trading) and wanted to use Market Microstructure variables to inform my trading strategy. I wanted to use perptual cryptocurrency instruments and use order flow imbalance.

I however, instead tok the chance to change this into a fun project to practise and learn Docker and Kafka. What ultimately came of it was a simple real-time streaming data pipeline.

Please check out my [website](https://kostyafarber.github.io/projects/crpyto-perpetual-futures-kafka-streaming) for more info!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Apache Kafka](https://kafka.apache.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose](https://www.docker.com/)
* [Deribit API V2.1.1](https://docs.deribit.com/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
### Installation

_This app was built using Docker. This solution assumes you have Docker installed on your machine_

1. Make sure you have API keys from Deribit and store them as `CLIENT_ID_DERIBIT` and `CLIENT_SECRET_DERIBIT` environment variables on your machine

1. Clone the repo

   ```sh
   git clone git@github.com:kostyafarber/crypto-lob-data-pipeline.git
   ```
2. Run the kafka and zookeeper container

   ```sh
   cd src/kafka
   docker-compose -f 'docker-compose.yml' up -d
   ```

Run the producer container

3. ```sh
    cd src/producer
    docker-compose -f 'docker-compose.yml' up 
    ```

Finally run the consumer container
  ```sh
  cd src/consumer
  docker-compose up -f `docker-compose.yml` up
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

What you should see is output that looks something like this:

![demo gif][demo-gif]

On the left is raw JSON being published to the kafka broker and on the right the JSON is being transformed with the order flow imbalance and mid-price being printed to the console.



<!-- USAGE EXAMPLES -->
## Architecture
The pipeline was built with the microservices principles in mind. Kafka, the Producer and Consumer are all in their own seperate docker containers and have no knowledge of each other apart from being on the same bridge network I defined in the `docker-compose.yml` files.

![architecture diagram][architecture-diagram]
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [] Add another script to make the consumer portion into a producer.

- [] Add docker youtube video in acknowledgments.

See the [open issues](https://github.com/kostyafarber/crypto-lob-data-pipeline/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Kostya Farber - kostya.farber@gmail.com

Project Link: [https://kostyafarber.github.io/projects/crpyto-perpetual-futures-kafka-streaming](https://kostyafarber.github.io/projects/crpyto-perpetual-futures-kafka-streaming)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[project-image]: images/kafka.png
[demo-gif]: images/kafka-demo.gif
[architecture-diagram]: images/kafka-crypto-pipeline.png

[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com

### Core Implementation Code & Architecture
#### File: `src/utilities/__init__.py`
```python

```

#### File: `src/utilities/utils.py`
```python
from datetime import datetime
import glob
import os

# API labels from Binance
labels_aggTrades = ['Aggregate tradeId', 'Price', 'Quantity', 'First TradeId', 'Last tradeId', 'Timestamp', 'Was the buyer the maker?', 'Was the trade the best price match?']
labels_klines = ["Time", "Open", "High", "Low", "Close", "Volume", "Close Time", "Quote Asset", "Number of Trades", "Taker buy base", "Taker buy Quote", "Ignore"]

# parse dates from Binance CSV (timestamp)
def parse_dates(timestamp: str):
    """
    A date parser which parses timestamps from binance for pandas dataframe.
    """
    return datetime.utcfromtimestamp(int(timestamp)/1000)

data_path = '../data/data/spot/monthly/aggTrades/ETHBTC/*'

files = glob.glob(data_path)

def get_api_keys(client_id, client_secret, aws=False):
    if aws:
        # obtain deribit api keys from aws
        ssm = boto3.client('ssm', region_name='ap-southeast-2')
        response = ssm.get_parameters(Names=[client_id, client_secret], WithDecryption=True)
        client_id = response['Parameters'][0]["Value"]
        client_secret = response['Parameters'][1]["Value"]
        return client_id, client_secret
    else:
        client_id = os.environ[client_id]
        client_secret = os.environ[client_secret]
        return client_id, client_secret


if __name__ == "__main__":
    print(files)
```

#### File: `src/consumer/lob_consumer.py`
```python
from kafka import KafkaConsumer
from json import loads
from datetime import datetime
import pandas as pd

class OrderbookConsumer():

    def __init__(self):

        self.consumer = KafkaConsumer(
        'prices',
        bootstrap_servers=['kafka:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-id',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

        self._data = dict(orderbook=pd.DataFrame(), ticker=pd.DataFrame())

    def parse(self):
        for data in self.consumer:
            event = data.value
            timestamp = datetime.fromtimestamp(event['params']['data']['timestamp']/1000)
            bids = event['params']['data']['bids']
            asks = event['params']['data']['asks']

            total_bids = 0
            total_asks = 0

            for bid, ask in zip(bids, asks):
                total_bids += bid[1]
                total_asks += ask[1]
            
            mid_price = (bids[0][0] + asks[0][0])/2
            net_ofi = (total_bids - total_asks)/(total_bids + total_asks)
            data = dict(timestamp=[timestamp], mid_price=[mid_price], net_ofi=[net_ofi])

            orderbook = pd.DataFrame(data)
            orderbook.set_index('timestamp')

            self._data['orderbook'] = pd.concat([self._data['orderbook'], orderbook], ignore_index=True, copy=False)
            print(self._data['orderbook'])
            #self._data = pd.merge_asof(self._data, orderbook, on='timestamp')
            
            #instrument = event['params']['data']['instrument_name']

if __name__ == '__main__':

    consumer = OrderbookConsumer()
    consumer.parse()
```

#### File: `src/producer/producer.py`
```python
from deribit import DeribitClient
from datetime import datetime
import pandas as pd
import os
import json
from kafka import KafkaProducer

client_id = os.environ["CLIENT_ID_DERIBIT"]
client_secret = os.environ["CLIENT_SECRET_DERIBIT"]

exchange_version = 'wss://www.deribit.com/ws/api/v2/'

class DeribitProducer(DeribitClient):
    def __init__(self, client_id, client_secret, testnet=False) -> None:
        """Generates crpyto data. Can collect and save to csv.

        Args:
            client_id (str): Public API Key
            client_secret (str): Private API Key
            testnet (bool, optional): Whether to use tesnet exchange. Defaults to False.
        """
        
        super().__init__(client_id, client_secret, testnet=testnet)
        self._data = dict(orderbook=pd.DataFrame(), ticker=pd.DataFrame())
        self.producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'])

    def _process_callback(self, response: json):
        """Override this method to process the callback message

        Args:
            response (json): Contains the response message from the websocket.
        """

        # processes LOB data
        if 'params' in response.keys() and response['method'] == 'subscription':
            if response['params']['channel'] == 'book.BTC-PERPETUAL.none.10.100ms':
                
                # send json to kafka topic
                self.producer.send(topic='prices', value=json.dumps(response).encode('utf-8'))
                print("message sent: {}".format(response))

    def _on_open_message(self):

        # To subscribe to this channel:
        msg = \
            {"jsonrpc": "2.0",
            "method": "public/subscribe",
            "id": 42,
            "params": {
                "channels": ['book.BTC-PERPETUAL.none.10.100ms']}
            }
        
        self.ws.send(json.dumps(msg))

if __name__ == '__main__':

    stream = DeribitProducer(client_id, client_secret)
    stream.start()
```

#### File: `src/producer/deribit.py`
```python
import time
import json
import hashlib
import hmac
import os
from websocket import WebSocketApp, enableTrace
from datetime import datetime, timedelta
import pandas as pd
import secrets
import sys
from argparse import ArgumentParser
from threading import Thread

# get api keys
client_id = os.environ["CLIENT_ID_DERIBIT"]
client_secret = os.environ["CLIENT_SECRET_DERIBIT"]

class DeribitClient(Thread, WebSocketApp):
    def __init__(self, client_id, client_secret, testnet=False) -> None:
        """Base client for Deribit apps.

        Args:
            client_id (str): Public API Key
            client_secret (str): Private API Key
            testnet (bool, optional): Whether to use testnet exchange. Defaults to False.
        """

        # housekeeping
        Thread.__init__(self)
        self.client_id = client_id
        self.client_secret = client_secret
        self.testnet = testnet
        self.exchange_version = self._set_exchange()
        self.time = datetime.now()
        self.expires_in = None
        self.heartbeat_requested_flag = 0
        self.heartbeat_set_flag = 0

        # Client Signature Authentication
        self.tstamp = str(int(time.time()) * 1000)
        self.data = ''
        self.nonce = secrets.token_urlsafe(10)
        self.base_signature_string = self.tstamp + "\n" + self.nonce + "\n" + self.data
        self.byte_key = client_secret.encode()
        self.message = self.base_signature_string.encode()
        self.signature = hmac.new(self.byte_key, self.message, hashlib.sha256).hexdigest()

        self.parser = ArgumentParser()
        self.args = self._add_args()
    
    def _set_exchange(self):
        if self.testnet:
            exchange_version = 'wss://test.deribit.com/ws/api/v2'
            return exchange_version
        else:
            exchange_version = 'wss://www.deribit.com/ws/api/v2/'
            return exchange_version

    def _authentication(self):
        # Initial Authentication
        ws_data = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "public/auth",
            "params": {
                "grant_type": "client_signature",
                "client_id": self.client_id,
                "timestamp": self.tstamp,
                "nonce": self.nonce,
                "signature": self.signature,
                "data": self.data}
        }
        
        self.ws.send(json.dumps(ws_data))

    def _on_message(self, ws, message):
            
        response = json.loads(message)
        
        self._process_callback(response)

        # housekeeping connection tasks
        if 'result' in response.keys(): 

            if response['result']['token_type'] == 'bearer':
                print(f'SUCCESSFULLY CONNECTED AT: {self.time.strftime("%Y-%m-%d %H:%M:%S")}\n')
            
                expires_in = response['result']['expires_in']
                self.expires_in = (self.time + timedelta(seconds=expires_in))
                print(f'AUTHENTICATION EXPIRES IN: {self.expires_in.strftime("%Y-%m-%d %H:%M:%S")}\n')


        # respond to a test request
        if 'params' in response.keys() and response['method'] == 'heartbeat':                                    # noqa: E501
            ws_data = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": "public/test",
                "params": {
                }
            }
            self.ws.send(json.dumps(ws_data))
        
        # heartbeat set success check and heartbeat response
        if 'params' in response.keys() and response['params']['type'] == 'heartbeat' and self.heartbeat_set_flag == 0:      # noqa: E501
            self.heartbeat_set_flag = 1
            print('Heartbeat Successfully Initiated at: ' + str(datetime.now().time().strftime('%H:%M:%S'))) 
        
    def _on_open(self, ws):

        self._authentication()

         # Initiating Heartbeat
        if self.heartbeat_set_flag == 0 and self.heartbeat_requested_flag == 0:                                                     # noqa: E501
            self.heartbeat_requested_flag = 1
            print('Heartbeat Requested at: ' + str(datetime.now().time().strftime('%H:%M:%S')))                                     # noqa: E501
            ws_data = {
                        "jsonrpc": "2.0",
                        "id": 1,
                        "method": "public/set_heartbeat",
                        "params": {
                            "interval": 60
                        }
                        }
            self.ws.send(json.dumps(ws_data))

        self._on_open_message()

    def _on_close(self, ws):
        #print('CONNECTION CLOSED AT: ' + str(datetime.now().time().strftime('%H:%M:%S')))  # noqa: E501
        print('Attempting Reconnection at: ' + str(datetime.now().time().strftime('%H:%M:%S')))  # noqa: E501
        self.run()

    def run(self):
        self.ws = WebSocketApp(self.exchange_version, on_message=self._on_message, on_open=self._on_open)
    
        if self.args.trace:
            enableTrace(True)   

        # run forever
        while True:
            try:
                self.ws.run_forever()
            except:
                continue
    
    # override this method to process the websocket response
    def _process_callback(self, response):
        pass

    def _on_open_message(self):
        pass

    def _add_args(self):

        self.parser.add_argument('--trace', type=bool)
        self.parser.add_argument('--testnet', type=bool)
        args = self.parser.parse_args()

        return args
        

if __name__ == '__main__':

    test = DeribitClient(client_id, client_secret, testnet=True)
    test.start()
```


==================================================


## [2/3] Repository: orderbook-heatmap (`WHEEL_orderbook-heatmap`)
- **Full Name**: `orderbook-heatmap`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# orderbook-heatmap

A focused, real-time **L2 order-flow terminal**: it connects to a live order book feed
(Binance public depth + trade WebSocket streams), maintains a local book from the diffs, and
turns raw microstructure into things you can read at a glance — a **Bookmap-style liquidity
heatmap**, **book imbalance**, **delta / cumulative delta**, **liquidity clusters**,
**absorption detection**, and a transparent **setup score**.

Raw L2 in, actionable intelligence out. Everything runs in the browser — no account, no API key,
no backend.

> This is a market-data **visualization / analysis** tool — **not trading or investment advice**.

---

## Screenshots

**Live liquidity heatmap + order-flow metrics (BTC/USDT).** Green = resting bid depth, red =
resting ask depth, brightness ∝ size. The white line is mid price traveling *through* the book;
persistent horizontal bands are liquidity clusters. Here rolling delta is positive (+109) while the
book is ask-heavy (−36.5%) — a textbook flow / near-touch divergence.

![BTC liquidity heatmap](screenshots/heatmap-btc.png)

**Absorption at support (BTC/USDT).** Price sells into the 67,836 bid cluster with heavy
sell-side aggression (rolling delta −154, cumulative −246) but refuses to break — the resting bid
soaks the flow. The **Absorption — sell-side flow held** flag fires and the setup read tilts short
into the failed push.

![Absorption at a bid cluster](screenshots/heatmap-absorb.png)

**Price working through resistance (ETH/USDT).** Mid rallies up into the 3,553.84 ask band; you
can see the band get chewed (green intrudes into red) as offers lift, then depth rebuilds above.

![ETH liquidity heatmap](screenshots/heatmap-eth.png)

<sub>Screenshots are generated headlessly by [`src/capture.py`](src/capture.py),
which drives the **real application code** but swaps the live socket for a synthetic feed that
replays the exact Binance message shapes — so a CI box with no market access renders a
deterministic frame. Point a browser at `index.html` for the genuine live feed. See
[Reproducing the screenshots](#reproducing-the-screenshots).</sub>

---

## Quick start

No build step. Serve the folder and open it:

```bash
# any static server works
python -m http.server 5500
# → open http://localhost:5500
```

Or, in VS Code, install **Live Server** and right-click `index.html` → *Open with Live Server*.

Pick a symbol (BTC / ETH / SOL / BNB) from the dropdown; the app opens the Binance WebSocket on
load and the heatmap and metrics update live. A modern browser is all that's required — WebSocket,
Canvas, and ES modules are built in.

---

## What the signals mean

Everything here is derived from two raw inputs — the **L2 book** (resting limit orders) and the
**trade tape** (executions). The point is to make the microstructure legible, not to bury it.

| Signal | Read |
| --- | --- |
| **Liquidity heatmap** | Where size is resting, over time, on an absolute price axis. Thick persistent bands = liquidity clusters; a band that thins as price approaches = liquidity being pulled. |
| **Book imbalance** | Summed bid vs ask size across the top 20 levels → `[-1,+1]`. Which side is *stacked* near the touch right now. |
| **Delta** (rolling 5 s) | Signed aggressor volume — buys that lifted the offer minus sells that hit the bid. Current directional *pressure* from the tape. |
| **Cumulative delta** | Session running sum of delta. Persistent one-sided aggression trends; **divergence from price is the classic absorption read**. |
| **Liquidity clusters** | The heaviest resting level above and below mid, drawn as dashed *target levels* — where price tends to gravitate and stall. |
| **Absorption** | Large delta meeting a book that won't move: strong aggression, tiny price range → flow is being *absorbed* by resting size. |
| **Setup read** | A transparent 0–100 blend of imbalance, flow, and location, with a LONG/SHORT/FLAT bias. Every driver is shown, so you see *why*, not just a number. |

---

## How it works

### Data in
One **combined** Binance stream:

```
wss://stream.binance.com:9443/stream?streams=<symbol>@depth@100ms/<symbol>@aggTrade
```

- **`@depth@100ms`** — L2 order book *diffs* every 100 ms: `{ b: [[price, qty], …], a: [...] }`.
  A `qty` of `0` means the level was removed.
- **`@aggTrade`** — aggregated trades, each with a size and a maker flag used to classify the
  aggressor side.

### The local order book (`OrderBook`)
Maintained **incrementally** from the diffs — levels are inserted/updated and `qty 0` deletes
them, rather than rebuilt on every message. Bids and asks live in maps; top-of-book is cached and
only recomputed when the book actually changes.

### Metrics
**Book imbalance** — `(bidVol − askVol) / (bidVol + askVol)` over the top *N* levels (default 20).
`+1` = all near-touch size is on the bid.

**Delta** — Binance's `m` flag says whether the buyer was the maker: `m = true` → the **seller**
aggressed (hit the bid) → **negative**; `m = false` → the **buyer** lifted the offer →
**positive**. Summed over a rolling window (default 5 s).

**Cumulative delta** — the running session sum; trend and price-divergence are the absorption cue.

### The liquidity heatmap (`Heatmap`)
A scrolling ring of columns. Every ~120 ms the book is snapshotted into a new column: resting size
is bucketed by price and written to the grid — green for bids, red for asks, brightness scaled to
size (with a `sqrt` lift so small size stays visible and a smoothed normaliser so one iceberg
can't wash out the map).

Crucially the price axis is **absolute**, not centred per-column: every column uses the *same*
price→row mapping, so persistent size renders as **true horizontal bands** (à la Bookmap) and the
mid-price line travels *through* the liquidity instead of being pinned to the centre. The axis
auto-ranges only when price nears an edge, shifting stored rows so existing bands keep their real
price.

### Signals on top
**Liquidity clusters** — the heaviest in-view resting level on each side of mid, surfaced as
dashed target lines and a table (support / resistance, size, distance). **Absorption** — flagged
when rolling |delta| is large while the 5 s mid range stays tiny. **Setup read** — a weighted,
fully itemised blend of imbalance, rolling/cumulative flow, and proximity to a cluster.

### Rendering, decoupled from ingestion
WebSocket callbacks only **mutate in-memory state**. A separate `requestAnimationFrame` loop reads
that state and paints once per frame. A burst of hundreds of messages updates state cheaply;
painting still happens at a steady frame rate rather than once per message.

---

## Performance notes

- **Incremental order book** — updated from diffs, never rebuilt per message; top-of-book cached.
- **Bounded history** — the heatmap keeps only on-screen columns in a fixed ring; old columns are
  overwritten in place (typed `Float32Array`, no per-frame allocation).
- **Ingestion / render separation** — data callbacks are cheap; drawing is batched to one paint
  per frame.
- **Robust, allocation-aware hot path** — a smoothed normaliser and `sqrt` intensity keep the map
  readable under a fast feed without re-scanning history.

---

## Project structure

```
orderbook-heatmap/
├── index.html            # the whole app: layout, styling, and the module script
├── README.md
├── docs/                 # original brief + reference sketch
├── src/
│   └── capture.py        # headless-Chrome screenshot pipeline (stdlib only)
└── screenshots/
    └── *.png
```

The app is a single file so it runs with zero build. The script is organised into clear units —
`OrderBook`, metrics, `Heatmap`, the signal layer, and the app wiring — that map directly onto the
sections above. To move to a TypeScript build, each unit becomes its own `.ts` module
(`book.ts`, `metrics.ts`, `heatmap.ts`, `signals.ts`, `app.ts`) bundled with Vite/esbuild; the
logic is already separated along those lines. The app also exposes a small **feed seam**
(`window.__feed`) so the live socket can be swapped for a replay/simulated source without touching
the compute or render code — which is exactly how the screenshots are produced.

---

## Reproducing the screenshots

```bash
python src/capture.py
```

It injects a synthetic Binance feed (defining `window.__feed`) into a copy of `index.html`,
launches headless Chrome, lets the real app run until the heatmap fills, and captures each frame
over the DevTools Protocol using only the Python standard library. The synthetic feed emits the
exact `@depth` / `@aggTrade` message shapes, so the production ingest/compute/render path runs
unmodified.

---

## Extending it

- **Footprint view** — bucket executed volume by price and time for bid/ask traded volume per cell.
- **Multi-venue** — add other exchange feeds behind the same `OrderBook` / metrics interface.
- **Probability calibration** — fit the setup score against forward outcomes instead of fixed
  weights.
- **TypeScript build** — split the units into `.ts` modules and bundle with Vite for types and
  tree-shaking.

---

## Notes

- Uses Binance's public market-data streams, which require no authentication.
- All computation is client-side; nothing is sent anywhere.
- Again: a visualization / analysis tool — **not trading or investment advice**.

### Core Implementation Code & Architecture
#### File: `src/capture.py`
```python
#!/usr/bin/env python3
"""
Screenshot pipeline for orderbook-heatmap.

1. Reads the shipped index.html and injects a tiny synthetic Binance feed that
   defines window.__feed(...) — the app's documented feed seam. The REAL app
   code (OrderBook / metrics / Heatmap / signals) runs unchanged; only the data
   source is swapped, so the screenshots show the genuine rendering pipeline.
2. Launches headless Chrome, lets the feed run in real time until the heatmap
   fills, then captures a screenshot over the DevTools Protocol (pure-stdlib
   WebSocket client — no third-party packages).
"""
import base64, json, os, re, socket, subprocess, sys, time, urllib.request, tempfile, struct, secrets

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.html")
OUTDIR = os.path.join(ROOT, "screenshots")
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# --- synthetic feed: emits exactly the Binance combined-stream message shapes --
SIM_JS = r"""
<script>
// Synthetic Binance depth/aggTrade feed for deterministic screenshots.
// Emits { stream, data } messages in the exact shape the app parses, so the
// production code path (applyDiff / delta / heatmap) runs untouched.
(function () {
  const P = new URLSearchParams(location.search);
  const SYMBOL   = P.get("symbol")   || "btcusdt";
  const SCENARIO = P.get("scenario") || "flow";
  let seed = (parseInt(P.get("seed") || "7", 10) >>> 0) || 7;
  const rnd = () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; };

  const CFG = {
    btcusdt: { px: 68000, dec: 1, step: 3.0 },
    ethusdt: { px: 3550,  dec: 2, step: 0.16 },
    solusdt: { px: 172.0, dec: 3, step: 0.008 },
    bnbusdt: { px: 605.0, dec: 2, step: 0.03 },
  }[SYMBOL] || { px: 100, dec: 2, step: 0.05 };

  const dec = CFG.dec, step = CFG.step, start = CFG.px;
  const round = (p) => +p.toFixed(dec);
  let mid = start, drift = 0, t0 = performance.now();

  // persistent resting clusters at fixed absolute prices → horizontal bands
  const clusters = [-0.0024, -0.0012, 0.0011, 0.0025].map((f) => ({
    price: round(start * (1 + f)), size: 45 + rnd() * 70,
  }));

  const levelSize = (price) => {
    let s = 2.5 + rnd() * 6;
    for (const c of clusters) {
      const d = Math.abs(price - c.price);
      if (d < step * 1.6) s += c.size * (1 - d / (step * 1.6));
    }
    return +s.toFixed(3);
  };

  // separate bid/ask books so a price that flips side is removed from the old
  // side and set on the new one — Binance depth diffs never cross the book.
  let emittedB = new Map(), emittedA = new Map();
  function depthTick(on) {
    const elapsed = performance.now() - t0;
    const absorbing = SCENARIO === "absorb" && elapsed > 19000;
    // random-walk mid with mean reversion; in the absorb scene, pin it (a big
    // resting bid soaks the selling and price refuses to break).
    drift = drift * 0.9 + (rnd() - 0.5) * step * 0.7 + (start - mid) * 0.0009;
    if (absorbing) drift = drift * 0.15 + (start - mid) * 0.02;
    mid = mid + drift;
    const bestBid = round(mid - step * 0.5), bestAsk = round(mid + step * 0.5);
    const N = 80, nb = new Map(), na = new Map(), b = [], a = [];
    for (let i = 0; i < N; i++) {
      const bp = round(bestBid - i * step); if (bp < mid) nb.set(bp, levelSize(bp));
      const ap = round(bestAsk + i * step); if (ap > mid) na.set(ap, levelSize(ap));
    }
    for (const [p, q] of nb) if (emittedB.get(p) !== q) b.push([p.toFixed(dec), q.toFixed(3)]);
    for (const [p] of emittedB) if (!nb.has(p)) b.push([p.toFixed(dec), "0"]);
    for (const [p, q] of na) if (emittedA.get(p) !== q) a.push([p.toFixed(dec), q.toFixed(3)]);
    for (const [p] of emittedA) if (!na.has(p)) a.push([p.toFixed(dec), "0"]);
    emittedB = nb; emittedA = na;
    on.message({ stream: SYMBOL + "@depth", data: { b, a } });
  }

  function tradeTick(on) {
    const elapsed = performance.now() - t0;
    let up = 0.5 + (drift / (step * 1.2)) * 0.5;
    if (SCENARIO === "absorb" && elapsed > 19000) up = 0.18;   // heavy selling into support
    up = Math.max(0.12, Math.min(0.88, up));
    const n = 1 + (rnd() * 4 | 0);
    for (let i = 0; i < n; i++) {
      const buyerAggresses = rnd() < up;
      const q = 0.4 + rnd() * rnd() * 9;
      on.message({ stream: SYMBOL + "@aggTrade", data: { q: q.toFixed(4), m: !buyerAggresses } });
    }
  }

  window.__feed = function (symbol, on) {
    setTimeout(() => on.open(), 0);
    // seed a full book immediately so the first frame has depth
    depthTick(on);
    const d = setInterval(() => depthTick(on), 100);
    const tr = setInterval(() => tradeTick(on), 130);
    return { close() { clearInterval(d); clearInterval(tr); } };
  };
})();
</script>
"""

def build_harness():
    html = open(INDEX, "r", encoding="utf-8").read()
    # inject the sim right before the app's module script so the <select> exists
    # and window.__feed is defined before the module boots
    marker = '<script type="module">'
    assert marker in html, "module script marker not found"
    # also let ?symbol= drive the dropdown before boot
    boot = ('<script>window.addEventListener("DOMContentLoaded",()=>{});'
            'var __s=new URLSearchParams(location.search).get("symbol");'
            'if(__s){var el=document.getElementById("symbol");if(el)el.value=__s;}</script>\n')
    html = html.replace(marker, SIM_JS + boot + marker, 1)
    out = os.path.join(OUTDIR, "harness.html")
    open(out, "w", encoding="utf-8").write(html)
    return out


# ----------------------------- minimal CDP client ---------------------------
class WS:
    def __init__(self, url):
        m = re.match(r"ws://([^:/]+):(\d+)(/.*)", url)
        host, port, path = m.group(1), int(m.group(2)), m.group(3)
        self.s = socket.create_connection((host, port), timeout=30)
        self.s.settimeout(40)
        key = base64.b64encode(secrets.token_bytes(16)).decode()
        req = (f"GET {path} HTTP/1.1\r\nHost: {host}:{port}\r\nUpgrade: websocket\r\n"
               f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n")
        self.s.sendall(req.encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += self.s.recv(4096)

    def _read(self, n):
        out = b""
        while len(out) < n:
            chunk = self.s.recv(n - len(out))
            if not chunk:
                raise ConnectionError("socket closed")
            out += chunk
        return out

    def send(self, obj):
        payload = json.dumps(obj).encode()
        header = bytearray([0x81])  # FIN + text
        ln = len(payload)
        mask = secrets.token_bytes(4)
        if ln < 126:
            header.append(0x80 | ln)
        elif ln < 65536:
            header.append(0x80 | 126); header += struct.pack(">H", ln)
        else:
            header.append(0x80 | 127); header += struct.pack(">Q", ln)
        masked = bytes(b ^ mask[i % 4] for i, b in enumerate(payload))
        self.s.sendall(bytes(header) + mask + masked)

    def recv(self):
        data = b""
        while True:
            b1, b2 = self._read(2)
            opcode = b1 & 0x0F
            ln = b2 & 0x7F
            if ln == 126:
                ln = struct.unpack(">H", self._read(2))[0]
            elif ln == 127:
                ln = struct.unpack(">Q", self._read(8))[0]
            payload = self._read(ln) if ln else b""
            if opcode == 0x8:
                raise ConnectionError("ws closed by peer")
            data += payload
            if b1 & 0x80:  # FIN
                break
        return json.loads(data.decode())

    def call(self, mid, method, params=None):
        self.send({"id": mid, "method": method, "params": params or {}})
        while True:
            msg = self.recv()
            if msg.get("id") == mid:
                return msg


def capture(symbol, scenario, seed, outfile, wait=27, port=9333):
    harness = "file:///" + build_harness().replace("\\", "/")
    url = f"{harness}?symbol={symbol}&scenario={scenario}&seed={seed}"
    profile = tempfile.mkdtemp(prefix="ch-ob-")
    args = [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
            "--no-first-run", "--no-default-browser-check", "--mute-audio",
            "--force-color-profile=srgb", "--force-device-scale-factor=2",
            "--window-size=1520,940", f"--user-data-dir={profile}",
            f"--remote-debugging-port={port}", url]
    proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        ws_url = None
        for _ in range(60):
            try:
                targets = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=2))
                for tt in targets:
                    if tt.get("type") == "page" and tt.get("webSocketDebuggerUrl"):
                        ws_url = tt["webSocketDebuggerUrl"]; break
                if ws_url:
                    break
            except Exception:
                pass
            time.sleep(0.5)
        if not ws_url:
            raise RuntimeError("no CDP page target")
        print(f"  feeding {symbol}/{scenario} for {wait}s ...", flush=True)
        time.sleep(wait)  # let the real-time synthetic feed fill the heatmap
        ws = WS(ws_url)
        res = ws.call(1, "Page.captureScreenshot", {"format": "png", "captureBeyondViewport": False})
        png = base64.b64decode(res["result"]["data"])
        open(outfile, "wb").write(png)
        print(f"  wrote {outfile} ({len(png)//1024} KB)", flush=True)
    finally:
        proc.terminate()
        try: proc.wait(timeout=10)
        except Exception: proc.kill()


if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    shots = [
        ("btcusdt", "flow",   7,  "heatmap-btc.png",     9333),
        ("ethusdt", "flow",   19, "heatmap-eth.png",     9334),
        ("btcusdt", "absorb", 31, "heatmap-absorb.png",  9335),
    ]
    for sym, scen, seed, name, port in shots:
        print(f"[{name}]")
        capture(sym, scen, seed, os.path.join(OUTDIR, name), port=port)
    print("done")
```


==================================================


## [3/3] Repository: High-Frequency-Trading-FPGA-System (`PHASE4-QUANT-003`)
- **Full Name**: `PHASE4-QUANT-003_muditbhargava66__High-Frequency-Trading-FPGA-System`
- **Description**: The High-Frequency Trading FPGA System is an ultra-low latency platform for electronic trading on FPGAs. It features a TCP/IP stack, order matching engine, custom IP core, and risk management module for accelerated and reliable trade execution.
- **GitHub Stars**: 194
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# High-Frequency Trading FPGA System

This repository contains the code and documentation for a high-frequency trading (HFT) system implemented on an FPGA. The system utilizes a TCP/IP stack for communication, an order matching engine for trade execution, and a custom IP core for accelerated processing. The design is optimized for ultra-low latency and high throughput.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Directory Structure](#directory-structure)
- [System Overview](#system-overview)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
  - [Testbench Hierarchy](#testbench-hierarchy)
  - [Running Tests](#running-tests)
- [Synthesis and Implementation](#synthesis-and-implementation)
  - [Resource Utilization](#resource-utilization)
  - [Timing Analysis](#timing-analysis)
- [Deployment](#deployment)
- [Future Work](#future-work)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The High-Frequency Trading FPGA System is designed to provide a high-performance and low-latency solution for electronic trading. It leverages the power of FPGAs to achieve deterministic and fast execution of trading algorithms. The system includes a full-featured TCP/IP stack for reliable communication, an order matching engine for efficient trade matching, and a custom IP core for accelerated processing of financial data.

## Features
- Ultra-low latency and high throughput design
- Full-featured TCP/IP stack for reliable communication
- Order matching engine for efficient trade execution
  - Support for advanced order types (limit, market, stop, trailing stop)
  - Multiple execution strategies (aggressive, passive, iceberg, VWAP)
- Custom IP core for accelerated processing of financial data
- Risk management module for trade validation and position monitoring
- Modular and parameterizable design for easy customization
- Comprehensive testbench and verification environment
- Detailed documentation and usage instructions

## Directory Structure
```
|- hft_fpga_system/
   |- hft_fpga_system.srcs/
      |- sources_1/
         |- new/
            |- order_matching_engine.v
            |- tcp_ip_stack.v
            |- ethernet_layer.v
            |- ip_layer.v
            |- tcp_layer.v
            |- custom_ip_core.v
            |- axi_stream_if.v
            |- risk_management.v
            |- top_level.v
      |- constrs_1/
         |- new/
            |- timing_constraints.xdc
      |- sim_1/
         |- new/
            |- tb_order_matching_engine.v
            |- tb_tcp_ip_stack.v
            |- tb_custom_ip_core.v
            |- tb_risk_management.v
            |- tb_top_level.v
   |- hft_fpga_system.xpr
```

## System Overview
The High-Frequency Trading FPGA System is built on a modular architecture that allows for seamless integration of various components. The system consists of the following key modules:

- **TCP/IP Stack**: Implements the TCP/IP protocol for reliable communication with the trading infrastructure. It includes the Ethernet layer, IP layer, and TCP layer.
- **Order Matching Engine**: Performs real-time matching of buy and sell orders based on price-time priority. It supports advanced order types and multiple execution strategies.
- **Custom IP Core**: Accelerates specific processing tasks related to financial data. It can be customized based on specific algorithmic trading requirements.
- **Risk Management Module**: Validates trades and monitors positions to ensure compliance with risk limits and regulations.
- **AXI Stream Interfaces**: Enables seamless integration of custom IP cores with the rest of the system.

## Architecture
The architecture of the High-Frequency Trading FPGA System is designed to optimize for low latency and high throughput. The system utilizes a pipelined architecture to achieve maximum performance.

The data flow begins with the receipt of Ethernet packets through the Ethernet layer. The packets are then processed by the IP layer and forwarded to the TCP layer. The TCP layer ensures reliable, connection-oriented communication and passes the data to the order matching engine.

The order matching engine receives orders from the TCP layer and performs real-time matching based on the specified order types and execution strategies. The matched trades are then sent back to the TCP layer for transmission to the trading infrastructure.

The custom IP core can be integrated into the system using AXI Stream interfaces. It can perform specialized processing tasks on financial data to accelerate trading algorithms.

The risk management module monitors the trades and positions to ensure compliance with predefined risk limits. It validates trades before execution and provides real-time position monitoring.

![Block Diagram](/images/hft-fpga-png-output.png)

## Getting Started

### Prerequisites
To use and modify the High-Frequency Trading FPGA System, you need the following:
- Xilinx Vivado Design Suite (version 2020.2 or later)
- FPGA development board (e.g., Xilinx Virtex UltraScale+ or Kintex UltraScale+)
- Trading infrastructure and market data feed
- Knowledge of Verilog and FPGA development

### Installation
1. Clone the repository:
   ```
   git clone https://github.com/muditbhargava66/High-Frequency-Trading-FPGA-System.git
   ```
2. Open Xilinx Vivado and create a new project.
3. Add the source files from the `sources_1/new` directory to the project.
4. Add the constraint file `timing_constraints.xdc` from the `constrs_1/new` directory to the project.
5. Set the target FPGA device and configure the project settings accordingly.

## Usage
1. Customize the parameters and configuration settings in the top-level module (`top_level.v`) to match your specific requirements.
2. Modify the custom IP core (`custom_ip_core.v`) to implement your desired processing logic.
3. Update the risk management module (`risk_management.v`) with your specific risk limits and monitoring rules.
4. Verify the functionality of the system using the provided testbenches.
5. Run synthesis and implementation to generate the bitstream.
6. Program the FPGA with the generated bitstream.
7. Integrate the FPGA system with your trading infrastructure and market data feed.

## Testing

### Testbench Hierarchy
The repository includes a comprehensive testbench environment to verify the functionality of the High-Frequency Trading FPGA System. The testbench hierarchy is as follows:

- `tb_order_matching_engine.v`: Testbench for the order matching engine module.
- `tb_tcp_ip_stack.v`: Testbench for the TCP/IP stack module.
- `tb_custom_ip_core.v`: Testbench for the custom IP core module.
- `tb_risk_management.v`: Testbench for the risk management module.
- `tb_top_level.v`: Top-level testbench for the entire system.

### Running Tests
To run the tests:
1. Open the testbench files in Xilinx Vivado.
2. Set up the simulation environment and configure the test parameters.
3. Run the simulation and observe the results.
4. Verify that the system behaves as expected and meets the specified requirements.

## Synthesis and Implementation

### Resource Utilization
After running synthesis and implementation, review the resource utilization report to ensure that the design fits within the available FPGA resources. Optimize the design if necessary to meet the resource constraints.

### Timing Analysis
Analyze the timing reports generated by Vivado to verify that the design meets the required timing constraints. Pay attention to the worst negative slack (WNS) and total negative slack (TNS) values. Ensure that there are no timing violations.

If timing violations are present, review the critical paths and optimize the design accordingly. Consider pipelining, register balancing, and other optimization techniques to improve timing performance.

## Deployment
To deploy the High-Frequency Trading FPGA System:
1. Connect the FPGA development board to your trading infrastructure.
2. Configure the network settings and ensure connectivity.
3. Program the FPGA with the generated bitstream.
4. Integrate the FPGA system with your trading software and market data feed.
5. Monitor the system performance and verify the trading functionality.

## Future Work
The following tasks and features are planned for future development and improvement of the High-Frequency Trading FPGA System:
- [x] Implement advanced order types and execution strategies
- [x] Enhance the risk management module for better trade validation and position monitoring
- [ ] Optimize the TCP/IP stack for even lower latency and higher throughput
- [ ] Integrate market data feed parsers for real-time price updates
- [ ] Develop a user-friendly web interface for system monitoring and configuration
- [ ] Conduct extensive performance testing and benchmarking
- [ ] Implement failover and redundancy mechanisms for increased reliability
- [ ] Explore the use of machine learning algorithms for predictive trading
- [ ] Integrate with additional trading venues and protocols
- [ ] Provide comprehensive documentation and user guides

## Contributing
Contributions to the High-Frequency Trading FPGA System are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Make sure to follow the contribution guidelines outlined in the repository.

## License
The High-Frequency Trading FPGA System is open-source and released under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for both commercial and non-commercial purposes.


## Star History

<a href="https://star-history.com/#muditbhargava66/High-Frequency-Trading-FPGA-System&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=muditbhargava66/High-Frequency-Trading-FPGA-System&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=muditbhargava66/High-Frequency-Trading-FPGA-System&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=muditbhargava66/High-Frequency-Trading-FPGA-System&type=Date" />
 </picture>
</a>


==================================================
