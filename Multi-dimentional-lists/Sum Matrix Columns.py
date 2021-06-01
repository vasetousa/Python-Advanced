def read_matrix():
    rows, columns = [int(el) for el in (input().split(", "))]
    matrix = []
    for r in range(rows):
        x = [int(el) for el in (input().split())]
        matrix.append(x)
    return matrix


def sum_columns_matrix(result):
    sums = []
    rows = len(matrix)
    colls = len(matrix[0])
    for i in range(colls):
        col_sum = 0
        for j in range(rows):
            col_sum += matrix[j][i]  # using the indices to iterate
        sums.append(col_sum)
    return sums


def print_results(values):
    [print(x) for x in values]


matrix = read_matrix()
result = sum_columns_matrix(matrix)
print_results(result)
