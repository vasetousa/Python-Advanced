def make_matrix(size, is_test=False):
    if is_test:
        """ matrix before the bombs are placed """
        matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
              ]
        return matrix
    else:
        matrix = []
        for r in range(size):
            x = [el for el in ([0] * size)]
            matrix.append(x)
        return matrix


def calculate_numbers_around_bombs(matrix):
    """ add 1 to the cells around the bomb """
    size = len(matrix)
    for row in range(size):
        for col in range(size):
            current_position = matrix[row][col]
            if current_position == "*":
                mapper(matrix, row, col)
    return matrix


def mapper(matrix, row, col):
    """ directions mapper """
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
        "upLeft": (-1, -1),
        "downRight": (1, 1),
        "upRight": (-1, 1),
        "downLeft": (1, -1)
    }
    size = len(matrix)
    for direction in directions:
        next_row = row + directions[direction][0]
        next_col = col + directions[direction][1]

        """ redirect to check if the move goes out the matrix """
        if is_move_valid(next_row, next_col, size):
            if not matrix[next_row][next_col] == "*":
                matrix[next_row][next_col] += 1
            next_row += directions[direction][0]
            next_col += directions[direction][1]


def is_move_valid(row1, col1, size):
    """ check if the direction will not go out of the matrix """
    if not row1 in range(0, size) or not col1 in range(0, size):
        return False
    return True


bomb_list = []
side = int(input()) # matrix size
matrix = make_matrix(side)  # for local testing use matrix = read_matrix(is_test=True), input side = 5

bombs = int(input())    # number of bombs
for _ in range(bombs):
    try:
        bomb_position_coordinates = input()  # tuple of 2 numbers as a string
        pos1 = int(bomb_position_coordinates[1])
        pos2 = int(bomb_position_coordinates[4])
        bomb_list.append((pos1, pos2))
    except ValueError:
        # print("Invalid bomb coordinates")
        continue
    if is_move_valid(pos1, pos2, side):
        matrix[pos1][pos2] = "*"

calculate_numbers_around_bombs(matrix)
for el in matrix:
    print(*el)