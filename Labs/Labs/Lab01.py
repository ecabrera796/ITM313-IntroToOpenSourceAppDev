x = int(input("Please enter a number: "))
y = int(input("Please enter a second number: "))
add = x + y
print("x + y = ",add)
sub = x - y
print("x - y = ",sub)
mult = x * y
print("x * y = ",mult)
div = x / y
print("x % y = ",round(div,3))
mod = x % y
print("x % y = ",mod)

celsius = float(input("Enter a temperture in Celsius: "))
fahrenheit = 9/5 * celsius + 32
print("Temperature: ", celsius, chr(176), "C =", round(fahrenheit,2), chr(176), "F")

sFahrenheit = float(input("Enter a temperature in Fahrenheit: "))
sCelsius = (sFahrenheit-32) * 5/9
print("Temperature: ", sFahrenheit, chr(176), "F =", round(sCelsius,2), chr(176), "C")