from collections import deque

bomb_effects = deque([int(x) for x in input().split(', ')])
bomb_casings = [int(x) for x in input().split(', ')]  # stack

bombs = {'Datura Bombs': 0, 'Cherry Bombs': 0, 'Smoke Decoy Bombs': 0}
is_pouch_filled = False

while bomb_effects and bomb_casings:
    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    value = current_effect + current_casing

    if value == 40:
        bombs['Datura Bombs'] += 1
    elif value == 60:
        bombs['Cherry Bombs'] += 1
    elif value == 120:
        bombs['Smoke Decoy Bombs'] += 1
    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)

    if bombs['Datura Bombs'] >= 3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >= 3:
        is_pouch_filled = True
        break

if is_pouch_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f'Bomb Effects: ', end='')
    print(*bomb_effects, sep=', ')

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    print(f'Bomb Casings: ', end='')
    print(*bomb_casings, sep=', ')

print(f"Cherry Bombs: {bombs['Cherry Bombs']}")
print(f"Datura Bombs: {bombs['Datura Bombs']}")
print(f"Smoke Decoy Bombs: {bombs['Smoke Decoy Bombs']}")
