# def triangle():
#     print("\n")
#     rows = 10
#     for i in range(rows):
#         print("*"*(i+1))
#     print("\n")


# def square():
#     print("\n")
#     rows = 10
#     columns = 20

#     for i in range(1, rows+1):
#         for j in range(1, columns+1):
#             if (i == 1 or i == rows or
#                     j == 1 or j == columns):
#                 print("*", end="")
#             else:
#                 print(" ", end="")

#         print()
#     print("\n")


# def rTriangle():
#     print("\n")
#     rows = 10
#     for i in range(rows):
#         print("*"*(rows-i))
#     print("\n")


# def bowtie():
#     print("\n")
#     num = 11
#     center = (num - 1)//2
#     for row in range(num):
#         spaces = 2*abs(row - center)
#         stars = num - spaces
#         print(stars*'*' + 2*spaces*' ' + stars*'*')
#     print("\n")


# def exit():
#     bye = print("\nSee ya!")
#     return bye


# def switch(option):
#     func = switcher.get(option, "Invalid Option")
#     return func()


# switcher = {
#     1: triangle,
#     2: square,
#     3: rTriangle,
#     4: bowtie,
#     5: exit
# }


# def main():
#     num = 0
#     while num != 5:
#         print("1. Triangle\n2. Square\n3. Reverse Triangle\n4. Bowtie\n5. Exit")
#         num = input("Please choose a shape to print: ")
#         if (num.isdigit()):
#             num = int(num)
#             if 1 <= num <= 5:
#                 switch(num)
#             else:
#                 print("\nPlease enter a number on the list!\n")
#         else:
#             print("\nPlease only enter numbers!\n")


# main()

bal = 10000


def pin():
    tries = 3
    while tries >= 0:
        pin = int(input('Please enter PIN (1234): '))
        if pin == (1234):
            print("Pin Accepted")
            return True
        else:
            print("Incorrect PIN, please try again: ")
            tries += 1
    print("Incorrect PIN, you have no reached the maximum limit of attempts.")
    print("Goodbye")
    return False


def balance():
    transaction = 0
    if transaction == 1:
        print('Your Balance is $', balance)
        restart = input('Would You you like to go back? ')
        if restart in ('NO', 'no'):
            print('Thank you enjoy the remainder of your day  type start_menu()')


def withdrawal():
    withdrawl = float(
        input('How Much Would you like to  withdraw? \n$10 $20 $40 $60 $80 $100 :'))
    if withdrawl in [10, 20, 40, 60, 80, 100]:
        balance = balance - withdrawl
        print('\nYour Balance is now $', balance)
        restart = input('Would You you like to go back? ')
        if restart in ('NO', 'no'):
            print(
                'Thank you enjoy the remainder of your day  type start_menu() ')

    elif withdrawl != [10, 20, 40, 60, 80, 100]:
        print('Invalid Amount, Please Re-try')
        restart = ('yes')


def deposit():
    deposit = float(
        input('How much money would you want our trustworthy money elves to protect?  '))
    balance = bal + deposit
    print('Your Balance is $', balance)
    restart = input('Would You you like to go back? ')
    if restart in ('NO', 'no'):
        print('Thank You, enjoy the remainder of your day type start_menu() ')


def exit():
    print('Thank you for your business.')
    print("Goodbye.")


def switch(option):
    func = switcher.get(option, "Invalid Option")
    return func()


switcher = {
    1: balance,
    2: withdrawal,
    3: deposit,
    4: exit
}


def menu():
    print('Welcome to IIT Bank ATM!')
    print("Hint: PIN is 1234")

    if pin():
        print('1. Balance\n')
        print('2. Withdrawal\n')
        print('3. Deposit\n')
        print('4. Exit\n')

        transaction = input('What wouyld you like to do today? ')
        if (transaction.isdigit()):
            transaction = int(transaction)
            if 1 <= transaction <= 4:
                switch(transaction)
            else:
                print("\nPlease enter a number on the list!\n")
        else:
            print("\nPlease only enter numbers!\n")


menu()
