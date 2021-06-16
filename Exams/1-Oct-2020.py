cycles = [int(el) for el in input().split(', ')]
task_index = int(input())
from collections import deque

jobs = deque(cycles)
""" First make the job_wanted the first index in the queue """
sum_cycles = 0
for _ in range(task_index):
    current_index = jobs.popleft()
    jobs.append(current_index)
job_wanted = jobs.popleft()
""" find the number of cycles and their sum """
for i in range(len(jobs)):
    current_el = jobs[i]
    if current_el <= job_wanted:
        sum_cycles += current_el

print(sum_cycles + job_wanted)
