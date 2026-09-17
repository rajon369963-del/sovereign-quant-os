# ⚡ [QUANT-SOURCE-178] Consolidated Quant & Algo Trading Repositories
**Category**: `MARKET_MAKING_ORDER_FLOW` | **Repositories in this Source**: 3
**Generated**: QUANT_BUNDLE_178_MARKET_MAKING_ORDER_FLOW.md | **Target**: NotebookLM 290+ Quant Code Brain

---

## [1/3] Repository: tradesphere (`VAULT_IN-QUANT-032_DarkEnergyOverflow__tradesphere`)
- **Full Name**: `IN-QUANT-032_DarkEnergyOverflow__tradesphere`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `indian_quant_vault`

### Documentation & Overview (README.md)
# TradeSphere - Virtual Stock Trading Simulator

A full-stack virtual stock trading platform built with Next.js, featuring real-time market data, portfolio management, and institutional-grade UI/UX design.

## Features

- 🔐 **Secure Authentication** - NextAuth.js with credentials and OAuth support
- 📊 **Real-time Market Data** - Live stock prices via Finnhub API
- 💼 **Portfolio Management** - Track holdings, P/L, and performance
- 💰 **Virtual Trading** - Buy and sell stocks with ₹1,00,000 starting capital
- 📈 **Interactive Charts** - Price charts using Lightweight Charts
- 🎨 **Premium UI/UX** - Institutional-grade design with Material Symbols
- 🇮🇳 **Indian Market Focus** - NSE/BSE references, IST timezone, ₹ currency


## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Database**: PostgreSQL with Prisma ORM
- **Authentication**: NextAuth.js
- **Styling**: Tailwind CSS
- **Charts**: Lightweight Charts
- **Market Data**: Finnhub API along with yahooo finace 
- **Icons**: Material Symbols Outlined

## Getting Started

### Prerequisites

