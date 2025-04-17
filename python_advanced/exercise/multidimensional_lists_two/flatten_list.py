flatten_list = input().split('|')
flatten_list.reverse()

print(' '.join(' '.join(flatten_list).split()))