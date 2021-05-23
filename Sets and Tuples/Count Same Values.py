string = tuple([float(el) for el in input().split()])
dicting = {}

for value in string:
    dicting[value] = string.count(value)

for key, value in dicting.items():
    print(f"{key} - {value} times")