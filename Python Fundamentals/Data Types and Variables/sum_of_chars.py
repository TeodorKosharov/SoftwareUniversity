n = int(input())

suma = 0

for character in range(n):
    char = input()

    suma += ord(char)

print(f"The sum equals: {suma}")
