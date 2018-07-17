import json as OOOOO00OO0O00000O #line:8
import requests as OOO0000000O0O0O00 #line:9
from time import strftime as OOOOOOOO0O00O0OO0 ,gmtime as OOO0OOOOO000O000O #line:10
import time as O00O00OOOOO0O0O0O #line:11
import hmac as O000O000O0OO00O0O #line:12
import hashlib as O0O0O0000000000OO #line:13
import pprint as O00O0O00OO000O00O #line:14
import pdb as OOOOO0OOOOOO000OO #line:15
import platform as O00OOOO0O0O0O00O0 #line:16
import colorama as O00O0O0OO0O00OO00 #line:17
import utils as O0OO0OO0O0O00O000 #line:18
import datetime as O0000O0OO0O000OO0 #line:19
import random as O0O00OO0OO00O00O0 #line:20
import YobitApiManager
try :#line:21
    from urllib import urlencode as OO0OO000OOO000OOO #line:22
    from urlparse import urljoin as O0OOO000O0OO0O000 #line:23
except ImportError :#line:24
    from urllib .parse import urlencode as OO0OO000OOO000OOO #line:25
    from urllib .parse import urljoin as O0OOO000O0OO0O000 #line:26
import configparser as O000O0O0OOOO00O00 #line:28
import sys as O00OO000000OOO00O #line:29
O00OO000000OOO00O .setrecursionlimit (10000 )#line:30
config =O000O0O0OOOO00O00 .ConfigParser ()#line:31
config .readfp (open ('config.txt'))#line:32
key =config .get ('Yobit','Key')#line:33
secret =config .get ('Yobit','Secret')#line:34
manager = YobitApiManager.YoBit(key, secret)
secret =bytes (secret ,'utf8')#line:35
BuyPercent =config .get ('PriceLip','BuyPercent')#line:36
SellPercent =config .get ('PriceLip','SellPercent')#line:37
BuyPercent ,SellPercent =O0OO0OO0O0O00O000 .percentageFix (BuyPercent ,SellPercent )#line:38
lastNonce = int(O00O00OOOOO0O0O0O.time())
def nonceHandler ():#line:40
    global lastNonce
    while True:
        nonce = int(O00O00OOOOO0O0O0O.time())
        if nonce != lastNonce:
            break
        O00O00OOOOO0O0O0O.sleep(1)
    lastNonce = nonce
    return lastNonce
def generate_nonce (length =9 ):#line:51
    ""#line:52
    return ''.join ([str (O0O00OO0OO00O00O0 .randint (0 ,9 ))for OOOO00O00OO0OOOO0 in range (length )])#line:53
def mean (OOOO0OO0O0OO000O0 ):#line:56
    return float (sum (OOOO0OO0O0OO000O0 ))/max (len (OOOO0OO0O0OO000O0 ),1 )#line:57
def getTicker (OO00O0000O0O000O0 ):#line:60
    O000O00O0OOOO00OO ='https://yobit.net/api/3/ticker/'+OO00O0000O0O000O0 +'_btc'#line:61
    OOOOOOOOOOO00O00O =OOO0000000O0O0O00 .get (O000O00O0OOOO00OO ,headers ={'apisign':O000O000O0OO00O0O .new (secret ,O000O00O0OOOO00OO .encode (),O0O0O0000000000OO .sha512 ).hexdigest ()})#line:62
    OO0O0OO0OO00OOOOO =OOOOO00OO0O00000O .loads (OOOOOOOOOOO00O00O .text )#line:63
    return OO0O0OO0OO00OOOOO [OO00O0000O0O000O0 +'_btc']['last']#line:64
def getTickerBuy (OO00O0000O0O000O0 ):#line:60
    O000O00O0OOOO00OO ='https://yobit.net/api/3/ticker/'+OO00O0000O0O000O0 +'_btc'#line:61
    OOOOOOOOOOO00O00O =OOO0000000O0O0O00 .get (O000O00O0OOOO00OO ,headers ={'apisign':O000O000O0OO00O0O .new (secret ,O000O00O0OOOO00OO .encode (),O0O0O0000000000OO .sha512 ).hexdigest ()})#line:62
    OO0O0OO0OO00OOOOO =OOOOO00OO0O00000O .loads (OOOOOOOOOOO00O00O .text )#line:63
    return OO0O0OO0OO00OOOOO [OO00O0000O0O000O0 +'_btc']['buy']#line:64
