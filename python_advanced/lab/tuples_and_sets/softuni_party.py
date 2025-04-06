codes_count = int(input())
reservations = set()

for _ in range(codes_count):
    reservation_code = input()
    reservations.add(reservation_code)

command = input()

while command != 'END':
    reservation = command
    reservations.remove(reservation)

    command = input()

normal_reservations = []
all_reservations = list(r for r in reservations)
all_reservations.sort()

print(len(all_reservations))

for res in all_reservations:
    if res[0].isnumeric():
        print(res)
    else:
        normal_reservations.append(res)

if normal_reservations:
    print('\n'.join(normal_reservations))

# 5
# 7IK9Yo0h
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# tSzE5t0p
# 9NoBUajQ
# Ce8vwPmE
# SVQXQCbc
# END