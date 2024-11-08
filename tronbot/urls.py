
from django.urls import path
from .views import activeTronBot,walletBalance

urlpatterns = [
    path('',activeTronBot, name='tron-bot-home'),
    path('wallet-balance/',walletBalance,name='get-sender-reciever-wallet-balance')
]
