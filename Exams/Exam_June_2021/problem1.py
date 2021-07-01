from collections import deque

milkshake = 0
chocolates = deque([int(el) for el in input().split(", ")]) # last one
cups_of_milk = deque([int(el) for el in input().split(", ")])   # first one
made_5 = False

while True:
    if not chocolates:
        break
    if not cups_of_milk:
        break
    last_choco = chocolates[len(chocolates)-1]
    first_milk = cups_of_milk[0]
    if last_choco <= 0:
        chocolates.pop()
        continue
    if first_milk <= 0:
        cups_of_milk.popleft()
        continue
    if milkshake >= 5:
        made_5 = True
        break
    if last_choco == first_milk:
        milkshake += 1
        chocolates.pop()
        cups_of_milk.popleft()
    else:
        if cups_of_milk:
            x = cups_of_milk.popleft()
            cups_of_milk.append(x)
            if chocolates:
                last_choco = (chocolates.pop() - 5)
                chocolates.append(last_choco)

if made_5 or milkshake >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    choco_list = list(chocolates)
    print(f"Chocolate: ", end=''), print(*choco_list, sep=', ')
else:
    print("Chocolate: empty")
if cups_of_milk:
    milk_list = list(cups_of_milk)
    print(f"Milk: ", end=''), print(*milk_list, sep=', ')
else:
    print("Milk: empty")

