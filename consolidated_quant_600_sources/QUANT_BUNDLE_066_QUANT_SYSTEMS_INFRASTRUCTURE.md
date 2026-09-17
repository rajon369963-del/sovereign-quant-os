# ⚡ [QUANT-SOURCE-066] Consolidated Quant & Algo Trading Repositories
**Category**: `QUANT_SYSTEMS_INFRASTRUCTURE` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_066_QUANT_SYSTEMS_INFRASTRUCTURE.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: Python-Stock-News-Scraper (`VAULT_IN-QUANT-072_meticulousCraftman__Python-Stock-News-Scraper`)
- **Full Name**: `IN-QUANT-072_meticulousCraftman__Python-Stock-News-Scraper`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Python-News-Scraper
A program that scrapes for announcements from [moneycontrol.com](www.moneycontrol.com) so that traders can take informed decision.
Here is how to get started,
 

    import moneycontrol as mc
    
    # First parameter is the ticker symbol
    stock = mc.MoneyControl("ONGC")

The "stock" object has 3 main methods at present that can be used to extract announcements from Money Control.

### fetch_a(page_no=1)
This method is used to fetch announcements from the given page number. By default, page_no is 1. It returns a list of dictionary with all the values in it.

	# Fetching the announcements on page number 3 ofthe website
    stock.fetch_a(3)
    
	# Here is the output after running this method. 
	[
	   {
	      'content':'Oil & Natural Gas Corporation Limited has informed the Exchange regarding Change in Director(s) of the company.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=10266461',
	      'date':'4th-Jan-2018 14:11',
	      'title':' Oil & Natural Gas Corporation Limited ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oil-natural-gas-corporation-limited-10266461.html'
	   },
	   {
	      'content':'Pursuant to Regulation 30 of Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015, we hereby inform that Shri T K Sengupta, Director (Offshore), has ceased to be Director of the Company upon his attaining superannuation on 31.12.2017.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=10266101',
	      'date':'4th-Jan-2018 13:21',
	      'title':'Oil and Natural Gas Corporation - Change in Directorate ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-changedirectorate-10266101.html'
	   },
	   {
	      'content':'The Exchange had sought clarification from the Company with respect to news item captioned "Venezuela\'\'s PDVSA misses debt payments, used Russian bank to pay ONGC". The response from the Company is enclosed.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9926541',
	      'date':'15th-Nov-2017 16:56',
	      'title':' Oil & Natural Gas Corporation Limited ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oil-natural-gas-corporation-limited-9926541.html'
	   },
	   {
	      'content':'Reply to Clarification on media report.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9925541',
	      'date':'15th-Nov-2017 16:24',
	      'title':'Oil and Natural Gas Corporation - Updates ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-updates-9925541.html'
	   },
	   {
	      'content':'The Exchange has sought clarification from Oil & Natural Gas Corporation Ltd with respect to news article appearing on moneycontrol.com on November 13, 2017 titled "Venezuela likely to go bankrupt in a day?."The reply is awaited.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9860941',
	      'date':'13th-Nov-2017 14:23',
	      'title':'Oil and Natural Gas Corporation - Clarification sought from Oil & Natural Gas Corporation Ltd ',
	      'pdf_link':None
	   },
	   {
	      'content':'Oil & Natural Gas Corporation Limited has informed the Exchange regarding Change in Director(s) of the company.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9719361',
	      'date':'2nd-Nov-2017 12:20',
	      'title':' Oil & Natural Gas Corporation Limited ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oil-natural-gas-corporation-limited-9719361.html'
	   },
	   {
	      'content':'Shri A K Srinivasan, Director Finance, has ceased to be Director of the Company upon his attaining superannuation on 31.10.2017',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9717921',
	      'date':'2nd-Nov-2017 11:15',
	      'title':'Oil and Natural Gas Corporation - Change in Directorate ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-changedirectorate-9717921.html'
	   },
	   {
	      'content':"Un-audited Financial Results for the second Quarter and Half Year ended 30th September, 2017- Auditors''Limited Review Report",
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9660001',
	      'date':'28th-Oct-2017 16:58',
	      'title':'Oil and Natural Gas Corporation - Updates ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-updates-9660001.html'
	   },
	   {
	      'content':"ONGC declares results for Q2 FY''18; records impressive production performance",
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9659761',
	      'date':'28th-Oct-2017 16:37',
	      'title':'Oil and Natural Gas Corporation - Press Release / Media Release ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-press-release-media-release-9659761.html'
	   },
	   {
	      'content':'Pursuant to Regulation 30 of Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015, it is hereby inform that Govt. of India has nominated Dr. Sambit Patra, as an Independent Director on the Board of the Company.The Board of Directors of the Company have also approved induction of Dr. Sambit Patra, as an Additional Director with effect from 28th October, 2017.',
	      'link':'http://www.moneycontrol.com/stocks/stock_market/corp_notices.php?autono=9658841',
	      'date':'28th-Oct-2017 15:56',
	      'title':'Oil and Natural Gas Corporation - Change in Directorate ',
	      'pdf_link':'http://www.moneycontrol.com/stocks/reports/oilnatural-gas-corporation-changedirectorate-9658841.html'
	   }
	]

