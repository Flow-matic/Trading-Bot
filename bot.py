from web3 import Web3
import time

# Use Binance Smart Chain (BSC) RPC URL or Infura/Alchemy if needed
rpc_url = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(rpc_url))

# Check if the connection is successful
if web3.is_connected():
    print("Connected to Binance Smart Chain")
else:
    print("Failed to connect to Binance Smart Chain")

# Replace with actual PancakeSwap prediction market contract address and ABI
CONTRACT_ADDRESS = "0x18B2A687610328590Bc8F2e5fEdDe3b582A49cdA"  # Replace with the actual contract address
ABI = [
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

# Set up the contract
contract = web3.eth.contract(address=web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)

# Function to fetch historical round data
def fetch_historical_round_data(round_count=10):
    rounds = []
    current_epoch = contract.functions.currentEpoch().call()
    
    for epoch in range(current_epoch - round_count, current_epoch):
        try:
            round_data = contract.functions.rounds(epoch).call()
            rounds.append(round_data)
            print(f"Fetched round {epoch}: {round_data}")
        except Exception as e:
            print(f"Error fetching data for round {epoch}: {e}")
    
    return rounds

# Logic for making predictions based on historical data
def make_prediction(rounds):
    # Placeholder logic: Simple strategy based on past price movements
    # You can replace this with more sophisticated analysis
    
    prediction = "bull"  # Default prediction is "bull"
    
    if rounds:
        last_round = rounds[-1]
        prev_round = rounds[-2] if len(rounds) > 1 else None
        
        # If price closed higher in the last round than the previous round, predict "bull"
        if prev_round and last_round[5] > prev_round[5]:  # closePrice comparison
            prediction = "bull"
        else:
            prediction = "bear"
    
    print(f"Prediction for current round: {prediction}")
    return prediction

# Function to place a prediction
def place_prediction(prediction, amount_in_wei):
    try:
        # Replace with actual account details and the method to place a bet
        # For now, we assume you want to send a transaction for the prediction
        account = web3.eth.account.privateKeyToAccount('your_private_key')  # Replace with your private key
        nonce = web3.eth.get_transaction_count(account.address)
        
        # Assuming the contract has a method for placing bets (adjust according to the actual ABI)
        if prediction == "bull":
            tx = contract.functions.placeBullBet().buildTransaction({
                'chainId': 56,  # BSC mainnet chain ID
                'gas': 2000000,
                'gasPrice': web3.toWei('5', 'gwei'),
                'nonce': nonce,
            })
        else:
            tx = contract.functions.placeBearBet().buildTransaction({
                'chainId': 56,  # BSC mainnet chain ID
                'gas': 2000000,
                'gasPrice': web3.toWei('5', 'gwei'),
                'nonce': nonce,
            })
        
        # Sign and send the transaction
        signed_tx = web3.eth.account.sign_transaction(tx, private_key='your_private_key')
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
        
        print(f"Transaction sent. Hash: {web3.toHex(tx_hash)}")
    except Exception as e:
        print(f"Error placing prediction: {e}")

# Main function
def main():
    try:
        # Fetch historical data (last 5 rounds)
        rounds = fetch_historical_round_data(5)

        # Make a prediction based on the historical data
        prediction = make_prediction(rounds)

        # Place the prediction (for example, placing 1 BNB worth of prediction)
        amount_in_wei = web3.toWei(1, 'ether')  # Example: 1 BNB
        place_prediction(prediction, amount_in_wei)
    
    except Exception as e:
        print(f"Error interacting with the contract: {e}")

if __name__ == "__main__":
    main()

