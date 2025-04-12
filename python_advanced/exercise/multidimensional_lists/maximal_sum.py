def create_matrix(rows: int) -> list:
    return [[int(n) for n in input().split()] for _ in range(rows)]

def find_max_sum(matrix: list, rows: int,  cols: int) -> None:
    cube_matrix = []
    max_sum = float('-inf')

    for row in range(rows - 2):
        for col in range(cols - 2):
            top_left = matrix[row][col]
            top_mid = matrix[row][col + 1]
            top_right = matrix[row][col + 2]
            mid_left = matrix[row + 1][col]
            mid_mid = matrix[row + 1][col + 1]
            mid_right = matrix[row + 1][col + 2]
            bottom_left = matrix[row + 2][col]
            bottom_mid = matrix[row + 2][col + 1]
            bottom_right = matrix[row + 2][col + 2]

            cube_sum = sum([
                top_left, top_mid, top_right,
                mid_left, mid_mid, mid_right,
                bottom_left, bottom_mid, bottom_right]
            )

            if cube_sum  > max_sum:
                max_sum = cube_sum
                cube_matrix = [
                [top_left, top_mid, top_right],
                [mid_left, mid_mid, mid_right],
                [bottom_left, bottom_mid, bottom_right]
                ]

    print(f"Sum = {max_sum}")
    for row in cube_matrix:
        print(*row)


r, c = [int(n) for n in input().split(' ')]

m = create_matrix(r)
find_max_sum(m, r, c)

