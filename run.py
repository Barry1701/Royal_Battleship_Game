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
    
def hit_shot(board, guess_row, guess_col):
    """
    Check if a shot hit a ship.
    """
    return board[guess_row][guess_col] == "$"

def player_turn(board, player_score):
    """
    This function handles a player's turn in the game.it prompts a player
    to pick a row and a column, checks the validity of the input, updates
    the board game accordingly. It also checks if the player hit a ship,
    increment the players score and prints the updated score.
    """
    while True:
        try:
            guess_row = int(input("Pick a row (0,4): "))
            guess_col = int(input("Pick a column (0,4): "))
            if not (0 <= guess_row <= 4) or not (0 <= guess_col <= 4):
                raise ValueError("Values must be numbers between 0 & 4!")
            break
        except ValueError:
            print("You must enter a number!")

    if board[guess_row][guess_col] == "*" or board[guess_row][guess_col] == "X":
        print("You can't guess the same coordinates twice!")
        return False

    if hit_shot(board, guess_row, guess_col):
        print("Player got a Hit!")
        board[guess_row][guess_col] == "*"
        player_score += 1
        print_scores(player_score, 0)
        return True
    else:
        print("Player missed this time!")
        board[guess_row][guess_col] == "X"
        return False

def computer_turn(board, computer_score):
    """
    This function handles the computer's turn in the game. It generates random
    coordinates for the computer's guess, checks if it's a hit, updates the game
    board, and prints the updated scores.
    """
    guess_row = random.randint(0, len(board) -1)
    guess_col = random.randint(0, len(board[0]) -1)

    if hit_shot(board, guess_row, guess_col):
        print("Computer got a hit!")
        board[guess_row][guess_col] = "*"
        computer_score += 1
        print_score(0, computer_score)
        return True

    else:
        print("Computer missed this time!")
        board[guess_row][guess_col] = "X"
        return False



