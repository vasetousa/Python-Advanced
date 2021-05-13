from collections import deque # deque structure

d = deque()
d.append("Hello")
d.append("Man")
d.append("Camera")
print(d)

d.popleft()
print(d)

