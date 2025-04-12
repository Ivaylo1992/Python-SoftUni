rows = int(input())

matrix = [[int(n) for n in input().split(' ')] for _ in range(rows)]

diagonal_sum = 0

for idx in range(rows):
    diagonal_sum += matrix[idx][idx]

print(diagonal_sum)


