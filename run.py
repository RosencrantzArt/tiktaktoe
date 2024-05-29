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
    
