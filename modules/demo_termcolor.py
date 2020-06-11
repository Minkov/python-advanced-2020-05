# from termcolor import figlet_format
from pyfiglet import figlet_format

from demo import shuffle, nums, Person

print(figlet_format("Python",font="isometric1"))
print(figlet_format("Python",font="bubble"))
print(figlet_format("Python",font="block"))


vals = [1, 2, 3, 4]
shuffle(vals)
print(vals)
print(nums)

print(Person("Gosho", 3))