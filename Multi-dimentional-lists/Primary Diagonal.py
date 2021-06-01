def read_matrix(side):
    matrix = []
    for r in range(side):
        x = [int(el) for el in (input().split())]
        matrix.append(x)
    return matrix


def sum_diagonal_matrix():
    sums = []
    diagonal_sum = 0
    for i in range(size):
        diagonal_sum += matrix[i][i] # using the indices to iterate
        sums.append(diagonal_sum)
    return diagonal_sum


size = int(input())
matrix = read_matrix(size)
result = sum_diagonal_matrix()
print(result)