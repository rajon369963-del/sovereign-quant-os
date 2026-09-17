# ⚡ [QUANT-SOURCE-037] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_037_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Motilal-Oswal-Algo-Trading-Engine (`PHASE4-QUANT-084`)
- **Full Name**: `PHASE4-QUANT-084_hemanthsai8104__Motilal-Oswal-Algo-Trading-Engine`
- **Description**: FastAPI middleware for algorithmic trading via the Motilal Oswal API across NSE, BSE, MCX, and more.
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Motilal Oswal Algo Trading Engine

A high-performance, modular Python middleware for the Motilal Oswal (MOFSL) Trading API. Built with **FastAPI**, this application acts as a bridge to execute algorithmic trades across multiple exchanges (NSE, BSE, MCX, NFO, CDS).

## 🚀 Features

- **Multi-Exchange Support:** Unified logic for NSE, BSE, NSEFO, BSEFO, MCX, and Currency (CDS).
- **Automatic Instrument Mapping:** Downloads and caches Scrip Masters automatically to map symbols (e.g., "GOLDPETAL") to internal tokens.
- **Smart Quantity Logic:** Auto-calculates lot sizes for derivatives.
- **Full API Coverage:**
  - Place, Modify, Cancel Orders.
  - Fetch Order Book, Trade Book, Positions, and Holdings.
  - Get Live LTP and Margin Summaries.
- **Security:** Implements TOTP (2FA) generation and strictly follows MOFSL header requirements (IP/MAC address binding).
- **Modular Architecture:** Clean separation of concerns (Models, Backend, Routes).

## 📂 Project Structure
motilal-oswal-algo-trading-engine/
├── main.py # Entry point (FastAPI Routes)
├── backend.py # Core logic (MOFSL API communication)
├── models.py # Pydantic data models (Request/Response schemas)
├── utils.py # Helper functions (Public IP, MAC Address)
├── config.py # Configuration constants and URLs
├── requirements.txt # Python dependencies
└── README.md # Project documentation


## 🛠️ Installation

**1. Clone the repository:**
```bash
git clone https://github.com/hemanthsai8104/Motilal-Oswal-Algo-Trading-Engine.git
cd Motilal-Oswal-Algo-Trading-Engine
```

**2. Create a virtual environment:**
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies:**
```bash
pip install -r requirements.txt
```

## ⚡ Usage

**Start the server:**
```bash
python main.py
# OR for auto-reload during development
uvicorn main:app --reload
```

**Access the API:**
The server starts at `http://127.0.0.1:8000`.

**Interactive documentation:**
Visit `http://127.0.0.1:8000/docs` to test endpoints via Swagger UI.

## 🔗 Key Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/validate_motilal` | Login & download instrument masters |
| POST | `/place_order_motilal` | Place order (auto-detects exchange logic) |
| POST | `/modify_order_motilal` | Modify an existing order |
| POST | `/cancel_order_motilal` | Cancel an order |
| POST | `/get_positions` | Get current open positions |
| POST | `/get_ltp` | Get live price for any scrip |
| POST | `/get_margin_summary` | Check available funds |

## ⚠️ Disclaimer

This software is provided for educational purposes only. Algorithmic trading involves significant financial risk. The developer of this repository is not responsible for any financial losses incurred while using this code. Always test strategies in a controlled environment before using real funds.

### Core Implementation Code & Architecture
#### File: `config.py`
```python
# config.py

BASE_URL = "https://openapi.motilaloswal.com"

# You can add other constants here if needed
USER_AGENT = 'MOSL/V.1.1.0'
SOURCE_ID = 'WEB'
```

#### File: `utils.py`
```python
# utils.py
import requests
import uuid

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=3).text.strip()
    except:
        return "127.0.0.1"

def get_mac_address():
    try:
        mac = uuid.getnode()
        return ':'.join(('%012X' % mac)[i:i+2] for i in range(0, 12, 2))
    except:
        return "00:00:00:00:00:00"
```

#### File: `models.py`
```python
# models.py
from typing import Optional
from pydantic import BaseModel

class MotilalInput(BaseModel):
    api_key: str
    secretKey: str = "" 
    redirectURL: str = "" 
    mobile: str      # userId / ClientCode
    pin: str         # The Password
    totp_key: str
    userId: str      # ClientCode
    dob: str         # Date of Birth (DD/MM/YYYY)

class OrderInput(BaseModel):
    userId: str
    symbol: str             # e.g. "RELIANCE", "GOLD", "SENSEX"
    exchange: str = "NSE"   # NSE, NSEFO, BSE, BSEFO, MCX, NSECD
    transaction_type: str   # BUY or SELL
    order_type: str         # LIMIT, MARKET, STOPLOSS
    quantity: int           # Total quantity
    price: Optional[float] = 0.0
    trigger_price: Optional[float] = 0.0
    product: str = "NORMAL" # MIS, CNC, NORMAL, DELIVERY
    validity: str = "DAY"   # DAY, IOC
    tag: Optional[str] = "OpenAlgo"
    is_amo: str = "N"       # Y or N

class ModifyOrderInput(BaseModel):
    userId: str
    unique_order_id: str
    new_order_type: str        
    new_quantity: int          
    new_price: float
    new_trigger_price: float = 0.0
    new_validity: str = "DAY"
    last_modified_time: Optional[str] = None 
    qty_traded_today: Optional[int] = 0
    exchange: str = "NSE"      

class CancelOrderInput(BaseModel):
    userId: str
    unique_order_id: str

class GenericRequest(BaseModel):
    userId: str
    exchange: Optional[str] = None
    scripcode: Optional[str] = None
    symbol: Optional[str] = None
```

#### File: `main.py`
```python
# main.py
import uvicorn
import logging
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

from models import MotilalInput, OrderInput, ModifyOrderInput, CancelOrderInput, GenericRequest
from backend import MotilalBackend

# Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("MOFSL_App")

# Global Store
MOFSL_SESSIONS = {} 

app = FastAPI(title="Motilal Oswal Integration (Modular)")

@app.post("/validate_motilal")
async def login(data: MotilalInput):
    try:
        backend = MotilalBackend(data.api_key, data.userId, data.pin, data.totp_key, data.dob)
        
        token = await backend.login()
        await backend.load_instruments()
        funds = await backend.get_funds(token)
        
        MOFSL_SESSIONS[data.userId] = {"backend": backend, "token": token}
        
        return {"status": True, "message": "Login Successful", "data": {"userId": data.userId, "token": token, "funds": funds}}
    except Exception as e:
        logger.error(str(e))
        return JSONResponse(status_code=500, content={"status": False, "message": str(e)})

@app.post("/place_order_motilal")
async def place_order(data: OrderInput):
    try:
        session = MOFSL_SESSIONS.get(data.userId)
        if not session: raise HTTPException(status_code=401, detail="Session expired")
        return await session["backend"].place_order(session["token"], data)
    except Exception as e:
        logger.error(f"Order Error: {str(e)}")
        status = 400 if hasattr(e, 'detail') else 500
        return JSONResponse(status_code=status, content={"status": False, "message": str(e) if not hasattr(e, 'detail') else e.detail})

@app.post("/modify_order_motilal")
async def modify_order(data: ModifyOrderInput):
    session = MOFSL_SESSIONS.get(data.userId)
    if not session: return {"status": False, "message": "Session expired"}
    return await session["backend"].modify_order(session["token"], data)

@app.post("/cancel_order_motilal")
async def cancel_order(data: CancelOrderInput):
    session = MOFSL_SESSIONS.get(data.userId)
    if not session: return {"status": False, "message": "Session expired"}
    return await session["backend"].cancel_order(session["token"], data)

@app.post("/get_order_book")
async def get_order_book(user_id: str):
    session = MOFSL_SESSIONS.get(user_id)
    if not session: return {"status": False, "message": "Session expired"}
    return await session["backend"].get_generic_report(session["token"], "/rest/book/v2/getorderbook")

@app.post("/get_trade_book")
async def get_trade_book(user_id: str):
    session = MOFSL_SESSIONS.get(user_id)
    if not session: return {"status": False, "message": "Session expired"}
    return await session["backend"].get_generic_report(session["token"], "/rest/book/v1/gettradebook")

@app.post("/get_positions")
async def get_positions(user_id: str):
    session = MOFSL_SESSIONS.get(user_id)
    if not session: return {"status": False, "message": "Session expired"}
    return await session["backend"].get_generic_report(session["token"], "/rest/book/v1/getposition")

@app.post("/get_holdings")
async def get_holdings(user_id: str):
    session = MOFSL_SESSIONS.get(user_id)
    if not session: return {"status": False, "message": "Session expired"}
    return await session["backend"].get_generic_report(session["token"], "/rest/report/v1/getdpholding")

@app.post("/get_margin_summary")
async def get_margin_summary(user_id: str):
    session = MOFSL_SESSIONS.get(user_id)
    if not session: return {"status": False, "message": "Session expired"}
    return await session["backend"].get_generic_report(session["token"], "/rest/report/v1/getreportmarginsummary")

@app.post("/get_ltp")
async def get_ltp(req: GenericRequest):
    session = MOFSL_SESSIONS.get(req.userId)
    if not session: return {"status": False, "message": "Session expired"}
    if not req.exchange or not req.symbol: return {"status": False, "message": "Exchange and Symbol required"}
    return await session["backend"].get_ltp(session["token"], req.exchange, req.symbol)

@app.post("/get_brokerage")
async def get_brokerage(req: GenericRequest):
    session = MOFSL_SESSIONS.get(req.userId)
    if not session: return {"status": False, "message": "Session expired"}
    if not req.exchange: return {"status": False, "message": "Exchange required"}
    return await session["backend"].get_brokerage(session["token"], req.exchange)

@app.post("/logout_motilal")
async def logout(user_id: str):
    if user_id in MOFSL_SESSIONS:
        session = MOFSL_SESSIONS.pop(user_id)
        try:
            await session["backend"].logout(session["token"])
        except: pass
        return {"status": True, "message": "Logged out"}
    return {"status": False, "message": "User not logged in"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

#### File: `backend.py`
```python
# backend.py
import hashlib
import logging
import io
import json
import requests
import pandas as pd
import pyotp
import httpx
from datetime import datetime
from fastapi import HTTPException

