import json as OO0OOO0O00OO00OOO #line:1
import requests as O00OO0000O0O0O0O0 #line:2
from time import strftime as O0OO00OO000O0OOO0 ,gmtime as O0OO0000O00O0OO0O #line:3
import time as OOO00000OOO0OOO00 #line:4
import hmac as OOO00O00O000OO00O #line:5
import hashlib as O00OOO0OOOO0OO0OO #line:6
import pdb as OO0OO0000OOOO0OO0 #line:7

import sys
import _thread

import utils as OOO00O0O0O000000O #line:8
import colorama as O0OO00O00000OOO0O #line:9
import platform as O0O00O00O00O00OO0 #line:10
import random as OOOO0OOOO0OO00O00 #line:11
OOO000000OOO0OOOO =__import__ ('urllib.parse',globals (),locals ())#line:12
import datetime as O00OO0OO00OO0000O #line:13
import base64 as OOO00OOOOOOO0000O #line:14
import configparser as O00O000O0OOOO0OO0 #line:15
import sys as O0OO00O0O0000OO0O #line:16
import CryptopiaApiManager as ApiManager
config =O00O000O0OOOO0OO0 .ConfigParser ()#line:17
config .readfp (open ('config.txt'))#line:18
key =config .get ('Cryptopia','Key')#line:19
secret =config .get ('Cryptopia','Secret')#line:20
manager = ApiManager.Api(key, secret)
lastPrice = 0
currentSellOrderId = -1
BuyPercent =config .get ('PriceLip','BuyPercent')#line:21
SellPercent =config .get ('PriceLip','SellPercent')#line:22
BuyPercent ,SellPercent =OOO00O0O0O000000O .percentageFix (BuyPercent ,SellPercent )#line:23
def make_nonce ():#line:26
    return str (OOOO0OOOO0OO00O00 .randint (0 ,100000000 ))#line:27
# get price to buy
def getTicker (OOOOOOOOOO00O0OO0 ):#line:29
    O0OOO0O0000000000 ='https://www.cryptopia.co.nz/api/GetMarket/'+OOOOOOOOOO00O0OO0 +'_BTC'#line:30
    O00O00OOO0O00000O =O00OO0000O0O0O0O0 .get (O0OOO0O0000000000 )#line:31
    O0000OO0000O00O0O =OO0OOO0O00OO00OOO .loads (O00O00OOO0O00000O .text )#line:32
    while O0000OO0000O00O0O ['Data']==None :#line:33
        O00O00OOO0O00000O =O00OO0000O0O0O0O0 .get (O0OOO0O0000000000 )#line:34
        O0000OO0000O00O0O =OO0OOO0O00OO00OOO .loads (O00O00OOO0O00000O .text )#line:35
    OO0O00O0OOO0O00O0 =O0000OO0000O00O0O ['Data']#line:36
    return OO0O00O0OOO0O00O0 ['AskPrice']#line:37
# get price to sell
def getBidTicker (OOOOOOOOOO00O0OO0 ):#line:29
    O0OOO0O0000000000 ='https://www.cryptopia.co.nz/api/GetMarket/'+OOOOOOOOOO00O0OO0 +'_BTC'#line:30
    O00O00OOO0O00000O =O00OO0000O0O0O0O0 .get (O0OOO0O0000000000 )#line:31
    O0000OO0000O00O0O =OO0OOO0O00OO00OOO .loads (O00O00OOO0O00000O .text )#line:32
    while O0000OO0000O00O0O ['Data']==None :#line:33
        O00O00OOO0O00000O =O00OO0000O0O0O0O0 .get (O0OOO0O0000000000 )#line:34
        O0000OO0000O00O0O =OO0OOO0O00OO00OOO .loads (O00O00OOO0O00000O .text )#line:35
    OO0O00O0OOO0O00O0 =O0000OO0000O00O0O ['Data']#line:36
    return OO0O00O0OOO0O00O0 ['BidPrice']#line:37
