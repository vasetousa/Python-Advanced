n = int(input())    # number of actions
stack = []

for _ in range(n):
    action = input()
    if action.startswith('1'):
        comm, num = action.split()
        num = int(num)
        stack.append(num)
    elif action == '2':
        if stack:
            stack.pop()
    elif action == '3':
        if stack:
            print(max(stack))
    elif action == '4':
        if stack:
            print(min(stack))
reversed_stack = reversed(stack)
print(*reversed_stack, sep=', ')