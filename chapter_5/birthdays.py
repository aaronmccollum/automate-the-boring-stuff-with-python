birthdays = {'Alice': 'Apr 1',
             'Bob': 'Dec 12',
             'Carol': 'Mar 4'}

while True:
    # Get the name from the user to look up birthday in dictionary
    # If no name given, exit the program.
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    # Return birthday if name is in the dictionary
    # Update dictionary if name isn't in the dictionary with new input
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
