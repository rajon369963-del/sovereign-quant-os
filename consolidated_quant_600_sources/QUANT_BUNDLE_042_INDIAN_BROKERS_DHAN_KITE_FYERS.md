# ⚡ [QUANT-SOURCE-042] Consolidated Quant & Algo Trading Repositories
**Category**: `INDIAN_BROKERS_DHAN_KITE_FYERS` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_042_INDIAN_BROKERS_DHAN_KITE_FYERS.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: watchlistpro (`PHASE4-QUANT-153`)
- **Full Name**: `PHASE4-QUANT-153_muraliprajapati__watchlistpro`
- **Description**: Advanced TradingView like watchlists for Zerodha Kite
- **GitHub Stars**: 12
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# Watchlist Pro for Kite

Advanced watchlists for Zerodha Kite.

## 🚀 Features

- ✅ Create as many watchlists as you want. No limit.
- 📊 Import & track 1000 stocks in a watchlist.
- 🖱️ Open stock chart in Kite
- ⌨️ Use arrow keys to navigate the list.
- 🔀 Move stock from one watchlist to another
- 🎨 Light & Dark themes.
- 🔄 Backup & restore your watchlists.
- 🔒 100% safe & secure. No access to your Kite account information. The extension data never leaves your computer.

## 🤝 Support
Drop a mail to mpdevlabs@gmail.com with your queries and feature requests.

## 🔗 Share
Share this extension with your friends, family & trading group who use Zerodha Kite.

### Core Implementation Code & Architecture
#### File: `package.json`
```python
{
  "name": "watchlistpro-website",
  "version": "1.0.0",
  "description": "Advanced TradingView like watchlists for Zerodha Kite.",
  "main": "index.js",
  "scripts": {
    "css": "npx tailwindcss -i ./styles.css -o ./build.css --minify",
    "css:w": "npx tailwindcss -i ./styles.css -o ./build.css --watch"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "tailwindcss": "^3.4.11"
  }
}
```