from config import BASE_URL, USER_AGENT, SOURCE_ID
from utils import get_public_ip, get_mac_address
from models import OrderInput, ModifyOrderInput, CancelOrderInput

# Setup Logger
logger = logging.getLogger("MOFSL_Backend")
logging.basicConfig(level=logging.INFO)

class MotilalBackend:
    def __init__(self, api_key, client_code, password, totp_key, dob):
        self.api_key = api_key
        self.client_code = client_code
        self.password = password
        self.totp_key = totp_key
        self.dob = dob
        
        self.public_ip = get_public_ip()
        self.mac_addr = get_mac_address()
        
        # Caches for Instruments
        self._equity_df = None  
        self._fno_df = None     
        self._bse_df = None     
        self._bsefo_df = None   
        self._mcx_df = None     
        self._nsecd_df = None   
        self._bsecd_df = None   

    def _get_headers(self, auth_token=None):
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': USER_AGENT,
            'ApiKey': self.api_key,
            'ClientLocalIp': '127.0.0.1',
            'ClientPublicIp': self.public_ip,
            'MacAddress': self.mac_addr,
            'SourceId': SOURCE_ID,
            'vendorinfo': self.client_code, 
            'osname': 'Windows 10',
            'osversion': '10.0.19041',
            'devicemodel': 'AHV',
            'manufacturer': 'DELL',
            'productname': 'OpenAlgo',
            'productversion': '1.0.0',
            'browsername': 'Chrome',
            'browserversion': '120.0'
        }
        if auth_token:
            headers["Authorization"] = auth_token
        return headers

    def _generate_password_hash(self):
        raw = f"{self.password}{self.api_key}"
        return hashlib.sha256(raw.encode()).hexdigest()

    def get_totp(self):
        try:
            return pyotp.TOTP(self.totp_key).now()
        except Exception:
            raise ValueError("Invalid TOTP Key")

    # --- 1. LOGIN ---
    async def login(self):
        url = f"{BASE_URL}/rest/login/v3/authdirectapi"
        payload = {
            "userid": self.client_code,
            "password": self._generate_password_hash(),
            "totp": self.get_totp(),
            "2FA": self.dob 
        }
        
        logger.info(f"Attempting login for {self.client_code}")
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=self._get_headers())
            
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "SUCCESS":
                return data.get("AuthToken")
            else:
                raise ValueError(f"Login Failed: {data.get('message')}")
        else:
            raise HTTPException(status_code=response.status_code, detail=response.text)

    # --- 2. INSTRUMENT MAPPING ---
    async def load_instruments(self):
        try:
            def fetch_csv(name):
                logger.info(f"Downloading {name} Masters...")
                r = requests.get(f"{BASE_URL}/getscripmastercsv?name={name}")
                if r.status_code == 200:
                    df = pd.read_csv(io.StringIO(r.text))
                    df.columns = [c.strip().lower() for c in df.columns]
                    return df
                return None

            if self._equity_df is None: self._equity_df = fetch_csv("NSE")
            if self._fno_df is None: self._fno_df = fetch_csv("NSEFO")
            if self._bse_df is None: self._bse_df = fetch_csv("BSE")
            if self._mcx_df is None: self._mcx_df = fetch_csv("MCX")
            if self._bsefo_df is None: self._bsefo_df = fetch_csv("BSEFO")
            if self._nsecd_df is None: self._nsecd_df = fetch_csv("NSECD")

            logger.info("All Instruments loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to download instruments: {e}")

    def get_instrument_data(self, symbol, exchange):
        symbol = symbol.strip().upper()
        exchange = exchange.upper()
        
        if str(symbol).isdigit():
            return {"scripcode": int(symbol), "lotsize": 1}

        df = None
        if exchange == "NSE": df = self._equity_df
        elif exchange in ["NSEFO", "NFO"]: df = self._fno_df
        elif exchange == "BSE": df = self._bse_df
        elif exchange == "MCX": df = self._mcx_df
        elif exchange == "BSEFO": df = self._bsefo_df
        elif exchange in ["NSECD", "CDS"]: df = self._nsecd_df
        elif exchange == "BSECD": df = self._bsecd_df

        if df is None:
            raise ValueError(f"Instruments not loaded or Invalid Exchange {exchange}")

        res = df[df['scripshortname'] == symbol]
        if res.empty:
            res = df[df['scripname'] == symbol]
        if res.empty and exchange in ["NSE", "BSE"]:
            res = df[df['scripname'].str.contains(symbol, na=False)]

        if not res.empty:
            row = res.iloc[0]
            lot = row.get('marketlot', 1)
            if pd.isna(lot): lot = 1
            return {"scripcode": int(row['scripcode']), "lotsize": int(lot)}
            
        raise ValueError(f"Symbol {symbol} not found in {exchange}")

    # --- 3. FUNDS ---
    async def get_funds(self, auth_token):
        url = f"{BASE_URL}/rest/report/v1/getreportmargindetail"
        headers = self._get_headers(auth_token)
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json={}, headers=headers)
        
        avail_cash = 0.0
        if response.status_code == 200:
            data = response.json()
            if data.get("status") == "SUCCESS":
                items = data.get("data", [])
                for item in items:
                    srno = item.get("srno")
                    amount = float(item.get("amount", 0))
                    if srno == 102:
                        avail_cash = amount
                        break
                    elif srno == 201 and avail_cash == 0:
                        avail_cash = amount
        return avail_cash

    # --- 4. PLACE ORDER ---
    def _map_product_type(self, product: str) -> str:
        p = product.upper()
        if p in ["MIS", "INTRADAY"]: return "NORMAL" 
        elif p in ["CNC", "DELIVERY"]: return "DELIVERY"
        elif p in ["NRML", "NORMAL", "CARRYFORWARD"]: return "NORMAL"
        elif p == "VALUEPLUS": return "VALUEPLUS"
        return "NORMAL"

    def _map_exchange(self, exchange: str) -> str:
        exc = exchange.upper()
        if exc == "NFO": return "NSEFO"
        if exc == "CDS": return "NSECD"
        return exc

    async def place_order(self, auth_token, data: OrderInput):
        exch = self._map_exchange(data.exchange)
        inst = self.get_instrument_data(data.symbol, exch)
        scrip_code = inst['scripcode']
        lot_size = inst['lotsize']
        
        actual_qty = data.quantity
        qty_in_lots = actual_qty
        
        if exch in ["NSEFO", "MCX", "NSECD", "BSEFO", "BSECD"]:
            if actual_qty % lot_size != 0:
                raise ValueError(f"Qty {actual_qty} must be multiple of Lot {lot_size}")
            qty_in_lots = int(actual_qty / lot_size)
        
        payload = {
            "clientcode": self.client_code,
            "exchange": exch,
            "symboltoken": scrip_code,
            "buyorsell": data.transaction_type.upper(),
            "ordertype": data.order_type.upper(),
            "producttype": self._map_product_type(data.product),
            "orderduration": data.validity.upper(),
            "price": float(data.price),
            "triggerprice": float(data.trigger_price),
            "quantityinlot": qty_in_lots,
            "disclosedquantity": 0,
            "amoorder": data.is_amo,
            "tag": data.tag
        }
        
        logger.info(f"Place Order: {payload}")
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BASE_URL}/rest/trans/v1/placeorder", json=payload, headers=self._get_headers(auth_token))
            
        res_data = response.json()
        if res_data.get("status") == "SUCCESS":
            return {"status": "success", "order_id": res_data.get("uniqueorderid"), "message": res_data.get("message")}
        else:
            msg = res_data.get("message", "Unknown Error")
            code = res_data.get("errorcode", "")
            raise HTTPException(status_code=400, detail=f"{msg} (Code: {code})")

    async def logout(self, auth_token):
        url = f"{BASE_URL}/rest/login/v1/logout"
        headers = self._get_headers(auth_token)
        payload = {"clientcode": self.client_code}
        async with httpx.AsyncClient() as client:
            await client.post(url, json=payload, headers=headers)

    # --- NEW METHODS ---
    async def modify_order(self, auth_token, data: ModifyOrderInput):
        last_mod_time = data.last_modified_time or datetime.now().strftime("%d-%b-%Y %H:%M:%S")
        payload = {
            "clientcode": self.client_code,
            "uniqueorderid": data.unique_order_id,
            "newordertype": data.new_order_type,
            "neworderduration": data.new_validity,
            "newprice": data.new_price,
            "newtriggerprice": data.new_trigger_price,
            "newquantityinlot": data.new_quantity,
            "newdisclosedquantity": 0,
            "newgoodtilldate": "",
            "lastmodifiedtime": last_mod_time,
            "qtytradedtoday": data.qty_traded_today
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BASE_URL}/rest/trans/v2/modifyorder", json=payload, headers=self._get_headers(auth_token))
        return response.json()

    async def cancel_order(self, auth_token, data: CancelOrderInput):
        payload = {"clientcode": self.client_code, "uniqueorderid": data.unique_order_id}
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BASE_URL}/rest/trans/v1/cancelorder", json=payload, headers=self._get_headers(auth_token))
        return response.json()

    async def get_generic_report(self, auth_token, endpoint):
        payload = {"clientcode": self.client_code}
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BASE_URL}{endpoint}", json=payload, headers=self._get_headers(auth_token))
        return response.json()

    async def get_ltp(self, auth_token, exchange, symbol):
        exch = self._map_exchange(exchange)
        inst = self.get_instrument_data(symbol, exch)
        payload = {"clientcode": self.client_code, "exchange": exch, "scripcode": inst['scripcode']}
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BASE_URL}/rest/report/v1/getltpdata", json=payload, headers=self._get_headers(auth_token))
        return response.json()

    async def get_brokerage(self, auth_token, exchange, series="EQ"):
        payload = {"clientcode": self.client_code, "exchangename": self._map_exchange(exchange), "series": series}
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{BASE_URL}/rest/report/v1/getbrokeragedetail", json=payload, headers=self._get_headers(auth_token))
        return response.json()
