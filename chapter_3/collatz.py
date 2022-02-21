# Practice Problem 1: The Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        print(number / 2)
        return number / 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print("Please type a number:")
userInput = int(input())

while userInput > 1:
    userInput = collatz(userInput)
