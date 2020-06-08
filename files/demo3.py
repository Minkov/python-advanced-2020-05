# file_path = 'e:/repos/python-advanced-2020-05/files/demo.py'
file_path = './files/demo.txt'

file = open(file_path, 'r')

index = 0
for line in file:
    print(f'{index}: {line.strip()}')
    index += 1
