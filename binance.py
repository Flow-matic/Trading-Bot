from web3 import Web3
import requests
import time

# Binance Smart Chain (BSC) RPC URL
BSC_RPC = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(BSC_RPC))

# PancakeSwap Prediction Contract (Mainnet)
PREDICTION_CONTRACT_ADDRESS = "0x18B2A687610328590Bc8F2e5fEdDe3b582A49cdA"
PREDICTION_ABI = "https://raw.githubusercontent.com/pancakeswap/pancake-frontend/master/src/config/abi/prediction.json"

# Fetch the Prediction Contract ABI
response = requests.get(PREDICTION_ABI)
prediction_abi = response.json()
prediction_contract = web3.eth.contract(address=PREDICTION_CONTRACT_ADDRESS, abi=prediction_abi)

# Fetch Current Epoch
def fetch_current_epoch():
    try:
        current_epoch = prediction_contract.functions.currentEpoch().call()
        return current_epoch
    except Exception as e:
        print(f"Error fetching current epoch: {e}")
        return None

# Fetch Round Data
def fetch_round_data(epoch):
    try:
        round_data = prediction_contract.functions.rounds(epoch).call()
        return {
            "epoch": round_data[0],
            "start_time": round_data[1],
            "lock_time": round_data[2],
            "close_time": round_data[3],
            "lock_price": web3.fromWei(round_data[4], 'ether'),
            "close_price": web3.fromWei(round_data[5], 'ether'),
            "total_amount": web3.fromWei(round_data[8], 'ether'),
            "bull_amount": web3.fromWei(round_data[9], 'ether'),
            "bear_amount": web3.fromWei(round_data[10], 'ether'),
        }
    except Exception as e:
        print(f"Error fetching round data: {e}")
        return None

# Monitor Real-Time Data
def monitor_prediction():
    while True:
        current_epoch = fetch_current_epoch()
        if current_epoch:
            print(f"Current Epoch: {current_epoch}")
            round_data = fetch_round_data(current_epoch)
            if round_data:
                print(f"Round Data: {round_data}")
        time.sleep(5)

if __name__ == "__main__":
    monitor_prediction()