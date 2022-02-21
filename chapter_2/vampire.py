# Using control flow to determine if Alice is a vampire

print("Is your name 'Alice'?")
answer = input()

if answer == 'yes':
    print("Hello Alice, how old are you?")
    age = int(input())
    if age < 12:
        print("You are a child, probably not a vampire.")
    elif age > 120:
        print("Whoa you might be a vampire!")
    elif age > 100:
        print("You might be a vampire, but time will tell.")
    else:
        print("Let's see what happens when you go out in the day.")

else:
    print("Hello, " + answer + ". You are not a vampire.")
