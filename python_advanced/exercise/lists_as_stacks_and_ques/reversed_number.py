numbers = input().split()

iterations = len(numbers)

[print(numbers.pop(), end=' ') for _ in range(iterations)]

