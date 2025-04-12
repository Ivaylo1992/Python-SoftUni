rows, cols = [int(n) for n in input().split(', ')]

matrix = [[int(n) for n in input().split(', ')] for _ in range(rows)]

max_sum = float('-inf')
sub_matrix = []

for row in range(rows - 1):
    for col in range(cols - 1):
        top_left = matrix[row][col]
        bottom_left = matrix[row + 1][col]
        top_right = matrix[row][col + 1]
        bottom_right = matrix[row + 1][col + 1]

        current_sum = top_left + bottom_left + top_right + bottom_right

        if max_sum < current_sum:
            max_sum = current_sum
            sub_matrix = [
                [top_left, top_right],
                [bottom_left, bottom_right]
            ]

for row in sub_matrix:
    print(*row)
print(max_sum)


