start = ord(input())
end = ord(input())
given_string = input()

start = min(start, end)
end = max(start, end)

suma = 0
formed_str = ''

for i in range(start + 1, end):
    formed_str += chr(i)

for char in given_string:
    if char in formed_str:
        suma += ord(char)

print(suma)
