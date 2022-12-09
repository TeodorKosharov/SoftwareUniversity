from collections import deque

chocolate = [int(x) for x in input().split(', ')]  # stack
milk_cups = deque([int(x) for x in input().split(', ')])

milkshakes = 0

while milkshakes < 5 and chocolate and milk_cups:
    current_chocolate = chocolate[-1]
    current_milk_cup = milk_cups[0]

    if current_chocolate <= 0 and current_milk_cup <= 0:
        chocolate.pop()
        milk_cups.popleft()
        continue

    if current_chocolate <= 0:
        chocolate.pop()
        continue
    if current_milk_cup <= 0:
        milk_cups.popleft()
        continue

    if current_chocolate == current_milk_cup:
        milkshakes += 1
        chocolate.pop()
        milk_cups.popleft()
    else:
        removed_milk_cup = milk_cups.popleft()
        milk_cups.append(removed_milk_cup)
        chocolate[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print('Chocolate: ', end='')
    print(*chocolate, sep=', ')
else:
    print("Chocolate: empty")

if milk_cups:
    print('Milk: ', end='')
    print(*milk_cups, sep=', ')
else:
    print("Milk: empty")
