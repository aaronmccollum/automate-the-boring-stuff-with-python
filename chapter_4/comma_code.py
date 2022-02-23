# Practice problem 1 for chapter 4

# Function that takes an array and returns a comma-separated string
def make_string(array):
    answer_string = ""
    for i in array:
        if array.index(i) == 0:
            answer_string += str(i)
        # Last index word finishes with "and" before it
        elif array.index(i) == len(array) - 1:
            answer_string += ", and " + str(i)
        else:
            answer_string += ", " + str(i)
    
    print(answer_string)

# Test from book
my_arr = ["apple", "bananas", "tofu", "cats"]
answer = make_string(my_arr)
