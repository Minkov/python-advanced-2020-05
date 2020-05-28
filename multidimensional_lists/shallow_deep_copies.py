class Student:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


students = [Student(f'Student #{i}') for i in range(5)]
print(', '.join(str(s) for s in students))

students2 = students
print('*' * 20)
print(', '.join(str(s) for s in students))
print(', '.join(str(s) for s in students2))

students.append(Student('new'))
print('*' * 20)
print(', '.join(str(s) for s in students))
print(', '.join(str(s) for s in students2))

print('*' * 20)
print(' -- Shallow copies -- ')
students3 = [x for x in students]
students.append(Student('new 2'))
print(', '.join(str(s) for s in students))
print(', '.join(str(s) for s in students3))

students[1].name = 'Changed name'
print('*' * 20)

print(', '.join(str(s) for s in students))
print(', '.join(str(s) for s in students3))


print('*' * 20)
print(' -- Deep copies -- ')
students4 = [Student(x.name) for x in students]
students.append(Student('new 3'))
print(', '.join(str(s) for s in students))
print(', '.join(str(s) for s in students4))

students[2].name = 'Changed name'
print('*' * 20)

print(', '.join(str(s) for s in students))
print(', '.join(str(s) for s in students4))
