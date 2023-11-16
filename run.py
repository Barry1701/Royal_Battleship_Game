import random

def make_board(size):
    """
    Create a game board filled with "0" characters
    using list comprehension.
    """
    return[["0" for _ in range(size)] for _ in range(size)]
