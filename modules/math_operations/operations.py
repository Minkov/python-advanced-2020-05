def perform_sum(x, y):
    return x + y


def perform_subtraction(x, y):
    return x - y


def perform_operation(x, y, operation):
    if operation == '+':
        return perform_sum(x, y)
    elif operation == '-':
        return perform_subtraction(x, y)
