
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
