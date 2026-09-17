# ⚡ [QUANT-SOURCE-007] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_007_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: indian-stock-market (`VAULT_IN-QUANT-060_Zero65Tech__indian-stock-market`)
- **Full Name**: `IN-QUANT-060_Zero65Tech__indian-stock-market`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# Indian Stock Market

This npm package provides utilities to work with the Indian stock market, including functions to determine market holidays, expiry dates for futures and options, and market open/close status.

## Installation

```sh
npm install @zero65tech/indian-stock-market
```

## Usage

### Importing the package

```javascript
const ism = require('@zero65tech/indian-stock-market');
```

### Functions

#### `fo(name)`

Returns information about the futures or options contract.

```javascript
const info = ism.fo('NIFTY21OCTFUT');
console.log(info); // { scrip: 'NIFTY', exp: '21OCT', expiry: '2021-10-28', type: 'FUT' }
```

#### `isOpen()`

Checks if the market is currently open.

```javascript
const open = ism.isOpen();
console.log(open); // true or false
```

#### `hasOpened()`

Checks if the market has opened today.

```javascript
const opened = ism.hasOpened();
console.log(opened); // true or false
```

#### `hasClosed()`

Checks if the market has closed today.

```javascript
const closed = ism.hasClosed();
console.log(closed); // true or false
```

#### `isHoliday(date)`

Checks if the given date is a market holiday. If no date is provided, it checks for today.

```javascript
const holiday = ism.isHoliday();
console.log(holiday); // true or false
```

```javascript
const holiday = ism.isHoliday('2021-10-02');
console.log(holiday); // true or false
```

```javascript
const holiday = ism.isHoliday(new Date('2021-10-02'));
console.log(holiday); // true or false
```

### License

This project is licensed under the MIT License.

### Core Implementation Code & Architecture
#### File: `.vscode/extensions.json`
```python
{
  "recommendations": [
    "openai.chatgpt",
    "anthropic.claude-code",
    "github.vscode-pull-request-github",
    "dbaeumer.vscode-eslint",
    "esbenp.prettier-vscode"
  ]
}
```

#### File: `.devcontainer/devcontainer.json`
```python
{
  "image": "mcr.microsoft.com/devcontainers/javascript-node:24",
  "postStartCommand": "npm update",
  "customizations": {
    "vscode": {
      "extensions": [
        "openai.chatgpt",
        "anthropic.claude-code",
        "github.vscode-pull-request-github",
        "dbaeumer.vscode-eslint",
        "esbenp.prettier-vscode"
      ]
    }
  }
}
```

#### File: `src/data/special-days.json`
```python
{
  "2012": { "1": [7], "3": [3], "4": [28], "9": [8], "11": [11] },
  "2013": { "5": [11], "11": [3] },
  "2014": { "3": [22] },
  "2015": { "2": [28] },
  "2016": { "10": [30] },
  "2019": { "10": [27] },
  "2020": { "2": [1], "11": [14] },
  "2023": { "11": [12] },
  "2024": { "1": [20], "3": [2], "5": [18], "11": [1] },
  "2025": { "2": [1], "10": [21] },
  "2026": { "2": [1], "11": [8] }
}
```

#### File: `.vscode/settings.json`
```python
{
  "files.exclude": {
    "node_modules/": true,
    "coverage/": true
  },
  "explorer.fileNesting.enabled": true,
  "explorer.fileNesting.patterns": {
    ".gitignore": ".prettierignore, .npmignore",
    "package.json": "package-lock.json, eslint.config.js, prettier.config.js",
    "README.md": "LICENSE"
  },
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit",
    "source.organizeImports": "explicit"
  },
  "editor.formatOnType": true,
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "diffEditor.ignoreTrimWhitespace": false,
  "git.autofetch": true,
  "git.confirmSync": false
}
```