def getBalance (OO000000OOO00OO00 ):#line:39
    O0O0000OO0O000O00 ="https://www.cryptopia.co.nz/Api/GetBalance"#line:40
    OOO00O000OO000O00 =make_nonce ()#line:41
    O00OOO0O0OO00O000 =OO0OOO0O00OO00OOO .dumps ({"Currency":OO000000OOO00OO00 })#line:42
    O0OO00O0OOO0OOOOO =O00OOO0OOOO0OO0OO .md5 ()#line:43
    O0OO00O0OOO0OOOOO .update (O00OOO0O0OO00O000 .encode ('utf-8'))#line:44
    O000OO0000000O0O0 =OOO00OOOOOOO0000O .b64encode (O0OO00O0OOO0OOOOO .digest ()).decode ('utf-8')#line:45
    OO0000000OOO00OO0 =key +"POST"+OOO000000OOO0OOOO .parse .quote_plus (O0O0000OO0O000O00 ).lower ()+OOO00O000OO000O00 +O000OO0000000O0O0 #line:46
    O0OO00O0OO0O0OOO0 =OOO00OOOOOOO0000O .b64encode (OOO00O00O000OO00O .new (OOO00OOOOOOO0000O .b64decode (secret ),OO0000000OOO00OO0 .encode ('utf-8'),O00OOO0OOOO0OO0OO .sha256 ).digest ())#line:47
    O000O000O0O0000OO ="amx "+key +":"+O0OO00O0OO0O0OOO0 .decode ('utf-8')+":"+OOO00O000OO000O00 #line:48
    O00O00OO0OO0O0O0O ={'Authorization':O000O000O0O0000OO ,'Content-Type':'application/json; charset=utf-8'}#line:49
    OOO0O0O0OO00OOOO0 =O00OO0000O0O0O0O0 .post (O0O0000OO0O000O00 ,data =O00OOO0O0OO00O000 ,headers =O00O00OO0OO0O0O0O )#line:50
    O00OOO00000O0OOOO =OO0OOO0O00OO00OOO .loads (OOO0O0O0OO00OOOO0 .text )#line:51
    for OOOOOOOO0000O0OO0 in O00OOO00000O0OOOO ['Data']:#line:52
        return OOOOOOOO0000O0OO0 ['Available']#line:53
def getOrder (O00OOO0OOO0OOO000 ):#line:56
    OOOOO00OO00O00O0O ='https://www.cryptopia.co.nz/api/GetTradeHistory'#line:57
    O00000OOO00OO00OO =make_nonce ()#line:58
    OOOOO0OO0O0OOO000 =OO0OOO0O00OO00OOO .dumps ({'Market':O00OOO0OOO0OOO000 ,"Count":10 })#line:59
    OO0OOO0OO0O00O0OO =O00OOO0OOOO0OO0OO .md5 ()#line:60
    OO0OOO0OO0O00O0OO .update (OOOOO0OO0O0OOO000 .encode ('utf-8'))#line:61
    O00O00OO0O00O0O0O =OOO00OOOOOOO0000O .b64encode (OO0OOO0OO0O00O0OO .digest ()).decode ('utf-8')#line:62
    O00OO0OO000000OO0 =key +"POST"+OOO000000OOO0OOOO .parse .quote_plus (OOOOO00OO00O00O0O ).lower ()+O00000OOO00OO00OO +O00O00OO0O00O0O0O #line:63
    O0OOO0O00OO00OO00 =OOO00OOOOOOO0000O .b64encode (OOO00O00O000OO00O .new (OOO00OOOOOOO0000O .b64decode (secret ),O00OO0OO000000OO0 .encode ('utf-8'),O00OOO0OOOO0OO0OO .sha256 ).digest ())#line:64
    OO0000OOO0OO0O0O0 ="amx "+key +":"+O0OOO0O00OO00OO00 .decode ('utf-8')+":"+O00000OOO00OO00OO #line:65
    O0OOO000O0O000O00 ={'Authorization':OO0000OOO0OO0O0O0 ,'Content-Type':'application/json; charset=utf-8'}#line:66
    O0OO000O0O000O0O0 =O00OO0000O0O0O0O0 .post (OOOOO00OO00O00O0O ,data =OOOOO0OO0O0OOO000 ,headers =O0OOO000O0O000O00 )#line:67
    OOO0OO0O0O00OOOOO =O0OO000O0O000O0O0 .json ()#line:68
    return OOO0OO0O0O00OOOOO ['Data']#line:69
