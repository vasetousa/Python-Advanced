from collections import deque

q = deque()
s = []
q_list = []
for i in range(1, 6):
    q.append(i)
    s.append(i)
    q_list.append(i)

print("Queue:")
while q:
    print(q.popleft())

print("Queue as list:")
while q_list:
    print(q_list.pop(0))

print("Stack:")
while s:
    print(s.pop())


