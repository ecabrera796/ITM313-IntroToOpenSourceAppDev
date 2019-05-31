class Employee:
    def __init__(self, name, idNumber, department, position):
        self.name = name
        self.idNumber = idNumber
        self.department = department
        self.position = position

    def table(self):
        print("Name:", self.name)
        print("ID Number:", self.idNumber)
        print("Department:", self.department)
        print("Position:", self.position + "\n")
