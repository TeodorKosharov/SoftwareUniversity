# events = input()
#
# events_list = events.split('|')
#
# energy = 100
# coins = 100
#
# for element in events_list:
#
#     cell_list = element.split('-')
#     event = cell_list[0]
#     number = int(cell_list[1])
#
#     if event == 'rest':
#         gained_energy = number
#         energy += gained_energy
#
#         if energy > 100:
#             energy = 100
#
#         if energy == 100:
#             gained_energy = 0
#
#         print(f"You gained {gained_energy} energy.")
#         print(f"Current energy: {energy}.")
#
#     elif event == 'order':
#
#         if energy >= 30:
#             print(f"You earned {number} coins.")
#             coins += number
#             energy -= 30
#         else:
#             energy += 50
#             print("You had to rest!")
#
#     else:
#         needed_coins = number
#
#         if needed_coins < coins:
#             print(f"You bought {event}.")
#             coins -= needed_coins
#         else:
#             print(f"Closed! Cannot afford {event}.")
#             exit()
#
# if coins > 0:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {energy}")


events = input().split('|')

energy = 100
coins = 100

for event in events:
    event_data = event.split('-')

    if event_data[0] == 'rest':
        if energy + int(event_data[1]) > 100:
            gained = 100 - energy
        else:
            gained = int(event_data[1])

        energy += gained
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")

    elif event_data[0] == 'order':
        if energy >= 30:
            print(f"You earned {event_data[1]} coins.")
            coins += int(event_data[1])
            energy -= 30
        else:
            print("You had to rest!")
            energy += 50

    else:
        if coins > int(event_data[1]):
            print(f"You bought {event_data[0]}.")
            coins -= int(event_data[1])
        else:
            print(f"Closed! Cannot afford {event_data[0]}.")
            exit()

print("Day completed!")
print(f"Coins: {coins}")
print(f"Energy: {energy}")
