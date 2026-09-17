# ⚡ [QUANT-SOURCE-149] Consolidated Quant & Algo Trading Repositories
**Category**: `OPTIONS_GREEKS_VOLATILITY` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_149_OPTIONS_GREEKS_VOLATILITY.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: fetchNSEOptionChainData (`VAULT_IN-QUANT-076_RepleteSS__fetchNSEOptionChainData`)
- **Full Name**: `IN-QUANT-076_RepleteSS__fetchNSEOptionChainData`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# fetchNSEOptionChainData

On executing this application , it gives NSE option chain data with current Nifty spot price nearer to strike price (10 Upper and 10 Lower strike prices)
It gives OI, OI Chng, and volume data for both PE and CE. 

It also indicates Highest OI, Highest OI CHNG and Highest Volume on every run. With the help of this data we can predict about nifty to gap up or gap down for next day.

Trade can be taken at 3:20pm the previous day. Basically it will help to take BTST trade. 

For logic to predict gap up or gap down. Ping me.

### Core Implementation Code & Architecture
#### File: `imrnseOptionChain.py`
```python
# Libraries
import time

import requests
import json
import math
from datetime import datetime
import shutil
from pytz import timezone

# Python program to print
# colored text and background
def strRed(skk):         return "\033[91m {}\033[00m".format(skk)
def strGreen(skk):       return "\033[92m {}\033[00m".format(skk)
def strYellow(skk):      return "\033[93m {}\033[00m".format(skk)
def strLightPurple(skk): return "\033[94m {}\033[00m".format(skk)
def strPurple(skk):      return "\033[95m {}\033[00m".format(skk)
def strCyan(skk):        return "\033[96m {}\033[00m".format(skk)
def strLightGray(skk):   return "\033[97m {}\033[00m".format(skk)
def strBlack(skk):       return "\033[98m {}\033[00m".format(skk)
def strBold(skk):        return "\033[1m {}\033[0m".format(skk)

now = datetime.now()
format = "%Y-%m-%d %H:%M:%S %Z%z"
now_utc = datetime.now(timezone('UTC'))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))
fName = "NSE-OptionChain_"+ now_asia.strftime(format)+".csv"
print(fName)

# Method to get nearest strikes
def round_nearest(x,num=50): return int(math.ceil(float(x)/num)*num)
def nearest_strike_bnf(x): return round_nearest(x,100)
def nearest_strike_nf(x): return round_nearest(x,50)

# Urls for fetching Data
url_oc      = "https://www.nseindia.com/option-chain"
url_bnf     = 'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY'
url_nf      = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
url_indices = "https://www.nseindia.com/api/allIndices"

# Headers
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'accept-language': 'en,gu;q=0.9,hi;q=0.8',
            'accept-encoding': 'gzip, deflate, br'}

sess = requests.Session()
cookies = dict()

# Local methods
def set_cookie():
    request = sess.get(url_oc, headers=headers, timeout=5)
    cookies = dict(request.cookies)

def get_data(url):
    set_cookie()
    response = sess.get(url, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==401):
        set_cookie()
        response = sess.get(url_nf, headers=headers, timeout=5, cookies=cookies)
    if(response.status_code==200):
        return response.text
    return ""

def set_header():
    global bnf_ul
    global nf_ul
    global bnf_nearest
    global nf_nearest
    response_text = get_data(url_indices)
    data = json.loads(response_text)
    for index in data["data"]:
        if index["index"]=="NIFTY 50":
            nf_ul = index["last"]
            print("nifty")
        if index["index"]=="NIFTY BANK":
            bnf_ul = index["last"]
            print("banknifty")
    bnf_nearest=nearest_strike_bnf(bnf_ul)
    nf_nearest=nearest_strike_nf(nf_ul)

# Showing Header in structured format with Last Price and Nearest Strike

def print_header(index="",ul=0,nearest=0):
    print(strPurple( index.ljust(12," ") + " => ")+ strLightPurple(" Last Price: ") + strBold(str(ul)) + strLightPurple(" Nearest Strike: ") + strBold(str(nearest)))

def print_hr():
    print(strYellow("|".rjust(70,"-")))

# Fetching CE and PE data based on Nearest Expiry Date
def print_oi(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                #print(strCyan(str(item["strikePrice"])) + strGreen(" CE ") + "[ " + strBold(str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + strRed(" PE ")+"[ " + strBold(str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
                print(data["records"]["expiryDates"][0] + " " + str(item["strikePrice"]) + " CE " + "[ " + strBold(str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + " PE " + "[ " + strBold(str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
                strike = strike + step

# Finding highest Open Interest of People's in CE based on CE data
def highest_oi_CE(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_oi = 0
    max_oi_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["CE"]["openInterest"] > max_oi:
                    max_oi = item["CE"]["openInterest"]
                    max_oi_strike = item["strikePrice"]
                strike = strike + step
    return max_oi_strike

#Fetching Highest Oi Data for CE
def highest_oi_CE_Data(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_oi = 0
    max_oi_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["CE"]["openInterest"] > max_oi:
                    max_oi = item["CE"]["openInterest"]
                    max_oi_strike = item["strikePrice"]
                strike = strike + step
    return max_oi

# Finding highest Change In OI Strike Price in CE based on CE data
def highest_ChngInOI_CE(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_OiChng = 0
    max_oiChng_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["CE"]["changeinOpenInterest"] > max_OiChng:
                    max_OiChng = item["CE"]["changeinOpenInterest"]
                    max_oiChng_strike = item["strikePrice"]
                strike = strike + step
    return max_oiChng_strike

#Fetching highest OI at PE
def highest_oi_PE(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_oi = 0
    max_oi_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["PE"]["openInterest"] > max_oi:
                    max_oi = item["PE"]["openInterest"]
                    max_oi_strike = item["strikePrice"]
                strike = strike + step
    return max_oi_strike

def highest_oi_PE_Data(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_oi = 0
    max_oi_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["PE"]["openInterest"] > max_oi:
                    max_oi = item["PE"]["openInterest"]
                    max_oi_strike = item["strikePrice"]
                strike = strike + step
    return max_oi
#Finding Highest OI chng at CE
def highest_ChngInOI_CE_Data(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_OiChng = 0
    max_oiChng_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["CE"]["changeinOpenInterest"] > max_OiChng:
                    max_OiChng = item["CE"]["changeinOpenInterest"]
                    max_oiChng_strike = item["strikePrice"]
                strike = strike + step
    return max_OiChng


# Finding highest Change In OI Strik Price in PE based on PE data
def highest_ChngInOI_PE(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_OiChng = 0
    max_OiChng_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["PE"]["changeinOpenInterest"] > max_OiChng:
                    max_OiChng = item["PE"]["changeinOpenInterest"]
                    max_OiChng_strike = item["strikePrice"]
                strike = strike + step
    return max_OiChng_strike


#Finding highest Change In OI Data in PE based on PE data

def highest_ChngInOI_PE_Data(num,step,nearest,url):
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_OiChng = 0
    max_OiChng_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                if item["PE"]["changeinOpenInterest"] > max_OiChng:
                    max_OiChng = item["PE"]["changeinOpenInterest"]
                    max_OiChng_strike = item["strikePrice"]
                strike = strike + step
    return max_OiChng

# Fetching CE and PE Change in OI data based on Nearest Expiry Date
def print_ChngInOI(num,step,nearest,url):
    print("------------>>>>>>>>> Printing Chng In OI Data <<<<<<<<<<----------------")
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                #print(strCyan(str(item["strikePrice"])) + strGreen(" CE ") + "[ " + strBold(str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + strRed(" PE ")+"[ " + strBold(str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
                print(data["records"]["expiryDates"][0] + " " + str(item["strikePrice"]) + " CE " + "[ " + strBold(str(item["CE"]["changeinOpenInterest"]).rjust(10," ")) + " ]" + " PE " + "[ " + strBold(str(item["PE"]["changeinOpenInterest"]).rjust(10," ")) + " ]")
                strike = strike + step
#Printing Highest Change In Oi For CE and PE
def print_ChngInOI_Data(num,step,nearest,url):
    print("------------>>>>>>>>> Printing Chng In OI Data <<<<<<<<<<----------------")
    strike = nearest - (step*num)
    start_strike = nearest - (step*num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike+(step*num*2):
                #print(strCyan(str(item["strikePrice"])) + strGreen(" CE ") + "[ " + strBold(str(item["CE"]["openInterest"]).rjust(10," ")) + " ]" + strRed(" PE ")+"[ " + strBold(str(item["PE"]["openInterest"]).rjust(10," ")) + " ]")
                print(data["records"]["expiryDates"][0] + " " + str(item["strikePrice"]) + " CE " + "[ " + strBold(str(item["CE"]["changeinOpenInterest"]).rjust(10," ")) + " ]" + " PE " + "[ " + strBold(str(item["PE"]["changeinOpenInterest"]).rjust(10," ")) + " ]")
                strike = strike + step
# Finding Highest Volume at CE

def highest_Vol_CE(num, step, nearest, url):
            #print("-------------------->>>>>>>>>>>>>>> Find HIGHEST VOLUME AT CE <<<<<<<<<<<<<----------------------------")
            strike = nearest - (step * num)
            start_strike = nearest - (step * num)
            response_text = get_data(url)
            data = json.loads(response_text)
            currExpiryDate = data["records"]["expiryDates"][0]
            max_vol = 0
            max_vol_strike = 0
            for item in data['records']['data']:
                if item["expiryDate"] == currExpiryDate:
                    if item["strikePrice"] == strike and item["strikePrice"] < start_strike + (step * num * 2):
                        if item["CE"]["totalTradedVolume"] > max_vol:
                            max_vol = item["CE"]["totalTradedVolume"]
                            max_vol_strike = item["strikePrice"]
                        strike = strike + step
            return max_vol_strike


def highest_Volume_Data_CE(num, step, nearest, url):
    # print("-------------------->>>>>>>>>>>>>>> Find HIGHEST VOLUME AT CE <<<<<<<<<<<<<----------------------------")
    strike = nearest - (step * num)
    start_strike = nearest - (step * num)
    response_text = get_data(url)
    data = json.loads(response_text)
    currExpiryDate = data["records"]["expiryDates"][0]
    max_vol_data = 0
    max_vol_strike = 0
    for item in data['records']['data']:
        if item["expiryDate"] == currExpiryDate:
            if item["strikePrice"] == strike and item["strikePrice"] < start_strike + (step * num * 2):
                if item["CE"]["totalTradedVolume"] > max_vol_data:
                    max_vol_data = item["CE"]["totalTradedVolume"]
                    max_vol_strike = item["strikePrice"]
                strike = strike + step
    return max_vol_data
def highest_Vol_PE(num, step, nearest, url):
           # print("-------------------->>>>>>>>>>>>>>> Find HIGHEST VOLUME AT PE <<<<<<<<<<<<<----------------------------")
            strike = nearest - (step * num)
            start_strike = nearest - (step * num)
            response_text = get_data(url)
            data = json.loads(response_text)
            currExpiryDate = data["records"]["expiryDates"][0]
            max_vol = 0
            max_vol_strike = 0
            for item in data['records']['data']:
                if item["expiryDate"] == currExpiryDate:
                    if item["strikePrice"] == strike and item["strikePrice"
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: NSE-Options-Scrapper (`VAULT_IN-QUANT-083_maniceet__NSE-Options-Scrapper`)
- **Full Name**: `IN-QUANT-083_maniceet__NSE-Options-Scrapper`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# NSE Options Scrapper

The python script will enable you to download Options data for all derivative stocks on NSE.
It checks the present underlying value and for a call option gets the Last Traded price of the Strike Price higher than Underlying Value

## Updates
Dependencies on csv files has been removed, the script downloads csv online while it is running and gets the stocsk and lot sizes automatically. Dependency on nsepy package has also been removed.

## Getting Started

Just run the Script NSEScrapper.py on your terminal and the output csv will be generated.

### Prerequisites

Anaconda is preferred, however requirements.txt file is there in the git repo


### Installing

Install anaconda and use python 3.x version

```
conda create --name <myenv>

