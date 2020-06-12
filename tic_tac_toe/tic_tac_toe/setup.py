from tic_tac_toe.Player import Player
from tic_tac_toe.utils import decode_position
from tic_tac_toe.validations import is_position_valid


def get_board(size):
    return [[None] * size for _ in range(size)]


def get_player(mark=None):
    name = input("Name: ")
    if mark:
        print(f'Mark: {mark}')

    while mark not in ('X', 'O'):
        mark = input("Mark: ")
    return Player(name, mark)


def get_position(player, board):
    board_size = len(board)
    position = None
    while not is_position_valid(position, board):
        position = int(input(f'{player.name} chooses a free position [1-9]: '))

    return decode_position(position, board_size)


def setup_game(board_size):
    player_one = get_player()
    player_two = get_player('O' if player_one.mark == 'X' else 'X')
    board = get_board(board_size)

    return (board, player_one, player_two)
