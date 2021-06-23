def is_move_valid(row1, col1, size):
    if not row1 in range(0, size) or not col1 in range(0, size):
        return False
    return True


def check_directions(matrix, king, side):
    """ directions mapper """
    directions = {
        "up":       (-1, 0),
        "down":      (1, 0),
        "left":     (0, -1),
        "right":     (0, 1),
        "upLeft":  (-1, -1),
        "downRight": (1, 1),
        "upRight":  (-1, 1),
        "downLeft": (1, -1)
                }

    queens = []
    k_row, k_col = king
    matrix_len = len(matrix)
    for direction in directions:
        next_row = k_row + directions[direction][0]
        next_col = k_col + directions[direction][1]
        while is_move_valid(next_row, next_col, size):
            if matrix[next_row][next_col] == "Q":
                queens.append((next_row, next_col))
                break
            next_row += directions[direction][0]
            next_col += directions[direction][1]
    return queens


def find_king(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            current_position = matrix[row][col]
            if current_position == "K":
                king_coordinates = row, col
                return king_coordinates   # King coordinates

# second diagonal ->     matrix[i][- i - 1]

def read_matrix(is_test=False):
    if is_test:
        return [
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['Q', '.', '.', '.', '.', '.', '.', '.'],
            ['.', 'K', '.', '.', '.', 'Q', '.', '.'],
            ['.', '.', '.', 'Q', '.', '.', '.', '.'],
            ['Q', '.', '.', '.', 'Q', '.', '.', '.'],
            ['.', 'Q', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'Q', '.'],
            ['.', 'Q', '.', 'Q', '.', '.', '.', '.']
              ]     # 2, 1 King
    else:
        """ read the matrix from input """
        side = 8
        matrix = []
        for r in range(side):
            x = [el for el in (input().split())]
            matrix.append(x)
        return matrix


matrix = read_matrix(is_test=True)  # for local testing use matrix = read_matrix(is_test=True)
size = 8
king_position = find_king(matrix)
queens = check_directions(matrix, king_position, size)
if queens:
    [print(list(el)) for el in queens]
else:
    print("The king is safe!")
