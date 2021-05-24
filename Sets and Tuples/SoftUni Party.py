def input_data_in_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines

def print_results(data):
    print(len(data))
    for e in data:
        print(e)

n = int(input())
reservations = input_data_in_list(n)
new_list = set(reservations)
vip = set()
regular = set()
all_guests = set()

guests = input()
while not guests == "END":
    if guests[0].isdigit():
        vip.add(guests)
    else:
        regular.add(guests)
    guests = input()
all_guests = vip | regular
result = sorted(new_list.difference(all_guests))

print_results(result)