def buyOrder (OO0O0O0OO0O0OO000 ,O0OO0OO0OO0OOO00O ):#line:72
    O0000000O0000OO00 =getTicker (OO0O0O0OO0O0OO000 )#line:73
    OO0O000O0OOO000OO =O0000000O0000OO00 *(1 +float (BuyPercent ))#line:74
    OOO00OOOO0O000O0O ="https://www.cryptopia.co.nz/Api/SubmitTrade"#line:75
    O0OO000OOOOO00000 =make_nonce ()#line:76
    OO0O0O0OO0O0OO000 =OO0O0O0OO0O0OO000 +'/BTC'#line:77
    OOOOO00OO00OOO0OO =OO0OOO0O00OO00OOO .dumps ({'Market':OO0O0O0OO0O0OO000 ,"Type":"Buy","Rate":OO0O000O0OOO000OO  ,"Amount":O0OO0OO0OO0OOO00O })#line:78
    O00O0O0O0OO00OO0O =O00OOO0OOOO0OO0OO .md5 ()#line:79
    O00O0O0O0OO00OO0O .update (OOOOO00OO00OOO0OO .encode ('utf-8'))#line:80
    O000000OO0OO00O0O =OOO00OOOOOOO0000O .b64encode (O00O0O0O0OO00OO0O .digest ()).decode ('utf-8')#line:81
    O0O0O0O00O0O0O0O0 =key +"POST"+OOO000000OOO0OOOO .parse .quote_plus (OOO00OOOO0O000O0O ).lower ()+O0OO000OOOOO00000 +O000000OO0OO00O0O #line:82
    OOOOOO000O0O00OOO =OOO00OOOOOOO0000O .b64encode (OOO00O00O000OO00O .new (OOO00OOOOOOO0000O .b64decode (secret ),O0O0O0O00O0O0O0O0 .encode ('utf-8'),O00OOO0OOOO0OO0OO .sha256 ).digest ())#line:83
    O00OOO000O00OOOO0 ="amx "+key +":"+OOOOOO000O0O00OOO .decode ('utf-8')+":"+O0OO000OOOOO00000 #line:84
    OO00O000O0O000OO0 ={'Authorization':O00OOO000O00OOOO0 ,'Content-Type':'application/json; charset=utf-8'}#line:85
    O000000O00OOOOO0O =O00OO0000O0O0O0O0 .post (OOO00OOOO0O000O0O ,data =OOOOO00OO00OOO0OO ,headers =OO00O000O0O000OO0 )#line:86
    O000000OOO00OO0OO =O000000O00OOOOO0O .json ()#line:87
    if O000000OOO00OO0OO ['Success']==False :#line:88
        print ('Error!')#line:89
        O0OO00O0O0000OO0O .exit ('Message: '+O000000OOO00OO0OO ['Error'])#line:90
    else :#line:91
        if len(O000000OOO00OO0OO ['Data']['FilledOrders']) == 0:
            cancelOrderById(O000000OOO00OO0OO ['Data']['OrderId'])
            print('Can\'t buy because price was increased rapidly.')
            print('Order cancelled')
            print('')
            return [-1]
        OO0O0O0OOOOOO00OO =O000000OOO00OO0OO ['Data']['FilledOrders'][0 ]#line:92
        O000OOOO00OOOO00O =[OO0O0O0OOOOOO00OO ,OO0O000O0OOO000OO ]#line:93
        return O000OOOO00OOOO00O #line:94
def sellOrder (OO00000O00OO0O000 ,O0OOOO0OO00OO0O0O ):#line:96
    O0O0O0OOOO0OOOOOO =getBalance (OO00000O00OO0O000 )#line:97
    OO0O0OO000OO00OO0 ="https://www.cryptopia.co.nz/Api/SubmitTrade"#line:98
    OO00OO00O0000OO00 =make_nonce ()#line:99
    O000OOOOOOOOOO00O =OO00000O00OO0O000 +'/BTC'#line:100
    OOO000OOO0O00000O =OO0OOO0O00OO00OOO .dumps ({'Market':O000OOOOOOOOOO00O ,"Type":"Sell","Rate":O0OOOO0OO00OO0O0O ,"Amount":O0O0O0OOOO0OOOOOO })#line:101
    OOO0OO00O0O0OOO00 =O00OOO0OOOO0OO0OO .md5 ()#line:102
    OOO0OO00O0O0OOO00 .update (OOO000OOO0O00000O .encode ('utf-8'))#line:103
    O00OOO0OO00000OO0 =OOO00OOOOOOO0000O .b64encode (OOO0OO00O0O0OOO00 .digest ()).decode ('utf-8')#line:104
    O0O0OO000OO000O0O =key +"POST"+OOO000000OOO0OOOO .parse .quote_plus (OO0O0OO000OO00OO0 ).lower ()+OO00OO00O0000OO00 +O00OOO0OO00000OO0 #line:105
    OOO000OOO0000OOOO =OOO00OOOOOOO0000O .b64encode (OOO00O00O000OO00O .new (OOO00OOOOOOO0000O .b64decode (secret ),O0O0OO000OO000O0O .encode ('utf-8'),O00OOO0OOOO0OO0OO .sha256 ).digest ())#line:106
    O0OO0O0OO0OOOOO00 ="amx "+key +":"+OOO000OOO0000OOOO .decode ('utf-8')+":"+OO00OO00O0000OO00 #line:107
    O00O00O0OOOO00O0O ={'Authorization':O0OO0O0OO0OOOOO00 ,'Content-Type':'application/json; charset=utf-8'}#line:108
    O00O000OO0O0OO000 =O00OO0000O0O0O0O0 .post (OO0O0OO000OO00OO0 ,data =OOO000OOO0O00000O ,headers =O00O00O0OOOO00O0O )#line:109
    OO0O00000000O00OO =OO0OOO0O00OO00OOO .loads (O00O000OO0O0OO000 .text )#line:110
    #return OO0O00000000O00OO ['Data']['OrderId']#line:111
    return int(OO0O00000000O00OO ['Data']['FilledOrders'][0])
