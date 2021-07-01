def move_the_player(matrix, row1, col1):
    matrix[row1][col1] = "A"
    # pprint(matrix)
    return


def direction_vector(matrix, direction, player):
    row1 = 0
    col1 = 0
    if direction == "right":
        row1 = player[0]
        col1 = player[1] + steps
        if is_move_valid(matrix, row1, col1):
            if not matrix[row1][col1] == 'x':   # check if the new player spot is a target or not
                matrix[player[0]][player[1]] = "."
                player = row1, col1
                move_the_player(matrix, row1, col1)
    elif direction == "left":
        row1 = player[0]
        col1 = player[1] - steps
        if is_move_valid(matrix, row1, col1):
            if not matrix[row1][col1] == 'x':  # check if the new player spot is a target or not
                matrix[player[0]][player[1]] = "."
                player = row1, col1
                move_the_player(matrix, row1, col1)
    elif direction == "up":
        row1 = player[0] - steps
        col1 = player[1]
        if is_move_valid(matrix, row1, col1):
            if not matrix[row1][col1] == 'x':  # check if the new player spot is a target or not
                matrix[player[0]][player[1]] = "."
                player = row1, col1
                move_the_player(matrix, row1, col1)
    elif direction == "down":
        row1 = player[0] + steps
        col1 = player[1]
        if is_move_valid(matrix, row1, col1):
            if not matrix[row1][col1] == 'x':  # check if the new player spot is a target or not
                matrix[player[0]][player[1]] = "."
                player = row1, col1
                move_the_player(matrix, row1, col1)
    return player


def shoot(matrix, direction, player):
    if direction == "left":
        row1, col1 = player
        for r in range(row1, -1, -1):
            bullet = matrix[row1][r]
            if bullet == "x":
                targets.append((col1, r))
                matrix[col1][r] = "."
                break
    elif direction == "right":
        row1, col1 = player
        for r in range(row1, len(matrix)):
            bullet = matrix[row1][r]
            if bullet == "x":
                targets.append((row1, r))
                matrix[row1][r] = "."
                break
    elif direction == "up":
        row1, col1 = player
        for r in range(row1-1, -1, -1):
            bullet = matrix[r][col1]
            if bullet == "x":
                targets.append((r, col1))
                matrix[r][col1] = "."
                break
    elif direction == "down":
        row1, col1 = player
        for r in range(row1, len(matrix)):
            bullet = matrix[r][col1]
            if bullet == "x":
                targets.append((r, col1))
                matrix[r][col1] = "."
                break
    return matrix


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
            if current_position == 'A':
                current_position = (row, col)
                is_found = True
                break
        if is_found:
            break
    return row, col


def find_targets_left(matrix):
    targets_left = []
    for r in range(len(matrix)):
        for c in range(len(matrix)):
            current_spot = matrix[r][c]
            if current_spot == "x":
                targets_left.append((r, c))
    return targets_left


def read_matrix(is_test=False):
    """ sample matrix, use 5 for size """
    if is_test:
        return [
            ['.', '.', '.', '.', '.'],
            ['x', '.', '.', '.', '.'],
            ['.', 'A', '.', '.', '.'],
            ['.', '.', '.', 'x', '.'],
            ['.', 'x', '.', '.', 'x']
              ] # 2, 1 player
    else:
        side = int(input("Input matrix size: "))
        matrix = []
        for r in range(side):
            x = input().split()
            matrix.append(x)

        return matrix


from collections import deque
from pprint import pprint

targets = []
matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
player = find_the_player(matrix)
pprint(matrix)

""" directions mapper """
directions = {
    "up": (-1, 0),  # take -1 and add steps
    "down": (1, 0),  # take 1 and add steps
    "left": (0, -1), # take -1 and add steps
    "right": (0, 1), # take 1 and add steps
             }

target_positions = []
number_of_commands = int(input("How many commands: "))
command = input("Command: ")
for comm in range(1, number_of_commands+1):

    if command.startswith('move'):
        command, direction, steps = command.split()
        steps = int(steps)
        player = direction_vector(matrix, direction, player)

    elif command.startswith('shoot'):
        command, direction = command.split()
        matrix = shoot(matrix, direction, player)
        print(f"Targets hit: {targets}")
    if comm == number_of_commands:
        break
    pprint(matrix)
    print()

    command = input("Command: ")

rest_of_targets = find_targets_left(matrix)
print(f"Targets left: {rest_of_targets}")
if not rest_of_targets:
    print(f"Training completed! All {len(targets)} targets hit.")
    for _ in targets:
        x = list(_)
        print(x)

else:
    print(f"Training not completed! {len(rest_of_targets)} targets left.")
    for _ in targets:
        x = list(_)
        print(x)
pprint(matrix)