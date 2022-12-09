quantity_food = float(input())
quantity_hay = float(input())
quantity_cover = float(input())
guinea_weight = float(input())

total_food = quantity_food * 1000
total_hay = quantity_hay * 1000
total_cover = quantity_cover * 1000
guinea_weight_grams = guinea_weight * 1000

for day in range(1, 31):

    total_food -= 300

    if day % 2 == 0:
        total_hay -= 0.05 * total_food

    if day % 3 == 0:
        total_cover -= 1 / 3 * guinea_weight_grams

    if total_food <= 0 or total_hay <= 0 or total_cover <= 0:
        print("Merry must go to the pet store!")
        exit()

print(
    f"Everything is fine! Puppy is happy! Food: {total_food / 1000:.2f}, Hay: {total_hay / 1000:.2f}, Cover: {total_cover / 1000:.2f}.")
