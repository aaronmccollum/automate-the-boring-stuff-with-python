# Using Python exception handling keywords 'try' and 'except'

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print("Error: Invalid argument.")

print(spam(2))
print(spam(4))
print(spam(0))
print(spam(10))
