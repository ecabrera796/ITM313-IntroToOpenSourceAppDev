fahrenheit = float(input("Please enter temperature in Fahrenheit: "))
celsius = float(input("Please enter temperature in Celsius: "))

print("{0:16}{1:32}{2:14}{3:20}".format(chr(176)+"F", chr(176)+"F to "+chr(176)+"C", chr(176)+"C", chr(176)+"C to "+chr(176)+"F"))
print("{0:15}{1:30}{2:15}{3:20}".format("----------", "-----------", "---------", "-----------"))
for x in range(0,16):
    celsius += 1
    ctof = float(round((celsius*9/5) + 32, 2))
    fahrenheit += 1
    ftoc = float(round((fahrenheit-32) * 5/9, 2))
    print("{0:6}{1:17}{2:28}{3:16}".format(fahrenheit,round(ftoc,2), celsius,round(ctof,2)))