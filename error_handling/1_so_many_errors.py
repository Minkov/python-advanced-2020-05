numbers_list = [int(x) for x in '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11'.split(", ")]
result = 1

for number in numbers_list:
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)