Each announcement is described using 5 keys, namely:

 - **content** - The small description of the announcement present on the website.
 - **link** - The exact link of the announcement page from where the data is scraped.
 - **date** - The date and time of the announcement
 - **title** - The title of the announcement
 - **pdf_link** - The PDF link of the announcement if present, otherwise, None

### Core Implementation Code & Architecture
#### File: `bse.py`
```python
import requests
import bs4
import pytz

# For this to work I need to convert the ticker symbol to security code
SEARCH_URL = "http://www.bseindia.com/corporates/ann.aspx?curpg=1&annflag=1&dt=&dur=D&dtto=&cat=&scrip=%s&anntype=C"
PREFIX_URL = "http://www.bseindia.com"


class BSE(object):

    def __init__(self, security_code):
        
        # Declaring all the instance variable for the class
        self.security_code = security_code
        self.a = []     # Stores the announcements listed on the given page
        self.more_anno_link = ""    # Link of the announcement page for the company
        self.more_news_link = ""    # Link of news page for the company
        self.template_next_a_page = ""     # For storing the link of the next page of the announcement
        self.a_page_links = []    # Stores the list of links all the announcement pages.
        self.link = ""      # Link to the front page of the company we are looking for on moneycontrol
        self.present_a_page = 0

        self.fetch_ticker()
        # self.__fetch_a_next_page_link()


    def fetch_ticker(self):
        try:
            self.link = SEARCH_URL % self.security_code
            r = requests.get(self.link)
            if r.status_code==200:
                print("Fetched page for ticker : "+self.security_code)
                # Creating a bs4 object to store the contents of the requested page
                self.soup = bs4.BeautifulSoup(r.content, 'html.parser')
                print("Fetched page successfully")

            elif r.status_code==404:
                print("Page not found")
            else:
                print("A different status code received : "+str(r.status_code))

        except requests.ConnectionError as ce:
            print("There is a network problem (DNS Failure, refused connectionn etc.). Error : "+str(ce))
            raise Exception
        
        except requests.Timeout as te:
            print("Request timed out. Error : "+str(te))
            raise Exception
        
        except requests.TooManyRedirects as tmre:
            print("The request exceeded the maximum no. of redirections. Error : "+str(tmre))
            raise Exception
        
        except requests. requests.exceptions.RequestException as oe:
            print("Any type of request related error : "+str(oe))
            raise Exception


    def __fetch_a_next_page_link(self):

        # Fetches the template URL for fetching different announcement pages
        r = requests.get(self.more_anno_link)
        announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        # Checking whether the link for the next page is available or not
        if len(announcement_soup.find("div", attrs={"class":"gray2_11"}).find_all("a")) > 0:
            a = announcement_soup.find("div", attrs={"class":"gray2_11"}).find_all("a")[0]["href"]
            self.template_next_a_page = PREFIX_URL + a[0:-1]    # Removing the page no. of the given link so that it becomes general link


    def fetch_a(self, page_no=1):

        if self.has_a(self.template_next_a_page + str(page_no)):

            # Clear all the previous data in "a" instance variable
            self.a = []

            r = requests.get(self.template_next_a_page + str(page_no))

            self.present_a_page = page_no

            announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
            raw_links = announcement_soup.find_all("a", attrs={"class":"bl_15"})
            
            # List of links of all the announcements on the given page
            list_of_links = []
            for x in raw_links:
                link = PREFIX_URL + x['href']
                list_of_links.append(link)
                a = requests.get(PREFIX_URL + x['href'])
                anno_page = bs4.BeautifulSoup(a.content, "html.parser")

                pdf_link = ""
                title = ""
                content = ""

                date = next(anno_page.find("p", attrs={"class":"gL_10"}).children)
                date = self.format_date(date)

                
                # Checking whether the title of the announcement is available or not
                if anno_page.find("span", attrs={"class":"bl_15"}):
                    title = anno_page.find("span", attrs={"class":"bl_15"}).text

                # Checking whether content is available or not
                if anno_page.find("p", attrs={"class":"PT10 b_12"}):
                    content = anno_page.find("p", attrs={"class":"PT10 b_12"}).text
                 
                # Checking whether the PDF link is availableor not
                if anno_page.find("p", attrs={"class":"PT5"}).find("a"):
                    pdf_link = PREFIX_URL + anno_page.find("p", attrs={"class":"PT5"}).find("a")["href"]


                anno = {"link":link, "pdf_link":pdf_link, "content":content, "title":title, "date":date}
                self.a.append(anno)

        else:
            self.a = []
        
        return self.a


    def has_a(self, link):
        result = False
        r = requests.get(link)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        a = soup.find_all("p", attrs={"class":"gL_10"})     # Finding the list of the all the dates available on the page
        if len(a)>0:
            result = True

        return result


    def fetch_all_a_pages(self):
        i = 2
        # fetch the announcement on first page only when this instance variable is empty
        if self.template_next_a_page == "":
            self.fetch_a()
        link = self.template_next_a_page+str(i)
        while self.has_a(link):
            link = self.template_next_a_page+str(i)
            print("Page added : "+str(i))
            self.a_page_links.append(link)
            i += 1  # Keep incrementing the value of i to check the next page
        return self.a_page_links

    def format_date(self,datetime):
        datetime = datetime.split(" ")
        
        date = datetime[0].split("-")
        time = datetime[1]

        date[0] = date[0][:-2]
        month = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12'
        }
        date[1] = month[date[1]]
        date.reverse()
        date = '-'.join(date)
        final = date+" "+time
        return final
```

