import json as OOOOO0000OO0OO0OO #line:1
import requests as O0OO00O0O00O0O0O0 #line:2
from time import strftime as O00OO0OO0000O0O00 ,gmtime as OOO00OO00O0OOOOO0 #line:3
import time as OO0000O000O0OOOOO #line:4
import hmac as OO0OO0OO0OO0O0OOO #line:5
import hashlib as OO00O0O0O00OOOO00 #line:6
import pdb as O0O0000O00OOO0OOO #line:7
import colorama as OOOO0OOOO0OO0OO00 #line:8
import platform as OOO0O000OO00OOO00 #line:9
import BittrexBot as O00OOOOOOOOOO0OO0 #line:10
try :#line:11
    from urllib import urlencode as OO0000O0OO0OO0O0O #line:12
    from urlparse import urljoin as OOOO00000O0O00000 #line:13
except ImportError :#line:14
    from urllib .parse import urlencode as OO0000O0OO0OO0O0O #line:15
    from urllib .parse import urljoin as OOOO00000O0O00000 #line:16
import logger as O0O0OO000O00O000O #line:18
import configparser as OO0O0O00O00000OO0 #line:19
nonce =str (int (OO0000O000O0OOOOO .time ()*1000 ))#line:20
config =OO0O0O00O00000OO0 .ConfigParser ()#line:21
config .readfp (open ('config.txt'))#line:22
key =config .get ('Bittrex','Key')#line:23
secret =config .get ('Bittrex','Secret')#line:24
price =[]#line:25
volume =[]#line:26
volumeDict ={}#line:27
def market ():#line:29
    OO0000OO00O0O00O0 ='https://bittrex.com/api/v1.1/public/getmarketsummaries'#line:30
    O0O0OO0O000O00O00 =O0OO00O0O00O0O0O0 .get (OO0000OO00O0O00O0 ,headers ={'apisign':OO0OO0OO0OO0O0OOO .new (secret .encode (),OO0000OO00O0O00O0 .encode (),OO00O0O0O00OOOO00 .sha512 ).hexdigest ()})#line:31
    O0O00OO0O0000OOO0 =OOOOO0000OO0OO0OO .loads (O0O0OO0O000O00O00 .text )#line:32
    return O0O00OO0O0000OOO0 #line:33
