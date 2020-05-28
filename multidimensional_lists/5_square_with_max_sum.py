def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


def get_submatrix_sum(matrix, row, col, size):
    # return matrix[row][col] + matrix[row][col + 1] + \
    #        matrix[row + 1][col] + matrix[row + 1][col + 1]
    the_sum = 0
    for r in range(row, row + size):
        for c in range(col, col + size):
            the_sum += matrix[r][c]
    return the_sum


def print_summatrix(matrix, row, col, size):
    for r in range(row, row + size):
        for c in range(col, col + size):
            print(matrix[r][c], end=' ')
        print()


(rows_count, columns_count) = read_int_list_from_input(', ')
matrix = [read_int_list_from_input(', ') for _ in range(rows_count)]
size = 3

best_position = (0, 0)
best_value = get_submatrix_sum(matrix, 0, 0, size)

# rows - 1 = rows - size + x
# -1 = x - size
# x = size - 1
# size = 2 => x = 2 - 1 = 1
for row in range(len(matrix) - size + 1):
    for col in range(len(matrix[row]) - size + 1):
        current_value = get_submatrix_sum(matrix, row, col, size)
        if best_value < current_value:
            best_value = current_value
            best_position = (row, col)

(best_row, best_col) = best_position
print_summatrix(matrix, best_row, best_col, size)
print(best_value)