#### File: `package.json`
```python
{
  "author": "Prashant Gupta @ Zero65 Technologies Pvt. Ltd.",
  "name": "@zero65tech/indian-stock-market",
  "version": "4.5.3",
  "description": "Indian Stock Market Toolkit",
  "type": "module",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/Zero65Tech/indian-stock-market"
  },
  "keywords": [
    "bse",
    "nse",
    "bse-timings",
    "nse-timings",
    "stock-bse",
    "stock-nse",
    "indian-stock",
    "stock-market",
    "market-utils",
    "trading-utils",
    "zero65",
    "zero65-tech"
  ],
  "main": "src/index.js",
  "scripts": {
    "build": "node src/build.js",
    "test": "node --experimental-vm-modules node_modules/.bin/jest",
    "lint": "npx eslint src test"
  },
  "dependencies": {},
  "devDependencies": {
    "@eslint/js": "^9.37.0",
    "@eslint/json": "^0.13.2",
    "@eslint/markdown": "^7.4.0",
    "eslint": "^9.37.0",
    "globals": "^16.4.0",
    "jest": "^30.2.0",
    "prettier": "^3.6.2"
  },
  "publishConfig": {
    "access": "public"
  }
}
```

#### File: `src/data/holidays.json`
```python
{
  "2011": {
    "1": [26],
    "3": [2],
    "4": [12, 14, 22],
    "8": [15, 31],
    "9": [1],
    "10": [6, 27],
    "11": [7, 10],
    "12": [6]
  },
  "2012": {
    "1": [26],
    "2": [20],
    "3": [8],
    "4": [5, 6],
    "5": [1],
    "8": [15, 20],
    "9": [19],
    "10": [2, 24],
    "11": [14, 28],
    "12": [25]
  },
  "2013": {
    "3": [27, 29],
    "4": [19, 24],
    "5": [1],
    "8": [9, 15],
    "9": [9],
    "10": [2, 16],
    "11": [4, 15],
    "12": [25]
  },
  "2014": {
    "2": [27],
    "3": [17],
    "4": [8, 14, 18, 24],
    "5": [1],
    "7": [29],
    "8": [15, 29],
    "10": [2, 3, 6, 15, 24],
    "11": [4, 6],
    "12": [25]
  },
  "2015": {
    "1": [26],
    "2": [17],
    "3": [6],
    "4": [2, 3, 14],
    "5": [1],
    "9": [17, 25],
    "10": [2, 22],
    "11": [12, 25],
    "12": [25]
  },
  "2016": {
    "1": [26],
    "3": [7, 24, 25],
    "4": [14, 15, 19],
    "7": [6],
    "8": [15],
    "9": [5, 13],
    "10": [11, 12, 31],
    "11": [14]
  },
  "2017": {
    "1": [26],
    "2": [24],
    "3": [13],
    "4": [4, 14],
    "5": [1],
    "6": [26],
    "8": [15, 25],
    "10": [2, 20],
    "12": [25]
  },
  "2018": {
    "1": [26],
    "2": [13],
    "3": [2, 29, 30],
    "5": [1],
    "8": [15, 22],
    "9": [13, 20],
    "10": [2, 18],
    "11": [8, 23],
    "12": [25]
  },
  "2019": {
    "3": [4, 21],
    "4": [17, 19, 29],
    "5": [1],
    "6": [5],
    "8": [12, 15],
    "9": [2, 10],
    "10": [2, 8, 21, 28],
    "11": [12],
    "12": [25]
  },
  "2020": {
    "2": [21],
    "3": [10],
    "4": [2, 6, 10, 14],
    "5": [1, 25],
    "10": [2],
    "11": [16, 30],
    "12": [25]
  },
  "2021": {
    "1": [26],
    "3": [11, 29],
    "4": [2, 14, 21],
    "5": [13],
    "7": [21],
    "8": [19],
    "9": [10],
    "10": [15],
    "11": [5, 19]
  },
  "2022": {
    "1": [26],
    "3": [1, 18],
    "4": [14, 15],
    "5": [3],
    "8": [9, 15, 31],
    "10": [5, 26],
    "11": [8]
  },
  "2023": {
    "1": [26],
    "3": [7, 30],
    "4": [4, 7, 14],
    "5": [1],
    "6": [29],
    "8": [15],
    "9": [19],
    "10": [2, 24],
    "11": [14, 27],
    "12": [25]
  },
  "2024": {
    "1": [22, 26],
    "3": [8, 25, 29],
    "4": [11, 17],
    "5": [1, 20],
    "6": [17],
    "7": [17],
    "8": [15],
    "10": [2],
    "11": [1, 15, 20],
    "12": [25]
  },
  "2025": {
    "2": [26],
    "3": [14, 31],
    "4": [10, 14, 18],
    "5": [1],
    "8": [15, 27],
    "10": [2, 21, 22],
    "11": [5],
    "12": [25]
  },
  "2026": {
    "1": [15, 26],
    "3": [3, 26, 31],
    "4": [3, 14],
    "5": [1, 28],
    "6": [26],
    "9": [14],
    "10": [2, 20],
    "11": [10, 24],
    "12": [25]
  }
}
```


