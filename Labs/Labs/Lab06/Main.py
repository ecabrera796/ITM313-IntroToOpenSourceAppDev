import Employee

name = input("Employee Name: ")
idNumber = input("Employee ID Number: ")
department = input("Employee Department: ")
position = input("Employee Position: ")

name2 = input("Second Employee Name: ")
idNumber2 = input("Second Employee ID Number: ")
department2 = input("Second Employee Department: ")
position2 = input("Second Employee Position: ")

name3 = input("Third Employee Name: ")
idNumber3 = input("Third Employee ID Number: ")
department3 = input("Third Employee Department: ")
position3 = input("Third Employee Position: ")

employee = Employee.Employee(name, idNumber, department, position)
employee2 = Employee.Employee(name2, idNumber2, department2, position2)
employee3 = Employee.Employee(name3, idNumber3, department3, position3)

employee.table()
employee2.table()
employee3.table()
