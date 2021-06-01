def read_matrix(side):
    matrix = []
    for r in range(side):
        x = [x for x in input()]
        matrix.append(x)

    return matrix


def find_symbol(matrix, symbol):
    for el in range(len(matrix)):
        for ch in range(len(matrix[el])):
            current_symbol = matrix[el][ch]
            if current_symbol == symbol:
                return el, ch
    return


size = int(input())

matrix = read_matrix(size)
symbol = input()
result = find_symbol(matrix, symbol)
if result:
    print(result)
else:
    print(f"{symbol} does not occur in the matrix")