#### File: `package-lock.json`
```python
{
  "name": "watchlistpro-website",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "watchlistpro-website",
      "version": "1.0.0",
      "license": "ISC",
      "devDependencies": {
        "tailwindcss": "^3.4.11"
      }
    },
    "node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
      "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
      "dev": true,
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@isaacs/cliui": {
      "version": "8.0.2",
      "resolved": "https://registry.npmjs.org/@isaacs/cliui/-/cliui-8.0.2.tgz",
      "integrity": "sha512-O8jcjabXaleOG9DQ0+ARXWZBTfnP4WNAqzuiJK7ll44AmxGKv/J2M4TPjxjY3znBCfvBXFzucm1twdyFybFqEA==",
      "dev": true,
      "dependencies": {
        "string-width": "^5.1.2",
        "string-width-cjs": "npm:string-width@^4.2.0",
        "strip-ansi": "^7.0.1",
        "strip-ansi-cjs": "npm:strip-ansi@^6.0.1",
        "wrap-ansi": "^8.1.0",
        "wrap-ansi-cjs": "npm:wrap-ansi@^7.0.0"
      },
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.5.tgz",
      "integrity": "sha512-IzL8ZoEDIBRWEzlCcRhOaCupYyN5gdIK+Q6fbFdPDg6HqX6jpkItn7DFIpW9LQzXG6Df9sA7+OKnq0qlz/GaQg==",
      "dev": true,
      "dependencies": {
        "@jridgewell/set-array": "^1.2.1",
        "@jridgewell/sourcemap-codec": "^1.4.10",
        "@jridgewell/trace-mapping": "^0.3.24"
      },
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/set-array": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/@jridgewell/set-array/-/set-array-1.2.1.tgz",
      "integrity": "sha512-R8gLRTZeyp03ymzP/6Lil/28tGeGEzhx1q2k703KGWRAI1VdvPIXdG70VJc2pAMw3NA6JKL5hhFu1sJX0Mnn/A==",
      "dev": true,
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.0",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.0.tgz",
      "integrity": "sha512-gv3ZRaISU3fjPAgNsriBRqGWQL6quFx04YMPW/zD8XMLsU32mhCCbfbO6KZFLjvYpCZ8zyDEgqsgf+PwPaM7GQ==",
      "dev": true
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.25",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.25.tgz",
      "integrity": "sha512-vNk6aEwybGtawWmy/PzwnGDOjCkLWSD2wqvjGGAgOAwCGWySYXfYoxt00IJkTF+8Lb57DwOb3Aa0o9CApepiYQ==",
      "dev": true,
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@nodelib/fs.scandir": {
      "version": "2.1.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.scandir/-/fs.scandir-2.1.5.tgz",
      "integrity": "sha512-vq24Bq3ym5HEQm2NKCr3yXDwjc7vTsEThRDnkp2DK9p1uqLR+DHurm/NOTo0KG7HYHU7eppKZj3MyqYuMBf62g==",
      "dev": true,
      "dependencies": {
        "@nodelib/fs.stat": "2.0.5",
        "run-parallel": "^1.1.9"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.stat": {
      "version": "2.0.5",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.stat/-/fs.stat-2.0.5.tgz",
      "integrity": "sha512-RkhPPp2zrqDAQA/2jNhnztcPAlv64XdhIp7a7454A5ovI7Bukxgt7MX7udwAu3zg1DcpPU0rz3VV1SeaqvY4+A==",
      "dev": true,
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@nodelib/fs.walk": {
      "version": "1.2.8",
      "resolved": "https://registry.npmjs.org/@nodelib/fs.walk/-/fs.walk-1.2.8.tgz",
      "integrity": "sha512-oGB+UxlgWcgQkgwo8GcEGwemoTFt3FIO9ababBmaGwXIoBKZ+GTy0pP185beGg7Llih/NSHSV2XAs1lnznocSg==",
      "dev": true,
      "dependencies": {
        "@nodelib/fs.scandir": "2.1.5",
        "fastq": "^1.6.0"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/@pkgjs/parseargs": {
      "version": "0.11.0",
      "resolved": "https://registry.npmjs.org/@pkgjs/parseargs/-/parseargs-0.11.0.tgz",
      "integrity": "sha512-+1VkjdD0QBLPodGrJUeqarH8VAIvQODIbwh9XpP5Syisf7YoQgsJKPNFoqqLQlu+VQ/tVSshMR6loPMn8U+dPg==",
      "dev": true,
      "optional": true,
      "engines": {
        "node": ">=14"
      }
    },
    "node_modules/ansi-regex": {
      "version": "6.1.0",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.1.0.tgz",
      "integrity": "sha512-7HSX4QQb4CspciLpVFwyRe79O3xsIZDDLER21kERQ71oaPodF8jL725AgJMFAYbooIqolJoRLuM81SpeUkpkvA==",
      "dev": true,
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-regex?sponsor=1"
      }
    },
    "node_modules/ansi-styles": {
      "version": "6.2.1",
      "resolved": "https://registry.npmjs.org/ansi-styles/-/ansi-styles-6.2.1.tgz",
      "integrity": "sha512-bN798gFfQX+viw3R7yrGWRqnrN2oRkEkUjjl4JNn4E8GxxbjtG3FbrEIIY3l8/hrwUwIeCZvi4QuOTP4MErVug==",
      "dev": true,
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-styles?sponsor=1"
      }
    },
    "node_modules/any-promise": {
      "version": "1.3.0",
      "resolved": "https://registry.npmjs.org/any-promise/-/any-promise-1.3.0.tgz",
      "integrity": "sha512-7UvmKalWRt1wgjL1RrGxoSJW/0QZFIegpeGvZG9kjp8vrRu55XTHbwnqq2GpXm9uLbcuhxm3IqX9OB4MZR1b2A==",
      "dev": true
    },
    "node_modules/anymatch": {
      "version": "3.1.3",
      "resolved": "https://registry.npmjs.org/anymatch/-/anymatch-3.1.3.tgz",
      "integrity": "sha512-KMReFUr0B4t+D+OBkjR3KYqvocp2XaSzO55UcB6mgQMd3KbcE+mWTyvVV7D/zsdEbNnV6acZUutkiHQXvTr1Rw==",
      "dev": true,
      "dependencies": {
        "normalize-path": "^3.0.0",
        "picomatch": "^2.0.4"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/arg": {
      "version": "5.0.2",
      "resolved": "https://registry.npmjs.org/arg/-/arg-5.0.2.tgz",
      "integrity": "sha512-PYjyFOLKQ9y57JvQ6QLo8dAgNqswh8M1RMJYdQduT6xbWSgK36P/Z/v+p888pM69jMMfS8Xd8F6I1kQ/I9HUGg==",
      "dev": true
    },
    "node_modules/balanced-match": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/balanced-match/-/balanced-match-1.0.2.tgz",
      "integrity": "sha512-3oSeUO0TMV67hN1AmbXsK4yaqU7tjiHlbxRDZOpH0KW9+CeX4bRAaX0Anxt0tx2MrpRpWwQaPwIlISEJhYU5Pw==",
      "dev": true
    },
    "node_modules/binary-extensions": {
      "version": "2.3.0",
      "resolved": "https://registry.npmjs.org/binary-extensions/-/binary-extensions-2.3.0.tgz",
      "integrity": "sha512-Ceh+7ox5qe7LJuLHoY0feh3pHuUDHAcRUeyL2VYghZwfpkNIy/+8Ocg0a3UuSoYzavmylwuLWQOf3hl0jjMMIw==",
      "dev": true,
      "engines": {
        "node": ">=8"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/brace-expansion": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/brace-expansion/-/brace-expansion-2.0.1.tgz",
      "integrity": "sha512-XnAIvQ8eM+kC6aULx6wuQiwVsnzsi9d3WxzV3FpWTGA19F621kwdbsAcFKXgKUHZWsy+mY6iL1sHTxWEFCytDA==",
      "dev": true,
      "dependencies": {
        "balanced-match": "^1.0.0"
      }
    },
    "node_modules/braces": {
      "version": "3.0.3",
      "resolved": "https://registry.npmjs.org/braces/-/braces-3.0.3.tgz",
      "integrity": "sha512-yQbXgO/OSZVD2IsiLlro+7Hf6Q18EJrKSEsdoMzKePKXct3gvD8oLcOQdIzGupr5Fj+EDe8gO/lxc1BzfMpxvA==",
      "dev": true,
      "dependencies": {
        "fill-range": "^7.1.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/camelcase-css": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/camelcase-css/-/camelcase-css-2.0.1.tgz",
      "integrity": "sha512-QOSvevhslijgYwRx6Rv7zKdMF8lbRmx+uQGx2+vDc+KI/eBnsy9kit5aj23AgGu3pa4t9AgwbnXWqS+iOY+2aA==",
      "dev": true,
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/chokidar": {
      "version": "3.6.0",
      "resolved": "https://registry.npmjs.org/chokidar/-/chokidar-3.6.0.tgz",
      "integrity": "sha512-7VT13fmjotKpGipCW9JEQAusEPE+Ei8nl6/g4FBAmIm0GOOLMua9NDDo/DWp0ZAxCr3cPq5ZpBqmPAQgDda2Pw==",
      "dev": true,
      "dependencies": {
        "anymatch": "~3.1.2",
        "braces": "~3.0.2",
        "glob-parent": "~5.1.2",
        "is-binary-path": "~2.1.0",
        "is-glob": "~4.0.1",
        "normalize-path": "~3.0.0",
        "readdirp": "~3.6.0"
      },
      "engines": {
        "node": ">= 8.10.0"
      },
      "funding": {
        "url": "https://paulmillr.com/funding/"
      },
      "optionalDependencies": {
        "fsevents": "~2.3.2"
      }
    },
    "node_modules/chokidar/node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "dev": true,
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/color-convert": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/color-convert/-/color-convert-2.0.1.tgz",
      "integrity": "sha512-RRECPsj7iu/xb5oKYcsFHSppFNnsj/52OVTRKb4zP5onXwVF3zVmmToNcOfGC+CRDpfK/U584fMg38ZHCaElKQ==",
      "dev": true,
      "dependencies": {
        "color-name": "~1.1.4"
      },
      "engines": {
        "node": ">=7.0.0"
      }
    },
    "node_modules/color-name": {
      "version": "1.1.4",
      "resolved": "https://registry.npmjs.org/color-name/-/color-name-1.1.4.tgz",
      "integrity": "sha512-dOy+3AuW3a2wNbZHIuMZpTcgjGuLU/uBL/ubcZF9OXbDo8ff4O8yVp5Bf0efS8uEoYo5q4Fx7dY9OgQGXgAsQA==",
      "dev": true
    },
    "node_modules/commander": {
      "version": "4.1.1",
      "resolved": "https://registry.npmjs.org/commander/-/commander-4.1.1.tgz",
      "integrity": "sha512-NOKm8xhkzAjzFx8B2v5OAHT+u5pRQc2UCa2Vq9jYL/31o2wi9mxBA7LIFs3sV5VSC49z6pEhfbMULvShKj26WA==",
      "dev": true,
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/cross-spawn": {
      "version": "7.0.3",
      "resolved": "https://registry.npmjs.org/cross-spawn/-/cross-spawn-7.0.3.tgz",
      "integrity": "sha512-iRDPJKUPVEND7dHPO8rkbOnPpyDygcDFtWjpeWNCgy8WP2rXcxXL8TskReQl6OrB2G7+UJrags1q15Fudc7G6w==",
      "dev": true,
      "dependencies": {
        "path-key": "^3.1.0",
        "shebang-command": "^2.0.0",
        "which": "^2.0.1"
      },
      "engines": {
        "node": ">= 8"
      }
    },
    "node_modules/cssesc": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/cssesc/-/cssesc-3.0.0.tgz",
      "integrity": "sha512-/Tb/JcjK111nNScGob5MNtsntNM1aCNUDipB/TkwZFhyDrrE47SOx/18wF2bbjgc3ZzCSKW1T5nt5EbFoAz/Vg==",
      "dev": true,
      "bin": {
        "cssesc": "bin/cssesc"
      },
      "engines": {
        "node": ">=4"
      }
    },
    "node_modules/didyoumean": {
      "version": "1.2.2",
      "resolved": "https://registry.npmjs.org/didyoumean/-/didyoumean-1.2.2.tgz",
      "integrity": "sha512-gxtyfqMg7GKyhQmb056K7M3xszy/myH8w+B4RT+QXBQsvAOdc3XymqDDPHx1BgPgsdAA5SIifona89YtRATDzw==",
      "dev": true
    },
    "node_modules/dlv": {
      "version": "1.1.3",
      "resolved": "https://registry.npmjs.org/dlv/-/dlv-1.1.3.tgz",
      "integrity": "sha512-+HlytyjlPKnIG8XuRG8WvmBP8xs8P71y+SKKS6ZXWoEgLuePxtDoUEiH7WkdePWrQ5JBpE6aoVqfZfJUQkjXwA==",
      "dev": true
    },
    "node_modules/eastasianwidth": {
      "version": "0.2.0",
      "resolved": "https://registry.npmjs.org/eastasianwidth/-/eastasianwidth-0.2.0.tgz",
      "integrity": "sha512-I88TYZWc9XiYHRQ4/3c5rjjfgkjhLyW2luGIheGERbNQ6OY7yTybanSpDXZa8y7VUP9YmDcYa+eyq4ca7iLqWA==",
      "dev": true
    },
    "node_modules/emoji-regex": {
      "version": "9.2.2",
      "resolved": "https://registry.npmjs.org/emoji-regex/-/emoji-regex-9.2.2.tgz",
      "integrity": "sha512-L18DaJsXSUk2+42pv8mLs5jJT2hqFkFE4j21wOmgbUqsZ2hL72NsUU785g9RXgo3s0ZNgVl42TiHp3ZtOv/Vyg==",
      "dev": true
    },
    "node_modules/fast-glob": {
      "version": "3.3.2",
      "resolved": "https://registry.npmjs.org/fast-glob/-/fast-glob-3.3.2.tgz",
      "integrity": "sha512-oX2ruAFQwf/Orj8m737Y5adxDQO0LAB7/S5MnxCdTNDd4p6BsyIVsv9JQsATbTSq8KHRpLwIHbVlUNatxd+1Ow==",
      "dev": true,
      "dependencies": {
        "@nodelib/fs.stat": "^2.0.2",
        "@nodelib/fs.walk": "^1.2.3",
        "glob-parent": "^5.1.2",
        "merge2": "^1.3.0",
        "micromatch": "^4.0.4"
      },
      "engines": {
        "node": ">=8.6.0"
      }
    },
    "node_modules/fast-glob/node_modules/glob-parent": {
      "version": "5.1.2",
      "resolved": "https://registry.npmjs.org/glob-parent/-/glob-parent-5.1.2.tgz",
      "integrity": "sha512-AOIgSQCepiJYwP3ARnGx+5VnTu2HBYdzbGP45eLw1vr3zB3vZLeyed1sC9hnbcOc9/SrMyM5RPQrkGz4aS9Zow==",
      "dev": true,
      "dependencies": {
        "is-glob": "^4.0.1"
      },
      "engines": {
        "node": ">= 6"
      }
    },
    "node_modules/fastq": {
      "version": "1.17.1",
      "resolved": "https://registry.npmjs.org/fastq/-/fastq-1.17.1.tgz",
      "integrity": "sha512-sRVD3lWVIXWg6By68ZN7vho9a1pQcN/WBFaAAsDDFzlJjvoGx0P8z7V1t72grFJfJhu3YPZBuu25f7Kaw2jN1w==",
      "dev": true,
      "dependencies": {
        "reusify": "^1.0.4"
      }
    },
    "node_modules/fill-range": {
      "version": "7.1.1",
      "resolved": "https://registry.npmjs.org/fill-range/-/fill-range-7.1.1.tgz",
      "integrity": "sha512-YsGpe3WHLK8ZYi4tWDg2Jy3ebRz2rXowDxnld4bkQB00cc/1Zw9AWnC0i9ztDJitivtQvaI9KaLyKrc+hBW0yg==",
      "dev": true,
      "dependencies": {
        "to-regex-range": "^5.0.1"
      },
      "engines": {
        "node": ">=8"
      }
    },
    "node_modules/foreground-child": {
      "version": "3.3.0",
      "resolved": "https://registry.npmjs.org/foreground-child/-/foreground-child-3.3.0.tgz",
      "integrity": "sha512-Ld2g8rrAyMYFXBhEqMz8ZAHBi4J4uS1i/CxGMDnjyFWddMXLVcDp051DZfu+t7+ab7Wv6SMqpWmyFIj5UbfFvg==",
      "dev": true,
      "dependencies": {
        "cross-spawn": "^7.0.0",
        "signal-exit": "^4.0.1"
      },
      "engines": {
        "node": ">=14"
      },
      "funding": {
        "url": "https://github.com
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: Zerodha-MCP-Trading (`PHASE4-QUANT-156`)
- **Full Name**: `PHASE4-QUANT-156_SirCharan__Zerodha-MCP-Trading`
- **Description**: MCP server for Zerodha's Kite API. Gives an LLM the tools to read market data, run strategies, and place orders on Indian equities and F&O.
- **GitHub Stars**: 7
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# 🚀 Zerodha Market Connect Pro

An advanced algorithmic trading system for Zerodha, featuring automated trading strategies, real-time market analysis, and LLM-powered decision making. Built with Python and integrated with Zerodha's Kite API.

## 📝 Description

Zerodha Market Connect Pro (MCP) is a comprehensive algorithmic trading platform designed specifically for Zerodha traders. This system combines cutting-edge technology with sophisticated trading strategies to provide a powerful automated trading solution. Here's what makes it special:

- **Intelligent Trading**: Leverages Large Language Models (LLMs) for market analysis and trading decisions
- **Real-time Processing**: Handles live market data with low-latency execution and websocket streaming
- **Risk Management**: Implements robust risk controls including position sizing, stop-losses, and exposure limits
- **Strategy Flexibility**: Supports multiple trading strategies with customizable parameters
- **Professional Tools**: Includes advanced technical analysis, volume profiling, and price action pattern recognition
- **Developer Friendly**: Well-documented API, extensive testing suite, and Docker support for easy deployment

Perfect for both professional traders looking to automate their strategies and developers interested in algorithmic trading.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Zerodha-orange)

## 🌟 Key Features

- **🤖 Automated Trading**
  - Real-time order execution
  - Multiple strategy support
  - Customizable entry/exit rules
  - Risk management automation

- **📊 Advanced Market Analysis**
  - Real-time market data processing
  - Technical indicator calculations
  - Volume profile analysis
  - Price action patterns

- **🧠 LLM Integration**
  - Natural language trading commands
  - Market sentiment analysis
  - Strategy optimization
  - Trading journal analysis

- **⚡ High Performance**
  - Asynchronous operations
  - Efficient data handling
  - Real-time websocket streaming
  - Low-latency execution

- **🛡️ Risk Management**
  - Position sizing rules
  - Stop-loss automation
  - Exposure limits
  - Portfolio diversification

## 🔧 Technical Architecture

```
zerodha_mcp/
├── auth/           # Authentication and session management
├── trading/        # Core trading functionality
├── analysis/       # Market analysis and indicators
└── llm/           # Language model integration
```

## 📋 Prerequisites

- Python 3.8 or higher
- [Zerodha Kite](https://kite.zerodha.com/) trading account
- API credentials from [Zerodha Developer Console](https://developers.kite.trade/)
- OpenAI API key (for LLM features)

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/SirCharan/zerodha-market-connect-pro.git
   cd zerodha-market-connect-pro
   ```

