def remove_all_products_required(q, ar):
    for el in ar:
        counter = q.lett_count(el)
        for i in range(counter):
            q.remove(el)
    return q


def stock_availability(start_list, *args):
    from collections import deque
    q = deque(start_list)
    ar = deque(args)
    command = ar.popleft()
    if command == "delivery":
        q.extend(ar)
    elif command == "sell":
        args_len = len(args)
        if args_len == 1:  # check if there is more than a command in the args
            q.popleft()
        elif args_len == 2:  # 2 means there is a command and a number or a name(s) to remove
            value = str(ar[0])  # value = number or name
            if value.isdigit():
                value = int(value)
                for _ in range(value):  # remove "value" cupcakes from q
                    q.popleft()
                    if _ == len(start_list) - 1:  # checks when "value" = count products to avoid index error
                        return list(q)
            else:
                # removing the requested item
                qq = remove_all_products_required(q, ar)
                return list(q)
        elif args_len > 2:
            # removing ALL requested items
            qq = remove_all_products_required(q, ar)
            return list(q)
    return list(q)


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
