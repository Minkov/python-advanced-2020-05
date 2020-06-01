# def transform(number):
#     return number ** 2
#
#
# numbers = [1, 2, 3, 4, 5]
#
# transformed_numbers = [transform(number) for number in numbers]
# print(numbers)
# print(transformed_numbers)
# print([x % 3 for x in numbers])
# print({x % 3 for x in numbers})
# print({print(x % 3) for x in numbers})


matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)

def generate_row(size):
    return [j for j in range(size)]

matrix = [generate_row(3) for _ in range(3)]
print(matrix)
