# ⚡ [QUANT-SOURCE-033] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_033_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Dhan-Calculator (`PHASE4-QUANT-066`)
- **Full Name**: `PHASE4-QUANT-066_naman-n-choudhary__Dhan-Calculator`
- **Description**: Risk Management & Position Sizing Calculator for traders. Calculates real post-tax Risk:Reward, position size, and brokerage costs using Dhan charges.
- **GitHub Stars**: 2
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Dhan Calculator – Risk Management & Position Sizing Tool 💹  

A practical Excel-based **risk management and position sizing calculator** for intraday and delivery traders.  
This tool calculates your **true, post-tax Risk:Reward**, factoring in brokerage charges and transaction taxes using Dhan’s fee structure — something most traders ignore.

It ensures disciplined risk management and accurate position sizing for every trade.

---

## 🔥 Key Features

### **1️⃣ Automatic Position Sizing**
Based on:
- Total Trading Capital  
- % Risk per Trade  
- Leverage Used  
- Stock LTP  
- Desired Risk : Reward Ratio  

The sheet calculates:
- Maximum position size  
- Quantity to trade  
- Gross & Net P/L  
- True risk amount  

---

### **2️⃣ True Risk–Reward After Taxes**
Most traders calculate RR **before charges**.  
This calculator gives your **REAL RR after:**  
- Brokerage  
- STT  
- Exchange Charges  
- GST  
- SEBI Fees  
- Stamp Duty  

You’ll finally know your *actual* profitability.

---

### **3️⃣ Full Brokerage & Tax Breakdown (Order Estimator Tab)**
The second tab includes:
- Buy-side & Sell-side cost breakdown  
- Target-hit vs Stop Loss-hit calculations  
- All charges as per **Dhan (Equity/NSE)**  
- Total cost on both outcomes  

This helps you check the real impact of costs on each trade.

---

### **4️⃣ Daily Ledger (Auto Balance Tracker)**
Automatically logs:
- Trade number  
- P&L  
- Balance  
- Running returns  
- Daily gains/losses  

Useful for consistency tracking and journaling.

---

## 📝 How to Use

### **1. Only Edit BLUE Cells**
Editable inputs (BLUE font):
- Your Capital  
- Risk %  
- LTP  
- Desired Risk:Reward  
- Order Type (Buy/Sell)  
- Type of Trade 

⚠️ **Do NOT edit cells in black/green/orange — those contain formulas.**

---

### **2. Let the Sheet Auto-Calculate**
Once inputs are filled, the model computes:
- Ideal Position Size  
- Quantity  
- Max allowed position  
- Gross & Net profit/loss  
- Practical RR (after taxes)  

---

### **3. Use the Order Estimator Tab**
View:
- All brokerage components  
- Total charges after Target Hit  
- Total charges after Stop Loss Hit  

This tab handles all Dhan-specific taxes.

---

## ⚠️ IMPORTANT: Excel Error Fix  
When opening for the first time, Excel may show:

- **Circular reference warning**  
- Or formulas not updating  

This happens because the sheet uses **iterative logic** for position sizing.

### ✅ To Fix:
1. Go to **File → Options**  
2. Click **Formulas**  
3. Under *Calculation Options* →  
   ✔ Tick **Enable iterative calculations**  
4. Press **OK**  

The model will work perfectly afterwards.

---

## 📂 Files Included
| File | Description |
|------|-------------|
| `Dhan Calculator.xlsx` | Main model for risk sizing, RR calculation & ledger tracking |
| `Order Estimator` Tab | Full brokerage & tax breakdown |

---

## 🎯 Why This Tool Matters
Every trader talks about:
- “RR 2:1 hai”  
- “Setup strong hai”  
- “Accuracy high hai”  

But almost NO ONE checks:
- **RR after taxes**  
- **Net profit after charges**  
- **Practical vs theoretical RR**  

This calculator bridges that gap and makes your trading realistic & professional.

---

## 👤 Author
**Naman Narendra Choudhary**  
🔗 GitHub: https://github.com/LIGHTARK-2903  
🔗 LinkedIn: https://linkedin.com/in/lightark


