import colorama as OO00O0O00OOO0O0O0 #line:9
import logger as OOO0000OOOO00OOO0 #line:10
import BittrexBot as O0OO00000O0000O0O #line:11
import BittrexPumpDetector as OOOO00O0000O000OO #line:12
import YobitPumpDetector as OOO000000OOOOO0OO #line:13
import YobitBot as O0OO000O000OOO0O0 #line:14
import CryptopiaBot as OOO0000OO0000O00O #line:15
import CryptopiaPumpDetector as OOO00O0O0OOOO0000 #line:16
import PoloniexBot as O00OO00O00OOOO0O0 #line:17
import PoloniexPumpDetector as OOOOOO0OOO0000O0O #line:18
import BinanceBot
import colorama
import requests
import uuid

baseurl = 'https://www.cluely.eu/'
loginurl = baseurl + 'user/login.php'

def callapi(url, params):
    data = requests.post(url, params).json()
    if data['success'] == 1:
        return True
    else:
        print(data['message'])
        return False

def get_uuid():
    return ''.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1])

if __name__ =='__main__':#line:21
    log =OOO0000OOOO00OOO0 .getLogger ('test')#line:25
#    log .debug (' _____ _____ _____ _____                            ')#line:26
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '                         _          ')#test color
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '                        | |         ')#line:27
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '    ___ _ __ _   _ _ __ | |_ ___    ')#line:28
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '   / __|  __| | | |  _ \| __/ _ \   ')#line:29
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '  | (__| |  | |_| | |_) | || (_) |  ')#line:30
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '   \___|_|   \__, | .__/ \__\___/   ')#line:31
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '              __/ | |               ')#line:32
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '         _ _ |___/|_|               ')#line:33
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '        (_| |  (_)           v1.0   ')#line:34
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '  __   ___| | ___ _ __   __ _ ___   ')#line:35
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '  \ \ / | | |/ | |  _ \ / _  / __|  ')#line:36
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '   \ V /| |   <| | | | | (_| \_ \   ')#line:37
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '    \_/ |_|_|\_|_|_| |_|\__, |___/  ')#line:38
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '                                    ')#line:39
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '                                    ')#line:39
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '                                    ')#line:39
    print(colorama.Fore.LIGHTBLUE_EX + colorama.Back.LIGHTWHITE_EX + '                                    ')#line:39
    print('')
    print('')
    print(colorama.Fore.LIGHTCYAN_EX + colorama.Back.BLACK + 'Welcome to Crypto Vikings v1.0')#line:40
    print ('')#line:41

    while True:
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        print('')
        print('')
        if callapi(loginurl, {'email':email, 'password':password, 'uuid':get_uuid()}):
            break
        else:
            toquit = input('Quit? (0=No | 1=Yes)')
            print('')
            if toquit == '1':
                exit()
    while True:
        print(colorama.Fore.LIGHTWHITE_EX + 'Please choose an exchange, 1 or 2: ')#line:42
        print(colorama.Fore.LIGHTWHITE_EX + '[1]Cryptopia')#line:43
        print(colorama.Fore.LIGHTWHITE_EX + '[2]Yobit')#line:44
        print(colorama.Fore.LIGHTWHITE_EX + '[3]Binance')#line:45
        #print(colorama.Fore.LIGHTWHITE_EX + '[4]Poloniex')#line:46
        print ('')#line:47
        exchange =input ('')#line:48 # input exchange type
        #exchange = '3'
        print ('')#line:49
        #print(colorama.Fore.LIGHTWHITE_EX + 'Please choose an option: ')#line:50
        #print(colorama.Fore.LIGHTWHITE_EX + '[1]Auto Trader')#line:51
        #print(colorama.Fore.LIGHTWHITE_EX + '[2]Pump and Dump Detector')#line:52
        #print(colorama.Fore.LIGHTWHITE_EX + '[3]Auto Trader with Pump and Dump Detector')#line:53
        #print ('')#line:55
        #option =input ('')#line:56    #input option : Auto | Pump&Dump | Auto & PUmp
        option = '1'
        if exchange =='3':#line:57
            if option =='1':#line:58
                BinanceBot .main ()#line:59
            if option =='2':#line:60
                auto =None #line:61
                BinanceBot .main (auto )#line:62
            if option =='3':#line:63
                auto =1 #line:64
                BinanceBot .main (auto )#line:65
        elif exchange =='2':#line:66
            if option =='1':#line:67
                O0OO000O000OOO0O0 .main ()#line:68
            if option =='2':#line:69
                auto =None #line:70
                OOO000000OOOOO0OO .main (auto )#line:71
            if option =='3':#line:72
                auto =1 #line:73
                OOO000000OOOOO0OO .main (auto )#line:71
        elif exchange =='1':#line:74
            if option =='1':#line:75
                OOO0000OO0000O00O .main ()#line:76
            if option =='2':#line:77
                auto =None #line:78
                OOO00O0O0OOOO0000 .main (auto )#line:79
            if option =='3':#line:80
                auto =1 #line:81
                OOO00O0O0OOOO0000 .main (auto )#line:82
        elif exchange =='4':#line:83
            if option =='1':#line:84
                O00OO00O00OOOO0O0 .main ()#line:85
            if option =='2':#line:86
                auto =None #line:87
                OOOOOO0OOO0000O0O .main (auto )#line:88
            if option =='3':#line:89
                auto =1 #line:90
                OOOOOO0OOO0000O0O .main (auto )#line:91
        else :#line:92
            print ("Not a valid option!")
        print('')
        print('')
        print('')
#e9015584e6a44b14988f13e2298bcbf9