def getTickerSell (OO00O0000O0O000O0 ):#line:60
    O000O00O0OOOO00OO ='https://yobit.net/api/3/ticker/'+OO00O0000O0O000O0 +'_btc'#line:61
    OOOOOOOOOOO00O00O =OOO0000000O0O0O00 .get (O000O00O0OOOO00OO ,headers ={'apisign':O000O000O0OO00O0O .new (secret ,O000O00O0OOOO00OO .encode (),O0O0O0000000000OO .sha512 ).hexdigest ()})#line:62
    OO0O0OO0OO00OOOOO =OOOOO00OO0O00000O .loads (OOOOOOOOOOO00O00O .text )#line:63
    return OO0O0OO0OO00OOOOO [OO00O0000O0O000O0 +'_btc']['sell']#line:64
def getBalance (OO0O00OOOO0O0O00O ):#line:67
    OOOO0O0OO00O0OOO0 ={}#line:68
    O0OO0OOOO000O000O ='https://yobit.net/tapi'#line:69
    OO000OO00O0O00OO0 =None #line:70
    while OO000OO00O0O00OO0 ==None :#line:71
        OO00000O0OO0O0OO0 =nonceHandler ()#line:72
        OOOO0O0OO00O0OOO0 ['method']='getInfo'#line:73
        OOOO0O0OO00O0OOO0 ['nonce']=OO00000O0OO0O0OO0 #line:74
        OOO000000O0OOO000 =OO0OO000OOO000OOO (OOOO0O0OO00O0OOO0 )#line:75
        OOO00OO0O00O00O00 =O000O000O0OO00O0O .new (secret ,OOO000000O0OOO000 .encode ('utf8'),O0O0O0000000000OO .sha512 ).hexdigest ()#line:76
        OOO00OO00OOO00O0O ={'Content-Type':'application/x-www-form-urlencoded','Key':key ,'Sign':OOO00OO0O00O00O00 }#line:79
        O0OO0000000O0O00O =OOO0000000O0O0O00 .post (O0OO0OOOO000O000O ,data =OOOO0O0OO00O0OOO0 ,headers =OOO00OO00OOO00O0O )#line:80
        OO00000O0OOOOO0O0 =OOOOO00OO0O00000O .loads (O0OO0000000O0O00O .text )#line:81
        if OO00000O0OOOOO0O0 ['success']==0 :#line:125
            #print(OO00000O0OOOOO0O0 ['error'])
            continue
            O00OO000000OOO00O .exit (OO00000O0OOOOO0O0 ['error'])#line:126
        if OO0O00OOOO0O0O00O in OO00000O0OOOOO0O0 ['return']['funds']:#line:82
            return OO00000O0OOOOO0O0 ['return']['funds'][OO0O00OOOO0O0O00O ]#line:83
            OO000OO00O0O00OO0 =1 #line:84
def getOrder (OOOOO000OO000OO00 ):#line:89
    O000O000OO000O0OO =nonceHandler ()#line:90
    O0O0OO0OOOOO00O0O ={}#line:91
    OO00OOOOOO0OO0OOO ='https://yobit.net/tapi'#line:92
    O0O0OO0OOOOO00O0O ['method']='OrderInfo'#line:93
    O0O0OO0OOOOO00O0O ['nonce']=O000O000OO000O0OO #line:94
    O0O0OO0OOOOO00O0O ['order_id']=OOOOO000OO000OO00 #line:95
    OO00O00000OOO00O0 =OO0OO000OOO000OOO (O0O0OO0OOOOO00O0O )#line:96
    O0OOO0OOOOO0OO000 =O000O000O0OO00O0O .new (secret ,OO00O00000OOO00O0 .encode ('utf8'),O0O0O0000000000OO .sha512 ).hexdigest ()#line:97
    OOOO00OO0OOO0OOOO ={'Content-Type':'application/x-www-form-urlencoded','Key':key ,'Sign':O0OOO0OOOOO0OO000 }#line:100
    O0O0O000O000OOO00 =OOO0000000O0O0O00 .post (OO00OOOOOO0OO0OOO ,data =O0O0OO0OOOOO00O0O ,headers =OOOO00OO0OOO0OOOO )#line:101
    OO0O000O00OOOO0O0 =OOOOO00OO0O00000O .loads (O0O0O000O000OOO00 .text )#line:102
    return OO0O000O00OOOO0O0 ['return'][OOOOO000OO000OO00 ]#line:103