#### File: `moneycontrol.py`
```python
import requests
import bs4
import pytz

SEARCH_URL = "http://www.moneycontrol.com/stocks/cptmarket/compsearchnew.php?search_data=&cid=&mbsearch_str=&topsearch_type=1&search_str="
PREFIX_URL = "http://www.moneycontrol.com"


class MoneyControl(object):

    def __init__(self, ticker):
        
        # Declaring all the instance variable for the class
        self.ticker = ticker
        self.a = []     # Stores the announcements listed on the given page
        self.more_anno_link = ""    # Link of the announcement page for the company
        self.more_news_link = ""    # Link of news page for the company
        self.template_next_a_page = ""     # For storing the link of the next page of the announcement
        self.a_page_links = []    # Stores the list of links all the announcement pages.
        self.link = ""      # Link to the front page of the company we are looking for on moneycontrol
        self.present_a_page = 0

        self.fetch_ticker()
        self.__fetch_a_next_page_link()


    def fetch_ticker(self):
        try:
            self.link = SEARCH_URL+self.ticker
            r = requests.get(self.link)
            if r.status_code==200:
                print("Fetched page for ticker : "+self.ticker)
                # Creating a bs4 object to store the contents of the requested page
                self.soup = bs4.BeautifulSoup(r.content, 'html.parser')
                self.more_anno_link = PREFIX_URL + str(self.soup.find("div", attrs={"class":"PT5 gL_11", "align":"right"}).find("a")["href"] ) # class name extracted after looking at the document
                self.more_news_link = PREFIX_URL + str(self.soup.find("div", attrs={"class":"PT5 gL_11 FR"}).find("a")["href"])
            elif r.status_code==404:
                print("Page not found")
            else:
                print("A different status code received : "+str(r.status_code))

        except requests.ConnectionError as ce:
            print("There is a network problem (DNS Failure, refused connectionn etc.). Error : "+str(ce))
            raise Exception
        
        except requests.Timeout as te:
            print("Request timed out. Error : "+str(te))
            raise Exception
        
        except requests.TooManyRedirects as tmre:
            print("The request exceeded the maximum no. of redirections. Error : "+str(tmre))
            raise Exception
        
        except requests. requests.exceptions.RequestException as oe:
            print("Any type of request related error : "+str(oe))
            raise Exception


    def __fetch_a_next_page_link(self):

        # Fetches the template URL for fetching different announcement pages
        r = requests.get(self.more_anno_link)
        announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        # Checking whether the link for the next page is available or not
        if len(announcement_soup.find("div", attrs={"class":"gray2_11"}).find_all("a")) > 0:
            a = announcement_soup.find("div", attrs={"class":"gray2_11"}).find_all("a")[0]["href"]
            self.template_next_a_page = PREFIX_URL + a[0:-1]    # Removing the page no. of the given link so that it becomes general link


    def fetch_a(self, page_no=1):

        if self.has_a(self.template_next_a_page + str(page_no)):

            # Clear all the previous data in "a" instance variable
            self.a = []

            r = requests.get(self.template_next_a_page + str(page_no))

            self.present_a_page = page_no

            announcement_soup = bs4.BeautifulSoup(r.content, 'html.parser')
            raw_links = announcement_soup.find_all("a", attrs={"class":"bl_15"})
            
            # List of links of all the announcements on the given page
            list_of_links = []
            for x in raw_links:
                link = PREFIX_URL + x['href']
                list_of_links.append(link)
                a = requests.get(PREFIX_URL + x['href'])
                anno_page = bs4.BeautifulSoup(a.content, "html.parser")

                pdf_link = ""
                title = ""
                content = ""

                date = next(anno_page.find("p", attrs={"class":"gL_10"}).children)
                date = self.format_date(date)

                
                # Checking whether the title of the announcement is available or not
                if anno_page.find("span", attrs={"class":"bl_15"}):
                    title = anno_page.find("span", attrs={"class":"bl_15"}).text

                # Checking whether content is available or not
                if anno_page.find("p", attrs={"class":"PT10 b_12"}):
                    content = anno_page.find("p", attrs={"class":"PT10 b_12"}).text
                 
                # Checking whether the PDF link is availableor not
                if anno_page.find("p", attrs={"class":"PT5"}).find("a"):
                    pdf_link = PREFIX_URL + anno_page.find("p", attrs={"class":"PT5"}).find("a")["href"]


                anno = {"link":link, "pdf_link":pdf_link, "content":content, "title":title, "date":date}
                self.a.append(anno)

        else:
            self.a = []
        
        return self.a


    def has_a(self, link):
        result = False
        r = requests.get(link)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        a = soup.find_all("p", attrs={"class":"gL_10"})     # Finding the list of the all the dates available on the page
        if len(a)>0:
            result = True

        return result


    def fetch_all_a_pages(self):
        i = 2
        # fetch the announcement on first page only when this instance variable is empty
        if self.template_next_a_page == "":
            self.fetch_a()
        link = self.template_next_a_page+str(i)
        while self.has_a(link):
            link = self.template_next_a_page+str(i)
            print("Page added : "+str(i))
            self.a_page_links.append(link)
            i += 1  # Keep incrementing the value of i to check the next page
        return self.a_page_links

    def format_date(self,datetime):
        datetime = datetime.split(" ")
        
        date = datetime[0].split("-")
        time = datetime[1]

        date[0] = date[0][:-2]
        month = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12'
        }
        date[1] = month[date[1]]
        date.reverse()
        date = '-'.join(date)
        final = date+" "+time
        return final
```