2. **Set Up Environment**
   ```bash
   # Create and activate virtual environment
   python -m venv .venv
   source .venv/bin/activate  # Linux/macOS
   .venv\Scripts\activate     # Windows
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure Credentials**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Edit .env with your credentials
   ZERODHA_API_KEY=your_api_key
   ZERODHA_API_SECRET=your_api_secret
   OPENAI_API_KEY=your_openai_api_key  # Optional
   ```

4. **Start Trading System**
   ```bash
   python main.py
   ```

## 📊 Trading Strategies

### Built-in Strategies

1. **Moving Average Crossover**
   ```python
   from zerodha_mcp.trading.strategies import MACrossStrategy
   
   strategy = MACrossStrategy(
       fast_period=10,
       slow_period=30,
       timeframe="5min"
   )
   ```

2. **RSI Mean Reversion**
   ```python
   from zerodha_mcp.trading.strategies import RSIMeanReversionStrategy
   
   strategy = RSIMeanReversionStrategy(
       period=14,
       overbought=70,
       oversold=30
   )
   ```

### Custom Strategy Development

Create your own strategy by inheriting from the base Strategy class:

```python
from zerodha_mcp.trading.base import Strategy

class MyCustomStrategy(Strategy):
    def __init__(self, **params):
        super().__init__()
        self.params = params

    def generate_signals(self, data):
        # Implement your strategy logic here
        pass

    def on_trade(self, trade):
        # Handle trade events
        pass
```