```


==================================================


## [2/3] Repository: Quantum-Trading-Bot-for-NSE-BSE (`PHASE4-QUANT-085`)
- **Full Name**: `PHASE4-QUANT-085_jitenkr2030__Quantum-Trading-Bot-for-NSE-BSE`
- **Description**: A next-generation, enterprise-grade algorithmic trading platform with quantum-enhanced machine learning, real-time market analysis, and institutional-quality performance reporting. Built for professional traders, quantitative analysts, and financial institutions.
- **GitHub Stars**: 1
- **Source Pool**: `phase4_quant_wheels_100`

### Core Implementation Code & Architecture
#### File: `count_lines.py`
```python
import os

base_path = "/workspace/quantum-trading-bot"

print("="*70)
print("PHASE 2: INTELLIGENCE - IMPLEMENTATION COMPLETE")
print("="*70)

# Core modules
modules = [
    'backend/ml_models.py',
    'backend/quantum_ml.py',
    'backend/sentiment_analysis.py',
    'backend/data_pipeline.py',
    'backend/backtesting_engine.py',
    'backend/main_phase2.py',
    'backend/test_phase2.py'
]

print("\n📦 Core Modules:")
total_code = 0
for module in modules:
    path = os.path.join(base_path, module)
    if os.path.exists(path):
        with open(path, 'r') as f:
            lines = len(f.readlines())
            total_code += lines
            print(f"  ✓ {module:40s} {lines:>5} lines")

print(f"\n  Total Code: {total_code:>5} lines")

# Documentation
docs = [
    'PHASE2_IMPLEMENTATION_GUIDE.md',
    'PHASE2_README.md',
    'PHASE2_COMPLETE.md'
]

print("\n📚 Documentation:")
total_docs = 0
for doc in docs:
    path = os.path.join(base_path, doc)
    if os.path.exists(path):
        with open(path, 'r') as f:
            lines = len(f.readlines())
            total_docs += lines
            print(f"  ✓ {doc:40s} {lines:>5} lines")

print(f"\n  Total Documentation: {total_docs:>5} lines")

print("\n" + "="*70)
print(f"GRAND TOTAL: {total_code + total_docs:>5} lines")
print("="*70)
```

#### File: `quantum-trading-bot/mobile/package.json`
```python
{
  "name": "QuantumTradingBotMobile",
  "version": "1.0.0",
  "description": "Mobile app for Quantum Trading Bot - NSE/BSE Markets",
  "main": "node_modules/expo/AppEntry.js",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web",
    "build:android": "expo build:android",
    "build:ios": "expo build:ios",
    "lint": "eslint ."
  },
  "dependencies": {
    "expo": "~49.0.15",
    "expo-status-bar": "~1.6.0",
    "react": "18.2.0",
    "react-native": "0.72.6",
    "react-native-paper": "^5.10.6",
    "react-native-vector-icons": "^10.0.0",
    "react-navigation": "^4.4.4",
    "@react-navigation/native": "^6.1.7",
    "@react-navigation/bottom-tabs": "^6.5.8",
    "@react-navigation/stack": "^6.3.17",
    "react-native-screens": "~3.22.0",
    "react-native-safe-area-context": "4.6.3",
    "react-native-gesture-handler": "~2.12.0",
    "react-native-reanimated": "~3.3.0",
    "react-native-charts-wrapper": "^0.5.11",
    "victory-native": "^36.6.11",
    "react-native-svg": "13.9.0",
    "react-native-calendars": "^1.1301.0",
    "expo-notifications": "~0.20.1",
    "expo-device": "~5.4.0",
    "expo-constants": "~14.4.2",
    "react-native-push-notification": "^8.1.1",
    "@react-native-async-storage/async-storage": "1.18.2",
    "react-native-firebase": "^18.6.2",
    "axios": "^1.5.0",
    "moment": "^2.29.4",
    "lodash": "^4.17.21"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0",
    "@types/react": "~18.2.14",
    "@types/react-native": "~0.72.2",
    "@typescript-eslint/eslint-plugin": "^6.0.0",
    "@typescript-eslint/parser": "^6.0.0",
    "eslint": "^8.0.0",
    "eslint-plugin-react": "^7.33.2",
    "eslint-plugin-react-native": "^4.1.0",
    "typescript": "^5.1.3"
  },
  "private": true
}
```

#### File: `quantum-trading-bot/backend/setup_database.py`
```python
"""
Database Setup and Migration Script
Run this script to initialize the PostgreSQL database
"""

import sys
import os
from getpass import getpass
import subprocess

# Add backend directory to path
sys.path.insert(0, os.path.dirname(__file__))

from database import init_database, SessionLocal, User
from auth import AuthService

