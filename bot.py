from web3 import Web3
import os
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()
RPC_URL = os.getenv("BSC_RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
WALLET_ADDRESS = os.getenv("WALLET_ADDRESS")

# Connect to Binance Smart Chain
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# PancakeSwap Prediction Market Smart Contract Details
CONTRACT_ADDRESS = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with actual contract address
ABI = [...]  # Paste the contract ABI here

contract = web3.eth.contract(address=Web3.to_checksum_address(CONTRACT_ADDRESS), abi=ABI)

def place_bet(direction, amount):
    """
    Function to place a bet on PancakeSwap Prediction market.
    direction: "bull" (UP) or "bear" (DOWN)
    amount: Amount of BNB to bet
    """
    # Determine function to call based on direction
    if direction.lower() == "bull":
        bet_function = contract.functions.betBull
    elif direction.lower() == "bear":
        bet_function = contract.functions.betBear
    else:
        raise ValueError("Invalid direction. Use 'bull' or 'bear'.")

    # Prepare transaction
    txn = bet_function().build_transaction({
        'from': WALLET_ADDRESS,
        'value': web3.to_wei(amount, 'ether'),
        'gas': 300000,
        'gasPrice': web3.to_wei('5', 'gwei'),
        'nonce': web3.eth.get_transaction_count(WALLET_ADDRESS),
    })

    # Sign and send transaction
    signed_txn = web3.eth.account.sign_transaction(txn, private_key=PRIVATE_KEY)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(f"Transaction sent! TX Hash: {tx_hash.hex()}")
    return tx_hash

def main():
    while True:
        # Fetch current round details
        current_round = contract.functions.currentEpoch().call()
        print(f"Current Round: {current_round}")

        # Fetch data for decision-making (e.g., historical trends)
        # Add logic to decide "bull" or "bear" based on your strategy
        decision = "bull"  # Example: always bet "bull" for now

        # Place bet with a fixed amount (e.g., 0.01 BNB)
        tx_hash = place_bet(decision, 0.01)
        print(f"Bet placed on {decision.upper()}! TX Hash: {tx_hash.hex()}")

        # Wait for the next round (PancakeSwap rounds are 5 minutes)
        print("Waiting for the next round...")
        time.sleep(5 * 60)  # 5 minutes

if __name__ == "__main__":
    main()
