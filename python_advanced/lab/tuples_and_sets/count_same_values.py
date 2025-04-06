numbers_tuple = tuple(float(num) for num in input().split())

occurrences = dict()

for number in numbers_tuple:
    if not occurrences.get(number):
        occurrences[number] = numbers_tuple.count(number)

result = [f"{n} - {c} times" for n, c in occurrences.items()]

print('\n'.join(result))