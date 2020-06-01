def read_matrix():
    rows_count = int(input())
    return [[int(x)
             for x in input().split(', ')]
            for _ in range(rows_count)]


matrix = read_matrix()
flattened = [num
             for sublist in matrix
             for num in sublist]
print(flattened)
#
# flattened2 = []
# for sublist in matrix:
#     [flattened2.append(x) for x in sublist]
#     # for num in sublist:
#     #     flattened2.append(num)
#
# print(flattened)
# print(flattened2)
