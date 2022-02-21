from collections import deque

orders = deque(int(x) for x in input().split(', '))
employee_capacities = [int(x) for x in input().split(', ')]

pizzas_made = 0

while orders and employee_capacities:
    current_order = orders.popleft()
    current_capacity = employee_capacities.pop()

    if current_order > 10 or current_order <= 0:
        employee_capacities.append(current_capacity)
        continue

    if current_order > current_capacity:
        orders.appendleft(current_order - current_capacity)
        pizzas_made += current_capacity
        continue

    pizzas_made += current_order

if not orders:
    print('All orders are successfully completed!')
    print(f'Total pizzas made: {pizzas_made}')
    print(f'Employees: {", ".join(map(str, employee_capacities))}')

elif orders and not employee_capacities:
    print('Not all orders are completed.')
    print(f'Orders left: {", ".join(map(str, orders))}')
