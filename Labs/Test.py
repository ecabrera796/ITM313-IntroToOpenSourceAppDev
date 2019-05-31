# import turtle


# def main():
#     t = turtle.Turtle()
#     t.hideturtle()
#     t.speed(10)
#     level = 12
#     fract(t, -80, 60, 80, 60, level)


# def fract(t, x1, y1, x2, y2, level):
#     newX = 10
#     newY = 10
#     if level == 0:
#         drawLine(t, x1, y1, x2, y2)
#     else:
#         newX = (x1+x2)/2 + (y2-y1)/2
#         newY = (y1+y2)/2 - (x2-x1)/2
#         fract(t, x1, y1, newX, newY, level - 1)
#         fract(t, newX, newY, x2, y2, level - 1)


# def drawLine(t, x1, y1, x2, y2):
#     t.up()
#     t.goto(x1, y1)
#     t.down()
#     t.goto(x2, y2)


# main()

###############################################################################################

import student


def main():
    listOfStudents = obtainListofStudents()
    displayResults(listOfStudents)


def obtainListofStudents():
    listOfStudents = []
    carryOn = 'Y'
    while carryOn == 'Y'
       name = input("Enter student's name: ")
        midterm = float(input("Enter student's grade on midterm exam: "))
        final = float(input("Enter student's grade on fnal exam: "))
        categoryy = input("Enter category (LG or PF): ")
           if category.upper() == "LG":
                st = student.LGstudent(name, midterm, final)
            else:
                st = student.PFstudent(name, midterm, final)
            listOfStudents.append(st)
            carryON = input("Do you want to continue (Y/N)?")
            carryON = carryON.upper()
        return listOfStudents


def displayResults(listOfStudents):
    print("\nNAME\tGRADE")
       listOfStudents.sort(key=lambda x: x.getName())
        for pupil in listOfStudents:
            print(pupil)

main()
