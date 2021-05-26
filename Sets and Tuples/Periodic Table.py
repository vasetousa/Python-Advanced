n = int(input())
el = set()
for _ in range(n):
    elements = input().split()
    for i in elements:
        el.add(i)

for el in el:
    print(el)