source activate <myenv>

pip install -r requirements.txt

```
### Running the script

Open terminal or command line, navigate to the folder where the files are and run

```
python3 NSEScrapper.py

```


## Authors

* **Maniceet Sahay** 



## Acknowledgments

* The script was written using Beautiful soup and on NSEPY. For more details on [NSEPY](https://github.com/swapniljariwala/nsepy)

### Core Implementation Code & Architecture
#### File: `NSEScrapper.py`
```python
#Importing libraries required
import re
from datetime import date
from nsepy import get_history
import numpy as np
import pandas as pd
import datetime
from tqdm import tqdm
import requests
import io

#Reading the options list file online
response = requests.get('http://www.nseindia.com/content/fo/fo_mktlots.csv')

file_object = io.StringIO(response.content.decode('utf-8'))
lot_size = pd.read_csv(file_object, skiprows=[0,1,2,3], usecols = [0,1,2])
lot_size.columns = [x.replace(" ", "") for x in lot_size.columns]
lot_size['Symbol'] = lot_size['Symbol'].str.strip()


stocks = list(lot_size['Symbol'])
stocks = [x.replace('&', '%26') for x in stocks]

import requests
from bs4 import BeautifulSoup

# Get all get possible expiry date details for the given script
import requests
from bs4 import BeautifulSoup

