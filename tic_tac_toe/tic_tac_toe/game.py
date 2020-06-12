from tic_tac_toe.printing import print_board, print_welcome
from tic_tac_toe.setup import setup_game, get_position
from tic_tac_toe.utils import all_single_value


def place_mark(board, player):
    (row, column) = get_position(player, board)
    board[row][column] = player.mark


def check_game_over(board, player):
    board_size = len(board)
    rows = board
    columns = [[board[i][j] for i in range(board_size)] for j in range(board_size)]
    diagonals = [
        [board[i][i] for i in range(board_size)],
        [board[i][board_size - i - 1] for i in range(board_size)]
    ]

    row_checks = [all_single_value(row, player.mark) for row in rows]
    column_checks = [all_single_value(column, player.mark) for column in columns]
    diagonal_checks = [all_single_value(diagonal, player.mark) for diagonal in diagonals]

    all_checks = [
        *row_checks,
        *column_checks,
        *diagonal_checks
    ]
    return any(all_checks)


def print_game_over(board, player):
    print_board(board)
    print(f'{player.name} won!')


def game_loop(board, players):
    current_player, next_player = players

    while True:
        print_board(board)
        place_mark(board, current_player)
        if check_game_over(board, current_player):
            print_game_over(board, current_player)
            break
        current_player, next_player = next_player, current_player


def start_game(board_size):
    (board, *players) = setup_game(board_size)
    print_welcome(players[0])
    game_loop(board, players)
