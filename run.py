import os
import sys
import colorama
from colorama import Fore, Style

coloroma.init()


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
    board(list of the list str): The game board.
    player(str): The player symbol to check for a win. 

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
    """.devcontainer/Checks if the game board is full (no moves possible).

    
    Args:
    board(list of list of str): The game board. 

    
    Returns:
    bool: True if the board is full, False otherwise. 
    """
    return all(cell !='' for row in board for cell in row)






    
