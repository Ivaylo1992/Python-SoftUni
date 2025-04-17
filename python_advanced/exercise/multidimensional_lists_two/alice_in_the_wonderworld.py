size = int(input())

field = []
alice_position = []
needed_tea_bags = 10
collected_tee_bags = 0

for row in range(size):
    field.append(input().split(' '))

    if 'A' in field[row]:
        alice_position = [row, field[row].index('A')]
        field[alice_position[0]][alice_position[1]] = '*'

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

command = input()

row, col = [
    alice_position[0] + directions[command][0],
    alice_position[1] + directions[command][1]
]

while 0 <= row < size and 0 <= col < size:
    current_value = field[row][col]
    field[row][col] = '*'

    if current_value == 'R':
        break

    if current_value.isnumeric():
        collected_tee_bags += int(current_value)

    if collected_tee_bags >= needed_tea_bags:
        break

    command = input()
    row += directions[command][0]
    col += directions[command][1]


print('She did it! She went to the party.'
      if collected_tee_bags >= needed_tea_bags else 'Alice didn\'t make it to the tea party.')

for row in field:
    print(' '.join(row))


# 5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left

# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right