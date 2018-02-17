import json as O0O00OO0O0000000O #line:1
import requests as O0O0OO00OO00OOOOO #line:2
from time import strftime as OOOO0OOO00O00O00O ,gmtime as OOOO0OO0O0OOO0O0O #line:3
import time as O0000O0OOOOOOOOO0 #line:4
import hmac as O00OO0O00000OO0O0 #line:5
import hashlib as OO0000O0OO0O000O0 #line:6
import pdb as O0O00O00O00OO00O0 #line:7
import colorama as OO0000000000O00OO #line:8
import platform
import PoloniexBot as OO0OOO00O000OO000 #line:9
try :#line:10
    from urllib import urlencode as OO000O0OO00O0O0OO #line:11
    from urlparse import urljoin as OO0OOO0000O00000O #line:12
except ImportError :#line:13
    from urllib .parse import urlencode as OO000O0OO00O0O0OO #line:14
    from urllib .parse import urljoin as OO0OOO0000O00000O #line:15
import logger as OO0OO0000OOO0O000 #line:17
import configparser as O00000OO0OO00O000 #line:18
nonce =str (int (O0000O0OOOOOOOOO0 .time ()*1000 ))#line:19
config =O00000OO0OO00O000 .ConfigParser ()#line:20
config .readfp (open ('config.txt'))#line:21
key =config .get ('Poloniex','Key')#line:22
secret =config .get ('Poloniex','Secret')#line:23
price =[]#line:24
volume =[]#line:25
names =[]#line:26
priceNew =[]#line:27
volumeNew =[]#line:28
volumeDict ={}#line:29
def market ():#line:31
    O00O00OOOOO0OO00O ='https://poloniex.com/public?command=returnTicker'#line:32
    OOO0O0OOO0OO000O0 =O0O0OO00OO00OOOOO .get (O00O00OOOOO0OO00O )#line:33
    OOO000OO000000O00 =O0O00OO0O0000000O .loads (OOO0O0OOO0OO000O0 .text )#line:34
    return OOO000OO000000O00 #line:35
