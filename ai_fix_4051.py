def distribute_bounty(wallet_address, amount):
    try:
        # Attempt to send the bounty
        transaction = send_transaction(wallet_address, amount)
        if transaction.status == 'success':
            print(f"Bounty successfully sent to {wallet_address}")
        else:
            print(f"Failed to send bounty to {wallet_address}. Transaction status: {transaction.status}")
    except InsufficientFundsError as e:
        print(f"Insufficient funds to send bounty to {wallet_address}. Error: {e}")
    except GasLimitError as e:
        print(f"Gas limit exceeded for bounty transaction to {wallet_address}. Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
wallet_address = "0x1028CB5543e73167E6708f94E08Aff8a640F0164"
amount = 100  # Amount in USDC
distribute_bounty(wallet_address, amount)