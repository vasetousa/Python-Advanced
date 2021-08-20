def fill_the_box(height, length, width, *args):
    from collections import deque
    args = deque(args)
    new_args = []
    box_size = height * length * width
    box = box_size
    for el in args:
        if el == "Finish":
           break
        if el > box:
            rest = el - box
            el = box
            box -= el
            new_args.append(el+rest)
            new_args = set(new_args)
            args = set(args)
            numbers = args - new_args
            x = [a for a in numbers if a != "Finish"]
            x = sum(x) + rest
            break
        new_args.append(el)
        box -= el
    if box > 0:
        return f"There is free space in the box. You could put {box} more cubes."
    return f"No more free space! You have {x} more cubes."





print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))