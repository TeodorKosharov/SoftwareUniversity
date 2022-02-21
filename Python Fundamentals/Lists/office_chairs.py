n = int(input())

total_free_chairs = 0
condition = False
for room in range(1, n + 1):

    command = input().split()
    free_chairs = len(str(command[0]))
    people = int(command[1])

    if people > free_chairs:
        print(f"{people - free_chairs} more chairs needed in room {room}")
        condition = True
    else:
        total_free_chairs += free_chairs - people

if not condition:
    print(f"Game On, {total_free_chairs} free chairs left")
