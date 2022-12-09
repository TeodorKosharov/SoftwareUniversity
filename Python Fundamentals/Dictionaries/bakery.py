# string = input().split(' ')
#
# foods = {}
# index = 0
# end = int(len(string) / 2)
#
# for i in range(end):
#     key = string[index]
#     value = int(string[index + 1])
#     index += 2
#     foods[key] = value
#
# print(foods)

inp = input().split()
foods = [f for f in inp if inp.index(f) % 2 == 0]
quantities = [int(q) for q in inp if inp.index(q) % 2 == 1]
print(dict(zip(foods, quantities)))
