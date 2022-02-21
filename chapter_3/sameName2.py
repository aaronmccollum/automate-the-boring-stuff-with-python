# Example showing the 'global' keyword in a local environment to pull the
# variable value from the global scope

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)