==================================================


## [2/3] Repository: zerodha-kite-auto-trading (`PHASE4-QUANT-068`)
- **Full Name**: `PHASE4-QUANT-068_arneish__zerodha-kite-auto-trading`
- **Description**: 
- **GitHub Stars**: 7
- **Source Pool**: `phase4_quant_wheels_100`

### Core Implementation Code & Architecture
#### File: `portfolioManager.py`
```python
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import json

class portfolioManager(object):
    def __init__(self):
        self.stockElement = None
        self.stockElementTicker = []
        self.maxIters = 100
        self.tickerInterval = 1
        self.maxNumOrders = 100
        self.timeout = 10
        
        self.loadLoginDetails()
        self.launchDriver()
        

    def getXpathElement(self, xpath):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def getAllXpathElements(self, xpath):
        firstMatch = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        allElements = self.driver.find_elements_by_xpath(xpath)
        return allElements

    def loadLoginDetails(self):
        with open("loginDetails.json") as loginFile:
            credentials = json.load(loginFile)
            self.userID = credentials['userID']
            self.password = credentials['password']
            self.twoFactorPIN = credentials['twoFactorPIN']

    def launchDriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")        
        self.driver = webdriver.Chrome(chrome_options=options)
        self.pageURL = "https://kite.zerodha.com"
        self.driver.get(self.pageURL)

    def executeLogin(self):
        try:
            xpathUserID = '//*[@id="container"]/div/div/div/form/div[2]/input'
            xpathPassword = '//*[@id="container"]/div/div/div/form/div[3]/input'
            # xpathLoginButton = '//*[@id="container"]/div/div/div/form/div[4]/button'
            inputUserID = self.getXpathElement(xpathUserID)
            inputUserID.send_keys(self.userID)
            inputPassword = self.getXpathElement(xpathPassword)
            inputPassword.send_keys(self.password)
            inputPassword.send_keys(Keys.ENTER)
            # loginButton = self.getXpathElement(xpathLoginButton)
            # loginButton.click()

            #Two Factor Authentication:
            xpathTwoFactorPIN ='//*[@id="container"]/div/div/div/form/div[2]/div/input'
            inputTwoFactorPIN = self.getXpathElement(xpathTwoFactorPIN)
            inputTwoFactorPIN.send_keys(self.twoFactorPIN)
            inputTwoFactorPIN.send_keys(Keys.ENTER)
            # while True:
            #     a = 5
        except TimeoutException:
            print("Login Failue.")
    
    def executeOrder(self, orderType, numUnits=2):
        # try:
        hoverOverStockName = ActionChains(self.driver).move_to_element(self.stockElement)
        hoverOverStockName.perform()
        if (orderType=='BUY'):
            xpathStockElementBuyButton = '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div/span/button[1]'
            self.getXpathElement(xpathStockElementBuyButton).click()
            self.setOrderOptions(numUnits=numUnits)
            xpathBuyButton = '//*[@id="app"]/div[3]/div/form/div[3]/div[3]/div[2]/button[1]'
            # self.getXpathElement(xpathBuyButton).send_keys("\n")
        else:
            xpathStockElementSellButton = '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div/span/button[2]'
            self.getXpathElement(xpathStockElementSellButton).click()
            self.setOrderOptions(numUnits=numUnits)
            xpathSellButton = '//*[@id="app"]/div[3]/div/form/div[3]/div[3]/div[2]/button[1]'
            # self.getXpathElement(xpathSellButton).send_keys("\n")
        hoverOverStockName.release()
        # except TimeoutException:
        #     print("Timeout Exception in Placing Order")
    
    def setOrderOptions(self, MIS=True, market=True, numUnits=1):
        if (MIS):
            misRadioButton = self.getXpathElement('//*[@value="MIS"]')
            misRadioButton.send_keys(Keys.SPACE)
        if (market):
            self.getXpathElement('//*[@value="MARKET"]').send_keys(Keys.SPACE)
        self.getXpathElement('//*[@label="Qty."]').send_keys(numUnits)

    def executeStrategyOne(self, stockName='YESBANK'):
        if (self.stockElement==None):
            xpathMarketWatchNames = '//*[@id="app"]/div[2]/div[1]/div/div[2]/div/div/div/div/span[1]/span/span'
            xpathStockElementTicker = 
            allMarketWatchStockElements = self.getAllXpathElements(xpathMarketWatchNames)
            self.stockElement = next(stockElement_ for stockElement_ in allMarketWatchStockElements if stockElement_.text == stockName)
            self.stockElementTicker = self.getXpathElement()
        countIter = 0
        countOrders = 0
        while (countIter < self.maxIters and countOrders < self.maxNumOrders):
            
            
            
            
            countIter+=1


        
        

        
            

if __name__=="__main__":
    obj = portfolioManager()
    obj.executeLogin()
    obj.executeOrder(orderType='BUY')
    obj.executeOrder(orderType='SELL')
    # while True:
    #     a = 5
```


