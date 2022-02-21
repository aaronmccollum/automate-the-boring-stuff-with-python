# Practice problem 2: Input Validation adding 'try' and 'except' to
# program from problem 1

# Collatz function from Problem 1
def collatz(number):
    if number % 2 == 0:
        print(number / 2)
        return number / 2
    else:
        print(3 * number + 1)
        return 3 * number + 1
    


# Main program that runs when mainProgram() is called
def mainProgram():
    try:
        print("Please type a number:")
        userInput = int(input())
        while userInput > 1:
            userInput = collatz(userInput)
    except ValueError:
        print("You need to input an integer. Please try again.")

# Calling the main program
mainProgram()
