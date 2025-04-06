logs = int(input())
usernames = {input() for _ in range(logs)}
print('\n'.join(usernames))