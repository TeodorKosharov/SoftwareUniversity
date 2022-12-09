# import re
#
# furniture_list = []
# pattern = r'>>(?P<name>[a-zA-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)'
# total_price = 0
#
# while True:
#     inp = input()
#     if inp == 'Purchase':
#         break
#
#     match = re.match(pattern, inp)
#     if match:
#         data = match.groupdict()
#         furniture_list.append(data['name'])
#         total_price += float(data['price']) * int(data['quantity'])
#
# if furniture_list:
#     print('Bought furniture:')
#     print('\n'.join(furniture_list))
#     print(f'Total money spend: {total_price:.2f}')
# else:
#     print('Bought furniture:')
#     print(f'Total money spend: {total_price:.2f}')



### Втори начин
import re

furniture_list = []
pattern = r'>>(?P<name>[a-zA-z]+)<<(?P<price>\d+(\.\d+)?)\!(?P<quantity>\d+)'
total_price = 0

while True:

    inp = input()
    if inp == 'Purchase':
        break

    match = re.findall(pattern, inp)
    if match:
        furniture_list.append(match[0][0])
        price = float(match[0][1])
        quantity = int(match[0][3])
        total_price += price * quantity

if furniture_list:
    print('Bought furniture:')
    print('\n'.join(furniture_list))
    print(f'Total money spend: {total_price:.2f}')
else:
    print('Bought furniture:')
    print(f'Total money spend: {total_price:.2f}')
