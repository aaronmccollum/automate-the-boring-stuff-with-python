# Grid from page 103
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]


# Create a loop that loops the length of the arr 6 times
# Each time, the index of the list is incremented by one and those values are appended to a new list inside answer_arr
def flip_image(arr):
    for i in range(6):
        for j in range(9):
            print(grid[j][i], end=' ')
        print('')

            
# Test function call
flip_image(grid)
