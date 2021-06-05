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
            x = [el for el in (input().split())]
            matrix.append(x)
        # pprint(matrix)
        return matrix


def find_submatrix(matrix, current_row, current_col):
    first = matrix[current_row][current_col]
    right_from_first = matrix[current_row][current_col + 1]
    under_first = matrix[current_row + 1][current_col]
    under_first_and_right = matrix[current_row + 1][current_col + 1]
    if first == right_from_first == under_first == under_first_and_right:
        return True
    return False


counter = 0
size = 2
matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)

for row_ in range(len(matrix)-1):
    le = len(matrix[0])-1
    for col_ in range(le):
        if find_submatrix(matrix, row_, col_):
            counter += 1
print(counter)

