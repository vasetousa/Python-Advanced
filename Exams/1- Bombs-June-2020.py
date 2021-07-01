def materials_table(value):
    bomb_was_made = False
    if value == 40:
        bombs["Datura Bombs"] += 1
        bomb_was_made = True
    elif value == 60:
        bombs["Cherry Bombs"] += 1
        bomb_was_made = True
    elif value == 120:
        bombs["Smoke Decoy Bombs"] += 1
        bomb_was_made = True
    return bomb_was_made


from collections import deque
bombs = {"Datura Bombs": 0, "Cherry Bombs": 0, "Smoke Decoy Bombs": 0}
effects = deque([int(el) for el in input().split(", ")])  #
bomb_casings = deque([int(el) for el in input().split(", ")])  #
full_pouch = False

while True:
    if bombs["Datura Bombs"] >= 3 and bombs["Cherry Bombs"] >= 3 and bombs["Smoke Decoy Bombs"] >= 3:
        full_pouch = True
        break
    elif not bomb_casings:
        break
    elif not effects:
        break
    current_effect = effects[0]
    current_bomb = bomb_casings[len(bomb_casings)-1]
    suma = current_effect + current_bomb
    result = materials_table(suma)
    if not result:
        current_bomb -= 5
        bomb_casings[len(bomb_casings)-1] = current_bomb
    else:
        effects.popleft()
        bomb_casings.pop()
print()
if full_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not effects:
    print("Bomb Effects: empty")
else:
    effects_left = list(effects)
    print(f"Bomb Effects: ", end=''), print(*effects_left, sep=', ')

if not bomb_casings:
    print("Bomb Casings: empty")
else:
    bomb_casings_left = list(bomb_casings)
    print(f"Bomb Casings: ", end=''), print(*bomb_casings_left, sep=', ')
for key, value in sorted(bombs.items()):
    print(f"{key}: {value}")
