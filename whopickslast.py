"""
import required modules
"""
import random


def main():
    """
    Starts with n flags.
    Two players takes turn to remove 1, 2,or 3 flags.
    Player who picks the last flag wins.
    """
    n_flags = 21
    for _ in range(5):
        print(play_one_game(n_flags))


def play_one_game(n_flags):
    """
    Player take turns to pick flage until a winner is determined
    """
    count = n_flags
    flags_remaining = []
    player1 = []
    player2 = []
    while True:
        if count <= 3:
            player1_pick = count
        else:
            player1_pick = random.randint(1,3)
        player1.append(player1_pick)
        count = count - player1_pick
        if count == 0:
            print('Player1 has won')
            print(player1)
            print(player2)
            break
        if count <= 3:
            player2_pick = count
        else:
            player2_pick = random.randint(1,3)
        player2.append(player2_pick)
        count = count - player2_pick
        if count == 0:
            print('Player2 has won')
            print(player1)
            print(player2)
            break
        flags_remaining.append(count)
    return flags_remaining


main()