==================================================


## [2/3] Repository: kinetick (`VAULT_IN-QUANT-073_imvinaypatil__kinetick`)
- **Full Name**: `IN-QUANT-073_imvinaypatil__kinetick`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
`>_• <./resources/kinetick512.png>`_ Kinetick Trade Bot
=======================================================
.. image:: .resources/kinetick-beta128.png
    :height: 128
    :width: 128
    :alt: **>_•**

\

.. image:: https://img.shields.io/github/checks-status/imvinaypatil/kinetick/main
    :target: https://github.com/imvinaypatil/kinetick
    :alt: Branch state

.. image:: https://img.shields.io/badge/python-3.4+-blue.svg?style=flat
    :target: https://pypi.python.org/pypi/kinetick
    :alt: Python version

.. image:: https://img.shields.io/pypi/v/kinetick.svg?maxAge=60
    :target: https://pypi.python.org/pypi/kinetick
    :alt: PyPi version

.. image:: https://img.shields.io/discord/881151290741256212?logo=discord
    :target: https://discord.gg/xqD6RmqvBV
    :alt: Chat on Discord

\

    Kinetick is a framework for creating and running trading strategies without worrying
    about integration with broker and data streams (currently integrates with zerodha [*]_).
    Kinetick is aimed to make systematic trading available for everyone.

Leave the heavy lifting to kinetick and you focus on building strategies.

WARNING

This project is still in its early stages, please be cautious when dealing with real money.

`Changelog » <./CHANGELOG.rst>`_

📱 Screenshots
==============

.. |screen1| image:: .resources/screenshot1.jpeg
   :scale: 100%
   :align: middle
.. |screen2| image:: .resources/screenshot2.jpeg
   :scale: 100%
   :align: top
.. |screen3| image:: .resources/screenshot3.jpeg
   :scale: 100%
   :align: middle

+-----------+-----------+-----------+
| |screen1| | |screen2| | |screen3| |
+-----------+-----------+-----------+

Features
========

- A continuously-running Blotter that lets you capture market data even when your algos aren't running.
- Tick, Bar and Trade data is stored in MongoDB for later analysis and backtesting.
- Using pub/sub architecture using `ØMQ <http://zeromq.org>`_ (ZeroMQ) for communicating between the Algo and the Blotter allows for a single Blotter/multiple Algos running on the same machine.
- **Support for Order Book, Quote, Time, Tick or Volume based strategy resolutions**.
- Includes many common indicators that you can seamlessly use in your algorithm.
- **Market data events use asynchronous, non-blocking architecture**.
- Realtime alerts and order confirmation delivered to your mobile via Telegram bot (requires a `Telegram bot <https://t.me/botfather>`_ token).
- Full integration with `TA-Lib <https://pypi.org/project/TA-Lib/>`_ via dedicated module (`see example <strategies/macd_super_strategy.py>`_).
- Ability to import any Python library (such as `scikit-learn <http://scikit-learn.org>`_ or `TensorFlow <https://www.tensorflow.org>`_) to use them in your algorithms.
- Live charts powered by TradingView
- **RiskAssessor** to manage and limit the risk even if strategy goes unexpected
- Power packed batteries included
- Deploy wherever `Docker <https://www.docker.com>`_ lives

-----

Installation
============

Install using ``pip``:

.. code:: bash

    $ pip install kinetick

Telegram bot must be configured in order to take TOTP input for zerodha login

    use ``/zlogin <totp>`` command to login to zerodha

Quickstart
==========

There are 5 main components in Kinetick:

1. ``Bot`` - sends alert and signals with actions to perform.
2. ``Blotter`` - handles market data retrieval and processing.
3. ``Broker`` - sends and process orders/positions (abstracted layer).
4. ``Algo`` - (sub-class of ``Broker``) communicates with the ``Blotter`` to pass market data to your strategies, and process/positions orders via ``Broker``.
5. Lastly, **Your Strategies**, which are sub-classes of ``Algo``, handle the trading logic/rules. This is where you'll write most of your code.


1. Get Market Data
------------------

To get started, you need to first create a Blotter script:

.. code:: python

    # blotter.py
    from kinetick.blotter import Blotter

    class MainBlotter(Blotter):
        pass # we just need the name

    if __name__ == "__main__":
        blotter = MainBlotter()
        blotter.run()

Then run the Blotter from the command line:

.. code:: bash

    $ python -m blotter

