heroes = input().split(", ")
inventory = {hero: {} for hero in heroes}

items = input()
while not items == "End":
    hero, item, cost = items.split('-')
    cost = int(cost)
    if item not in inventory[hero]:
        inventory[hero][item] = cost
    items = input()

for hero, values in inventory.items():
    print(f"{hero} -> Items: {len(inventory[hero])}, Cost: {sum(inventory[hero].values())}")