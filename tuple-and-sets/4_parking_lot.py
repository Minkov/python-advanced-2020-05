parking_lot = set()

commands_count = int(input())

for _ in range(commands_count):
    (command, car) = input().split(', ')
    if command == 'IN':
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

if parking_lot:
    [print(car) for car in parking_lot]
else:
    print('Parking Lot is Empty')
