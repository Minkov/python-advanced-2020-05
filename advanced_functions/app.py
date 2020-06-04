# def func3():
#     print(sum([1, 2, 3, 4]))
#
#
# lambda_func = lambda : print(sum([1, 2, 3, 4]))
#
# lambda_sum = lambda x, y: x + y
# print(lambda_sum(1, 5))
#
# def increment(x):
#     return x + 1
#
# ll = list(range(5, 0, -1))
# print(ll)
# ll2 = list(map(increment, ll))
# print(ll2)
#
# ll3 = [increment(x) for x in ll]
# print(ll3)


def is_even(x):
    return x % 2 == 0


def increment(x):
    return x + 1


def sort_by(x):
    return x % 4

ll = [5, 1, 2, -5, 2, 7, -10, 11, 3, 4]

print(ll)

print(list(filter(lambda x: x % 2 == 0, ll)))
print(list(filter(is_even, ll)))

print([x for x in ll if x % 2 == 0])
print([x for x in ll if is_even(x)])

print(list(map(lambda x: x + 1, ll)))
print(list(map(increment, ll)))

print([x + 1 for x in ll])
print([increment(x) for x in ll])

print(list(map(lambda x: x + 1, filter(lambda x: x % 2 == 0, ll))))
print([x + 1 for x in ll if x % 2 == 0])

print(sorted(ll))
print(sorted(ll, reverse=False))
print(sorted(ll, reverse=True))
print(sorted(ll, key=lambda x: x))
print(sorted(ll, key=lambda x: x % 4))
print(sorted(ll, key=sort_by))

ll2 = sorted(ll)
print(ll)
print(ll2)
ll.sort()
print(ll)

dd = {
    'y': -1,
    'x': 1,
}

def order_by2(pair):
    (key, value) = pair
    return (value, key)

print(dd)
print(sorted(dd))
print(sorted(dd, key=lambda k: k))
print(sorted(dd.items(), key=lambda k: k[1]))
print(dict(sorted(dd.items())))
print(dict(sorted(dd.items(), key=lambda tokens: (tokens[1], tokens[0]))))
print(dict(sorted(dd.items(), key=order_by2)))

operator = '*'

exp = f'2{operator}3'
print(eval(exp))
