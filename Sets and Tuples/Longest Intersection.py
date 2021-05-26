from collections import deque

n = int(input())
intersections = deque()
current_intersection = []
compare = []
r = []


for _ in range(n):
    data_ranges = input().split('-')
    for el in data_ranges:
        start, end = el.split(',')
        start = int(start)
        end = int(end)
        for num in range(start, end+1):
            r.append(num)
        compare.append(r)
        r = []
    if len(compare) > 1:
        com1 = set(compare[0])
        com2 = set(compare[1])
        current_intersection = com1 & com2
        intersections.append(current_intersection)
        current_intersection = []
        compare = []

base = 0
while intersections:
    x = intersections.popleft()
    el_len = len(x)
    if el_len > base:
        base = el_len
        intersections.append(x)

inter = list(x)

print(f"Longest intersection is {inter} with length {base}")