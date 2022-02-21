def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    backet = set()
    result = ''

    for product, info in kwargs.items():
        if len(backet) == 5:
            break

        price = info[0] * info[1]
        if budget >= price:
            budget -= price
            backet.add(product)
            result += f"You bought {product} for {price:.2f} leva." + "\n"

    return result


print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))
