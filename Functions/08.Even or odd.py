def even_odd(*args):
    command = args[(len(args) - 1)]
    args = list(args)
    args.pop()
    odd = []
    even = []
    if command == "even":
        for x in args:
            if x % 2 == 0:
              even.append(x)
        return even
    else:
        for x in args:
            if x % 2 == 1:
              odd.append(x)
        return odd

print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))


# def even_odd(x):
#   if x % 2 == 1:
#     return False
#   else:
#     return True
#
# status = filter(even_odd, args)


#
# for x in status:
#   print(x)

