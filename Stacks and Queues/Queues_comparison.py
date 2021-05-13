from collections import deque
from datetime import datetime


def deque_queue_test():
    q = deque()
    for el in range(1 << 27):
        q.append(el)


def list_queue_test():
    q = []
    for el in range(1 << 27):
        q.append(el)


def measure(action):
    start_time = datetime.now()

    end_time = datetime.now()
    print(f"Finished in: {end_time - start_time}")

print("Deque:")
measure(deque_queue_test())
print("List:")
measure(list_queue_test())
