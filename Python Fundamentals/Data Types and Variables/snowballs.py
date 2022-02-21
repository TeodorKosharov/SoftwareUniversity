from sys import maxsize

number_of_snowballs = int(input())

snowball_value = 0
max_value = -maxsize
max_weight = 0
max_time = 0
max_quality = 0

for snowball in range(1, number_of_snowballs + 1):

    snowball_weight = int(input())
    time = int(input())
    quality = int(input())

    snowball_value = (snowball_weight / time) ** quality

    if snowball_value > max_value:
        max_value = snowball_value
        max_weight = snowball_weight
        max_quality = quality
        max_time = time

print(f'{max_weight} : {max_time} = {max_value:.0f} ({max_quality})')