- Node.js 18+ and npm
- PostgreSQL database
- Finnhub API key (free tier available)

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd tradesphere
```

2. Install dependencies:
```bash
npm install
```

3. Set up environment variables:
```bash
cp .env.example .env
```

Edit `.env` and add your credentials:
```env
DATABASE_URL="postgresql://user:password@localhost:5432/tradesphere"
NEXTAUTH_SECRET="your-secret-key"
NEXTAUTH_URL="http://localhost:3000"
FINNHUB_API_KEY="your-finnhub-api-key"
```

4. Run database migrations:
```bash
npx prisma migrate dev
```

5. Start the development server:
```bash
npm run dev
```

6. Open [http://localhost:3000](http://localhost:3000) in your browser

## Project Structure

```
tradesphere/
├── src/
│   ├── app/                    # Next.js app router pages
│   │   ├── api/               # API routes
│   │   ├── auth/              # Authentication pages
│   │   ├── dashboard/         # Dashboard page
│   │   ├── portfolio/         # Portfolio page
│   │   ├── stocks/            # Stock pages
│   │   └── transactions/      # Transactions page
│   ├── components/            # React components
│   ├── lib/                   # Utility libraries
│   ├── services/              # Business logic services
│   └── types/                 # TypeScript type definitions
├── prisma/
│   ├── schema.prisma          # Database schema
│   └── migrations/            # Database migrations
└── public/                    # Static assets
```

## Database Schema

- **User**: User accounts with email, password, and balance
- **Portfolio**: User stock holdings with quantity and average price
- **Transaction**: Trading history (buy/sell transactions)

## API Routes

- `POST /api/auth/signup` - Create new account
- `POST /api/auth/[...nextauth]` - NextAuth.js authentication
- `GET /api/portfolio` - Get user portfolio
- `GET /api/stocks` - Get popular stocks
- `GET /api/stocks/search` - Search stocks
- `GET /api/stocks/[symbol]` - Get stock details
- `POST /api/trade/buy` - Buy stocks
- `POST /api/trade/sell` - Sell stocks
- `GET /api/transactions` - Get transaction history

## Deployment

See [DEPLOYMENT.md](./DEPLOYMENT.md) for detailed deployment instructions for Vercel.

### Quick Deploy to Vercel

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/yourusername/tradesphere)

1. Click the button above
2. Set environment variables in Vercel dashboard
3. Deploy!

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `DATABASE_URL` | PostgreSQL connection string | Yes |
| `NEXTAUTH_SECRET` | Secret for NextAuth.js | Yes |
| `NEXTAUTH_URL` | Application URL | Yes |
| `FINNHUB_API_KEY` | Finnhub API key | Yes |

## Features Roadmap

- [ ] Real Indian stock support (NSE/BSE)
- [ ] Advanced charting with indicators
- [ ] Watchlist functionality
- [ ] Price alerts
- [ ] Portfolio analytics
- [ ] Social trading features
- [ ] Mobile app (React Native)
- [ ] Paper trading competitions

## Known Limitations

- Currently uses US stocks (AAPL, MSFT, etc.) due to Finnhub free tier limitations
- Indian stocks (.NS suffix) have limited support on Finnhub free tier
- Consider using NSE India API or Alpha Vantage for better Indian stock coverage

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - feel free to use this project for learning or commercial purposes.

## Support

For issues and questions:
- Create an issue on GitHub
- Check the [DEPLOYMENT.md](./DEPLOYMENT.md) guide
- Review Finnhub API documentation

## Acknowledgments

- Design inspired by institutional trading platforms
- Market data provided by Finnhub
- Icons by Google Material Symbols
- Charts by TradingView Lightweight Charts

---

Built with ❤️ for the Indian trading community

### Core Implementation Code & Architecture
#### File: `prisma/migrations/migration_lock.toml`
```python
# Please do not edit this file manually
# It should be added in your version-control system (i.e. Git)
provider = "postgresql"
```

#### File: `vercel.json`
```python
{
  "buildCommand": "prisma generate && next build",
  "installCommand": "npm install",
  "framework": "nextjs",
  "regions": ["bom1"]
}
```

#### File: `tsconfig.json`
```python
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules"]
}
```

#### File: `package.json`
```python
{
  "name": "tradesphere",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "prisma generate && next build",
    "start": "next start",
    "lint": "next lint",
    "postinstall": "prisma generate",
    "vercel-build": "prisma generate && prisma migrate deploy && next build"
  },
  "dependencies": {
    "@prisma/client": "^5.14.0",
    "bcryptjs": "^2.4.3",
    "lightweight-charts": "^4.1.0",
    "next": "^14.2.0",
    "next-auth": "^4.24.0",
    "react": "^18.3.0",
    "react-dom": "^18.3.0",
    "yahoo-finance2": "^3.14.0",
    "zod": "^3.23.0"
  },
  "devDependencies": {
    "@types/bcryptjs": "^2.4.6",
    "@types/node": "^20.12.0",
    "@types/react": "^18.3.0",
    "@types/react-dom": "^18.3.0",
    "autoprefixer": "^10.4.0",
    "eslint": "^8.57.0",
    "eslint-config-next": "^14.2.0",
    "postcss": "^8.4.0",
    "prisma": "^5.14.0",
    "tailwindcss": "^3.4.0",
    "typescript": "^5.4.0"
  }
}
```

#### File: `package-lock.json`
```python
{
  "name": "tradesphere",
  "version": "0.1.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "tradesphere",
      "version": "0.1.0",
      "hasInstallScript": true,
      "dependencies": {
        "@prisma/client": "^5.14.0",
        "bcryptjs": "^2.4.3",
        "lightweight-charts": "^4.1.0",
        "next": "^14.2.0",
        "next-auth": "^4.24.0",
        "react": "^18.3.0",
        "react-dom": "^18.3.0",
        "yahoo-finance2": "^3.14.0",
        "zod": "^3.23.0"
      },
      "devDependencies": {
        "@types/bcryptjs": "^2.4.6",
        "@types/node": "^20.12.0",
        "@types/react": "^18.3.0",
        "@types/react-dom": "^18.3.0",
        "autoprefixer": "^10.4.0",
        "eslint": "^8.57.0",
        "eslint-config-next": "^14.2.0",
        "postcss": "^8.4.0",
        "prisma": "^5.14.0",
        "tailwindcss": "^3.4.0",
        "typescript": "^5.4.0"
      }
    },
    "node_modules/@alloc/quick-lru": {
      "version": "5.2.0",
      "resolved": "https://registry.npmjs.org/@alloc/quick-lru/-/quick-lru-5.2.0.tgz",
      "integrity": "sha512-UrcABB+4bUrFABwbluTIBErXwvbsU/V7TZWfmbgJfbkwiBuziS9gxdODUyuiecfdGQ85jglMW6juS3+z5TsKLw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=10"
      },
      "funding": {
        "url": "https://github.com/sponsors/sindresorhus"
      }
    },
    "node_modules/@babel/runtime": {
      "version": "7.29.2",
      "resolved": "https://registry.npmjs.org/@babel/runtime/-/runtime-7.29.2.tgz",
      "integrity": "sha512-JiDShH45zKHWyGe4ZNVRrCjBz8Nh9TMmZG1kh4QTK8hCBTWBi8Da+i7s1fJw7/lYpM4ccepSNfqzZ/QvABBi5g==",
      "license": "MIT",
      "engines": {
        "node": ">=6.9.0"
      }
    },
    "node_modules/@deno/shim-deno": {
      "version": "0.18.2",
      "resolved": "https://registry.npmjs.org/@deno/shim-deno/-/shim-deno-0.18.2.tgz",
      "integrity": "sha512-oQ0CVmOio63wlhwQF75zA4ioolPvOwAoK0yuzcS5bDC1JUvH3y1GS8xPh8EOpcoDQRU4FTG8OQfxhpR+c6DrzA==",
      "license": "MIT",
      "dependencies": {
        "@deno/shim-deno-test": "^0.5.0",
        "which": "^4.0.0"
      }
    },
    "node_modules/@deno/shim-deno-test": {
      "version": "0.5.0",
      "resolved": "https://registry.npmjs.org/@deno/shim-deno-test/-/shim-deno-test-0.5.0.tgz",
      "integrity": "sha512-4nMhecpGlPi0cSzT67L+Tm+GOJqvuk8gqHBziqcUQOarnuIax1z96/gJHCSIz2Z0zhxE6Rzwb3IZXPtFh51j+w==",
      "license": "MIT"
    },
    "node_modules/@deno/shim-deno/node_modules/isexe": {
      "version": "3.1.5",
      "resolved": "https://registry.npmjs.org/isexe/-/isexe-3.1.5.tgz",
      "integrity": "sha512-6B3tLtFqtQS4ekarvLVMZ+X+VlvQekbe4taUkf/rhVO3d/h0M2rfARm/pXLcPEsjjMsFgrFgSrhQIxcSVrBz8w==",
      "license": "BlueOak-1.0.0",
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@deno/shim-deno/node_modules/which": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/which/-/which-4.0.0.tgz",
      "integrity": "sha512-GlaYyEb07DPxYCKhKzplCWBJtvxZcZMrL+4UkrTSJHHPyZU4mYYTv3qaOe77H7EODLSSopAUFAc6W8U4yqvscg==",
      "license": "ISC",
      "dependencies": {
        "isexe": "^3.1.1"
      },
      "bin": {
        "node-which": "bin/which.js"
      },
      "engines": {
        "node": "^16.13.0 || >=18.0.0"
      }
    },
    "node_modules/@emnapi/core": {
      "version": "1.10.0",
      "resolved": "https://registry.npmjs.org/@emnapi/core/-/core-1.10.0.tgz",
      "integrity": "sha512-yq6OkJ4p82CAfPl0u9mQebQHKPJkY7WrIuk205cTYnYe+k2Z8YBh11FrbRG/H6ihirqcacOgl2BIO8oyMQLeXw==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/wasi-threads": "1.2.1",
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.10.0",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.10.0.tgz",
      "integrity": "sha512-ewvYlk86xUoGI0zQRNq/mC+16R1QeDlKQy21Ki3oSYXNgLb45GV1P6A0M+/s6nyCuNDqe5VpaY84BzXGwVbwFA==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@emnapi/wasi-threads": {
      "version": "1.2.1",
      "resolved": "https://registry.npmjs.org/@emnapi/wasi-threads/-/wasi-threads-1.2.1.tgz",
      "integrity": "sha512-uTII7OYF+/Mes/MrcIOYp5yOtSMLBWSIoLPpcgwipoiKbli6k322tcoFsxoIIxPDqW01SQGAgko4EzZi2BNv2w==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@eslint-community/eslint-utils": {
      "version": "4.9.1",
      "resolved": "https://registry.npmjs.org/@eslint-community/eslint-utils/-/eslint-utils-4.9.1.tgz",
      "integrity": "sha512-phrYmNiYppR7znFEdqgfWHXR6NCkZEK7hwWDHZUjit/2/U0r6XvkDl0SYnoM51Hq7FhCGdLDT6zxCCOY1hexsQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "eslint-visitor-keys": "^3.4.3"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      },
      "peerDependencies": {
        "eslint": "^6.0.0 || ^7.0.0 || >=8.0.0"
      }
    },
    "node_modules/@eslint-community/regexpp": {
      "version": "4.12.2",
      "resolved": "https://registry.npmjs.org/@eslint-community/regexpp/-/regexpp-4.12.2.tgz",
      "integrity": "sha512-EriSTlt5OC9/7SXkRSCAhfSxxoSUgBm33OH+IkwbdpgoqsSsUg7y3uh+IICI/Qg4BBWr3U2i39RpmycbxMq4ew==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^12.0.0 || ^14.0.0 || >=16.0.0"
      }
    },
    "node_modules/@eslint/eslintrc": {
      "version": "2.1.4",
      "resolved": "https://registry.npmjs.org/@eslint/eslintrc/-/eslintrc-2.1.4.tgz",
      "integrity": "sha512-269Z39MS6wVJtsoUl10L60WdkhJVdPG24Q4eZTH3nnF6lpvSShEK3wQjDX9JRWAUPvPh7COouPpU9IrqaZFvtQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ajv": "^6.12.4",
        "debug": "^4.3.2",
        "espree": "^9.6.0",
        "globals": "^13.19.0",
        "ignore": "^5.2.0",
        "import-fresh": "^3.2.1",
        "js-yaml": "^4.1.0",
        "minimatch": "^3.1.2",
        "strip-json-comments": "^3.1.1"
      },
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      },
      "funding": {
        "url": "https://opencollective.com/eslint"
      }
    },
    "node_modules/@eslint/js": {
      "version": "8.57.1",
      "resolved": "https://registry.npmjs.org/@eslint/js/-/js-8.57.1.tgz",
      "integrity": "sha512-d9zaMRSTIKDLhctzH12MtXvJKSSUhaHcjV+2Z+GK+EEY7XKpP5yR4x+N3TAcHTcu963nIr+TMcCb4DBCYX1z6Q==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": "^12.22.0 || ^14.17.0 || >=16.0.0"
      }
    },
    "node_modules/@humanwhocodes/config-array": {
      "version": "0.13.0",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/config-array/-/config-array-0.13.0.tgz",
      "integrity": "sha512-DZLEEqFWQFiyK6h5YIeynKx7JlvCYWL0cImfSRXZ9l4Sg2efkFGTuFf6vzXjK1cq6IYkU+Eg/JizXw+TD2vRNw==",
      "deprecated": "Use @eslint/config-array instead",
      "dev": true,
      "license": "Apache-2.0",
      "dependencies": {
        "@humanwhocodes/object-schema": "^2.0.3",
        "debug": "^4.3.1",
        "minimatch": "^3.0.5"
      },
      "engines": {
        "node": ">=10.10.0"
      }
    },
    "node_modules/@humanwhocodes/module-importer": {
      "version": "1.0.1",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/module-importer/-/module-importer-1.0.1.tgz",
      "integrity": "sha512-bxveV4V8v5Yb4ncFTT3rPSgZBOpCkjfK0y4oVVVJwIuDVBRMDXrPyXRL988i5ap9m9bnyEEjWfm5WkBmtffLfA==",
      "dev": true,
      "license": "Apache-2.0",
      "engines": {
        "node": ">=12.22"
      },
      "funding": {
        "type": "github",
        "url": "https://github.com/sponsors/nzakas"
      }
    },
    "node_modules/@humanwhocodes/object-schema": {
      "version": "2.0.3",
      "resolved": "https://registry.npmjs.org/@humanwhocodes/object-schema/-/object-schema-2.0.3.tgz",
      "integrity": "sha512-93zYdMES/c1D69yZiKDBj0V24vqNzB/koF26KPaagAfd3P/4gUlh3Dys5ogAK+Exi9QyzlD8x/08Zt7wIKcDcA==",
      "deprecated": "Use @eslint/object-schema instead",
      "dev": true,
      "license": "BSD-3-Clause"
    },
    "node_modules/@isaacs/cliui": {
      "version": "8.0.2",
      "resolved": "https://registry.npmjs.org/@isaacs/cliui/-/cliui-8.0.2.tgz",
      "integrity": "sha512-O8jcjabXaleOG9DQ0+ARXWZBTfnP4WNAqzuiJK7ll44AmxGKv/J2M4TPjxjY3znBCfvBXFzucm1twdyFybFqEA==",
      "dev": true,
      "license": "ISC",
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
    "node_modules/@isaacs/cliui/node_modules/ansi-regex": {
      "version": "6.2.2",
      "resolved": "https://registry.npmjs.org/ansi-regex/-/ansi-regex-6.2.2.tgz",
      "integrity": "sha512-Bq3SmSpyFHaWjPk8If9yc6svM8c56dB5BAtW4Qbw5jHTwwXXcTLoRMkpDJp6VL0XzlWaCHTXrkFURMYmD0sLqg==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/ansi-regex?sponsor=1"
      }
    },
    "node_modules/@isaacs/cliui/node_modules/strip-ansi": {
      "version": "7.2.0",
      "resolved": "https://registry.npmjs.org/strip-ansi/-/strip-ansi-7.2.0.tgz",
      "integrity": "sha512-yDPMNjp4WyfYBkHnjIRLfca1i6KMyGCtsVgoKe/z1+6vukgaENdgGBZt+ZmKPc4gavvEZ5OgHfHdrazhgNyG7w==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "ansi-regex": "^6.2.2"
      },
      "engines": {
        "node": ">=12"
      },
      "funding": {
        "url": "https://github.com/chalk/strip-ansi?sponsor=1"
      }
    },
    "node_modules/@jridgewell/gen-mapping": {
      "version": "0.3.13",
      "resolved": "https://registry.npmjs.org/@jridgewell/gen-mapping/-/gen-mapping-0.3.13.tgz",
      "integrity": "sha512-2kkt/7niJ6MgEPxF0bYdQ6etZaA+fQvDcLKckhy1yIQOzaoKjBBjSj63/aLVjYE3qhRt5dvM+uUyfCg6UKCBbA==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/sourcemap-codec": "^1.5.0",
        "@jridgewell/trace-mapping": "^0.3.24"
      }
    },
    "node_modules/@jridgewell/resolve-uri": {
      "version": "3.1.2",
      "resolved": "https://registry.npmjs.org/@jridgewell/resolve-uri/-/resolve-uri-3.1.2.tgz",
      "integrity": "sha512-bRISgCIjP20/tbWSPWMEi54QVPRZExkuD9lJL+UIxUKtwVJA8wW1Trb1jMs1RFXo1CBTNZ/5hpC9QvmKWdopKw==",
      "dev": true,
      "license": "MIT",
      "engines": {
        "node": ">=6.0.0"
      }
    },
    "node_modules/@jridgewell/sourcemap-codec": {
      "version": "1.5.5",
      "resolved": "https://registry.npmjs.org/@jridgewell/sourcemap-codec/-/sourcemap-codec-1.5.5.tgz",
      "integrity": "sha512-cYQ9310grqxueWbl+WuIUIaiUaDcj7WOq5fVhEljNVgRfOUhY9fy2zTvfoqWsnebh8Sl70VScFbICvJnLKB0Og==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/@jridgewell/trace-mapping": {
      "version": "0.3.31",
      "resolved": "https://registry.npmjs.org/@jridgewell/trace-mapping/-/trace-mapping-0.3.31.tgz",
      "integrity": "sha512-zzNR+SdQSDJzc8joaeP8QQoCQr8NuYx2dIIytl1QeBEZHJ9uW6hebsrYgbz8hJwUQao3TWCMtmfV8Nu1twOLAw==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "@jridgewell/resolve-uri": "^3.1.0",
        "@jridgewell/sourcemap-codec": "^1.4.14"
      }
    },
    "node_modules/@napi-rs/wasm-runtime": {
      "version": "0.2.12",
      "resolved": "https://registry.npmjs.org/@napi-rs/wasm-runtime/-/wasm-runtime-0.2.12.tgz",
      "integrity": "sha512-ZVWUcfwY4E/yPitQJl481FjFo3K22D6qF0DuFH6Y/nbnE11GY5uguDxZMGXPQ8WQ0128MXQD7TnfHyK4oWoIJQ==",
      "dev": true,
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "@emnapi/core": "^1.4.3",
        "@emnapi/runtime": "^1.4.3",
        "@tybys/wasm-util": "^0.10.0"
      }
    },
    "node_modules/@next/env": {
      "version": "14.2.35",
      "resolved": "https://registry.npmjs.org/@next/env/-/env-14.2.35.tgz",
      "integrity": "sha512-DuhvCtj4t9Gwrx80dmz2F4t/zKQ4ktN8WrMwOuVzkJfBilwAwGr6v16M5eI8yCuZ63H9TTuEU09Iu2HqkzFPVQ==",
      "license": "MIT"
    },
    "node_modules/@next/eslint-plugin-next": {
      "version": "14.2.35",
      "resolved": "https://registry.npmjs.org/@next/eslint-plugin-next/-/eslint-plugin-next-14.2.35.tgz",
      "integrity": "sha512-Jw9A3ICz2183qSsqwi7fgq4SBPiNfmOLmTPXKvlnzstUwyvBrtySiY+8RXJweNAs9KThb1+bYhZh9XWcNOr2zQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "glob": "10.3.10"
      }
    },
    "node_modules/@next/swc-darwin-arm64": {
      "version": "14.2.33",
      "resolved": "https://registry.npmjs.org/@next/swc-darwin-arm64/-/swc-darwin-arm64-14.2.33.tgz",
      "integrity": "sha512-HqYnb6pxlsshoSTubdXKu15g3iivcbsMXg4bYpjL2iS/V6aQot+iyF4BUc2qA/J/n55YtvE4PHMKWBKGCF/+wA==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 10"
      }
    },
    "node_modules/@next/swc-darwin-x64": {
      "version": "14.2.33",
      "resolved": "https://registry.npmjs.org/@next/swc-darwin-x64/-/swc-darwin-x64-14.2.33.tgz",
      "integrity": "sha512-8HGBeAE5rX3jzKvF593XTTFg3gxeU4f+UWnswa6JPhzaR6+zblO5+fjltJWIZc4aUalqTclvN2QtTC37LxvZAA==",
      "cpu": [
        "x64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">= 10"
      }
    },
    "node_modules/@next/swc-linux-arm64-gnu": {
      "version": "14.2.33",
      "resolved": "https://registry.npmjs.org/@next/swc-linux-arm64-gnu/-/swc-linux-arm64-gnu-14.2.33.tgz",
      "integrity": "sha512-JXMBka6lNNmqbkvcTtaX8Gu5by9547bukHQvPoLe9VRBx1gHwzf5tdt4AaezW85HAB3pikcvyqBToRTDA4DeLw==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 10"
      }
    },
    "node_modules/@next/swc-linux-arm64-musl": {
      "version": "14.2.33",
      "resolved": "https://registry.npmjs.org/@next/swc-linux-arm64-musl/-/swc-linux-arm64-musl-14.2.33.tgz",
      "integrity": "sha512-Bm+QulsAItD/x6Ih8wGIMfRJy4G73tu1HJsrccPW6AfqdZd0Sfm5Imhgkgq2+kly065rYMnCOxTBvmvFY1BKfg==",
      "cpu": [
        "arm64"
      ],
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">= 10"
      }
    },
    "node_modules/@next/swc-linux-x64-gnu": {
      "version": "14.2.33",
      "resolved": "https://registry.npmjs.org/@next/swc-linux-x64-gnu/-/swc-linux-x64-gnu-14.2.33.tgz",
      "integrity": "sha512-
# ... [TRUNCATED FILE CONTENT]
```


==================================================


## [2/3] Repository: Multi-Level-Order-Flow-Imbalance-And-Market-Cross-Impact (`WHEEL_Multi-Level-Order-Flow-Imbalance-And-Market-Cross-Impact`)
- **Full Name**: `Multi-Level-Order-Flow-Imbalance-And-Market-Cross-Impact`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# Multi Level Order Flow Imbalance And Market Cross Impact

## Overview
This repository contains the implementation of a quantitative study on **Order Flow Imbalance (OFI)** metrics and their impact on equity markets, focusing on:
- **Multi-level Limit Order Book (LOB)** dynamics.
- **Cross-asset impacts** and predictive modeling of price changes.

Key objectives:
1. Calculate **Order Flow Imbalance (OFI)** at multiple levels of the LOB.
2. Integrate OFI metrics using **Principal Component Analysis (PCA)**.
3. Analyze contemporaneous and lagged **cross-impact** between equities.
4. Evaluate the predictive power of OFI metrics on short-term price changes.

---

## Features
- **Data Preprocessing**: Scripts to clean, preprocess, and extract relevant LOB data.
- **OFI Metric Calculation**: Multi-level OFI computation for bid/ask sides.
- **Cross-Impact Analysis**: Regression-based analysis to measure cross-asset impacts.
- **Visualization**: Generate plots to illustrate trends, relationships, and findings.

---

## Directory Structure
```plaintext
.
├── data/               # Placeholder for raw and processed data
├── notebooks/          # Jupyter notebooks for exploration and analysis
├── scripts/            # Core Python scripts
├── results/            # Outputs (e.g., figures, tables, models)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── LICENSE             # License file

### Core Implementation Code & Architecture
#### File: `Scripts/blockhouse.py`
```python
# -*- coding: utf-8 -*-
"""BLOCKHOUSE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nPO_RjwpoaSoGv_o2IfAztnEcewBkB14

Step 1: PREPROCESSING
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, LassoCV
from sklearn.metrics import r2_score

# Function to calculate Multi-Level OFI

# Function to preprocess a single file
def preprocess_lob_data_fixed(file_path, levels=5):
    """
    Preprocess Limit Order Book (LOB) data with improved error handling.
    """
    # Load data
    lob_data = pd.read_csv(file_path)
    lob_data.columns = lob_data.columns.str.strip().str.lower()

    # Ensure timestamp column exists
    if 'ts_event' not in lob_data.columns:
        raise ValueError("Missing 'ts_event' column in data.")

    # Create timestamp and sort
    lob_data['timestamp'] = pd.to_datetime(lob_data['ts_event'])
    lob_data.sort_values(by='timestamp', inplace=True)

    # Fill missing values
    lob_data.fillna(method='ffill', inplace=True)
    lob_data.fillna(method='bfill', inplace=True)

    # Select relevant columns
    level_columns = ['timestamp']
    for i in range(1, levels + 1):
        level_columns.extend([f'bid_px_0{i}', f'bid_sz_0{i}', f'ask_px_0{i}', f'ask_sz_0{i}'])

    valid_columns = [col for col in level_columns if col in lob_data.columns]
    filtered_data = lob_data[valid_columns]

    # Ensure data is not empty
    if filtered_data.empty:
        print("Warning: Filtered dataset is empty. Returning original dataset.")
        return lob_data

    return filtered_data

# Define file paths for the uploaded datasets
file_paths = {
    "AAPL": "/content/AAPL.csv",
    "AMGN": "/content/AMGN.csv",
    "JPM": "/content/JPM.csv",
    "TSLA": "/content/TSLA.csv",
    "XOM": "/content/XOM.csv"
}

# Preprocess all files and save the cleaned data
processed_data = {}
for stock, path in file_paths.items():
    processed_data[stock] = preprocess_lob_data_fixed(path)
    # Save each processed file
    processed_data[stock].to_csv(f"/content/Processed/Processed_{stock}.csv", index=False)

print("Processing complete. Processed files saved.")

"""Step 2: Compute OFI Metrics"""

def calculate_ofi(data):
    """
    Calculate Order Flow Imbalance (OFI) for bid and ask sides at 5 levels.
    Args:
        data (pd.DataFrame): Processed LOB data with bid and ask prices/sizes.
    Returns:
        pd.DataFrame: Data with OFI columns added for all 5 levels.
    """
    for level in range(1, 6):  # For levels 1 to 5
        bid_price_col = f'bid_px_0{level}'
        bid_size_col = f'bid_sz_0{level}'
        ask_price_col = f'ask_px_0{level}'
        ask_size_col = f'ask_sz_0{level}'

        # Calculate bid-side OFI
        data[f'ofi_bid_{level}'] = np.where(
            data[bid_price_col] > data[bid_price_col].shift(1),
            data[bid_size_col],
            np.where(
                data[bid_price_col] == data[bid_price_col].shift(1),
                data[bid_size_col] - data[bid_size_col].shift(1),
                -data[bid_size_col]
            )
        )

        # Calculate ask-side OFI
        data[f'ofi_ask_{level}'] = np.where(
            data[ask_price_col] > data[ask_price_col].shift(1),
            -data[ask_size_col],
            np.where(
                data[ask_price_col] == data[ask_price_col].shift(1),
                data[ask_size_col] - data[ask_size_col].shift(1),
                data[ask_size_col]
            )
        )

    return data
# Function to integrate Multi-Level OFI using PCA
def integrate_ofi_with_pca(data):
    """
    Integrate multi-level OFI using PCA.
    Args:
        data (pd.DataFrame): LOB data with OFI columns for each level.
    Returns:
        pd.DataFrame: Data with integrated OFI column added.
    """
    ofi_columns = [f'ofi_bid_{i}' for i in range(1, 6)] + [f'ofi_ask_{i}' for i in range(1, 6)]

    # Ensure the columns exist and are valid
    ofi_columns = [col for col in ofi_columns if col in data.columns]
    if not ofi_columns:
        raise ValueError("No valid OFI columns found for PCA integration.")

    # Fill NaN values with 0 for PCA
    ofi_data = data[ofi_columns].fillna(0)

    # Check if there are enough rows for PCA
    if ofi_data.shape[0] < 1:
        raise ValueError("No data available for PCA integration. Check input dataset.")

    # Apply PCA
    pca = PCA(n_components=1)
    integrated_ofi = pca.fit_transform(ofi_data)
    data['ofi_integrated'] = integrated_ofi
    return data

# Example Usage: Calculate OFI for all stocks
processed_data_with_ofi = {}
for stock, df in processed_data.items():
    df = calculate_ofi(df)
    df = integrate_ofi_with_pca(df)
    processed_data_with_ofi[stock] = df

"""Step 3: Analyze Cross-Impact"""

# Step 1: Add Returns Calculation to Preprocessing
def calculate_returns(data):
    mid_price = (data['bid_px_01'] + data['ask_px_01']) / 2
    returns = mid_price.pct_change().fillna(0)
    return returns

for stock, df in processed_data_with_ofi.items():
    df['returns'] = calculate_returns(df)

# Step 2: Analyze Contemporaneous Cross-Impact
def analyze_cross_impact(processed_data):
    stock_names = list(processed_data.keys())
    integrated_ofis = {stock: df['ofi_integrated'] for stock, df in processed_data.items()}
    returns = {stock: df['returns'] for stock, df in processed_data.items()}

    # Create a matrix of OFIs and returns
    X = np.column_stack([integrated_ofis[stock] for stock in stock_names])
    y = np.column_stack([returns[stock] for stock in stock_names])

    # Linear regression for cross-impact
    model = LinearRegression()
    model.fit(X, y)
    cross_impact_coefficients = pd.DataFrame(model.coef_, columns=stock_names, index=stock_names)
    return cross_impact_coefficients

cross_impact_coefficients = analyze_cross_impact(processed_data_with_ofi)

# Step 3: Evaluate Predictive Power
def predictive_power(processed_data, lag=1):
    results = {}
    for stock, df in processed_data.items():
        X = df['ofi_integrated'].shift(lag).fillna(0).values.reshape(-1, 1)
        y = df['returns'].values

        model = LassoCV(cv=5)
        model.fit(X, y)
        predictions = model.predict(X)
        results[stock] = r2_score(y, predictions)
    return results

predictive_r2 = predictive_power(processed_data_with_ofi)

# Step 4: Print Results
print("Cross-Impact Coefficients:")
print(cross_impact_coefficients)

print("Predictive R-Squared Values:")
print(predictive_r2)

"""Step 4: Quantify Results"""

# Print R-squared values for predictive power
print("R-squared values for predictive models:")
print(predictive_r2)

# Compare cross-impact coefficients
print("Cross-impact coefficients:")
print(cross_impact_coefficients)

"""Step 5: Visualize Results"""

# Plot OFI trends for a stock
def plot_ofi_trends(stock, df):
    plt.figure(figsize=(10, 6))
    for level in range(1, 6):
        plt.plot(df['timestamp'], df[f'ofi_bid_{level}'], label=f'Bid Level {level}')
        plt.plot(df['timestamp'], df[f'ofi_ask_{level}'], label=f'Ask Level {level}')
    plt.title(f"OFI Trends for {stock}")
    plt.xlabel("Time")
    plt.ylabel("OFI")
    plt.legend()
    plt.show()

plot_ofi_trends("AAPL", processed_data_with_ofi["AAPL"])
plot_ofi_trends("AMGN", processed_data_with_ofi["AMGN"])
plot_ofi_trends("JPM", processed_data_with_ofi["JPM"])
plot_ofi_trends("TSLA", processed_data_with_ofi["TSLA"])
plot_ofi_trends("XOM", processed_data_with_ofi["XOM"])

# Heatmap for cross-impact relationships
sns.heatmap(cross_impact_coefficients, annot=True, cmap='coolwarm')
plt.title("Cross-Impact Coefficients")
plt.show()
```

#### File: `Notebook/blockhouse.py`
```python
# -*- coding: utf-8 -*-
"""BLOCKHOUSE.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nPO_RjwpoaSoGv_o2IfAztnEcewBkB14

Step 1: PREPROCESSING
"""

import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression, LassoCV
from sklearn.metrics import r2_score

# Function to calculate Multi-Level OFI

# Function to preprocess a single file
def preprocess_lob_data_fixed(file_path, levels=5):
    """
    Preprocess Limit Order Book (LOB) data with improved error handling.
    """
    # Load data
    lob_data = pd.read_csv(file_path)
    lob_data.columns = lob_data.columns.str.strip().str.lower()

    # Ensure timestamp column exists
    if 'ts_event' not in lob_data.columns:
        raise ValueError("Missing 'ts_event' column in data.")

    # Create timestamp and sort
    lob_data['timestamp'] = pd.to_datetime(lob_data['ts_event'])
    lob_data.sort_values(by='timestamp', inplace=True)

    # Fill missing values
    lob_data.fillna(method='ffill', inplace=True)
    lob_data.fillna(method='bfill', inplace=True)

    # Select relevant columns
    level_columns = ['timestamp']
    for i in range(1, levels + 1):
        level_columns.extend([f'bid_px_0{i}', f'bid_sz_0{i}', f'ask_px_0{i}', f'ask_sz_0{i}'])

    valid_columns = [col for col in level_columns if col in lob_data.columns]
    filtered_data = lob_data[valid_columns]

    # Ensure data is not empty
    if filtered_data.empty:
        print("Warning: Filtered dataset is empty. Returning original dataset.")
        return lob_data

    return filtered_data

# Define file paths for the uploaded datasets
file_paths = {
    "AAPL": "/content/AAPL.csv",
    "AMGN": "/content/AMGN.csv",
    "JPM": "/content/JPM.csv",
    "TSLA": "/content/TSLA.csv",
    "XOM": "/content/XOM.csv"
}

# Preprocess all files and save the cleaned data
processed_data = {}
for stock, path in file_paths.items():
    processed_data[stock] = preprocess_lob_data_fixed(path)
    # Save each processed file
    processed_data[stock].to_csv(f"/content/Processed/Processed_{stock}.csv", index=False)

print("Processing complete. Processed files saved.")

"""Step 2: Compute OFI Metrics"""

def calculate_ofi(data):
    """
    Calculate Order Flow Imbalance (OFI) for bid and ask sides at 5 levels.
    Args:
        data (pd.DataFrame): Processed LOB data with bid and ask prices/sizes.
    Returns:
        pd.DataFrame: Data with OFI columns added for all 5 levels.
    """
    for level in range(1, 6):  # For levels 1 to 5
        bid_price_col = f'bid_px_0{level}'
        bid_size_col = f'bid_sz_0{level}'
        ask_price_col = f'ask_px_0{level}'
        ask_size_col = f'ask_sz_0{level}'

        # Calculate bid-side OFI
        data[f'ofi_bid_{level}'] = np.where(
            data[bid_price_col] > data[bid_price_col].shift(1),
            data[bid_size_col],
            np.where(
                data[bid_price_col] == data[bid_price_col].shift(1),
                data[bid_size_col] - data[bid_size_col].shift(1),
                -data[bid_size_col]
            )
        )

        # Calculate ask-side OFI
        data[f'ofi_ask_{level}'] = np.where(
            data[ask_price_col] > data[ask_price_col].shift(1),
            -data[ask_size_col],
            np.where(
                data[ask_price_col] == data[ask_price_col].shift(1),
                data[ask_size_col] - data[ask_size_col].shift(1),
                data[ask_size_col]
            )
        )

    return data
# Function to integrate Multi-Level OFI using PCA
def integrate_ofi_with_pca(data):
    """
    Integrate multi-level OFI using PCA.
    Args:
        data (pd.DataFrame): LOB data with OFI columns for each level.
    Returns:
        pd.DataFrame: Data with integrated OFI column added.
    """
    ofi_columns = [f'ofi_bid_{i}' for i in range(1, 6)] + [f'ofi_ask_{i}' for i in range(1, 6)]

    # Ensure the columns exist and are valid
    ofi_columns = [col for col in ofi_columns if col in data.columns]
    if not ofi_columns:
        raise ValueError("No valid OFI columns found for PCA integration.")

    # Fill NaN values with 0 for PCA
    ofi_data = data[ofi_columns].fillna(0)

    # Check if there are enough rows for PCA
    if ofi_data.shape[0] < 1:
        raise ValueError("No data available for PCA integration. Check input dataset.")

    # Apply PCA
    pca = PCA(n_components=1)
    integrated_ofi = pca.fit_transform(ofi_data)
    data['ofi_integrated'] = integrated_ofi
    return data

# Example Usage: Calculate OFI for all stocks
processed_data_with_ofi = {}
for stock, df in processed_data.items():
    df = calculate_ofi(df)
    df = integrate_ofi_with_pca(df)
    processed_data_with_ofi[stock] = df

"""Step 3: Analyze Cross-Impact"""

# Step 1: Add Returns Calculation to Preprocessing
def calculate_returns(data):
    mid_price = (data['bid_px_01'] + data['ask_px_01']) / 2
    returns = mid_price.pct_change().fillna(0)
    return returns

for stock, df in processed_data_with_ofi.items():
    df['returns'] = calculate_returns(df)

# Step 2: Analyze Contemporaneous Cross-Impact
def analyze_cross_impact(processed_data):
    stock_names = list(processed_data.keys())
    integrated_ofis = {stock: df['ofi_integrated'] for stock, df in processed_data.items()}
    returns = {stock: df['returns'] for stock, df in processed_data.items()}

    # Create a matrix of OFIs and returns
    X = np.column_stack([integrated_ofis[stock] for stock in stock_names])
    y = np.column_stack([returns[stock] for stock in stock_names])

    # Linear regression for cross-impact
    model = LinearRegression()
    model.fit(X, y)
    cross_impact_coefficients = pd.DataFrame(model.coef_, columns=stock_names, index=stock_names)
    return cross_impact_coefficients

cross_impact_coefficients = analyze_cross_impact(processed_data_with_ofi)

# Step 3: Evaluate Predictive Power
def predictive_power(processed_data, lag=1):
    results = {}
    for stock, df in processed_data.items():
        X = df['ofi_integrated'].shift(lag).fillna(0).values.reshape(-1, 1)
        y = df['returns'].values

        model = LassoCV(cv=5)
        model.fit(X, y)
        predictions = model.predict(X)
        results[stock] = r2_score(y, predictions)
    return results

predictive_r2 = predictive_power(processed_data_with_ofi)

# Step 4: Print Results
print("Cross-Impact Coefficients:")
print(cross_impact_coefficients)

print("Predictive R-Squared Values:")
print(predictive_r2)

"""Step 4: Quantify Results"""

# Print R-squared values for predictive power
print("R-squared values for predictive models:")
print(predictive_r2)

# Compare cross-impact coefficients
print("Cross-impact coefficients:")
print(cross_impact_coefficients)

"""Step 5: Visualize Results"""

# Plot OFI trends for a stock
def plot_ofi_trends(stock, df):
    plt.figure(figsize=(10, 6))
    for level in range(1, 6):
        plt.plot(df['timestamp'], df[f'ofi_bid_{level}'], label=f'Bid Level {level}')
        plt.plot(df['timestamp'], df[f'ofi_ask_{level}'], label=f'Ask Level {level}')
    plt.title(f"OFI Trends for {stock}")
    plt.xlabel("Time")
    plt.ylabel("OFI")
    plt.legend()
    plt.show()

plot_ofi_trends("AAPL", processed_data_with_ofi["AAPL"])
plot_ofi_trends("AMGN", processed_data_with_ofi["AMGN"])
plot_ofi_trends("JPM", processed_data_with_ofi["JPM"])
plot_ofi_trends("TSLA", processed_data_with_ofi["TSLA"])
plot_ofi_trends("XOM", processed_data_with_ofi["XOM"])

# Heatmap for cross-impact relationships
sns.heatmap(cross_impact_coefficients, annot=True, cmap='coolwarm')
plt.title("Cross-Impact Coefficients")
plt.show()
```


==================================================


## [3/3] Repository: OFI (`WHEEL_OFI`)
- **Full Name**: `OFI`
- **Description**: 
- **GitHub Stars**: 0
- **Source Pool**: `cloned_trading_wheels`

### Documentation & Overview (README.md)
# OFI

This project constructs the various versions of Order Flow Imbalance (OFI) features defined in the article below.

Rama Cont, Mihai Cucuringu & Chao Zhang (2023) Cross-impact of
order flow imbalance in equity markets, Quantitative Finance, 23:10, 1373-1393, DOI:
10.1080/14697688.2023.2236159

To apply the construction in the code, use/modify the following sample command in terminal:

python ofi_features.py first_25000_rows.csv AAPL 2024-10-21T11:55:00Z --window 1s

### Core Implementation Code & Architecture
#### File: `ofi_features.py`
```python
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from typing import Dict, List, Tuple, Union
Symbol = str
Timestamp = pd.Timestamp

class OFICalculator:
    def __init__(
        self,
        *,
        depth: int = 10,
        window: pd.Timedelta = pd.Timedelta("1s"),   # window = h as in (t, t+h]
        pca_history: pd.Timedelta = pd.Timedelta("1D"),
    ) -> None:
        self.depth = depth
        self.window = window
        self.pca_history = pca_history

        # last LOB snapshot
        self._snap: Dict[Symbol, Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]] = {}

        # current OFI accumulator
        self._accum: Dict[Symbol, np.ndarray] = {}
        # right edge of current window
        self._win_end: Dict[Symbol, Timestamp] = {}

        # for PCA weight estimation 
        self._pca_buf: List[Tuple[Symbol, Timestamp, np.ndarray]] = []
        self._pca_w: Dict[Symbol, np.ndarray] = {}

    # ---------------------------------------------------------------------

    def _roll_window(self, sym: Symbol, ts: Timestamp) -> None:
        """Locate time window that encloses *ts*."""
        if sym not in self._win_end:
            # first appearance → align window_end to the *ceiling* multiple of `window`
            base = pd.Timestamp.floor(ts + self.window, freq=self.window)
            self._win_end[sym] = base
            self._accum[sym] = np.zeros(self.depth)
        while ts > self._win_end[sym]:
            # step to next bucket
            self._win_end[sym] += self.window
            self._accum[sym][...] = 0.0  # reset

    # ---------------------------------------------------------------------

    def ingest_row(self, row: pd.Series) -> None:
        """Process a single post‑event LOB row."""
        ts = pd.to_datetime(row["ts_event"])
        sym: Symbol = row["symbol"]

        bid_px = np.array([row[f"bid_px_{i:02d}"] for i in range(self.depth)])
        ask_px = np.array([row[f"ask_px_{i:02d}"] for i in range(self.depth)])
        bid_sz = np.array([row[f"bid_sz_{i:02d}"] for i in range(self.depth)])
        ask_sz = np.array([row[f"ask_sz_{i:02d}"] for i in range(self.depth)])

        
        if sym in self._snap:
            l_bid_px, l_ask_px, l_bid_sz, l_ask_sz = self._snap[sym]
            omega = np.zeros(self.depth)
            for m in range(self.depth):
                # bid side
                if bid_px[m] > l_bid_px[m]:
                    ofib = bid_sz[m]
                elif bid_px[m] == l_bid_px[m]:
                    ofib = bid_sz[m] - l_bid_sz[m]
                else:
                    ofib = -l_bid_sz[m]
                # ask side
                if ask_px[m] > l_ask_px[m]:
                    ofia = -ask_sz[m]
                elif ask_px[m] == l_ask_px[m]:
                    ofia = ask_sz[m] - l_ask_sz[m]
                else:
                    ofia = l_ask_sz[m]
                omega[m] = ofib - ofia
            # accumulate into current time window
            self._roll_window(sym, ts)
            self._accum[sym] += omega
            # store omega for PCA
            self._pca_buf.append((sym, ts, omega))
        
        self._snap[sym] = (bid_px, ask_px, bid_sz, ask_sz)

    # ---------------------------------------------------------------------

    def finalize_interval(self, *, horizon_end: Timestamp) -> None:
        """Re‑estimate PCA weights on the buffer up to *horizon_end*."""
        if not self._pca_buf:
            return
        cutoff = horizon_end - self.pca_history
        # slice buffer to the last day
        recent = [(s, t, v) for (s, t, v) in self._pca_buf if t >= cutoff]
        self._pca_buf = recent  # prune old rows
        if not recent:
            return
        df = (
            pd.DataFrame(
                {"symbol": s, "ts": t, **{f"lvl_{i}": v[i] for i in range(self.depth)}}
                for s, t, v in recent
            )
            .groupby("symbol")
        )
        for sym, grp in df:
            X = grp[[f"lvl_{i}" for i in range(self.depth)]].values
            if len(X) < 10:
                continue
            # run PCA for integrated ofi
            pca = PCA(n_components=1)
            pca.fit(X)
            w = pca.components_[0]
            w /= np.sum(np.abs(w))
            self._pca_w[sym] = w

    # ---------------------------------------------------------------------
    
    def get_features(self, symbol: Symbol, timestamp: Timestamp) -> Dict[str, Union[float, np.ndarray]]:
        """Return OFI features aggregated over (t‑h, t] with *t = timestamp*."""
        if symbol not in self._accum:
            raise KeyError(f"No data for symbol {symbol}")
        # ensure `timestamp` is within the current bucket for symbol
        self._roll_window(symbol, timestamp)
        if timestamp > self._win_end[symbol]:
            raise RuntimeError("Timestamp beyond ingested data – call ingest_row first")

        # use definitions of the ofi features
        vec = self._accum[symbol].copy()
        best = float(vec[0]) 
        w = self._pca_w.get(symbol)
        integrated = float(np.dot(w, vec)) if w is not None else best
        # cross‑asset best‑level
        cross = sum(self._accum[s][0] for s in self._accum if s != symbol)
        return {
            "best_level_ofi": best,
            "multi_level_ofi": vec,
            "integrated_ofi": integrated,
            "cross_asset_ofi": float(cross),
        }

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

def compute_features_for_timestamp(
    book_df: pd.DataFrame,
    ts: Union[str, Timestamp],
    *,
    symbol: str,
    depth: int = 10,
    window: str | pd.Timedelta = "1s",
) -> Dict[str, Union[float, np.ndarray]]:
    ts = pd.to_datetime(ts)
    window = pd.Timedelta(window)

    calc = OFICalculator(depth=depth, window=window)
    for _, row in book_df.sort_values("ts_event").iterrows():
        calc.ingest_row(row)
        if pd.to_datetime(row["ts_event"]) >= ts:
            break
    calc.finalize_interval(horizon_end=ts)
    return calc.get_features(symbol, ts)

# ---------------------------------------------------------------------
# ---------------------------------------------------------------------

if __name__ == "__main__":
    import argparse, textwrap, json

    parser = argparse.ArgumentParser(
        description="Compute OFI features aggregated over (t‑h,t] for a single timestamp.",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("csv", help="LOB snapshot CSV (post‑event rows)")
    parser.add_argument("symbol", help="Ticker symbol, e.g. AAPL")
    parser.add_argument("timestamp", help="End‑of‑window timestamp (ISO‑8601)")
    parser.add_argument("--window", default="1s", help="Aggregation window, e.g. 1s 500ms 5min (default 1s)")
    parser.add_argument("--depth", type=int, default=10, help="LOB depth to use (default 10)")
    args = parser.parse_args()

    df = pd.read_csv(args.csv)
    feats = compute_features_for_timestamp(
        df,
        args.timestamp,
        symbol=args.symbol,
        depth=args.depth,
        window=args.window,
    )
    # json style output
    print(json.dumps({k: (v.tolist() if isinstance(v, np.ndarray) else v) for k, v in feats.items()}, indent=2))

"""
Sample usage in terminal:
python ofi_features.py first_25000_rows.csv AAPL 2024-10-21T11:55:00Z --window 1s
"""
```


==================================================
