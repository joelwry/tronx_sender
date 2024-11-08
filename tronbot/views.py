from django.shortcuts import render,HttpResponse
from .tasks import check_wallet_task
from .bot_utility.main import getSenderAndRecieverWalletBalance

# Create your views here.
check_wallet_task(repeat=5) # schedules the task to run

def activeTronBot(request):
    return HttpResponse('<h2>TRON BOT ACTIVE </h2>')

def walletBalance(request) : 
    balance = getSenderAndRecieverWalletBalance()
    if balance :
        return HttpResponse(
            f'''
            <div style='text-align:center'>
                <h2 align='center' style='text-shadow: 1px 1px 2px rgba(1, 1, 1, 0.2);font-size: -webkit-xxx-large;color: darkslateblue;'> Wallet Balance </h2>

                <div>
                    <img src="https://s3.coinmarketcap.com/static/img/portraits/62837c68ab0e763d5f77e9a6.png" style="width : 100px; height:auto; margin-bottom : 50px;"/>
                </div>
                
                <div style="background: #faebd714;padding: 5px;padding-top: 20px;filter: drop-shadow(1px 1px 1px rgba(12,12,1,0.4));border-radius: 10px;width: 70%;margin-left: 15%;">
                    <div>
                        <span> Sender Wallet  : </span> <span style='font-weight:bold'>{balance.get("sender_wallet_address")}</span>
                    </div>
                    <div style='display: flex;align-items: center;justify-content: center;'>
                        <span> Sender balance : </span> 
                        <span style='font-weight:bold;color: brown;font-size: xxx-large;'>{balance.get("sender_wallet_balance")} TRX</span>
                    </div>
                </div>

                <br><br>

                <div style="background: #f4f4f4;padding: 5px;padding-top: 20px;filter: drop-shadow(1px 1px 1px rgba(12,12,1,0.4));border-radius: 10px;width: 70%;margin-left: 15%;">
                    <div>
                        <span> Reciever Wallet  : </span> <span style='font-weight:bold'>{balance.get("reciever_wallet_address")}</span>
                    </div>
                    <div style='display: flex;align-items: center;justify-content: center;'>
                        <span> Reciever Balance : </span> 
                        <span style='font-weight:bold;color: brown;font-size: xxx-large;'>{balance.get("reciever_wallet_balance")} TRX</span>
                    </div>
                </div>
            </div>
            '''
        )
    else : 
        return HttpResponse("<h2 align='center' style='color:red'> Error Retrieving Account Details </h2>")