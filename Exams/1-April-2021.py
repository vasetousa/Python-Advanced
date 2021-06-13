pizza_order = [int(el) for el in input().split(", ")]
makers_capacity = [int(el) for el in input().split(", ")]

total_pizza = 0
current_order = 0

while True:
    if pizza_order:
        current_order = pizza_order[0]
    else:
        break
    if makers_capacity:
        current_maker = makers_capacity[len(makers_capacity) - 1]
    else:
        break
    if current_order <= 0:
        pizza_order.pop(0)
    elif not makers_capacity:
        break
    elif current_order > 10:    # order not valid (max 10)
        pizza_order.pop(0)
    elif current_order <= current_maker:  # remove both if true
        pizza_order.pop(0)
        makers_capacity.pop()
        total_pizza += current_order
    else:
        rest = current_order - current_maker
        makers_capacity.pop()
        pizza_order.pop(0)
        pizza_order.insert(0, rest)
        total_pizza += current_maker

if not pizza_order:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizza}")
    print(f"Employees: {', '.join(str(x) for x in makers_capacity)}")
else:
    print("Not all orders are completed.")
    print(f'Orders left: {", ".join(str(x) for x in pizza_order)}')