If your strategy needs order book / market depth data, add the ``--orderbook`` flag to the command:

.. code:: bash

    $ python -m blotter --orderbook


2. Write your Algorithm
-----------------------

While the Blotter running in the background, write and execute your algorithm:

.. code:: python

    # strategy.py
    from kinetick.algo import Algo

    class CrossOver(Algo):

        def on_start(self):
            pass

        def on_fill(self, instrument, order):
            pass

        def on_quote(self, instrument):
            pass

        def on_orderbook(self, instrument):
            pass

        def on_tick(self, instrument):
            pass

        def on_bar(self, instrument):
            # get instrument history
            bars = instrument.get_bars(window=100)

            # or get all instruments history
            # bars = self.bars[-20:]

            # skip first 20 days to get full windows
            if len(bars) < 20:
                return

            # compute averages using internal rolling_mean
            bars['short_ma'] = bars['close'].rolling(window=10).mean()
            bars['long_ma']  = bars['close'].rolling(window=20).mean()

            # get current position data
            positions = instrument.get_positions()

            # trading logic - entry signal
            if bars['short_ma'].crossed_above(bars['long_ma'])[-1]:
                if not instrument.pending_orders and positions["position"] == 0:

                    """ buy one contract.
                     WARNING: buy or order instrument methods will bypass bot and risk assessor.
                     Instead, It is advised to use create_position, open_position and close_position instrument methods
                     to route the order via bot and risk assessor. """
                    instrument.buy(1)

                    # record values for later analysis
                    self.record(ma_cross=1)

            # trading logic - exit signal
            elif bars['short_ma'].crossed_below(bars['long_ma'])[-1]:
                if positions["position"] != 0:

                    # exit / flatten position
                    instrument.exit()

                    # record values for later analysis
                    self.record(ma_cross=-1)


    if __name__ == "__main__":
        strategy = CrossOver(
            instruments = ['ACC', 'SBIN'], # scrip symbols
            resolution  = "1T", # Pandas resolution (use "K" for tick bars)
            tick_window = 20, # no. of ticks to keep
            bar_window  = 5, # no. of bars to keep
            preload     = "1D", # preload 1 day history when starting
            timezone    = "Asia/Calcutta" # convert all ticks/bars to this timezone
        )
        strategy.run()


To run your algo in a **live** environment, from the command line, type:

.. code:: bash

    $ python -m strategy --logpath ~/orders


The resulting trades be saved in ``~/orders/STRATEGY_YYYYMMDD.csv`` for later analysis.


3. Login to bot
----------------------

While the Strategy running in the background:

  Assuming you have added the telegram bot to your chat

- ``/login <password>`` - Password can be found in the strategy console. This step is required if you have not provided your telegram chat id as an env var
- ``/zlogin <totp>`` Command to login to zerodha using totp


commands
--------

- ``/report`` - get overview about trades
- ``/help`` - get help
- ``/resetrms`` - resets RiskAssessor parameters to its initial values.



Configuration
-------------
Can be specified either as env variable or cmdline arg

.. list-table::

   * - Parameter
     - Required?
     - Example
     - Default
     - Description
   * - ``symbols``
     -
     -  symbols=./symbols.csv
     -
     -
   * - ``LOGLEVEL``
     -
     - LOGLEVEL=DEBUG
     - INFO
     -
   * - ``zerodha_user``
     - yes - if live trading
     - zerodha_user=ABCD
     -
     -
   * - ``zerodha_password``
     - yes - if live trading
     - zerodha_password=abcd
     -
     -
   * - ``zerodha_pin``
     - yes - if live trading
     - zerodha_pin=1234
     -
     -
   * - ``BOT_TOKEN``
     - optional
     - BOT_TOKEN=12323:asdcldf..
     -
     - IF not provided then orders will bypass
   * - ``initial_capital``
     - yes
     - initial_capital=10000
     - 1000
     - Max capital deployed
   * - ``initial_margin``
     - yes
     - initial_margin=1000
     - 100
     - Not to be mistaken with broker margin. This is the max amount you can afford to loose
   * - ``risk2reward``
     - yes
     - risk2reward=1.2
     - 1
     - Set risk2reward for your strategy. This will be used in determining qty to trade
   * - ``risk_per_trade``
     - yes
     - risk_per_trade=200
     - 100
     - Risk you can afford with each trade
   * - ``max_trades``
     - yes
     - max_trades=2
     - 1
     - Max allowed concurrent positions
   * - ``dbport``
     -
     - dbport=27017
     - 27017
     -
   * - ``dbhost``
     -
     - dbhost=localhost
     - localhost
     -
   * - ``dbuser``
     -
     - dbuser=user
     -
     -
   * - ``dbpassword``
     -
     - dbpassword=pass
     -
     -
   * - ``dbname``
     -
     - dbname=kinetick
     - kinetick
     -
   * - ``orderbook``
     -
     - orderbook=true
     - false
     - Enable orderbook stream
   * - ``resolution``
     -
     - resolution=1m
     - 1
     - Min Bar interval
   * - ``preload_positions``
     - No
     - preload_positions=30D
     - -
     - Loads only overnight positions.Available options: 1D - 1 Day, 1W - 1 Week, 1H - 1 Hour
   * - ``CHAT_ID``
     - No
     - CHAT_ID=12345
     - -
     - default chat user id to which trade notifications are sent requiring no login

