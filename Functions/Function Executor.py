def func_executor(*args):
    values = []
    for func, fargs in args:
       x = func(*fargs)
       values.append(x)
    return values

def sum_numbers(*nums):
    return sum(nums)

def multiply_numbers(*nums):
    res = 1
    for el in nums:
        res *= el
    return res


print(func_executor((sum_numbers, (1, 1, 2, 6)), (multiply_numbers, (2, 4, 2))))
