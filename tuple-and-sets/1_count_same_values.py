def input_to_list(lines_count):
    return [input() for _ in range(lines_count)]

def input_to_list_until_command(command):
    result = []

    while True:
        line = input()
        if line == command:
            break
        result.append(line)

    return result

def count_numbers(values):
    values_counts = {}

    for value in values:
        if value not in values_counts:
            values_counts[value] = 0
        values_counts[value] += 1

    return values_counts


def print_result(values_counts):
    for (value, count) in values_counts.items():
        print(f'{value} - {count} times')


# print_result(
#     count_numbers(
#         map(
#             float,
#             '-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3'.split(' '))))
#
# print_result(
#     count_numbers(
#         map(
#             float,
#             '2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3'.split(' '))))

print_result(count_numbers(map(float, input().split(' '))))
