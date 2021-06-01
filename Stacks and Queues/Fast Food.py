from collections import deque
orders = deque()
last_orders = []

food_quantity = int(input())
numbers = [orders.append(int(el)) for el in input().split() if el >= "0"]

max_order = max(orders)
if sum(orders) <= 0:
    exit(0)
print(max_order)

while orders:
    current_order = orders.popleft()
    if food_quantity >= current_order:
        food_quantity -= current_order
    else:
        last_orders.append(current_order)
        for i in range(len(orders)):
            current_pop = orders.popleft()
            last_orders.append(current_pop)
        break
numbers.clear()
orders = [str(el) for el in orders]

if len(last_orders) == 0:
    print('Orders complete')
    # print(food_quantity)

else:
    print(f"Orders left: ", end=''), print(*last_orders, sep=', ')
    # print(food_quantity)