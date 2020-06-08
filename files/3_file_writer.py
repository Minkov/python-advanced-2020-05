file_path='my_first_file.txt'
text='I just created my first file!'

with open(file_path, 'w') as file:
    print(text, file=file)