def marketHistory (O000O0OOO0OO0O000 ):#line:114
    O0000O00OOOOO0OOO ='https://www.cryptopia.co.nz/api/GetMarketHistory/'+O000O0OOO0OO0O000 +'_BTC'#line:115
    O00O00O000O00000O =O00OO0000O0O0O0O0 .get (O0000O00OOOOO0OOO )#line:116
    O0OOO0000O0O0OOOO =OO0OOO0O00OO00OOO .loads (O00O00O000O00000O .text )#line:117
    OOOOOOO000O00000O =O0OOO0000O0O0OOOO ['Data']#line:118
    with open ('mh.json','w')as OO0O0OOO0O00O0OO0 :#line:119
        OO0OOO0O00OO00OOO .dump (O0OOO0000O0O0OOOO ,OO0O0OOO0O00O0OO0 )#line:120
    OOO0O0OO0O0O0000O =[]#line:122
    OO0OOO00OO0O0OO0O =[]#line:123
    for O000O0O00OO0OO0O0 in OOOOOOO000O00000O :#line:124
        OOO0O0OO0O0O0000O .append (O000O0O00OO0OO0O0 ['Price'])#line:125
        OO0OOO00OO0O0OO0O .append (O000O0O00OO0OO0O0 ['Timestamp'])#line:126
    OO000OO00OO0OOOOO =OO0OOO00OO0O0OO0O [0 ]#line:128
    O0OO0OOO0O00O0OOO =O00OO0OO00OO0000O .datetime .fromtimestamp (OO000OO00OO0OOOOO ).strftime ('%M')#line:129
    O00OO00OOO00OOOOO =0 #line:130
    O0O00O0OOOO00O0OO =0 #line:131
    for O000O0O00OO0OO0O0 in OO0OOO00OO0O0OO0O :#line:132
        O000OOO0000O00O0O =O00OO0OO00OO0000O .datetime .fromtimestamp (O000O0O00OO0OO0O0 ).strftime ('%M')#line:133
        if float (O000OOO0000O00O0O )==float (O0OO0OOO0O00O0OOO )-1 :#line:134
            O00OO00OOO00OOOOO =OO0OOO00OO0O0OO0O .index (O000O0O00OO0OO0O0 )#line:135
            O0O00O0OOOO00O0OO =OOO0O0OO0O0O0000O [O00OO00OOO00OOOOO ]#line:136
            break #line:137
    O000OOO0OOOOO0O00 =0 #line:139
    OOO0OO0O0000O0O00 =0 #line:140
    for O000O0O00OO0OO0O0 in OO0OOO00OO0O0OO0O :#line:141
        O000OOO0000O00O0O =O00OO0OO00OO0000O .datetime .fromtimestamp (O000O0O00OO0OO0O0 ).strftime ('%M')#line:142
        if float (O000OOO0000O00O0O )==float (O0OO0OOO0O00O0OOO )-2 :#line:143
            O000OOO0OOOOO0O00 =OO0OOO00OO0O0OO0O .index (O000O0O00OO0OO0O0 )#line:144
            OOO0OO0O0000O0O00 =OOO0O0OO0O0O0000O [O000OOO0OOOOO0O00 ]#line:145
            break #line:146
    return (O0O00O0OOOO00O0OO ,OOO0OO0O0000O0O00 )#line:148
def USD_BTC_Price ():#line:151
    OO0000000O0O000OO ='https://www.cryptopia.co.nz/api/GetMarket/BTC_USDT'#line:152
    O0O00OO0OO00OOO00 =O00OO0000O0O0O0O0 .get (OO0000000O0O000OO )#line:153
    O0O0O0OOO00000OOO =OO0OOO0O00OO00OOO .loads (O0O00OO0OO00OOO00 .text )#line:154
    OOOOOOOOO000OO0O0 =O0O0O0OOO00000OOO ['Data']#line:155
    return OOOOOOOOO000OO0O0 ['LastPrice']#line:156
def getCurrentPrice(coinname):
    global lastPrice
    for i in range(1, 1000):
        lastPrice = getBidTicker(coinname)
        #OOO00000OOO0OOO00.sleep(1)
