import sys

while True:
    print("Type 'exit' to end program.")
    response = input()
    if response == 'exit':
        sys.exit()
    print("You typed " + response + ".")