==================================================


## [2/3] Repository: market-holidays-india (`VAULT_IN-QUANT-061_welomoneynews__market-holidays-india`)
- **Full Name**: `IN-QUANT-061_welomoneynews__market-holidays-india`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
<div align="center">

<img src="https://welomoney.com/finscannlogo.png" width="180"/>

# NSE & BSE Market Holidays

<img src="https://readme-typing-svg.demolab.com?font=Poppins&weight=700&size=22&duration=3500&pause=1200&color=0A66C2&center=true&vCenter=true&width=900&lines=Official+NSE+%26+BSE+Trading+Holidays;Indian+Stock+Market+Holiday+Calendar;Plan+Your+Trading+Year;Market+Holiday+Schedule+2026;Powered+by+WeloMoney.com" />

<br>

<a href="https://welomoney.com">
<img src="https://img.shields.io/badge/🌐%20Website-WeloMoney.com-0052CC?style=for-the-badge&logo=googlechrome&logoColor=white"/>
</a>

<a href="https://welomoney.com/market">
<img src="https://img.shields.io/badge/📊%20Live%20Markets-View%20Market%20Updates-success?style=for-the-badge"/>
</a>

</div>

---

## 📖 About

This repository maintains the **official trading holiday calendar** for the **National Stock Exchange (NSE)** and **Bombay Stock Exchange (BSE)**.

Whether you're an investor, trader, analyst, or developer, this calendar helps you plan trading activities around official market closures.

🌐 **Website:** https://welomoney.com

📊 **Live Market Updates:** https://welomoney.com/market

---

# 📅 2026 NSE & BSE Trading Holidays

| 📅 Date | 📆 Day | 🎉 Holiday |
|:---------|:------|:-----------|
| **26 Jan 2026** | Monday | 🇮🇳 Republic Day |
| **18 Feb 2026** | Wednesday | 🕉️ Mahashivratri |
| **14 Mar 2026** | Saturday | 🌈 Holi |
| **31 Mar 2026** | Tuesday | 🌙 Id-Ul-Fitr (Ramzan Eid) |
| **02 Apr 2026** | Thursday | 🛕 Mahavir Jayanti |
| **03 Apr 2026** | Friday | ✝️ Good Friday |
| **14 Apr 2026** | Tuesday | 📖 Dr. B. R. Ambedkar Jayanti |
| **01 May 2026** | Friday | 🏛 Maharashtra Day |
| **28 May 2026** | Thursday | 🕌 Bakri Eid |
| **15 Aug 2026** | Saturday | 🇮🇳 Independence Day |
| **27 Aug 2026** | Thursday | 🪔 Ganesh Chaturthi |
| **02 Oct 2026** | Friday | 🕊️ Gandhi Jayanti & Dussehra |
| **08 Nov 2026** | Sunday | 🪔 Diwali *(Muhurat Trading session timing announced separately by NSE & BSE)* |
| **16 Nov 2026** | Monday | ☬ Guru Nanak Jayanti |
| **25 Dec 2026** | Friday | 🎄 Christmas |

---

# 📌 Important Notes

✅ Trading remains **closed** on all holidays listed above.

🪔 **Muhurat Trading** is conducted on **Diwali**, with the session timing announced separately by the exchanges.

📢 Holiday schedules are subject to change based on official notifications from **NSE** and **BSE**.

---

# 🌐 Stay Connected

<div align="center">

<a href="https://welomoney.com">
<img src="https://img.shields.io/badge/🌐%20Visit-WeloMoney.com-0052CC?style=for-the-badge&logo=googlechrome&logoColor=white"/>
</a>

