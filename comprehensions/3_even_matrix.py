def read_matrix():
    rows_count = int(input())
    return [[int(x)
             for x in input().split(', ')]
            for _ in range(rows_count)]


def get_only_even_list(ll):
    return [x for x in ll if x % 2 == 0]


matrix = read_matrix()

print(
    [get_only_even_list(row) for row in matrix]
)
