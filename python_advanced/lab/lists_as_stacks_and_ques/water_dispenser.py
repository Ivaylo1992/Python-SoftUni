from collections import deque

dispenser_liters = int(input())

people_que = deque()
command = input()

while command != 'Start':
    people_que.append(command)
    command = input()

command = input()

while command != 'End':
    if command.isdigit():
        needed_water = int(command)
        person = people_que.popleft()

        if dispenser_liters >= needed_water:
            print(f"{person} got water")
            dispenser_liters -= needed_water
        else:
            print(f"{person} must wait")
    else:
        _, refill_liters = command.split()
        dispenser_liters += int(refill_liters)

    command = input()

print(f"{dispenser_liters} liters left")