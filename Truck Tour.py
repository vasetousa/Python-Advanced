from collections import deque
pumps = int(input())
gas_stations = []
index = deque(gas_stations)
tank = 0
counter = 0
valid = True
for t in range(pumps):
    index.append(input())


for el in range(pumps):
    for _ in index:
        petrol, distance = _.split()   # liters of petrol from this pump
        petrol = int(petrol)     # from this pump to the next in km
        distance = int(distance)     # from this pump to the next in km
        tank += petrol
        if tank >= distance:
            tank -= distance
            counter += 1
        elif tank < distance:
            tank_capacity = 0
            index.rotate(-1)  # current station goes last, next station becomes 1st later
            valid = False
            counter = 0
            tank = 0
            break
        if counter == len(index):
            valid = True
            break
    if valid:
        print(el)
        break
    else:
        valid = True

# 5
# 5 5
# 10 9
# 1 4
# 6 2
# 8 3