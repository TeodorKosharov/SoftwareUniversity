import re

inp = input()

emoji_pattern = r'(?P<sep>::|\*\*)[A-Z][a-z]{2,}(?P=sep)'
matches = re.finditer(emoji_pattern, inp)
cool_threshold = re.findall(r'\d', inp)
emojis = []
cool_emojis = []

for match in matches:
    emojis.append(match.group())

cool_result = 1
for num in cool_threshold:
    cool_result *= int(num)

for curr_emoji in emojis:
    curr_emoji_formated_value = 0
    if ':' in curr_emoji:
        curr_emoji_formated = curr_emoji.replace(':', '')
    elif '*' in curr_emoji:
        curr_emoji_formated = curr_emoji.replace('*', '')

    for char in curr_emoji_formated:
        curr_emoji_formated_value += ord(char)
    if curr_emoji_formated_value >= cool_result:
        cool_emojis.append(curr_emoji)

print(f"Cool threshold: {cool_result}")
print(f"{len(emojis)} emojis found in the text. The cool ones are:")
for i in cool_emojis:
    print(i)
