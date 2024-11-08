from django.apps import AppConfig
#from .tasks import check_wallet_task

class TronbotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tronbot'

    # def ready(self):
    #     # Schedule the task on startup if it's not already scheduled
    #     check_wallet_task(repeat=20)  # Repeat every 20 seconds
