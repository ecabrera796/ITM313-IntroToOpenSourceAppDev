num1 = float(input("Please enter a number: "))
num2 = float(input("Please enter a second number: "))

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

def presentValue(fv, r, n):
    p = (fv / ((1+(r/100)) ** n))
    print("You would need to deposit", round(p,2), "in order to have", round(fv,2), "in 10 years at an interest rate of", round(r,3))

def main():
    a = add(num1, num2)
    s = sub(num1, num2)
    m = mult(num1, num2)
    d = div(num1, num2)
    print("Addition:", round(a,2))
    print("Subtraction:", round(s,2))
    print("Multiplication:", round(m,2))
    print("Division:", round(d,2))

    print("--------------------------------------------------------------------------------------------------------------------")

    fv = float(input("How much would you like to have in your account in 10 years? "))
    r = float(input("What interest rate would you like? "))
    n = 10
    presentValue(fv, r, n)

main()