from collections import deque
from datetime import datetime, timedelta

data = input().split(';')
time_now = datetime.strptime(input(), '%H:%M:%S')

robots = []
available_robots = deque([])
for _ in data:
    name, time = _.split('-')
    time = int(time)
    robot = {'name': name, 'processing_time': time, 'available_at': time_now}
    robots.append(robot)
    available_robots.append(robot)

product = input()
q = deque([])

while not product == 'End':
    q.append(product)
    product = input()

time_now = time_now + timedelta(seconds=1)
while q:
    current_product = q.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        current_robot['available_at'] = time_now + timedelta(seconds=current_robot['processing_time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['available_at'] = time_now + timedelta(seconds=current_robot['processing_time'])
        print(f"{robot['name']} - {current_product} [{time_now.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time_now >= r['available_at']:
                available_robots.append(r)
        if not available_robots:
            q.append(current_product)
        else:
            current_robot = available_robots.popleft()
            current_robot['available_at'] = time_now + timedelta(seconds=current_robot['processing_time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['available_at'] = time_now + timedelta(seconds=current_robot['processing_time'])
            print(f"{robot['name']} - {current_product} [{time_now.strftime('%H:%M:%S')}]")
    time_now = time_now + timedelta(seconds=1)
