from random import *

def lotto() :
    lot = set()
    while len(lot) < 6 :
        lot.add(randint(1, 45))

    lot = list(lot)
    lot.sort()
    print(lot)

lotto()