def buyOrder (OOOOO00OO0O0OO00O ,O0000OO00OOO00OOO ):#line:106
    OO000OOO00OOOO0O0 =getTickerSell (OOOOO00OO0O0OO00O )#line:108
    OO00O0000O00OO0O0 =nonceHandler ()#line:107
    O00O0OOO0OOO0OOO0 =OO000OOO00OOOO0O0 *(1 +float (BuyPercent ))#line:109
    OO0O00OO0O000OO00 ={}#line:110
    O00000O0O000O0O0O ='https://yobit.net/tapi'#line:111
    OO0O00OO0O000OO00 ['method']='Trade'#line:112
    OO0O00OO0O000OO00 ['nonce']=OO00O0000O00OO0O0 #line:113
    OO0O00OO0O000OO00 ['pair']=OOOOO00OO0O0OO00O +'_btc'#line:114
    OO0O00OO0O000OO00 ['type']='buy'#line:115
    OO0O00OO0O000OO00 ['rate']="%.8f" % float(O00O0OOO0OOO0OOO0)#line:116
    OO0O00OO0O000OO00 ['amount']=O0000OO00OOO00OOO #line:117
    O00000O000O0OO0OO =OO0OO000OOO000OOO (OO0O00OO0O000OO00 )#line:118
    OOO0O0O0O00O0O00O =O000O000O0OO00O0O .new (secret ,O00000O000O0OO0OO .encode ('utf8'),O0O0O0000000000OO .sha512 ).hexdigest ()#line:119
    O00O0O0000000O00O ={'Content-Type':'application/x-www-form-urlencoded','Key':key ,'Sign':OOO0O0O0O00O0O00O }#line:122
    O0O000OOO00OO00O0 =OOO0000000O0O0O00 .post (O00000O0O000O0O0O ,data =OO0O00OO0O000OO00 ,headers =O00O0O0000000O00O )#line:123
    O0OO00OO000O0OOOO =OOOOO00OO0O00000O .loads (O0O000OOO00OO00O0 .text )#line:124
    if O0OO00OO000O0OOOO ['success']==0 :#line:125
        O00OO000000OOO00O .exit (O0OO00OO000O0OOOO ['error'])#line:126
    else :#line:128
        OO0OOO00O00O000OO =O0OO00OO000O0OOOO ['return']['order_id']#line:129
        OOOOOOOOOO0OOO000 =[OO0OOO00O00O000OO ,O00O0OOO0OOO0OOO0 ]#line:130
        return OOOOOOOOOO0OOO000 #line:131
def sellOrder (O0O00O000O0OOOOOO ,OO0O0OOO000000000 ):#line:134
    O0O00OOOOO0OOOOO0 =getBalance (O0O00O000O0OOOOOO )#line:135
    OOO00O00000OO00O0 =nonceHandler ()#line:136
    OO00OO0O0OO0OOOOO ={}#line:137
    OOOOO000O0OOOO0O0 ='https://yobit.net/tapi'#line:138
    OO00OO0O0OO0OOOOO ['method']='Trade'#line:139
    OO00OO0O0OO0OOOOO ['nonce']=OOO00O00000OO00O0 #line:140
    OO00OO0O0OO0OOOOO ['pair']=O0O00O000O0OOOOOO +'_btc'#line:141
    OO00OO0O0OO0OOOOO ['type']='sell'#line:142
    OO00OO0O0OO0OOOOO ['rate']= "%.8f" % float(OO0O0OOO000000000) #line:143
    OO00OO0O0OO0OOOOO ['amount']=O0O00OOOOO0OOOOO0 #line:144
    O00000000O00000OO =OO0OO000OOO000OOO (OO00OO0O0OO0OOOOO )#line:145
    O0O0O00OO00OO0O0O =O000O000O0OO00O0O .new (secret ,O00000000O00000OO .encode ('utf8'),O0O0O0000000000OO .sha512 ).hexdigest ()#line:146
    O0OOOOO00O0OOO000 ={'Content-Type':'application/x-www-form-urlencoded','Key':key ,'Sign':O0O0O00OO00OO0O0O }#line:149
    while True:
        O0000O00O000OOO0O =OOO0000000O0O0O00 .post (OOOOO000O0OOOO0O0 ,data =OO00OO0O0OO0OOOOO ,headers =O0OOOOO00O0OOO000 )#line:150
        OO0000O0OO000OO00 =OOOOO00OO0O00000O .loads (O0000O00O000OOO0O .text )#line:151
        if OO0000O0OO000OO00['success'] == 0:
            print("Debug: " + OO0000O0OO000OO00['error'])
            continue
        else:
            break
    O000OOO0OO0OO000O =OO0000O0OO000OO00 ['return']['order_id']#line:152
    return O000OOO0OO0OO000O #line:153
