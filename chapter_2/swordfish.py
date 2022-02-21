while True:
    print("Please enter your name.")
    name = input()
    if name != 'Joe':
        continue
    print("Hello Joe! Please provide your password.")
    password = input()
    if password == "swordfish":
        break

print("Access granted.")
