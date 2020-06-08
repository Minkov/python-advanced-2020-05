# file_path = 'e:/repos/python-advanced-2020-05/files/demo.py'
file_path = './files/demo.txt'

file = open(file_path, 'r')
lines = file.readlines()

print(lines)