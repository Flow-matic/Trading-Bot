import requests
import time

# Replace with your API keys and secrets
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

# Main bot function
def trading_bot():
    crypto_symbol = "BNBUSDT"  # Corrected symbol for Binance Coin in USD
    start_time = time.time()
    duration = 120  # Time in seconds to collect data
    while time.time() - start_time < duration:
        # Fetch cryptocurrency data
        crypto_price = fetch_crypto_data(crypto_symbol)
        if crypto_price is not None:
            print(f"Cryptocurrency ({crypto_symbol}) Price: {crypto_price}")

        time.sleep(10)  # Adjust the frequency as needed

if __name__ == "__main__":
    trading_bot()

