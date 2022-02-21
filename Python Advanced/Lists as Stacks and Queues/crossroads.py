# from collections import deque
#
# green_light = int(input())
# yellow_light = int(input())
#
# cars = deque()
# passed_cars = 0
#
# while True:
#     command = input()
#     if command == 'END':
#         break
#     if command != 'green':
#         cars.append(command)
#     else:
#         seconds_left = green_light
#         while cars:
#             car = cars[0]
#             if len(car) < seconds_left:
#                 passed_cars += 1
#                 cars.popleft()
#                 seconds_left -= len(car)
#             else:
#                 if len(car) <= seconds_left + yellow_light:
#                     passed_cars += 1
#                     cars.popleft()
#                     break
#                 else:
#                     print('A crash happened!')
#                     print(f"{car} was hit at {car[seconds_left + yellow_light]}.")
#                     exit()
#
# print('Everyone is safe.')
# print(f"{passed_cars} total cars passed the crossroads.")


# Second variant:

from collections import deque

green_light = int(input())
yellow_light = int(input())
cars = deque()

passed_cars = 0

while True:
    command = input()
    if command == 'END':
        break

    if command != 'green':
        cars.append(command)
    else:
        current_green_light = green_light
        while cars:
            current_car = len(cars[0])
            if current_green_light > current_car:
                cars.popleft()
                passed_cars += 1
                current_green_light -= current_car
            elif current_green_light <= current_car:
                current_car -= current_green_light
                current_green_light = 0
                if yellow_light >= current_car:
                    cars.popleft()
                    passed_cars += 1
                    break
                else:
                    print("A crash happened!")
                    print(f"{cars[0]} was hit at {cars[0][current_car - yellow_light]}.")
                    exit()

print("Everyone is safe.")
print(f"{passed_cars} total cars passed the crossroads.")
