string_inp = input().split()
new_list = [product for product in string_inp if len(product) % 2 == 0]

for element in new_list:
    print(element)
