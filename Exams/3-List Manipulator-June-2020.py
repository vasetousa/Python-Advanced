def list_manipulator(list_a, add_remove, beginning_end, *args):
    from collections import deque
    args_len = len(args)
    if add_remove == 'add':
        if beginning_end == 'beginning':
            index = 0
            for i in args:
                list_a.insert(index, i)
                index += 1
            return list_a
        else:
            for i in args:
                list_a.append(i)
            return list_a
    elif add_remove == 'remove':
        if beginning_end == 'beginning':
            if args_len > 0:
                list_a = deque(list_a)
                number = args[0]
                for _ in range(number):
                    list_a.popleft()
                return list(list_a)
            else:
                list_a = deque(list_a)
                list_a.popleft()
                return list(list_a)
        else:
            if args_len > 0:
                number = args[0]
                for _ in range(number):
                    list_a.pop()

                return list_a
            else:
                list_a.pop()
    return list_a






print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))