## 🔧 Configuration

### Trading Parameters

Edit `config/default.yaml` to customize trading behavior:

```yaml
trading:
  default_quantity: 1
  max_position_size: 100000
  stop_loss_percent: 2.0
  target_profit_percent: 4.0

risk_management:
  max_daily_loss: 10000
  max_trades_per_day: 10
  max_open_positions: 5

strategies:
  moving_average_crossover:
    enabled: true
    timeframe: "5min"
    fast_period: 10
    slow_period: 30
```

## 🐳 Docker Deployment

1. **Build Image**
   ```bash
   docker build -t zerodha-market-connect-pro .
   ```

2. **Run Container**
   ```bash
   docker run -d \
     --name zerodha-market-connect-pro \
     -v $(pwd)/config:/app/config \
     -v $(pwd)/.env:/app/.env \
     zerodha-market-connect-pro
   ```

## 📈 Performance Monitoring

### Real-time Monitoring
```bash
# View trading logs
tail -f mcp.log

# Check system status
python -m zerodha_mcp.status

# Generate performance report
python -m zerodha_mcp.report
```

### Metrics Dashboard
Access the web dashboard at `http://localhost:5000/dashboard` for:
- P&L visualization
- Strategy performance
- Risk metrics
- Trade history

## 🧪 Development

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=zerodha_mcp tests/

