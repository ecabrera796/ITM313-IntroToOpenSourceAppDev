import Coin
import random

heads = 0
tails = 0

for i in range(20):
    HorT = random.randint(0,1)
    myCoin = Coin.Coin(HorT)
    HorT = int(HorT)
    if HorT == 0:
        myCoin.headsUp()
        heads += 1
    if HorT == 1:
        myCoin.tailsUp()
        tails += 1
print("Total Heads:", heads)
print("Total Tails:", tails) 