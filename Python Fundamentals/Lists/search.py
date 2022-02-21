n = int(input())
word = input()

first_list = []
second_list = []

for i in range(n):

    some_string = input()

    first_list.append(some_string)

    if word in some_string:
        second_list.append(some_string)

print(first_list)
print(second_list)
