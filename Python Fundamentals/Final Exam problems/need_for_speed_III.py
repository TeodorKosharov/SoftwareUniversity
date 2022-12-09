n = int(input())

cars = {}

for _ in range(n):
    inp = input().split('|')

    car = inp[0]
    mileage = int(inp[1])
    fuel = int(inp[2])
    cars[car] = [mileage, fuel]

while True:
    command = input()
    if command == 'Stop':
        break
    command_list = command.split(' : ')
    action = command_list[0]

    if action == 'Drive':
        given_car = command_list[1]
        given_distance = int(command_list[2])
        given_fuel = int(command_list[3])

        if given_fuel > cars[given_car][1]:
            print("Not enough fuel to make that ride")
        elif cars[given_car][1] > given_fuel:
            print(f"{given_car} driven for {given_distance} kilometers. {given_fuel} liters of fuel consumed.")
            cars[given_car][0] += given_distance
            cars[given_car][1] -= given_fuel

            if cars[given_car][0] >= 100000:
                print(f"Time to sell the {given_car}!")
                cars.pop(given_car)

    elif action == 'Refuel':
        given_car = command_list[1]
        given_fuel = int(command_list[2])
        if cars[given_car][1] + given_fuel > 75:
            needed_fuel = 75 - cars[given_car][1]
            cars[given_car][1] = 75
        elif cars[given_car][1] + given_fuel <= 75:
            cars[given_car][1] += given_fuel
            needed_fuel = given_fuel

        print(f"{given_car} refueled with {needed_fuel} liters")

    elif action == 'Revert':
        given_car = command_list[1]
        given_kilometers = int(command_list[2])
        cars[given_car][0] -= given_kilometers
        if cars[given_car][0] < 10000:
            cars[given_car][0] = 10000
        else:
            print(f"{given_car} mileage decreased by {given_kilometers} kilometers")

cars = dict(sorted(cars.items(), key=lambda x: (-x[1][0], x[0])))

for current_car, car_data in cars.items():
    print(f"{current_car} -> Mileage: {car_data[0]} kms, Fuel in the tank: {car_data[1]} lt.")
