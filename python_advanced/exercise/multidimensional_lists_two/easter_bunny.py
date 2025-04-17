from sys import maxsize

size = int(input())
bunny_pos = []
field = []

best_moves = []
best_direction = ''
max_points = float('-inf')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    sublist = input().split()
    if 'B' in sublist:
        bunny_pos = [row, sublist.index('B')]

    field.append(sublist)


for direction, moves in directions.items():
    current_points = 0
    current_path = []
    row_pos = bunny_pos[0] + moves[0]
    col_pos = bunny_pos[1] + moves[1]

    while 0 <= row_pos < size and 0 <= col_pos < size:
        current_element = field[row_pos][col_pos]
        if current_element == 'X':
            break

        current_path.append([row_pos, col_pos])
        current_points += int(current_element)

        row_pos += moves[0]
        col_pos += moves[1]

    if current_points >= max_points:
        max_points = current_points
        best_moves = current_path
        best_direction = direction

print(best_direction)
print(*best_moves, sep='\n')
print(max_points)





# 8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0