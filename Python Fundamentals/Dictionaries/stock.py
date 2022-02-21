# string = input().split(' ')
# search_products = input().split(' ')
#
# foods = {}
#
# end = int(len(string) / 2)
# index = 0
# for i in range(end):
#     key = string[index]
#     value = int(string[index + 1])
#     foods[key] = value
#     index += 2
#
# food_products = list(foods.keys())
#
# for product in search_products:
#     if product in food_products:
#         print(f"We have {foods[product]} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")


inp = input().split()
search_foods = input().split()

foods = [f for f in inp if inp.index(f) % 2 == 0]
quantities = [int(q) for q in inp if inp.index(q) % 2 == 1]
result = dict(zip(foods, quantities))

for current_food in search_foods:
    if current_food in result:
        print(f"We have {result[current_food]} of {current_food} left")
    else:
        print(f"Sorry, we don't have {current_food}")
