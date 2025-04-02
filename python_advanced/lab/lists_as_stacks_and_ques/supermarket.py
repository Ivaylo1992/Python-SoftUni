from collections import deque

clients = deque()

command = input()

while command != 'End':
    if command == 'Paid':
        for _ in range(0, len(clients)):
            print(clients.popleft())
    else:
        clients.append(command)
    
    command = input()

print(f'{len(clients)} people remaining.')

