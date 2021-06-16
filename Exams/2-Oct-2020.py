def check_directions(matrix, king):
    queens_row = []
    queens_col = []
    k_row, k_col = king
    matrix_len = len(matrix)

    # check K row
    for i in range(matrix_len):  # 2, 0 --> 2, 7
        current_position = matrix[k_row][i]
        if current_position == "Q":
            queens_row.append((k_row, i))

    # check K column
    for i in range(matrix_len):  # 2, 1 --> 3, 1
        current_position = matrix[i][k_col]
        print(current_position)
        print([k_row], [i])
        if current_position == "Q":
            queens_col.append((i, k_col))

    # check diagonal down
    for i in range(k_row, matrix_len):
        current_position = matrix[i][i-1]
        if current_position == "Q":
            queens_row.append((i, i-1))

    # check other diagonal
    for i in range(matrix_len):  # 2, 1 --> 1, 0
        current_position = matrix[i][-i-1]
        if current_position == "Q":
            queens_row.append((i-1, i-2))

    return queens_row


def find_king(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            current_position = matrix[row][col]
            if current_position == "K":
                king_coordinates = row, col
                return king_coordinates   # King coordinates

# diagonal ->        0,0 1,1 2,2 3,3 4,4 5,5 6,6 7,7
# under main ->      1,0 2,1, 3,2 4,3 5,4 6,5 7,6
# second diagonal -> 0,7 1,6 2,5 3,4 4,3 5,2 6,1 7,0    matrix[i][- i - 1]
# under second ->    1,7 2,6 3,5 4,4 5,3 6,2 7,1
def read_matrix(is_test=False):
    if is_test:
        return [
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['Q', '.', 'V', '.', '.', '.', '.', '.'],
            ['.', 'K', '.', '.', '.', 'Q', '.', '.'],
            ['G', '.', 'A', 'Q', '.', '.', '.', '.'],
            ['Q', '.', '.', '.', 'Q', '.', '.', '.'],
            ['.', 'Q', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'Q', '.'],
            ['.', 'Q', '.', 'Q', '.', '.', '.', '.']
              ]     # 2, 1

    else:
        side = 8
        matrix = []
        for r in range(side):
            x = [el for el in (input().split())]
            matrix.append(x)
        return matrix

from pprint import pprint
matrix = read_matrix(is_test=True)  # for local testing use matrix = read_matrix(is_test=True)
# pprint(matrix)
king_position = find_king(matrix)
# print(king_position)
queens = check_directions(matrix, king_position)
if queens:
    [print(list(el)) for el in queens]
else:
    print("The king is safe!")

    # TODO not finished yet!