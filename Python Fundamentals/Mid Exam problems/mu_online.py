rooms = input().split('|')

hp = 100
bitcoins = 0
passed_rooms = 0

for current_room in rooms:
    passed_rooms += 1
    data = current_room.split()
    if data[0] == 'potion':
        if hp + int(data[1]) > 100:
            healed = 100 - hp
            hp = 100
        else:
            hp += int(data[1])
            healed = int(data[1])
        print(f"You healed for {healed} hp.")
        print(f"Current health: {hp} hp.")
    elif data[0] == 'chest':
        print(f"You found {int(data[1])} bitcoins.")
        bitcoins += int(data[1])
    else:
        hp -= int(data[1])
        if hp > 0:
            print(f"You slayed {data[0]}.")
        else:
            print(f"You died! Killed by {data[0]}.")
            print(f"Best room: {passed_rooms}")
            exit()

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {hp}")