def Trade (O00O0OOO000O00OOO ,O00OO00000OOOO00O , O00O0OO0000000OO0, OOOOO000OOOOO000O ,O0O0OOO0O0000O00O ):#line:159
    global lastPrice, BuyPercent, SellPercent
    BuyPercent = O00OO00000OOOO00O
    SellPercent = O00O0OO0000000OO0
    OOO0OOO0000OOO000 =O0OO00O00000OOO0O .Fore .BLACK +O0OO00O00000OOO0O .Back .LIGHTCYAN_EX +'['#line:160
    O0O0O000OOOOO0O00 =']'+O0OO00O00000OOO0O .Style .RESET_ALL + O0OO00O00000OOO0O.Back.BLACK + ' '#line:161
    OO00O0O0O000OOO00 =O0OO00O00000OOO0O .Fore .LIGHTCYAN_EX #line:162
    OO0O0O0O0OO0O00O0 =O0OO00O00000OOO0O .Style .RESET_ALL + O0OO00O00000OOO0O.Fore.LIGHTWHITE_EX #line:163
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Symbol: '+OO0O0O0O0OO0O00O0 +O00O0OOO000O00OOO )#line:164
    O0OO0OOO0O00O0OO0 =getTicker (O00O0OOO000O00OOO )#line:165
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Current Price: '+OO0O0O0O0OO0O00O0 +'%.8f'%O0OO0OOO0O00O0OO0 )#line:166
    OOOO00O00000O000O =USD_BTC_Price ()#line:167
    OO000OO0O000OO000 =getBalance ('BTC')#line:168
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Bitcoin Balance:  '+OO0O0O0O0OO0O00O0 +'%.8f'%float (OO000OO0O000OO000 )+' | $'+str (float (OO000OO0O000OO000 )*OOOO00O00000O000O ))#line:169
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Amount to use:  '+OO0O0O0O0OO0O00O0 +'%.8f'%OOOOO000OOOOO000O +' | $'+str (OOOOO000OOOOO000O *OOOO00O00000O000O ))#line:170
    OOO0OOOO0OO000OOO =OOOOO000OOOOO000O /O0OO0OOO0O00O0OO0 #line:171
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Amount To Purchase: '+OO0O0O0O0OO0O00O0 +'%.8f'%OOO0OOOO0OO000OOO )#line:172
    print ('------------------------------------'+OO0O0O0O0OO0O00O0 )#line:173
    print (' ')#line:174
    if float (O0O0OOO0O0000O00O )!=0 :#line:176
        OO00000O00O00O00O ,OO00O0000OO0OOOOO =marketHistory (O00O0OOO000O00OOO )#line:177
        OO00O0OO0O0O00000 =config .get ('RiskMultiplier',O0O0OOO0O0000O00O )#line:178
        OO0O000OO0OO000OO =OO00000O00O00O00O *float (OO00O0OO0O0O00000 )#line:179
        OO00OO0O000O00O0O =OO00O0000OO0OOOOO *float (OO00O0OO0O0O00000 )#line:180
        if OO00000O00O00O00O !=0 and O0OO0OOO0O00O0OO0 +O0OO0OOO0O00O0OO0 *float (O00OO00000OOOO00O )>=OO0O000OO0OO000OO :#line:181
            print ('Buy conditions not met, canceling order.')#line:182
            print ('price 1')#line:183
            OO0O0O0OO0O00O00O =O0OO0OOO0O00O0OO0 *OOOO00O00000O000O #line:184
            print ('Last Price: BTC '+'%.8f'%O0OO0OOO0O00O0OO0 +' | $'+'%.2f'%OO0O0O0OO0O00O00O )#line:185
            O000000OO00O00O00 =O0OO0OOO0O00O0OO0 +O0OO0OOO0O00O0OO0 *float (O00OO00000OOOO00O )#line:186
            O0OOOOOO000O000O0 =O000000OO00O00O00 *OOOO00O00000O000O #line:187
            print ('Potential Sell Price: BTC '+'%.2f'%O000000OO00O00O00 +' | $'+'%.2f'%O0OOOOOO000O000O0 )#line:188
            O0O0O00OOO00O000O =OO0O000OO0OO000OO *OOOO00O00000O000O #line:189
            print ('Price Limit: BTC '+'%.8f'%OO0O000OO0OO000OO +' | $'+'%.2f'%O0O0O00OOO00O000O )#line:190
            OOO0OOO0000OOO000 =getTicker (O00O0OOO000O00OOO )#line:191
            OOOOOOOO00O0000O0 =OOO0OOO0000OOO000 *OOOO00O00000O000O #line:192
            print ('Current Price: BTC '+'%.8f'%OOO0OOO0000OOO000 +' | $'+'%.2f'%OOOOOOOO00O0000O0 )#line:193
            return #line:194
        if OO00O0000OO0OOOOO !=0 and O0OO0OOO0O00O0OO0 +O0OO0OOO0O00O0OO0 *float (O00OO00000OOOO00O )>=OO00OO0O000O00O0O :#line:197
            print ('Buy conditions not met, canceling order.')#line:198
            print ('price 2')#line:199
            OO0O0O0OO0O00O00O =O0OO0OOO0O00O0OO0 *OOOO00O00000O000O #line:200
            print ('Last Price: BTC '+'%.8f'%O0OO0OOO0O00O0OO0 +' | $'+'%.2f'%OO0O0O0OO0O00O00O )#line:201
            O000000OO00O00O00 =O0OO0OOO0O00O0OO0 +O0OO0OOO0O00O0OO0 *float (O00OO00000OOOO00O )#line:202
            O0OOOOOO000O000O0 =O000000OO00O00O00 *OOOO00O00000O000O #line:203
            print ('Potential Sell Price: BTC '+'%.2f'%O000000OO00O00O00 +' | $'+'%.2f'%O0OOOOOO000O000O0 )#line:204
            O0O0O00OOO00O000O =OO0O000OO0OO000OO *OOOO00O00000O000O #line:205
            print ('Price Limit: BTC '+'%.8f'%OO0O000OO0OO000OO +' | $'+'%.2f'%O0O0O00OOO00O000O )#line:206
            OOO0OOO0000OOO000 =getTicker (O00O0OOO000O00OOO )#line:207
            OOOOOOOO00O0000O0 =OOO0OOO0000OOO000 *OOOO00O00000O000O #line:208
            print ('Current Price: BTC '+'%.8f'%OOO0OOO0000OOO000 +' | $'+'%.2f'%OOOOOOOO00O0000O0 )#line:209
            return #line:210
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Placing Order...')#line:212
    OOO0O000O00O00O00 =buyOrder (O00O0OOO000O00OOO ,OOO0OOOO0OO000OOO )#line:213
    if OOO0O000O00O00O00[0] == -1:
        return
    O0OOOO0000OOO00O0 =O00O0OOO000O00OOO +"/BTC"#line:214
    O0OOO00O0OOO00000 =getOrder (O0OOOO0000OOO00O0 )#line:215
    OO00OOOOO00000OOO =int (OOO0O000O00O00O00 [0 ])#line:217
    for OOO000OOO0O0O0O0O in O0OOO00O0OOO00000 :#line:218
        if OO00OOOOO00000OOO ==OOO000OOO0O0O0O0O ['TradeId']:#line:219
            OOO0OOOO0000O00O0 =OOO000OOO0O0O0O0O ['Rate']#line:220
            buyPrice = OOO0OOOO0000O00O0
            bought = True
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Order Successful!')#line:221
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Price: '+OO0O0O0O0OO0O00O0 +'%.8f'%OOO0OOOO0000O00O0 )#line:222
    print ('------------------------------------')#line:223
    print (' ')#line:224
    #begin
    #originalPrice = getTicker (O00O0OOO000O00OOO )
    #_thread.start_new_thread(getCurrentPrice, (O00O0OOO000O00OOO,))
    while True:
        bidPrice = getBidTicker(O00O0OOO000O00OOO)
        #sellPrice = bidPrice / (1 + float(SellPercent))
        sellPrice = bidPrice * (1 - float(SellPercent))
        sellPrice = round(sellPrice, 8)
        percentage = float(bidPrice) / float(buyPrice) * 100
        percentage = round(percentage, 1)
        #sys.stdout.write("\r" + '%.0f' % percentage) + "% (0=Cancel order | 1=Sell on market price)")
        try:
            print('%.1f' % percentage + "% " + '%.8f' % bidPrice + "/" + '%.8f' % buyPrice + " (0=Cancel order | 1=Sell on market price)")
        except:
            continue
        option = OOO00O0O0O000000O.input_key_timeout(1)
        if option == '0':
            print('')
            #cancelled = cancelOrderById(OO00OOOOO00000OOO)
            #if cancelled:
            #    print('Order cancelled')
            break
        elif option == '1':
            print('')
            print('Sell price is ' + '%.8f' % sellPrice)
            OO000O00O0OOO0OO0 = sellOrder(O00O0OOO000O00OOO, sellPrice)  # line:229
            #print("For debug: " + str(OO000O00O0OOO0OO0))
            currentSellOrderId = OO000O00O0OOO0OO0
            print(OOO0OOO0000OOO000 + O0OO00OO000O0OOO0('%H:%M:%S', O0OO0000O00O0OO0O()) + O0O0O000OOOOO0O00 + OO00O0O0O000OOO00 + 'Sell Order Placed!')  # line:230
            print(OOO0OOO0000OOO000 + O0OO00OO000O0OOO0('%H:%M:%S', O0OO0000O00O0OO0O()) + O0O0O000OOOOO0O00 + OO00O0O0O000OOO00 + 'Price: ' + OO0O0O0O0OO0O00O0 + '%.8f' % sellPrice)  # line:231
            print(OOO0OOO0000OOO000 + O0OO00OO000O0OOO0('%H:%M:%S', O0OO0000O00O0OO0O()) + O0O0O000OOOOO0O00 + OO00O0O0O000OOO00 + 'Patiently Waiting...' + OO0O0O0O0OO0O00O0)  # line:232
            O0OOO00O0OOO00000 = getOrder(O0OOOO0000OOO00O0)  # line:235
            for OOO000OOO0O0O0O0O in O0OOO00O0OOO00000:  # line:237
                if OO000O00O0OOO0OO0 == OOO000OOO0O0O0O0O['TradeId']:  # line:238
                    soldPrice = OOO000OOO0O0O0O0O['Rate'];
                    percentage = round(float(soldPrice) / float(buyPrice) * 100, 1)
                    print('------------------------------------')  # line:239
                    print(OOO0OOO0000OOO000 + O0OO00OO000O0OOO0('%H:%M:%S', O0OO0000O00O0OO0O()) + O0O0O000OOOOO0O00 + O0OO00O00000OOO0O.Fore.LIGHTCYAN_EX + 'Successfully sold at ' + O0OO00O00000OOO0O.Style.RESET_ALL + O0OO00O00000OOO0O.Fore.LIGHTWHITE_EX + '%.8f' % soldPrice + ' / ' + (percentage > 100 and 'profit ' or (percentage < 100 and 'loss ' or '')) + '%.1f' % (percentage - 100) + '%')  # line:240
                    return
            break
    return
    print("not reached")
    #end
    OO0000OOO0OO0O000 =OOO0OOOO0000O00O0 *float (O00OO00000OOOO00O )#line:226
    O00OO0O0O00O0O0OO =OOO0OOOO0000O00O0 +OO0000OOO0OO0O000 #line:227
    OOO0OOOO0000O00O0 =O00OO0O0O00O0O0OO /(1 +float (SellPercent ))#line:228
    OO000O00O0OOO0OO0 =sellOrder (O00O0OOO000O00OOO ,OOO0OOOO0000O00O0 )#line:229
    currentSellOrderId = OO000O00O0OOO0OO0
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Sell Order Placed!')#line:230
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Price: '+OO0O0O0O0OO0O00O0 +'%.8f'%OOO0OOOO0000O00O0 )#line:231
    print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Patiently Waiting...'+OO0O0O0O0OO0O00O0 )#line:232
    OOO000OOOOOO0000O =True #line:233
    count = 0
    while OOO000OOOOOO0000O :#line:234
        count = count + 1
        if count == 10:
            cancelOrderById(OO000O00O0OOO0OO0)
            print('Can\'t sell because price is rapidly decreased.')
            print('Order cancelled.')
            break
        O0OOO00O0OOO00000 =getOrder (O0OOOO0000OOO00O0 )#line:235
        for OOO000OOO0O0O0O0O in O0OOO00O0OOO00000 :#line:237
            if OO000O00O0OOO0OO0 ==OOO000OOO0O0O0O0O ['TradeId']:#line:238
                print ('------------------------------------')#line:239
                print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Sold!')#line:240
                print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Bitcoin Balance: '+OO0O0O0O0OO0O00O0 +'%.8f'%getBalance ('btc'))#line:241
                OOOO00O00000O000O =USD_BTC_Price ()#line:242
                print (OOO0OOO0000OOO000 +O0OO00OO000O0OOO0 ('%H:%M:%S',O0OO0000O00O0OO0O ())+O0O0O000OOOOO0O00 +OO00O0O0O000OOO00 +'Bitcoin Balance in USD: '+OO0O0O0O0OO0O00O0 +str (getBalance ('btc')*OOOO00O00000O000O ))#line:243
                OOO000OOOOOO0000O =False #line:244
