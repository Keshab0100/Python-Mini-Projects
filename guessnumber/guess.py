import random

n = int(input("Enter the range to guess the no. \n"))


def guess(x):
    random_number = random.randint(1, x)
    user_number = 0
    while (random_number != user_number):
        user_number = int(input(f"Guess a number from 1 to {x} \n"))
        if (user_number > random_number):
            print("Too high, guess a lower number \n")
        elif (user_number < random_number):
            print("Too low, guess a higher number \n")

    print("Congratulations You have guessed the no. \n")


guess(n)
