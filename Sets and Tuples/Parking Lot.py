def input_data_in_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())
    return lines


def print_parking_lot(data):
    if parking_lot:
        for _ in data:
            print(_)
    else:
        print("Parking Lot is Empty")


n = int(input())
cars = input_data_in_list(n)

# cars = [
#         'IN, CA2844AA',
#         'IN, CA1234TA',
#         'OUT, CA2844AA',
#         'IN, CA9999TT',
#         'IN, CA2866HI',
#         'OUT, CA1234TA',
#         'IN, CA2844AA',
#         'OUT, CA2866HI',
#         'IN, CA9876HH',
#         'IN, CA2822UU',
#          ]
parking_lot = set()
for el in cars:
    status, plate = el.split(', ')
    if status == 'IN':
        if plate not in parking_lot:
            parking_lot.add(plate)
    else:
        if plate in parking_lot:
            parking_lot.remove(plate)

print_parking_lot(parking_lot)
