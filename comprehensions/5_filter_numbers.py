def is_number_valid(number):
    return any([number % d == 0 for d in range(2, 11)])


start_number = int(input())
end_number = int(input())

print(
    [x for x in range(start_number, end_number + 1) if is_number_valid(x)]
)
