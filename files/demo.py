# file_path = 'e:/repos/python-advanced-2020-05/files/demo.py'
file_path = './files/demo.txt'

file = open(file_path, 'r')

while True:
    line = file.readline(15)
    if not line:
        break
    print(line)

print('*' * 30)
file = open(file_path, 'r')

while True:
    line = file.read(15)
    if not line:
        break
    print(line)