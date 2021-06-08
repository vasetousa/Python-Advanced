numbers = [int(el) for el in input().split(', ')]

# positive = [el for el in numbers if el >= 0]
# negative = [el for el in numbers if el < 0]
# odd = [el for el in numbers if el % 2 == 1]
# even = [el for el in numbers if el % 2 == 0]

print(f'Positive: {", ".join([str(el) for el in numbers if el >= 0])}')
print(f'Negative: {", ".join([str(el) for el in numbers if el < 0])}')
print(f'Even: {", ".join([str(el) for el in numbers if el % 2 == 0])}')
print(f'Odd: {", ".join([str(el) for el in numbers if el % 2 == 1])}')
