def calculate_sum_with_loop(file_path):
    file = open(file_path, 'r')
    result = 0

    for number_str in file:
        result += int(number_str)
    return result

def calculate_sum_with_readline(file_path):
    file = open(file_path, 'r')
    result = 0

    while True:
        number_str = file.readline()
        if not number_str:
            break
        result += int(number_str)
    return result

file_path = './files/File Reader/numbers.txt'

print(calculate_sum_with_loop(file_path))
print(calculate_sum_with_readline(file_path))