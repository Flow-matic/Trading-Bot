from web3 import Web3

# Set up Web3 connection (using Binance Smart Chain RPC URL)
rpc_url = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Check if connected
if web3.is_connected():
    print("Connected to Binance Smart Chain")
else:
    print("Failed to connect to Binance Smart Chain")

# Test web3.toWei method
try:
    amount_in_wei = web3.toWei(1, 'ether')  # Convert 1 ether to Wei
    print(f"1 Ether is {amount_in_wei} Wei")
except AttributeError as e:
    print(f"Error: {e}")
