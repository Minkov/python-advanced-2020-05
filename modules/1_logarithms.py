from math import log

def calc_log(x, b):
    if b == 'natural':
        return log(x)
    else:
        return log(x, b)


tests = [
    ('natural', 10),  # 2.3
    (2, 1024)  # 10
]

[print(calc_log(x, b)) for (b, x) in tests]
