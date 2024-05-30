import os
import sys
import colorama
from colorama import Fore, Style


colorama.init()


print(Fore.RED + "Colorama is working!" + Style.RESET_ALL)

def print_board(board):
    """
    Prints the current state of the game board.

    Args:
    board (list of list of str): The game board to print.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    """
    Checks if the given player has won the game.

    Args:
    board (list of list of str): The game board.
    player (str): The player symbol to check for a win.

    Returns:
    bool: True if the player has won, False otherwise.
    """
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for condition in win_conditions:
        if all(board[x][y] == player for x, y in condition):
            return True
    return False

def is_full(board):
    """
    Checks if the game board is full (no more moves possible).

    Args:
    board (list of list of str): The game board.

    Returns:
    bool: True if the board is full, False otherwise.
    """
    return all(cell != ' ' for row in board for cell in row)

def main():
    """
    Main function to run the Tic Tac Toe game.
    """
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = [
        Fore.RED + 'X' + Style.RESET_ALL,
        Fore.BLUE + 'O' + Style.RESET_ALL
    ]
    current_player = 0
    while True:
        print_board(board)
        try:
            row = int(input(f"Player {players[current_player]}, enter row (0, 1, 2): "))
            col = int(input(f"Player {players[current_player]}, enter column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue
        if 0 <= row <= 2 and 0 <= col <= 2:
            if board[row][col] == ' ':
                board[row][col] = players[current_player]
                if check_win(board, players[current_player]):
                    print_board(board)
                    print(f"Player {players[current_player]} wins!")
                    break
                elif is_full(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_player = 1 - current_player
            else:
                print("That spot is already taken. Try again.")
        else:
            print("Invalid input. Row and column must be between 0 and 2.")

if __name__ == "__main__":
    main()

