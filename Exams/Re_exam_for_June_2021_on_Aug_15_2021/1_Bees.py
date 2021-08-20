from collections import deque

working_bees = deque([int(el) for el in input().split(" ")])  # take first bee
nectar = [int(x) for x in input().split(" ")]  # take last nectar
process_symbols = deque([str(el) for el in input().split(" ")])
total_honey = 0
no_bee = False
no_nectar = False

while True:
    if not working_bees:
        no_bee = True
        break
    if not nectar:
        no_nectar = True
        break
    current_bee = working_bees[0]
    current_nectar = nectar[len(nectar) - 1]
    current_symbol = process_symbols[0]
    if current_nectar == 0 and current_symbol == "/":
        nectar.pop()
        continue

    if current_nectar >= current_bee:
        current_symbol = process_symbols[0]
        if current_symbol == "+":
            total_honey += abs(current_bee + current_nectar)
        elif current_symbol == "-":
            total_honey += abs(current_bee - current_nectar)
        elif current_symbol == "*":
            total_honey += abs(current_bee * current_nectar)
        elif current_symbol == "/":
            total_honey += abs(current_bee / current_nectar)
        working_bees.popleft()  # removing the bee
        nectar.pop()  # removing the nectar
        process_symbols.popleft()  # removing the symbol
    else:
        nectar.pop()  # removing the nectar

print(f"Total honey made: {abs(total_honey)}")
if not no_nectar:
    print(f"Nectar left: ", end=""), print(*nectar, sep=", ")

if not no_bee:
    print(f"Bees left: ", end=""), print(*working_bees, sep=", ")

