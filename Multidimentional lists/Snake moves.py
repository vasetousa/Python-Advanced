rows, cols = [int(el) for el in input().split()]
string = input()
index_string = 0
matrix = []

for r in range(rows):
    matrix.append([0 for el in range(cols)])

for row_index in range(rows):
    for col_index in range(cols):
        matrix[row_index][col_index] = string[index_string]
        index_string += 1
        if index_string == len(string):
            index_string = 0

for r in range(rows):
    if r % 2 == 1:
        matrix[r].reverse()
    print(''.join(matrix[r]))
