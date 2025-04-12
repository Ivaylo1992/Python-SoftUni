n = int(input())
flatten_matrix = []

for _ in range(n):
    flatten_matrix.extend(int(n) for n in input().split(', '))

print(flatten_matrix)