def main (O0OO00OO0O0OO0000 ):#line:38
    if platform .system ()=="Windows":#line:39
        OO0O0000OO000000O =input ('Price Percent Change? ')#line:40
        OO0OOO0OOO00O00OO =input ('Volume Percent Change? ')#line:41
    else :#line:42
        OO0O0000OO000000O =input (OO0000000000O00OO .Fore .CYAN +'Price Percent Change? '+OO0000000000O00OO .Style .RESET_ALL )#line:43
        OO0OOO0OOO00O00OO =input (OO0000000000O00OO .Fore .CYAN +'Volume Percent Change? '+OO0000000000O00OO .Style .RESET_ALL )#line:44
    if O0OO00OO0O0OO0000 !=None :#line:45
        OOO0O0OOOOO0O0OO0 =OO0OOO00O000OO000 .getBalance ('BTC')#line:46
        O00O0OO000OOOO0O0 =OO0OOO00O000OO000 .USD_BTC_Price ()#line:47
        OOOO0000O00000000 =float (OOO0O0OOOOO0O0OO0 )*float (O00O0OO000OOOO0O0 )#line:48
        print (OO0000000000O00OO .Fore .RED +'_____________________________________________________________________'+OO0000000000O00OO .Style .RESET_ALL )#line:49
        print (OO0000000000O00OO .Fore .RED +'Balance (BTC): '+str (OOO0O0OOOOO0O0OO0 )+OO0000000000O00OO .Style .RESET_ALL )#line:50
        print (OO0000000000O00OO .Fore .RED +'Balance in USD: '+str (OOOO0000O00000000 )+OO0000000000O00OO .Style .RESET_ALL )#line:51
        print (OO0000000000O00OO .Fore .RED +'_____________________________________________________________________'+OO0000000000O00OO .Style .RESET_ALL )#line:52
        if platform .system ()=="Windows":#line:53
            OOO000O0O000OOO00 =input ('[1] Risk Multiplier: ')#line:54
            O00OO0O00O0OO0000 =input ('[2] % of bitcoin to spend: ')#line:55
            O00O000O0O00O00O0 =input ('[3] Profit %: ')#line:56
        else :#line:57
            OOO000O0O000OOO00 =input (OO0000000000O00OO .Fore .CYAN +'[1] Risk Multiplier: '+OO0000000000O00OO .Style .RESET_ALL )#line:58
            O00OO0O00O0OO0000 =input (OO0000000000O00OO .Fore .CYAN +'[2] % of bitcoin to spend: '+OO0000000000O00OO .Style .RESET_ALL )#line:59
            O00O000O0O00O00O0 =input (OO0000000000O00OO .Fore .CYAN +'[3] Profit %: '+OO0000000000O00OO .Style .RESET_ALL )#line:60
        O00OO0O00O0OO0000 ,O00O000O0O00O00O0 =percentageFix (O00OO0O00O0OO0000 ,O00O000O0O00O00O0 )#line:61
    O000000O0O00O0O0O ,O00OO0O0O00O000OO =percentageFix (OO0O0000OO000000O ,OO0OOO0OOO00O00OO )#line:62
    O00O000OO0OOO000O =market ()#line:63
    for O00O0OO000O00OOOO in O00O000OO0OOO000O :#line:64
        if 'BTC_'in O00O0OO000O00OOOO :#line:65
            price .append (O00O000OO0OOO000O [O00O0OO000O00OOOO ]['last'])#line:66
            volume .append (O00O000OO0OOO000O [O00O0OO000O00OOOO ]['baseVolume'])#line:67
            names .append (O00O0OO000O00OOOO )#line:68
    O0O000000OOO0O000 =True #line:70
    OO0OOO00O0O00OO00 =1 #line:71
    O0OO0O0O00O00O000 =OO0000000000O00OO .Fore .YELLOW +OO0000000000O00OO .Back .BLUE #line:72
    O0O000OOOOO0O0000 =OO0000000000O00OO .Style .RESET_ALL #line:73
    OOO0OO00O0O00O000 =OO0OO0000OOO0O000 .getLogger ('test')#line:74
    OOO0OO00O0O00O000 .critical ('working')#line:75
    print (' ')#line:76
    while 1 :#line:77
        if O0O000000OOO0O000 ==True :#line:78
            OO00OO00O000OOO0O =market ()#line:79
            for O00O0OO000O00OOOO in OO00OO00O000OOO0O :#line:80
                if 'BTC_'in O00O0OO000O00OOOO :#line:81
                    priceNew .append (OO00OO00O000OOO0O [O00O0OO000O00OOOO ]['last'])#line:82
                    volumeNew .append (OO00OO00O000OOO0O [O00O0OO000O00OOOO ]['baseVolume'])#line:83
            for O00O0OO000O00OOOO in priceNew :#line:85
                OO0O0O0OOO0OO0O0O =priceNew .index (O00O0OO000O00OOOO )#line:86
                if float (O00O0OO000O00OOOO )>float (price [OO0O0O0OOO0OO0O0O ])+float (price [OO0O0O0OOO0OO0O0O ])*float (O000000O0O00O0O0O )and float (volumeNew [OO0O0O0OOO0OO0O0O ])>float (volume [OO0O0O0OOO0OO0O0O ])+float (volume [OO0O0O0OOO0OO0O0O ])*float (O00OO0O0O00O000OO ):#line:87
                    O0000O00OO00O0OO0 =str (float (O00O0OO000O00OOOO )/float (price [OO0O0O0OOO0OO0O0O ]))#line:88
                    OO00000OO000OO0O0 =str (float (volumeNew [OO0O0O0OOO0OO0O0O ])/float (volume [OO0O0O0OOO0OO0O0O ]))#line:89
                    print (O0OO0O0O00O00O000 +'Time: '+O0O000OOOOO0O0000 +timestamp ())#line:90
                    print (O0OO0O0O00O00O000 +'Name: '+O0O000OOOOO0O0000 +names [OO0O0O0OOO0OO0O0O ])#line:91
                    print (O0OO0O0O00O00O000 +'Price % Change: '+O0O000OOOOO0O0000 +O0000O00OO00O0OO0 [2 :4 ]+'%')#line:92
                    print (O0OO0O0O00O00O000 +'Volume % Change: '+O0O000OOOOO0O0000 +OO00000OO000OO0O0 [2 :4 ]+'%')#line:93
                    print (O0OO0O0O00O00O000 +'Old Price: '+O0O000OOOOO0O0000 +'%.8f'%float (price [OO0O0O0OOO0OO0O0O ]))#line:94
                    print (O0OO0O0O00O00O000 +'New Price: '+O0O000OOOOO0O0000 +'%.8f'%float (O00O0OO000O00OOOO ))#line:95
                    print (O0OO0O0O00O00O000 +'Old Volume: '+O0O000OOOOO0O0000 +'%.8f'%float (volume [OO0O0O0OOO0OO0O0O ]))#line:96
                    print (O0OO0O0O00O00O000 +'New Volume: '+O0O000OOOOO0O0000 +'%.8f'%float (volumeNew [OO0O0O0OOO0OO0O0O ]))#line:97
                    print ('------------------------------')#line:98
                    if O0OO00OO0O0OO0000 !=None :#line:99
                        OOO0O0OOOOO0O0OO0 =OO0OOO00O000OO000 .getBalance ('BTC')#line:100
                        OOO00000OOO0O0OOO =float (OOO0O0OOOOO0O0OO0 )*float (O00OO0O00O0OO0000 )#line:101
                        OOOOO0O0O0OOO0OOO =names [OO0O0O0OOO0OO0O0O ].split ('_')#line:102
                        BittrexBot .Trade (OOOOO0O0O0OOO0OOO [0 ],O00O000O0O00O00O0 ,OOO00000OOO0O0OOO ,OOO000O0O000OOO00 )#line:103
                    price [OO0O0O0OOO0OO0O0O ]=priceNew [OO0O0O0OOO0OO0O0O ]#line:104
                    volume [OO0O0O0OOO0OO0O0O ]=volumeNew [OO0O0O0OOO0OO0O0O ]#line:105
                else :#line:106
                    price [OO0O0O0OOO0OO0O0O ]=priceNew [OO0O0O0OOO0OO0O0O ]#line:107
                    volume [OO0O0O0OOO0OO0O0O ]=volumeNew [OO0O0O0OOO0OO0O0O ]#line:108
            volumeNew [:]=[]#line:109
            priceNew [:]=[]#line:110
            O0000O0OOOOOOOOO0 .sleep (1 )#line:111
