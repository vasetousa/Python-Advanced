from collections import deque
orders = deque()
last_orders = []

food_quanity = int(input())
numbers = [orders.append(int(el)) for el in input().split()]

max_order = max(orders)
print(max_order)

while orders:
    current_order = orders.popleft()
    if food_quanity >= current_order:
        food_quanity -= current_order
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
else:
    for el in last_orders:
        el = str(el)
        numbers.append(el)
    print(f"Orders left: {', '.join(numbers)}")