def marketHistory (OOO0OOOOO0O0OO0OO ):#line:156
    O00O0OOOO000O0OOO ='https://yobit.net/api/3/trades/'+OOO0OOOOO0O0OO0OO +'_btc'#line:157
    O0O0O00OOOO000000 =OOO0000000O0O0O00 .get (O00O0OOOO000O0OOO ,headers ={'apisign':O000O000O0OO00O0O .new (secret ,O00O0OOOO000O0OOO .encode (),O0O0O0000000000OO .sha512 ).hexdigest ()})#line:158
    O0OOO00000O0O00O0 =OOOOO00OO0O00000O .loads (O0O0O00OOOO000000 .text )#line:159
    O0000O0OO0O000OO0 .datetime .fromtimestamp (1499275110 ).strftime ('%H:%M')#line:160
    with open ('mh.json','w')as OO00O00OOO0O00O0O :#line:161
        OOOOO00OO0O00000O .dump (O0OOO00000O0O00O0 ,OO00O00OOO0O00O0O )#line:162
    OOO000000OO0000OO =[]#line:163
    O00O00O00OO000OOO =[]#line:164
    for OOOO0O00O00OO000O in O0OOO00000O0O00O0 [OOO0OOOOO0O0OO0OO +'_btc']:#line:165
        OOO000000OO0000OO .append (OOOO0O00O00OO000O ['price'])#line:166
        O00O00O00OO000OOO .append (OOOO0O00O00OO000O ['timestamp'])#line:167
    O0O000OOO0O00OOOO =O00O00O00OO000OOO [0 ]#line:169
    OOOO0O0OOOO00O0O0 =O0000O0OO0O000OO0 .datetime .fromtimestamp (O0O000OOO0O00OOOO ).strftime ('%M')#line:170
    O00000O00O00OOOOO =0 #line:171
    O0O0OO0OO00OO00O0 =0 #line:172
    for OOOO0O00O00OO000O in O00O00O00OO000OOO :#line:173
        OO00O000OO00000OO =O0000O0OO0O000OO0 .datetime .fromtimestamp (OOOO0O00O00OO000O ).strftime ('%M')#line:174
        if float (OO00O000OO00000OO )==float (OOOO0O0OOOO00O0O0 )-1 :#line:175
            O00000O00O00OOOOO =O00O00O00OO000OOO .index (OOOO0O00O00OO000O )#line:176
            O0O0OO0OO00OO00O0 =OOO000000OO0000OO [O00000O00O00OOOOO ]#line:177
            break #line:178
    O000OOOO0OO0OOOO0 =0 #line:180
    O00OOOOO000O0O000 =0 #line:181
    for OOOO0O00O00OO000O in O00O00O00OO000OOO :#line:182
        OO00O000OO00000OO =O0000O0OO0O000OO0 .datetime .fromtimestamp (OOOO0O00O00OO000O ).strftime ('%M')#line:183
        if float (OO00O000OO00000OO )==float (OOOO0O0OOOO00O0O0 )-2 :#line:184
            O000OOOO0OO0OOOO0 =O00O00O00OO000OOO .index (OOOO0O00O00OO000O )#line:185
            O00OOOOO000O0O000 =OOO000000OO0000OO [O000OOOO0OO0OOOO0 ]#line:186
            break #line:187
    return (O0O0OO0OO00OO00O0 ,O00OOOOO000O0O000 )#line:189
