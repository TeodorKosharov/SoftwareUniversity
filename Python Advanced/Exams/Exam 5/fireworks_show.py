from collections import deque

firework_effects = deque(int(x) for x in input().split(', '))
explosive_powers = [int(x) for x in input().split(', ')]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
show = False

while firework_effects and explosive_powers:
    current_effect = firework_effects[0]
    current_explosive = explosive_powers[-1]

    if current_effect <= 0:
        firework_effects.popleft()
        continue

    if current_explosive <= 0:
        explosive_powers.pop()
        continue

    result = current_effect + current_explosive

    if result % 3 == 0 and result % 5 != 0:
        palm_fireworks += 1
    elif result % 5 == 0 and result % 3 != 0:
        willow_fireworks += 1
    elif result % 3 == 0 and result % 3 == 0:
        crossette_fireworks += 1
    else:
        firework_effects.append(firework_effects.popleft() - 1)
        continue

    firework_effects.popleft()
    explosive_powers.pop()

    if willow_fireworks >= 3 and palm_fireworks >= 3 and crossette_fireworks >= 3:
        show = True
        break

if show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")

if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
