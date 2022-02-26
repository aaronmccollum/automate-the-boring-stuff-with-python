# Creating the tic-tac-toe board
the_board = {"top-L": " ", "top-M": " ", "top-R": " ",
             "mid-L": " ", "mid-M": " ", "mid-R": " ",
             "low-L": " ", "low-M": " ", "low-R": " "}

# Function that prints the tic-tac-toe board to the console
def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-+-+-")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-+-+-")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


# Game function to start with player X
# Player X inputs a move destination.
# Program searches the board dictionary for destination (key) and modifies value
# If X went, then Player 0 goes. Else, Player X's turn

turn = "X"
for i in range(9):
    print_board(the_board)
    print("Turn for " + turn + ". Move on which space?")
    move = input()
    the_board[move] = turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

print_board(the_board)
