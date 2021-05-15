from collections import deque
names = deque()

name = input()
while not name == "End":
    if name == 'Paid':
        print('\n'.join(names))
        names.clear()
    else:
        names.append(name)
    name = input()

print(f"{len(names)} people remaining.")
