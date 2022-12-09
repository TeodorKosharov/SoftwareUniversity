reservation_numbers = set()

for _ in range(int(input())):
    reservation_numbers.add(input())

while True:
    command = input()
    if command == 'END':
        break
    reservation_numbers.discard(command)

reservation_numbers = sorted(reservation_numbers)
print(len(reservation_numbers))
print(*reservation_numbers, sep='\n')
