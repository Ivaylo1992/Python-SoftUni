def func_executor(*args):
    result = []
    for func_info in args:
        result.append(f'{func_info[0].__name__} - {func_info[0](*func_info[1])}')

    return '\n'.join(result)

def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4)))
)