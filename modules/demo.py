# import random
from random import randint, shuffle as random_shuffle
from termcolor import colored

from p1.my_module import f2
from p2 import f1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'I am {self.name}'

def shuffle(values):
    x = values.pop()
    values.insert(0, x)

nums = [randint(1, 500) for _ in range(20)]

# for _ in range(5):
#     print(random.choice(nums))

ss = set()
[ss.add(randint(1, 2)) for _ in range(2*20)]

print(ss)

print(nums)
shuffle(nums)
print(nums)
shuffle(nums)
print(nums)
shuffle(nums)
print(nums)
shuffle(nums)
print(nums)
shuffle(nums)
print(nums)

print(colored("Hello", 'green'))
print(colored("Hello", 'green', attrs=['bold']))

f2()