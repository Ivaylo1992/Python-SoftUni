iterations = int(input())
max_len_intersection = set()

for _ in range(iterations):
    range_one, range_two = input().split('-')

    first_start, first_end = [int(n) for n in range_one.split(',')]
    second_start, second_end = [int(n) for n in range_two.split(',')]

    first_set = {n for n in range(first_start, first_end + 1)}
    second_set = {n for n in range(second_start, second_end + 1)}

    intersection = first_set & second_set

    if len(intersection)  > len(max_len_intersection):
        max_len_intersection = intersection

print(f'Longest intersection is [{", ".join(str(n) for n in max_len_intersection)}]'
      f' with length {len(max_len_intersection)}')