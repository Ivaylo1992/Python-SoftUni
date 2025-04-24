def recursive_power(number, power):
    if power == 1:
        return number
    return recursive_power(number, power - 1) * number

print(recursive_power(10, 100))