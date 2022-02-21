def stock_availability(inventory: list, action, *args):
    if action == "delivery":
        inventory.extend(args)
        return inventory
    else:
        if args:
            if type(args[0]) == int:
                return inventory[int(args[0]):]
            else:
                for product in args:
                    if product in inventory:
                        inventory = [x for x in inventory if x != product]
                return inventory
        else:
            return inventory[1:]


print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
