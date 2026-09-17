# ⚡ [QUANT-SOURCE-205] Consolidated Quant & Algo Trading Repositories
**Category**: `HFT_MICROSTRUCTURE_LOB` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_205_HFT_MICROSTRUCTURE_LOB.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: nodejs-order-book (`PHASE4-QUANT-041`)
- **Full Name**: `PHASE4-QUANT-041_fasenderos__nodejs-order-book`
- **Description**: Ultra-fast Limit Order Book for Node.js written in TypeScript for high-frequency trading (HFT) :rocket::rocket:
- **GitHub Stars**: 207
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
<p align="center">
    <a href="https://www.npmjs.com/package/nodejs-order-book" target="_blank"><img src="https://img.shields.io/npm/v/nodejs-order-book?color=blue" alt="NPM Version"></a>
    <a href="https://github.com/fasenderos/nodejs-order-book/blob/main/LICENSE" target="_blank"><img src="https://img.shields.io/npm/l/nodejs-order-book" alt="Package License"></a>
    <a href="https://www.npmjs.com/package/nodejs-order-book" target="_blank"><img src="https://img.shields.io/npm/dm/nodejs-order-book" alt="NPM Downloads"></a>
    <a href="https://circleci.com/gh/fasenderos/nodejs-order-book" target="_blank"><img src="https://img.shields.io/circleci/build/github/fasenderos/nodejs-order-book/main" alt="CircleCI" ></a>
    <a href="https://codecov.io/github/fasenderos/nodejs-order-book" target="_blank"><img src="https://img.shields.io/codecov/c/github/fasenderos/nodejs-order-book" alt="Codecov"></a>
    <a href="https://github.com/fasenderos/nodejs-order-book"><img src="https://badgen.net/badge/icon/typescript?icon=typescript&label" alt="Built with TypeScript"></a>
</p>

# Node.js Order Book

<p align="center">
A fast, feature-complete limit order book engine for Node.js, written in TypeScript. </br>
Designed for trading systems, exchanges, and HFT simulations. </br></br>
:star: Star me on GitHub — it motivates me a lot!
</p>

