rows = 10
print("{0:30}{1:30}".format("Pattern A", "Pattern B"))
print("-----------------------------------------")
for i in range(rows):
    print("{0:30}{1:30}".format("*"*(i+1), "*"*(rows-i)))
