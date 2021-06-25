def flights(*args):
    flight_data = {}
    for el in range(0, len(args)-1, 2):
        if args[el] == "Finish":
            break
        if args[el] not in flight_data:
            flight_data[args[el]] = args[el+1]
        else:
            flight_data[args[el]] += args[el+1]
    return flight_data


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))