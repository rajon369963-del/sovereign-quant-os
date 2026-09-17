# ⚡ [QUANT-SOURCE-024] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_024_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: dhan-java-sdk (`WHEEL_dhan-java-sdk`)
- **Full Name**: `dhan-java-sdk`
- **Description**: Unofficial Kotlin/Java SDK for the DhanHQ Trading API.
- **GitHub Stars**: 1
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Dhan Java SDK

[![Maven Central](https://img.shields.io/maven-central/v/io.github.sonicalgo/dhan-java-sdk)](https://central.sonatype.com/artifact/io.github.sonicalgo/dhan-java-sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Java](https://img.shields.io/badge/Java-11%2B-blue)](https://www.oracle.com/java/)

Unofficial Kotlin/Java SDK for the [Dhan](https://dhanhq.co) trading platform. Supports REST APIs and real-time WebSocket streaming.

## Installation

### Gradle (Kotlin DSL)

```kotlin
implementation("io.github.sonicalgo:dhan-java-sdk:2.2.0")
```

### Gradle (Groovy)

```groovy
implementation 'io.github.sonicalgo:dhan-java-sdk:2.2.0'
```

### Maven

```xml
<dependency>
    <groupId>io.github.sonicalgo</groupId>
    <artifactId>dhan-java-sdk</artifactId>
    <version>2.0.0</version>
</dependency>
```

## Quick Start

<details open>
<summary>Kotlin</summary>

```kotlin
import io.github.sonicalgo.dhan.Dhan
import io.github.sonicalgo.dhan.usecase.*
import io.github.sonicalgo.dhan.common.*

// Create SDK instance
val dhan = Dhan.builder()
    .clientId("your-client-id")
    .accessToken("your-access-token")
    .build()

// Get user profile
val profile = dhan.getProfile()
println("Client: ${profile.dhanClientId}")

// Get market quote
val ltps = dhan.getLtp(mapOf(
    "NSE_EQ" to listOf(1333)  // HDFC Bank
))
println("LTP: ${ltps["NSE_EQ"]?.get("1333")?.lastPrice}")

// Place an order
val response = dhan.placeOrder(PlaceOrderParams {
    transactionType = TransactionType.BUY
    exchangeSegment = ExchangeSegment.NSE_EQ
    productType = ProductType.CNC
    orderType = OrderType.LIMIT
    validity = Validity.DAY
    securityId = "1333"
    quantity = 10
    price = 1428.0
})
println("Order ID: ${response.orderId}")
```

</details>

<details>
<summary>Java</summary>

```java
import io.github.sonicalgo.dhan.Dhan;
import io.github.sonicalgo.dhan.usecase.*;
import io.github.sonicalgo.dhan.common.*;
import java.util.Map;
import java.util.List;

// Create SDK instance
Dhan dhan = Dhan.builder()
    .clientId("your-client-id")
    .accessToken("your-access-token")
    .build();

// Get user profile
var profile = dhan.getProfile();
System.out.println("Client: " + profile.getDhanClientId());

// Get market quote
var ltps = dhan.getLtp(Map.of(
    "NSE_EQ", List.of(1333)  // HDFC Bank
));
System.out.println("LTP: " + ltps.get("NSE_EQ").get("1333").getLastPrice());

// Place an order using builder
var response = dhan.placeOrder(PlaceOrderParamsBuilder.builder()
    .transactionType(TransactionType.BUY)
    .exchangeSegment(ExchangeSegment.NSE_EQ)
    .productType(ProductType.CNC)
    .orderType(OrderType.LIMIT)
    .validity(Validity.DAY)
    .securityId("1333")
    .quantity(10)
    .price(1428.0)
    .build());
System.out.println("Order ID: " + response.getOrderId());
```

</details>

> **Note:** All code examples below assume you have initialized the SDK as shown above:
> ```kotlin
> val dhan = Dhan.builder()
>     .clientId("your-client-id")
>     .accessToken("your-access-token")
>     .build()
> ```

## Type-Safe Enums

The SDK uses type-safe enums throughout the API responses for better code safety and IDE support:

```kotlin
// Order response uses enums
val order = dhan.getOrderById("order-id")
when (order.orderStatus) {
    OrderStatus.TRADED -> println("Order filled")
    OrderStatus.REJECTED -> println("Order rejected")
    OrderStatus.PENDING -> println("Order pending")
    OrderStatus.PART_TRADED -> println("Partial fill: ${order.filledQty}/${order.quantity}")
    else -> println("Status: ${order.orderStatus}")
}

// Position uses enums
val positions = dhan.getPositions()
positions.filter { it.positionType == PositionType.LONG }
    .forEach { println("Long position: ${it.tradingSymbol}") }
```

**Available enums:**

| Category | Enums |
|----------|-------|
| Trading | `ExchangeSegment`, `TransactionType`, `ProductType`, `OrderType`, `Validity` |
| Order Status | `OrderStatus`, `AmoTime`, `LegName` |
| Forever Orders | `ForeverOrderFlag` |
| Historical Data | `ChartInterval`, `InstrumentType` |
| Portfolio | `PositionType` |
| Options | `DrvOptionType` |
| Auth/Config | `IpFlag`, `KillSwitchStatus`, `DdpiStatus`, `MtfStatus`, `DataPlanStatus` |
| EDIS | `EdisStatus`, `Exchange`, `Segment` |

## Why This SDK?

- **Modern & Secure** - Built with latest libraries (OkHttp 5.x, Jackson 2.x) with no known vulnerabilities
- **WebSocket Ready** - Binary protocol parsing for market feed; no manual binary handling needed
- **Auto-Reconnection** - WebSocket clients automatically reconnect with exponential backoff
- **Simple API** - Clean builder pattern: `Dhan.builder().clientId("id").accessToken("token").build()`
- **Type-Safe** - Kotlin data classes with proper types; no raw Maps or Object casting
- **Rich Error Handling** - Exceptions with helpers like `isRateLimitError`, `isAuthenticationError`
- **Thread-Safe** - Designed for concurrent usage in trading applications
- **Resource Management** - Implements `Closeable` for clean resource cleanup

## Features

- **43 REST API operations** - Orders, Portfolio, Market Quotes, Historical Data, Option Chain, and more
- **Real-time market data** - WebSocket streaming with binary protocol (low latency)
- **Real-time order updates** - Order and trade updates via WebSocket
- **Automatic reconnection** - WebSocket clients reconnect with exponential backoff
- **Configurable rate limiting** - Automatic retry with exponential backoff for HTTP 429
- **Debug logging** - Optional HTTP request/response logging for troubleshooting
- **Full Kotlin & Java compatibility** - Use from either language

---

## API Reference

| Method | Description |
|--------|-------------|
| **Authentication** | |
| `generateConsent(appId, appSecret)` | Generate consent app ID for auth flow |
| `consumeConsent(tokenId, appId, appSecret)` | Exchange token for access credentials |
| `getProfile()` | Get user profile |
| `setIp()` | Set static IP for order APIs |
| `modifyIp()` | Modify IP (once per 7 days) |
| `getIpConfiguration()` | Get current IP config |
| `renewToken()` | Extend token validity |
| **Orders** | |
| `placeOrder()` | Place a single order |
| `placeSlicingOrder()` | Place slicing order (auto-split) |
| `modifyOrder()` | Modify an existing order |
| `cancelOrder()` | Cancel an order |
| `getOrders()` | Get all orders for the day |
| `getOrderById()` | Get specific order |
| `getOrderByCorrelationId()` | Get order by correlation ID |
| `getTrades()` | Get all trades for the day |
| `getTradesByOrderId()` | Get trades for specific order |
| **Super Orders** | |
| `placeSuperOrder()` | Place super order (entry + target + SL) |
| `modifySuperOrder()` | Modify super order leg |
| `cancelSuperOrder()` | Cancel super order leg |
| `getSuperOrders()` | Get all super orders |
| **Forever Orders (GTT)** | |
| `placeForeverOrder()` | Place GTT order |
| `modifyForeverOrder()` | Modify GTT order |
| `cancelForeverOrder()` | Cancel GTT order |
| `getForeverOrders()` | Get all GTT orders |
| **Portfolio** | |
| `getHoldings()` | Get holdings |
| `getPositions()` | Get positions |
| `convertPosition()` | Convert position product type |
| **Funds** | |
| `getFundLimits()` | Get fund limits |
| `calculateMargin()` | Calculate margin requirements |
| **Market Quotes** | |
| `getLtp()` | Get last traded price |
| `getOhlc()` | Get OHLC data |
| `getQuote()` | Get full quote with depth |
| **Historical Data** | |
| `getDailyHistory()` | Get daily OHLCV |
| `getIntradayHistory()` | Get intraday OHLCV |
| **Option Chain** | |
| `getExpiryList()` | Get expiry dates |
| `getOptionChain()` | Get option chain |
| **Instruments** | |
| `getCompactCsvUrl()` | Get compact CSV URL |
| `getDetailedCsvUrl()` | Get detailed CSV URL |
| `getInstruments()` | Download segment instruments |
| **EDIS** | |
| `generateTpin()` | Generate T-PIN |
| `generateEdisForm()` | Generate EDIS form |
| `inquireEdisStatus()` | Check EDIS status |
| **Traders Control** | |
| `setKillSwitch()` | Activate/deactivate kill switch |
| **Statement** | |
| `getLedger()` | Get ledger entries |
| `getTradeHistory()` | Get trade history |
| **WebSocket** | |
| `createMarketFeedClient()` | Create market data WebSocket |
| `createOrderStreamClient()` | Create order update WebSocket |

---

## Configuration

### SDK Configuration

```kotlin
// Configure during initialization using builder pattern
val dhan = Dhan.builder()
    .clientId("your-client-id")       // Required
    .accessToken("your-access-token") // Optional at build, can set later
    .loggingEnabled(true)             // Enable HTTP request/response logging
    .rateLimitRetries(3)              // Configure rate limit retry (0-5 attempts)
    .build()
```

| Setting | Builder Method | Default | Range | Description |
|---------|----------------|---------|-------|-------------|
| Client ID | `clientId(String)` | - | - | Your Dhan client ID (required) |
| Access Token | `accessToken(String)` | `""` | - | OAuth access token (can set later) |
| HTTP Logging | `loggingEnabled(Boolean)` | `false` | - | Log HTTP requests/responses for debugging |
| Rate Limit Retry | `rateLimitRetries(Int)` | `0` | 0-5 | Auto-retry on HTTP 429 with exponential backoff |

> **Note:** When `rateLimitRetries > 0`, the SDK automatically retries rate-limited requests (HTTP 429) with exponential backoff (1s, 2s, 4s, ...) before throwing an exception.

### WebSocket Configuration

WebSocket reconnection settings are configured per-client during creation:

```kotlin
// Market Data Feed Client
val feedClient = dhan.createMarketFeedClient(
    maxReconnectAttempts = 10,      // Default: 5, Max reconnection attempts
    autoReconnectEnabled = true,    // Default: true, Auto-reconnect on disconnect
    autoResubscribeEnabled = true   // Default: true, Auto-resubscribe after reconnect
)

// Order Update Client
val orderClient = dhan.createOrderStreamClient(
    maxReconnectAttempts = 10,   // Default: 5
    autoReconnectEnabled = true  // Default: true
)
```

### Timeouts

| Setting | Default |
|---------|---------|
| Connect timeout | 10 seconds |
| Read timeout | 30 seconds |
| Write timeout | 30 seconds |

### WebSocket Settings

| Setting | Default |
|---------|---------|
| Ping interval | 10 seconds |
| Initial reconnect delay | 1 second |
| Max reconnect delay | 30 seconds |
| Max reconnect attempts | 5 (configurable 1-20) |
| Max instruments per connection | 5,000 |
| Max instruments per subscription | 100 |
| Max connections per user | 5 |

### Base URLs

| Endpoint | URL |
|----------|-----|
| REST API v2 | `https://api.dhan.co/v2` |
| Auth | `https://auth.dhan.co` |
| Instruments | `https://images.dhan.co/api-data` |
| Market Feed WebSocket | `wss://api-feed.dhan.co` |
| Order Update WebSocket | `wss://api-order-update.dhan.co` |

## Table of Contents

- [API Reference](#api-reference)
- [Configuration](#configuration)
- [WebSocket Streaming](#websocket-streaming)
  - [Market Data Feed](#market-data-feed)
  - [Order Updates](#order-updates)
  - [Token Refresh with WebSocket](#token-refresh-with-websocket)
- [REST API Reference](#rest-api-reference)
  - [Authentication](#authentication)
  - [Orders](#orders)
  - [Super Orders](#super-orders)
  - [Forever Orders (GTT)](#forever-orders-gtt)
  - [Portfolio](#portfolio)
  - [Funds & Margins](#funds--margins)
  - [Market Quotes](#market-quotes)
  - [Historical Data](#historical-data)
  - [Option Chain](#option-chain)
  - [Instruments](#instruments)
  - [EDIS](#edis)
  - [Traders Control](#traders-control)
  - [Statement](#statement)
- [Error Handling](#error-handling)
- [Resource Management](#resource-management)
- [Requirements](#requirements)
- [License](#license)

---

## WebSocket Streaming

### Market Data Feed

Real-time market data via WebSocket with binary protocol encoding (low latency). Prices are formatted as String with 2 decimal places (e.g., `"1428.50"`).

```kotlin
import io.github.sonicalgo.dhan.websocket.marketFeed.*

// Create client with custom reconnection settings (optional)
val feedClient = dhan.createMarketFeedClient(
    maxReconnectAttempts = 10,      // Default: 5
    autoReconnectEnabled = true,    // Default: true
    autoResubscribeEnabled = true   // Default: true, auto-resubscribe after reconnect
)

// Add listener
feedClient.addListener(object : MarketFeedListener {
    override fun onConnected() {
        println("Connected to market feed!")
        // Subscribe with TICKER mode
        feedClient.subscribe(
            listOf(
                Instrument(ExchangeSegment.NSE_EQ, "1333"),   // HDFC Bank
                Instrument(ExchangeSegment.NSE_EQ, "11536"),  // TCS
                Instrument(ExchangeSegment.IDX_I, "26000")    // Nifty 50
            ),
            FeedMode.TICKER
        )
    }

    override fun onReconnected() {
        println("Reconnected! Subscriptions restored.")
    }

    override fun onDisconnected(code: Int, reason: String) {
        println("Disconnected: $reason")
    }

    override fun onError(error: Throwable) {
        println("Error: ${error.message}")
    }

    override fun onTickerData(data: TickerData) {
        // data.ltp is String (e.g., "1428.50")
        println("${data.securityId}: LTP=${data.ltp}")
    }

    override fun onQuoteData(data: QuoteData) {
        println("${data.securityId}: LTP=${data.ltp}, Volume=${data.volume}")
        println("OHLC: O=${data.openPrice} H=${data.highPrice} L=${data.lowPrice} C=${data.closePrice}")
    }

    override fun onFullData(data: FullData) {
        println("${data.securityId}: LTP=${data.ltp}, OI=${data.openInterest}")
        data.bids.forEachIndexed { i, bid ->
            println("  Bid $i: ${bid.quantity} @ ${bid.price}")
        }
    }

    override fun onIndexData(data: IndexData) {
        println("Index ${data.securityId}: ${data.indexValue}")
    }

    override fun onReconnecting(attempt: Int, delayMs: Long) {
        println("Reconnecting (attempt $attempt) in ${delayMs}ms...")
    }
})

// Connect to WebSocket
feedClient.connect()
```

#### Feed Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| `FeedMode.TICKER` | LTP, LTQ, Volume, OHLC | Minimal bandwidth, price tracking |
| `FeedMode.QUOTE` | Ticker + best 5 bid/ask | Standard trading |
| `FeedMode.FULL` | Quote + Open Interest | F&O trading with OI data |

#### Subscription Management

```kotlin
// Subscribe to instruments
feedClient.subscribe(listOf(Instrument(ExchangeSegment.NSE_EQ, "1333")), FeedMode.TICKER)

// Change mode for specific instruments
feedClient.subscribe(listOf(Instrument(ExchangeSegment.NSE_EQ, "1333")), FeedMode.QUOTE)

// Subscribe to full mode with market depth
feedClient.subscribe(listOf(Instrument(ExchangeSegment.NSE_FNO, "43225")), FeedMode.FULL)

// Unsubscribe
feedClient.unsubscribe(listOf(Instrument(ExchangeSegment.NSE_EQ, "11536")))

// Get current subscriptions
val subscriptions = feedClient.getSubscriptions()  // Map<Instrument, FeedMode>
val count = feedClient.subscriptionCount

// Unsubscribe all
feedClient.unsubscribeAll()

// Close connection
feedClient.close()
```

#### Instrument Creation

```kotlin
Instrument(ExchangeSegment.NSE_EQ, "1333")       // NSE stocks
Instrument(ExchangeSegment.NSE_FNO, "43225")     // NSE F&O
Instrument(ExchangeSegment.IDX_I, "26000")       // NIFTY 50
Instrument(ExchangeSegment.MCX_COMM, "224035")   // MCX instruments
Instrument(ExchangeSegment.BSE_EQ, "532540")     // BSE stocks
Instrument(ExchangeSegment.BSE_FNO, "...")       // BSE F&O
Instrument(ExchangeSegment.NSE_CURRENCY, "...")  // NSE Currency
Instrument(ExchangeSegment.BSE_CURRENCY, "...")  // BSE Currency
```

### Order Updates

Real-time order and trade updates via WebSocket.

```kotlin
import io.github.sonicalgo.dhan.websocket.order.*

// Create client with custom reconnection settings (optional)
val orderClient = dhan.createOrderStreamClient(
    maxReconnectAttempts = 10,   // Default: 5
    autoReconnectEnabled = true  // Default: true
)

// Add listener
orderClient.addListener(object : OrderStreamListener {
    override fun onConnected() {
        println("Connected to order updates!")
    }

    override fun onReconnected() {
        println("Reconnected to order updates")
    }

    override fun onDisconnected(code: Int, reason: String) {
        println("Disconnected: $reason")
    }

    override fun onError(error: Throwable) {
        println("Error: ${error.message}")
    }

    override fun onOrderUpdate(update: OrderUpdate) {
        println("Order ${update.orderId}: ${update.orderStatus}")
        when (update.orderStatus) {
            OrderStatus.TRADED -> println("Order fully executed!")
            OrderStatus.REJECTED -> println("Rejected: ${update.omsErrorDescription}")
            OrderStatus.PART_TRADED -> println("Partial fill: ${update.filledQty}/${update.quantity}")
            else -> {}
        }
    }

    override fun onTradeUpdate(update: TradeUpdate) {
        println("Trade: ${update.tradedQuantity} @ ${update.tradedPrice}")
    }

    override fun onReconnecting(attempt: Int, delayMs: Long) {
        println("Reconnecting (attempt $attempt) in ${delayMs}ms...")
    }
})

// Connect
orderClient.connect()

// Close when done
orderClient.close()
```

### Token Refresh with WebSocket

REST API calls automatically use the latest access token. However, WebSocket clients authenticate once at connection time. If you update the token while a WebSocket is connected, reconnect to use the new token:

```kotlin
// Update token
dhan.setAccessToken("new-access-token")

// REST API calls immediately use new token
dhan.getOrders()  // Uses new token

// WebSocket needs reconnection to use new token
feedClient.close()
feedClient.connect()  // Now authenticates with new token
```

---

## REST API Reference

### Authentication

#### Consent-Based Authentication Flow

For individual traders using the API Key method, the SDK provides a consent-based authentication flow:

<details open>
<summary>Kotlin</summary>

```kotlin
// Step 1: Create SDK instance with just client ID
val dhan = Dhan.builder()
    .clientId("1000000001")
    .build()

// Step 2: Generate consent (returns consentAppId)
val consent = dhan.generateConsent(
    appId = "your-app-id",
    appSecret = "your-app-secret"
)
println("Consent App ID: ${consent.consentAppId}")

// Step 3: Redirect user to browser for login
// URL: https://login.dhan.co?consent_id=${consent.consentAppId}
// After login, user is redirected to your callback URL with tokenId

// Step 4: Exchange token for access credentials
val credentials = dhan.consumeConsent(
    tokenId = "token-from-callback",
    appId = "your-app-id",
    appSecret = "your-app-secret"
)
println("Access Token: ${credentials.accessToken}")
println("Client Name: ${credentials.dhanClientName}")
println("Expires: ${credentials.expiryTime}")

// Step 5: Set access token for trading APIs
dhan.setAccessToken(credentials.accessToken)

// Now you can use trading APIs
val profile = dhan.getProfile()
```

</details>

<details>
<summary>Java</summary>

```java
// Step 1: Create SDK instance with just client ID
Dhan dhan = Dhan.builder()
    .clientId("1000000001")
    .build();

// Step 2: Generate consent (returns consentAppId)
GenerateConsentResult consent = dhan.generateConsent("your-app-id", "your-app-secret");
System.out.println("Consent App ID: " + consent.getConsentAppId());

// Step 3: Redirect user to browser for login
// URL: https://login.dhan.co?consent_id=<consentAppId>
// After login, user is redirected to your callback URL with tokenId

// Step 4: Exchange token for access credentials
ConsumeConsentResult credentials = dhan.consumeConsent(
    "token-from-callback",
    "your-app-id",
    "your-app-secret"
);
System.out.println("Access Token: " + credentials.getAccessToken());
System.out.println("Client Name: " + credentials.getDhanClientName());

// Step 5: Set access token for trading APIs
dhan.setAccessToken(credentials.getAccessToken());

// Now you can use trading APIs
var profile = dhan.getProfile();
```

</details>

> **Note:** Users can generate up to 25 consent app IDs daily.

#### Profile and IP Configuration

```kotlin
// Get user profile
val profile = dhan.getProfile()
// Returns: dhanClientId, tokenValidity, activeSegments, dataPlan

// Set static IP (required for order APIs)
dhan.setIp(SetIpParams {
    ip = "203.0.113.50"
    ipFlag = IpFlag.PRIMARY
})

// Modify IP (allowed once every 7 days)
dhan.modifyIp(SetIpParams {
    ip = "203.0.113.51"
    ipFlag = IpFlag.SECONDARY
})

// Get IP configuration
val ipConfig = dhan.getIpConfiguration()
println("Primary IP: ${ipConfig.primaryIp}")
println("Secondary IP: ${ipConfig.secondaryIp}")

// Renew token (extends validity for 24 hours)
dhan.renewToken()
```

### Orders

> **Note:** Order placement, modification, and cancellation APIs require static IP whitelisting. Configure your IP at [web.dhan.co](https://web.dhan.co).

#### Place Order

<details open>
<summary>Kotlin</summary>

```kotlin
val response = dhan.placeOrder(PlaceOrderParams {
    transactionType = TransactionType.BUY
    exchangeSegment = ExchangeSegment.NSE_EQ
    productType = ProductType.CNC        // CNC, INTRADAY, MARGIN, MTF, CO, BO
    orderType = OrderType.LIMIT          // LIMIT, MARKET, STOP_LOSS, STOP_LOSS_MARKET
    validity = Validity.DAY              // DAY or IOC
    securityId = "1333"
    quantity = 10
    price = 1428.0
    disclosedQuantity = 0                // Optional
    triggerPrice = 0.0                   // For SL orders
    afterMarketOrder = false             // AMO flag
    amoTime = AmoTime.OPEN               // PRE_OPEN, OPEN, OPEN_30, OPEN_60
    correlationId = "my-order-1"         // Optional tracking ID
})
println("Order ID: ${response.orderId}")
println("Status: ${response.orderStatus}")
```

</details>

<details>
<summary>Java</summary>

```java
var response = dhan.placeOrder(PlaceOrderParamsBuilder.builder()
    .transactionType(TransactionType.BUY)
    .exchangeSegment(ExchangeSegment.NSE_EQ)
    .productType(ProductType.CNC)
    .orderType(OrderType.LIMIT)
    .validity(Validity.DAY)
    .securityId("1333")
    .quantity(10)
    .price(1428.0)
    .disclosedQuantity(0)
    .triggerPrice(0.0)
    .afterMarketOrder(false)
    .amoTime(AmoTime.OPEN)
    .correlationId("my-order-1")
    .build());
System.out.println("Order ID: " + response.getOrderId());
System.out.println("Status: " + response.getOrderStatus());
```

</details>

#### Slicing Order (Large Orders)

```kotlin
// Auto-splits large orders per exchange freeze limits
val response = dhan.placeSlicingOrder(SlicingOrderParams {
    transactionType = TransactionType.BUY
    exchangeSegment = ExchangeSegment.NSE_FNO
    productType = ProductType.INTRADAY
    orderType = OrderType.LIMIT
    validity = Validity.DAY
    securityId = "43225"
    quantity = 5000  // Will be sliced into smaller orders
    price = 21000.0
})
```

#### Modify Order

<details open>
<summary>Kotlin</summary>

```kotlin
val modified = dhan.modifyOrder(
    orderId = "240108010918222",
    params = ModifyOrderParams {
        orderType = OrderType.LIMIT
        legName = LegName.ENTRY_LEG
        quantity = 15
        price = 1430.0
        disclosedQuantity = 0
        triggerPrice = 0.0
        validity = Validity.DAY
    }
)
```

</details>

<details>
<summary>Java</summary>

```java
var modified = dhan.modifyOrder(
    "240108010918222",
    ModifyOrderParamsBuilder.builder()
        .orderType(OrderType.LIMIT)
        .legName(LegName.ENTRY_LEG)
        .quantity(15)
        .price(1430.0)
        .disclosedQuantity(0)
        .triggerPrice(0.0)
        .validity(Validity.DAY)
        .build()
);
```

</details>

#### Cancel Order

```kotlin
val cancelled = dhan.cancelOrder("240108010445130")
```

#### Query Orders

```kotlin
// Get all orders for the day
val orderBook = dhan.getOrders()

// Get specific order details
val order = dhan.getOrderById("240108010445130")

// Get order by correlation ID
val orderByCorr = dhan.getOrderByCorrelationId("my-order-1")

// Get all trades for the day
val trades = dhan.getTrades()

// Get trades for specific order
val orderTrades = dhan.getTradesByOrderId("240108010445100")
```

### Super Orders

Multi-leg orders with entry, target, and stop-loss.

<details open>
<summary>Kotlin</summary>

```kotlin
// Place super order
val response = dhan.placeSuperOrder(PlaceSuperOrderParams {
    transactionType = TransactionType.BUY
    exchangeSegment = ExchangeSegment.NSE_EQ
    productType = ProductType.INTRADAY
    orderType = OrderType.LIMIT
    securityId = "1333"
    quantity = 10
    price = 1428.0
    targetPrice = 1450.0
    stopLossPrice = 1410.0
    trailingJump = 5.0  // Trailing stop-loss
})
println("Super Order ID: ${response.orderId}")

// Modify specific leg
dhan.modifySuperOrder(
    orderId = "order-id",
    para
... [TRUNCATED README]


==================================================


## [2/3] Repository: dhan-nifty-algo-trading-lab (`WHEEL_dhan-nifty-algo-trading-lab`)
- **Full Name**: `dhan-nifty-algo-trading-lab`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Dhan NIFTY Algo Trading Lab

**An algorithmic trading research platform for Indian markets (Dhan / NSE)**

![Python](https://img.shields.io/badge/python-3.13-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Mode](https://img.shields.io/badge/mode-paper%20trading-brightgreen)

Back-test, validate, and **paper-trade** equity-intraday and NIFTY-options strategies —
with a full Indian cost model, out-of-sample validation, and a live control dashboard.

> **Find out whether a strategy actually works — before you risk a rupee.**
> A backtest that ignores brokerage, STT and slippage will tell you almost anything you
> want to hear. This platform is built to give you the real answer: every trade is
> booked at a realistic fill price net of the full Indian charge stack, and every
> promising result is re-tested on data it has never seen.
>
> It is deliberately strategy-agnostic. Bring your own idea, run it through the same
> pipeline, and get a verdict you can trust — the included strategies come with their
> complete, unedited test results as a worked example of the method.

**🟢 v1 is paper trading only.** It ships no live-order broker, so real orders are
impossible in this release — not merely switched off. Live trading is planned for v2
(see [ROADMAP.md](ROADMAP.md)).

> ### ⚠️ Read this before using any of it
>
> I am **not a SEBI-registered Investment Adviser or Research Analyst**, and not a
> certified or professional trader. This is a **personal project shared out of personal
> interest** — not a product, not a service, not a recommendation, and not a
> solicitation to buy or sell anything. **Nothing here is investment advice.**
>
> **Much of this codebase was written with AI assistance, and AI makes mistakes.**
> Some are subtle and survive a passing test suite. Read the code, run the tests, and
> satisfy yourself before relying on any part of it.
>
> Markets are volatile and **cannot be predicted**. A backtest is evidence about the
> past, never a promise about the future. Anyone who chooses to use, modify or extend
> this does so **entirely at their own risk**, and **I accept no responsibility or
> liability whatsoever** for any loss, damage or cost arising from it.
>
> Full statement below: [Before you use this](#before-you-use-this--please-read) · [LICENSE](LICENSE)

---

## Try it in 60 seconds — fully offline

No broker account, no API keys, no market-data files.

```bash
pip install -r requirements.txt
python run_paper.py --demo
```

Then in a second terminal, open the dashboard:

```bash
streamlit run dashboard.py
```

→ **http://localhost:8501** — watch simulated trades open and close, and use the live
pause / kill / flatten controls.

## What it does

- **Equity intraday** — opening-range breakout, momentum, and VWAP mean-reversion across a liquid F&O universe.
- **NIFTY options** — directional ATM buying and defined-risk credit spreads (bull-put / bear-call).
- **Research → paper in one code path** — back-test, then out-of-sample validation, then paper-trade the same strategy object.
- **Streamlit dashboard** — pause / kill / flatten controls, per-class P&L, net-of-cost projections, permanent history.
- **SQLite journal** — every fill, every charge, each day's P&L; trade history survives a daily reset.

## The engineering that makes the results trustworthy

*Results are only as good as the machine that produced them. This is what backs them:*

- **Real fills, real costs.** A fill is the *actual* executed price with slippage, never the intended price, and every trade is booked net of the full Indian charge stack — brokerage, STT, exchange, SEBI, stamp duty, GST.
- **Risk sizing from the stop.** `qty = fixed-rupee risk ÷ stop distance`, rounded down to whole lots and capped by a max-notional rule. If one lot is too big, the trade is *skipped* — never forced to a single unit.
- **An un-bypassable veto pipeline.** Every order funnels through one choke-point whose checks run in order: kill switch → daily-loss halt → position caps (re-read live, enforced per-position).
- **Stops are mandatory.** A signal without a stop raises at construction; there is no way to open an unprotected position.
- **A kill switch that flattens and survives a restart.** It comes back *frozen* — it never wakes up trading by accident.
- **No-lookahead backtester + out-of-sample validator.** Strategy selection is validated on unseen data; in-sample winners are treated as luck until they persist.

## The method, demonstrated

Rather than ship a polished backtest, this repo publishes its **complete test results**
so you can judge the pipeline for yourself. Each classic intraday strategy was run on
real market data, net of costs, and validated out-of-sample:

| Strategy | Test | Result vs the gate |
|---|---|---|
| Equity — ORB breakout | 210 F&O stocks, out-of-sample split | did not clear (Spearman +0.05; field PF 0.07) |
| Equity — momentum | full universe | did not clear (PF 0.65) |
| Equity — VWAP mean-reversion | 210 stocks, OOS | did not clear (field PF ~0.00) |
| NIFTY — bull-put spread (sell) | 6 months real option data | did not clear (PF 0.60) |
| NIFTY — directional option buying | 85 days real option data | did not clear (best PF 0.51) |

The gate is deliberately strict: profit factor **> 1.2 after costs**, a meaningful
number of trades, and persistence on unseen data. None of these textbook intraday
setups cleared it — a result worth knowing *before* funding them, and consistent with
the structural cost hurdle in Indian intraday trading.

**The most useful lesson is in the near-miss.** A full-sample scan surfaced 21
"winning" ORB names, the best at PF 2.75. Out-of-sample, they collapsed to luck. Any
pipeline without that second step would have shipped them as a strategy — which is
exactly the failure mode this project is built to catch.

Where results did look more promising: **lower-frequency** approaches (monthly
cross-sectional momentum, index SIP), where costs stop dominating once holding periods
stretch to days or months. That is the direction the [roadmap](ROADMAP.md) points.

Full write-up with methodology: **[FINDINGS.md](FINDINGS.md)**.

## Verify the safety machine

```bash
python demo_spine.py         # plain-English walk-through of the risk/execution spine
python tests/test_spine.py   # automated safety checks (sizing, vetoes, kill switch)
```

## Optional: paper-trade on real live prices

The demo above is fully synthetic. To run the paper engine against **real live market
data**, add Dhan Data API credentials (see `.env.example`) and run:

```bash
python run_paper.py --strategy orb --reset
```

Trades are still fake — v1 has no live-order broker. Credentials are read-only market
data here, are gitignored, and are never logged.

## Architecture

```
config.yaml            all knobs: capital, risk, session, universe, options
run_paper.py           paper engine (equity + options; --demo runs fully offline)
dashboard.py           Streamlit control panel
run_report.py          week / month / all-time P&L report (+ Excel export)
demo_spine.py          offline walk-through of the safety machine
verify_dhan.py         read-only market-data connection check

gk/
  models.py            typed objects (Signal, OrderRequest, Fill, Position, ...)
  config.py            loads config.yaml + .env into a typed Settings
  constants.py         DhanHQ v2.2.0 enums (captured from the SDK)
  instruments.py       symbol -> security_id / lot / tick
  costs.py             full Indian cost model
  clock.py             IST market-hours helpers
  journal.py           SQLite: fills, audit log, kill switch, day P&L, history
  risk.py              position sizing + un-bypassable veto pipeline
  execution.py         OrderManager — the single order choke-point
  runtime.py           broker factory (paper only in v1)
  control.py           dashboard <-> engine control bridge + heartbeat
  reports.py           P&L projections + performance reporting
  marketdata.py        live LTP / candles / option chain (Dhan Data API)
  backtest.py          no-lookahead backtester
  strategies/          orb.py, momentum.py, vwap.py, nifty_breakout.py
  brokers/
    base.py            Broker interface
    paper.py           PaperBroker — fake money, realistic mechanics
tests/test_spine.py    automated safety-spine checks
```

### Research scripts

`run_equity_backtest.py` · `run_fo_scan.py` · `run_oos_validation.py` ·
`run_strategy_oos.py` · `run_spread_backtest.py` · `run_option_buy.py` ·
`run_options_study.py` · `run_pcr_test.py`

These reproduce the findings above. They need historical data, which is not
redistributed here — fetch your own via the Dhan API.

## Tech stack

Python 3.13 · dhanhq 2.2.0 · pandas / numpy · Streamlit · SQLite (WAL) · PyYAML · python-dotenv

## What is deliberately *not* in this repo

- `.env` / API tokens — bring your own (`.env.example` shows the shape)
- `state/` databases — trade history stays local
- `data/` historical CSVs — licensed market data; fetch it yourself

## Before you use this — please read

This project is shared for **education and research**. It is a personal project,
published out of personal interest — a testing platform, not a money-making product,
not a service, and nothing in it is financial advice or a solicitation to trade.

**Who I am, and am not.** I am not a SEBI-registered Investment Adviser or Research
Analyst, not a certified or professional trader, and not qualified to tell anyone what
to do with their money. Nothing here should be read as a recommendation to buy, sell or
hold any security.

**This code was written with substantial AI assistance, and AI makes mistakes.**
That is not a formality. AI-written code can be confidently wrong in ways that read
perfectly and pass their own tests — a wrong assumption, an off-by-one, a check that
looks rigorous and measures nothing. Several such bugs were found and fixed during
development, and the honest expectation is that more remain. If you use this, audit it
yourself; do not treat a green test suite as proof of correctness.

**Markets cannot be predicted.** Volatility, gaps, liquidity droughts, regulatory
changes and plain bad luck are all outside anyone's control. No strategy here — or
anywhere — can promise a result.

**What you can rely on**
- The engine, cost model, backtester and validator are the deliverable, and they are
  built to be correct. Run `python tests/test_spine.py` to check the safety machine yourself.
- v1 is **paper trading only** — it ships no live-order broker, so it cannot place a
  real order. Nothing you do here can move real money.
- Every number in the results above is reproducible with the included research scripts.

**What you should not assume**
- The bundled strategies are **examples of the method, not recommendations**. They were
  tested and did not clear the profitability gate after costs. Please do not fund them
  because they appear in a repository.
- A passing backtest is evidence, not a guarantee. Markets change, and past results
  never promise future returns.
- Cost, lot-size and expiry rules are current as of 2026 and change over time — verify
  them against your broker before drawing conclusions.
- If you extend this toward live trading, that is your own risk to own. Test on paper
  first, start at the smallest possible size, and never trade money you cannot afford
  to lose.

**Not investment advice. No responsibility accepted.** I am not a licensed financial
adviser, nor SEBI-registered in any capacity. Trading equities and options carries
substantial risk, including the loss of your entire capital, and losses can exceed
expectations in fast or illiquid markets.

Anyone who downloads, runs, modifies or extends this software does so **entirely at
their own risk and on their own judgement**. I accept **no responsibility and no
liability whatsoever** — direct, indirect, incidental or consequential — for any
trading loss, financial loss, data loss, missed opportunity, or any other damage or
cost arising from its use, misuse, correctness or incorrectness. If you are not
prepared to own that risk completely, do not use this.

If you want advice about your money, speak to a SEBI-registered adviser. Not to me,
and not to a repository.

## License

MIT — see [LICENSE](LICENSE).

### Core Implementation Code & Architecture
#### File: `gk/brokers/__init__.py`
```python
from .base import Broker
from .paper import PaperBroker

__all__ = ["Broker", "PaperBroker"]
```

#### File: `gk/strategies/__init__.py`
```python
from .base import Strategy
from .orb import OpeningRangeBreakout
from .momentum import MomentumMover
from .vwap import VWAPReversion
from .nifty_breakout import NiftyIntradayBreakout

__all__ = ["Strategy", "OpeningRangeBreakout", "MomentumMover", "VWAPReversion",
           "NiftyIntradayBreakout"]
```

#### File: `gk/__init__.py`
```python
"""Dhan NIFTY Algo Trading Lab — safety-first research platform (PAPER ONLY).

Package layout:
    constants.py    real DhanHQ v2.2.0 enums (captured from the installed SDK)
    models.py       typed data objects (Signal, OrderRequest, Fill, Position, ...)
    config.py       loads config.yaml + .env
    instruments.py  symbol -> security_id / lot size / tick size registry
    costs.py        Indian cost model (brokerage, STT, GST, slippage, ...)
    clock.py        IST market-hours helper
    journal.py      SQLite journal + persisted state (kill switch, day P&L)
    risk.py         position sizing + risk veto pipeline + kill switch
    execution.py    OrderManager — the single choke-point for placing orders
    brokers/        base.Broker, paper.PaperBroker  (no live broker in v1)
"""

__version__ = "1.0.0"
```

#### File: `gk/strategies/base.py`
```python
"""Strategy contract. The SAME object is used by the backtester and the live
engine — so what we validate is exactly what trades.

A strategy turns a candle frame into three added columns, computed causally:
  signal  : +1 (go long), -1 (go short), 0 (nothing) — decided at bar close
  stop    : protective stop price for a signal bar (else NaN)
  target  : profit target price for a signal bar (else NaN)

The engine enters on the NEXT bar's open, so a signal at bar i never uses i+1.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class Strategy(ABC):
    name: str = "base"

    @abstractmethod
    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        """Return df with 'signal', 'stop', 'target' columns added."""

    def _blank(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        out["signal"] = 0
        out["stop"] = float("nan")
        out["target"] = float("nan")
        return out
```

#### File: `gk/clock.py`
```python
"""IST market-hours helper. All trading-time decisions go through here."""
from __future__ import annotations

from datetime import datetime, time
from typing import Optional

import pytz

IST = pytz.timezone("Asia/Kolkata")


def _to_time(hhmm: str) -> time:
    h, m = hhmm.split(":")
    return time(int(h), int(m))


def now_ist() -> datetime:
    return datetime.now(IST)


def is_weekday(dt: Optional[datetime] = None) -> bool:
    dt = dt or now_ist()
    return dt.weekday() < 5   # Mon-Fri (holiday calendar added at go-live)


def is_market_open(open_="09:15", close="15:30", dt: Optional[datetime] = None) -> bool:
    dt = dt or now_ist()
    if not is_weekday(dt):
        return False
    return _to_time(open_) <= dt.time() <= _to_time(close)


def past(hhmm: str, dt: Optional[datetime] = None) -> bool:
    """True if the current IST time is at/after hhmm."""
    dt = dt or now_ist()
    return dt.time() >= _to_time(hhmm)


def before(hhmm: str, dt: Optional[datetime] = None) -> bool:
    dt = dt or now_ist()
    return dt.time() < _to_time(hhmm)
```

#### File: `gk/constants.py`
```python
"""DhanHQ v2.2.0 constants — captured directly from the installed SDK.

These are the EXACT string values the dhanhq==2.2.0 API expects. The #1 failure
mode in the repos we reviewed was code written against a hallucinated/older SDK
(e.g. `dhanhq(client_id, token)` monolithic init, `get_market_quote`, `NSE`).
The v2.2.0 SDK is modular (DhanContext + Funds/Order/SuperOrder/... classes) and
uses the segment strings below. Verified via `inspect` on 2026-07-22.
"""

# ---- Exchange segments ----
NSE_EQ = "NSE_EQ"
NSE_FNO = "NSE_FNO"
BSE_EQ = "BSE_EQ"
BSE_FNO = "BSE_FNO"
IDX_I = "IDX_I"          # index (spot), e.g. NIFTY index value
MCX_COMM = "MCX_COMM"

# ---- Transaction types ----
BUY = "BUY"
SELL = "SELL"

# ---- Order types ----
MARKET = "MARKET"
LIMIT = "LIMIT"
STOP_LOSS = "STOP_LOSS"            # SL (limit)
STOP_LOSS_MARKET = "STOP_LOSS_MARKET"  # SL-M

# ---- Product types ----
INTRADAY = "INTRADAY"   # MIS
CNC = "CNC"             # delivery
MARGIN = "MARGIN"       # carry-forward F&O
MTF = "MTF"
CO = "CO"
BO = "BO"

# ---- Validity ----
DAY = "DAY"
IOC = "IOC"

# ---- Super Order leg names (for modify/cancel of a leg) ----
LEG_ENTRY = "ENTRY_LEG"
LEG_TARGET = "TARGET_LEG"
LEG_STOP = "STOP_LOSS_LEG"

# ---- Scrip master CSVs ----
COMPACT_CSV_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"
DETAILED_CSV_URL = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"
```


==================================================


## [3/3] Repository: dhan-nifty-lab (`WHEEL_dhan-nifty-lab`)
- **Full Name**: `dhan-nifty-lab`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Dhan NIFTY Algo Trading Lab

**An algorithmic trading research platform for Indian markets (Dhan / NSE)**

![Python](https://img.shields.io/badge/python-3.13-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Version](https://img.shields.io/badge/version-1.0.0-blue) ![Mode](https://img.shields.io/badge/mode-paper%20trading-brightgreen)

Back-test, validate, and **paper-trade** equity-intraday and NIFTY-options strategies —
with a full Indian cost model, out-of-sample validation, and a live control dashboard.

> **Find out whether a strategy actually works — before you risk a rupee.**
> A backtest that ignores brokerage, STT and slippage will tell you almost anything you
> want to hear. This platform is built to give you the real answer: every trade is
> booked at a realistic fill price net of the full Indian charge stack, and every
> promising result is re-tested on data it has never seen.
>
> It is deliberately strategy-agnostic. Bring your own idea, run it through the same
> pipeline, and get a verdict you can trust — the included strategies come with their
> complete, unedited test results as a worked example of the method.

**🟢 v1 is paper trading only.** It ships no live-order broker, so real orders are
impossible in this release — not merely switched off. Live trading is planned for v2
(see [ROADMAP.md](ROADMAP.md)).

> ### ⚠️ Read this before using any of it
>
> I am **not a SEBI-registered Investment Adviser or Research Analyst**, and not a
> certified or professional trader. This is a **personal project shared out of personal
> interest** — not a product, not a service, not a recommendation, and not a
> solicitation to buy or sell anything. **Nothing here is investment advice.**
>
> **Much of this codebase was written with AI assistance, and AI makes mistakes.**
> Some are subtle and survive a passing test suite. Read the code, run the tests, and
> satisfy yourself before relying on any part of it.
>
> Markets are volatile and **cannot be predicted**. A backtest is evidence about the
> past, never a promise about the future. Anyone who chooses to use, modify or extend
> this does so **entirely at their own risk**, and **I accept no responsibility or
> liability whatsoever** for any loss, damage or cost arising from it.
>
> Full statement below: [Before you use this](#before-you-use-this--please-read) · [LICENSE](LICENSE)

---

## Try it in 60 seconds — fully offline

No broker account, no API keys, no market-data files.

```bash
pip install -r requirements.txt
python run_paper.py --demo
```

Then in a second terminal, open the dashboard:

```bash
streamlit run dashboard.py
```

→ **http://localhost:8501** — watch simulated trades open and close, and use the live
pause / kill / flatten controls.

## What it does

- **Equity intraday** — opening-range breakout, momentum, and VWAP mean-reversion across a liquid F&O universe.
- **NIFTY options** — directional ATM buying and defined-risk credit spreads (bull-put / bear-call).
- **Research → paper in one code path** — back-test, then out-of-sample validation, then paper-trade the same strategy object.
- **Streamlit dashboard** — pause / kill / flatten controls, per-class P&L, net-of-cost projections, permanent history.
- **SQLite journal** — every fill, every charge, each day's P&L; trade history survives a daily reset.

## The engineering that makes the results trustworthy

*Results are only as good as the machine that produced them. This is what backs them:*

- **Real fills, real costs.** A fill is the *actual* executed price with slippage, never the intended price, and every trade is booked net of the full Indian charge stack — brokerage, STT, exchange, SEBI, stamp duty, GST.
- **Risk sizing from the stop.** `qty = fixed-rupee risk ÷ stop distance`, rounded down to whole lots and capped by a max-notional rule. If one lot is too big, the trade is *skipped* — never forced to a single unit.
- **An un-bypassable veto pipeline.** Every order funnels through one choke-point whose checks run in order: kill switch → daily-loss halt → position caps (re-read live, enforced per-position).
- **Stops are mandatory.** A signal without a stop raises at construction; there is no way to open an unprotected position.
- **A kill switch that flattens and survives a restart.** It comes back *frozen* — it never wakes up trading by accident.
- **No-lookahead backtester + out-of-sample validator.** Strategy selection is validated on unseen data; in-sample winners are treated as luck until they persist.

## The method, demonstrated

Rather than ship a polished backtest, this repo publishes its **complete test results**
so you can judge the pipeline for yourself. Each classic intraday strategy was run on
real market data, net of costs, and validated out-of-sample:

| Strategy | Test | Result vs the gate |
|---|---|---|
| Equity — ORB breakout | 210 F&O stocks, out-of-sample split | did not clear (Spearman +0.05; field PF 0.07) |
| Equity — momentum | full universe | did not clear (PF 0.65) |
| Equity — VWAP mean-reversion | 210 stocks, OOS | did not clear (field PF ~0.00) |
| NIFTY — bull-put spread (sell) | 6 months real option data | did not clear (PF 0.60) |
| NIFTY — directional option buying | 85 days real option data | did not clear (best PF 0.51) |

The gate is deliberately strict: profit factor **> 1.2 after costs**, a meaningful
number of trades, and persistence on unseen data. None of these textbook intraday
setups cleared it — a result worth knowing *before* funding them, and consistent with
the structural cost hurdle in Indian intraday trading.

**The most useful lesson is in the near-miss.** A full-sample scan surfaced 21
"winning" ORB names, the best at PF 2.75. Out-of-sample, they collapsed to luck. Any
pipeline without that second step would have shipped them as a strategy — which is
exactly the failure mode this project is built to catch.

Where results did look more promising: **lower-frequency** approaches (monthly
cross-sectional momentum, index SIP), where costs stop dominating once holding periods
stretch to days or months. That is the direction the [roadmap](ROADMAP.md) points.

Full write-up with methodology: **[FINDINGS.md](FINDINGS.md)**.

## Verify the safety machine

```bash
python demo_spine.py         # plain-English walk-through of the risk/execution spine
python tests/test_spine.py   # automated safety checks (sizing, vetoes, kill switch)
```

## Optional: paper-trade on real live prices

The demo above is fully synthetic. To run the paper engine against **real live market
data**, add Dhan Data API credentials (see `.env.example`) and run:

```bash
python run_paper.py --strategy orb --reset
```

Trades are still fake — v1 has no live-order broker. Credentials are read-only market
data here, are gitignored, and are never logged.

## Architecture

```
config.yaml            all knobs: capital, risk, session, universe, options
run_paper.py           paper engine (equity + options; --demo runs fully offline)
dashboard.py           Streamlit control panel
run_report.py          week / month / all-time P&L report (+ Excel export)
demo_spine.py          offline walk-through of the safety machine
verify_dhan.py         read-only market-data connection check

gk/
  models.py            typed objects (Signal, OrderRequest, Fill, Position, ...)
  config.py            loads config.yaml + .env into a typed Settings
  constants.py         DhanHQ v2.2.0 enums (captured from the SDK)
  instruments.py       symbol -> security_id / lot / tick
  costs.py             full Indian cost model
  clock.py             IST market-hours helpers
  journal.py           SQLite: fills, audit log, kill switch, day P&L, history
  risk.py              position sizing + un-bypassable veto pipeline
  execution.py         OrderManager — the single order choke-point
  runtime.py           broker factory (paper only in v1)
  control.py           dashboard <-> engine control bridge + heartbeat
  reports.py           P&L projections + performance reporting
  marketdata.py        live LTP / candles / option chain (Dhan Data API)
  backtest.py          no-lookahead backtester
  strategies/          orb.py, momentum.py, vwap.py, nifty_breakout.py
  brokers/
    base.py            Broker interface
    paper.py           PaperBroker — fake money, realistic mechanics
tests/test_spine.py    automated safety-spine checks
```

### Research scripts

`run_equity_backtest.py` · `run_fo_scan.py` · `run_oos_validation.py` ·
`run_strategy_oos.py` · `run_spread_backtest.py` · `run_option_buy.py` ·
`run_options_study.py` · `run_pcr_test.py`

These reproduce the findings above. They need historical data, which is not
redistributed here — fetch your own via the Dhan API.

## Tech stack

Python 3.13 · dhanhq 2.2.0 · pandas / numpy · Streamlit · SQLite (WAL) · PyYAML · python-dotenv

## What is deliberately *not* in this repo

- `.env` / API tokens — bring your own (`.env.example` shows the shape)
- `state/` databases — trade history stays local
- `data/` historical CSVs — licensed market data; fetch it yourself

## Before you use this — please read

This project is shared for **education and research**. It is a personal project,
published out of personal interest — a testing platform, not a money-making product,
not a service, and nothing in it is financial advice or a solicitation to trade.

**Who I am, and am not.** I am not a SEBI-registered Investment Adviser or Research
Analyst, not a certified or professional trader, and not qualified to tell anyone what
to do with their money. Nothing here should be read as a recommendation to buy, sell or
hold any security.

**This code was written with substantial AI assistance, and AI makes mistakes.**
That is not a formality. AI-written code can be confidently wrong in ways that read
perfectly and pass their own tests — a wrong assumption, an off-by-one, a check that
looks rigorous and measures nothing. Several such bugs were found and fixed during
development, and the honest expectation is that more remain. If you use this, audit it
yourself; do not treat a green test suite as proof of correctness.

**Markets cannot be predicted.** Volatility, gaps, liquidity droughts, regulatory
changes and plain bad luck are all outside anyone's control. No strategy here — or
anywhere — can promise a result.

**What you can rely on**
- The engine, cost model, backtester and validator are the deliverable, and they are
  built to be correct. Run `python tests/test_spine.py` to check the safety machine yourself.
- v1 is **paper trading only** — it ships no live-order broker, so it cannot place a
  real order. Nothing you do here can move real money.
- Every number in the results above is reproducible with the included research scripts.

**What you should not assume**
- The bundled strategies are **examples of the method, not recommendations**. They were
  tested and did not clear the profitability gate after costs. Please do not fund them
  because they appear in a repository.
- A passing backtest is evidence, not a guarantee. Markets change, and past results
  never promise future returns.
- Cost, lot-size and expiry rules are current as of 2026 and change over time — verify
  them against your broker before drawing conclusions.
- If you extend this toward live trading, that is your own risk to own. Test on paper
  first, start at the smallest possible size, and never trade money you cannot afford
  to lose.

**Not investment advice. No responsibility accepted.** I am not a licensed financial
adviser, nor SEBI-registered in any capacity. Trading equities and options carries
substantial risk, including the loss of your entire capital, and losses can exceed
expectations in fast or illiquid markets.

Anyone who downloads, runs, modifies or extends this software does so **entirely at
their own risk and on their own judgement**. I accept **no responsibility and no
liability whatsoever** — direct, indirect, incidental or consequential — for any
trading loss, financial loss, data loss, missed opportunity, or any other damage or
cost arising from its use, misuse, correctness or incorrectness. If you are not
prepared to own that risk completely, do not use this.

If you want advice about your money, speak to a SEBI-registered adviser. Not to me,
and not to a repository.

## License

MIT — see [LICENSE](LICENSE).

### Core Implementation Code & Architecture
#### File: `gk/brokers/__init__.py`
```python
from .base import Broker
from .paper import PaperBroker

__all__ = ["Broker", "PaperBroker"]
```

#### File: `gk/strategies/__init__.py`
```python
from .base import Strategy
from .orb import OpeningRangeBreakout
from .momentum import MomentumMover
from .vwap import VWAPReversion
from .nifty_breakout import NiftyIntradayBreakout

__all__ = ["Strategy", "OpeningRangeBreakout", "MomentumMover", "VWAPReversion",
           "NiftyIntradayBreakout"]
```

#### File: `gk/__init__.py`
```python
"""Dhan NIFTY Algo Trading Lab — safety-first research platform (PAPER ONLY).

Package layout:
    constants.py    real DhanHQ v2.2.0 enums (captured from the installed SDK)
    models.py       typed data objects (Signal, OrderRequest, Fill, Position, ...)
    config.py       loads config.yaml + .env
    instruments.py  symbol -> security_id / lot size / tick size registry
    costs.py        Indian cost model (brokerage, STT, GST, slippage, ...)
    clock.py        IST market-hours helper
    journal.py      SQLite journal + persisted state (kill switch, day P&L)
    risk.py         position sizing + risk veto pipeline + kill switch
    execution.py    OrderManager — the single choke-point for placing orders
    brokers/        base.Broker, paper.PaperBroker  (no live broker in v1)
"""

__version__ = "1.0.0"
```

#### File: `gk/strategies/base.py`
```python
"""Strategy contract. The SAME object is used by the backtester and the live
engine — so what we validate is exactly what trades.

A strategy turns a candle frame into three added columns, computed causally:
  signal  : +1 (go long), -1 (go short), 0 (nothing) — decided at bar close
  stop    : protective stop price for a signal bar (else NaN)
  target  : profit target price for a signal bar (else NaN)

The engine enters on the NEXT bar's open, so a signal at bar i never uses i+1.
"""
from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class Strategy(ABC):
    name: str = "base"

    @abstractmethod
    def generate_signals(self, df: pd.DataFrame) -> pd.DataFrame:
        """Return df with 'signal', 'stop', 'target' columns added."""

    def _blank(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        out["signal"] = 0
        out["stop"] = float("nan")
        out["target"] = float("nan")
        return out
```

#### File: `gk/clock.py`
```python
"""IST market-hours helper. All trading-time decisions go through here."""
from __future__ import annotations

from datetime import datetime, time
from typing import Optional

import pytz

IST = pytz.timezone("Asia/Kolkata")


def _to_time(hhmm: str) -> time:
    h, m = hhmm.split(":")
    return time(int(h), int(m))


def now_ist() -> datetime:
    return datetime.now(IST)


def is_weekday(dt: Optional[datetime] = None) -> bool:
    dt = dt or now_ist()
    return dt.weekday() < 5   # Mon-Fri (holiday calendar added at go-live)


def is_market_open(open_="09:15", close="15:30", dt: Optional[datetime] = None) -> bool:
    dt = dt or now_ist()
    if not is_weekday(dt):
        return False
    return _to_time(open_) <= dt.time() <= _to_time(close)


def past(hhmm: str, dt: Optional[datetime] = None) -> bool:
    """True if the current IST time is at/after hhmm."""
    dt = dt or now_ist()
    return dt.time() >= _to_time(hhmm)


def before(hhmm: str, dt: Optional[datetime] = None) -> bool:
    dt = dt or now_ist()
    return dt.time() < _to_time(hhmm)
```

#### File: `gk/constants.py`
```python
"""DhanHQ v2.2.0 constants — captured directly from the installed SDK.

These are the EXACT string values the dhanhq==2.2.0 API expects. The #1 failure
mode in the repos we reviewed was code written against a hallucinated/older SDK
(e.g. `dhanhq(client_id, token)` monolithic init, `get_market_quote`, `NSE`).
The v2.2.0 SDK is modular (DhanContext + Funds/Order/SuperOrder/... classes) and
uses the segment strings below. Verified via `inspect` on 2026-07-22.
"""

# ---- Exchange segments ----
NSE_EQ = "NSE_EQ"
NSE_FNO = "NSE_FNO"
BSE_EQ = "BSE_EQ"
BSE_FNO = "BSE_FNO"
IDX_I = "IDX_I"          # index (spot), e.g. NIFTY index value
MCX_COMM = "MCX_COMM"

# ---- Transaction types ----
BUY = "BUY"
SELL = "SELL"

# ---- Order types ----
MARKET = "MARKET"
LIMIT = "LIMIT"
STOP_LOSS = "STOP_LOSS"            # SL (limit)
STOP_LOSS_MARKET = "STOP_LOSS_MARKET"  # SL-M

# ---- Product types ----
INTRADAY = "INTRADAY"   # MIS
CNC = "CNC"             # delivery
MARGIN = "MARGIN"       # carry-forward F&O
MTF = "MTF"
CO = "CO"
BO = "BO"

# ---- Validity ----
DAY = "DAY"
IOC = "IOC"

# ---- Super Order leg names (for modify/cancel of a leg) ----
LEG_ENTRY = "ENTRY_LEG"
LEG_TARGET = "TARGET_LEG"
LEG_STOP = "STOP_LOSS_LEG"

# ---- Scrip master CSVs ----
COMPACT_CSV_URL = "https://images.dhan.co/api-data/api-scrip-master.csv"
DETAILED_CSV_URL = "https://images.dhan.co/api-data/api-scrip-master-detailed.csv"
```


==================================================
