clothes = [int(el) for el in input().split()]
rack_capacity = int(input())
rack = []
rack_counter = 0
current_add = 0

while clothes:
    current_cloth = clothes.pop()
    current_add += current_cloth
    if current_add == rack_capacity:
        rack.append(current_add)
        current_add = 0
        rack_counter += 1
    elif current_add > rack_capacity:
        current_add -= current_cloth
        rack.append(current_add)
        clothes.append(current_cloth)
        current_add = 0
        rack_counter += 1
    if not clothes:
        if not current_add == 0:
            rack.append(current_add)
            rack_counter += 1
            current_add = 0

print(rack_counter)

