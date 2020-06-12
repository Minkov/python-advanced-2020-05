def read_input():
    text = input()
    times = int(input())
    return (text, times)


def solve():
    try:
        (text, times) = read_input()
    except ValueError:
        return 'Variable times must be an integer'
    return text * times


print(solve())
