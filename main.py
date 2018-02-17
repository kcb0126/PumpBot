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
if __name__ =='__main__':#line:21
    log =OOO0000OOOO00OOO0 .getLogger ('test')#line:25
    log .debug (' _____ _____ _____ _____                            ')#line:26
    log .debug ('|  _  |  |  |     |  _  |                           ')#line:27
    log .debug ('|   __|  |  | | | |   __|                           ')#line:28
    log .debug ('|__|  |_____|_|_|_|__|                              ')#line:29
    log .debug ('                                           __ __ __ ')#line:30
    log .debug (' _____ _____ _____ _____ _____ _____ _____|  |  |  |')#line:31
    log .debug ('|     |  _  |     |  |  |     |   | |   __|  |  |  |')#line:32
    log .debug ('| | | |     |   --|     |-   -| | | |   __|__|__|__|')#line:33
    log .debug ('|_|_|_|__|__|_____|__|__|_____|_|___|_____|__|__|__|')#line:34
    log .debug (' _____ ___                                          ')#line:35
    log .debug ('|  |  |_  |                                         ')#line:36
    log .debug ('|  |  |  _|                                         ')#line:37
    log .debug (' \___/|___|                                         ')#line:38
    print ('')#line:39
    log .info ('Welcome to the pump machine!!!')#line:40
    print ('')#line:41
    log .info ('Please choose an exchange, 1 or 2: ')#line:42
    log .info ('[1]Bittrex')#line:43
    log .info ('[2]Yobit')#line:44
    log .info ('[3]Cryptopia')#line:45
    log .info ('[4]Poloniex')#line:46
    print ('')#line:47
    exchange =input ('')#line:48
    print ('')#line:49
    log .info ('Please choose an option: ')#line:50
    log .info ('[1]Auto Trader')#line:51
    log .info ('[2]Pump and Dump Detector')#line:52
    log .info ('[3]Auto Trader with Pump and Dump Detector')#line:53
    print ('')#line:55
    option =input ('')#line:56
    if exchange =='1':#line:57
        if option =='1':#line:58
            O0OO00000O0000O0O .main ()#line:59
        if option =='2':#line:60
            auto =None #line:61
            OOOO00O0000O000OO .main (auto )#line:62
        if option =='3':#line:63
            auto =1 #line:64
            OOOO00O0000O000OO .main (auto )#line:65
    elif exchange =='2':#line:66
        if option =='1':#line:67
            O0OO000O000OOO0O0 .main ()#line:68
        if option =='2':#line:69
            auto =None #line:70
            OOO000000OOOOO0OO .main (auto )#line:71
        if option =='3':#line:72
            auto =1 #line:73
            OOO000000OOOOO0OO .main (auto )#line:71
    elif exchange =='3':#line:74
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
#e9015584e6a44b14988f13e2298bcbf9