**Why this library?** Originally ported from a [Go orderbook](https://github.com/i25959341/orderbook), this engine has been extended with conditional orders, Self-Trade Prevention (STP), snapshot/journaling for crash recovery, and full TypeScript support — while maintaining high throughput.

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Conditional Orders](#conditional-orders)
- [Primary Functions](#primary-functions)
  - [createOrder()](#createorder)
  - [limit()](#limit)
  - [market()](#market)
  - [stopLimit()](#stoplimit)
  - [stopMarket()](#stopmarket)
  - [oco()](#oco)
  - [modify()](#modify)
  - [cancel()](#cancel)
- [Understanding Order Results](#understanding-order-results)
- [Self-Trade Prevention (STP)](#self-trade-prevention-stp)
- [Order Book Options](#order-book-options)
  - [Snapshot](#snapshot)
  - [Journal Logs](#journal-logs)
  - [Enable Journaling](#enable-journaling)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)
- [Donation](#donation)

## Features

- Standard price-time priority matching
- Market, limit, and post-only limit orders
- Conditional orders: Stop Limit, Stop Market, and OCO (One-Cancels-the-Other)
- Time-in-force: GTC (Good-Til-Cancelled), FOK (Fill-Or-Kill), IOC (Immediate-Or-Cancel)
- Self-Trade Prevention (STP) with 4 modes (NONE, EXPIRE_MAKER, EXPIRE_TAKER, EXPIRE_BOTH)
- Order cancellation
- Order price and/or size modification
- Snapshot and journaling for order book state persistence and recovery
- **High throughput** — benchmarked at 300k+ trades per second
- Full TypeScript support with dual ESM/CJS exports

## Quick Start

```ts
import { OrderBook, Side } from 'nodejs-order-book'

const ob = new OrderBook()

// Place a sell limit order
ob.limit({ side: Side.SELL, id: 'order-1', size: 55, price: 100 })

// Place a buy market order
const result = ob.market({ side: Side.BUY, size: 10 })

console.log(result.done)     // Filled orders
console.log(result.partial)  // Partial fill, if any
```

## Requirements

- **Node.js** 18+ (ES2022 target)
- **npm**, **yarn**, or **pnpm**

## Installation

Install with npm:

```
npm install nodejs-order-book
```

Install with yarn:

```
yarn add nodejs-order-book
```

Install with pnpm:

```
pnpm add nodejs-order-book
```

## Usage

The package supports both **ESM** and **CommonJS**:

```ts
// ESM (recommended)
import { OrderBook, Side, OrderType, SelfTradePreventionMode } from 'nodejs-order-book'

// CommonJS
const { OrderBook, Side, OrderType, SelfTradePreventionMode } = require('nodejs-order-book')
```

To start using the order book you need to import `OrderBook` and create a new instance:

```ts
import { OrderBook } from 'nodejs-order-book'

const ob = new OrderBook()
```

Then you'll be able to use the following primary functions:

```ts
ob.createOrder({
      type: 'limit' | 'market',
      side: 'buy' | 'sell',
      size: number,
      price?: number,
      id?: string,
      postOnly?: boolean,
      timeInForce?: 'GTC' | 'FOK' | 'IOC'
})

ob.limit({
      id: string,
      side: 'buy' | 'sell',
      size: number,
      price: number,
      postOnly?: boolean,
      timeInForce?: 'GTC' | 'FOK' | 'IOC'
})

ob.market({ side: 'buy' | 'sell', size: number })

ob.modify(orderID: string, {
      side: 'buy' | 'sell',
      size: number,
      price: number
})

ob.cancel(orderID: string)
```

### Conditional Orders

`Stop Market`, `Stop Limit` and `OCO` orders are supported.

```ts
import { OrderBook } from 'nodejs-order-book'

const ob = new OrderBook()

ob.createOrder({
      type: 'stop_limit' | 'stop_market' | 'oco',
      side: 'buy' | 'sell',
      size: number,
      price?: number,
      id?: string,
      stopPrice?: number,
      timeInForce?: 'GTC' | 'FOK' | 'IOC',
      stopLimitTimeInForce?: 'GTC' | 'FOK' | 'IOC'
})

ob.stopLimit({
      id: string,
      side: 'buy' | 'sell',
      size: number,
      price: number,
      stopPrice: number,
      timeInForce?: 'GTC' | 'FOK' | 'IOC'
})

ob.stopMarket({
      side: 'buy' | 'sell',
      size: number,
      stopPrice: number
})

ob.oco({
      id: string,
      side: 'buy' | 'sell',
      size: number,
      price: number,
      stopPrice: number,
      stopLimitPrice: number,
      timeInForce?: 'GTC' | 'FOK' | 'IOC',
      stopLimitTimeInForce?: 'GTC' | 'FOK' | 'IOC'
})
```

## Primary Functions

To add an order to the order book you can call the general `createOrder()` function or use the underlying `limit()`, `market()`, `stopLimit()`, `stopMarket()` or `oco()` directly.

### createOrder()

A unified entry point that accepts a `type` field to dispatch to the correct handler:

```ts
// Limit order
ob.createOrder({
      type: 'limit',
      side: 'buy' | 'sell',
      size: number,
      price: number,
      id: string,
      postOnly?: boolean,
      timeInForce?: 'GTC' | 'FOK' | 'IOC'
})

// Market order
ob.createOrder({
      type: 'market',
      side: 'buy' | 'sell',
      size: number
})

// Stop limit order
ob.createOrder({
      type: 'stop_limit',
      side: 'buy' | 'sell',
      size: number,
      price: number,
      id: string,
      stopPrice: number,
      timeInForce?: 'GTC' | 'FOK' | 'IOC'
})

// Stop market order
ob.createOrder({
      type: 'stop_market',
      side: 'buy' | 'sell',
      size: number,
      stopPrice: number
})

// OCO order
ob.createOrder({
      type: 'oco',
      side: 'buy' | 'sell',
      size: number,
      stopPrice: number,
      stopLimitPrice: number,
      timeInForce?: 'GTC' | 'FOK' | 'IOC',
      stopLimitTimeInForce?: 'GTC' | 'FOK' | 'IOC'
})
```

### limit()

Create a limit order.

```ts
/**
 * @param options.side - `sell` or `buy`
 * @param options.id - Unique order ID
 * @param options.size - How much of currency you want to trade in units of base currency
 * @param options.price - The price at which the order is to be fulfilled, in units of the quote currency
 * @param options.postOnly - When `true` the order is rejected if it immediately matches as a taker. Default is `false`
 * @param options.timeInForce - GTC, FOK, or IOC. Default is GTC
 * @returns An object with the result of the processed order or an error.
 */
ob.limit({
      side: 'buy' | 'sell',
      id: string,
      size: number,
      price: number,
      postOnly?: boolean,
      timeInForce?: 'GTC' | 'FOK' | 'IOC'
})
```

For example:

```ts
ob.limit({ side: "sell", id: "uniqueID", size: 55, price: 100 })

asks: 110 -> 5      110 -> 5
      100 -> 1      100 -> 56
--------------  ->  --------------
bids: 90  -> 5      90  -> 5
      80  -> 1      80  -> 1

done    - null
partial - null
```

```ts
ob.limit({ side: "buy", id: "uniqueID", size: 7, price: 120 })

asks: 110 -> 5
      100 -> 1
--------------  ->  --------------
bids: 90  -> 5      120 -> 1
      80  -> 1      90  -> 5
                    80  -> 1

done    - 2 (or more orders)
partial - uniqueID order
```

```ts
ob.limit({ side: "buy", id: "uniqueID", size: 3, price: 120 })

asks: 110 -> 5
      100 -> 1      110 -> 3
--------------  ->  --------------
bids: 90  -> 5      90  -> 5
      80  -> 1      80  -> 1

done    - 1 order with 100 price, (may be also few orders with 110 price) + uniqueID order
partial - 1 order with price 110
```

### market()

Create a market order.

```ts
/**
 * @param options.side - `sell` or `buy`
 * @param options.size - How much of currency you want to trade in units of base currency
 * @returns An object with the result of the processed order or an error.
 */
ob.market({ side: 'buy' | 'sell', size: number })
```

For example:

```ts
ob.market({ side: 'sell', size: 6 })

asks: 110 -> 5      110 -> 5
      100 -> 1      100 -> 1
--------------  ->  --------------
bids: 90  -> 5      80 -> 1
      80  -> 2

done         - 2 (or more orders)
partial      - 1 order with price 80
quantityLeft - 0
```

```ts
ob.market({ side: 'buy', size: 10 })

asks: 110 -> 5
      100 -> 1
--------------  ->  --------------
bids: 90  -> 5      90  -> 5
      80  -> 1      80  -> 1

done         - 2 (or more orders)
partial      - null
quantityLeft - 4
```

### stopLimit()

Create a stop limit order.

```ts
/**
 * @param options.side - `sell` or `buy`
 * @param options.id - Unique order ID
 * @param options.size - How much of currency you want to trade in units of base currency
 * @param options.price - The price at which the order is to be fulfilled, in units of the quote currency
 * @param options.stopPrice - The price at which the order is triggered
 * @param options.timeInForce - GTC, FOK, or IOC. Default is GTC
 * @returns An object with the result of the processed order or an error.
 */
ob.stopLimit({
      side: 'buy' | 'sell',
      id: string,
      size: number,
      price: number,
      stopPrice: number,
      timeInForce?: 'GTC' | 'FOK' | 'IOC'
})
```

### stopMarket()

Create a stop market order.

```ts
/**
 * @param options.side - `sell` or `buy`
 * @param options.size - How much of currency you want to trade in units of base currency
 * @param options.stopPrice - The price at which the order is triggered
 * @returns An object with the result of the processed order or an error.
 */
ob.stopMarket({
      side: 'buy' | 'sell',
      size: number,
      stopPrice: number
})
```

### oco()

Create an OCO (One-Cancels-the-Other) order. An OCO combines a `stop_limit` and a `limit` order: when one is triggered or filled, the other is automatically canceled. Both orders share the same `side` and `size`. If you cancel one, the entire OCO pair is canceled.

For BUY orders: `stopPrice` must be above the current price, `price` below.
For SELL orders: `stopPrice` must be below the current price, `price` above.

```ts
/**
 * @param options.side - `sell` or `buy`
 * @param options.id - Unique order ID
 * @param options.size - How much of currency you want to trade in units of base currency
 * @param options.price - The limit order price, in units of the quote currency
 * @param options.stopPrice - The stop trigger price
 * @param options.stopLimitPrice - The stop_limit order price, in units of the quote currency
 * @param options.timeInForce - Time-in-force of the limit order. GTC, FOK, IOC. Default is GTC
 * @param options.stopLimitTimeInForce - Time-in-force of the stop_limit order. GTC, FOK, IOC. Default is GTC
 * @returns An object with the result of the processed order or an error.
 */
ob.oco({
      side: 'buy' | 'sell',
      id: string,
      size: number,
      price: number,
      stopPrice: number,
      stopLimitPrice: number,
      timeInForce?: 'GTC' | 'FOK' | 'IOC',
      stopLimitTimeInForce?: 'GTC' | 'FOK' | 'IOC'
})
```

### modify()

Modify an existing order by ID. When an order is modified (price or quantity), it is treated as a new entry: under price-time-priority, it moves to the back of the matching queue.

```ts
/**
 * @param orderID - The ID of the order to modify
 * @param orderUpdate - An object with `{size, price}`. Only provided fields are updated
 * @returns An object with the result or an error
 */
ob.modify(orderID: string, { size: number, price: number })
```

For example:

```ts
ob.limit({ side: "sell", id: "uniqueID", size: 55, price: 100 })

asks: 110 -> 5      110 -> 5
      100 -> 1      100 -> 56
--------------  ->  --------------
bids: 90  -> 5      90  -> 5
      80  -> 1      80  -> 1

// Modify the size from 55 to 65
ob.modify("uniqueID", { size: 65 })

asks: 110 -> 5      110 -> 5
      100 -> 56     100 -> 66
--------------  ->  --------------
bids: 90  -> 5      90  -> 5
      80  -> 1      80  -> 1


// Modify the price from 100 to 110
ob.modify("uniqueID", { price: 110 })

asks: 110 -> 5      110 -> 70
      100 -> 66     100 -> 1
--------------  ->  --------------
bids: 90  -> 5      90  -> 5
      80  -> 1      80  -> 1
```

### cancel()

Remove an existing order by ID from the order book.

```ts
/**
 * @param orderID - The ID of the order to remove
 * @returns The removed order if found, or `undefined`
 */
ob.cancel(orderID: string)
```

For example:

```ts
ob.cancel("myUniqueID-Sell-1-with-100")

asks: 110 -> 5
      100 -> 1      110 -> 5
--------------  ->  --------------
bids: 90  -> 5      90  -> 5
      80  -> 1      80  -> 1
```

## Understanding Order Results

When creating an order, the library returns an `IProcessOrder` object:

```ts
interface IProcessOrder {
  done: IOrder[];                    // Fully consumed orders
  activated: IStopOrder[];           // Triggered stop orders (stop limit, stop market, OCO)
  partial: ILimitOrder | null;       // Partially consumed limit order (if any)
  quantityLeft: number;              // Unfilled quantity of the taker order
  partialQuantityProcessed: number;  // Quantity consumed from the order in 'partial'
  err: OrderBookError | null;
  log?: JournalLog;                  // Journal entry (only when enableJournaling is true)
  stpExpired?: IOrder[];             // Orders expired due to Self-Trade Prevention
}
```

### When Does the Taker Appear in Results?

**The taker order does NOT always appear in the result arrays.**

| Order Type | Fill Status | Taker in `done[]` | Taker in `partial` | `quantityLeft` |
|------------|-------------|-------------------|--------------------|----------------|
| LIMIT | Fully filled | ✅ YES | ❌ NO | `0` |
| LIMIT | Partially filled | ❌ NO | ✅ YES | `> 0` |
| MARKET | Fully or partially filled | ❌ NO | ❌ NO | `>= 0` |

**Key facts:**
- **Market orders never appear in `done[]` or `partial`** - only the matched maker orders appear
- **Limit orders fully filled**: Taker appears in `done[]` alongside matched makers
- **Limit orders partially filled**: Taker appears in `partial`, matched makers appear in `done[]`
- **`quantityLeft`**: Always represents unfilled quantity of the taker, regardless of where it appears

> **Note on `activated[]`**: When a stop limit, stop market, or OCO order is triggered, the triggered order(s) appear in the `activated` array. These are orders that were resting in the stop book and have now been activated for matching.
>
> **Note on `stpExpired[]`**: When Self-Trade Prevention is configured and triggered, expired orders are listed in `stpExpired`. See [Self-Trade Prevention (STP)](#self-trade-prevention-stp) for details.

### What is `partialQuantityProcessed`?

This represents **how much of the order in `partial` was processed**, not how much is left.

- If `partial` contains the **taker** (partially filled limit order): represents amount of taker that was filled
- If `partial` contains a **maker** (partially consumed resting order): represents amount of maker that was consumed

**Example 1 - Taker in partial:**
```ts
// 10-unit buy order, only 5 available
{
  done: [{ id: 'maker-1', size: 5 }],       // Fully consumed maker
  partial: { id: 'taker', size: 5 },        // Taker (5 still unfilled)
  quantityLeft: 5,                          // 5 units of taker unfilled
  partialQuantityProcessed: 5               // 5 units of taker were filled
}
```

**Example 2 - Maker in partial:**
```ts
// 8-unit buy order, 20 available from one maker
{
  done: [{ id: 'taker', size: 8 }],         // Fully filled taker
  partial: { id: 'maker-1', size: 12 },     // Maker: 12 still unfilled (20 - 8)
  quantityLeft: 0,                          // Taker fully filled
  partialQuantityProcessed: 8               // 8 units of maker were consumed
}
```

> `partial.size` always represents the **remaining** quantity of that order, not what was consumed. In this example, the maker started with size 20, had 8 consumed, so `partial.size` is 12 (what's left on the book).

### Example: Market Order (Fully Filled)

```ts
// Market order for 10 units (10 available)
book.createOrder({ type: 'market', id: 'buy-1', size: 10, side: 'buy' })

// Result:
{
  done: [{ id: 'sell-1', side: 'sell', size: 10 }],  // Matched maker only
  partial: null,                                      // Taker NOT here
  quantityLeft: 0,                                    // Fully filled
  partialQuantityProcessed: 0
}
```

### Example: Limit Order (Fully Filled)

```ts
// Limit order for 10 units (10 available)
book.createOrder({ type: 'limit', id: 'buy-1', price: 100, size: 10, side: 'buy' })

// Result:
{
  done: [
    { id: 'sell-1', side: 'sell', size: 10 },  // Matched maker
    { id: 'buy-1', side: 'buy', size: 10 }     // Taker ✅
  ],
  partial: null,
  quantityLeft: 0,
  partialQuantityProcessed: 0
}
```

### Example: Limit Order (Partially Filled)

```ts
// Limit order for 10 units (only 5 available)
book.createOrder({ type: 'limit', id: 'buy-1', price: 100, size: 10, side: 'buy' })

// Result:
{
  done: [{ id: 'sell-1', side: 'sell', size: 5 }],  // Fully consumed maker
  partial: { id: 'buy-1', side: 'buy', size: 5 },   // Taker ✅ (5 unfilled)
  quantityLeft: 5,                                  // 5 units unfilled
  partialQuantityProcessed: 5                       // 5 units filled
}
```

## Self-Trade Prevention (STP)

> Inspired by [Binance's Self-Trade Prevention](https://developers.binance.com/docs/derivatives/usds-margined-futures/faq/stp-faq) — prevents orders from the same account from matching against each other.

### How it works

Each order can carry an `accountId` and a `stpMode`. When a taker order enters the book and would match against a maker order with the same `accountId`, the STP mode of the **taker order** determines what happens:

| Mode | Effect |
|------|--------|
| `NONE` | No prevention — orders match normally |
| `EXPIRE_MAKER` | The resting maker order(s) expire; the taker order continues |
| `EXPIRE_TAKER` | The taker order is rejected; the resting maker order(s) stay on the book |
| `EXPIRE_BOTH` | Both the taker and the matching maker order(s) expire |

The STP mode of the **taker** order always takes precedence — the mode stored on a resting maker order is ignored for STP purposes.

### API reference

Add `accountId` and `stpMode` to any order:

```ts
import { OrderBook, SelfTradePreventionMode, Side } from 'nodejs-order-book'

const ob = new OrderBook()

// Place a resting limit order from account "alice"
ob.limit({
  side: Side.BUY,
  id: 'maker-order',
  size: 5,
  price: 100,
  accountId: 'alice',
})

// Taker from the same account with STP enabled
const result = ob.limit({
  side: Side.SELL,
  id: 'taker-order',
  size: 3,
  price: 90,
  accountId: 'alice',
  stpMode: SelfTradePreventionMode.EXPIRE_MAKER,
})

// Check which orders expired due to STP
console.log(result.stpExpired) // [{ id: 'maker-order', ... }]
```

### Response fields

When STP is triggered, the response (`IProcessOrder`) includes:

| Field | Type | Description |
|-------|------|-------------|
| `stpExpired` | `IOrder[] \| undefined` | Orders removed from the book due to STP |
| `err` | `OrderBookError \| null` | Error with `code: 1202` and `message: "Self-trade prevention triggered"` for `EXPIRE_TAKER` / `EXPIRE_BOTH` |

### Error code

STP rejections return error code `1202`:

```ts
import { ErrorCodes } from 'nodejs-order-book'

assert.equal(result.err?.code, ErrorCodes.STP_TRIGGERED)
// → 1202
assert.equal(result.err?.message, 'Self-trade prevention triggered')
```

### Scenarios

#### A) EXPIRE_MAKER — maker expires, taker continues

```
Maker BUY  @ 100  qty: 5  account: "alice"
Maker BUY  @  90  qty: 5  account: "alice"
Taker SELL @  90  qty: 3  account: "alice"  mode: EXPIRE_MAKER
```

The two resting buy orders share the same account as the taker. With `EXPIRE_MAKER`, they are removed from the book and reported in `stpExpired[]`. The taker order (size 3) is placed on the book as a new maker.

```
stpExpired → [maker-buy-100, maker-buy-90]
err        → null
```

#### B) EXPIRE_TAKER — taker expires, maker stays

```
Maker BUY @ 100  qty: 5  account: "alice"
Taker SELL @ 90  qty: 3  account: "alice"  mode: EXPIRE_TAKER
```

The taker order is rejected immediately. The resting maker order remains untouched on the book.

```
stpExpired → undefined
err        → { code: 1202, message: "Self-trade prevention triggered" }
```

#### C) EXPIRE_BOTH — both orders expire

```
Maker BUY @ 100  qty: 5  account: "alice"
Taker SELL @ 90  qty: 3  account: "alice"  mode: EXPIRE_BOTH
```

The maker is removed from the book and the taker is rejected. Both sides expire.

```
stpExpired → [maker-buy-100]
err        → { code: 1202, message: "Self-trade prevention triggered" }
```

#### D) Different accounts — normal matching (no STP)

```
Maker BUY @ 100  qty: 5  account: "alice"
Taker SELL @ 90  qty: 3  account: "bob"  mode: EXPIRE_MAKER
```

The accounts differ, so STP does **not** trigger. The orders match normally.

```
done   → [filled trade summary]
stpExpired → undefined
```

#### E) Mode NONE — no prevention

```
Maker BUY @ 100  qty: 5  account: "alice"
Taker SELL @ 90  qty: 3  account: "alice"  mode: NONE
```

Even though both orders are from the same account, `NONE` mode allows the match.

```
done   → [filled trade summary]
stpExpired → undefined
```

#### F) Market order with EXPIRE_MAKER

```
Maker BUY @ 100  qty: 5  account: "alice"
Taker SELL (market)  qty: 3  account: "alice"  mode: EXPIRE_MAKER
```

The resting maker is expired via STP. The market order has no remaining liquidity, so it also expires.

```
stpExpired → [maker-buy-100]
err        → null
```

#### G) Mixed accounts at the same price level

```
Maker "alice" BUY @ 100  qty: 5
Maker "bob"   BUY @ 100  qty: 5
Taker "alice" SELL @ 90  qty: 8  mode: EXPIRE_MAKER
```

At price level 100, alice's maker is expired (`stpExpired`), while bob's maker matches normally (`done`). The remaining taker quantity (3) rests on the book.

```
stpExpired → [maker-alice-100]
done       → [maker-bob-100]
```

#### H) STP carries through triggered stop orders

Stop orders preserve the `stpMode` they were created with. When a stop order is triggered and becomes a taker, its STP mode is applied at match time.

```ts
ob.createOrder({
  type: OrderType.STOP_LIMIT,
  side: Side.BUY,
  size: 3,
  price: 110,
  stopPrice: 108,
  accountId: 'alice',
  stpMode: SelfTradePreventionMode.EXPIRE_MAKER,
})
```

### Important notes

- STP is evaluated using the **taker order's** mode, regardless of what mode the resting maker orders carry.
- If no `accountId` is specified on either side, STP is **not** triggered (backward compatible).
- If no `stpMode` is specified, it defaults to `NONE` (no prevention).
- Stop market and stop limit orders preserve the `stpMode` and apply it when triggered.
- Modify operations reset `stpMode` to `NONE`.

## Order Book Options

The order book can be initialized with the following options by passing them to the constructor:

### Snapshot

A `snapshot` represents the state of the order book at a specific point in time. It includes:

- `asks`: List of ask orders, each with a `price` and a list of associated `orders`.
- `bids`: List of bid orders, each with a `price` and a list of associated `orders`.
- `stopBook`: An object with `bids` and `asks` properties related to every `StopOrder` in the order book.
- `ts`: A Unix timestamp of when the snapshot was taken.
- `lastOp`: The ID of the last operation included in the snapshot.

Snapshots are crucial for restoring the order book to a previous state. The order book can restore from a snapshot before processing any journal logs, ensuring consistency and accuracy. After taking a snapshot, you can safely remove all logs preceding the `lastOp` id.

**Note**: The snapshot returns an object containing arrays of `bids` and `asks`. If the snapshot is saved to the database as a string, use `JSON.parse` 
... [TRUNCATED README]

### Core Implementation Code & Architecture
#### File: `test/tsconfig.json`
```python
{
	"extends": "../tsconfig.json",
	"compilerOptions": {
		"noEmit": true
	},
	"include": ["**/*"]
}
```

#### File: `.opencode/context/core/config/paths.json`
```python
{
  "description": "Additional context file paths - agents load this via @ reference for dynamic pathing",
  "paths": {
    "local": ".opencode/context",
    "global": "~/.config/opencode/context"
  }
}
```

#### File: `config/tsconfig.types.json`
```python
{
  "extends": "../tsconfig",
  "compilerOptions": {
    "declaration": true /* Generates corresponding '.d.ts' file. */,
    "emitDeclarationOnly": true,
    "rootDir": "../src",
    "outDir": "../dist/types" /* Redirect output structure to the directory. */
  }
}
```

#### File: `config/tsconfig.esm.json`
```python
{
  "extends": "../tsconfig",
  "compilerOptions": {
    "module": "ESNext" /* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', or 'ESNext'. */,
    "rootDir": "../src",
    "outDir": "../dist/esm" /* Redirect output structure to the directory. */
  }
}
```

#### File: `config/tsconfig.cjs.json`
```python
{
  "extends": "../tsconfig",
  "compilerOptions": {
    "module": "commonjs" /* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', or 'ESNext'. */,
    "moduleResolution": "node",
    "ignoreDeprecations": "6.0",
    "rootDir": "../src",
    "outDir": "../dist/cjs" /* Redirect output structure to the directory. */
  }
}
```

#### File: `biome.json`
```python
{
	"$schema": "https://biomejs.dev/schemas/2.5.1/schema.json",
	"vcs": {
		"enabled": true,
		"clientKind": "git",
		"useIgnoreFile": true
	},
	"files": {
		"includes": ["**", "!!**/dist"]
	},
	"formatter": {
		"enabled": true,
		"indentStyle": "tab"
	},
	"linter": {
		"enabled": true,
		"rules": {
			"preset": "recommended",
			"complexity": {
				"noForEach": "off"
			}
		}
	},
	"javascript": {
		"formatter": {
			"quoteStyle": "double"
		}
	},
	"assist": {
		"enabled": true,
		"actions": {
			"source": {
				"organizeImports": "on"
			}
		}
	}
}
```


==================================================


## [2/3] Repository: order-matcher (`PHASE4-QUANT-042`)
- **Full Name**: `PHASE4-QUANT-042_ArjunVachhani__order-matcher`
- **Description**: simple, fast and feature rich order matching engine supports limit, market, stop-loss, iceberg, IOC, FOK, GTD orders
- **GitHub Stars**: 173
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# order-matcher

![](https://github.com/ArjunVachhani/order-matcher/workflows/.NET%20Core/badge.svg?branch=master)

order-matcher is a simple and fast library to build crypto-currency exchange, stock exchange or commodity exchange. order-matcher matches buy and sell orders using price-time priority algorithm. order-matcher supports multiple order types and able to excecute upto 1 million messages per seconds.

 - Support multiple order types
	 - Limit 
	 - Market  
	 - Stop Loss
  	 - Stop Limit
  - Supports multiple options on order
	 - Book or Cancel
	 - Immediate or Cancel(IOC) 
	 - Fill or kill(FOK)
	 - Iceberg
	 - Good till Date(GTD) 
  	 - Self Trade Prevention 	
       
**1 Million orders per seconds on AWS c6a.xlarge instance**

**Supports integer & real numbers/decimal for price and quantity**

**Hand written serializer faster than any serializer. x15 times faster than JSON, x5 times faster than messagepack**

## Documentation
[home](https://github.com/ArjunVachhani/order-matcher/wiki)

[1. Terminology](https://github.com/ArjunVachhani/order-matcher/wiki/1.-Terminology)

[2. Order](https://github.com/ArjunVachhani/order-matcher/wiki/2.-Order)

[3. Frequently Asked Questions(FAQ)](https://github.com/ArjunVachhani/order-matcher/wiki/FAQ----Frequently-Asked-Questions)

## Project Development Status : Actively maintained. 

## Community
Questions and pull requests are welcomed. 

## Are you building spot crypto exchange?
Chat with me on telegram at [https://t.me/Arjun_Vachhani](https://t.me/Arjun_Vachhani), I may be able to help you.

## Code
```csharp

class Program
{
    static void Main(string[] args)
    {
        //timeProvider will provide epoch 
        var timeProvider = new TimeProvider();

        //create instance of matching engine.
        MatchingEngine matchingEngine = new MatchingEngine(new MyTradeListener(), new MyFeeProvider(), new Quantity(0.0000_0001m), 8);

        Order order1 = new Order { IsBuy = true, OrderId = 1, OpenQuantity = 0.01m, Price = 69_000 };
        //push new order engine.
        var addResult = matchingEngine.AddOrder(order1, timeProvider.GetSecondsFromEpoch());
        if (addResult == OrderMatchingResult.OrderAccepted)
        {
            // matching engine has accepted order
        }

        //cancel existing orders
        var cancelResult = matchingEngine.CancelOrder(1);//pass orderId to cancel
        if (cancelResult == OrderMatchingResult.CancelAcepted)
        {
            // cancel request is accepted
        }
    }
}



//create a listener to receive events from matching engine. pass it to constructore of MatchingEngine
class MyTradeListener : ITradeListener
{
    public void OnAccept(OrderId orderId, UserId userId)
    {
        Console.WriteLine($"Order Accepted.... orderId : {orderId}");
    }

    public void OnCancel(OrderId orderId, UserId userId, Quantity remainingQuantity, Amount cost, Amount fee, CancelReason cancelReason)
    {
        Console.WriteLine($"Order Cancelled.... orderId : {orderId}, remainingQuantity : {remainingQuantity}, cancelReason : {cancelReason}");
    }

    public void OnOrderTriggered(OrderId orderId, UserId userId)
    {
        Console.WriteLine($"Stop Order Triggered.... orderId : {orderId}");
    }

    public void OnTrade(OrderId incomingOrderId, OrderId restingOrderId, UserId incomingUserId, UserId restingUserId, bool incomingOrderSide, Price matchPrice, Quantity matchQuantiy, Quantity? askRemainingQuantity, Amount? askFee, Amount? bidCost, Amount? bidFee)
    {
        if (bidCost.HasValue)
        {
            // buy order completed
        }
        if (askRemainingQuantity.HasValue)
        {
            // sell order completed
        }

        Console.WriteLine($"Order matched.... incomingOrderId : {incomingOrderId}, restingOrderId : {restingOrderId}, executedQuantity : {matchQuantiy}, exetedPrice : {matchPrice}");
    }
}

class MyFeeProvider : IFeeProvider
{
    public Fee GetFee(short feeId)
    {
        return new Fee
        {
            TakerFee = 0.5m, //0.5% taker fee
            MakerFee = 0.1m, //0.1% maker fee
        };
    }
}
```


==================================================


## [3/3] Repository: lob-deep-learning (`PHASE4-QUANT-043`)
- **Full Name**: `PHASE4-QUANT-043_Jeonghwan-Cheon__lob-deep-learning`
- **Description**: Implementation of various deep learning models for limit order book. DeepLOB (Zhang et al., 2018), TransLOB (Wallbridge, 2020), DeepFolio (Sangadiev et al., 2020), etc.
- **GitHub Stars**: 159
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# LOBster 

LOBster is a project entitled <Limit order book (LOB) driven simultaneous time-series estimation in real-market-microstructure>, which is end-to-end machine learning pipeline to predict future mid-price using limit order book. Our project provides a source code of the machine learning pipeline that contains data processing, model training and inference. It contains an implementation of DeepLOB (Zhang, 2018) and our modified model.  
We also provide an implementation of handling code for FI-2010 (Ntakaris et al., 2017), a publicly available benchmark dataset for mid-price forecasting for limit order book data. In addition, we provide a pre-processing tools for custom raw LOB dataset collected in real market microstructure. The pre-processing tool contains several useful functions, such as down-sampling, normalization and labeling.  
Lastly, our project provides some modules that test the classification performance of trained model. Specially, it contains a simple market simulator that test whether inference of model works in real market microstructure. It tests the trading performance (i.e. cumulative profits) based of inference on the test set.


## Problem and challenge

### Importance of estimate the order flow
- Estimate the order flow and predict the future mid-price is important and useful for various market participants.
- For regulation authorities: For regulation authorities, they can predict the market toxic orders and price collapses. Also, based on the prediction, they can preemptively intervene the market for financial market stability. There is a well known example like market flash crash (2010), which shows toxic orders and its positive feedback causes market collapse.
- For liquidity providers (market makers): Market makers takes bid-ask spread as their profit. However, they take risks from malicious inventories caused by one-sided orders from 'information-based traders'. This kind of risk is often calls 'inventory risk', which is a major challenge for market makers. Estimate the order flow gives a change that can minimize the inventory risk for market makers.
- For other market participants: Hedge investors can further defend profit by minimize their risk based on predictions of future mid-price. Also, speculate traders can pursue profits based on predicted information.

### Difficulty
- Efficient market hypothesis: It is a hypothesis about financial market tha asset prices reflect all available information in the market (Ball and Brown 1968; Fama et al., 1969). According to this hypothesis, we can not extract any meaningful information from the price data to predict its future.
- Validation challenges of the financial models: Financial market and its data has extremely high complexity. Due to its high complexity, it is easy to be overfitted in long-term financial data (S. Jen, 2021).
- Based on these difficulties, our approach is to use limit order book data. Since it is a collection of order information, it contains more information than price data. Also, it has extremely short timeframe with millisecond unit. So, it has low risk to be overfitted.

### Limit order book (LOB)
![Limit order book](./sources/limit_order_book.png)
- LOB is a centralised and transparent system that matches customer orders on an ‘price time priority’ basis.
- LOB data is a stack of order and execution which might have information from market participants (Easley, et al., 2012)


## Dataset

### FI-2010
- FI-2010 (Ntakaris et al., 2017) is a publicly available benchmark dataset for mid-price forecasting for limit order book data
([FI-2010](https://etsin.fairdata.fi/dataset/73eb48d7-4dbc-4a10-a52a-da745b47a649)).
- It is collected for 5 stocks in NASDAQ Nordic stock market for a time period of ten consecutive days.
- It has 10 levels of LOB data that has been normalized with three different methods: Z-scoring, min-max and decimal-precision normalization.
- It also provides annotated label for 5 different time horizons: 10, 20, 30, 50, and 100 ticks.
### KRX
- FI-2010 is a useful benchmark LOB dataset, but it can not guarantee that the model works on current market which is much high-frequent.
- To ensure model works on current market microstructure, we collected LOB of two futures (KS200, KQ150) for 13 days (Nov 16 ~ Dec 2, 2022) without down-sampling.
- KRX future market has 5 levels limit order book system.
- Using ```loaders.krx_preprocess.__normalize_data__```, you can normalize the raw collected data with three different methods: Z-scoring, min-max and decimal-precision normalization.
- Using ```loaders.krx_loader.__split_x_y__```, you can generate the label with any arbitrary predict horizon. More detailed labeling method is shown in following equation.
  $$m_{-}(t)=\frac{1}{k} \sum_{i=0}^k p_{t-i}$$
  $$m_{+}(t)=\frac{1}{k} \sum_{i=0}^k p_{t+i}$$
  $$l_t=\frac{m_{+}(t)-m_{-}(t)}{m_{-}(t)}$$  
  If the $l_t > +\alpha$, the label is $+1$ (Up). Else, if the $l_t < -\alpha$, the label is $-1$ (Down). Otherwise, the label is $0$ (Stationary). The $\alpha$ indicates threshold.

## Models
![Model architecture](./sources/model_architecture.png)

### DeepLOB (Zhang, 2018)
- DeepLOB is a convolutional neural network based model for limit order book data.
- It consists of three convolution block, inception layer and LSTM.

### LOBster (Our model)
- LOBster is a lighten version of DeepLOB tuned for 5 level orderbook system (i.e. Korea exchange future market). Convolution layer for feature extraction were modified for 5 level orderbook input data.
- Since the number of input feature is reduced to half, the risk of overfitting the model has increased. Thus, we adopted a symmetric-mask dropout after the inception layer. Symmetric-mask dropout means that mask is replicated in time-axis, to keep the timeseries dependent extracted feature.
- LSTM was replaced to Gated recurrent unit (Chung et al., 2014)

### Hierarchical feature integration
![Hierarchical feature integration](./sources/hierarchical_feature_integration.png)
- DeepLOB and our modified model has three convolutional block. This architecture is a specialized form of convolutional neural network to utilize the characteristic of limit order book data.
- The first convolutional block integrates the price and volume data in each ask-side and bid-side.
- The second convolutional block integrates the ask-side and bid-side in a level.
- The third convolutional block integrates the multi levels of LOB.
- These hierarchical feature integration helps the network to extract the meaningful feature as the combination of price and volume data, such as micro-price.

## Guideline

### Setup
1. Download the FI-2010 dataset ([FI-2010](https://etsin.fairdata.fi/dataset/73eb48d7-4dbc-4a10-a52a-da745b47a649)) and unzip it on the project folder.
2. Install the NVIDIA toolkit for GPU support
   ([CUDA 11.0](https://developer.nvidia.com/cuda-toolkit-archive),
   [CUDNN 8](https://developer.nvidia.com/rdp/cudnn-download))
3. Check the CUDA is available
    ```angular2html
    nvidia-smi
    ```
4. Install the dependency libraries
    ```angular2html
    pip install requirements.txt
    ```

### Running experiments
1. Hyperparameter setting  
   Open the ```optimizers/hyperparams.yaml``` to modify the hyperparameter setting. You can set the batch size, learning rate, epsilon, maximum epoch and number of workers to load dataset. Otherwise, the experiments will conduct under our fine-tuned hyperparameters.
   ```angular2html
   [model name]:
     batch_size: 128
     learning_rate: 0.0001
     epsilon: 1e-08
     epoch: 30
     num_workers: 4
   ```
2. Experiment setting  
   Open the ```main.py``` to set the experiment parameters. Our base experiment setting already implements in the ```main.py```, so you don't have to modify it.
   ```angular2html
    # experiment parameter setting
    dataset_type = 'fi2010'
    normalization = 'Zscore'
    model_type = 'lobster'
    lighten = True
    
    T = 100
    k = 4
    stock = [0, 1, 2, 3, 4]
    train_test_ratio = 0.7
   ```
   - ```dataset_type```: Dataset for experiment. You can select 'fi2010' or 'krx'. (only 'fi2010' is available in public demo version)
   - ```normalization```: Normalization method. 'Zscore', 'MinMax', and 'DecPre' are available.
   - ```lighten```: It determines whether the experiment uses the 10-level LOB data or 5-level reduced LOB data. If lighten is True, experiment will only use the 5-level reduced data. This parameter affects not only the input dataset, but also the architecture of the model.
   - ```model_type```: Model used in experiment. 'deeplob' and 'lobster' is available.
   - ```T```: Length of time window used in single input. T = 100 used in paper and our experiment.
   - ```k```: Prediction horizion. For fi-2010, 0, 1, 2, 3, 4 is available, which indicates the 10, 20, 30, 50, 100 ticks of horizon. For krx, any prediction horizon is available.
   - ```stock```: Stock dataset used in experiment. For FI-2010, [0, 1, 2, 3, 4] are available, which indicates corresponding individual stocks. For KRX, ['KS200', 'KQ150'] are available. You can use multi-stocks for single experiments.
   - ```train_test_ratio```: Ratio to split the training set and test set. For example, if the train_test_ratio is 0.7, the early 0.7 days data are used for training set and the late 0.3 days data are used for test set.
3. Run the main.py
    ```angular2html
    python main.py
    ```
4. Check the experiment result  
   When you run the ```main.py```, it will automatically generate a unique ID for each experiment and print it. It includes some information for experiment, such as model type and experiment datetime (ex. lobster-lighten_2022-12-03_10:34:05). The trained model and all the corresponding result will save in ```loggers/results/[model id]```.
5. Evaluate the model  
   The implemented code will automatically give the visualization of training process, classification reports (confusion matrix, accuracy, precision, recall, f1-score) and market simulation result. Note that market simulation is not available on FI-2010 dataset, since it only provides the normalized price data. Or, if you want to re-generate the above evaluation, you can run the code with the corresponding model id.

## References
Our reference papers are listed in [References.md](./References.md).

### Core Implementation Code & Architecture
#### File: `models/__init__.py`
```python

```

#### File: `optimizers/__init__.py`
```python

```

#### File: `simulator/__init__.py`
```python

```

#### File: `loaders/__init__.py`
```python

```

#### File: `simulator/classification_report.py`
```python
import os
import pickle
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from loggers import logger


def report(model_id):
    with open(os.path.join(logger.find_save_path(model_id), 'prediction.pkl'), 'rb') as f:
        all_midprices, all_targets, all_predictions = pickle.load(f)

    test_acc = accuracy_score(all_targets, all_predictions)
    print(f"Test acc: {test_acc:.4f}")
    print(classification_report(all_targets, all_predictions, digits=4))
    print(confusion_matrix(all_targets, all_predictions))
```

#### File: `simulator/training_vis.py`
```python
import os
import pickle
import matplotlib.pyplot as plt

from loggers import logger


def vis_training_process(model_id):
    with open(os.path.join(logger.find_save_path(model_id), 'training_process.pkl'), 'rb') as f:
        training_info = pickle.load(f)

    plt.figure(figsize=(15,6))

    plt.subplot(1, 2, 1)
    plt.plot(training_info['train_loss_hist'], label='train loss')
    plt.plot(training_info['val_loss_hist'], label='validation loss')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.ylim([0.6, 1.2])

    plt.subplot(1, 2, 2)
    plt.plot(training_info['train_acc_hist'], label='train acc')
    plt.plot(training_info['val_acc_hist'], label='validation acc')
    plt.legend()
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.ylim([0.5, 0.9])

    path = logger.find_save_path(model_id)
    plt.savefig(os.path.join(path, 'training_process.svg'), format='svg')
```


==================================================
