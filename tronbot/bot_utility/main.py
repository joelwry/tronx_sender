import os 
import time
from tronpy import Tron
from tronpy.keys import PrivateKey

from .transfer import send_trx
from .check_balance import getAccountBalance

from dotenv import load_dotenv
load_dotenv()


PRIVATE_KEY = os.getenv('TRON_SENDER_PRIVATE_KEY')
SOURCE_ADDRESS = os.getenv('TRON_SENDER_PUBLIC_ADDRESS')
DESTINATION_ADDRESS = os.getenv('TRON_RECIEVER_PUBLIC_ADDRESS')


client = Tron(network="shasta")  # or 'mainnet' for production


def monitor_wallet():
    transaction_count = 0
    private_key = PrivateKey(bytes.fromhex(PRIVATE_KEY))
    try:
        balance = getAccountBalance(SOURCE_ADDRESS,client)
        if balance and balance > 3:
            amount_to_send = balance - 2
            was_successful = send_trx(DESTINATION_ADDRESS,amount_to_send,client,private_key)
            transaction_count = transaction_count + 1 if was_successful else transaction_count
            print(f'Transaction count : {transaction_count}')

            # now showing account balance for sender and reciever 
            getAccountBalance(SOURCE_ADDRESS,client)
            getAccountBalance(DESTINATION_ADDRESS,client)

        time.sleep(10)  # Poll every 120 seconds

    except Exception as e:
        print("Error:", e)
        time.sleep(20)

def getSenderAndRecieverWalletBalance()->dict | None:
    try : 
        sender_balance = getAccountBalance(SOURCE_ADDRESS,client)
        reciever_balance = getAccountBalance(DESTINATION_ADDRESS,client)
        return {
            "sender_wallet_address":SOURCE_ADDRESS,
            "sender_wallet_balance": sender_balance,
            "reciever_wallet_address":DESTINATION_ADDRESS,
            "reciever_wallet_balance": reciever_balance
        }
    except Exception as e :
        print(e)
        return None

# if __name__ == "__main__": 
#     monitor_wallet()