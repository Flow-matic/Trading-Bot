import requests
import time

# Replace with your API keys and secrets
CRYPTO_API_URL = "https://api.binance.com/api/v3/ticker/price"
FOREX_API_URL = "https://www.alphavantage.co/query"
FOREX_API_KEY = "your_alpha_vantage_api_key"

# Fetch real-time cryptocurrency data
def fetch_crypto_data(symbol):
    try:
        response = requests.get(CRYPTO_API_URL, params={"symbol": symbol})
        response.raise_for_status()
        data = response.json()
        price = float(data["price"])
        return price
    except Exception as e:
        print(f"Error fetching cryptocurrency data: {e}")
        return None

# Fetch real-time forex data
def fetch_forex_data(pair):
    try:
        response = requests.get(FOREX_API_URL, params={
            "function": "CURRENCY_EXCHANGE_RATE",
            "from_currency": pair.split('/')[0],
            "to_currency": pair.split('/')[1],
            "apikey": FOREX_API_KEY
        })
        response.raise_for_status()
        data = response.json()
        rate = float(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])
        return rate
    except Exception as e:
        print(f"Error fetching forex data: {e}")
        return None

# Main bot function
def trading_bot():
    crypto_symbol = "BTCUSDT"  # Replace with your desired cryptocurrency pair
    forex_pair = "EUR/USD"  # Replace with your desired forex pair

    start_time = time.time()
    duration = 5  # Time in seconds to collect data
    while time.time() - start_time < duration:
        # Fetch cryptocurrency data
        crypto_price = fetch_crypto_data(crypto_symbol)
        if crypto_price is not None:
            print(f"Cryptocurrency ({crypto_symbol}) Price: {crypto_price}")

        # Fetch forex data
        forex_rate = fetch_forex_data(forex_pair)
        if forex_rate is not None:
            print(f"Forex ({forex_pair}) Exchange Rate: {forex_rate}")

        # Implement your trading strategy here
        # For example, if crypto_price < threshold, buy; if forex_rate > threshold, sell

        time.sleep(10)  # Adjust the frequency as needed

if __name__ == "__main__":
    trading_bot()