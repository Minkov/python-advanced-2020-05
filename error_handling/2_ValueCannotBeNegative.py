class ValueCannotBeNegativeError(Exception):
    def __init__(self, value):
        msg = f'Value {value} is negative'
        super(ValueCannotBeNegativeError, self).__init__(msg)

n = 5
for _ in range(n):
    x = int(input())
    if x < 0:
        raise ValueCannotBeNegativeError(x)
