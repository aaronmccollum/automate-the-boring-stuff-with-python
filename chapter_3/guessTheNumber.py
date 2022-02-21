# Simple 'guess the right number' game

import random

secretNumber = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20")

# Ask players to guess a number 6 times
for guessesTaken in range(1, 7):
    print("Take a guess:")
    guess = int(input())

    if guess < secretNumber:
        print("Too low, try again.")
    elif guess > secretNumber:
        print("Too high, try again.")
    else:
        print("Correct! My secret number was " + str(secretNumber) + "!")
        break