def cancelAllTrade():
    result = manager.cancel_trade('All', '-1')
    if result[0] == None:
        print(result[1])
def cancelOrderById(tradeId):
    result = manager.cancel_trade('Trade', str(tradeId), '-1')
    if result[0] == None:
        print(result[1])
        return False
    else:
        return True
def main ():#line:247
    O0O000O00000O0OOO =getBalance ('BTC')#line:249
    OOOOOOOOOO00O00OO =USD_BTC_Price ()#line:250
    OOOO000000000O000 =float (O0O000O00000O0OOO )*OOOOOOOOOO00O00OO #line:251
    print (O0OO00O00000OOO0O .Fore .LIGHTCYAN_EX +'_____________________________________________________________________')#line:252
    print (O0OO00O00000OOO0O .Fore .LIGHTCYAN_EX +'                                                                     ')#line:252
    print (O0OO00O00000OOO0O .Fore .LIGHTCYAN_EX +'Balance (BTC): '+str (O0O000O00000O0OOO ))#line:253
    print (O0OO00O00000OOO0O .Fore .LIGHTCYAN_EX +'Balance in USD: '+str (OOOO000000000O000 ))#line:254
    print (O0OO00O00000OOO0O .Fore .LIGHTCYAN_EX +'_____________________________________________________________________')#line:255
    if O0O00O00O00O00OO0 .system ()=="Windows":#line:256
        #O0OO0000OOOO00000 =input ('[1] Risk Multiplier: ')#line:257
        OO000OOO00O00O0O0 =input ('[1] % of bitcoin to spend: ')#line:258
        O00O0OO0000000OOO =input ('[2] Buy PriceLip %: ')#line:259
        O00O0OO0000000OO0 =input ('[3] Sell PriceLip %: ')#line:259
        OO0O00OO0000OOO0O =input ('[4] Coin: ')#line:260
    else :#line:261
        #O0OO0000OOOO00000 =input (O0OO00O00000OOO0O .Fore .CYAN +'[1] Risk Multiplier: ')#line:262
        OO000OOO00O00O0O0 =input (O0OO00O00000OOO0O .Fore .CYAN +'[1] % of bitcoin to spend: ')#line:263
        O00O0OO0000000OOO =input (O0OO00O00000OOO0O .Fore .CYAN +'[2] PriceLip %: ')#line:264
        O00O0OO0000000OO0 =input (O0OO00O00000OOO0O .Fore .CYAN +'[3] Sell PriceLip %: ')#line:259
        OO0O00OO0000OOO0O =input (O0OO00O00000OOO0O .Fore .CYAN +'[4] Coin: ')#line:265
    print('')
    print('')
    if len (O00O0OO0000000OOO )<=1 :#line:267
        O00O0OO0000000OOO ='0.0'+O00O0OO0000000OOO #line:268
    elif len (O00O0OO0000000OOO )<=2 :#line:269
        O00O0OO0000000OOO ='0.'+O00O0OO0000000OOO #line:270
    else :#line:271
        if len (O00O0OO0000000OOO )<=3 :#line:272
            O00O0OO0000000OOO =O00O0OO0000000OOO [0 ]+'.'+O00O0OO0000000OOO [1 :]#line:273
        else :#line:274
            O00O0OO0000000OOO =O00O0OO0000000OOO [0 :2 ]#line:275
    if len (O00O0OO0000000OO0 )<=1 :#line:267
        O00O0OO0000000OO0 ='0.0'+O00O0OO0000000OO0 #line:268
    elif len (O00O0OO0000000OO0 )<=2 :#line:269
        O00O0OO0000000OO0 ='0.'+O00O0OO0000000OO0 #line:270
    else :#line:271
        if len (O00O0OO0000000OO0 )<=3 :#line:272
            O00O0OO0000000OO0 =O00O0OO0000000OO0 [0 ]+'.'+O00O0OO0000000OO0 [1 :]#line:273
        else :#line:274
            O00O0OO0000000OO0 =O00O0OO0000000OO0 [0 :2 ]#line:275
    if len (OO000OOO00O00O0O0 )<=1 :#line:276
        OO000OOO00O00O0O0 ='0.0'+OO000OOO00O00O0O0 #line:277
    elif len (OO000OOO00O00O0O0 )<=2 :#line:278
        OO000OOO00O00O0O0 ='0.'+OO000OOO00O00O0O0 #line:279
    else :#line:280
        if len (OO000OOO00O00O0O0 )<=3 :#line:281
            OO000OOO00O00O0O0 =OO000OOO00O00O0O0 [0 ]+'.'+OO000OOO00O00O0O0 [1 :]#line:282
        else :#line:283
            OO000OOO00O00O0O0 =OO000OOO00O00O0O0 [0 :2 ]#line:284
    OOO0OO0000OOOO0OO =O0O000O00000O0OOO *float (OO000OOO00O00O0O0 )#line:286
    Trade (OO0O00OO0000OOO0O .upper (),O00O0OO0000000OOO , O00O0OO0000000OO0, OOO0OO0000OOOO0OO ,0 )
#e9015584e6a44b14988f13e2298bcbf9

