def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 5, 5, 2,  4],
            [2, 1, 4, 14, 3],
            [3, 7, 11, 2,  8],
            [4, 8, 12, 16, 4],
                ]
    else:
        rows, columns = [int(el) for el in (input().split())]
        matrix = []
        for r in range(rows):
            x = [el for el in (input().split())]
            matrix.append(x)
        # pprint(matrix)
        return matrix

def find_submatrix_largest_sum(matrix, submatrix_row, submatrix_col, size):
    the_sum = 0
    for r in range(submatrix_row, submatrix_row + size):
        for c in range(submatrix_col, submatrix_col + size):
            the_sum += matrix[r][c]
    return the_sum

def get_best_submatrix_sum_coordinates(matrix, submatrix_size):
    best_row_index = 0
    best_column_index = 0
    best_sum = find_submatrix_largest_sum(matrix, 0, 0, submatrix_size)

    for row_index in range(len(matrix) - submatrix_size + 1):
        for col_index in range(len(matrix[row_index]) - submatrix_size + 1):
            current_sum = find_submatrix_largest_sum(matrix, row_index, col_index, submatrix_size)
            if best_sum < current_sum:
                best_sum = current_sum
                best_row_index = row_index
                best_column_index = col_index
    return (best_row_index, best_column_index)

submatrix_size = 3
matrix = read_matrix(is_test=True)  # for local testing use matrix = read_matrix(is_test=True)
print(find_submatrix_largest_sum(matrix, 0, 0, 3))
