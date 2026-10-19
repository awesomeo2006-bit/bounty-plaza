# Import necessary libraries
from web3 import Web3

# Connect to the Ethereum network
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# Define the target wallet address
target_wallet = '0x1028CB5543e73167E6708f94E08Aff8a640F0164'

# Define the amount to send (in wei)
amount_to_send = Web3.toWei(1, 'ether')

# Define the contract address and ABI
contract_address = '0xYourContractAddress'
contract_abi = [
    # Add your contract ABI here
]

# Create a contract instance
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Define the function to send the bounty
def send_bounty():
    # Get the current account
    account = w3.eth.defaultAccount

    # Check if the account has enough balance
    if w3.eth.get_balance(account) < amount_to_send:
        print("Insufficient funds")
        return

    # Call the function to send the bounty
    tx_hash = contract.functions.sendBounty(target_wallet).transact({'from': account})

    # Wait for the transaction to be mined
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)

    # Check if the transaction was successful
    if receipt.status == 1:
        print("Bounty sent successfully")
    else:
        print("Transaction failed")

# Call the function to send the bounty
send_bounty()