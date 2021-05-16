from collections import deque
from collections import defaultdict
robots = input().split(';')
data_robots = []
for _ in robots:
    name, time = _.split('-')
    data_robots.append((name, time))
start_time, minutes, seconds = input().split(':')
minutes = int(minutes)
seconds = int(seconds)
product = input()
q = deque()

while not product == 'End':
    q.append(product)






    product = input()

print()