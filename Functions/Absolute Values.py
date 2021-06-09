def abs_func():
    numbers = [abs(float(el)) for el in input().split()]
    return numbers

print(abs_func())