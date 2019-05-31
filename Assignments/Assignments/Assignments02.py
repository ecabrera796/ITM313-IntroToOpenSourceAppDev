import random
numGuesses = 1
num = random.randint(0,20)
try:
    guess = int(input("Please try and guess the number I am thinking of: "))
    while numGuesses < 5:
        numGuesses += 1
        print
        if guess < num:
            guess = int(input("Nope, too low! Try again: "))
        elif guess > num:
            guess = int(input("Nope, too high! Try again: "))
        elif guess == num:
            print("Ding! Ding! Ding! Got a WINNER!!")
            break
    else: 
        print("Nice try buddy. Don't let the door hit you on the way out!")
except ValueError:
    print("I SAID NUMBERS!!!")