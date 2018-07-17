import time

import msvcrt


def percentageFix(pricepercent, volumepercent):
    if len(pricepercent) <= 1:
        pricepercent = '0.0' + pricepercent
    elif len(pricepercent) <= 2:
        pricepercent = '0.' + pricepercent
    else:
        if len(pricepercent) <= 3:
            pricepercent = pricepercent[0] + '.' + pricepercent[1:]
        else:
            pricepercent = pricepercent[0:2]
    if len(volumepercent) <= 1:
        volumepercent = '0.0' + volumepercent
    elif len(volumepercent) <= 2:
        volumepercent = '0.' + volumepercent
    elif len(volumepercent) <= 3:
        volumepercent = volumepercent[0] + '.' + volumepercent[1:]
    else:
        volumepercent = volumepercent[0:2]
    return (pricepercent, volumepercent)

def input_with_timeout(timeout=30.0):
    finishat = time.time() + timeout
    result = []
    while True:
        if msvcrt.kbhit():
            result.append(msvcrt.getche())
            if result[-1] == b'\r':   # or \n, whatever Win returns;-)
                return bytes.join(b'', result[:-1]).decode('utf-8')
            time.sleep(0.1)          # just to yield to other processes/threads
        else:
            if time.time() > finishat:
                return None

def input_key_timeout(timeout=30.0):
    finishat = time.time() + timeout
    result = []
    while True:
        if msvcrt.kbhit():
            result.append(msvcrt.getche())
            return bytes.join(b'', result).decode('utf-8')
            time.sleep(0.1)          # just to yield to other processes/threads
        else:
            if time.time() > finishat:
                return None