# Get all get possible expiry date details for the given script
def get_expiry_from_option_chain (symbol):

    # Base url page for the symbole with default expiry date
    Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=-"

    # Load the page and sent to HTML parse
    page = requests.get(Base_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    
    # Locate where expiry date details are available
    locate_expiry_point = soup.find(id="date")
    underlying_value = str(soup.find('b', {'style':"font-size:1.2em;"}))
    #print(underlying_value)
    underlying_value = re.sub(r'<.*?>', '', underlying_value)
    #print(underlying_value)
    underlying_value = float(re.sub(r'(?=[A-Za-z]).*(?=[A-Za-z])[^\d.]+', '', underlying_value))
    #underlying_value = soup.get_text(underlying_value)
    # Convert as rows based on tag option
    expiry_rows = locate_expiry_point.find_all('option')

    index = 0
    expiry_list = []
    for each_row in expiry_rows:
        # skip first row as it does not have value
        if index <= 0:
            index = index + 1
            continue
        index = index + 1
        # Remove HTML tag and save to list
        expiry_list.append(BeautifulSoup(str(each_row), 'html.parser').get_text())

    # print(expiry_list)
    return expiry_list, underlying_value # return list

def get_strike_price_from_option_chain(symbol, expdate):

    Base_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbol=" + symbol + "&date=" + expdate
    #lot_url = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuoteFO.jsp?underlying=" + symbol + "&instrument=FUTSTK&expiry=" + expdate+"&type=-&strike=-"
    page = requests.get(Base_url)
    #lot_page = requests.get(lot_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    table_cls_2 = soup.find(id="octable")
    req_row = table_cls_2.find_all('tr')

    strike_price_list = []
    call_volume_list = []
    put_volume_list = []
    call_ltp_list = []

    for row_number, tr_nos in enumerate(req_row):

        # This ensures that we use only the rows with values
        if row_number <= 1 or row_number == len(req_row) - 1:
            continue

        td_columns = tr_nos.find_all('td')
        strike_price = float(BeautifulSoup(str(td_columns[11]), 'html.parser').get_text())
        call_volume_list_html = BeautifulSoup(str(td_columns[3]), 'html.parser').get_text()
        put_volume_list_html = BeautifulSoup(str(td_columns[19]), 'html.parser').get_text()
        call_ltp_list_html =  BeautifulSoup(str(td_columns[5]), 'html.parser').get_text()
        call_ltp_list_html = str.strip(call_ltp_list_html).replace(",", "")
        
        num_format = re.compile("^[\-]?[0-9][0-9]*\.?[0-9]+$")
        
        if call_volume_list_html == "-":
            call_volume = 0
        else:
            call_volume = int(str.strip(call_volume_list_html).replace(",",""))
            
        if put_volume_list_html == "-":
            
            put_volume = 0
        else:
            put_volume = int(str.strip(put_volume_list_html).replace(",",""))
        
        if re.match(num_format, call_ltp_list_html):
            
            call_ltp = float(call_ltp_list_html)
        else:
            call_ltp = 0
            
            
        strike_price_list.append(strike_price)
        call_volume_list.append(call_volume)
        put_volume_list.append(put_volume)
        call_ltp_list.append(call_ltp)
        
    #soup = BeautifulSoup(lot_page.content, 'html.parser')
    # print (strike_price_list)
    return strike_price_list, call_volume_list, put_volume_list, call_ltp_list

options_dict = {}
empty_returns = []
for stock in tqdm(stocks) :
    try:
        
        exp_dates, value = get_expiry_from_option_chain(stock)
        
        strike_prices, call_volume_list, put_volume_list, call_ltp_list = \
                np.asarray(get_strike_price_from_option_chain(stock, exp_dates[0]))
        
        price_index = np.where(strike_prices > value)[0].tolist()
    
    except(ValueError, RuntimeError, TypeError, NameError):
        empty_returns.append(stock)
        continue
        
    if not price_index:
        empty_returns.append(stock)
        continue
        
    strike_price = float(strike_prices[price_index[0]])
    call_ltp_price = float(call_ltp_list[price_index[0]])
    expiry_date = datetime.datetime.strptime(exp_dates[0], '%d%b%Y')
    '''
    stock_opt = get_history(symbol= stock,
                        start=start_date,
                        end= end_date,
                        option_type="CE",
                        strike_price= strike_price,
                        expiry_date= expiry_date)
    '''
    call_volume = sum(x for x in call_volume_list)
    put_volume = sum(x for x in put_volume_list)
    
    if 'Stock' in options_dict:        
        options_dict['Underlying_value'].append(value)
        options_dict['Strike_price'].append(strike_price)
        options_dict['call_LTP'].append(float(call_ltp_price))
        options_dict['Stock'].append(stock)
        options_dict['call_volume'].append(call_volume)
        options_dict['put_volume'].append(put_volume)
        
    else:
        options_dict['Stock'] = [stock]
        options_dict['Underlying_value'] = [value]
        options_dict['Strike_price'] = [strike_price]
        options_dict['call_LTP'] = [float(call_ltp_price)]
        options_dict['call_volume'] = [call_volume]
        options_dict['put_volume'] = [put_volume]

output = pd.DataFrame(options_dict)
output['Stock'] = [x.replace('%26', '&') for x in output['Stock']]
output2 = pd.merge(output, lot_size, how = 'left', left_on = ['Stock'], right_on = ['Symbol'])

output2.rename(columns = {'DerivativesonIndividualSecurities' : 'Stock_Name',
                         'Underlying_value': 'Stock_Price'}, inplace = True)
output2.drop(['Symbol'], axis = 1, inplace = True)
output2['call_LTP*Lot'] = output2['call_LTP']*output2[output2.columns[7]]
output2['Price*Lot'] = output2['Stock_Price']*output2[output2.columns[7]]
print(output2.shape)
print(empty_returns)
output2.to_csv(exp_dates[0]+'list.csv', index = False)
```


==================================================


## [3/3] Repository: NseOptionsChainScrapper (`VAULT_IN-QUANT-086_abbazs__NseOptionsChainScrapper`)
- **Full Name**: `IN-QUANT-086_abbazs__NseOptionsChainScrapper`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# NseOptionsChainScrapper
How to get options chain data from nse.com?

### Core Implementation Code & Architecture
#### File: `oc_scr.py`
```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from string import Template

start_url = Template('https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?segmentLink=17&instrument=OPTIDX&symbol=$SYMBOL')

def get_expirys(url):
    try:
        pg = requests.get(url)
        bsf = BeautifulSoup(pg.content, 'html5lib')
        exps = bsf.find('select', attrs={'name':'date'}).findAll('option')
        expirys = []
        for e in exps[1:]:
            expirys.append(e.contents[0].strip())
        return expirys
    except Exception as e:
        print(e)

def get_chain(url, date, symbol):
    try:
        url = f'{url}&date={date}'
        pg = requests.get(url)
        bsf = BeautifulSoup(pg.content, 'html5lib')
        table = bsf.find("table", attrs={'id':'octable'})
        table.find('thead')('tr')[0].extract()
        df = pd.read_html(table.prettify())
        df = df[0]
        df = df.replace('-', 0)
        name = f'{symbol}_{date}_{datetime.now():%Y-%m-%d_%H-%M-%S}.xlsx'
        df.to_excel(name)
        print(f'Saved {name} ...')
    except Exception as e:
        print(e)

def get_options_chain(symbol):
    url = start_url.substitute(SYMBOL=symbol)
    exps = get_expirys(url)
    for d in exps:
        get_chain(url, d, symbol)

def get_nifty():
    get_options_chain('NIFTY')

def get_bank_nifty():
    get_options_chain('BANKNIFTY')

if __name__ == '__main__':
    get_bank_nifty()
    get_nifty()
```


==================================================
