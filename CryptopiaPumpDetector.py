import json as OO0O0OO00O000O00O #line:1
import requests as O000OO0OOO000O00O #line:2
from time import strftime as O0O00O00000O00OO0 ,gmtime as O0000O0OO0OO0OOOO #line:3
import time as OOO000O00O0OOOO0O #line:4
import hmac as O0OO00OO0O0OOOO00 #line:5
import hashlib as O00O00000OO0O0000 #line:6
import pdb as O0O000O0O000OO000 #line:7
import colorama as O00O00OO0OOOO0OO0 #line:8
import CryptopiaBot as O0O00OO000OO0OO0O #line:9
try :#line:10
    from urllib import urlencode as O0OO000OOOOOO00O0 #line:11
    from urlparse import urljoin as OO000000OOOO000OO #line:12
except ImportError :#line:13
    from urllib .parse import urlencode as O0OO000OOOOOO00O0 #line:14
    from urllib .parse import urljoin as OO000000OOOO000OO #line:15
import platform as OO0O000O00O0O0000 #line:16
import logger as O0O00O0000000O00O #line:17
import configparser as OOOO000O0OO0O0O0O #line:18
nonce =str (int (OOO000O00O0OOOO0O .time ()*1000 ))#line:19
config =OOOO000O0OO0O0O0O .ConfigParser ()#line:20
config .readfp (open ('config.txt'))#line:21
key =config .get ('Cryptopia','Key')#line:22
secret =config .get ('Cryptopia','Secret')#line:23
price =[]#line:24
volume =[]#line:25
volumeDict ={}#line:26
def market ():#line:28
    O0OOOOO0OOOO0O0OO ='https://www.cryptopia.co.nz/api/GetMarkets/BTC'#line:29
    O0000O000O0O0OO0O =O000OO0OOO000O00O .get (O0OOOOO0OOOO0O0OO )#line:30
    OOOOO00O0O0000O00 =OO0O0OO00O000O00O .loads (O0000O000O0O0OO0O .text )#line:31
    return OOOOO00O0O0000O00 #line:32
