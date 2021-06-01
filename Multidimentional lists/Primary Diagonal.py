# def read_matrix(side):
#     matrix = []
#     for r in range(side):
#         x = [int(el) for el in (input().split())]
#         matrix.append(x)
#     return matrix
#
#
# def sum_diagonal_matrix():
#     sums = []
#     diagonal_sum = 0
#     for i in range(size):
#         diagonal_sum += matrix[i][i] # using the indices to iterate
#         sums.append(diagonal_sum)
#     return diagonal_sum
#
#
# size = int(input())
# matrix = read_matrix(size)
# result = sum_diagonal_matrix()
# print(result)


matrix = [
    [1, 1, 3, 5, 6, 6],
    [7, 8, 9, 10, 1, 3],
    [8, 7, 2, 3, 1, 7],
    [5, 3, 2, 8, 4, 3],
    [2, 8, 8, 7, 1, 3],
    [8, 9, 1, 1, 2, 3],
]

def calculate_primary_diagonal_sum(matrix):
    primary_diagonal_sum = 0

    for i in range(len(matrix)):
        primary_diagonal_sum += matrix[i][i]
    return primary_diagonal_sum


def calculate_secondary_diagonal_sum(matrix):
    secondary_diagonal_sum = 0
    n = len(matrix)

    for i in range(n):
        secondary_diagonal_sum += matrix[i][- i - 1]
    return secondary_diagonal_sum

def calculate_below_primary_diagonal_sum(matrix):
    n = len(matrix)
    the_sum = 0
    for row in range(n):
        for col in range(row + 1):
            the_sum += matrix[row][col]
    return the_sum

def calculate_below_secondary_diagonal_sum(matrix):
    n = len(matrix)
    the_sum = 0
    for row in range(n):
        for col in range(n - row - 1, n):
            the_sum += matrix[row][col]
    return the_sum

print(calculate_primary_diagonal_sum(matrix))
print(calculate_secondary_diagonal_sum(matrix))
print(calculate_below_primary_diagonal_sum(matrix))
print(calculate_below_secondary_diagonal_sum(matrix))