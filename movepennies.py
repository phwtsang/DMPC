"""
import all required modules
"""
import random

def main():
    """
    main program
    """
    starting_board = [4,3,2,1]
    print(one_move())

def one_move():
    """
    plays one move
    """
    moves = []
    for _ in range(4):
        moves.append(random.randint(0,1))
    return moves