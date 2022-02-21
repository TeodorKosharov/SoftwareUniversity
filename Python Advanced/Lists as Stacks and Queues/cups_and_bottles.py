from collections import deque

cups_capacities = deque(list(map(int, input().split())))
bottles_capacities = list(map(int, input().split()))  # stack

wasted_water = 0

while cups_capacities:
    current_cup_capacity = cups_capacities[0]

    while current_cup_capacity > 0:
        current_cup_capacity -= bottles_capacities[-1]
        bottles_capacities.pop()
        if current_cup_capacity <= 0:
            wasted_water += -current_cup_capacity
            cups_capacities.popleft()

    if not bottles_capacities:
        print(f'Cups: {" ".join(map(str, cups_capacities))}')
        print(f"Wasted litters of water: {wasted_water}")
        exit(0)

print(f'Bottles: {" ".join(map(str, bottles_capacities))}')
print(f"Wasted litters of water: {wasted_water}")
