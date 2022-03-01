# Get age from user and validate using an infinite while loop
# to ensure it's just a number
while True:
    print("Enter your age.")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for your age.")


# Get password from the user and use another infinite while loop
# to validate that it is using numbers and letters only
while True:
    print("Select a new password (letters and numbers only):")
    password = input()
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")