==================================================


## [3/3] Repository: kite_kill_switch (`PHASE4-QUANT-070`)
- **Full Name**: `PHASE4-QUANT-070_Pranavoro__kite_kill_switch`
- **Description**: A simple kill switch for a kite to prevent overtrading.
- **GitHub Stars**: 6
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Kite Kill Switch Project
A simple kill switch for a kite to prevent overtrading.

## Description
This project is a simple kill switch for a kite. It is designed to stop overtrading. The kill switch will check if you have any open positions and if the total loss is above a specified threshold. If the loss is above the threshold, the kill switch will close all positions, cancel all orders, and activate the kill switch. The kill switch will wait for a specified time before checking again. This project is designed to prevent overtrading and protect your capital.

## Language
- Python 3.8

## Libraries
- kiteconnect
- pandas
- json
- time
- datetime
- os
- sys
- logging
- selenium

## Installation
1. Clone the repository
2. Add `position_kill_switch.py` to your task scheduler or crontab.

## Configuration
A template configuration file (`credentials_template.json`) is provided in the repository. You can copy the template and rename it to `credentials.json`. Then you can modify the configuration file to suit your needs.

> You need to have the necessary API credentials to run the script. You can get the API credentials from the [Kite Connect](https://kite.trade/).

> TOTP must be enabled in your Kite account for this project to work.

> Please ensure that you have the necessary API credentials in the `credentials.json` file before running the script. Without the correct credentials, the script will not be able to access the necessary data and perform the required actions.

## Usage
1. Run `position_kill_switch.py`.
2. The script will check if you have any open positions.
3. Then the script will check if the total loss is above threshold.
4. If the loss is above threshold, the script will close positions, cancel all orders and activate the kill switch.
5. The script will wait for a specified time before checking again.

## Alt Usage
1. You can also directly run the `kill_switch.py` script to manually activate the kill switch.
2. This script will skip the checks and wont cancel orders or close positions, but directly activate the kill switch.

## Author
Hi, I'm `Pranav Meher`, the author of this project.
I am a skilled software developer with a strong background in algorithmic trading. I have a deep understanding of the financial markets and have successfully implemented numerous trading strategies. I am passionate about creating reliable solutions to prevent overtrading and am dedicated to continuously improving this kill switch project. I welcome feedback and contributions from the community.

You can connect with me or reach out to me to learn more about my work and stay updated on the latest developments.
- [LinkedIn](https://www.linkedin.com/in/pranavmeher/) 
- [GitHub](https://github.com/Pranavoro)
- [Email](mailto:meherpranav5@gmail.com)
- [Twitter](https://twitter.com/pranav_meher)
- [Upwork](https://www.upwork.com/freelancers/~01bae9d3b236500043)
- [Buy me a coffee ☕️](https://buymeacoffee.com/pranavoro)

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License
This project is licensed under the GNU GENERAL PUBLIC LICENSE - see the [LICENSE](LICENSE.txt) file for details.

### Core Implementation Code & Architecture
#### File: `credentials_template.json`
```python
{
    "<client_id>": {
        "client_id": "<Client ID>",
        "totp_key": "<Kite TOTP key (not the otp)>",
        "password": "<Kite password>",
        "api_key": "<API key from kite connect app>",
        "secret_key": "<secret from kite connect app>",
        "access_token": "<leave this blank>",
        "loss_threshold": "<loss threshold in rupees>"
    }
}
```

#### File: `get_logger.py`
```python
import logging
import os
import datetime as dt
import pytz

def get_logger(file_name):
    # get logs path as current files path
    logs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"logs")
    
    print(logs_path)
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)

    tz = pytz.timezone('Asia/Kolkata')
    tz_abbreviation = dt.datetime.now(tz=tz).strftime('%Z')
    logging.Formatter.converter = lambda *args: dt.datetime.now(tz=tz).timetuple()
    formatter = logging.Formatter('[%(asctime)s '+tz_abbreviation+'][%(filename)s :%(lineno)4s][%(levelname)8s] ~ %(message)s',"%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(filename= os.path.join(logs_path,f"{file_name}_{dt.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime('%Y_%m_%d')}.log"),mode="a")
    file_handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    try:
        if len(logger.handlers) > 0:
            logger.removeHandler(file_handler)
            logger.removeHandler(console_handler)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    except:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
```

#### File: `login_kite.py`
```python
import requests
import json
import pyotp
from kiteconnect import KiteConnect
from urllib.parse import urlparse
from urllib.parse import parse_qs
import os
import traceback
import json

current_file_path = os.path.dirname(os.path.realpath(__file__))


def get_client_doc_from_json(client_id):
   try:
       json_file = os.path.join(current_file_path,'credentials.json')
       with open(json_file) as f:
           data = json.load(f)
           return data[client_id]
   except Exception as e:
       traceback.print_exc()

def login(client_id):
    user_doc = get_client_doc_from_json(client_id)
    api_key = user_doc['api_key']
    user_id = user_doc['client_id']
    user_password = user_doc['password']
    totp_key = user_doc['totp_key']
    api_secret = user_doc['secret_key']

    http_session = requests.Session()
    url = http_session.get(url='https://kite.trade/connect/login?v=3&api_key='+api_key).url
    response = http_session.post(url='https://kite.zerodha.com/api/login', data={'user_id':user_id, 'password':user_password})
    resp_dict = json.loads(response.content)
    http_session.post(url='https://kite.zerodha.com/api/twofa', data={'user_id':user_id, 'request_id':resp_dict["data"]["request_id"], 'twofa_value':pyotp.TOTP(totp_key).now()})
    url = url + "&skip_session=true"
    response = http_session.get(url=url, allow_redirects=True).url
    print(response)
    request_token = parse_qs(urlparse(response).query)['request_token'][0]

    kite = KiteConnect(api_key=api_key)
    data = kite.generate_session(request_token, api_secret=api_secret)
    access_token = data["access_token"]
    return access_token
```

#### File: `kill_switch.py`
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import mintotp
import traceback
import os
import time


current_file_path = os.path.dirname(os.path.realpath(__file__))


def get_client_doc_from_json(client_id):
   try:
       json_file = os.path.join(current_file_path,'credentials.json')
       with open(json_file) as f:
           data = json.load(f)
           return data[client_id]
   except Exception as e:
       traceback.print_exc()

def get_totp(userid):
    totp_key = get_client_doc_from_json(userid)['totp_key']
    totp = mintotp.totp(totp_key)
    return totp

def disable_segment(client_id):
    try:
        password = get_client_doc_from_json(client_id)['password']
        #! Get to the console - segment activation page
        driver.get("https://console.zerodha.com/account/segment-activation")
        time.sleep(2)
       
        
        #! Login
        driver.find_element(by=By.ID,value="userid").send_keys(client_id)
        time.sleep(1)
        driver.find_element(by=By.ID,value="password").send_keys(password)
        time.sleep(1)
        driver.find_element(by = By.XPATH, value = "/html/body/div[1]/div/div/div[1]/div/div/div/form/div[4]/button").click()
        time.sleep(1)
        driver.find_element(by = By.XPATH, value = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/form/div[1]/input").send_keys(get_totp(client_id))
        time.sleep(5)


        #! Disable the NSE-FO segment.
        #! To add different segments, you can always copy xpath from inspecting element and replace below xpath.
        driver.find_element(by = By.XPATH, value = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/div[2]/div/div/div/div[3]/div/div/div/label").click()
        time.sleep(1)

        #! Clicking on continue
        driver.find_element(by = By.XPATH, value = "/html/body/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[4]/div[1]/button").click()
        time.sleep(5)

        #! Clicking on confirm-page continue button
        driver.find_element(by = By.XPATH, value = "/html/body/div[2]/div[2]/div/div/div[2]/div/div/div/div/form/div[2]/button[2]").click()
        time.sleep(10)

        #! Exit the browser
        driver.quit()
    except:
        traceback.print_exc()


def main(client_id):
    global driver
    options = webdriver.ChromeOptions()
    options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    # options.add_argument("--headless")
    disable_segment(client_id)


if __name__ == '__main__':
    global driver
    options = webdriver.ChromeOptions()
    options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    # options.add_argument("--headless")
    disable_segment("<your client id here>")
    # driver.quit()
```

#### File: `positions_kill_switch.py`
```python
from kiteconnect import KiteConnect
import os
import sys
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import traceback
import json
import login_kite
import kill_switch
import get_logger
import datetime as dt
import pytz
import sqlite3

logger = get_logger.get_logger("positions_kill_switch")

current_file_path = os.path.dirname(os.path.realpath(__file__))


def get_client_doc_from_json(client_id):
    try:
        json_file = os.path.join(current_file_path, 'credentials.json')
        with open(json_file) as f:
            data = json.load(f)
            return data[client_id]
    except Exception as e:
        logger.error(f"Error reading client document for {client_id}: {traceback.format_exc()}")
        return None


def save_field_to_json(client_id, field, value):
    try:
        json_file = os.path.join(current_file_path, 'credentials.json')
        with open(json_file) as f:
            data = json.load(f)
            data[client_id][field] = value
        with open(json_file, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Successfully saved {field} for {client_id} in credentials.json")
    except Exception as e:
        logger.error(f"Error saving field to JSON for {client_id}: {traceback.format_exc()}")

def save_data_to_sqllite(client_id, field, value):
    try:
        conn = sqlite3.connect(os.path.join(current_file_path,'client_data.db'))
        c = conn.cursor()
        c.execute(f'''CREATE TABLE IF NOT EXISTS clients (client_id TEXT PRIMARY KEY, loss_threshold REAL);''')
        c.execute(f"INSERT OR REPLACE INTO clients (client_id, {field}) VALUES (?, ?)", (client_id, value))
        conn.commit()
        conn.close()
        logger.info(f"Successfully saved {field} for {client_id} in SQLite")
    except:
        logger.error(f"Error saving field to SQLite for {client_id}: {traceback.format_exc()}")
        traceback.print_exc()

def get_data_from_sqllite(client_id, field):
    try:
        conn = sqlite3.connect(os.path.join(current_file_path,'client_data.db'))
        c = conn.cursor()
        c.execute(f"SELECT {field} FROM clients WHERE client_id = ?", (client_id,))
        value = c.fetchone()[0]
        conn.close()
        return value
    except:
        logger.error(f"Error fetching field from SQLite for {client_id}: {traceback.format_exc()}")
        traceback.print_exc()

def get_kite_client(client_id):
    api_key = get_client_doc_from_json(client_id)['api_key']
    global kite
    kite = KiteConnect(api_key=api_key)
    try:
        access_token = get_client_doc_from_json(client_id)['access_token']
        kite.set_access_token(access_token=access_token)
        profile = kite.profile()
        logger.info(f"Access Token is valid, fetched from json for {client_id}. Profile: {profile}")
    except Exception as e:
        logger.error(f"Error with access token for {client_id}, attempting login: {traceback.format_exc()}")
        try:
            access_token = login_kite.login(client_id)
            kite.set_access_token(access_token=access_token)
            profile = kite.profile()
            logger.info(f"Successfully logged in and retrieved profile for {client_id}. Profile: {profile}")
            save_field_to_json(client_id, 'access_token', access_token)
        except:
            logger.error(f"Error in login for {client_id}: {traceback.format_exc()}")
            sys.exit(0)

    return kite


def get_positions_mtm():
    try:
        positions = kite.positions()
        logger.info(f"Fetched positions: {positions}")
        mtm = 0.0
        for position in positions['net']:
            if 'NIFTY' in position['tradingsymbol'] or 'BANKNIFTY' in position['tradingsymbol']:
                logger.info(f"Processing position: {position}")
                symbol = position['tradingsymbol']
                pos_qty = position['buy_quantity'] - position['sell_quantity']
                ltp_symbol = f"{position['exchange']}:{symbol}"
                ltp = kite.ltp([ltp_symbol])
                logger.info(f"Fetched LTP for {ltp_symbol}: {ltp}")
                
                mtm += (position['sell_value'] - position['buy_value']) + (pos_qty * ltp[ltp_symbol]['last_price'] * position['multiplier'])
        return mtm
    except Exception as e:
        logger.error(f"Error calculating MTM: {traceback.format_exc()}")
        return 0


def cancel_all_orders():
    try:
        orders = kite.orders()
        open_orders = [order for order in orders if order['status'] == 'OPEN']
        for order in open_orders:
            logger.info(f"Cancelling order: {order}")
            if 'NIFTY' in order['tradingsymbol'] or 'BANKNIFTY' in order['tradingsymbol']:
                kite.cancel_order(variety=order['variety'], order_id=order['order_id'])
    except Exception as e:
        logger.error(f"Error cancelling orders: {traceback.format_exc()}")


def exit_all_positions():
    try:
        positions = kite.positions()
        open_positions = [position for position in positions['net'] if ('NIFTY' in position['tradingsymbol'] or 'BANKNIFTY' in position['tradingsymbol']) and position['quantity'] != 0]
        for position in open_positions:
            transaction_type = 'SELL' if position['quantity'] > 0 else 'BUY'
            logger.info(f"Exiting position: {position}")
            kite.place_order(
                variety='regular',
                exchange=position['exchange'],
                tradingsymbol=position['tradingsymbol'],
                transaction_type=transaction_type,
                quantity=abs(position['quantity']),
                order_type='MARKET',
                product='NRML'
            )
    except Exception as e:
        logger.error(f"Error exiting positions: {traceback.format_exc()}")


if __name__ == '__main__':
    start_time = time.time()
    try:
        save_loss_threshold = False
        ist = pytz.timezone('Asia/Kolkata')
        now = dt.datetime.now(ist)
        if now.hour == 9 and now.minute == 15 and now.second < 20:
            save_loss_threshold = True


        json_file = os.path.join(current_file_path, 'credentials.json')
        with open(json_file) as f:
            data = json.load(f)
            data = dict(data)
            for client_id in data.keys():
                if save_loss_threshold:
                    LT = get_client_doc_from_json(client_id)['loss_threshold']
                    if type(LT) in [int, float]:
                        save_data_to_sqllite(client_id, 'loss_threshold', LT)
                    else:
                        logger.error(f"Loss Threshold for {client_id} is not a number: {LT}")

                loss_threshold = float(get_data_from_sqllite(client_id, 'loss_threshold'))
                kite = get_kite_client(client_id)
                MTM = 0.0
                MTM = float(get_positions_mtm())
                logger.info(f"Current MTM for {client_id}: {MTM} ; Loss Threshold: {loss_threshold}")

                if MTM <= loss_threshold * -1:
                    cancel_all_orders()
                    exit_all_positions()
                    # kill_switch.main(client_id) # This will turn off the Segment. (To Turn on, remove the comment (the hash and space before kill_switch.main(client_id)))
            save_loss_threshold = False
    except Exception as e:
        logger.error(f"Error reading credentials.json: {traceback.format_exc()}")
    end_time = time.time()
    logger.info(f"Time taken to execute: {end_time - start_time:.2f} seconds")
```


==================================================
