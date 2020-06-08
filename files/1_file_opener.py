file_path='./files/File Opener/te3xt.txt'

try:
    open(file_path, 'r')
    print('File found')
except:
    print('File not found')