def read_matrix(is_test=False):
    if is_test:
        return [
            [0, 'K', 0, 'K', 0],
            ['K', 0, 0, 0, 'K'],
            [0, 0, 'K', 0, 0  ],
            ['K', 0, 0, 0, 'K'],
            [0, 'K', 0, 'K', 0],
        ]
    else:
        matrix_size = int(input())
        matrix = []
        for r in range(matrix_size):
            x = [el for el in list(input())]
            matrix.append(x)
        return matrix

from pprint import pprint
matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
pprint(matrix)
