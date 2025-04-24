def multiply(*args):
    sum_nums = 1

    for num in args:
        sum_nums *= num

    return sum_nums

print(multiply(4, 5, 6, 1, 3))