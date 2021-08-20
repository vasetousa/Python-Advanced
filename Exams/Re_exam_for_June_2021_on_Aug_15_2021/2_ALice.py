def read_matrix(side, is_test=False):
    if is_test:
        return [
            ['.', 'A', '.', '.', '1'],
            ['R', '.', '2', '.', '.'],
            ['4', '7', '.', '1', '.'],
            ['.', '.', '.', '2', '.'],
            ['.', '3', '.', '.', '.'],
        ]
    else:
        """ read the matrix from input """
        matrix = []
        for r in range(side):
            x = [ch for ch in input().split(" ")]
            matrix.append(x)
        return matrix

def find_player(matrix):
    is_found = False
    current_position = None
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            current_position = matrix[row][col]
            if current_position == 'A':
                current_position = row, col
                is_found = True
                break
        if is_found:
            break
    return current_position


def rabbit_hole(matrix):
    is_found = False
    current_position = None
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            current_position = matrix[row][col]
            if current_position == 'R':
                current_position = row, col
                is_found = True
                break
        if is_found:
            break
    return current_position


def directions(command):
    """ directions mapper """
    directions = {
        "up":       (-1, 0),
        "down":      (1, 0),
        "left":     (0, -1),
        "right":     (0, 1),
                }
    next_stop = directions[command]
    return next_stop


def is_move_valid(row1, col1, size):
    if not row1 in range(0, size) or not col1 in range(0, size):
        return False
    return True

# def print_matrix(matrix):
#     print()
#     for el in matrix:
#         count = 1
#         for char in el:
#             print(char, end=" ")
#             if count == side:
#                 print()
#             count += 1
#     print("*" * 25)

ALICE = "A"
RABBIT_HOLE = "R"
EMPTY = "*"
tea_quantity = 0

side = int(input())
matrix = read_matrix(side, is_test=False)  # for local testing use matrix = read_matrix(is_test=True)
alice = find_player(matrix)
rabbit_hole = rabbit_hole(matrix)
current_spot = alice
current_r, current_c = alice # start position
current_spot = alice

while True:
    alice_direction = input()
    next_row, next_col = directions(alice_direction)
    alice_next_move_r, alice_next_move_c = current_r + next_row, current_c + next_col   # next spot to move "A"

    if not is_move_valid(alice_next_move_r, alice_next_move_c, side):
        matrix[current_r][current_c] = EMPTY
        print("Alice didn't make it to the tea party.")
        break

    elif matrix[alice_next_move_r][alice_next_move_c] == RABBIT_HOLE:
        matrix[alice_next_move_r][alice_next_move_c] = EMPTY
        matrix[current_r][current_c] = EMPTY
        print("Alice didn't make it to the tea party.")
        break

    elif matrix[alice_next_move_r][alice_next_move_c].isdigit():
        spot_value = matrix[alice_next_move_r][alice_next_move_c]
        spot_value = int(spot_value)
        tea_quantity += spot_value
        matrix[alice_next_move_r][alice_next_move_c] = ALICE
        matrix[current_r][current_c] = EMPTY
        current_r, current_c = alice_next_move_r, alice_next_move_c

    elif matrix[alice_next_move_r][alice_next_move_c] == "*":
        matrix[alice_next_move_r][alice_next_move_c] = ALICE
        matrix[current_r][current_c] = EMPTY
        current_r, current_c = alice_next_move_r, alice_next_move_c

    elif matrix[alice_next_move_r][alice_next_move_c] == ".":
        matrix[alice_next_move_r][alice_next_move_c] = ALICE
        matrix[current_r][current_c] = EMPTY
        current_r, current_c = alice_next_move_r, alice_next_move_c

    if tea_quantity >= 10:
        print("She did it! She went to the party.")
        matrix[alice_next_move_r][alice_next_move_c] = EMPTY
        break

    # print_matrix(matrix)

for el in matrix:
    count = 1
    for char in el:
        print(char, end=" ")
        if count == side:
            print()
        count += 1