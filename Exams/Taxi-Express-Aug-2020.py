from collections import deque

customers = deque([int(el) for el in input().split(", ")])  # time it takes to drive the customer to his/her destination
taxi_vehicles = deque([int(el) for el in input().split(", ")])  # time they can drive, before they need to refill their tanks
total_time = 0      # values of all customers
no_taxi = False

""" put the first customer in the last taxi until there are no customers left """
while True:
    if not taxi_vehicles:
        no_taxi = True
        break
    current_customer = customers[0]
    current_taxi = taxi_vehicles[len(taxi_vehicles)-1]
    if current_taxi >= current_customer:
        total_time += current_customer
        customers.popleft() # removing the customer
        taxi_vehicles.pop() # removing the taxi
    else:
        taxi_vehicles.pop()  # removing the taxi

if customers:
    customers = list(customers)
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
else:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
