def math_operations(*args, **kwargs):
    from collections import deque
    numbers = []
    for el in args:
        numbers.append(el)
    numbers = deque(numbers)
    while numbers:
        for x in kwargs:
            if numbers:
                first_num = numbers.popleft()
                if x == 'a':
                    kwargs[x] += first_num
                elif x == 's':
                    kwargs[x] -= first_num
                elif x == 'd':
                    if not first_num == 0:
                        kwargs[x] /= first_num
                elif x == 'm':
                    kwargs[x] *= first_num
    return kwargs




print(math_operations(2, 12, 0, -3, 6, -20, -11, a=1, s=7, d=33, m=15))
print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))