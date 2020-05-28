(rows_counts, columns_count) = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows_counts):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

sum_of_matrix = 0
for row in matrix:
    sum_of_matrix += sum(row)

print(sum_of_matrix)
print(matrix)