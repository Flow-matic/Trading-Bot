from web3 import Web3
import requests
import time

# Binance Smart Chain (BSC) RPC URL
BSC_RPC = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(BSC_RPC))

# Check Web3 connection
if not web3.is_connected():
    print("Failed to connect to Binance Smart Chain.")
    exit()

print("Connected to Binance Smart Chain.")

# PancakeSwap Prediction Contract for BNBUSD (Mainnet)
BNBUSD_CONTRACT_ADDRESS = "0x18B2A687610328590Bc8F2e5fEdDe3b582A49cdA"

# Manually define the ABI for the contract
BNBUSD_ABI = [
    {
        "inputs": [],
        "name": "currentEpoch",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "rounds",
        "outputs": [
            {"internalType": "uint256", "name": "epoch", "type": "uint256"},
            {"internalType": "uint256", "name": "startTime", "type": "uint256"},
            {"internalType": "uint256", "name": "lockTime", "type": "uint256"},
            {"internalType": "uint256", "name": "closeTime", "type": "uint256"},
            {"internalType": "uint256", "name": "lockPrice", "type": "uint256"},
            {"internalType": "uint256", "name": "closePrice", "type": "uint256"},
            {"internalType": "uint256", "name": "totalAmount", "type": "uint256"},
            {"internalType": "uint256", "name": "bullAmount", "type": "uint256"},
            {"internalType": "uint256", "name": "bearAmount", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]

bnbusd_contract = web3.eth.contract(address=BNBUSD_CONTRACT_ADDRESS, abi=BNBUSD_ABI)

# Binance API for CAKEUSD Price Data
BINANCE_API_URL = "https://api.binance.com/api/v3/ticker/price"

# Fetch BNBUSD Prediction Round Data
def fetch_bnbusd_round_data(epoch):
    try:
        round_data = bnbusd_contract.functions.rounds(epoch).call()
        return {
            "epoch": round_data[0],
            "start_time": round_data[1],
            "lock_time": round_data[2],
            "close_time": round_data[3],
            "lock_price": web3.from_wei(round_data[4], "ether"),
            "close_price": web3.from_wei(round_data[5], "ether"),
            "total_amount": web3.from_wei(round_data[6], "ether"),
            "bull_amount": web3.from_wei(round_data[7], "ether"),
            "bear_amount": web3.from_wei(round_data[8], "ether"),
        }
    except Exception as e:
        print(f"Error fetching BNBUSD round data: {e}")
        return None

# Fetch CAKEUSD Price from Binance API
def fetch_cakeusd_price():
    try:
        response = requests.get(BINANCE_API_URL, params={"symbol": "CAKEUSDT"})
        response.raise_for_status()
        data = response.json()
        price = float(data["price"])
        return price
    except Exception as e:
        print(f"Error fetching CAKEUSD price: {e}")
        return None

# Monitor Data for BNBUSD and CAKEUSD
def monitor_bnbusd_and_cakeusd():
    while True:
        try:
            # Fetch Current Epoch for BNBUSD Prediction Market
            current_epoch = bnbusd_contract.functions.currentEpoch().call()
            print(f"Current BNBUSD Epoch: {current_epoch}")

            bnbusd_data = fetch_bnbusd_round_data(current_epoch)
            if bnbusd_data:
                print(f"BNBUSD Round Data: {bnbusd_data}")

            # Fetch CAKEUSD Price
            cakeusd_price = fetch_cakeusd_price()
            if cakeusd_price:
                print(f"CAKEUSD Price: {cakeusd_price}")

        except KeyboardInterrupt:
            print("Monitoring stopped by user.")
            break
        except Exception as e:
            print(f"Unexpected error: {e}")

        time.sleep(5)

if __name__ == "__main__":
    monitor_bnbusd_and_cakeusd()

