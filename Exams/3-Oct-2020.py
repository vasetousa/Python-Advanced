def best_list_pureness(*numbers):
    l = list(numbers[0])
    k = numbers[1]
    pureness = []
    current_suma = 0

    """ first sum is with the current list"""
    if k == 0:
        for i in enumerate(l):
            multiplication = i[0] * i[1]
            current_suma += multiplication
        return f"Best pureness {current_suma} after {0} rotations"

    for _ in range(k+1):
        current_suma = 0
        """ summing the (numbers * indices) """
        for i in enumerate(l):
            multiplication = i[0] * i[1]
            current_suma += multiplication

        current_number = l.pop()
        l.insert(0, current_number)
        pureness.append(current_suma)

    """ find the highest number and its index (or number of rotations) """
    if pureness:
        best_pureness = max(pureness)
        rotations = pureness.index(best_pureness)
        return f"Best pureness {best_pureness} after {rotations} rotations"




test = ([4, 3, 2, 6], 4)
# test = ([7, 9, 2, 5, 3, 4], 3)
# test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)