<a href="https://welomoney.com/market">
<img src="https://img.shields.io/badge/📊%20Market-Live%20Updates-success?style=for-the-badge"/>
</a>

</div>

---

<div align="center">

### 💰 WeloMoney

**India's Trusted Financial News Platform**

📈 Stock Market • IPO • Business • Economy • Global Markets

⭐ **Stay Ahead. Stay Informed. Stay Invested.**

🌐 **https://welomoney.com**

</div>

---

> **Source:** National Stock Exchange (NSE) & Bombay Stock Exchange (BSE). Holiday schedules are based on official exchange notifications and may be revised. For the latest market news and trading updates, visit **WeloMoney**. :contentReference[oaicite:0]{index=0}


==================================================


## [3/3] Repository: nse-scraper (`VAULT_IN-QUANT-067_ShekarArun__nse-scraper`)
- **Full Name**: `IN-QUANT-067_ShekarArun__nse-scraper`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# NSE Data Scraper

A Python-based tool for scraping financial data from the National Stock Exchange (NSE) of India. Currently supports fetching underlying securities data with planned support for contracts information.

## Features

- Fetches underlying securities data from NSE
- Exports data to CSV and JSON formats
- Automated data updates
- Coming soon: Contract information scraping

## Prerequisites

- Python 3.8 or higher
- Poetry (Python package manager)
- Node.js (for some helper scripts)

## Installation

1. Clone the repository: 
```bash
git clone https://github.com/yourusername/nse-data-scraper.git
cd nse-data-scraper
```

2. Install dependencies using Poetry:
```bash
poetry install
```

3. Install Node.js dependencies (if using helper scripts):
```bash
npm install
```

## Usage

1. Activate the Poetry virtual environment:
```bash
poetry shell
```

2. Run the data fetching script:
```bash
python fetchData.py
```

The script will:
- Fetch the latest underlying securities data from NSE
- Save the data to `underlyings.csv`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [x] Underlying securities data scraping
- [ ] Contracts information fetching
- [ ] Historical data support
- [ ] Real-time data updates
- [ ] API endpoint creation

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- National Stock Exchange of India for providing the data
- Contributors and maintainers of the project

## Disclaimer

This project is for educational purposes only. Please ensure you comply with NSE's terms of service and data usage policies when using this tool.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Building the Executable

1. Ensure you have all dependencies installed:
   ```
   pip install -r requirements.txt
   ```

2. Run the build script:
   ```
   python build.py
   ```

3. The executable will be created in the `dist` folder

## For Users

Simply double-click the executable file in the `dist` folder to run the application.

### Core Implementation Code & Architecture
#### File: `build.py`
```python
import PyInstaller.__main__
import os

PyInstaller.__main__.run([
    'gui.py',
    '--onefile',
    '--windowed',
    '--name=NSE-Underlyings-Scraper',
    # '--add-data=underylings_20241110.csv;.',  # Include your data file
    # '--icon=app.ico',  # Optional: You can add this later with your own icon
])
```

