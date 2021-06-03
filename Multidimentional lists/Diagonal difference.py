def read_matrix(is_test=False):
    if is_test:
        return [
            [11, 2, 4],
            [4, 5, 6],
            [10, 8, -12],
            ]
    else:
        size = int(input())
        matrix = []
        for r in range(size):
            x = [int(el) for el in (input().split())]
            matrix.append(x)
        return matrix

def sum_prime_diagonal(matrix):
    sum_prime = 0
    for el in range(len(matrix)):
        sum_prime += matrix[el][el]
    return sum_prime


def sum_secondary_diagonal(matrix):
    sum_second = 0
    for el in range(len(matrix)):
        sum_second += matrix[el][-el-1]
    return sum_second


matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
sum_pr = sum_prime_diagonal(matrix)
sum_sec = sum_secondary_diagonal(matrix)
print(abs(sum_sec-sum_pr))
