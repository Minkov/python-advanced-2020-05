def my_sum(x, *args):
    print(f'Index 0: {args[0]}')
    return x + sum(args)

def fullname(firstname, lastname):
    return f'{firstname} {lastname}'

def kwargs_func(**kwargs):
    print(kwargs)

def positional_args_kwargs(x, *args, **kwargs):
    print(x)
    print(args)
    print(kwargs)


print(my_sum(1, 5))
print(my_sum(1, 2))
print(my_sum(1, 2, 3))
print(fullname('Doncho', 'Minkov'))
print(fullname(lastname='Minkov', firstname='Doncho'))
kwargs_func(firstname='Doncho')
positional_args_kwargs(1, 2, 3, 4, 5, 6, first_name='Doncho', last_name='Minkov')

person_info = {
    'firstname': 'Doncho',
    'lastname': 'Minkov',
    'age': 18,
}

print(fullname(person_info['firstname'], person_info['lastname']))
# print(fullname(**person_info))

ll = [1, 2, 3, ]
dd = {'x':1, 'y': 2}
