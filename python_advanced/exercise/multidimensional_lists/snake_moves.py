from collections import deque

def main():
    rows, cols = [int(n) for n in input().split(' ')]

    text = deque([el for el in input()])

    matrix = []

    for row in range(rows):
        matrix.append(deque([]))
        if row % 2 == 0:
            for _ in range(cols):
                element = text.popleft()
                matrix[row].append(element)
                text.append(element)

        else:
            for _ in range(cols):
                element = text.popleft()
                matrix[row].appendleft(element)
                text.append(element)

    for row in matrix:
        print(''.join(row))

main()



