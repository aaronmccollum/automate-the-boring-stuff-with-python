# Annoying loop that forces you to type explicitly 'your name'

print("What is your name?")
name = input()

while name != "your name":
    print("Please type your name.")
    name = input()
print("Thank you!")
