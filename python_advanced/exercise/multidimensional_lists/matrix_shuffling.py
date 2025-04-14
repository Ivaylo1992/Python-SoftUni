def create_matrix(rows: int) -> list:
    # Creates the initial matrix which we'll be modified
    return [[el for el in input().split(' ')] for _ in range(rows)]

def swap_elements(
        matrix: list, row_one: int, col_one:int,
        row_two: int, col_two: int
) -> list:
    # Swaps elements in the matrix when the validity of the command is checked

    buffer = matrix[row_one][col_one]
    matrix[row_one][col_one] = matrix[row_two][col_two]
    matrix[row_two][col_two] = buffer

    return  matrix

def validate_initial_command(command_list: list, needed_elements_count: int, needed_command_name) -> bool:
    # Checks if the count of the elements and if the given command name are valid

    command_name = command_list[0]

    return len(command_list) == needed_elements_count and command_name == needed_command_name


def validate_indexes(
        rows: int, cols: int, row_one: int,col_one: int,
        row_two: int, col_two: int
) -> bool:
    # Check if all the given indexes are positive and are in range of the matrix rows and columns

    return (
            row_one < rows > row_two & col_one < cols > col_two
            & col_one >= 0 <= col_two >= 0 <= row_one >= 0 <= row_two
    )

def main() -> list:
    valid_command_name = 'swap'
    valid_elements_count = 5

    result = []

    r, c = [int(n) for n in input().split(' ')]
    m = create_matrix(r)

    while True:
        current_command = input()
        if current_command == 'END':
            break

        command_elements = current_command.split(' ')

        if not validate_initial_command(
                command_elements, valid_elements_count, valid_command_name):
            print('Invalid input!')
            continue

        r_one, c_one, r_two, c_two = [int(n) for n in command_elements[1::]]

        if not validate_indexes(
            r, c, r_one, c_one, r_two, c_two
        ):
            print('Invalid input!')
            continue

        m = swap_elements(
            m, r_one, c_one, r_two, c_two
        )

        for row in m:
            print(*row)


main()



# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END