iterations = int(input())
final_set = set()

for _ in range(iterations):
    set_to_add = set(input().split(' '))
    final_set = final_set | set_to_add

print('\n'.join(final_set))