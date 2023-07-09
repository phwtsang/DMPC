"""
import all required modules
"""
import random

def main():
    """
    main program
    """
    player1_wins = 0
    player2_wins = 0
    #starting_board = [4,3,2,1]
    for i in range(10000):
        starting_board = [4,5,4,5]
        #print(i, 'START')
        winner = one_game(starting_board)
        #print(i, 'END')
        if winner == 1:
            player1_wins +=1
        else:
            player2_wins +=1
    print(player1_wins, player2_wins)


def one_game(starting_board):
    """
    Plays one game.
    """
    #print(starting_board)
    new_board = starting_board
    sum_board = sum(new_board)
    player = 0
    move_count = 0
    while sum_board > 0:
        move_count +=1
        player = move_count%2
        moves = one_move_random(new_board)
        #print(moves)
        for i in range(len(starting_board)):
            updated = starting_board[i] - moves[i]
            if updated <= 0:
                new_board[i] = 0
            else:
                new_board[i] = updated
        #print(moves)
        sum_board = sum(new_board)
        #print(new_board, player)
    return player

def one_move_random(new_board):
    """
    plays one move randomly
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
