expression = input()

opening_indexes = []

for i in range(0, len(expression)):
    if expression[i] == '(':
        opening_indexes.append(i)
    elif expression[i] == ')':
        print(expression[opening_indexes.pop() : i + 1])