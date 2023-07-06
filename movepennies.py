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
    sum_moves = 0
    for _ in range(4):
        move = random.randint(0,1)
        moves.append(move)
        sum_moves +=move
    if sum_moves == 0:
        return moves
    else:
        return moves

main()
