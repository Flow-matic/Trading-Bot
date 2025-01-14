import requests
import time

# Binance API URL
CRYPTO_API_URL = "https://api.binance.com/api/v3/ticker/price"

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

# Main bot function for cryptocurrency data
def crypto_trading_bot():
    crypto_symbol = "XRPUSDT"  # Replace with your desired cryptocurrency pair

    start_time = time.time()
    duration = 22  # Time in seconds to collect data
    while time.time() - start_time < duration:
        # Fetch cryptocurrency data
        crypto_price = fetch_crypto_data(crypto_symbol)
        if crypto_price is not None:
            print(f"Cryptocurrency ({crypto_symbol}) Price: {crypto_price}")

        # Implement your trading strategy here
        # For example, if crypto_price < threshold, buy; if crypto_price > threshold, sell

        time.sleep(10)  # Adjust the frequency as needed

if __name__ == "__main__":
    crypto_trading_bot()