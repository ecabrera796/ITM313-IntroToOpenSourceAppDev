
name = input("Please enter your first and last name: ")
hours = float(input("How many hours do you work per week? "))
rate = 10.50
print(name, "your hourly pay rate is $10.50.")
weekly = hours * rate
print("Your weekly pay is $",weekly)
biweekly = (hours * rate) * 2
print("Your biweekly pay is $",biweekly)
monthly = (hours * rate) * 4.35  #best way for approximation of weeks in a month
print("Your monthly pay is $", round(monthly,2))
yearly = (hours * rate) * 52.14  #best way for approximation of weeks in a year
print("Your yearly pay is $", round(yearly,2))