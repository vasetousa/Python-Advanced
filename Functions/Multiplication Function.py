def multiply(*args):
    result = 1
    for i in args:
        result *= i
    return result

print(multiply(1, 4, 5))
print(multiply(4, 5, 6, 1, 3))
print(multiply(2, 5, 1000, 5000))