import random


def play():
    user = input("r for rock, p for paper, s for scissor \n")
    print(f"You choose {user}")
    computer = random.choice(['R', 'P', "S"])
    print(f"Computer choose {computer}")

    if (user == computer):
        print("It's a tie")

    elif (game(user, computer)):
        print("You lost")
    else:
        print("You Won!!")


def game(user, computer):
    if (user == 'R' and computer == 'P') or (user == 'P' and computer == 'S') or (user == 'S' and computer == 'R'):
        return True


play()
