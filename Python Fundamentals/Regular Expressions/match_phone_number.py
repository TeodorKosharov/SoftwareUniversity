import re

phone_num = input()

pattern = r'\+359( |-)2\1\d{3}\1\d{4}\b'

x = re.finditer(pattern, phone_num)

result = [a.group() for a in x]

print(', '.join(result))
