# Table printer project from Ch. 6

tableData = [['apples', 'oranges', 'cheeries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    # Create a list for the length of the longest word of each sublist
    col_width = [0] * len(list)
    for i in range(len(col_width)):
        col_width[i] = find_max(list[i])

    # Format words with proper width and justified to the right
    for i in range(len(list[0])):
        for j in range(len(list)):
            print(list[j][i].rjust(col_width[j]), end = " ")
        print("")


# Function to find the max length in a given list
def find_max(list):
    max_length = len(list[0])
    for word in list:
        if len(word) > max_length:
            max_length = len(word)
    return max_length


# Test
printTable(tableData)
