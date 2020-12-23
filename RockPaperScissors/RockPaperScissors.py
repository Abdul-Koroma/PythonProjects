import random

def play():
    user = input("What's your first move? 'r' is for rock, 'p' is for paper, 's' is for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):

    # return true if player wins
    # r > s, s > p, p > r

    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True
    
