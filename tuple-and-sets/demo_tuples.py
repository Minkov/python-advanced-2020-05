tt = (
    'John', # 0
    'John', # 1
    'George', # 2
    'Megan', # 3
    'John', # 4
    'George', # 5
    'Tim', # 6
)

d = {
    'name': 'John',
    'age': 15
}

for (key, value) in d.items():
    print(key)
    print(value)

# (first_name, last_name, third_name, *rest) = tt
# print(first_name)
# print(last_name)
# print(rest)
#
# print(tt.index('Megan'))
# print(tt.count('Megan'))
# print(tt.count('George'))
# print(tt.count('John'))
#
# index = - 1
#
# for _ in range(tt.count('John')):
#     index = tt.index('John', index + 1)
#     print(index)
