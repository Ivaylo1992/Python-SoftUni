def operate(operator, *args):
    def add():
        return sum(args)

    def subtract():
        result = args[0]
        for num in args[1::]:
            result -= num
        return result

    def multiply():
        result = 1
        for num in args:
            result *= num
        return result

    def divide():
        result = args[0]
        for num in args[1::]:
            result /= num
        return result

    operations_mapper = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }

    return operations_mapper[operator]()

print(operate("*", 3, 4))