# This is a simple tic-tac-toe implemented using Python

def board():
    print('7' + '|' + '8' + '|' + '9')
    print('-' + '|' + '-' + '|' + '-')
    print('4' + '|' + '5' + '|' + '6')
    print('-' + '|' + '-' + '|' + '-')
    print('1' + '|' + '2' + '|' + '3')

def player_input():

    player1 = ''
    player2 = ''

    while player1 != 'x' and player1 != 'o':
        player1 = input("Player 1, please pick a marker x or o: ")

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return (player1, player2)

player1, player2 = player_input()

print((player1, player2))