# Run specific test category
pytest tests/test_trading.py
```

### Code Quality
```bash
# Format code
black zerodha_mcp tests

# Check typing
mypy zerodha_mcp

# Run linter
flake8 zerodha_mcp tests
```

## 🔍 Troubleshooting

### Common Issues

1. **Authentication Errors**
   - Verify API credentials in `.env`
   - Check token expiration
   - Ensure API access is enabled

2. **Order Placement Failures**
   - Verify account balance
   - Check trading hours
   - Review order parameters

3. **Strategy Issues**
   - Validate configuration
   - Check data availability
   - Review error logs

## 📚 API Documentation

### Trading Operations

```python
from zerodha_mcp import ZerodhaMCP

# Initialize client
client = ZerodhaMCP()

# Place order
order = client.place_order(
    symbol="RELIANCE",
    quantity=1,
    side="BUY",
    order_type="MARKET"
)

# Get positions
positions = client.get_positions()

# Get holdings
holdings = client.get_holdings()
```

### Market Data

```python
# Get historical data
data = client.get_historical_data(
    symbol="RELIANCE",
    interval="5minute",
    from_date="2024-01-01",
    to_date="2024-01-31"
)

# Stream live ticks
client.subscribe(["RELIANCE"], callback=on_tick)
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📬 Support & Contact

