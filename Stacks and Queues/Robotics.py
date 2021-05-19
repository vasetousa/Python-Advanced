from collections import deque

from datetime import datetime, timedelta

data = input().split(';')
time_now = datetime.strptime(input(), '%H:%M:%S')

robots = []
available_robots = deque([])
for _ in data:
    name, time = _.split('-')
    time = int(time)
    robot = {}
    robot['name'] = name
    robot['processing_time'] = time
    robot['available_at'] = time_now
    robots.append(robot)
    available_robots.append(robot)

product = input()
q = deque([])

while not product == 'End':
    q.append(product)
    product = input()

time_now = time_now + timedelta(seconds=1)
while product:
    current_product = q.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time_now + timedelta(seconds=current_robot['processing_time'])
    else:
        for r in robots:
            if time_now >= r['available_at']:
                available_robots.append(r)

print()