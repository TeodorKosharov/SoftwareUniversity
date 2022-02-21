cars = set()

for _ in range(int(input())):
    command = input().split(', ')
    if command[0] == 'IN':
        cars.add(command[1])
    else:
        cars.discard(command[1])

if cars:
    print(*cars, sep='\n')
else:
    print("Parking Lot is Empty")
