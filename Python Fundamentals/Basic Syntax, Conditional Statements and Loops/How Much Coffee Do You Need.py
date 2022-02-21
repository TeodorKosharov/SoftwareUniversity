total_coffee = 0

while True:

    command = input()

    if command == "END":

        if total_coffee > 5:
            print("You need extra sleep")
            exit()
        break

    if command.lower() == "coding" \
            or command.lower() == "dog" \
            or command.lower() == "cat" \
            or command.lower() == "movie":

        total_coffee += 1

        if command.isupper():
            total_coffee += 1

print(total_coffee)