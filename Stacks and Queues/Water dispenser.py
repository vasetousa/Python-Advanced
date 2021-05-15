from collections import deque
q = deque()
water_quantity = int(input())
names = input()

while not names == "Start":
    q.append(names)
    names = input()

command = input()
while not command == "End":
    if command.startswith("refill"):
        comm, litters = command.split()
        litters = int(litters)
        water_quantity += litters
    else:
        command = int(command)
        if command <= water_quantity:
            print(f"{q.popleft()} got water")
            water_quantity -= command
        else:
            print(f"{q.popleft()} must wait")

    command = input()

print(f"{water_quantity} liters left")
