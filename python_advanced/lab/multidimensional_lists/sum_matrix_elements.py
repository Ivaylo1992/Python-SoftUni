rows, cols = [int(el) for el in input().split(', ')]

matrix_sum = 0
matrix = []

for _ in range(rows):
    sublist = [int(el) for el in input().split(', ')]
    matrix.append(sublist)
    matrix_sum += sum(sublist)

print(matrix_sum)
print(matrix)

