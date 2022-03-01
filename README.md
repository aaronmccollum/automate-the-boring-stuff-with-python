# Automate the Boring Stuff with Python Repository
Practice problems and workbook problems from the book

## Notes
### Useful List Functions from Ch. 4
- len(list): returns the length of list
- list.append(v): adds v to the end of list
- list.index(v): returns index number of v in list
- list.insert(i, v): adds v to list at index i
- list.remove(v): removes (first instance of) v from list
- list.sort(): sorts list in ASCII order (usually numerically and a-z). Can have revserse=True as an optional argument to reverse sort
- range(n): returns list of 0 to n

### Useful String Functions from Ch. 6
- string.center(n, f): centers a string. Inserts optional f symbols by n/2 places on either side of word
- string.endswith(x): returns boolean statement based on if string ends with x
- string.isalnum(): returns boolean statement based on if string consists of only letteers and numbers
- string.isalpha(): returns boolean statement based on if all characters are letters
- string.isdecimal(): returns boolean statement based on string containing only numbers
- string.islower(): returns boolean statement based on if all letters are lower
- string.isspace(): returns boolean statement based on if all characters are spaces, newlines, and tabs
- string.isupper(): returns boolean statement based on if all letters are higher
- string.istitle(): returns boolean statement based on if all words begin with uppercase letter followed by lowercase letters
- string.join(list): returns a string with list elements separated by string
- string.ljust(n, f): justifies to the left a string by n spaces. Optional second argument that inserts f in each justified space.
- string.lower(): returns string with all lower letters
- string.rjust(n, f): justifies to the right a string by n spaces. Optional second argument that inserts f in each justified space.
- string.split(chars): returns a list of string words by default. Can take optional argument to split at certain chars
- string.startswith(x): returns boolean statement based on if string starts with x
- string.strip/lstrip/rstrip(x): returns a string without any whitespace (all/left/right) by default, or takes optional argument to remove x instead
- string.upper(): returns string with all uppercase letters

A copy and paste function is available by downloading Pyperclip then importing the module into my program
- pyperclip.copy(str): copies str onto clipboard
- pyperclip.paste(str): pastes str