Docker Instructions
===================

1. Build blotter

    ``$ docker build -t kinetick:blotter -f blotter.Dockerfile .``

2. Build strategy

    ``$ docker build -t kinetick:strategy -f strategy.Dockerfile .``

3. Run with docker-compose

    ``$ docker compose up``


Backtesting
===========

.. code:: bash

    $ python -m strategy --start "2021-03-06 00:15:00" --end "2021-03-10 00:15:00" --backtest --backfill


.. note::

    To get started checkout the patented BuyLowSellHigh strategy in ``strategies/`` directory.


🙏 Credits
==========

Thanks to @ran aroussi for all his initial work with Qtpylib.
Most of work here is derived from his library

Disclaimer
==========

Kinetick is licensed under the **Apache License, Version 2.0**. A copy of which is included in LICENSE.txt.

All trademarks belong to the respective company and owners. Kinetick is not affiliated to any entity.

.. [*] Kinetick is not affiliated to zerodha.

### Core Implementation Code & Architecture
#### File: `kinetick/tests/__init__.py`
```python

```

#### File: `kinetick/lib/brokers/zerodha/__init__.py`
```python

```

#### File: `kinetick/lib/brokers/webull/__init__.py`
```python

```

#### File: `kinetick/factory/__init__.py`
```python

```

#### File: `kinetick/utils/__init__.py`
```python
from . import *
```

#### File: `kinetick/lib/__init__.py`
```python
from .indicators import *
```


==================================================


## [3/3] Repository: stock-news (`VAULT_IN-QUANT-082_BennyThadikaran__stock-news`)
- **Full Name**: `IN-QUANT-082_BennyThadikaran__stock-news`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# BSE NEWS.py

A Python Terminal script for displaying Corporate filings on BSE exchange.

- Corporate Announcements
- Result Calendar
- Corporate Actions like Dividend, Bonus, Splits etc.

Use it to track company updates, quarterly results, dividend, bonus etc on your portfolio stocks.

