# Cryptocurrency and Forex Trading Bot

## Overview
This trading bot collects real-time cryptocurrency and forex market data and allows for further customization to implement trading strategies. It fetches data using:

- **Cryptocurrency Data**: Binance API
- **Forex Data**: Alpha Vantage API

The bot can be configured to run for a specific duration and supports adding trading logic like buy/sell signals.

---

## Features
1. **Real-Time Data Fetching**:
   - Cryptocurrency prices from Binance.
   - Forex exchange rates from Alpha Vantage.

2. **Customizable Duration**:
   - You can specify how long the bot collects data by changing the `duration` variable.

3. **Trading Strategy**:
   - Placeholder section for implementing buy/sell strategies based on fetched data.

4. **Error Handling**:
   - Includes basic exception handling to manage API errors or invalid responses.

---

## Requirements
### Prerequisites
- Python 3.6 or later
- Libraries: `requests`

### Installation
1. Install Python dependencies:
   ```bash
   pip install requests
   ```

2. Obtain API keys:
   - Binance API key (optional for public price data).
   - Alpha Vantage API key (sign up at [Alpha Vantage](https://www.alphavantage.co/)).

---

## Configuration
1. Replace placeholders in the code:
   - `your_alpha_vantage_api_key`: Add your Alpha Vantage API key.

2. Set desired trading pairs:
   - Cryptocurrency pair:
     ```python
     crypto_symbol = "BTCUSDT"  # Replace with your desired cryptocurrency pair
     ```
   - Forex pair:
     ```python
     forex_pair = "EUR/USD"  # Replace with your desired forex pair
     ```

3. Set data collection duration (in seconds):
   ```python
   duration = 5  # Time in seconds to collect data
   ```

---

## Usage
1. Save the script as `trading_bot.py`.
2. Run the bot in the terminal:
   ```bash
   python trading_bot.py
   ```
3. Monitor real-time data output in the terminal:
   ```
   Cryptocurrency (BTCUSDT) Price: 43200.0
   Forex (EUR/USD) Exchange Rate: 1.1250
   ```

---

## Future Improvements
- Add automated trade execution.
- Enhance error handling with logging.
- Integrate advanced strategies and technical indicators.
- Support more APIs or brokers for expanded coverage.

---

## Disclaimer
This bot is for educational purposes only. It does not include live trading functionality and is not intended for financial advice or use in real trading without further testing and risk management.

