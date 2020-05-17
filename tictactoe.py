# This is a simple tic-tac-toe implemented using Python
print('Welcome to Tic Tac Toe!')

position_list = []

def display_board(board):

    print('\n')
    print(f'{board[6]}|{board[7]}|{board[8]}')
    print('-' + '|' + '-' + '|' + '-')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print('-' + '|' + '-' + '|' + '-')
    print(f'{board[0]}|{board[1]}|{board[2]}')
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

    board = [' ']*9

    marker = player1
    player = 'player1'

    while len(position_list) != 9:
        position = int(input_position(player))
        board.pop(position-1)
        board.insert(position-1, marker)

        display_board(board)

        if marker == player1:
            marker = player2
            player = 'player2'
        else:
            marker = player1
            player = 'player1'

    # print(board)
    replay(board)



def input_position(player):

    cond = True

    while cond:
        try :
            if player == 'player1':
                position = int(input('Player 1, please enter a position number: '))
            else:
                position = int(input('Player 2, please enter a position number: '))
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