def Trade (OO000OOOO0000OOOO ,O0000000OO00OOO00 ,O0O00O0O000OOO000 ,O0OO0O0O00OOO0OO0 ):#line:192
    O000O0O0OOO00OOOO =O00O0O0OO0O00OO00 .Fore .BLACK +O00O0O0OO0O00OO00 .Back .LIGHTCYAN_EX +'['#line:194
    OOOO0OOOOO00000OO =']'+O00O0O0OO0O00OO00 .Style .RESET_ALL + O00O0O0OO0O00OO00.Back.BLACK +' '#line:195
    OOOO0O000O0OOO00O =O00O0O0OO0O00OO00 .Fore .LIGHTCYAN_EX #line:196
    OOO00000OOOOOO00O =O00O0O0OO0O00OO00 .Style .RESET_ALL + O00O0O0OO0O00OO00.Fore.LIGHTWHITE_EX #line:197
    print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Symbol: '+OOO00000OOOOOO00O +OO000OOOO0000OOOO )#line:199
    OO0O0O0OOO000000O =getTickerSell (OO000OOOO0000OOOO )#line:200
    print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Current Price: '+OOO00000OOOOOO00O +'%.8f'%OO0O0O0OOO000000O )#line:201
    OO0OO00OOO000OO00 =USD_BTC_Price ()#line:202
    OO0OOO0O0OOOO0OOO =getBalance ('btc')#line:203
    OOOOO0O000OO0O0O0 =OO0OOO0O0OOOO0OOO *OO0OO00OOO000OO00 #line:204
    OOO0OO000O0OOOO00 =O0O00O0O000OOO000 *OO0OO00OOO000OO00 #line:205
    print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Bitcoin Balance:  '+OOO00000OOOOOO00O +'%.8f'%OO0OOO0O0OOOO0OOO +' | $'+'%.2f'%OOOOO0O000OO0O0O0 )#line:206
    print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Amount to use:  '+OOO00000OOOOOO00O +'%.8f'%O0O00O0O000OOO000 +' | $'+'%.2f'%OOO0OO000O0OOOO00 )#line:207
    O00O00OOOO0OO0OO0 =O0O00O0O000OOO000 /OO0O0O0OOO000000O #line:208
    print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Amount To Purchase: '+OOO00000OOOOOO00O +'%.8f'%O00O00OOOO0OO0OO0 )#line:209
    print ('------------------------------------'+OOO00000OOOOOO00O )#line:210
    print (' ')#line:211
    O0000OOO0O000O0OO ,OOOO000000OOOOOO0 =marketHistory (OO000OOOO0000OOOO )#line:212
    if float (O0OO0O0O00OOO0OO0 )!=0 :#line:215
        O0000OOO0O000O0OO ,OOOO000000OOOOOO0 =marketHistory (OO000OOOO0000OOOO )#line:216
        OO000OO0O0OOOO0O0 =config .get ('RiskMultiplier',O0OO0O0O00OOO0OO0 )#line:217
        O00O0OO000O0000OO =O0000OOO0O000O0OO *float (OO000OO0O0OOOO0O0 )#line:218
        OOOO0O00O000OO0O0 =OOOO000000OOOOOO0 *float (OO000OO0O0OOOO0O0 )#line:219
        if O0000OOO0O000O0OO !=0 and OO0O0O0OOO000000O +OO0O0O0OOO000000O *float (O0000000OO00OOO00 )>=O00O0OO000O0000OO :#line:221
            print ('Buy conditions not met, canceling order.')#line:222
            print ('price 1')#line:223
            O000OOOO0O000O000 =OO0O0O0OOO000000O *OO0OO00OOO000OO00 #line:224
            print ('Last Price: BTC '+'%.8f'%OO0O0O0OOO000000O +' | $'+'%.2f'%O000OOOO0O000O000 )#line:225
            O000O00OOO00OO0O0 =OO0O0O0OOO000000O +OO0O0O0OOO000000O *float (O0000000OO00OOO00 )#line:226
            O000000OOOOO0O00O =O000O00OOO00OO0O0 *OO0OO00OOO000OO00 #line:227
            print ('Potential Sell Price: BTC '+'%.2f'%O000O00OOO00OO0O0 +' | $'+'%.2f'%O000000OOOOO0O00O )#line:228
            O0OOOO00000OOOO0O =O00O0OO000O0000OO *OO0OO00OOO000OO00 #line:229
            print ('Price Limit: BTC '+'%.8f'%O00O0OO000O0000OO +' | $'+'%.2f'%O0OOOO00000OOOO0O )#line:230
            O000O0O0OOO00OOOO =getTickerSell (OO000OOOO0000OOOO )#line:231
            O0O0OOOOOOO0OOOO0 =O000O0O0OOO00OOOO *OO0OO00OOO000OO00 #line:232
            print ('Current Price: BTC '+'%.8f'%O000O0O0OOO00OOOO +' | $'+'%.2f'%O0O0OOOOOOO0OOOO0 )#line:233
            return #line:234
        if OOOO000000OOOOOO0 !=0 and OO0O0O0OOO000000O +OO0O0O0OOO000000O *float (O0000000OO00OOO00 )>=OOOO0O00O000OO0O0 :#line:236
            print ('Buy conditions not met, canceling order.')#line:237
            print ('price 2')#line:238
            O000OOOO0O000O000 =OO0O0O0OOO000000O *OO0OO00OOO000OO00 #line:239
            print ('Last Price: BTC '+'%.8f'%OO0O0O0OOO000000O +' | $'+'%.2f'%O000OOOO0O000O000 )#line:240
            O000O00OOO00OO0O0 =OO0O0O0OOO000000O +OO0O0O0OOO000000O *float (O0000000OO00OOO00 )#line:241
            O000000OOOOO0O00O =O000O00OOO00OO0O0 *OO0OO00OOO000OO00 #line:242
            print ('Potential Sell Price: BTC '+'%.2f'%O000O00OOO00OO0O0 +' | $'+'%.2f'%O000000OOOOO0O00O )#line:243
            O0OOOO00000OOOO0O =O00O0OO000O0000OO *OO0OO00OOO000OO00 #line:244
            print ('Price Limit: BTC '+'%.8f'%O00O0OO000O0000OO +' | $'+'%.2f'%O0OOOO00000OOOO0O )#line:245
            O000O0O0OOO00OOOO =getTickerSell (OO000OOOO0000OOOO )#line:246
            O0O0OOOOOOO0OOOO0 =O000O0O0OOO00OOOO *OO0OO00OOO000OO00 #line:247
            print ('Current Price: BTC '+'%.8f'%O000O0O0OOO00OOOO +' | $'+'%.2f'%O0O0OOOOOOO0OOOO0 )#line:248
            return #line:249
    O0000OOOOO0OO0O0O =buyOrder (OO000OOOO0000OOOO ,O00O00OOOO0OO0OO0 )#line:251
    OOO0O0OOO00O0O00O =True #line:252
    print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Placing Order...')#line:253
    while OOO0O0OOO00O0O00O :#line:254
        result = manager.trade_history(OO000OOOO0000OOOO +'_btc')
        if result['success'] == 0:
            #print(result['error'])
            continue
        orders = result['return']
        for key in orders:
            order = orders[key]
            if order['order_id'] == str (O0000OOOOO0OO0O0O [0 ]):
                buyPrice = order['rate']
                print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Order Successful!')#line:257
                print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Price: '+OOO00000OOOOOO00O +'%.8f'%buyPrice)#line:258
                print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Bitcoin Balance: '+OOO00000OOOOOO00O +'%.8f'%getBalance ('btc'))#line:259
                print ('------------------------------------')#line:260
                print (' ')#line:261
                OOO0O0OOO00O0O00O =False #line:262
                break
    #begin
    while True:
        marketBuyPrice = getTickerBuy(OO000OOOO0000OOOO)
        percentage = float(marketBuyPrice) / float(buyPrice) * 100
        percentage = round(percentage, 1)
        try:
            print('%.1f' % percentage + "% " + '%.8f' % marketBuyPrice + " / " + '%.8f' % buyPrice + " (0=Cancel | 1=Sell)")
        except:
            continue
        option = O0OO0OO0O0O00O000.input_key_timeout(1)
        if option == '0':
            print('Sell is cancelled')
            break
        elif option == '1':
            print('')
            O0OOO0O0OOOO0O0O0 =marketBuyPrice * (1 - float (SellPercent ))#line:267
            O0OOOOOOO00O00O00 =sellOrder (OO000OOOO0000OOOO ,O0OOO0O0OOOO0O0O0 )#line:268
            print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Sell Order Placed!')#line:269
            print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Price: '+OOO00000OOOOOO00O +'%.8f'%O0OOO0O0OOOO0O0O0 )#line:270
            print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Patiently Waiting...'+OOO00000OOOOOO00O )#line:271
            OOOOOOOO00000OOOO =True #line:272
            while OOOOOOOO00000OOOO :#line:273
                result = manager.trade_history(OO000OOOO0000OOOO +'_btc')
                if result['success'] == 0:
                    #print(result['error'])
                    continue
                orders = result['return']
                for key in orders:
                    order = orders[key]
                    if order['order_id'] == str (O0OOOOOOO00O00O00 ):
                        soldPrice = order['rate']
                        percentage = float(soldPrice) / float(buyPrice) * 100
                        percentage = round(percentage, 1)
                        print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +"Current Price: "+OOO00000OOOOOO00O +'%.8f'%getTicker (OO000OOOO0000OOOO ),end ="\r")#line:275
                        print ('------------------------------------')#line:277
                        print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +O00O0O0OO0O00OO00.Fore.LIGHTCYAN_EX +'Successfully sold at ' + O00O0O0OO0O00OO00.Style.RESET_ALL + O00O0O0OO0O00OO00.Fore.LIGHTWHITE_EX + '%.8f' % soldPrice + ' / ' + (percentage > 100 and 'profit ' or (percentage < 100 and 'loss ' or '')) + '%.1f' % (percentage - 100) + '%')#line:278
                        print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Bitcoin Balance: '+OOO00000OOOOOO00O +'%.8f'%getBalance ('btc'))#line:279
                        OO0OO00OOO000OO00 =USD_BTC_Price ()#line:280
                        print (O000O0O0OOO00OOOO +OOOOOOOO0O00O0OO0 ('%H:%M:%S',OOO0OOOOO000O000O ())+OOOO0OOOOO00000OO +OOOO0O000O0OOO00O +'Bitcoin Balance in USD: '+OOO00000OOOOOO00O +str (getBalance ('btc')*OO0OO00OOO000OO00 ))#line:281
                        OOOOOOOO00000OOOO =False #line:282
                        break
            break
