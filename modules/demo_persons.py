class Person_str:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'I am {self.name}'

class Person_no_str:
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Person_no_str('Gosho', 5))
print(Person_str('Gosho', 5))
print(str(Person_str('Gosho', 5)))