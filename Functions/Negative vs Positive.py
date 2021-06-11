numbers = [int(el) for el in input().split()]


def is_positive(values):
    negative = []
    positive = []
    for i in values:
        if i > 0:
            positive.append(i)
        else:
            negative.append(i)
    return positive, negative


po, ne = (is_positive(numbers))
po_sum = sum(po)
ne_sum = sum(ne)
print(ne_sum)
print(po_sum)
if abs(ne_sum) > po_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