def main (OOOO0OO000OO000OO ):#line:35
    if OO0O000O00O0O0000 .system ()=="Windows":#line:36
        O0O0OO00O00OO0OO0 =input ('Price Percent Change? ')#line:37
        OOOO00O0000OO0OO0 =input ('Volume Percent Change? ')#line:38
    else :#line:39
        O0O0OO00O00OO0OO0 =input (O00O00OO0OOOO0OO0 .Fore .CYAN +'Price Percent Change? '+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:40
        OOOO00O0000OO0OO0 =input (O00O00OO0OOOO0OO0 .Fore .CYAN +'Volume Percent Change? '+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:41
    if OOOO0OO000OO000OO !=None :#line:42
        OO000OOO00O0O00O0 =O0O00OO000OO0OO0O .getBalance ('BTC')#line:43
        O0OOOO0O00000OO0O =O0O00OO000OO0OO0O .USD_BTC_Price ()#line:44
        OOOOOO0OO0000O0O0 =OO000OOO00O0O00O0 *O0OOOO0O00000OO0O #line:45
        print (O00O00OO0OOOO0OO0 .Fore .RED +'_____________________________________________________________________'+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:46
        print (O00O00OO0OOOO0OO0 .Fore .RED +'Balance (BTC): '+str (OO000OOO00O0O00O0 )+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:47
        print (O00O00OO0OOOO0OO0 .Fore .RED +'Balance in USD: '+str (OOOOOO0OO0000O0O0 )+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:48
        print (O00O00OO0OOOO0OO0 .Fore .RED +'_____________________________________________________________________'+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:49
        if OO0O000O00O0O0000 .system ()=="Windows":#line:50
            OOOO00000OOOO0O00 =input ('[1] Risk Multiplier: ')#line:51
            O0O0OO0O0O00OO00O =input ('[2] % of bitcoin to spend: ')#line:52
            O0OOOOOO0O0O0O0O0 =input ('[3] Profit %: ')#line:53
        else :#line:54
            OOOO00000OOOO0O00 =input (O00O00OO0OOOO0OO0 .Fore .CYAN +'[1] Risk Multiplier: '+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:55
            O0O0OO0O0O00OO00O =input (O00O00OO0OOOO0OO0 .Fore .CYAN +'[2] % of bitcoin to spend: '+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:56
            O0OOOOOO0O0O0O0O0 =input (O00O00OO0OOOO0OO0 .Fore .CYAN +'[3] Profit %: '+O00O00OO0OOOO0OO0 .Style .RESET_ALL )#line:57
        O0O0OO0O0O00OO00O ,O0OOOOOO0O0O0O0O0 =percentageFix (O0O0OO0O0O00OO00O ,O0OOOOOO0O0O0O0O0 )#line:58
    O0000OO0OO000OOO0 ,O0O0OOOO00000O00O =percentageFix (O0O0OO00O00OO0OO0 ,OOOO00O0000OO0OO0 )#line:59
    O00O000000OOO0OOO =market ()#line:60
    for OO00OOOOOOO0O0O00 in O00O000000OOO0OOO ['Data']:#line:61
        price .append (OO00OOOOOOO0O0O00 ['LastPrice'])#line:62
        volume .append (OO00OOOOOOO0O0O00 ['BaseVolume'])#line:63
        volumeDict [OO00OOOOOOO0O0O00 ['Label']]=[]#line:64
    O00OOO00OO0OOO00O =True #line:66
    OOOOO00OO0OOO00OO =1 #line:67
    OO0O00OOOOO00OO00 =O00O00OO0OOOO0OO0 .Fore .YELLOW +O00O00OO0OOOO0OO0 .Back .BLUE #line:68
    O00000OO00000OO0O =O00O00OO0OOOO0OO0 .Style .RESET_ALL #line:69
    OOOO000OOO00OO0O0 =O0O00O0000000O00O .getLogger ('test')#line:70
    OOOO000OOO00OO0O0 .critical ('working')#line:71
    print (' ')#line:72
    while 1 :#line:73
        if O00OOO00OO0OOO00O ==True :#line:74
            O00OOO000OO0O0000 =market ()#line:75
            while O00OOO000OO0O0000 ==None :#line:76
                O00OOO000OO0O0000 =market ()#line:77
            OOOOO00OO0OOO00OO +=1 #line:78
            for OO00OOOOOOO0O0O00 in O00OOO000OO0O0000 ['Data']:#line:79
                O00OOOO00000OO000 =O00OOO000OO0O0000 ['Data'].index (OO00OOOOOOO0O0O00 )#line:80
                if OO00OOOOOOO0O0O00 ['LastPrice']>price [O00OOOO00000OO000 ]+price [O00OOOO00000OO000 ]*float (O0000OO0OO000OOO0 )and OO00OOOOOOO0O0O00 ['BaseVolume']>volume [O00OOOO00000OO000 ]+volume [O00OOOO00000OO000 ]*float (O0O0OOOO00000O00O ):#line:81
                    O00O0O0O0OO00OO00 =str (OO00OOOOOOO0O0O00 ['LastPrice']/price [O00OOOO00000OO000 ])#line:82
                    OO0O00O00OO00OO00 =str (OO00OOOOOOO0O0O00 ['BaseVolume']/volume [O00OOOO00000OO000 ])#line:83
                    print (OO0O00OOOOO00OO00 +'Time: '+O00000OO00000OO0O +timestamp ())#line:84
                    print (OO0O00OOOOO00OO00 +'Name: '+O00000OO00000OO0O +OO00OOOOOOO0O0O00 ['Label'])#line:85
                    print (OO0O00OOOOO00OO00 +'Price % Change: '+O00000OO00000OO0O +O00O0O0O0OO00OO00 [2 :4 ]+'%')#line:86
                    print (OO0O00OOOOO00OO00 +'Volume % Change: '+O00000OO00000OO0O +OO0O00O00OO00OO00 [2 :4 ]+'%')#line:87
                    print (OO0O00OOOOO00OO00 +'Old Price: '+O00000OO00000OO0O +'%.8f'%price [O00OOOO00000OO000 ])#line:88
                    print (OO0O00OOOOO00OO00 +'New Price: '+O00000OO00000OO0O +'%.8f'%OO00OOOOOOO0O0O00 ['LastPrice'])#line:89
                    print (OO0O00OOOOO00OO00 +'Old Volume: '+O00000OO00000OO0O +'%.8f'%volume [O00OOOO00000OO000 ])#line:90
                    print (OO0O00OOOOO00OO00 +'New Volume: '+O00000OO00000OO0O +'%.8f'%OO00OOOOOOO0O0O00 ['BaseVolume'])#line:91
                    print ('------------------------------')#line:92
                    if OOOO0OO000OO000OO !=None :#line:93
                        OO000OOO00O0O00O0 =O0O00OO000OO0OO0O .getBalance ('BTC')#line:94
                        OO0000OOO0000O000 =OO000OOO00O0O00O0 *float (O0O0OO0O0O00OO00O )#line:95
                        O00O0000OO00OOO00 =OO00OOOOOOO0O0O00 ['Label'].split ('/')#line:96
                        O0O00OO000OO0OO0O .Trade (O00O0000OO00OOO00 [0 ],O0OOOOOO0O0O0O0O0 ,OO0000OOO0000O000 ,OOOO00000OOOO0O00 )#line:97
                    price [O00OOOO00000OO000 ]=OO00OOOOOOO0O0O00 ['LastPrice']#line:98
                    volume [O00OOOO00000OO000 ]=OO00OOOOOOO0O0O00 ['BaseVolume']#line:99
                else :#line:100
                    price [O00OOOO00000OO000 ]=OO00OOOOOOO0O0O00 ['LastPrice']#line:101
                    volume [O00OOOO00000OO000 ]=OO00OOOOOOO0O0O00 ['BaseVolume']#line:102
            OOO000O00O0OOOO0O .sleep (3 )#line:104
def timestamp ():#line:107
    return O0O00O00000O00OO0 ('%H:%M:%S',O0000O0OO0OO0OOOO ())#line:108
def percentageFix (O0000O0O00OO00OO0 ,OOOO0O0O0OOO0OO00 ):#line:111
    if len (O0000O0O00OO00OO0 )<=1 :#line:112
        O0000O0O00OO00OO0 ='0.0'+O0000O0O00OO00OO0 #line:113
    elif len (O0000O0O00OO00OO0 )<=2 :#line:114
        O0000O0O00OO00OO0 ='0.'+O0000O0O00OO00OO0 #line:115
    else :#line:116
        if len (O0000O0O00OO00OO0 )<=3 :#line:117
            O0000O0O00OO00OO0 =O0000O0O00OO00OO0 [0 ]+'.'+O0000O0O00OO00OO0 [1 :]#line:118
        else :#line:119
            O0000O0O00OO00OO0 =O0000O0O00OO00OO0 [0 :2 ]#line:120
    if len (OOOO0O0O0OOO0OO00 )<=1 :#line:121
        OOOO0O0O0OOO0OO00 ='0.0'+OOOO0O0O0OOO0OO00 #line:122
    elif len (OOOO0O0O0OOO0OO00 )<=2 :#line:123
        OOOO0O0O0OOO0OO00 ='0.'+OOOO0O0O0OOO0OO00 #line:124
    elif len (OOOO0O0O0OOO0OO00 )<=3 :#line:125
        OOOO0O0O0OOO0OO00 =OOOO0O0O0OOO0OO00 [0 ]+'.'+OOOO0O0O0OOO0OO00 [1 :]#line:126
    else :#line:127
        OOOO0O0O0OOO0OO00 =OOOO0O0O0OOO0OO00 [0 :2 ]#line:128
    return (O0000O0O00OO00OO0 ,OOOO0O0O0OOO0OO00 )
#e9015584e6a44b14988f13e2298bcbf9

