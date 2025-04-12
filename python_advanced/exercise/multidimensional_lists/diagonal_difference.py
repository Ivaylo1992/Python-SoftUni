def find_diagonals_sums(rows: int, matrix: list) -> tuple:
    primary_sum = 0
    secondary_sum = 0

    for row in range(rows):
        primary_sum += matrix[row][row]
        secondary_sum += matrix[row][-(row + 1)]

    return primary_sum, secondary_sum

def create_matrix(rows: int) -> list:
    return [[int(n) for n in input().split()] for _ in range(rows)]

def get_diagonals_difference(diagonals) -> int:
    diff = abs(diagonals[0] - diagonals[1])
    return diff

r = int(input())
m = create_matrix(r)
d = find_diagonals_sums(r, m)
print(get_diagonals_difference(d))

