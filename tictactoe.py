# This is a simple tic-tac-toe implemented using Python
print('\nWelcome to Tic Tac Toe!\n')

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

        if player1 == 'quit' or player1 == 'exit' or player1 == 'Quit' or player1 == 'Exit' or player1 == 'QUIT' or player1 == 'EXIT':
            print(f'\nYou entered {player1}\n\nQuitting the game\n\n')
            quit()

    if player1 == 'x':
        player2 = 'o'
    else:
        player2 = 'x'

    return (player1, player2)


def play():

    player1, player2 = player_marker()

    board = [' ']*9

    marker = player1
    player = 'Player 1'

    print('\nPress the number corresponding to the grid below where you want to place your marker:')
    display_board([1,2,3,4,5,6,7,8,9])

    while len(position_list) != 9:
        position = int(input_position(player))
        board.pop(position-1)
        board.insert(position-1, marker)

        display_board(board)

        win = check_win(board, marker, player)

        if win:
            break

        if marker == player1:
            marker = player2
            player = 'Player 2'
        else:
            marker = player1
            player = 'Player 1'

    if not win:
        print('The game was a tie!\n')

    # print(board)
    replay(board)


def check_win(board, marker, player):
    if (board[0] == board[1] == board[2] == marker) or \
    (board[3] == board[4] == board[5] == marker) or \
    (board[6] == board[7] == board[8] == marker) or \
    (board[0] == board[3] == board[6] == marker) or \
    (board[1] == board[4] == board[7] == marker) or \
    (board[2] == board[5] == board[8] == marker) or \
    (board[0] == board[4] == board[8] == marker) or \
    (board[2] == board[4] == board[6] == marker):
        print(f'{player} wins!\n\n')
        return True
    else:
        return False

def input_position(player):

    cond = True

    while cond:
        try :
            position = int(input(f'{player}, please enter a position number: '))
            cond = check_position(position, cond)

        except :
            print("\nEnter numeric value between 1 and 9\n")
            cond = True

    position_list.append(position)
    return position


def check_position(position, cond):

    if position in position_list:
        print('\nPosition already entered\n')
        return True

    if int(position) < 1 or int(position) > 9:
        print('\nPosition out of range, please enter a position between 1 and 9\n')
        return True

    return False


def replay(board):
    position_list.clear()
    board.clear()
    # del position_list[:]

    playagain = input('Do you want to play again? Enter Yes or No: ')

    if playagain == 'y' or playagain == 'Y' or playagain == 'yes' or playagain == 'Yes':
        print('\nRestarting the game\n\n')
        play()
    elif playagain == 'n' or playagain == 'N' or playagain == 'no' or playagain == 'No':
        print('\nStopping the game\n\n')
        quit()
    else:
        print('\nYour answer does not match the options')
        print('\nStopping the game\n\n')
        quit()

play()
