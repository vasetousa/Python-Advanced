n = int(input())
odd_set = set()
even_set = set()
for _ in range(1, n+1):
    names = input()
    names_len = len(names)
    sum_value = 0
    for l in names:
        value = ord(l)
        sum_value += value
    sum_value //= _
    if sum_value % 2 == 0:
        even_set.add(sum_value)
    else:
        odd_set.add(sum_value)
sum_odd = sum(odd_set)
sum_even = sum(even_set)
if sum_odd == sum_even:
    union = odd_set | even_set
    result = ', '.join(map(lambda y: y, union))
elif sum_odd > sum_even:
    sort = sorted(odd_set)
    listed = list(reversed(sort))
    print(*listed, sep=", ")
elif sum_odd < sum_even:
    sym = odd_set ^ even_set
    print(*sym, sep=", ")

