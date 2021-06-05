def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'B', 'D'],
            ['E', 'B', 'B', 'B'],
            ['I', 'J', 'B', 'B'],
                ]
    else:
        rows, columns = [int(el) for el in (input().split())]
        matrix = []
        for r in range(rows):
            x = [el for el in (input().split(", "))]
            matrix.append(x)
        return matrix

def find_submatrix(matrix):
    size = 2
    for r in range(size):







size = 2
matrix = read_matrix(is_test=True)  # for local testing use matrix = read_matrix(is_test=True)
print(matrix)


# TODO finish the problem later