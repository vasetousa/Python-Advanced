def is_move_valid(matrix, row1, col1):
    if not row1 in range(0, len(matrix)) or not col1 in range(0, len(matrix)):
        return False
    return True


def find_the_player(matrix):
    global current_position
    is_found = False
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            current_position = matrix[row][col]
            if current_position == 'P':
                current_position = (row, col)
                is_found = True
                break
        if is_found:
            break
    return current_position


def read_matrix(is_test=False):
    if is_test:
        return [
            ['P', '-', '-', '-'],
            ['M', 'a', 'r', 'k'],
            ['-', 'l', '-', 'y'],
            ['-', '-', 'e', '-'],
                ]
    else:
        side = int(input())
        matrix = []
        for el in range(side):
            str = list(input())
            matrix.append(str)
        return matrix

""" directions mapper """
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
             }

from collections import deque

string = input()    # initial string
string = deque(string)
matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
player = (find_the_player(matrix))  #  ***

M = int(input())    # a number
for move in range(M):
    directions_command = input()
    current_position_row = player[0]
    current_position_col = player[1]
    new_position_row = player[0] + directions[directions_command][0]
    new_position_col = player[1] + directions[directions_command][1]
    if is_move_valid(matrix, new_position_row, new_position_col):
        player = new_position_row, new_position_col                   # ***
        matrix[current_position_row][current_position_col] = "-"
        new_position = matrix[new_position_row][new_position_col]   # ***
        if not new_position == "-":
            string += new_position
            matrix[new_position_row][new_position_col] = 'P'
        else:
            matrix[new_position_row][new_position_col] = 'P'
    else:   # if move is invalid, player stays in old position
        new_position_row = player[0]
        new_position_col = player[1]
        if string:
            string.pop()

string = list(string)
print(''.join(string))

for el in matrix:
    for v in enumerate(el):
        print(v[1].strip(''), end='')
        if v[0] == len(el)-1:
            print()
