from EVGA.EVGABot import EVGABot

item = None
flag = False

while not flag:
    with EVGABot() as driver:
        while item is None:
            item = driver.findItem()
            if item == True:
                flag = driver.script()
            elif item == False:
                break
    if flag:
        break
    with EVGABot(False, False) as driver:
        item = driver.findItem()
        if item == True:
            flag = driver.script()

with EVGABot(True, False) as close:
    print("Purchased")
