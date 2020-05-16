# This is a simple tic-tac-toe implemented using Python

position_list = []

def board():
    print('7' + '|' + '8' + '|' + '9')
    print('-' + '|' + '-' + '|' + '-')
    print('4' + '|' + '5' + '|' + '6')
    print('-' + '|' + '-' + '|' + '-')
    print('1' + '|' + '2' + '|' + '3')


def player_marker():

    player1 = ''
    player2 = ''

    while player1 != 'x' and player1 != 'o':
        player1 = input("Player 1, please pick a marker x or o: ")

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return (player1, player2)

player1, player2 = player_marker()


def input_position():

    cond = True
    while cond:
        try :
            position = int(input('Please enter a position number: '))
            cond = check_position(position, cond)

        except :
            print("Enter numeric value between 1 and 9")
            cond = True

    position_list.append(position)


def check_position(position, cond):
    if position in position_list:
        print('Position already entered')
        return True
    if int(position) < 1 or int(position) > 9:
        print('Position out of range, please enter a position between 1 and 9')
        return True
    return False


def replay():
    position_list.clear()
    # del position_list[:]
