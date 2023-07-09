"""
import all required modules
"""
import random

def main():
    """
    main program
    """
    starting_board = [4,3,2,1]
    one_game(starting_board)


def one_game(starting_board):
    """
    Plays one game.
    """
    print(starting_board)
    new_board = starting_board
    sum_board = sum(new_board)
    while sum_board > 0:
        moves = one_move(new_board)
        #print(moves)
        for i in range(len(starting_board)):
            updated = starting_board[i] - moves[i]
            if updated <= 0:
                new_board[i] = 0
            else:
                new_board[i] = updated
        #print(moves)
        sum_board = sum(new_board)
        print(new_board)

def one_move(new_board):
    """
    plays one move
    """
    sum_moves = 0
    while sum_moves == 0:
        moves = []
        for i in range(4):
            move = random.randint(0,1)
            moves.append(move)
            # only count move when penny is not at the bottom
            if new_board[i] != 0:
                sum_moves +=move
    return moves

main()
