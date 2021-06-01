def read_matrix(row, col):
    total_sum = 0
    for r in range(row):
        x = [int(el) for el in (input().split(", "))]
        matrix.append(x)
    return matrix

def sum_matrix(result):
    total_sum = 0
    for i in result:
        for j in i:
            total_sum += j
    return total_sum


matrix = []

row, col = [int(el) for el in (input().split(", "))]


result = read_matrix(row, col)
sum_matrix_el = sum_matrix(result)
print(sum_matrix_el)
print(result)