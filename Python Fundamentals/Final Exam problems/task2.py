import re

n = int(input())

pattern = r'(?P<start>.+)>(?P<first>\d{3})\|(?P<second>[a-z]{3})\|(?P<third>[A-Z]{3})\|(?P<fourth>[^<>]{3})<(?P=start)'

for _ in range(n):
    given_password = input()
    matches = re.finditer(pattern, given_password)
    is_password = False

    for match in matches:
        is_password = True
        first_group = match.group('first')
        second_group = match.group('second')
        third_group = match.group('third')
        fourth_group = match.group('fourth')
        encrypted_password = first_group + second_group + third_group + fourth_group

    if is_password:
        print(f"Password: {encrypted_password}")
    elif not is_password:
        print("Try another password!")
