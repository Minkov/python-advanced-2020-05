def func(n):
    # base case
    if n == 0:
        return

    print(n)
    # recursive call
    func(n - 1)


# func(5)

# n
# [1, 2, 3, ..., n - 1, n]

# """
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1
# """

def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)


print(fact(4))
print(fact(5))


# 0 1 2 3 4 5 6  7
# 0 1 1 2 3 5 8 13

# fib(n) = fib(n-1) + fib(n-2)


def fib(n):
    print(f'Calculating fib({n})')
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) \
           + fib(n - 2)


# [print(fib(x)) for x in range(8)]

print(fib(7))