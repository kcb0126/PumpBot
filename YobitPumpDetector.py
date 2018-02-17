import json as O000O0OO000OOO000 #line:8
import requests as O0OOOOOOOO00OOOOO #line:9
from time import strftime as OOO0O000OOOOO0OOO ,gmtime as O0OO00000O0O00000 #line:10
import time as OOO00OO0OOOOOO0O0 #line:11
import hmac as O00O00O0OOO000OOO #line:12
import pickle as O0O0O000O0OOO0O00 #line:13
import hashlib as OO000OO00O0O0O00O #line:14
import pprint as OOOO0O00000OOO0OO #line:15
import grequests as OOOO0000O0000000O #line:16
try :#line:17
    from urllib import urlencode as O000O00OOO0OO0O00 #line:18
    from urlparse import urljoin as OO0000O00OO0OO00O #line:19
except ImportError :#line:20
    from urllib .parse import urlencode as O000O00OOO0OO0O00 #line:21
    from urllib .parse import urljoin as OO0000O00OO0OO00O #line:22
import logger as OO0OOO0O0OO0OOO0O #line:24
import colorama as OO0O0O00OOO0OO00O #line:25
import YobitBot as O0OOOO00000O00O0O #line:26
import platform
import configparser as O0OO00O0O0O000O00 #line:27
config =O0OO00O0O0O000O00 .ConfigParser ()#line:28
config .readfp (open ('config.txt'))#line:29
key =config .get ('Yobit','Key')#line:30
secret =config .get ('Yobit','Secret')#line:31
price =[]#line:32
volume =[]#line:33
priceNew =[]#line:34
volumeNew =[]#line:35
names =[]#line:36
querys =[]#line:37
def getQueries ():#line:39
    O00O0000OOOOOOO0O =''#line:40
    O00O00O000OOOO00O =''#line:41
    OO000OOO0O000OO0O =''#line:42
    OOO0000O00O0OO0O0 =''#line:43
    OO0OO0O000O000000 =''#line:44
    OO0O0OOOO0OO00OOO =''#line:45
    OOOO00OOOO0OO0O0O =''#line:46
    O0OOO000O000O0O00 =''#line:47
    O00O0O00OO000OOOO =''#line:48
    OO0OO00OO00OOO0OO =''#line:49
    O0O0O0OOO0OO0O000 =''#line:50
    O00OO0000OO0O00OO =''#line:51
    O0O0O00O0O000O0OO =''#line:52
    OO00OOO0OOO0O0O00 =''#line:53
    OO0O0OOO00OOOO000 =''#line:54
    O00O0O0O0OO00OO00 =''#line:55
    O000OOO00O0O00000 =''#line:56
    O0000OOOO00O0O00O =''#line:57
    OO000O0O0O0000O0O =''#line:58
    with open ('pairs.txt','rb')as O000O0OO00O0000OO :#line:59
        OO0OO0OO0000O0OO0 =O0O0O000O0OOO0O00 .load (O000O0OO00O0000OO )#line:60
    OOOOO0OO00O000OOO =0 #line:61
    for O0OO0OO000O0O0OO0 in OO0OO0OO0000O0OO0 :#line:62
        if OOOOO0OO00O000OOO <=50 :#line:63
            O00O0000OOOOOOO0O +=str (O0OO0OO000O0O0OO0 )+'-'#line:64
            OOOOO0OO00O000OOO +=1 #line:65
        if OOOOO0OO00O000OOO >50 and OOOOO0OO00O000OOO <=100 :#line:66
            O00O00O000OOOO00O +=str (O0OO0OO000O0O0OO0 )+'-'#line:67
            OOOOO0OO00O000OOO +=1 #line:68
        if OOOOO0OO00O000OOO >100 and OOOOO0OO00O000OOO <=150 :#line:69
            OO000OOO0O000OO0O +=str (O0OO0OO000O0O0OO0 )+'-'#line:70
            OOOOO0OO00O000OOO +=1 #line:71
        if OOOOO0OO00O000OOO >150 and OOOOO0OO00O000OOO <=200 :#line:72
            OOO0000O00O0OO0O0 +=str (O0OO0OO000O0O0OO0 )+'-'#line:73
            OOOOO0OO00O000OOO +=1 #line:74
        if OOOOO0OO00O000OOO >200 and OOOOO0OO00O000OOO <=250 :#line:75
            OO0OO0O000O000000 +=str (O0OO0OO000O0O0OO0 )+'-'#line:76
            OOOOO0OO00O000OOO +=1 #line:77
        if OOOOO0OO00O000OOO >250 and OOOOO0OO00O000OOO <=300 :#line:78
            OO0O0OOOO0OO00OOO +=str (O0OO0OO000O0O0OO0 )+'-'#line:79
            OOOOO0OO00O000OOO +=1 #line:80
        if OOOOO0OO00O000OOO >300 and OOOOO0OO00O000OOO <=350 :#line:81
            OOOO00OOOO0OO0O0O +=str (O0OO0OO000O0O0OO0 )+'-'#line:82
            OOOOO0OO00O000OOO +=1 #line:83
        if OOOOO0OO00O000OOO >350 and OOOOO0OO00O000OOO <=400 :#line:84
            O0OOO000O000O0O00 +=str (O0OO0OO000O0O0OO0 )+'-'#line:85
            OOOOO0OO00O000OOO +=1 #line:86
        if OOOOO0OO00O000OOO >400 and OOOOO0OO00O000OOO <=450 :#line:87
            O00O0O00OO000OOOO +=str (O0OO0OO000O0O0OO0 )+'-'#line:88
            OOOOO0OO00O000OOO +=1 #line:89
        if OOOOO0OO00O000OOO >450 and OOOOO0OO00O000OOO <=500 :#line:90
            OO0OO00OO00OOO0OO +=str (O0OO0OO000O0O0OO0 )+'-'#line:91
            OOOOO0OO00O000OOO +=1 #line:92
        if OOOOO0OO00O000OOO >500 and OOOOO0OO00O000OOO <=550 :#line:93
            O0O0O0OOO0OO0O000 +=str (O0OO0OO000O0O0OO0 )+'-'#line:94
            OOOOO0OO00O000OOO +=1 #line:95
        if OOOOO0OO00O000OOO >550 and OOOOO0OO00O000OOO <=600 :#line:96
            O00OO0000OO0O00OO +=str (O0OO0OO000O0O0OO0 )+'-'#line:97
            OOOOO0OO00O000OOO +=1 #line:98
        if OOOOO0OO00O000OOO >600 and OOOOO0OO00O000OOO <=650 :#line:99
            O0O0O00O0O000O0OO +=str (O0OO0OO000O0O0OO0 )+'-'#line:100
            OOOOO0OO00O000OOO +=1 #line:101
        if OOOOO0OO00O000OOO >650 and OOOOO0OO00O000OOO <=700 :#line:102
            OO00OOO0OOO0O0O00 +=str (O0OO0OO000O0O0OO0 )+'-'#line:103
            OOOOO0OO00O000OOO +=1 #line:104
        if OOOOO0OO00O000OOO >700 and OOOOO0OO00O000OOO <=750 :#line:105
            OO0O0OOO00OOOO000 +=str (O0OO0OO000O0O0OO0 )+'-'#line:106
            OOOOO0OO00O000OOO +=1 #line:107
        if OOOOO0OO00O000OOO >750 and OOOOO0OO00O000OOO <=800 :#line:108
            O00O0O0O0OO00OO00 +=str (O0OO0OO000O0O0OO0 )+'-'#line:109
            OOOOO0OO00O000OOO +=1 #line:110
        if OOOOO0OO00O000OOO >800 and OOOOO0OO00O000OOO <=850 :#line:111
            O000OOO00O0O00000 +=str (O0OO0OO000O0O0OO0 )+'-'#line:112
            OOOOO0OO00O000OOO +=1 #line:113
        if OOOOO0OO00O000OOO >850 and OOOOO0OO00O000OOO <=900 :#line:114
            O0000OOOO00O0O00O +=str (O0OO0OO000O0O0OO0 )+'-'#line:115
            OOOOO0OO00O000OOO +=1 #line:116
        if OOOOO0OO00O000OOO >900 and OOOOO0OO00O000OOO <=950 :#line:117
            OO000O0O0O0000O0O +=str (O0OO0OO000O0O0OO0 )+'-'#line:118
            OOOOO0OO00O000OOO +=1 #line:119
    querys .append (O00O0000OOOOOOO0O [:-1 ])#line:121
    querys .append (O00O00O000OOOO00O [:-1 ])#line:122
    querys .append (OO000OOO0O000OO0O [:-1 ])#line:123
    querys .append (OOO0000O00O0OO0O0 [:-1 ])#line:124
    querys .append (OO0OO0O000O000000 [:-1 ])#line:125
    querys .append (OO0O0OOOO0OO00OOO [:-1 ])#line:126
    querys .append (OOOO00OOOO0OO0O0O [:-1 ])#line:127
    querys .append (O0OOO000O000O0O00 [:-1 ])#line:128
    querys .append (O00O0O00OO000OOOO [:-1 ])#line:129
    querys .append (OO0OO00OO00OOO0OO [:-1 ])#line:130
    querys .append (O0O0O0OOO0OO0O000 [:-1 ])#line:131
    querys .append (O00OO0000OO0O00OO [:-1 ])#line:132
    querys .append (O0O0O00O0O000O0OO [:-1 ])#line:133
    querys .append (OO00OOO0OOO0O0O00 [:-1 ])#line:134
    querys .append (OO0O0OOO00OOOO000 [:-1 ])#line:135
    OO0OOOOOOO0000OOO ='https://yobit.net/api/3/ticker/'#line:136
    OO0O000O0OOO0OOOO =(OOOO0000O0000000O .get (OO0OOOOOOO0000OOO +O0OOOO0OO00O0O0OO ,headers ={'apisign':O00O00O0OOO000OOO .new (secret .encode (),O0OOOO0OO00O0O0OO .encode (),OO000OO00O0O0O00O .sha512 ).hexdigest ()})for O0OOOO0OO00O0O0OO in querys )#line:137
    O0O0OOO0OO0OOOO00 =OOOO0000O0000000O .map (OO0O000O0OOO0OOOO )#line:138
    O00O0O0000O000O00 =[OOO0OOOO0O00O00OO .json ()for OOO0OOOO0O00O00OO in O0O0OOO0OO0OOOO00 ]#line:139
    for OO00O0OOO000000O0 in O00O0O0000O000O00 :#line:140
        for O0OO0O0O0O0O000O0 in OO00O0OOO000000O0 :#line:141
            OO0O0OO0O0OOO0O0O =O0OO0O0O0O0O000O0 #line:142
            volume .append (OO00O0OOO000000O0 [OO0O0OO0O0OOO0O0O ]['vol'])#line:143
            price .append (OO00O0OOO000000O0 [OO0O0OO0O0OOO0O0O ]['last'])#line:144
            names .append (OO0O0OO0O0OOO0O0O )#line:145
