"""
import all required modules
"""
import random

def main():
    """
    main program
    """
    starting_board = [4,3,2,1]
    new_board = starting_board
    moves = one_move()
    print(moves)
    for i in range(len(starting_board)):
        new_board[i] = starting_board[i] - moves[i]
    print(moves)
    print(new_board)

def one_move():
    """
    plays one move
    """
    moves = []
    sum_moves = 0
    while sum_moves == 0:
        for _ in range(4):
            move = random.randint(0,1)
            moves.append(move)
            sum_moves +=move
    return moves

main()
