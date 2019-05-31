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
        print('Your Balance is $', balance)
        restart = input('Would You you like to go back? ')
        if restart in ('NO', 'no'):
            print('Thank you enjoy the remainder of your day  type start_menu()')

def withdrawal():
    withdrawl = float(input('How Much Would you like to  withdraw? '))
    balance = bal - withdrawl
    print('Available Balance: $', balance)
    more = input('Is there anything else you would like to do? ')
    if more == ('Yes', 'yes'):
       transaction = input('What would you like to do today? ')
       if (transaction.isdigit()):
            transaction = int(transaction)
            if 1 <= transaction <= 4:
                switch(transaction)
    else:
        print('Thank you for your business.')
        print("Goodbye.")

def deposit():
    deposit = float(
        input('How much money would you want our trustworthy money elves to protect?  '))
    balance = bal + deposit
    print('Your Balance is $', balance)
    restart = input('Would You you like to go back? ')
    if restart in ('Yes', 'yes'):
       transaction = input('What would you like to do today? ')
       if (transaction.isdigit()):
            transaction = int(transaction)
            if 1 <= transaction <= 4:
                switch(transaction)
    else:
        print('Thank you for your business.')
        print("Goodbye.")

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
    print('Hint: PIN is 1234')

    if pin():
        print('1. Balance')
        print('2. Withdrawal')
        print('3. Deposit')
        print('4. Exit')

        transaction = input('What wouyld you like to do today? ')
        if (transaction.isdigit()):
            transaction = int(transaction)
            if 1 <= transaction <= 4:
                switch(transaction)
            else:
                print("\nPlease enter a number on the list!")
        else:
            print("\nPlease only enter numbers!")

menu()


        # if transaction == 1:
        #     print('Your Balance is $', balance)
        #     restart = input('Would You you like to go back? ')
        #     if restart in ('NO', 'no'):
        #         print('Thank you enjoy the remainder of your day  type start_menu()')

        # elif transaction == 2:

        #     withdrawl = float(
        #         input('How Much Would you like to  withdraw? \n$10 $20 $40 $60 $80 $100 :'))
        #     if withdrawl in [10, 20, 40, 60, 80, 100]:
        #         balance = balance - withdrawl
        #         print('\nYour Balance is now $', balance)
        #         restart = input('Would You you like to go back? ')
        #         if restart in ('NO', 'no'):
        #             print(
        #                 'Thank you enjoy the remainder of your day  type start_menu() ')

        #     elif withdrawl != [10, 20, 40, 60, 80, 100]:
        #         print('Invalid Amount, Please Re-try')
        #         restart = ('yes')

        # elif transaction == 3:
        #     deposit = float(
        #         input('How much money would you want our trustworthy money elves to protect?  '))
        #     balance = balance + deposit
        #     print('Your Balance is $', balance)
        #     restart = input('Would You you like to go back? ')
        #     if restart in ('NO', 'no'):
        #         print('Thank You, enjoy the remainder of your day type start_menu() ')

        # elif transaction == 4:

        #     print('Thank you for your business.')
        #     print("Goodbye.")
