data = input().split()
stack = []

for el in data:
    stack.append(el[-1])
    stack.pop(el)

print()
