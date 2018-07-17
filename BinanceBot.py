import json
import requests

import sys
import _thread

import utils
import colorama
import platform
from time import strftime, gmtime
import random
import datetime
import base64
import configparser
import BinanceAPI

config = configparser.ConfigParser()
config.readfp(open('config.txt'))
key = config.get('Binance', 'Key')
secret = config.get('Binance', 'Secret')

manager = BinanceAPI.BinanceAPI(key, secret)

buyPriceLip = 0
sellPriceLip = 0


def getBalance(coin):
    while True:
        try:
            data = manager.get_account()
            balances = data['balances']
            for balance in balances:
                if balance['asset'] == coin:
                    return balance['free']
            return 0
        except:
            continue


def USD_BTC_Price():
    data = manager.get_order_books('BTCUSDT')
    return data['bids'][0][0]


def getTicker(coin):
    data = manager.get_order_books(coin + 'BTC')
    return data['asks'][0][0]


def getBidTicker(coin):
    data = manager.get_order_books(coin + 'BTC')
    return data['bids'][0][0]


def buyOrder(coin, amount):
    global buyPriceLip
    # price = getTicker(coin)
    # price = price * (1 + float(buyPriceLip))
    # result = manager.buy_limit(coin + 'BTC', amount, price)
    result = manager.buy_market(coin + 'BTC', amount)
    return result['price']


def sellOrder(coin, price):
    amount = getBalance(coin)
    # result = manager.sell_limit(coin + 'BTC', amount, price)
    result = manager.sell_market(coin + 'BTC', amount)
    return result['price']


def Trade(coin, buyLip, sellLip, amount):
    global buyPriceLip, sellPriceLip
    buyPriceLip = buyLip
    sellPriceLip = sellLip
    openBracket = colorama.Fore.BLACK + colorama.Back.LIGHTCYAN_EX + '['
    closeBracket = ']' + colorama.Style.RESET_ALL + colorama.Back.BLACK + ' '
    color1 = colorama.Fore.LIGHTCYAN_EX
    color2 = colorama.Style.RESET_ALL + colorama.Fore.LIGHTWHITE_EX
    print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Symbol: ' + color2 + coin)
    price = getTicker(coin)
    print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Current Price: ' + color2 + '%.8f' % price)
    usd_btc_price = USD_BTC_Price()
    balance = getBalance('BTC')
    print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Bitcoin Balance:  ' + color2 + '%.8f' % float(balance) + ' | $' + str(float(balance) * usd_btc_price))
    print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Amount to use:  ' + color2 + '%.8f' % amount + ' | $' + str(amount * usd_btc_price))
    amount_to_purchase = amount / price
    print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Amount To Purchase: ' + color2 + '%.8f' % amount_to_purchase)
    print('------------------------------------' + color2)
    print(' ')
    print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Placing Order...')
    buyPrice = buyOrder(coin, amount_to_purchase)
    print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Order Successful!')
    print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Price: ' + color2 + '%.8f' % buyPrice)
    print('------------------------------------')
    print(' ')
    # begin
    # originalPrice = getTicker (O00O0OOO000O00OOO )
    # _thread.start_new_thread(getCurrentPrice, (O00O0OOO000O00OOO,))
    while True:
        bidPrice = getBidTicker(coin)
        sellPrice = bidPrice * (1 - float(sellPriceLip))
        sellPrice = round(sellPrice, 8)
        percentage = float(bidPrice) / float(buyPrice) * 100
        percentage = round(percentage, 1)
        try:
            print('%.1f' % percentage + "% " + '%.8f' % bidPrice + "/" + '%.8f' % buyPrice + " (0=Cancel order | 1=Sell on market price)")
        except:
            continue
        option = utils.input_key_timeout(1)
        if option == '0':
            print('')
            break
        elif option == '1':
            print('')
            print('Sell price is ' + '%.8f' % sellPrice)
            soldPrice = sellOrder(coin, sellPrice)  # line:229
            print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Sell Order Placed!')  # line:230
            print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Price: ' + color2 + '%.8f' % sellPrice)  # line:231
            print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + color1 + 'Patiently Waiting...' + color2)  # line:232
            percentage = round(float(soldPrice) / float(buyPrice) * 100, 1)
            print('------------------------------------')  # line:239
            print(openBracket + strftime('%H:%M:%S', gmtime()) + closeBracket + colorama.Fore.LIGHTCYAN_EX + 'Successfully sold at ' + colorama.Style.RESET_ALL + colorama.Fore.LIGHTWHITE_EX + '%.8f' % soldPrice + ' / ' + (percentage > 100 and 'profit ' or (percentage < 100 and 'loss ' or '')) + '%.1f' % (percentage - 100) + '%')
            return


def main():
    balanceBTC = getBalance('BTC')
    priceBTCUSD = USD_BTC_Price()
    balanceUSD = float(balanceBTC) * priceBTCUSD
    print(colorama.Fore.LIGHTCYAN_EX + '_____________________________________________________________________')
    print(colorama.Fore.LIGHTCYAN_EX + '                                                                     ')
    print(colorama.Fore.LIGHTCYAN_EX + 'Balance (BTC): ' + str(balanceBTC))
    print(colorama.Fore.LIGHTCYAN_EX + 'Balance in USD: ' + str(balanceUSD))
    print(colorama.Fore.LIGHTCYAN_EX + '_____________________________________________________________________')
    if platform.system() == "Windows":
        percent = input('[1] % of bitcoin to spend: ')
        buyPricelip = input('[2] Buy PriceLip %: ')
        sellPricelip = input('[3] Sell PriceLip %: ')
        coin = input('[4] Coin: ')
    else:
        percent = input(colorama.Fore.CYAN + '[1] % of bitcoin to spend: ')
        buyPricelip = input(colorama.Fore.CYAN + '[2] Buy PriceLip %: ')
        sellPricelip = input(colorama.Fore.CYAN + '[3] Sell PriceLip %: ')
        coin = input(colorama.Fore.CYAN + '[4] Coin: ')
    print('')
    print('')
    if len(buyPricelip) <= 1:
        buyPricelip = '0.0' + buyPricelip
    elif len(buyPricelip) <= 2:
        buyPricelip = '0.' + buyPricelip
    else:
        if len(buyPricelip) <= 3:
            buyPricelip = buyPricelip[0] + '.' + buyPricelip[1:]
        else:
            buyPricelip = buyPricelip[0:2]
    if len(sellPricelip) <= 1:
        sellPricelip = '0.0' + sellPricelip
    elif len(sellPricelip) <= 2:
        sellPricelip = '0.' + sellPricelip
    else:
        if len(sellPricelip) <= 3:
            sellPricelip = sellPricelip[0] + '.' + sellPricelip[1:]
        else:
            sellPricelip = sellPricelip[0:2]
    if len(percent) <= 1:
        percent = '0.0' + percent
    elif len(percent) <= 2:
        percent = '0.' + percent
    else:
        if len(percent) <= 3:
            percent = percent[0] + '.' + percent[1:]
        else:
            percent = percent[0:2]
    amount = balanceBTC * float(percent)
    Trade(coin.upper(), buyPricelip, sellPricelip, amount)

#result = manager.buy_market('ETHBTC', 0.1)
#result = manager.buy_limit("ETHBTC", 0.1, 1)
result = getBalance('ETH')
print(result)