rows, cols = [int(n) for n in input().split(', ')]

matrix = [[int(num) for num in input().split(' ')] for _ in range(rows)]


for col_idx in range(cols):
    col_sum = 0
    for row_idx in range(rows):
        col_sum += matrix[row_idx][col_idx]

    print(col_sum)