- 📧 Email: charandeepkapoor3@gmail.com
- 💻 GitHub: [@SirCharan](https://github.com/SirCharan)
- 📝 Issues: [GitHub Issues](https://github.com/SirCharan/zerodha-market-connect-pro/issues)
- 📚 Wiki: [Project Documentation](https://github.com/SirCharan/zerodha-market-connect-pro/wiki)

## 🙏 Acknowledgments

- [Zerodha](https://zerodha.com/) for their excellent trading platform
- [KiteConnect](https://kite.trade/) for the robust API
- All contributors who have helped improve this project

### Core Implementation Code & Architecture
#### File: `tests/__init__.py`
```python
"""
Test suite for Zerodha MCP.
"""
```

#### File: `pyproject.toml`
```python
[project]
name = "zerodha-market-connect-pro"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "fastapi>=0.115.11",
    "httpx>=0.28.1",
    "kiteconnect>=5.0.1",
    "mcp[cli]>=1.3.0",
    "python-dotenv>=1.0.1",
    "uvicorn>=0.34.0",
]
```

#### File: `tests/conftest.py`
```python
"""
Pytest configuration and fixtures.
"""

import pytest
import yaml
from pathlib import Path

@pytest.fixture
def config():
    """Load test configuration."""
    config_path = Path("config/default.yaml")
    with open(config_path) as f:
        return yaml.safe_load(f)

@pytest.fixture
def mock_api_client():
    """Create a mock API client for testing."""
    class MockApiClient:
        def __init__(self):
            self.calls = []
        
        def place_order(self, *args, **kwargs):
            self.calls.append(("place_order", args, kwargs))
            return {"order_id": "TEST123"}
    
    return MockApiClient()
```

#### File: `tests/test_trading.py`
```python
"""
Tests for the trading module.
"""

import pytest
from zerodha_mcp.trading import utils

def test_risk_calculation():
    """Test risk calculation utilities."""
    position_size = 10000
    risk_percent = 2.0
    expected_risk = 200
    
    assert utils.calculate_risk(position_size, risk_percent) == expected_risk

def test_mock_order_placement(mock_api_client):
    """Test order placement with mock client."""
    order_params = {
        "tradingsymbol": "INFY",
        "quantity": 1,
        "price": 1000,
        "transaction_type": "BUY",
        "order_type": "LIMIT"
    }
    
    result = mock_api_client.place_order(**order_params)
    assert result["order_id"] == "TEST123"
    assert len(mock_api_client.calls) == 1
    assert mock_api_client.calls[0][0] == "place_order"
```

#### File: `zerodha_mcp/__init__.py`
```python
"""
Zerodha Market Connect Pro (MCP) - A sophisticated trading automation system.

This package provides a comprehensive suite of tools for automated trading on the
Zerodha platform, including:
- Automated trading execution
- Market analysis and visualization
- LLM-powered decision making
- Risk management systems
- Custom strategy implementation
- Real-time market data processing

For more information, see the documentation at:
https://github.com/charandeepkapoor/zerodha-mcp

Author: Charandeep Kapoor
License: MIT
"""

__version__ = "0.1.0"
__author__ = "Charandeep Kapoor"
__license__ = "MIT"

# Package level imports for convenience
from .trading.base import Strategy
from .auth.client import ZerodhaClient
from .analysis.market_data import MarketAnalyzer

# Version information
VERSION_INFO = {
    'major': 0,
    'minor': 1,
    'patch': 0,
    'status': 'beta'
}
```

#### File: `zerodha_mcp/trading/__init__.py`
```python
"""
Trading module for executing and managing trades on the Zerodha platform.

This module provides a comprehensive suite of trading functionality including:

Core Features:
-------------
- Order execution (market, limit, stop-loss)
- Position management
- Portfolio tracking
- Risk management
- Trade logging and analysis

Submodules:
-----------
- utils: Utility functions for trading operations
- strategies: Trading strategy implementations
- risk: Risk management tools and calculations
- orders: Order management and execution
- positions: Position tracking and management

Example Usage:
-------------
>>> from zerodha_mcp.trading import ZerodhaTrade
>>> trader = ZerodhaTrade()
>>> 
>>> # Place a market order
>>> order = trader.place_market_order(
...     symbol="RELIANCE",
...     quantity=1,
...     transaction_type="BUY"
... )
>>> 
>>> # Get current positions
>>> positions = trader.get_positions()

For detailed documentation on each submodule, refer to their respective docstrings.
"""

from .utils import calculate_risk, validate_order_params, calculate_position_value

__all__ = [
    'calculate_risk',
    'validate_order_params',
    'calculate_position_value',
]
```


==================================================


## [3/3] Repository: AutocopyTrade (`PHASE4-QUANT-157`)
- **Full Name**: `PHASE4-QUANT-157_ssjha__AutocopyTrade`
- **Description**: Zerodha Kite trade replicator
- **GitHub Stars**: 6
- **Source Pool**: `phase4_quant_wheels_100`

### Documentation & Overview (README.md)
# AutocopyTrade
Zerodha Kite trade replicator
The program allow the trades in one account to be replicated to mutliple accounts

# Getting started

Download the code in a new folder and install the requirements using
pip install -r requirements.txt

rename the file configTemplate.json to config.json. Populate the config.json with master and child accounts
To popualate the encrypted fields password and TOTPSecret, use the encryptpwd.py to generate encrypted values

D:\autocopytrade>python encryptpwd.py

run the program using the command below

D:\autocopytrade>python AutocopyTrade.py

To get the TOTP secret for zerodha, refer to the article
https://support.zerodha.com/category/your-zerodha-account/login-credentials/login-credentials-of-trading-platforms/articles/time-based-otp-setup

![image](https://user-images.githubusercontent.com/35311/160857289-b64fc532-f8cf-4e2e-a572-94e4f54fd18c.png)

click on "can't scan? copy the code" link to get the TOPT secret

reference
1. Kite api https://kite.trade/
2. Kite connect Python apis https://kite.trade/docs/pykiteconnect/v4/

### Core Implementation Code & Architecture
#### File: `encryptpwd.py`
```python
import base64
import os
import dotenv
from cryptography.fernet import Fernet
# for firsttime you can generate key and store in .env file 
dotenv.load()
if (dotenv.get('key')):
    mysecret = dotenv.get('key').encode()
else:
    mysecret = Fernet.generate_key()
    with open(".env", "w") as envf:
        envf.write("key={}".format(mysecret.decode()))
print(mysecret)
f = Fernet(mysecret)
password_provided = input("enter string to encrypt : ")
password = str(password_provided).encode()  # Convert to type bytes,
encrypted = f.encrypt(password)
print (encrypted.decode())
```

#### File: `configTemplate.json`
```python
{
    "MASTER" : 
	{
        "userid"        : "ZERODHAID",
        "password"      : "encrypted Kite password",
        "APIKey"        : "kite api key",
        "APISecret"     : "kite api secret",
        "loginURL"      : "kite login url <https://kite.trade/connect/login?api_key=<apikey>",
        "TOPTSecret"    : "encrypted secret of TOPT QR"
    },
    "CHILD" : 
	{
        "CHILDID1" : 
		{
			"userid"        : "CHILDID1",
            "password"      : "encrypted Kite password",
            "APIKey"        : "kite api key",
            "APISecret"     : "kite api secret",
            "loginURL"      : "kite login url <https://kite.trade/connect/login?api_key=<apikey>",
            "multiplier"    : 1,
			"enabled"       : "Y",
            "TOPTSecret"    : "encrypted secret of TOPT QR"
        },
        "CHILDID2" : 
		{
			"userid"        : "CHILDID2-",
            "password"      : "encrypted Kite password",
            "APIKey"        : "kite api key",
            "APISecret"     : "kite api secret",
            "loginURL"      : "kite login url <https://kite.trade/connect/login?api_key=<apikey>",
            "multiplier"    : 1,
			"enabled"       : "Y",
            "TOPTSecret"    : "encrypted secret of TOPT QR"
        }   
    }
}
```

#### File: `Autocopytrade.py`
```python
import time
import os
import traceback
import logging
import json
from turtle import dot
import dotenv
import sys
from urllib import parse
from kiteconnect import KiteTicker
from kiteconnect import  KiteConnect
from selenium import webdriver
from selenium.webdriver.common.by import By
import onetimepass as otp
from cryptography.fernet import Fernet

#set logger

logging.basicConfig(filename='logcopytrade.log',format='%(asctime)s-%(process)d-%(levelname)s-%(message)s',level=logging.ERROR)

logging.info("Program Copytrader started")

sourceOrders={}
childaccts={}
orderlookup={}
kitemaster=None
configFile='config.json'
cwd = os.getcwd()
with open(configFile, 'r') as f:
    config = json.load(f)

dotenv.load()
if (dotenv.get('key')):
    mysecret = dotenv.get('key').encode()
    #print(mysecret)
else:
    print('Environment file not found. Exiting')
    sys.exit()



def getRequestToken(loginConfig):
    
    logging.info("Getting the request token for : {}".format(loginConfig['userid']))
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-error')
    options.add_argument('--ignore-ssl-errors')
    #options.headless = True
    driver = webdriver.Chrome('chromedriver',options=options)
    driver.delete_all_cookies()
#    driver.delete_cookie('kite.zerodha.com')
    driver.implicitly_wait(2)
    driver.get(loginConfig['loginURL'])
    driver.implicitly_wait(4)
    driver.find_element(by=By.ID,value='userid').send_keys(loginConfig['userid'])
    driver.find_element(by=By.ID,value='password').send_keys(deCryptPwd(loginConfig['password']))
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/form/div[4]/button').click()
    time.sleep(3)
    #driver.implicitly_wait(2)
    # Get and enter TOPT
    myToken = otp.get_totp(deCryptPwd(loginConfig['TOPTSecret']))
    #driver.find_element(by=By.ID,value='External TOTP').send_keys(myToken)
    #driver.find_element(by=By.TAG_NAME,value='input').send_keys(myToken)
    driver.find_element(by=By.XPATH,value='//input[@type="text"]').send_keys(myToken)
    driver.find_element(by=By.XPATH,value='//button[@type="submit"]').click()
    time.sleep(4)
    url=driver.current_url
    requestToken = parse.parse_qs(parse.urlparse(url).query)['request_token'][0]
    driver.quit()
    logging.info("Successfully logged in for  : {}".format(loginConfig['userid']))
    print(loginConfig['userid'] + ' successfully logged in')
    return(requestToken)

def deCryptPwd(encodedPwd):
    f = Fernet(mysecret)
    enc =encodedPwd.encode()
    dec= f.decrypt(enc)
    return(dec.decode())

# Callback for tick reception.
def on_ticks(ws, ticks):
    if len(ticks) > 0:
        test=1
        #logging.info("Current mode: {}".format(ticks[0]["mode"]))

tokens = [260105] # dummy sensex token. Add tokens based 
# Callback for successful connection.
def on_connect(ws, response):
    logging.info("Successfully connected. Response: {}".format(response))
    ws.subscribe(tokens)
    ws.set_mode(ws.MODE_FULL, tokens)
    logging.info("Subscribe to tokens in Full mode: {}".format(tokens))

# Callback when current connection is closed.
def on_close(ws, code, reason):
    logging.info("Connection closed: {code} - {reason}".format(code=code, reason=reason))


# Callback when connection closed with error.
def on_error(ws, code, reason):
    logging.info("Connection error: {code} - {reason}".format(code=code, reason=reason))


# Callback when reconnect is on progress
def on_reconnect(ws, attempts_count):
    logging.info("Reconnecting: {}".format(attempts_count))


# Callback when all reconnect failed (exhausted max retries)
def on_noreconnect(ws):
    logging.info("Reconnect failed.")
    
def on_order_update(ws, data):
    logging.info("Order alert received : {}".format(data))
    copyTrade(data)
    
    
def copyTrade(data):
    logging.debug('starting copy trade')
    

    if data['product'] not in prodFilter:
        if data['status'] == 'CANCELLED':
            cancelTargetOrders(data)
        else:
            logging.debug('copy trade open and update')
            
            #ignore UPDATE messages as it is resulting in out of sequence order updates
            if (data['status'] == 'OPEN') or (data['status']=='TRIGGER PENDING'):
                if (data['order_id'] in sourceOrders):
                    updateTargetOrders(data)
                else: 
                    createTargetOrders(data)
        showMarginsAvailable()
    else:
        logging.info('Product type {} ignored'.format(data['product']))

# extract order parameters
# Validate if there is a change in order
# if new order create the target orders
# if update, update target orders 
# if cancelled, cancel target order


def getTargetOrder(orderid, userid):
    key = orderid + '|' + userid
    return orderlookup[key]
    
# store the child orders in lookup dictionary
def storeTargetOrder(parent_oid, userid,child_oid):
    key = parent_oid + '|' + userid
    orderlookup[key] = child_oid


def createTargetOrders(data):
    logging.info('inside create orders')
    for childacct in childaccts:
        accDetail = childaccts[childacct]
       # logging.info("Updated order {userid} - {cldorder}".format(userid=accDetail['userid'], cldorder=accDetail['multiplier']))
        createTargetOrder(data,accDetail['userid'], accDetail['kiteobj'], accDetail['multiplier'])
    
def createTargetOrder(orderdata, userid,targetAccnt,multiplier):
    logging.info('creating order{}'.format(orderdata['order_id']))

    try:
        order_id = targetAccnt.place_order(
            variety=orderdata['variety'],
            exchange=orderdata['exchange'],
            tradingsymbol=orderdata['tradingsymbol'],
            order_type=orderdata['order_type'],
            transaction_type=orderdata['transaction_type'],
            validity=orderdata['validity'],
            product=orderdata['product'],
            quantity=int(round(int(orderdata['quantity']) * float(multiplier),0)),
            price=orderdata['price'],
            trigger_price= orderdata['trigger_price']
        )
        sourceOrders[orderdata['order_id']] = orderdata
        storeTargetOrder(orderdata['order_id'], userid, order_id)
        logging.info("Created order {userid} - {cldorder}".format(userid=userid, cldorder=order_id))
    except Exception as e:
        stacktrace=traceback.format_exc()
        logging.error("***** ERROR Order create error {exception} - {stacktrace}".format(exception=e, stacktrace=stacktrace))
        print("Child order not created for parent order"+orderdata['order_id']+" for user id " + userid)
        
def showMarginsAvailable():
    print('---Margins--Available----------Used-----Cash Available-----------------------')
    #print('-----------------Margins----------------------------')
    showMargin(kite=kitemaster,userid=masterconfig['userid'])
    for childacct in childaccts:
        accDetail = childaccts[childacct]
       # logging.info("Updated order {userid} - {cldorder}".format(userid=accDetail['userid'], cldorder=accDetail['multiplier']))
        showMargin(kite=accDetail['kiteobj'],userid=accDetail['userid'])
    print('----------------------------------------------------')

    

def showMargin(kite,userid):
    margin = kite.margins(segment="equity")
    logging.debug("Margin: {}".format(margin))
    print ("{0} : {1:12,.0f}  {2:12,.0f}  {3:12,.0f}".format(userid,margin['net'],margin['utilised']['debits'],margin['available']['live_balance']))
    #print(userid + " margin: {0:12,.0f} ".format(margin['net']))


def checkifupdate(orderdata):
    origorder = sourceOrders[orderdata['order_id']]
    if (origorder['variety']== orderdata['variety'] and
        origorder['order_type']== orderdata['order_type'] and 
        origorder['quantity']== orderdata['quantity'] and
        origorder['price']== orderdata['price'] and
        origorder['trigger_price']== orderdata['trigger_price'] ):
        
        return False
    else:
        return True

#Update target order for each child account after checking if the order parameters have changed. 
#Show error if the it is an old order that doesn't have any mapping
def updateTargetOrders(data):
    logging.info('inside update orders')
    try:
        if checkifupdate(data):
            for childacct in childaccts:
                accDetail = childaccts[childacct]
                updateTargetOrder(data,accDetail['userid'], accDetail['kiteobj'], accDetail['multiplier'])
                sourceOrders[data['order_id']] = data
            else:
                logging.info("Order id {} not changed. Not updated to child accounts".format(data['order_id']))
    except Exception as e:
        stacktrace=traceback.format_exc()
        logging.error("***** ERROR Order update error {exception} - {stacktrace}".format(exception=e, stacktrace=stacktrace))
        print("Order mapping not found " + data['order_id'])
        
def updateTargetOrder(orderdata, userid, targetAccnt,multiplier):
    logging.info('Updating order{}'.format(orderdata['order_id']))

    try:
        targetorder= getTargetOrder(orderdata['order_id'], userid)
        order_id = targetAccnt.modify_order(
                order_id = targetorder,
                variety=orderdata['variety'],
                order_type=orderdata['order_type'],
                validity=orderdata['validity'],
                quantity=int(round(int(orderdata['quantity'])* float(multiplier),0)),
                price=orderdata['price'],
                trigger_price= orderdata['trigger_price']
            )
        logging.info("Updated order {userid} - {cldorder}".format(userid=userid, cldorder=order_id))
    except Exception as e:
        stacktrace=traceback.format_exc()
        logging.error("***** ERROR Order update error {exception} - {stacktrace}".format(exception=e, stacktrace=stacktrace))
        print("Child order not updated for parent order"+orderdata['order_id']+" for user id " + userid)
        
        
def cancelTargetOrders(data):
    for childacct in childaccts:
        accDetail = childaccts[childacct]
        cancelTargetOrder(data,accDetail['userid'], accDetail['kiteobj'])
        
def cancelTargetOrder(orderdata,userid, targetAccnt): 
    logging.info('Cancelling order{}'.format(orderdata['order_id']))
    try:
        targetorder= getTargetOrder(orderdata['order_id'], userid)
        targetAccnt.cancel_order(variety = orderdata['variety'], order_id=targetorder)
    except Exception as e:
        stacktrace=traceback.format_exc()
        logging.error("Order cancel error {exception} - {stacktrace}".format(exception=e, stacktrace=stacktrace))
    
    logging.info("Cancelled order {userid} - {cldorder}".format(userid=userid, cldorder=targetorder))
    
# Master account login
masterconfig = config['MASTER']
prodFilter = config['DONOTPROCESSPROD']

logging.info('Logging into Master account')

try:
    kitemaster= KiteConnect (api_key=masterconfig['APIKey'])
    requestToken = getRequestToken(masterconfig)
    print ("Request token received:",requestToken)
    time.sleep(2)
    data = kitemaster.generate_session(request_token=requestToken, api_secret=masterconfig['APISecret'])
    kws = KiteTicker(masterconfig['APIKey'], data["access_token"])       
    print ('Kitemaster Connection successful')
     
except Exception as e:
    stacktrace=traceback.format_exc()
    logging.error("Connection Error {exception} - {stacktrace}".format(exception=e, stacktrace=stacktrace))
    print("Connection error for master user id:",masterconfig['userid'],". Exiting program!!!")
    raise

# Assign the callbacks.
kws.on_ticks = on_ticks
kws.on_close = on_close
kws.on_error = on_error
kws.on_connect = on_connect
kws.on_reconnect = on_reconnect
kws.on_noreconnect = on_noreconnect
kws.on_order_update = on_order_update

logging.info('Logging into target accounts')

for childacct in config['CHILD']:
    child = {}
    childconfig = config['CHILD'][childacct]
    if ( childconfig['enabled'] == 'Y'):
        child['userid']= childconfig['userid']
        child['api_key']= childconfig['APIKey']
        child['api_secret'] = childconfig['APISecret'] 
        child['multiplier'] = childconfig['multiplier']
        child['request_token'] =    getRequestToken(childconfig)
        try:
            time.sleep(2)
            kite= KiteConnect (api_key=child['api_key'])
            data = kite.generate_session(request_token=child['request_token'], api_secret=child['api_secret'])
            kite.set_access_token(data["access_token"])
            print("Kiteconnect session established")
        
        except Exception as e:
            stacktrace=traceback.format_exc()
            logging.error("Connection Error {exception} - {stacktrace}".format(exception=e, stacktrace=stacktrace))
            print("Connection error for user id: ",child['userid'],". Exiting program!!!")
            raise
        child['access_token']  = data["access_token"]
        child['kiteobj']  = kite
        logging.info("Kite session created: {}".format(data))
        childaccts[child['userid']]=child

showMarginsAvailable()
#orderdet='{"account_id": "DR0900", "unfilled_quantity": 0, "checksum": "", "placed_by": "DR0900", "order_id": "220601400163639", "exchange_order_id": "1500000002188929", "parent_order_id": "", "status": "OPEN", "status_message": "", "status_message_raw": "", "order_timestamp": "2022-06-01 09:19:32", "exchange_update_timestamp": "2022-06-01 09:19:32", "exchange_timestamp": "2022-06-01 09:19:32", "variety": "regular", "exchange": "NFO", "tradingsymbol": "BANKNIFTY2260236800CE", "instrument_token": 12523778, "order_type": "LIMIT", "transaction_type": "BUY", "validity": "DAY", "product": "CNC", "quantity": 900, "disclosed_quantity": 0, "price": 4.7, "trigger_price": 0, "average_price": 0, "filled_quantity": 0, "pending_quantity": 900, "cancelled_quantity": 0, "market_protection": 0, "meta": {}, "tag": "", "guid": "01XLJGdTQEe05JN"}'
#copyTrade(json.loads(orderdet))
#Connect for subscribing to order updates in master account
kws.connect()
```


==================================================