def USD_BTC_Price ():#line:285
    OOO0O0OOOO0OOO00O ='https://yobit.net/api/3/ticker/btc_usd'#line:286
    OOO0O0O00O0OOO0O0 =OOO0000000O0O0O00 .get (OOO0O0OOOO0OOO00O ,headers ={'apisign':O000O000O0OO00O0O .new (secret ,OOO0O0OOOO0OOO00O .encode (),O0O0O0000000000OO .sha512 ).hexdigest ()})#line:287
    O0O0O0O00O0O00OOO =OOOOO00OO0O00000O .loads (OOO0O0O00O0OOO0O0 .text )#line:288
    return O0O0O0O00O0O00OOO ['btc_usd']['last']#line:289
def main ():#line:292
    global BuyPercent, SellPercent
    # debug begin
    #result = manager.trade_history('taxi_btc')
    #print(result)
    #orders = result['return']
    #for key in orders:
    #    order = orders[key]
    #    if order['order_id'] == '106715492032422':
    #        print('%.8f' % order['rate'])
    #return
    # end
    OOOOOO0O0O00000OO =getBalance ('btc')#line:293
    #return # debug
    OO0OOOO00O0OO0O00 =USD_BTC_Price ()#line:294
    OO00O0O0O00O0OO0O =OOOOOO0O0O00000OO *OO0OOOO00O0OO0O00 #line:295
    print (O00O0O0OO0O00OO00 .Fore .LIGHTCYAN_EX +'_____________________________________________________________________')#line:296
    print (O00O0O0OO0O00OO00 .Fore .LIGHTCYAN_EX +'                                                                     ')#line:296
    print (O00O0O0OO0O00OO00 .Fore .LIGHTCYAN_EX +'Balance (BTC): '+str (OOOOOO0O0O00000OO ))#line:297
    print (O00O0O0OO0O00OO00 .Fore .LIGHTCYAN_EX +'Balance in USD: '+str (OO00O0O0O00O0OO0O ))#line:298
    print (O00O0O0OO0O00OO00 .Fore .LIGHTCYAN_EX +'_____________________________________________________________________')#line:299
    if O00OOOO0O0O0O00O0 .system ()=="Windows":#line:300
        #OOO0O0000OO00000O =input ('[1] Risk Multiplier: ')#line:301
        O0OO0O0O00OOOOOO0 =input ('[1] % of bitcoin to spend: ')#line:302
        OO00O0O0O00O00000 =input ('[2] Buy PriceLip %: ')#line:303
        OO00O0O0O00O000O0 =input ('[3] Sell PriceLip %: ')#line:303
        O0O0OO0OO0O00OO00 =input ('[4] Coin: ')#line:304
    else :#line:305
        #OOO0O0000OO00000O =input (O00O0O0OO0O00OO00 .Fore .CYAN +'[1] Risk Multiplier: ')#line:306
        O0OO0O0O00OOOOOO0 =input (O00O0O0OO0O00OO00 .Fore .CYAN +'[1] % of bitcoin to spend: ')#line:307
        OO00O0O0O00O00000 =input (O00O0O0OO0O00OO00 .Fore .CYAN +'[2] Buy PriceLip %: ')#line:308
        OO00O0O0O00O000O0 =input (O00O0O0OO0O00OO00 .Fore .CYAN +'[3] Sell PriceLip %: ')#line:308
        O0O0OO0OO0O00OO00 =input (O00O0O0OO0O00OO00 .Fore .CYAN +'[4] Coin: ')#line:309
    print('')
    print('')
    if len (OO00O0O0O00O00000 )<=1 :#line:311
        OO00O0O0O00O00000 ='0.0'+OO00O0O0O00O00000 #line:312
    elif len (OO00O0O0O00O00000 )<=2 :#line:313
        OO00O0O0O00O00000 ='0.'+OO00O0O0O00O00000 #line:314
    else :#line:315
        if len (OO00O0O0O00O00000 )<=3 :#line:316
            OO00O0O0O00O00000 =OO00O0O0O00O00000 [0 ]+'.'+OO00O0O0O00O00000 [1 :]#line:317
        else :#line:318
            OO00O0O0O00O00000 =OO00O0O0O00O00000 [0 :2 ]#line:319
    if len (OO00O0O0O00O000O0 )<=1 :#line:311
        OO00O0O0O00O000O0 ='0.0'+OO00O0O0O00O000O0 #line:312
    elif len (OO00O0O0O00O000O0 )<=2 :#line:313
        OO00O0O0O00O000O0 ='0.'+OO00O0O0O00O000O0 #line:314
    else :#line:315
        if len (OO00O0O0O00O000O0 )<=3 :#line:316
            OO00O0O0O00O000O0 =OO00O0O0O00O000O0 [0 ]+'.'+OO00O0O0O00O000O0 [1 :]#line:317
        else :#line:318
            OO00O0O0O00O000O0 =OO00O0O0O00O000O0 [0 :2 ]#line:319
    if len (O0OO0O0O00OOOOOO0 )<=1 :#line:320
        O0OO0O0O00OOOOOO0 ='0.0'+O0OO0O0O00OOOOOO0 #line:321
    elif len (O0OO0O0O00OOOOOO0 )<=2 :#line:322
        O0OO0O0O00OOOOOO0 ='0.'+O0OO0O0O00OOOOOO0 #line:323
    else :#line:324
        if len (O0OO0O0O00OOOOOO0 )<=3 :#line:325
            O0OO0O0O00OOOOOO0 =O0OO0O0O00OOOOOO0 [0 ]+'.'+O0OO0O0O00OOOOOO0 [1 :]#line:326
        else :#line:327
            O0OO0O0O00OOOOOO0 =O0OO0O0O00OOOOOO0 [0 :2 ]#line:328
    O0OO0O0OOO0O000O0 =OOOOOO0O0O00000OO *float (O0OO0O0O00OOOOOO0 )#line:331
    BuyPercent = OO00O0O0O00O00000
    SellPercent = OO00O0O0O00O000O0
    Trade (O0O0OO0OO0O00OO00 .lower (),OO00O0O0O00O00000 ,O0OO0O0OOO0O000O0 ,0 )
#e9015584e6a44b14988f13e2298bcbf9