#### File: `storeData.py`
```python
import csv
import requests
import time
from datetime import datetime

# Define the URL and endpoint
url = "https://www.nseindia.com"
endpoint = "/api/live-analysis-oi-spurts-underlyings"
complete_url = url + endpoint


class DataCollector:
    def __init__(self):
        self.is_running = False
        self.output_file = 'underlyings.csv'

    def set_output_file(self, filename):
        self.output_file = filename

    def fetch_data(self):
        # Existing fetch_data function content
        s = requests.Session()
        headers = {
            'Host': 'www.nseindia.com',
            'user-agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/80.0.3987.149 Safari/537.36'
            ),
            'accept-language': 'en,gu;q=0.9,hi;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept': '*/*'
        }
        r = s.get(url, timeout=10, headers=headers)
        cookies = dict(r.cookies)
        print('Cookies fetched successfully')

        response = s.get(
            complete_url,
            timeout=10,
            headers=headers,
            cookies=cookies
        )
        print('Got response')
        print('Response status code: ', response.status_code)
        return response.json()

    def save_to_csv(self, data):
        # Modified save_to_csv function to use instance variable
        timestamp = data['timestamp']
        data_list = data['data']

        with open(self.output_file, mode='a+', newline='') as file:
            file.seek(0, 2)
            if file.tell() == 0:
                writer = csv.writer(file)
                header = ['timestamp'] + list(data_list[0].keys())
                writer.writerow(header)
            else:
                file.seek(0)
                last_line = list(csv.reader(file))[-1]
                last_timestamp = last_line[0]

                if timestamp == last_timestamp:
                    print(f"Skipping data write: timestamp {
                          timestamp} is the same as the last recorded timestamp.")
                    return

            file.seek(0, 2)
            writer = csv.writer(file)
            for item in data_list:
                row = [timestamp] + list(item.values())
                writer.writerow(row)

    def start_collection(self, interval=90):
        self.is_running = True
        while self.is_running:
            try:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"\n[{current_time}] Fetching data from NSE")

                data = self.fetch_data()
                print('Fetched data from NSE')

                print('Saving data to CSV')
                self.save_to_csv(data)

                print(f"Data saved to {self.output_file}")
                print(f"Waiting {interval} seconds before next fetch...")
                time.sleep(interval)

            except Exception as e:
                print(f"An error occurred: {e}")
                print("Retrying in 60 seconds...")
                time.sleep(60)

    def stop_collection(self):
        print("Collection stopped")
        self.is_running = False
```

#### File: `gui.py`
```python
import tkinter as tk
from tkinter import ttk, filedialog
from threading import Thread
from storeData import DataCollector
import os


class DataCollectorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("NSE Data Collector")
        self.root.geometry("600x400")
        self.collector = DataCollector()
        self.collection_thread = None

        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # File selection frame
        file_frame = ttk.LabelFrame(
            main_frame, text="Output File Selection", padding="5")
        file_frame.grid(row=0, column=0, columnspan=2,
                        sticky=(tk.W, tk.E), pady=5)

        self.file_path = tk.StringVar(value="underlyings.csv")
        self.file_entry = ttk.Entry(
            file_frame, textvariable=self.file_path, width=50)
        self.file_entry.grid(row=0, column=0, padx=5)

        browse_btn = ttk.Button(
            file_frame, text="Browse", command=self.browse_file)
        browse_btn.grid(row=0, column=1, padx=5)

        # Control buttons
        self.start_btn = ttk.Button(
            main_frame, text="Start Collection", command=self.start_collection)
        self.start_btn.grid(row=1, column=0, pady=10)

        self.stop_btn = ttk.Button(
            main_frame, text="Stop Collection", command=self.stop_collection, state=tk.DISABLED)
        self.stop_btn.grid(row=1, column=1, pady=10)

        # Status frame
        status_frame = ttk.LabelFrame(main_frame, text="Status", padding="5")
        status_frame.grid(row=2, column=0, columnspan=2,
                          sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)

        # Add text widget for logging
        self.log_text = tk.Text(status_frame, height=15, width=60)
        self.log_text.grid(row=0, column=0, padx=5, pady=5)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(
            status_frame, orient=tk.VERTICAL, command=self.log_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.log_text.configure(yscrollcommand=scrollbar.set)

        # Redirect print statements to the text widget
        import sys
        sys.stdout = self

    def write(self, text):
        self.log_text.insert(tk.END, text)
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def flush(self):
        pass

    def browse_file(self):
        initial_dir = os.path.dirname(self.file_path.get()) or os.getcwd()
        filename = filedialog.asksaveasfilename(
            initialdir=initial_dir,
            title="Select Output File",
            filetypes=(("CSV files", "*.csv"), ("All files", "*.*")),
            defaultextension=".csv"
        )
        if filename:
            self.file_path.set(filename)

    def start_collection(self):
        self.collector.set_output_file(self.file_path.get())
        self.collection_thread = Thread(
            target=self.collector.start_collection, daemon=True)
        self.collection_thread.start()

        self.start_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.file_entry.config(state=tk.DISABLED)

    def stop_collection(self):
        self.collector.stop_collection()
        if self.collection_thread:
            self.collection_thread.join(timeout=2)

        self.start_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.file_entry.config(state=tk.NORMAL)


def main():
    root = tk.Tk()
    app = DataCollectorGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
```


==================================================
