n = int(input())

capacity = 255
total_liters = 0

for line in range(1, n + 1):

    liters = int(input())

    if liters > capacity:
        print("Insufficient capacity!")
        continue

    capacity -= liters
    total_liters += liters

print(total_liters)
