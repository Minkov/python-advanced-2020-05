def read_int_list_from_input(separator=' '):
    return [int(x) for x in input().split(separator)]


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(read_int_list_from_input())

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)

