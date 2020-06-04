# N=3
# [1, 1, 1]
"""
+1+1+1 = 3
+1+1-1 = 1
+1-1+1 = 1
+1-1-1 = -1

-1+1+1 = 1
-1+1-1 = -1
-1-1+1 = -1
-1-1-1 = -3
"""

def expressions(numbers, current_result, expression=''):
    if not numbers:
        return [(expression, current_result)]
    result_plus = expressions(
        numbers[1:],
        current_result + numbers[0],
        f'{expression}+{numbers[0]}')
    result_minus = expressions(
        numbers[1:],
        current_result - numbers[0],
        f'{expression}-{numbers[0]}')
    return result_plus + result_minus

result = expressions([1] * 4, 0)
[print(f'{exp_str}={exp_result}') for (exp_str, exp_result) in result]