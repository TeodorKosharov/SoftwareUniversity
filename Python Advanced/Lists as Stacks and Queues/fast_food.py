from collections import deque

food_quantity = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))

while orders:
    if orders[0] <= food_quantity:
        food_quantity -= orders[0]
        orders.popleft()
    else:
        print('Orders left:', end=' ')
        while orders:
            print(orders.popleft(), end=' ')
        exit(0)

print('Orders complete')
