set_one_len, set_two_len = [int(num) for num in input().split(' ')]

set_one = {int(input()) for _ in range(set_one_len)}
set_two = {int(input()) for _ in range(set_two_len)}

intersection = set_one & set_two

print('\n'.join(str(num) for num in intersection))

