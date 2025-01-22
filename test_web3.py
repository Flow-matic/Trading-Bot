from web3 import Web3

# Binance Smart Chain RPC URL
rpc_url = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Check if connection is successful
if web3.is_connected():
    print("Connected to Binance Smart Chain")
else:
    print("Failed to connect to Binance Smart Chain")

# Custom middleware to handle POA chains (such as Binance Smart Chain)
def inject_poa_middleware(web3):
    # Replace the following code with the middleware logic
    # which handles POA chains (adjusted for web3.py v7.7.0)
    web3.provider.middlewares.stack.inject(
        lambda _, request: request.update({'method': 'eth_call'}), layer=0
    )

# Inject the middleware for POA support
inject_poa_middleware(web3)