def updatePrices ():#line:148
    O0000OOO0O00000OO ='https://yobit.net/api/3/ticker/'#line:149
    O0O0000OOO0OO0O0O =(OOOO0000O0000000O .get (O0000OOO0O00000OO +O0O00O00OO0OOOO0O ,headers ={'apisign':O00O00O0OOO000OOO .new (secret .encode (),O0O00O00OO0OOOO0O .encode (),OO000OO00O0O0O00O .sha512 ).hexdigest ()})for O0O00O00OO0OOOO0O in querys )#line:150
    O0O00O00O000O0O0O =None #line:151
    while O0O00O00O000O0O0O ==None :#line:153
        O0O00O00O000O0O0O =OOOO0000O0000000O .map (O0O0000OOO0OO0O0O )#line:154
    O000O0O00OO0OO0OO =[OOO0OOO00O00OOO0O .json ()for OOO0OOO00O00OOO0O in O0O00O00O000O0O0O ]#line:156
    for O0O00O0OOOOOO0OOO in O000O0O00OO0OO0OO :#line:157
        for OOOOO00OOOOOOO000 in O0O00O0OOOOOO0OOO :#line:158
            OO00OOO0O0OOOOO0O =OOOOO00OOOOOOO000 #line:159
            volumeNew .append (O0O00O0OOOOOO0OOO [OO00OOO0O0OOOOO0O ]['vol'])#line:160
            priceNew .append (O0O00O0OOOOOO0OOO [OO00OOO0O0OOOOO0O ]['last'])#line:161
            names .append (OO00OOO0O0OOOOO0O )#line:162