def check_postgresql():
    """Check if PostgreSQL is installed and running"""
    print("🔍 Checking PostgreSQL...")
    try:
        result = subprocess.run(
            ["pg_isready"],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print("✅ PostgreSQL is running")
            return True
        else:
            print("❌ PostgreSQL is not running")
            return False
    except FileNotFoundError:
        print("❌ PostgreSQL is not installed")
        return False

def create_database():
    """Create database if it doesn't exist"""
    print("\n📦 Creating database...")
    
    db_name = "quantum_trading_db"
    db_user = "trading_user"
    db_password = "trading_pass"
    
    # Instructions for creating database
    print(f"""
    Please run the following commands in PostgreSQL:
    
    1. Login as postgres user:
       sudo -u postgres psql
    
    2. Create user and database:
       CREATE USER {db_user} WITH PASSWORD '{db_password}';
       CREATE DATABASE {db_name} OWNER {db_user};
       GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {db_user};
       \\q
    
    3. Set environment variable (add to ~/.bashrc or ~/.zshrc):
       export DATABASE_URL="postgresql://{db_user}:{db_password}@localhost:5432/{db_name}"
    """)
    
    input("Press Enter after you've created the database...")

def initialize_tables():
    """Initialize database tables"""
    print("\n📊 Creating database tables...")
    try:
        init_database()
        print("✅ All tables created successfully")
        return True
    except Exception as e:
        print(f"❌ Error creating tables: {e}")
        return False

def create_admin_user():
    """Create initial admin user"""
    print("\n👤 Creating admin user...")
    
    db = SessionLocal()
    
    try:
        # Check if admin exists
        existing_admin = db.query(User).filter(User.is_admin == True).first()
        
        if existing_admin:
            print(f"✅ Admin user already exists: {existing_admin.username}")
            return
        
        # Get admin details
        print("\nEnter admin user details:")
        username = input("Username: ").strip()
        email = input("Email: ").strip()
        password = getpass("Password: ")
        password_confirm = getpass("Confirm Password: ")
        
        if password != password_confirm:
            print("❌ Passwords don't match")
            return
        
        full_name = input("Full Name (optional): ").strip() or None
        
        # Create admin user
        admin = AuthService.create_user(
            db=db,
            username=username,
            email=email,
            password=password,
            full_name=full_name,
            is_admin=True
        )
        
        print(f"✅ Admin user created: {admin.username}")
        
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")
    finally:
        db.close()

def run_migration():
    """Run complete database migration"""
    print("=" * 60)
    print("🗄️  QUANTUM TRADING BOT - DATABASE SETUP")
    print("=" * 60)
    
    # Step 1: Check PostgreSQL
    if not check_postgresql():
        print("\n⚠️  Please install and start PostgreSQL first")
        print("   Ubuntu/Debian: sudo apt-get install postgresql")
        print("   macOS: brew install postgresql")
        return
    
    # Step 2: Create database
    create_db = input("\nDo you need to create the database? (y/n): ").lower()
    if create_db == 'y':
        create_database()
    
    # Step 3: Initialize tables
    if not initialize_tables():
        return
    
    # Step 4: Create admin user
    create_admin = input("\nCreate admin user? (y/n): ").lower()
    if create_admin == 'y':
        create_admin_user()
    
    print("\n" + "=" * 60)
    print("✅ DATABASE SETUP COMPLETE!")
    print("=" * 60)
    print("\n📝 Next steps:")
    print("   1. Set DATABASE_URL environment variable")
    print("   2. Start the backend: python main_phase1.py")
    print("   3. Access API docs: http://localhost:8000/docs")

if __name__ == "__main__":
    run_migration()
```

#### File: `quantum-trading-bot/backend/main.py`
```python
"""
Quantum Trading Bot for NSE/BSE - Main FastAPI Backend
Author: MiniMax Agent
"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
import json
import asyncio
from datetime import datetime

app = FastAPI(
    title="Quantum Trading Bot - NSE/BSE",
    description="AI-Powered Quantum Trading System for Indian Stock Markets",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data Models
class StockQuery(BaseModel):
    symbols: List[str]
    start_date: str
    end_date: str

class PortfolioOptimizationRequest(BaseModel):
    symbols: List[str]
    risk_factor: float = 0.5
    budget: int = 10
    capital: float = 100000.0

class StrategyRequest(BaseModel):
    strategy_type: str  # momentum, mean_reversion, breakout, quantum_optimized
    symbols: List[str]
    parameters: Dict

class BacktestRequest(BaseModel):
    strategy: str
    symbols: List[str]
    start_date: str
    end_date: str
    initial_capital: float = 100000.0

# Active WebSocket connections
active_connections: List[WebSocket] = []

@app.get("/")
async def root():
    return {"message": "Quantum Trading Bot API - NSE/BSE", "status": "active"}

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "quantum_engine": "qiskit-finance",
        "version": "1.0.0"
    }

@app.get("/api/markets/status")
async def market_status():
    """Get NSE/BSE market status"""
    now = datetime.now()
    hour = now.hour
    
    # Simple market hours check (9:15 AM to 3:30 PM IST)
    is_open = 9 <= hour < 15 or (hour == 15 and now.minute <= 30)
    
    return {
        "nse": {
            "is_open": is_open,
            "name": "National Stock Exchange",
            "trading_hours": "09:15 - 15:30 IST"
        },
        "bse": {
            "is_open": is_open,
            "name": "Bombay Stock Exchange",
            "trading_hours": "09:15 - 15:30 IST"
        },
        "current_time": now.isoformat()
    }

# WebSocket for real-time updates
@app.websocket("/ws/market-data")
async def websocket_market_data(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    
    try:
        while True:
            # Send simulated real-time data
            data = {
                "timestamp": datetime.now().isoformat(),
                "type": "market_update",
                "data": {
                    "NIFTY50": 19500 + (hash(str(datetime.now())) % 100),
                    "SENSEX": 65000 + (hash(str(datetime.now())) % 200)
                }
            }
            await websocket.send_json(data)
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        active_connections.remove(websocket)

@app.post("/api/quantum/portfolio-optimization")
async def quantum_portfolio_optimization(request: PortfolioOptimizationRequest):
    """
    Quantum-enhanced portfolio optimization using Qiskit Finance
    """
    from quantum_engine import QuantumPortfolioOptimizer
    
    optimizer = QuantumPortfolioOptimizer()
    result = await optimizer.optimize(
        symbols=request.symbols,
        risk_factor=request.risk_factor,
        budget=request.budget,
        capital=request.capital
    )
    
    return result

@app.post("/api/quantum/risk-analysis")
async def quantum_risk_analysis(symbols: List[str]):
    """
    Quantum VaR and CVaR calculation
    """
    from quantum_engine import QuantumRiskAnalyzer
    
    analyzer = QuantumRiskAnalyzer()
    result = await analyzer.analyze_risk(symbols)
    
    return result

@app.post("/api/strategies/backtest")
async def backtest_strategy(request: BacktestRequest):
    """
    Backtest trading strategies
    """
    from strategy_engine import BacktestEngine
    
    engine = BacktestEngine()
    result = await engine.run_backtest(
        strategy=request.strategy,
        symbols=request.symbols,
        start_date=request.start_date,
        end_date=request.end_date,
        initial_capital=request.initial_capital
    )
    
    return result

@app.post("/api/strategies/generate")
async def generate_quantum_strategy(request: StrategyRequest):
    """
    Generate quantum-optimized trading strategy
    """
    from strategy_engine import QuantumStrategyGenerator
    
    generator = QuantumStrategyGenerator()
    strategy = await generator.generate(
        strategy_type=request.strategy_type,
        symbols=request.symbols,
        parameters=request.parameters
    )
    
    return strategy

@app.get("/api/data/nse-stocks")
async def get_nse_stocks():
    """Get NSE stock list"""
    # Top NSE stocks
    stocks = [
        {"symbol": "RELIANCE.NS", "name": "Reliance Industries Ltd", "sector": "Energy"},
        {"symbol": "TCS.NS", "name": "Tata Consultancy Services", "sector": "IT"},
        {"symbol": "HDFCBANK.NS", "name": "HDFC Bank Ltd", "sector": "Banking"},
        {"symbol": "INFY.NS", "name": "Infosys Ltd", "sector": "IT"},
        {"symbol": "ICICIBANK.NS", "name": "ICICI Bank Ltd", "sector": "Banking"},
        {"symbol": "HINDUNILVR.NS", "name": "Hindustan Unilever", "sector": "FMCG"},
        {"symbol": "ITC.NS", "name": "ITC Ltd", "sector": "FMCG"},
        {"symbol": "SBIN.NS", "name": "State Bank of India", "sector": "Banking"},
        {"symbol": "BHARTIARTL.NS", "name": "Bharti Airtel Ltd", "sector": "Telecom"},
        {"symbol": "KOTAKBANK.NS", "name": "Kotak Mahindra Bank", "sector": "Banking"},
        {"symbol": "LT.NS", "name": "Larsen & Toubro Ltd", "sector": "Infrastructure"},
        {"symbol": "AXISBANK.NS", "name": "Axis Bank Ltd", "sector": "Banking"},
        {"symbol": "ASIANPAINT.NS", "name": "Asian Paints Ltd", "sector": "Paints"},
        {"symbol": "MARUTI.NS", "name": "Maruti Suzuki India", "sector": "Auto"},
        {"symbol": "TITAN.NS", "name": "Titan Company Ltd", "sector": "Retail"},
    ]
    
    return {"stocks": stocks, "count": len(stocks)}

@app.get("/api/data/market-indices")
async def get_market_indices():
    """Get major Indian market indices"""
    indices = [
        {"symbol": "^NSEI", "name": "NIFTY 50", "exchange": "NSE"},
        {"symbol": "^NSEBANK", "name": "NIFTY BANK", "exchange": "NSE"},
        {"symbol": "^BSESN", "name": "SENSEX", "exchange": "BSE"},
        {"symbol": "NIFTYJR", "name": "NIFTY Next 50", "exchange": "NSE"},
    ]
    
    return {"indices": indices}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

#### File: `quantum-trading-bot/deployment/monitoring/grafana/dashboard.json`
```python
# Quantum Trading Bot - Grafana Dashboard
# Phase 4: Scale - Monitoring and Observability

{
  "dashboard": {
    "id": null,
    "title": "Quantum Trading Bot - Production Dashboard",
    "tags": ["quantum-trading", "trading", "production"],
    "timezone": "UTC",
    "refresh": "30s",
    "time": {
      "from": "now-1h",
      "to": "now"
    },
    "panels": [
      {
        "id": 1,
        "title": "System Overview",
        "type": "stat",
        "targets": [
          {
            "expr": "up{job=\"quantum-trading-bot\"}",
            "refId": "A"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "thresholds": {
              "steps": [
                {
                  "color": "red",
                  "value": 0
                },
                {
                  "color": "green",
                  "value": 1
                }
              ]
            }
          }
        },
        "gridPos": {
          "h": 8,
          "w": 6,
          "x": 0,
          "y": 0
        }
      },
      {
        "id": 2,
        "title": "Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_requests_total{job=\"quantum-trading-bot\"}[5m])",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 18,
          "x": 6,
          "y": 0
        }
      },
      {
        "id": 3,
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(http_requests_total{job=\"quantum-trading-bot\",status=~\"5..\"}[5m])",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 0,
          "y": 8
        }
      },
      {
        "id": 4,
        "title": "Response Time (95th percentile)",
        "type": "graph",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket{job=\"quantum-trading-bot\"}[5m]))",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 12,
          "y": 8
        }
      },
      {
        "id": 5,
        "title": "CPU Usage by Pod",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(container_cpu_usage_seconds_total{pod=~\"quantum-trading-bot-.*\"}[5m]) * 100",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 0,
          "y": 16
        }
      },
      {
        "id": 6,
        "title": "Memory Usage by Pod",
        "type": "graph",
        "targets": [
          {
            "expr": "container_memory_usage_bytes{pod=~\"quantum-trading-bot-.*\"} / 1024 / 1024 / 1024",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 12,
          "y": 16
        }
      },
      {
        "id": 7,
        "title": "Database Connections",
        "type": "graph",
        "targets": [
          {
            "expr": "pg_stat_database_numbackends",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 0,
          "y": 24
        }
      },
      {
        "id": 8,
        "title": "Redis Memory Usage",
        "type": "graph",
        "targets": [
          {
            "expr": "redis_memory_used_bytes / 1024 / 1024",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 12,
          "y": 24
        }
      },
      {
        "id": 9,
        "title": "Trading Volume (Last 24h)",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(trading_volume_total[1h])",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 0,
          "y": 32
        }
      },
      {
        "id": 10,
        "title": "Quantum Algorithm Performance",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(quantum_algorithm_executions_total[5m])",
            "refId": "A"
          },
          {
            "expr": "rate(quantum_algorithm_errors_total[5m])",
            "refId": "B"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 12,
          "y": 32
        }
      },
      {
        "id": 11,
        "title": "Alert System Status",
        "type": "stat",
        "targets": [
          {
            "expr": "rate(alert_delivery_failures_total[5m])",
            "refId": "A"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "thresholds": {
              "steps": [
                {
                  "color": "green",
                  "value": 0
                },
                {
                  "color": "yellow",
                  "value": 0.01
                },
                {
                  "color": "red",
                  "value": 0.1
                }
              ]
            }
          }
        },
        "gridPos": {
          "h": 6,
          "w": 8,
          "x": 0,
          "y": 40
        }
      },
      {
        "id": 12,
        "title": "SEBI Compliance Status",
        "type": "stat",
        "targets": [
          {
            "expr": "sebi_compliance_violations_total",
            "refId": "A"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "color": {
              "mode": "thresholds"
            },
            "thresholds": {
              "steps": [
                {
                  "color": "green",
                  "value": 0
                },
                {
                  "color": "red",
                  "value": 1
                }
              ]
            }
          }
        },
        "gridPos": {
          "h": 6,
          "w": 8,
          "x": 8,
          "y": 40
        }
      },
      {
        "id": 13,
        "title": "Portfolio Risk Exposure",
        "type": "graph",
        "targets": [
          {
            "expr": "portfolio_risk_exposure * 100",
            "refId": "A"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "unit": "percent"
          }
        },
        "gridPos": {
          "h": 6,
          "w": 8,
          "x": 16,
          "y": 40
        }
      },
      {
        "id": 14,
        "title": "Data Feed Latency",
        "type": "graph",
        "targets": [
          {
            "expr": "data_feed_latency_seconds",
            "refId": "A"
          }
        ],
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 0,
          "y": 46
        }
      },
      {
        "id": 15,
        "title": "ML Model Accuracy",
        "type": "graph",
        "targets": [
          {
            "expr": "ml_model_accuracy * 100",
            "refId": "A"
          }
        ],
        "fieldConfig": {
          "defaults": {
            "unit": "percent"
          }
        },
        "gridPos": {
          "h": 8,
          "w": 12,
          "x": 12,
          "y": 46
        }
      }
    ]
  }
}
```

#### File: `quantum-trading-bot/examples.py`
```python
"""
Quantum Trading Bot - Example Usage Scripts
Demonstrates how to use the quantum trading engine
Author: MiniMax Agent
"""

import asyncio
import sys
sys.path.append('/workspace/quantum-trading-bot/backend')

from quantum_engine import QuantumPortfolioOptimizer, QuantumRiskAnalyzer, QuantumMonteCarloSimulator
from strategy_engine import BacktestEngine, QuantumStrategyGenerator


async def example_portfolio_optimization():
    """
    Example 1: Quantum Portfolio Optimization
    """
    print("\n" + "="*60)
    print("EXAMPLE 1: Quantum Portfolio Optimization")
    print("="*60 + "\n")
    
    # Indian stocks to optimize
    symbols = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS", "ICICIBANK.NS"]
    
    optimizer = QuantumPortfolioOptimizer()
    
    print(f"Optimizing portfolio for: {', '.join(symbols)}")
    print("Using QAOA quantum algorithm...")
    print("This may take a moment...\n")
    
    result = await optimizer.optimize(
        symbols=symbols,
        risk_factor=0.5,
        budget=3,
        capital=100000.0,
        use_quantum=True  # Use quantum QAOA
    )
    
    if result['success']:
        print(f"✓ Optimization Method: {result['optimization_method']}")
        print(f"✓ Selected Stocks: {', '.join(result['selected_stocks'])}")
        print(f"\nPortfolio Metrics:")
        print(f"  Expected Return:  {result['metrics']['expected_return']:.2f}%")
        print(f"  Volatility:       {result['metrics']['volatility']:.2f}%")
        print(f"  Sharpe Ratio:     {result['metrics']['sharpe_ratio']:.2f}")
        
        print(f"\nStock Allocations (Total: ₹{100000:,.2f}):")
        for stock, data in result['allocations'].items():
            print(f"  {stock:15s} - {data['percentage']:.1f}% (₹{data['allocation']:,.2f})")
    
    return result


async def example_risk_analysis():
    """
    Example 2: Quantum Risk Analysis
    """
    print("\n" + "="*60)
    print("EXAMPLE 2: Quantum Risk Analysis")
    print("="*60 + "\n")
    
    symbols = ["TCS.NS", "INFY.NS", "WIPRO.NS"]
    
    analyzer = QuantumRiskAnalyzer()
    
    print(f"Analyzing risk for: {', '.join(symbols)}")
    print("Computing VaR, CVaR, and Quantum Risk Score...\n")
    
    result = await analyzer.analyze_risk(symbols, confidence_level=0.95, horizon_days=10)
    
    if result['success']:
        print(f"Risk Analysis Results (95% confidence, 10-day horizon):\n")
        print(f"Portfolio Metrics:")
        print(f"  Value at Risk (VaR):     {result['portfolio']['var']:.2f}%")
        print(f"  Conditional VaR (CVaR):  {result['portfolio']['cvar']:.2f}%")
        print(f"  Quantum Risk Score:      {result['portfolio']['quantum_risk_score']:.1f}/100")
        print(f"  Volatility:              {result['portfolio']['volatility']:.2f}%")
        print(f"  Risk Level:              {result['interpretation']}")
        
        print(f"\nIndividual Stock VaR:")
        for symbol, var in result['individual_stocks']['var'].items():
            print(f"  {symbol:15s} - {var:.2f}%")
    
    return result


async def example_monte_carlo_simulation():
    """
    Example 3: Quantum Monte Carlo Price Simulation
    """
    print("\n" + "="*60)
    print("EXAMPLE 3: Quantum Monte Carlo Simulation")
    print("="*60 + "\n")
    
    symbol = "RELIANCE.NS"
    
    simulator = QuantumMonteCarloSimulator()
    
    print(f"Simulating price paths for: {symbol}")
    print("Running 1000 quantum-enhanced simulations...\n")
    
    result = await simulator.simulate_price_paths(
        symbol=symbol,
        days=30,
        num_simulations=1000
    )
    
    if result['success']:
        print(f"Simulation Results (30 days, 1000 paths):\n")
        print(f"Current Price: ₹{result['current_price']:.2f}")
        print(f"\nExpected Price (30 days):")
        print(f"  Mean:    ₹{result['expected_price']['mean']:.2f}")
        print(f"  Std Dev: ₹{result['expected_price']['std']:.2f}")
        print(f"  Min:     ₹{result['expected_price']['min']:.2f}")
        print(f"  Max:     ₹{result['expected_price']['max']:.2f}")
        
        print(f"\nConfidence Intervals (Day 30):")
        ci = result['confidence_intervals'][30]
        print(f"  5th percentile:   ₹{ci['p5']:.2f}")
        print(f"  25th percentile:  ₹{ci['p25']:.2f}")
        print(f"  50th percentile:  ₹{ci['p50']:.2f}")
        print(f"  75th percentile:  ₹{ci['p75']:.2f}")
        print(f"  95th percentile:  ₹{ci['p95']:.2f}")
    
    return result


async def example_backtesting():
    """
    Example 4: Strategy Backtesting
    """
    print("\n" + "="*60)
    print("EXAMPLE 4: Momentum Strategy Backtesting")
    print("="*60 + "\n")
    
    symbols = ["TCS.NS", "INFY.NS", "HDFCBANK.NS"]
    
    engine = BacktestEngine()
    
    print(f"Backtesting momentum strategy")
    print(f"Stocks: {', '.join(symbols)}")
    print(f"Initial Capital: ₹1,00,000")
    print("Running backtest (this may take a minute)...\n")
    
    result = await engine.run_backtest(
        strategy="momentum",
        symbols=symbols,
        start_date="2023-01-01",
        end_date="2024-11-14",
        initial_capital=100000.0
    )
    
    if result['success']:
        print(f"Backtest Results:\n")
        print(f"Strategy:        {result['strategy']}")
        print(f"Initial Capital: ₹{result['initial_capital']:,.2f}")
        print(f"Final Capital:   ₹{result['final_capital']:,.2f}")
        print(f"Total Return:    {result['total_return']:.2f}%")
        print(f"Total Trades:    {result['total_trades']}")
        print(f"Winning Trades:  {result['winning_trades']}")
        print(f"Losing Trades:   {result['losing_trades']}")
        
        if 'metrics' in result:
            print(f"\nRisk Metrics:")
            print(f"  Sharpe Ratio:   {result['metrics'].get('sharpe_ratio', 'N/A')}")
            print(f"  Max Drawdown:   {result['metrics'].get('max_drawdown', 'N/A')}%")
        
        if result.get('trades'):
            print(f"\nRecent Trades (last 5):")
            for trade in result['trades'][-5:]:
                action = trade['action']
                color = '\033[92m' if action == 'BUY' else '\033[91m'
                reset = '\033[0m'
                print(f"  {color}{action:4s}{reset} {trade['symbol']:15s} @ ₹{trade['price']:.2f} x {trade['shares']} shares")
    
    return result


async def example_strategy_generation():
    """
    Example 5: Quantum Strategy Generation
    """
    print("\n" + "="*60)
    print("EXAMPLE 5: Quantum Strategy Generation")
    print("="*60 + "\n")
    
    symbols = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "INFY.NS"]
    
    generator = QuantumStrategyGenerator()
    
    print("Generating quantum-optimized strategy...")
    print(f"Universe: {', '.join(symbols)}\n")
    
    strategy = await generator.generate(
        strategy_type="quantum_optimized",
        symbols=symbols,
        parameters={"risk_tolerance": "moderate"}
    )
    
    if strategy['success']:
        print(f"Generated Strategy:\n")
        print(f"Type:        {strategy['strategy_type']}")
        print(f"Algorithm:   {strategy['quantum_algorithm']}")
        print(f"Description: {strategy['description']}")
        
        print(f"\nQuantum Weights:")
        for idx, weight in strategy['quantum_weights'].items():
            symbol = symbols[idx] if idx < len(symbols) else f"Asset {idx}"
            print(f"  {symbol:15s} - {weight*100:.2f}%")
        
        print(f"\nRebalancing:")
        print(f"  Frequency: {strategy['rebalancing']['frequency']}")
        print(f"  Method:    {strategy['rebalancing']['method']}")
    
    return strategy


async def run_all_examples():
    """
    Run all example demonstrations
    """
    print("\n" + "="*70)
    print(" " * 10 + "QUANTUM TRADING BOT - DEMO EXAMPLES")
    print(" " * 15 + "NSE/BSE Quantum Trading System")
    print("="*70)
    
    examples = [
        example_portfolio_optimization,
        example_risk_analysis,
        example_monte_carlo_simulation,
        example_backtesting,
        example_strategy_generation
    ]
    
    for example_func in examples:
        try:
            await example_func()
            await asyncio.sleep(1)  # Pause between examples
        except Exception as e:
            print(f"\n⚠ Error in {example_func.__name__}: {str(e)}")
    
    print("\n" + "="*70)
    print(" " * 20 + "ALL EXAMPLES COMPLETED!")
    print("="*70 + "\n")


if __name__ == "__main__":
    # Run examples
    print("Initializing Quantum Trading Bot examples...")
    print("Note: First run may take longer as data is fetched from yfinance\n")
    
    asyncio.run(run_all_examples())
```


==================================================


## [3/3] Repository: hjAlgos_notebooks (`PHASE4-QUANT-087`)
- **Full Name**: `PHASE4-QUANT-087_dreamhigh0525__hjAlgos_notebooks`
- **Description**: Algorithmic trading NSE and BSE stocks using Zerodha's kite-connect API.
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
![hjAlgos_logo](https://user-images.githubusercontent.com/12392345/125793534-770505fc-e5dd-4869-a5e4-3654ff9d0785.jpg)


Algorithmic trading NSE and BSE stocks using Zerodha's kite-connect API.

Steps to give authentication to this library:
1) Open "Allow_API.ipynb"
2) Run first block
3) Click on the output of first block and open the URL
4) Click on Allow/Give Access.
5) Done..!

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=hemangjoshi37a/hjAlgos_notebooks&type=Date)](https://star-history.com/#hemangjoshi37a/hjAlgos_notebooks&Date)


## 📫 How to reach me
[<img height="36" src="https://cdn.simpleicons.org/similarweb"/>](https://hjlabs.in/) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/WhatsApp"/>](https://wa.me/917016525813) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/telegram"/>](https://t.me/hjlabs) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Gmail"/>](mailto:hemangjoshi37a@gmail.com) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/LinkedIn"/>](https://www.linkedin.com/in/hemang-joshi-046746aa) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/facebook"/>](https://www.facebook.com/hemangjoshi37) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Twitter"/>](https://twitter.com/HemangJ81509525) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/tumblr"/>](https://www.tumblr.com/blog/hemangjoshi37a-blog) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/StackOverflow"/>](https://stackoverflow.com/users/8090050/hemang-joshi) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Instagram"/>](https://www.instagram.com/hemangjoshi37) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Pinterest"/>](https://in.pinterest.com/hemangjoshi37a) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/Blogger"/>](http://hemangjoshi.blogspot.com) &nbsp;
[<img height="36" src="https://cdn.simpleicons.org/gitlab"/>](https://gitlab.com/hemangjoshi37a) &nbsp;

 
## Checkout Cool GitHub Other Repositories:
- [pyPortMan](https://github.com/hemangjoshi37a/pyPortMan)
- [transformers_stock_prediction](https://github.com/hemangjoshi37a/transformers_stock_prediction)
- [TrendMaster](https://github.com/hemangjoshi37a/TrendMaster)
- [hjAlgos_notebooks](https://github.com/hemangjoshi37a/hjAlgos_notebooks)
- [AutoCut](https://github.com/hemangjoshi37a/AutoCut)
- [My_Projects](https://github.com/hemangjoshi37a/My_Projects)
- [Cool Arduino and ESP8266 or NodeMCU Projects](https://github.com/hemangjoshi37a/my_Arduino)
- [Telegram Trade Msg Backtest ML](https://github.com/hemangjoshi37a/TelegramTradeMsgBacktestML)

## Checkout Our Other Products:
- [WiFi IoT LED Matrix Display](https://hjlabs.in/product/wifi-iot-led-display)
- [SWiBoard WiFi Switch Board IoT Device](https://hjlabs.in/product/swiboard-wifi-switch-board-iot-device)
- [Electric Bicycle](https://hjlabs.in/product/electric-bicycle)
- [Product 3D Design Service with Solidworks](https://hjlabs.in/product/product-3d-design-with-solidworks/)
- [AutoCut : Automatic Wire Cutter Machine](https://hjlabs.in/product/automatic-wire-cutter-machine/)
- [Custom AlgoTrading Software Coding Services](https://hjlabs.in/product/custom-algotrading-software-for-zerodha-and-angel-w-source-code//)
- [SWiBoard :Tasmota MQTT Control](https://play.google.com/store/apps/details?id=in.hjlabs.swiboard)
- [Custom Token Classification or Named Entity Recognition (NER) model as in Natural Language Processing (NLP) Machine Learning](https://hjlabs.in/product/custom-token-classification-or-named-entity-recognition-ner-model-as-in-natural-language-processing-nlp-machine-learning/)

## Some Cool Arduino and ESP8266 (or NodeMCU) IoT projects:
- [IoT_LED_over_ESP8266_NodeMCU : Turn LED on and off using web server hosted on a nodemcu or esp8266](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_LED_over_ESP8266_NodeMCU)
- [ESP8266_NodeMCU_BasicOTA : Simple OTA (Over The Air) upload code from Arduino IDE using WiFi to NodeMCU or ESP8266](https://github.com/hemangjoshi37a/my_Arduino/tree/master/ESP8266_NodeMCU_BasicOTA)  
- [IoT_CSV_SD : Read analog value of Voltage and Current and write it to SD Card in CSV format for Arduino, ESP8266, NodeMCU etc](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_CSV_SD)  
- [Honeywell_I2C_Datalogger : Log data in A SD Card from a Honeywell I2C HIH8000 or HIH6000 series sensor having external I2C RTC clock](https://github.com/hemangjoshi37a/my_Arduino/tree/master/Honeywell_I2C_Datalogger)
- [IoT_Load_Cell_using_ESP8266_NodeMC : Read ADC value from High Precision 12bit ADS1015 ADC Sensor and Display on SSD1306 SPI Display as progress bar for Arduino or ESP8266 or NodeMCU](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_Load_Cell_using_ESP8266_NodeMC)
- [IoT_SSD1306_ESP8266_NodeMCU : Read from High Precision 12bit ADC seonsor ADS1015 and display to SSD1306 SPI as progress bar in ESP8266 or NodeMCU or Arduino](https://github.com/hemangjoshi37a/my_Arduino/tree/master/IoT_SSD1306_ESP8266_NodeMCU)  

## Checkout Our Awesome 3D GrabCAD Models:
- [AutoCut : Automatic Wire Cutter Machine](https://grabcad.com/library/automatic-wire-cutter-machine-1)
- [ESP Matrix Display 5mm Acrylic Box](https://grabcad.com/library/esp-matrix-display-5mm-acrylic-box-1)
- [Arcylic Bending Machine w/ Hot Air Gun](https://grabcad.com/library/arcylic-bending-machine-w-hot-air-gun-1)
- [Automatic Wire Cutter/Stripper](https://grabcad.com/library/automatic-wire-cutter-stripper-1)

## Our HuggingFace Models :
- [hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086 : Stock tip message NER(Named Entity Recognition or Token Classification) using HUggingFace-AutoTrain and LabelStudio and Ratnakar Securities Pvt. Ltd.](https://huggingface.co/hemangjoshi37a/autotrain-ratnakar_1000_sample_curated-1474454086)

## Our HuggingFace Datasets :
- [hemangjoshi37a/autotrain-data-ratnakar_1000_sample_curated : Stock tip message NER(Named Entity Recognition or Token Classification) using HUggingFace-AutoTrain and LabelStudio and Ratnakar Securities Pvt. Ltd.](https://huggingface.co/datasets/hemangjoshi37a/autotrain-data-ratnakar_1000_sample_curated)

## Awesome Youtube Videos :
- [❤️ હદય અને હદયના ધબકારા 💙 दिल और दिल की धड़कन 💖 Heart and beating of heart by Priyanka madam. 💕](https://www.youtube.com/watch?v=9v3MK6oTOeA)
- [🩸 રુધિર વહીનીઓ અને એના કર્યો. 🩸 Blood Vessels And Working of Blood Vessels 🩸 By Priyankama'am](https://www.youtube.com/watch?v=T7mMcEYNKyQ)
- [🩸 મનુષ્યમાં પરિવહન તંત્ર 🩸 परिसंचरण तंत्र 🩸 Blood Circulation System in Humans🩸 By Priyanka madam](https://www.youtube.com/watch?v=vxa6o_wrWnY)
- [AutoCut V2 - The World's Most Powerful Arduino Automatic Wire Cutting Machine](https://www.youtube.com/watch?v=oGr0mWmNhKY)
- [SWiBoard - A Killer Gadget to Boost Your Boring Switchboard](https://www.youtube.com/watch?v=ftza6WM4LiE)
- [🧪 મનુષ્યમાં ઉત્સર્જન-તંત્ર 🦠 मानव उत्सर्जन तंत्र ⚗️ excretory system 🩺](https://www.youtube.com/watch?v=UUGI-CFKsWI)
- [🌳વનસ્પતિમાં પાણી અને ખનીજ તત્વોનું વહન 🌲](https://youtu.be/1da9p6iYlr4)
- [🌲 વનસ્પતિમાં બાષ્પોત્સર્જન 🌳 पेड़ में वाष्पोत्सर्जन 🎄Transpiration in Trees](https://youtu.be/I9Sirc42Ktg)
- [🫁 સજીવોમાં શ્વસન 🧬 जीवों में श्वास 🫀 Breathing in organisms 👩🏻‍🔬](https://youtu.be/sIMl4t2OFmY)
- [🫁 શ્વસનની પ્રક્રિયા 🫀Respiratory System 🦠](https://youtu.be/hua8ZD5Ge1w)
- [🫁 મનુષ્યમાં શ્વાસ અને ઉચ્છશ્વાસ ⚛️ ](https://youtu.be/BI-CYgnkGCw)

## My Quirky Blog :
- [Hemang Joshi](http://hemangjoshi.blogspot.com/)

## Awesome Android Apps :
- [SWiBoard :Tasmota MQTT Control](https://play.google.com/store/apps/details?id=in.hjlabs.swiboard)
 
## Checkout Cool GitLab Other Repositories:
- [pyPortMan](https://gitlab.com/hemangjoshi37a/pyPortMan)
- [transformers_stock_prediction](https://gitlab.com/hemangjoshi37a/transformers_stock_prediction)
- [TrendMaster](https://gitlab.com/hemangjoshi37a/TrendMaster)
- [hjAlgos_notebooks](https://gitlab.com/hemangjoshi37a/hjAlgos_notebooks)
- [AutoCut](https://gitlab.com/hemangjoshi37a/AutoCut)
- [My_Projects](https://gitlab.com/hemangjoshi37a/My_Projects)
- [Cool Arduino and ESP8266 or NodeMCU Projects](https://gitlab.com/hemangjoshi37a/my_Arduino)
- [Telegram Trade Msg Backtest ML](https://gitlab.com/hemangjoshi37a/TelegramTradeMsgBacktestML)

## Awesome Fiverr. Gigs:
- [develop machine learning ner model as in nlp using python](https://www.fiverr.com/share/9YNabx)
- [train custom chatgpt question answering model](https://www.fiverr.com/share/rwx6r7)
- [build algotrading, backtesting and stock monitoring tools using python](https://www.fiverr.com/share/A7Y14q)
- [tutor you in your science problems](https://www.fiverr.com/share/zPzmlz)
- [make apps for you crossplatform	](https://www.fiverr.com/share/BGw12l)

### Core Implementation Code & Architecture
#### File: `.vscode/settings.json`
```python
{
    "editor.tabCompletion": "on",
    "diffEditor.codeLens": true
}
```

#### File: `ipython_cell_input.py`
```python
quote_list = []

for i in n50df['tradingsymbol']:
    print(i)
    myquote = kite.quote([exchange_type+':'+i])
    quote_list.append(myquote)
quote_list
#     print(n50df['tradingsymbol'])
```

#### File: `act.py`
```python
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import pdb

kws = ""
kite = ""

api_k = "w19o0chuo929jxkp"  # api_key
api_s = "gsw8ps17ex7lf3cuji4prfnwb4vlyr4y"  # api_secret


def get_login(api_k="w19o0chuo929jxkp", api_s="gsw8ps17ex7lf3cuji4prfnwb4vlyr4y"):  # log in to zerodha API panel
    global kws, kite
    kite = KiteConnect(api_key=api_k)

    print("[*] Generate access Token : ", kite.login_url())
    request_tkn = input("[*] Enter Your Request Token Here : ")
    data = kite.generate_session(request_tkn, api_secret=api_s)
    kite.set_access_token(data["access_token"])
    kws = KiteTicker(api_k, data["access_token"])
    print(data['access_token'])


get_login(api_k, api_s)
```

#### File: `calculator.py`
```python
import kivy
kivy.require('1.0.6')
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.properties import ObjectProperty

class Calculator(BoxLayout):
    nse = ObjectProperty(None)
    bse = ObjectProperty(None)
    input_filter = ObjectProperty(None, allownone=True)

    def backward(self, express):
        pass

    def calculate(self, express):
        if not express: return
        try:
            self.display.text = str(eval(express))
        except Exception:
            self.display.text = 'error'

    def calc(self, text):
        print(text)

    def change(self):
        if self.nse.active:
            print('NSE')
        elif self.bse.active:
            print('BSE')

class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ in ('__main__', '__android__'):
    CalculatorApp().run()
```

#### File: `login_old.py`
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.parse as urlparse
from selenium.webdriver.chrome.options import Options
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import pdb
import logging
logging.basicConfig(level=logging.ERROR)

# pip3 install selenium
# pip3 install urllib3

class ZerodhaAccessToken:
    def __init__(self):
        self.apiKey = 'w19o0chuo929jxkp'
        self.apiSecret = 'gsw8ps17ex7lf3cuji4prfnwb4vlyr4y'
        self.accountUserName = 'AB1234'
        self.accountPassword = 'mypassword'
        self.securityPin = 'myPIN'

    def getaccesstoken(self):
        try:
            login_url = "https://kite.trade/connect/login?v=3&api_key={apiKey}".format(apiKey=self.apiKey)

            chrome_driver_path = "/usr/bin/chromedriver"
            options = Options()
            options.add_argument('--headless') #for headless
            driver = webdriver.Chrome(chrome_driver_path, options=options)
            driver.get(login_url)
            wait = WebDriverWait(driver, 5)
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))\
                .send_keys(self.accountUserName)
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))\
                .send_keys(self.accountPassword)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))\
                .submit()
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).click()
            time.sleep(5)
            driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.securityPin)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).submit()
            wait.until(EC.url_contains('status=success'))
            tokenurl = driver.current_url
            parsed = urlparse.urlparse(tokenurl)
            driver.close()
            return urlparse.parse_qs(parsed.query)['request_token'][0]
        except Exception as ex:
            print(ex)

_ztoken = ZerodhaAccessToken()
actual_token = _ztoken.getaccesstoken()
print('access token : '+str(actual_token))
kite = KiteConnect(api_key=_ztoken.apiKey)
data = kite.generate_session(actual_token,api_secret=_ztoken.apiSecret)
kite.set_access_token(data["access_token"])
print('request token : '+str(data["access_token"]))
import joblib
joblib.dump(kite,'kitefile.p')
kws = KiteTicker(_ztoken.apiKey, data["access_token"])
```

#### File: `login.py`
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import urllib.parse as urlparse
from selenium.webdriver.chrome.options import Options
from kiteconnect import KiteConnect
from kiteconnect import KiteTicker
import pandas as pd
import datetime
import joblib
import pdb
import logging
logging.basicConfig(level=logging.ERROR)

# pip3 install selenium
# pip3 install urllib3

class ZerodhaAccessToken:
    def __init__(self):
        self.apiKey = 'w19o0chuo929jxkp'
        self.apiSecret = 'gsw8ps17ex7lf3cuji4prfnwb4vlyr4y'
        self.accountUserName = 'AB1234'
        self.accountPassword = 'mypassword'
        self.securityPin = 'myPIN'

    def getaccesstoken(self):
        try:
            login_url = "https://kite.trade/connect/login?v=3&api_key={apiKey}".format(apiKey=self.apiKey)

            chrome_driver_path = "/usr/bin/chromedriver"
            options = Options()
            options.add_argument('--headless') #for headless
            driver = webdriver.Chrome(chrome_driver_path, options=options)
            driver.get(login_url)
            wait = WebDriverWait(driver, 35)
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="text"]')))\
                .send_keys(self.accountUserName)
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')))\
                .send_keys(self.accountPassword)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))\
                .submit()
            wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="password"]'))).click()
            time.sleep(35)
            driver.find_element_by_xpath('//input[@type="password"]').send_keys(self.securityPin)
            wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]'))).submit()
            wait.until(EC.url_contains('status=success'))
            tokenurl = driver.current_url
            parsed = urlparse.urlparse(tokenurl)
            driver.close()
            return urlparse.parse_qs(parsed.query)['request_token'][0]
        except Exception as ex:
            print(ex)
            
_ztoken = ZerodhaAccessToken()
actual_token = _ztoken.getaccesstoken()
print('access token : '+str(actual_token))
kite = KiteConnect(api_key=_ztoken.apiKey)
data = kite.generate_session(actual_token,api_secret=_ztoken.apiSecret)
kite.set_access_token(data["access_token"])
print('request token : '+str(data["access_token"]))
joblib.dump(kite,'kitefile.p')
kws = KiteTicker(_ztoken.apiKey, data["access_token"])
            
def auto_login():
    global kite,kws,data,_ztoken,actual_token
    _ztoken = ZerodhaAccessToken()
    actual_token = _ztoken.getaccesstoken()
    print('access token : '+str(actual_token))
    kite = KiteConnect(api_key=_ztoken.apiKey)
    data = kite.generate_session(actual_token,api_secret=_ztoken.apiSecret)
    kite.set_access_token(data["access_token"])
    print('request token : '+str(data["access_token"]))
    joblib.dump(kite,'kitefile.p')
    kws = KiteTicker(_ztoken.apiKey, data["access_token"])
```


==================================================
