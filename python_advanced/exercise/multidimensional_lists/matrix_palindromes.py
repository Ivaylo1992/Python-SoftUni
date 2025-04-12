def create_matrix(rows: int, cols: int) -> list:
    start_num = 97

    matrix = [
        [f'{chr(r + start_num)}{chr(r + c + start_num)}{chr(r + start_num)}' for c in range(cols)] for r in range(rows)
    ]

    return matrix

r, c = [int(n) for n in input().split(' ')]

new_matrix = create_matrix(r, c)

for row in new_matrix:
    print(*row)

