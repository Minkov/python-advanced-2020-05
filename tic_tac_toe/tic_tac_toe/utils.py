def decode_position(position, board_size):
    row = (position - 1) // board_size
    column = (position - 1) % board_size
    return (row, column)


def all_single_value(ll, value):
    for v in ll:
        if v != value:
            return False
    return True
