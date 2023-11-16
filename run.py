import random

def make_board(size):
    """
    Create a game board filled with "0" characters
    using list comprehension.
    """
    return[["0" for _ in range(size)] for _ in range(size)]

def print_board(board, show_ships = False):
    """
    Print the game board.
    """
    for row in board:
        for cell in row:
            if cell == "$" and not show_ships:
                print("0", end = " ")
            else:
                print(cell, end = " ")
        print()

def place_ships(board, num_ships):
    """
    Randomly place ships on the game board
    """
    for _ in range(num_ships):
        while True:
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - 1)
            if board[row][col] == "0":
                board[row][col] = "$"
                break
