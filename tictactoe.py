# This is a simple tic-tac-toe implemented using Python
print('Welcome to Tic Tac Toe!')

position_list = []

def display_board():

    print('\n')
    print('7' + '|' + '8' + '|' + '9')
    print('-' + '|' + '-' + '|' + '-')
    print('4' + '|' + '5' + '|' + '6')
    print('-' + '|' + '-' + '|' + '-')
    print('1' + '|' + '2' + '|' + '3')
    print('\n')


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


def play():

    player1, player2 = player_marker()

    board = []

    marker = player1

    while len(position_list) != 9:
        position = input_position()
        board.append(marker)

        place_marker(board, marker, position)

        if marker == player1:
            marker = player2
        else:
            marker = player1

    print(board)
    replay(board)


def place_marker(board, marker, position):

    pass


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
    return position


def check_position(position, cond):

    if position in position_list:
        print('Position already entered')
        return True

    if int(position) < 1 or int(position) > 9:
        print('Position out of range, please enter a position between 1 and 9')
        return True

    return False


def replay(board):
    position_list.clear()
    board.clear()
    # del position_list[:]

    playagain = input('Do you want to play again? Enter Yes or No: ')

    if playagain == 'yes' or playagain == 'Yes':
        print('Restarting the game')
        play()
    elif playagain == 'no' or playagain == 'No':
        print('Stopping the game')
        quit()
    else:
        print('Your answer does not match the options')
        print('Stopping the game')
        quit()

play()
