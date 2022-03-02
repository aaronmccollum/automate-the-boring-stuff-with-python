#! python3
# This program adds Wikipedia bullet points to the start of each list item provided

import pyperclip

# Take a list of things on your PC's clipboard and paste them into a Python variable to work with
text = pyperclip.paste()


# Split list items up by the newline escape character and add stars
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '* ' + lines[i]


# Join the edited list back together
text = '\n'.join(lines)


pyperclip.copy(text)
