from collections import deque

def check_coordinates(row: int, col:int, matrix: list) -> bool:
    is_valid_row = 0 <= row < len(matrix)
    is_valid_col = 0 <= col < len(matrix[row])

    return is_valid_row and is_valid_col

def calculate(action: str, value_one: int, value_two: int) -> int:
    if action == 'Add':
        return value_one + value_two
    elif action == 'Subtract':
        return value_one - value_two

def create_matrix(rows: int) -> list:
    return [[int(el) for el in input().split()] for _ in range(rows)]

def main(matrix):
    """
    Runs the main command loop to modify the matrix based on user input.

    Accepts commands: 'Add', 'Subtract', and stops on 'END'.
    Validates coordinates and updates the matrix accordingly.
    Finally, prints the modified matrix.
    """
    while True:
        command = deque(input().split())

        if command[0] == 'END':
            break

        current_action = command.popleft()
        curr_row, curr_col, curr_val = [int(n) for n in command]

        if check_coordinates(curr_row, curr_col, matrix):
            old_value = matrix[curr_row][curr_col]
            new_value = calculate(current_action, old_value, curr_val)
            matrix[curr_row][curr_col] = new_value
        else:
            print('Invalid coordinates')

    for row in matrix:
        print(*row)


rows_count = int(input())
initial_matrix = create_matrix(rows_count)

if __name__ == '__main__':
    main(initial_matrix)

# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END


# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END