def numbers_searching(*args):
    """ finding the duplicates """
    list_a = []
    duplicates = []
    for el in args:
        if el not in list_a:
            list_a.append(el)
        else:
            duplicates.append(el)

    """ finding the missing numbers """
    x = sorted(set(list_a))
    y = set(range(x[0], x[-1]))
    result = y.difference(x)
    duplicates = set(duplicates)

    """ printing """
    final_list = []
    [final_list.append(x) for x in result]
    final_list.append(sorted(list(duplicates)))
    return final_list



print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

