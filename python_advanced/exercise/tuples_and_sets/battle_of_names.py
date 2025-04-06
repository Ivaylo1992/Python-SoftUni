iterations_count = int(input())
row = 1

odd_sums = set()
even_sums = set()

for _ in range(iterations_count):
    name = input()
    ascii_sum = int(sum(ord(ch) for ch in name) / row)
    row += 1

    if ascii_sum % 2 == 0:
        even_sums.add(ascii_sum)
    else:
        odd_sums.add(ascii_sum)

odd_sums_sum = sum(n for n in odd_sums)
even_sums_sum = sum(n for n in even_sums)

if odd_sums_sum == even_sums_sum:
    print(', '.join(str(n) for n in odd_sums | even_sums))
elif odd_sums_sum > even_sums_sum:
    print(', '.join(str(n) for n in odd_sums - even_sums))
else:
    print(', '.join(str(n) for n in odd_sums ^ even_sums))