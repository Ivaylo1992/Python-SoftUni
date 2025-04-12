rows = int(input())

matrix = [[int(n) for n in input().split(', ')] for _ in range(rows)]

primary_sum = 0
secondary_sum = 0

primary_diagonal = []
secondary_diagonal = []

for row in range(rows):
    primary_num = matrix[row][row]
    primary_sum += primary_num

    secondary_num = matrix[row][-(row + 1)]
    secondary_sum += secondary_num

    primary_diagonal.append(primary_num)
    secondary_diagonal.append(secondary_num)


print(f'Primary diagonal: {", ".join(str(n) for n in primary_diagonal)}. Sum: {primary_sum}')
print(f'Secondary diagonal: {", ".join(str(n) for n in secondary_diagonal)}. Sum: {secondary_sum}')



