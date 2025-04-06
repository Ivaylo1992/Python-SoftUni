logs = int(input())

parking_lot = {}

for _ in range(logs):
    car_direction, car_number = input().split(', ')
    parking_lot[car_number] = car_direction

is_empty = True

for car, direction in parking_lot.items():
    if direction == 'IN':
        print(car)
        is_empty = False

if is_empty:
    print('Parking Lot is Empty')

# 4
# IN, CA2844AA
# IN, CA1234TA
# OUT, CA2844AA
# OUT, CA1234TA