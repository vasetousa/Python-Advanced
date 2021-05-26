n, m = [int(el) for el in input().split()]
n_set = set()
m_set = set()


for _ in range(1, (n+m)+1):
    number = int(input())
    if _ <= n:
        n_set.add(number)
    else:
        m_set.add(number)

union = (n_set & m_set)
for _ in union:
    print(_)