def main (O00O0O00OOO0000OO ):#line:165
    O00000OOOO00OOO00 =True #line:166
    getQueries ()#line:167
    OO0OO0O000O0000OO =OO0OOO0O0OO0OOO0O .getLogger ('test')#line:168
    if platform .system ()=="Windows":#line:169
        O000OO0OOO00OO000 =input ('Price Percent Change? ')#line:170
        O0OOOO000OOO00O0O =input ('Volume Percent Change? ')#line:171
    else :#line:172
        O000OO0OOO00OO000 =input (OO0O0O00OOO0OO00O .Fore .CYAN +'Price Percent Change? '+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:173
        O0OOOO000OOO00O0O =input (OO0O0O00OOO0OO00O .Fore .CYAN +'Volume Percent Change? '+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:174
    if O00O0O00OOO0000OO !=None :#line:175
        OOO0O0OOO00O0000O =O0OOOO00000O00O0O .getBalance ('btc')#line:176
        O0OO0O0O000O0O00O =O0OOOO00000O00O0O .USD_BTC_Price ()#line:177
        O0O0O00000OO00O0O =OOO0O0OOO00O0000O *O0OO0O0O000O0O00O #line:178
        print (OO0O0O00OOO0OO00O .Fore .RED +'_____________________________________________________________________'+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:179
        print (OO0O0O00OOO0OO00O .Fore .RED +'Balance (BTC): '+str (OOO0O0OOO00O0000O )+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:180
        print (OO0O0O00OOO0OO00O .Fore .RED +'Balance in USD: '+str (O0O0O00000OO00O0O )+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:181
        print (OO0O0O00OOO0OO00O .Fore .RED +'_____________________________________________________________________'+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:182
        if platform .system ()=="Windows":#line:183
            O0O00OOO00000O000 =input ('[1] Risk Multiplier: ')#line:184
            OOOOOOOOO000000O0 =input ('[2] % of bitcoin to spend: ')#line:185
            O0OO000OO000000O0 =input ('[3] Profit %: ')#line:186
        else :#line:187
            O0O00OOO00000O000 =input (OO0O0O00OOO0OO00O .Fore .CYAN +'[1] Risk Multiplier: '+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:188
            OOOOOOOOO000000O0 =input (OO0O0O00OOO0OO00O .Fore .CYAN +'[2] % of bitcoin to spend: '+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:189
            O0OO000OO000000O0 =input (OO0O0O00OOO0OO00O .Fore .CYAN +'[3] Profit %: '+OO0O0O00OOO0OO00O .Style .RESET_ALL )#line:190
        OOOOOOOOO000000O0 ,O0OO000OO000000O0 =percentageFix (OOOOOOOOO000000O0 ,O0OO000OO000000O0 )#line:191
    O0000O000O000O0O0 ,OO0O0000O0000O0OO =percentageFix (O000OO0OOO00OO000 ,O0OOOO000OOO00O0O )#line:192
    O0O0OOO0OO0OOOOO0 =OO0O0O00OOO0OO00O .Fore .YELLOW +OO0O0O00OOO0OO00O .Back .BLUE #line:193
    O000O0000O0O0OO00 =OO0O0O00OOO0OO00O .Style .RESET_ALL #line:194
    OO0OO0O000O0000OO .critical ('working')#line:195
    print (' ')#line:196
    while 1 :#line:197
        if O00000OOOO00OOO00 ==True :#line:198
            updatePrices ()#line:199
            for O0OOO0O0O0OOOO000 in priceNew :#line:200
                O0O0O0O0O0OO000OO =priceNew .index (O0OOO0O0O0OOOO000 )#line:201
                if float (O0OOO0O0O0OOOO000 )>float (price [O0O0O0O0O0OO000OO ])+float (price [O0O0O0O0O0OO000OO ])*float (O0000O000O000O0O0 )and float (volumeNew [O0O0O0O0O0OO000OO ])>float (volume [O0O0O0O0O0OO000OO ])+float (volume [O0O0O0O0O0OO000OO ])*float (OO0O0000O0000O0OO ):#line:202
                    O0OO0O00OO000OO0O =str (O0OOO0O0O0OOOO000 /price [O0O0O0O0O0OO000OO ])#line:203
                    O0OOOO00O00OOOOO0 =str (volumeNew [O0O0O0O0O0OO000OO ]/volume [O0O0O0O0O0OO000OO ])#line:204
                    print (O0O0OOO0OO0OOOOO0 +'Time: '+O000O0000O0O0OO00 +OOO0O000OOOOO0OOO ('%H:%M:%S',O0OO00000O0O00000 ()))#line:205
                    print (O0O0OOO0OO0OOOOO0 +'Name: '+O000O0000O0O0OO00 +names [O0O0O0O0O0OO000OO ])#line:206
                    print (O0O0OOO0OO0OOOOO0 +'Price % Change: '+O000O0000O0O0OO00 +O0OO0O00OO000OO0O [2 :4 ]+'%')#line:207
                    print (O0O0OOO0OO0OOOOO0 +'Volume % Change: '+O000O0000O0O0OO00 +O0OOOO00O00OOOOO0 [2 :4 ]+'%')#line:208
                    print (O0O0OOO0OO0OOOOO0 +'Old Price: '+O000O0000O0O0OO00 +'%.8f'%price [O0O0O0O0O0OO000OO ])#line:209
                    print (O0O0OOO0OO0OOOOO0 +'New Price: '+O000O0000O0O0OO00 +'%.8f'%O0OOO0O0O0OOOO000 )#line:210
                    print (O0O0OOO0OO0OOOOO0 +'Old Volume: '+O000O0000O0O0OO00 +'%.8f'%volume [O0O0O0O0O0OO000OO ])#line:211
                    print (O0O0OOO0OO0OOOOO0 +'New Volume: '+O000O0000O0O0OO00 +'%.8f'%volumeNew [O0O0O0O0O0OO000OO ])#line:212
                    print ('--------------------------------')#line:213
                    if O00O0O00OOO0000OO !=None :#line:214
                        OOO0O0OOO00O0000O =O0OOOO00000O00O0O .getBalance ('btc')#line:215
                        OOO0OOO0O0OO0OO0O =OOO0O0OOO00O0000O *float (OOOOOOOOO000000O0 )#line:216
                        O0OOO0OOO000O0000 =names [O0O0O0O0O0OO000OO ].split ('_')#line:217
                        O0OOOO00000O00O0O .Trade (O0OOO0OOO000O0000 [0 ],O0OO000OO000000O0 ,OOO0OOO0O0OO0OO0O ,O0O00OOO00000O000 )#line:218
                    price [O0O0O0O0O0OO000OO ]=O0OOO0O0O0OOOO000 #line:219
                    volume [O0O0O0O0O0OO000OO ]=volumeNew [O0O0O0O0O0OO000OO ]#line:220
                else :#line:221
                    price [O0O0O0O0O0OO000OO ]=O0OOO0O0O0OOOO000 #line:222
                    volume [O0O0O0O0O0OO000OO ]=volumeNew [O0O0O0O0O0OO000OO ]#line:223
            volumeNew [:]=[]#line:225
            priceNew [:]=[]#line:226
            names [:]=[]#line:227
            OOO00OO0OOOOOO0O0 .sleep (3 )#line:228
def percentageFix (O0000OO0OOO00OOOO ,OOO00OO0OOOOO000O ):#line:231
    if len (O0000OO0OOO00OOOO )<=1 :#line:232
        O0000OO0OOO00OOOO ='0.0'+O0000OO0OOO00OOOO #line:233
    elif len (O0000OO0OOO00OOOO )<=2 :#line:234
        O0000OO0OOO00OOOO ='0.'+O0000OO0OOO00OOOO #line:235
    else :#line:236
        if len (O0000OO0OOO00OOOO )<=3 :#line:237
            O0000OO0OOO00OOOO =O0000OO0OOO00OOOO [0 ]+'.'+O0000OO0OOO00OOOO [1 :]#line:238
        else :#line:239
            O0000OO0OOO00OOOO =O0000OO0OOO00OOOO [0 :2 ]#line:240
    if len (OOO00OO0OOOOO000O )<=1 :#line:241
        OOO00OO0OOOOO000O ='0.0'+OOO00OO0OOOOO000O #line:242
    elif len (OOO00OO0OOOOO000O )<=2 :#line:243
        OOO00OO0OOOOO000O ='0.'+OOO00OO0OOOOO000O #line:244
    elif len (OOO00OO0OOOOO000O )<=3 :#line:245
        OOO00OO0OOOOO000O =OOO00OO0OOOOO000O [0 ]+'.'+OOO00OO0OOOOO000O [1 :]#line:246
    else :#line:247
        OOO00OO0OOOOO000O =OOO00OO0OOOOO000O [0 :2 ]#line:248
    return (O0000OO0OOO00OOOO ,OOO00OO0OOOOO000O )
#e9015584e6a44b14988f13e2298bcbf9

