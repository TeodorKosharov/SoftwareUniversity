# import re
#
#
# def split_symbol(element):
#     if '/' in element:
#         return '/'
#     elif '-' in element:
#         return '-'
#     elif '.' in element:
#         return '.'
#
#
# inp = input()
# pattern = r'\b\d{2}([\.\-\/])[A-Z]{1}[a-z]{2}\1\d{4}\b'
#
# matches = re.finditer(pattern, inp)
# result_list = [element.group() for element in matches]
#
# for item in result_list:
#     tokens = item.split(split_symbol(item))
#     print(f'Day: {tokens[0]}, Month: {tokens[1]}, Year: {tokens[2]}')

########## Втори начин:
import re

inp = input()
pattern = r'\b(?P<Day>\d{2})(?P<separator>[\.\-\/])(?P<Month>[A-Z]{1}[a-z]{2})(?P=separator)(?P<Year>\d{4})\b'

matches = re.finditer(pattern, inp)

valid_dates = [match.groupdict() for match in matches]

print('\n'.join([f'Day: {data["Day"]}, Month: {data["Month"]}, Year: {data["Year"]}' for data in valid_dates]))