def timestamp ():#line:114
    return OOOO0OOO00O00O00O ('%H:%M:%S',OOOO0OO0O0OOO0O0O ())#line:115
def percentageFix (O0000O0O00O00O0OO ,O00O00OO00OO00O0O ):#line:118
    if len (O0000O0O00O00O0OO )<=1 :#line:119
        O0000O0O00O00O0OO ='0.0'+O0000O0O00O00O0OO #line:120
    elif len (O0000O0O00O00O0OO )<=2 :#line:121
        O0000O0O00O00O0OO ='0.'+O0000O0O00O00O0OO #line:122
    else :#line:123
        if len (O0000O0O00O00O0OO )<=3 :#line:124
            O0000O0O00O00O0OO =O0000O0O00O00O0OO [0 ]+'.'+O0000O0O00O00O0OO [1 :]#line:125
        else :#line:126
            O0000O0O00O00O0OO =O0000O0O00O00O0OO [0 :2 ]#line:127
    if len (O00O00OO00OO00O0O )<=1 :#line:128
        O00O00OO00OO00O0O ='0.0'+O00O00OO00OO00O0O #line:129
    elif len (O00O00OO00OO00O0O )<=2 :#line:130
        O00O00OO00OO00O0O ='0.'+O00O00OO00OO00O0O #line:131
    elif len (O00O00OO00OO00O0O )<=3 :#line:132
        O00O00OO00OO00O0O =O00O00OO00OO00O0O [0 ]+'.'+O00O00OO00OO00O0O [1 :]#line:133
    else :#line:134
        O00O00OO00OO00O0O =O00O00OO00OO00O0O [0 :2 ]#line:135
    return (O0000O0O00O00O0OO ,O00O00OO00OO00O0O )
#e9015584e6a44b14988f13e2298bcbf9

