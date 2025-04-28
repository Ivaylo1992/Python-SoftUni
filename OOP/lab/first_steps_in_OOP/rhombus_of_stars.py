def print_top(num_rows):
    for row in range(1, num_rows + 1):
        print(' ' * (num_rows - row) + '* ' * row)

def print_bottom(num_rows):
    for row in range(1, num_rows):
        print(' ' * row + '* ' * (num_rows - row))

def print_rombus(num_rows):
    print_top(num_rows)
    print_bottom(num_rows)


rows = int(input())
print_rombus(rows)
