size = int(input())

matrix = [[el for el in input()] for _ in range(size)]

moves = (
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, 2),
    (-1, -2),
    (1, -2),
    (1, 2),
)


removed_knights = 0


while True:
    knight_with_most_attacks_pos = []
    max_attacks = 0

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == 'K':
                attacks = 0

                for move in moves:
                    row_pos = row + move[0]
                    col_pos = col + move[1]

                    if 0 <= row_pos < len(matrix) and 0 <= col_pos < len(matrix[row]):
                        if matrix[row_pos][col_pos] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knight_with_most_attacks_pos:
        matrix[knight_with_most_attacks_pos[0]][knight_with_most_attacks_pos[1]] = '0'
        removed_knights += 1
    else:
        print(removed_knights)
        break



# 8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK


# 5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0