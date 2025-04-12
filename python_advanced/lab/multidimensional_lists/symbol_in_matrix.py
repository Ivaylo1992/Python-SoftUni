rows = int(input())

matrix = [[el for el in input()] for _ in range(rows)]

searched_symbol = input()

for row in range(rows):
    for col in range(rows):
        if matrix[row][col] == searched_symbol:
            print(f'({row}, {col})')
            exit()
else:
    print(f'{searched_symbol} does not occur in the matrix')

