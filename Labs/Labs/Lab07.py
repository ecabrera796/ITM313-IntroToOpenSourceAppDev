import random
from array import *

# user = []
# for i in range(5):
#     n = input("Enter your lottery picks: ")
#     user.append(int(n))
# print(user)

lottery = []
for i in range(5):
    x = random.randint(0, 9)
    if x in lottery:
        y = random.randint(0, 9)
        lottery.append(y)
    if x not in lottery:
        lottery.append(x)
print("Lottery numbers:", str(lottery))

user = []
for i in range(5):
    n = input("Enter your lottery picks: ")
    user.append(int(n))
print(user)

if user == lottery:
    print("You are the grand winner!")
else:
    num = 0
    num = int(num)

    element = []
    for i in range(5):
        if user[num] == lottery[num]:
            element.append(user[num])
            num += 1
        else:
            print("This element did not match:", str(num))
            num += 1
    print("You have matching number(s):", str(element))
