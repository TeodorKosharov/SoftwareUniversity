# import re
#
# single_string = input()
# food_data = {}
#
# pattern = r'([#|])(?P<item>[A-Za-z(\s)?]+)(\1)(?P<date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>10000|[0-9]{1,4})(\1)'
# matches = re.finditer(pattern, single_string)
# total_calories = 0
#
# for match in matches:
#     food = match.group('item')
#     date = match.group('date')
#     calories = int(match.group('calories'))
#     total_calories += calories
#
#     food_data[food] = [date, calories]
#
# survive_days = total_calories // 2000
# print(f"You have food to last you for: {survive_days} days!")
#
# for food_name, list_data in food_data.items():
#     print(f"Item: {food_name}, Best before: {list_data[0]}, Nutrition: {list_data[1]}")


import re

single_string = input()
food_data = []

pattern = r'([#|])(?P<item>[A-Za-z(\s)?]+)(\1)(?P<date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>10000|[0-9]{1,4})(\1)'
matches = re.finditer(pattern, single_string)
total_calories = 0

for match in matches:
    current_match = match.groupdict()
    total_calories += int(current_match['calories'])
    food_data.append(current_match)

survive_days = total_calories // 2000
print(f"You have food to last you for: {survive_days} days!")

for i in food_data:
    print(f"Item: {i['item']}, Best before: {i['date']}, Nutrition: {i['calories']}")
