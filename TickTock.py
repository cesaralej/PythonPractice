from IPython.display import clear_output
import random


def display_board(board):
    clear_output()
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print('-----------')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('-----------')
    print(f' {board[1]} | {board[2]} | {board[3]} ')


def player_input():

    while True:
        player1 = input("Player 1 pick a marker 'X' or 'O'")
        if player1 == 'X':
            return 'X'
            break
        elif player1 == 'O':
            return 'O'
            break


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    win = False
    if [mark, mark, mark] == [board[1], board[2], board[3]]:
        win = True
    elif [mark, mark, mark] == [board[4], board[5], board[6]]:
        win = True
    elif [mark, mark, mark] == [board[7], board[8], board[9]]:
        win = True
    elif [mark, mark, mark] == [board[1], board[4], board[7]]:
        win = True
    elif [mark, mark, mark] == [board[2], board[5], board[8]]:
        win = True
    elif [mark, mark, mark] == [board[3], board[6], board[9]]:
        win = True
    elif [mark, mark, mark] == [board[1], board[5], board[9]]:
        win = True
    elif [mark, mark, mark] == [board[3], board[5], board[7]]:
        win = True

    return win


def choose_first():
    print(f'Player {random.randint(1,2)} goes first')


def space_check(board, position):
    return ' ' in board[position]


def full_board_check(board):
    return ' ' not in board


def player_choice(board):
    while True:
        position = int(input('Please enter a number '))
        if space_check(board, position):
            return position
            break
        print('That position is taken!')


def replay():
    rep = input('Do you want to play again?')
    return rep == 'yes'


print('Welcome to Tic Tac Toe!')
first = player_input()
if first == 'X':
    second = 'O'
else:
    second = 'X'
while True:
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    choose_first()
    while True:
        place_marker(board, first, player_choice(board))
        display_board(board)
        if win_check(board, first):
            print('Player 1 has won!')
            break
        if full_board_check(board):
            print("It's a tie!")
            break
        place_marker(board, second, player_choice(board))
        display_board(board)
        if win_check(board, second):
            print('Player 2 has won!')
            break
        if full_board_check(board):
            print("It's a tie!")
            break

    if not replay():
        break