def main (O000O00OO0000O0OO ):#line:36
    if OOO0O000OO00OOO00 .system ()=="Windows":#line:37
        O0O0O00OOOOOO000O =input ('Price Percent Change? ')#line:38
        O0OOOO0OOO00OOOOO =input ('Volume Percent Change? ')#line:39
    else :#line:40
        O0O0O00OOOOOO000O =input (OOOO0OOOO0OO0OO00 .Fore .CYAN +'Price Percent Change? '+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:41
        O0OOOO0OOO00OOOOO =input (OOOO0OOOO0OO0OO00 .Fore .CYAN +'Volume Percent Change? '+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:42
    if O000O00OO0000O0OO !=None :#line:43
        O00000OOOOOO0OO00 =O00OOOOOOOOOO0OO0 .getBalance ('btc')#line:44
        OO000O00O0OO0OO00 =O00OOOOOOOOOO0OO0 .USD_BTC_Price ()#line:45
        O0000O000OO0O0OOO =O00000OOOOOO0OO00 *OO000O00O0OO0OO00 #line:46
        print (OOOO0OOOO0OO0OO00 .Fore .RED +'_____________________________________________________________________'+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:47
        print (OOOO0OOOO0OO0OO00 .Fore .RED +'Balance (BTC): '+str (O00000OOOOOO0OO00 )+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:48
        print (OOOO0OOOO0OO0OO00 .Fore .RED +'Balance in USD: '+str (O0000O000OO0O0OOO )+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:49
        print (OOOO0OOOO0OO0OO00 .Fore .RED +'_____________________________________________________________________'+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:50
        if OOO0O000OO00OOO00 .system ()=="Windows":#line:51
            OOO00O000O0O0OO00 =input ('[1] Risk Multiplier: ')#line:52
            OOOOO0OOO0OOOO0OO =input ('[2] % of bitcoin to spend: ')#line:53
            O0OOOO000OOOOOO0O =input ('[3] Profit %: ')#line:54
        else :#line:55
            OOO00O000O0O0OO00 =input (OOOO0OOOO0OO0OO00 .Fore .CYAN +'[1] Risk Multiplier: '+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:56
            OOOOO0OOO0OOOO0OO =input (OOOO0OOOO0OO0OO00 .Fore .CYAN +'[2] % of bitcoin to spend: '+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:57
            O0OOOO000OOOOOO0O =input (OOOO0OOOO0OO0OO00 .Fore .CYAN +'[3] Profit %: '+OOOO0OOOO0OO0OO00 .Style .RESET_ALL )#line:58
        OOOOO0OOO0OOOO0OO ,O0OOOO000OOOOOO0O =percentageFix (OOOOO0OOO0OOOO0OO ,O0OOOO000OOOOOO0O )#line:59
    O00OOO00O00O00000 ,O0O0OOO0O000O000O =percentageFix (O0O0O00OOOOOO000O ,O0OOOO0OOO00OOOOO )#line:60
    O0OOO0OOOO0OOO00O =market ()#line:61
    for OOO0OOOOOOO0O0000 in O0OOO0OOOO0OOO00O ['result']:#line:62
        price .append (OOO0OOOOOOO0O0000 ['Last'])#line:63
        volume .append (OOO0OOOOOOO0O0000 ['Volume'])#line:64
        volumeDict [OOO0OOOOOOO0O0000 ['MarketName']]=[]#line:65
    O0OOO0OOO00O00000 =True #line:67
    OOO000O000O0OOOO0 =1 #line:68
    OOO0OOO0000O00OO0 =OOOO0OOOO0OO0OO00 .Fore .YELLOW +OOOO0OOOO0OO0OO00 .Back .BLUE #line:69
    OO0O0O00O000OOOO0 =OOOO0OOOO0OO0OO00 .Style .RESET_ALL #line:70
    OO0OO000O0OO00000 =O0O0OO000O00O000O .getLogger ('test')#line:71
    OO0OO000O0OO00000 .critical ('working')#line:72
    print (' ')#line:73
    while 1 :#line:74
        if O0OOO0OOO00O00000 ==True :#line:75
            O000OOOOOO0O0OOO0 =market ()#line:76
            OOO000O000O0OOOO0 +=1 #line:77
            for OOO0OOOOOOO0O0000 in O000OOOOOO0O0OOO0 ['result']:#line:78
                OOOO0OOO0OO0O00OO =O000OOOOOO0O0OOO0 ['result'].index (OOO0OOOOOOO0O0000 )#line:79
                if OOO0OOOOOOO0O0000 ['Last']>price [OOOO0OOO0OO0O00OO ]+price [OOOO0OOO0OO0O00OO ]*float (O00OOO00O00O00000 )and OOO0OOOOOOO0O0000 ['Volume']>volume [OOOO0OOO0OO0O00OO ]+volume [OOOO0OOO0OO0O00OO ]*float (O0O0OOO0O000O000O ):#line:80
                    O00OOO0OOO0OOOOO0 =str (OOO0OOOOOOO0O0000 ['Last']/price [OOOO0OOO0OO0O00OO ])#line:81
                    O000O00000O000OO0 =str (OOO0OOOOOOO0O0000 ['Volume']/volume [OOOO0OOO0OO0O00OO ])#line:82
                    print (OOO0OOO0000O00OO0 +'Time: '+OO0O0O00O000OOOO0 +timestamp ())#line:83
                    print (OOO0OOO0000O00OO0 +'Name: '+OO0O0O00O000OOOO0 +OOO0OOOOOOO0O0000 ['MarketName'])#line:84
                    print (OOO0OOO0000O00OO0 +'Price % Change: '+OO0O0O00O000OOOO0 +O00OOO0OOO0OOOOO0 [2 :4 ]+'%')#line:85
                    print (OOO0OOO0000O00OO0 +'Volume % Change: '+OO0O0O00O000OOOO0 +O000O00000O000OO0 [2 :4 ]+'%')#line:86
                    print (OOO0OOO0000O00OO0 +'Old Price: '+OO0O0O00O000OOOO0 +'%.8f'%price [OOOO0OOO0OO0O00OO ])#line:87
                    print (OOO0OOO0000O00OO0 +'New Price: '+OO0O0O00O000OOOO0 +'%.8f'%OOO0OOOOOOO0O0000 ['Last'])#line:88
                    print (OOO0OOO0000O00OO0 +'Old Volume: '+OO0O0O00O000OOOO0 +'%.8f'%volume [OOOO0OOO0OO0O00OO ])#line:89
                    print (OOO0OOO0000O00OO0 +'New Volume: '+OO0O0O00O000OOOO0 +'%.8f'%OOO0OOOOOOO0O0000 ['Volume'])#line:90
                    print ('------------------------------')#line:91
                    if O000O00OO0000O0OO !=None :#line:92
                        O00000OOOOOO0OO00 =O00OOOOOOOOOO0OO0 .getBalance ('btc')#line:93
                        OOOO0O0O00OOOO000 =O00000OOOOOO0OO00 *float (OOOOO0OOO0OOOO0OO )#line:94
                        OOOO00000O000OOOO =OOO0OOOOOOO0O0000 ['MarketName'].split ('-')#line:95
                        O00OOOOOOOOOO0OO0 .Trade (OOOO00000O000OOOO [1 ],O0OOOO000OOOOOO0O ,OOOO0O0O00OOOO000 ,OOO00O000O0O0OO00 )#line:96
                    price [OOOO0OOO0OO0O00OO ]=OOO0OOOOOOO0O0000 ['Last']#line:97
                    volume [OOOO0OOO0OO0O00OO ]=OOO0OOOOOOO0O0000 ['Volume']#line:98
                else :#line:99
                    price [OOOO0OOO0OO0O00OO ]=OOO0OOOOOOO0O0000 ['Last']#line:100
                    volume [OOOO0OOO0OO0O00OO ]=OOO0OOOOOOO0O0000 ['Volume']#line:101
            OO0000O000O0OOOOO .sleep (3 )#line:103
def timestamp ():#line:106
    return O00OO0OO0000O0O00 ('%H:%M:%S',OOO00OO00O0OOOOO0 ())#line:107
def percentageFix (OOOOOO0O000OOO00O ,OOOO000OOO0OOO000 ):#line:110
    if len (OOOOOO0O000OOO00O )<=1 :#line:111
        OOOOOO0O000OOO00O ='0.0'+OOOOOO0O000OOO00O #line:112
    elif len (OOOOOO0O000OOO00O )<=2 :#line:113
        OOOOOO0O000OOO00O ='0.'+OOOOOO0O000OOO00O #line:114
    else :#line:115
        if len (OOOOOO0O000OOO00O )<=3 :#line:116
            OOOOOO0O000OOO00O =OOOOOO0O000OOO00O [0 ]+'.'+OOOOOO0O000OOO00O [1 :]#line:117
        else :#line:118
            OOOOOO0O000OOO00O =OOOOOO0O000OOO00O [0 :2 ]#line:119
    if len (OOOO000OOO0OOO000 )<=1 :#line:120
        OOOO000OOO0OOO000 ='0.0'+OOOO000OOO0OOO000 #line:121
    elif len (OOOO000OOO0OOO000 )<=2 :#line:122
        OOOO000OOO0OOO000 ='0.'+OOOO000OOO0OOO000 #line:123
    elif len (OOOO000OOO0OOO000 )<=3 :#line:124
        OOOO000OOO0OOO000 =OOOO000OOO0OOO000 [0 ]+'.'+OOOO000OOO0OOO000 [1 :]#line:125
    else :#line:126
        OOOO000OOO0OOO000 =OOOO000OOO0OOO000 [0 :2 ]#line:127
    return (OOOOOO0O000OOO00O ,OOOO000OOO0OOO000 )
#e9015584e6a44b14988f13e2298bcbf9

