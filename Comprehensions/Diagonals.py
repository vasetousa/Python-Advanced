def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
    else:
        side = int(input())
        matrix = []
        for r in range(side):
            matrix.append([int(x) for x in input().split(', ')])
        return matrix


def find_first_diagonal_and_sum(matrix):
    the_sum = 0
    diagonal_numbers = []
    for r in range(len(matrix)):
        the_sum += matrix[r][r]
        diagonal_numbers.append(matrix[r][r])
    return diagonal_numbers, the_sum


def find_second_diagonal_and_sum(matrix):
    the_sum_2 = 0
    diagonal_numbers_2 = []
    for r in range(len(matrix)):
        the_sum_2 += matrix[r][-r - 1]
        diagonal_numbers_2.append(matrix[r][-r - 1])
    return diagonal_numbers_2, the_sum_2


matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
numbers_1, sum_1 = find_first_diagonal_and_sum(matrix)
numbers_2, sum_2 = find_second_diagonal_and_sum(matrix)

print(f'First diagonal: {", ".join(str(el) for el in numbers_1)}. Sum: {sum_1}')
print(f'Second diagonal: {", ".join(str(el) for el in numbers_2)}. Sum: {sum_2}')
