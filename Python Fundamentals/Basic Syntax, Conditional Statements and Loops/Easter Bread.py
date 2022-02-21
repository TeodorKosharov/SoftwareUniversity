budget = float(input())
price_1kg_flour = float(input())

price_one_pack_eggs = 0.75 * price_1kg_flour
milk_price = (price_1kg_flour + 0.25 * price_1kg_flour) / 4

price = price_1kg_flour + price_one_pack_eggs + milk_price

loaves = 0
colored_eggs = 0

while True:

    if price > budget:
        break

    budget -= price
    loaves += 1
    colored_eggs += 3

    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
