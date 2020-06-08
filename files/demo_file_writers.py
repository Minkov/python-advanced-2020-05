file_path = './files/to_write_2.txt'

file = open(file_path, 'a')
file.writelines(['Pesho\n', 'Gosho\n'])
file.close()

with open(file_path, 'a') as file2:
    file2.writelines(['Stamat\n', 'Mariika\n'])
