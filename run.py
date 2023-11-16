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
