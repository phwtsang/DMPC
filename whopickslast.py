"""
import required modules
"""
import random


def main():
    """
    Starts with n_flags flags.
    Two players takes turn to remove 1, 2,or 3 flags.
    Player who picks the last flag wins.
    """
    n_flags = 21
    player1_wins = 0
    player2_wins = 0
    for _ in range(5):
        results = play_one_game(n_flags)
        if results['Winner'] == 'Player1':
            player1_wins +=1
        else:
            player2_wins +=1
        print(results)
    print('Player1 wins:',player1_wins,'Player2 wins:',player2_wins)


def play_one_game(n_flags):
    """
    Player take turns to pick flage until a winner is determined
    Both players pick randomly until there are 3 or fewer flags remain
    """
    count = n_flags
    flags_remaining = []
    player1 = []
    player2 = []
    results = {}
    while True:
        if count <= 3:
            player1_pick = count
        else:
            player1_pick = random.randint(1,3)
        player1.append(player1_pick)
        count = count - player1_pick
        if count == 0:
            #print('Player1 has won')
            #print(player1)
            #print(player2)
            results['Player1'] = player1
            results['Player2'] = player2
            results['Winner'] = 'Player1'
            break
        if count <= 3:
            player2_pick = count
        else:
            player2_pick = random.randint(1,3)
        player2.append(player2_pick)
        count = count - player2_pick
        if count == 0:
            #print('Player2 has won')
            #print(player1)
            #print(player2)
            results['Player1'] = player1
            results['Player2'] = player2
            results['Winner'] = 'Player2'
            break
        flags_remaining.append(count)
        results['Flags Remaining'] = flags_remaining
    return results


main()
