key = int(input())

n = int(input())

total = ''

for line in range(n):
    character = input()

    new_character_value = ord(character) + key

    total += chr(new_character_value)

print(total)
