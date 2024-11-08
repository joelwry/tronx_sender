from background_task import background
from .bot_utility.main import monitor_wallet

@background(schedule=20)  # Schedule to run every 20 seconds
def check_wallet_task():
    # Call your function here
    monitor_wallet()
