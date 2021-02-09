import random

def game():
    user = input("Enter a 'r' for rock, 'p' for paper and 's' for scissors\n")
    comp = random.choice(['r', 'p', 's'])

    if user == comp:
        return 'None survive'

    if is_win(user, comp):
        return 'You win!!'
    return 'You Lost'

def is_win(player, opponent):
    # r > s, p > r, s > p
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
        return True

print(game())