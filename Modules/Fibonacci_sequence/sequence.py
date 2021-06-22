def create_sequence(n):
    if n == 0:
        print(0)
        return
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i-2] + sequence[i - 1])
    print(' '.join([str(x) for x in sequence]))


def locate(number):
    x, y = 0, 1

    while x < number:
        x, y = y, x + y
    if x == number:
        print('Found')
    else:
        print('Not found')