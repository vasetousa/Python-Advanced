def read_matrix(is_test=False):
    if is_test:
        return [
            [7, 1, 3, 3, 2, 1],
            [1, 3, 9, 8, 5, 6],
            [4, 6, 7, 9, 1, 0],
        ]
    else:
        rows, columns = [int(el) for el in (input().split(", "))]
        matrix = []
        for r in range(rows):
            x = [int(el) for el in (input().split(", "))]
            matrix.append(x)
        return matrix


def find_submatrix(matrix, row_index, column_index, size):
    the_sum = 0
    for r in range(row_index, row_index + size):
        for c in range(column_index, column_index + size):
            the_sum += matrix[r][c]
    return the_sum


def get_best_submatrix_sum_coordinates(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = find_submatrix(matrix, 0, 0, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = find_submatrix(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index
    return (best_row_index, best_column_index)


def print_result(coordinates, size):
    (row_index, col_index) = coordinates
    for r in range(row_index, row_index + size):
        row = []
        for c in range(col_index, col_index + size):
            row.append(matrix[r][c])
        print(" ".join(str(x) for x in row))   # reverse the ints to strings to be able to .join()
    print(find_submatrix(matrix, row_index, col_index, size))   # prints the sum of the submatrix


matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
SUBMATRIX_SIZE = 3
coordinates = get_best_submatrix_sum_coordinates(matrix, SUBMATRIX_SIZE)
print_result(coordinates, SUBMATRIX_SIZE)
