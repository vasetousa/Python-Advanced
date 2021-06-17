import os
width = 2
with open("table.txt", 'a') as table_file:

    for el in range(1, 13):
        result = el * 2
        if 1 <= el < 10:
            print(f"{str(el).rjust(width)} times 2 is {result}", file=table_file)
        else:
            print(f"{el} times 2 is {result}", file=table_file)
    print('_' * 20, file=table_file)
