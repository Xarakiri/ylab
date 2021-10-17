import random
import re


PLAY_BOARD = [[f"{j}{i}" if j > 0 else f"{i}" for i in range(10)] for j in range(10)]
PLAYERS_MARKS = ['X', 'O']
TOP = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


def display_board(board_list):
    """Prints the game board."""
    print(' '*5 + '|' + '|'.join([f"{i:^7}" for i in TOP]))

    for row_number, line in enumerate(board_list):
        to_print = f" {row_number+1:>3} | " + ' | '.join([f"{i:^5}" for i in line])
        print(to_print)
        print('-' * len(to_print))


def player_input():
    """Gets player's input string to choose the game mark to play."""
    player_first = ''
    while player_first not in ('X', 'O'):
        player_first = input('Please, choose your marker: X or O: ').upper()

    if player_first == 'X':
        player_second = 'O'
    else:
        player_second = 'X'

    return player_first, player_second


def place_marker(board, marker, position):
    """Puts a player mark to appropriate position."""
    if position < 0:
        return
    position = str(position)
    if position.isalpha():
        return
    if len(position) == 1:
        board[0][int(position)] = marker
    else:
        row = int(position[0])
        col = int(position[0]) 
        board[row][col] = marker


def choose_first():
    """Randomly returns the player's mark that goes first."""
    return PLAYERS_MARKS[random.choice((0, 1))]


def space_check(board, position):
    """Returns boolean value whether the cell is free or not."""
    position = str(position)
    if not position.isalnum():
        return True
    row, col = None, None
    if len(position) == 1:
        row = int(position)
    else:
        row = int(position[0]) - 1
        col = int(position[0]) - 1

    return board[row][col] not in PLAYERS_MARKS


def player_choice(board, player_mark):
    """Gets player's next position and check if it's appropriate to play."""
    position = -1

    while position not in [num for num in range(100)]:
        try:
            position = \
                int(input(f'Player "{player_mark}", choose your next position from 0 to 99: '))
        except ValueError as exc:
            print(f'Wrong value: {exc}. Please, try again.')

    position -= 1
    if space_check(board, position):
        return position

    return False

def win_check(board, mark):
    for board in [board, [*zip(*board)]]:
        for row in board:
            line = ''.join(row)
            for i in line.split(mark):
                if len(i) == 5:
                    s = set(i)
                    return len(s) == 1 and mark in s

    return False


def check_game_finish(board, mark):
    """Return boolean value is the game finished or not."""
    if win_check(board, mark):
        print(f'The player with the mark "{mark}" wins!')
        return True

    return False

def replay():
    """Asks the players to play again."""
    decision = ''
    while decision not in ('y', 'n'):
        decision = input('Would you like to play again? Type "y" or "n"').lower()

    return decision == 'y'

def switch_player(mark):
    """Switches player's marks to play next turn."""
    return 'O' if mark == 'X' else 'X'

def clear_screen():
    """Clears the game screen via adding new rows."""
    print('\n' * 100)


print("Welcome to Tic Tac Toe!")

PLAYER_MARKS = player_input()
CURRENT_PLAYER_MARK = choose_first()

print(f'Player with mark "{CURRENT_PLAYER_MARK}" goes first.')

while True:
    display_board(PLAY_BOARD)

    print(f'Turn of the player with the mark "{CURRENT_PLAYER_MARK}":')

    PLAYER_POSITION = player_choice(PLAY_BOARD, CURRENT_PLAYER_MARK)
    place_marker(PLAY_BOARD, CURRENT_PLAYER_MARK, PLAYER_POSITION)

    if check_game_finish(PLAY_BOARD, CURRENT_PLAYER_MARK):
        display_board(PLAY_BOARD)
        if not replay():
            break
        else:
            PLAY_BOARD = [[f"{j}{i}" if j > 0 else f"{i}" for i in range(10)] for j in range(10)]
            PLAYER_MARKS = player_input()
            CURRENT_PLAYER_MARK = choose_first()
    else:
        CURRENT_PLAYER_MARK = switch_player(CURRENT_PLAYER_MARK)
    clear_screen()
