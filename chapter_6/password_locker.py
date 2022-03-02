#! python3
# This file is an insecure password locker program from Ch.6

# A dictionary of passwords
PASSWORDS = {'email': 'FEYRBNDF564873HNFDS',
             'blog': 'RTNWE538@$%#@s%23',
             'luggage': 'RN5#%TNHFD74$R$%^!'}


# Importing ability to use command-line arguments into the program
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]


# Checking to see if account is in the PASSWORDS dictionary already
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
