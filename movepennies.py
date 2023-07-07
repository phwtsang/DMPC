"""
import all required modules
"""
import random

def main():
    """
    main program
    """
    starting_board = [4,3,2,1]
    print(starting_board)
    new_board = starting_board
    for _ in range(3):
        moves = one_move()
        #print(moves)
        for i in range(len(starting_board)):
            updated = starting_board[i] - moves[i]
            if updated <= 0:
                new_board[i] = 0
            else:
                new_board[i] = updated
        #print(moves)
        print(new_board, moves)

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
