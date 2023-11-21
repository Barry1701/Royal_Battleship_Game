import random


def make_board(size):
    """
    Create a game board filled with "0" characters
    using list comprehension.
    """
    return [["0" for _ in range(size)] for _ in range(size)]


def print_board(board, show_ships=False):
    """
    Print the game board.
    """
    for row in board:
        for cell in row:
            if cell == "$" and not show_ships:
                print("0", end=" ")
            else:
                print(cell, end=" ")
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


def player_turn(board, player_score, computer_score):
    """
    This function handles a player's turn in the game.it prompts a player
    to pick a row and a column, checks the validity of the input, updates
    the board game accordingly. It also checks if the player hit a ship,
    increment the players score and prints the updated score.
    """
    while True:
        user_input_row = input("Pick a row (0-4): ")
        user_input_col = input("Pick a column (0-4): ")

        if not (user_input_row.isdigit() and user_input_col.isdigit()):
            print("Only numbers are accepted for this input!")
            continue

        guess_row = int(user_input_row)
        guess_col = int(user_input_col)

        if not (0 <= guess_row <= 4) or not (0 <= guess_col <= 4):
            print("Invalid Input. Choose a number form 0 to 4")
            continue

        break
    if board[guess_row][guess_col] == "*" or board[guess_row][guess_col] == "X":
        print("You can't guess the same coordinates twice!")
        return False

    if hit_shot(board, guess_row, guess_col):
        print(f"Player Guessed: ({guess_row}, {guess_col}) - Bullseye! You got a Hit!")
        board[guess_row][guess_col] = "*"
        player_score[0] += 1
        return True
    else:
        print(f"Player Guesses: ({guess_row}, {guess_col}) - Missed!")
        board[guess_row][guess_col] = "X"
        return False


def computer_turn(board, computer_score, player_score):
    """
    This function handles the computer's turn in the game. 
    It generates random coordinates for the computer's guess, 
    checks if it's a hit, updates the game board, 
    and prints the updated scores.
    """
    guess_row = random.randint(0, len(board) - 1)
    guess_col = random.randint(0, len(board[0]) - 1)

    if hit_shot(board, guess_row, guess_col):
        print(f"Computer Guessed: ({guess_row}, {guess_col}) - Computer got a hit!")
        board[guess_row][guess_col] = "*"
        computer_score[0] += 1
        return True

    else:
        print(f"Computer Guessed: ({guess_row}, {guess_col}) - Missed!")
        board[guess_row][guess_col] = "X"
        return False


def separator_line():
    """
    Function print a separator line
    """
    print("-" * 50)


def print_scores(player, computer):
    """
    Function print the current scores.
    """
    print(f"After this round the scores are:\nPlayer: {player[0]}. Computer: {computer[0]}")


def end_game_message(player_name, player_score, computer_score):
    """
    Display the end game message based on the winner
    """
    separator_line()

    if player_score[0] == 4:
        print(f"Fantastic work {player_name}!\nYou are the champion!")
    else:
        print("Oh No! Computer takes the win.\nGive it another shot!")

    separator_line()


def new_game(player_board, computer_board, player_score, computer_score):
    """
    Reset the game state for a New Game
    """
    for row in player_board:
        for i in range(len(row)):
            row[i] = "0"

    for row in computer_board:
        for i in range(len(row)):
            row[i] = "0"

    player_score[0] = 0
    computer_score[0] = 0


def main():
    """
    Run the Royal Battleship Game, initializing boards, placing ships, and managing player and computer turns.
    """
    print("Welcome to Royal Battleship Game")
    print("Board Size: 5. Number of Ships: 4")
    print("Top Left Corner is Row: 0, Column: 0")

    player_name = input("Enter your name: ")

    while True:
        player_board = make_board(5)
        computer_board = make_board(5)

        place_ships(player_board, 4)
        place_ships(computer_board, 4)

        player_score = [0]
        computer_score = [0]

        while True:
            separator_line()
            print(f"{player_name}'s Board:")
            print_board(player_board, show_ships=True)

            separator_line()
            print("Computer's Board:")
            print_board(computer_board)

            player_turn(computer_board, player_score, computer_score)

            separator_line()

            computer_turn(player_board, computer_score, player_score)

            separator_line()

            print_scores(player_score, computer_score)

            if player_score[0] == 4 or computer_score[0] == 4:
                if not end_game_message(player_name, player_score, computer_score):
                    break

        choice = input("Press Enter to start a New Game.\nTo exit the game, type 'e' and press Enter:")
        if choice.lower() == "e":
            break
        else:
            new_game(player_board, computer_board, player_score, computer_score)


if __name__ == "__main__":
    main()
    



