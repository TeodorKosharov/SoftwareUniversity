# countries = input().split(', ')
# capitals = input().split(', ')
#
# dictionary = {}
#
# for index in range(len(countries)):
#     current_country = countries[index]
#     current_capital = capitals[index]
#
#     dictionary[current_country] = current_capital
#
# for element in dictionary:
#     print(f'{element} -> {dictionary[element]}')
#

result = dict(zip(input().split(', '), input().split(', ')))
for key, value in result.items():
    print(f'{key} -> {value}')
