string = input()

lower_letters = string.lower()  # Превръщаме стринга изцяло в малки букви

water_counter = lower_letters.count('water')
sand_counter = lower_letters.count('sand')
fish_counter = lower_letters.count('fish')
sun_counter = lower_letters.count('sun')

print(water_counter + sun_counter + sand_counter + fish_counter)