![news.py screenshot](https://res.cloudinary.com/doyu4uovr/image/upload/s--m5SBWD_8--/c_scale,f_auto,w_800/v1698247749/stock-news/news-bse_fisxgv.png)

Python version: >= 3.8

If you ❤️ my work so far, please 🌟 this repo.

## Installation

1. Clone this repo

2. Install dependencies: `pip install bse`

### Initial Setup

1. **Create a text file** of all stock symbols. One on each line. This could be your stocks portfolio or a watchlist.

```
hdfcbank
tcs
infy
```

2. **Run the script** with `-f` or `--file` option passing the file path.

`py news.py -f watch.txt`

This will generate a `watchlist.json` file and display all announcements & actions for the day.

## Usage

After the initial setup, run the script with no options.

`py news.py`

By default, the current day announcements are printed.

To **print the previous day**, use `-p` or `--prev` option.

```bash
py news.py -p
# print yesterdays announcements
```

Add an optional integer number like `py news.py -p 3` to go 3 days back.

To **jump to a specific date**, use `-d` or `--date` option passing a ISO date string (YYYY-MM-DD).

`py news.py -d 2023-10-18`

All output is displayed in terminal colors. To display no color and plain text, use `-t` or `--txt` option.

`py news.py -t`

To **display help**, use `-h` or `--help`

`py news.py -h`

To output in other formats, use `--fmt` with `txt` for plain or `md` for markdown format

To output to a file, use `-o` specifing the file path

## Notes

The announcements are filtered for certain keywords in the subject.

- trading window,
- reg. 74 (5)
- book closure
- investor meet
- loss of share
- loss of certificate
- investor conference
- shares in physical

IMHO these are unimportant and thus filtered out. If you wish to add or remove from this list, see `def isBlackListed` in `src/news.py`. The keywords in question are listed in `filtered_words`

### Core Implementation Code & Architecture
#### File: `src/news.py`
```python
from typing import Union, Dict, List
from bse import BSE
from datetime import datetime, timedelta
from os import system
from pathlib import Path
from argparse import ArgumentParser
import sys
import json
import re
import logging


class BaseFormatter:
    """Base Formatter"""

    def mainHeading(self, string: str) -> str:
        return f"{string}\n"

    def subHeading(self, string: str) -> str:
        return f"{string}\n"

    def string(
        self, key: str, val: str, date: Union[datetime, str, None] = None
    ) -> str:
        raise NotImplementedError

    @staticmethod
    def hr() -> str:
        return f'\n{"":->70}\n'


class ColorFormatter(BaseFormatter):
    """Format strings with Terminal color output"""

    HEADER = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

    def mainHeading(self, string: str) -> str:
        return f"{self.HEADER}{self.BOLD}{string}{self.ENDC}\n"

    def subHeading(self, string: str) -> str:
        return f"{self.BOLD}{string}{self.ENDC}\n"

    def heading(self, sym: str, category: str) -> str:
        return f"{self.CYAN}{self.BOLD}{sym.upper()} - {category}{self.ENDC}\n"

    def subject(self, subject: str, headline: str) -> str:
        return f"{self.GREEN}{subject}{self.ENDC}\n{headline}{self.ENDC}"

    def url(self, filename: str) -> str:
        baseurl = "https://www.bseindia.com/xml-data/corpfiling/AttachLive"
        return f"\n{self.CYAN}{baseurl}/{filename}{self.ENDC}"

    def string(
        self, key: str, val: str, date: Union[datetime, str, None] = None
    ) -> str:
        string = f"{self.HEADER}{self.BOLD}{key}:".ljust(25)
        string += f"{self.GREEN}{val}{self.ENDC}".ljust(48)

        if date:
            string += f"{date:%d %b %Y}" if isinstance(date, datetime) else date

        return string + "\n"


class TextFormatter(BaseFormatter):
    """Format strings in plain text"""

    def heading(self, sym: str, category: str) -> str:
        return f"{sym.upper()} - {category}\n"

    def subject(self, subject: str, headline: str) -> str:
        return f"{subject}\n{headline}"

    def url(self, filename: str) -> str:
        baseurl = "https://www.bseindia.com/xml-data/corpfiling/AttachLive"
        return f"\n{baseurl}/{filename}"

    def string(
        self, key: str, val: str, date: Union[datetime, str, None] = None
    ) -> str:
        string = f"{key}:".ljust(15)
        string += f"{val}".ljust(40)

        if date:
            string += f"{date:%d %b %Y}" if isinstance(date, datetime) else date

        return string + "\n"


class MarkdownFormatter(BaseFormatter):
    """Format strings in Markdown text"""

    div_table_start = True
    other_table_start = True
    result_table_start = True

    def mainHeading(self, string: str) -> str:
        return f"# {string}\n"

    def subHeading(self, string: str) -> str:
        return f"## {string}\n"

    def heading(self, sym: str, category: str) -> str:
        return f"## {sym.upper()} - {category}\n"

    def subject(self, subject: str, headline: str) -> str:
        return f"**{subject}**\n{headline}"

    def url(self, filename: str) -> str:
        baseurl = "https://www.bseindia.com/xml-data/corpfiling/AttachLive"
        return f"\n{baseurl}/{filename}"

    def string(
        self, key: str, val: str, date: Union[datetime, str, None] = None
    ) -> str:
        string = ""
        header = "|Company|Description|Ex Date|\n|---|---|---|\n"
        resultHeader = "|Company|Result Date|\n|---|---|\n"

        if date is None and self.result_table_start:
            string += resultHeader
            self.result_table_start = False

        if "Dividend" in val and self.div_table_start:
            string += header
            self.div_table_start = False

        if ("Bonus" in val or "Split" in val) and self.other_table_start:
            string += header
            self.other_table_start = False

        string += f"|{key}|{val}|"

        if date:
            dt = (
                date.strftime("%d %b %Y")
                if isinstance(date, datetime)
                else date
            )
            string += f"{dt}|"

        return string + "\n"


class FormatterFactory:
    @staticmethod
    def get(name: str):
        if name == "txt":
            return TextFormatter()

        if name == "md":
            return MarkdownFormatter()

        return ColorFormatter()


def isBlackListed(string: str) -> bool:
    """Looks for blacklisted keywords in string and returns True if found"""

    string = string.lower()

    # Picked from announcements subcategory
    filtered_words = (
        "trading window",
        "reg. 74 (5)",  # demat
        "book closure",
        "investor meet",
        "loss of share",
        "loss of certificate",
        "investor conference",
        "shares in physical",
    )

    for key in filtered_words:
        if key in string:
            return True

    return False


def cleanDividendAction(string: str) -> str:
    """Formats dividend string, removing '-' and extra zeroes

    'Interim Dividend - Rs. - 18.0000' => 'Interim Dividend Rs.18.0'
    """

    # 'Interim Dividend - Rs. - 18.0000' -> split on '-' and strip space chars
    # ['Interim Dividend', 'Rs.'], 18.0000
    *str_lst, dividend = tuple(i.strip() for i in string.split("-"))

    try:
        dividend = float(dividend)
    except ValueError:
        # Not a valid number. return string as is
        return string

    return f'{" ".join(str_lst)}{dividend}'


def parseComplaints(string) -> str:
    """Parses shareholder complaints string.
    Looks for integer values between HTML tags"""

    m = re.findall(r">(\d+)<", string)

    if len(m) < 4:
        return string

    return f"Pending: {m[0]}\nReceived: {m[1]}\nDisposed: {m[2]}\nUnresolved: {m[3]}"


# Check if system is windows or linux
if "win" in sys.platform:
    # enable color support in Windows
    system("color")

dt = datetime.now()

parser = ArgumentParser(
    prog="news.py",
    description="A script for displaying Corporate filings on BSE exchange.",
)

group = parser.add_mutually_exclusive_group(required=False)

group.add_argument(
    "-p",
    "--prev",
    type=int,
    nargs="?",
    const=1,
    default=None,
    dest="prev",
    metavar="N",
    help="Get news for previous day or N days back.",
)

group.add_argument(
    "-d",
    "--date",
    type=lambda x: datetime.fromisoformat(x),
    action="store",
    metavar="YYYY-MM-DD",
    help="Get news for specified date",
)

parser.add_argument(
    "--fmt",
    choices=("txt", "md", "html", "color"),
    default="color",
    help="Output format (choose from txt, md, html, color)",
)

parser.add_argument(
    "-f", "--file", type=Path, help="Add watchlist symbols file"
)

parser.add_argument(
    "-o",
    "--out",
    type=Path,
    help="Output to file",
)

args = parser.parse_args()


DIR = Path(__file__).parent
WATCH_FILE = DIR / "watchlist.json"

if args.date:
    if args.date > dt:
        raise ValueError("Date cannot be greater than today")

    dt = args.date

if args.prev:
    dt = dt - timedelta(args.prev)

symList: Union[List[str], None] = None

# set up logging
logger = logging.getLogger(__file__)

if args.out:
    log_handler = logging.FileHandler(args.out, mode="w")
else:
    log_handler = logging.StreamHandler(stream=sys.stdout)

logging.basicConfig(
    handlers=[log_handler],
    format="%(message)s",
    level=logging.INFO,
)


if args.file:
    watchlist: Dict[str, str] = {}

    if not args.file.exists():
        raise FileNotFoundError(f"{args.file} not found. ")

    symList = args.file.read_text().strip().split("\n")
else:
    if not WATCH_FILE.exists():
        raise FileNotFoundError(
            f"{WATCH_FILE} not found. Use -f to generate watchlist.json"
        )

    watchlist = json.loads(WATCH_FILE.read_bytes())

with BSE(DIR) as bse:
    if symList:
        for sym in symList:
            code: str = bse.getScripCode(sym)
            watchlist[code] = sym

        WATCH_FILE.write_text(json.dumps(watchlist, indent=3))
        print("watchlist.json file saved")

    try:
        actions: List[dict] = bse.actions()
        result_calendar: List[dict] = bse.resultCalendar()
    except (TimeoutError, ConnectionError) as e:
        exit(repr(e))

    announcements: List[dict] = []

    for code in watchlist:
        try:
            res: dict = bse.announcements(
                from_date=dt, to_date=dt, scripcode=code
            )
        except (TimeoutError, ConnectionError) as e:
            exit(repr(e))

        announcements.extend(res["Table"])

fmt = FormatterFactory.get(args.fmt)

ann_txt = result_txt = portfolio_acts = other_acts = ""

# PROCESS RESULT CALENDAR
for res in result_calendar:
    if res["scrip_Code"] in watchlist:
        result_txt += fmt.string(res["short_name"], res["meeting_date"])

# PROCESS CORP ANNOUNCEMENTS
for ann in announcements:
    code = str(ann["SCRIP_CD"])
    sym = watchlist[code]
    subject: str = ann["NEWSSUB"]

    if not (code in watchlist and ann["CATEGORYNAME"]):
        continue

    if isBlackListed(subject):
        continue

    if (
        "Regulation" in subject or "Notice" in subject or "Change" in subject
    ) and "-" in subject:
        # Strip company name, scrip code etc. and limit subject to 70 chars
        subject = subject[subject.find("-") + 1 :][:70]

    if "XBRL" in subject:
        subject = subject.replace("- XBRL", "")

    if "investor complaints" in subject.lower():
        headline = parseComplaints(ann["HEADLINE"])
    else:
        headline: str = ann["HEADLINE"].replace("<BR>", "")

    ann_txt += fmt.heading(sym, ann["CATEGORYNAME"])

    ann_txt += fmt.subject(subject.strip(), headline)

    if ann["ATTACHMENTNAME"]:
        ann_txt += fmt.url(ann["ATTACHMENTNAME"])

    ann_txt += fmt.hr()

# PROCESS CORP. ACTIONS
for act in actions:
    purpose_lc: str = act["Purpose"].lower()
    sym: str = act["short_name"]
    code = str(act["scrip_code"])
    ex_date = act["Ex_date"]

    if "dividend" in purpose_lc:
        act["Purpose"] = cleanDividendAction(act["Purpose"])

    if code in watchlist:
        portfolio_acts += fmt.string(sym, act["Purpose"], ex_date)
    elif "bonus" in purpose_lc or "split" in purpose_lc:
        other_acts += fmt.string(sym, act["Purpose"], ex_date)

# PRINT ANNOUNCEMENTS
logger.info(fmt.mainHeading(f"CORP. ANNOUNCEMENTS - {dt:%A %d %b %Y}"))

if ann_txt:
    logger.info(ann_txt)
else:
    logger.info(fmt.subHeading("No announcements to display."))

# PRINT RESULT CALENDAR
if result_txt:
    logger.info(fmt.mainHeading("Result Calendar"))
    logger.info(result_txt)

# PRINT ACTIONS
logger.info(fmt.mainHeading("Corporate Actions"))

if portfolio_acts:
    logger.info(fmt.subHeading("Portfolio"))
    logger.info(portfolio_acts)
else:
    logger.info("\tNo actions on Portfolio\n")

if other_acts:
    logger.info(fmt.subHeading("Other Corp. Actions"))
    logger.info(other_acts)
```


==================================================
