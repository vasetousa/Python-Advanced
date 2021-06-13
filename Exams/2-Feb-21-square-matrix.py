def is_new_position_valid(matrix, row, col):
    if r not in range(len(matrix)) or c not in range(len(matrix)):
        return False
    return True


def find_player(matrix):
    is_found = False
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            current_position = matrix[row][col]
            if current_position == 'P':
                current_position = row, col
                is_found = True
                break
        if is_found:
            break
    return row, col


def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 'X', 7, 9, 11],
            ['X', 14, 46, 62, 0],
            [15, 33, 21, 95, 'X'],
            ['P', 14, 3, 4, 18],
            [9, 20, 33, 'X', 0]

        ]

    else:
        side = int(input())
        matrix = []
        for r in range(side):
            x = [el for el in (input().split())]
            matrix.append(x)
        return matrix


""" P marks the Player, X marks a wall """
from math import floor
player_moves = []
coins = 0
matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
player_place = find_player(matrix)  # tuple with player coordinates
r, c = player_place

while coins < 100:
    command = input()
    if command == 'up':
        r -= 1
        if r not in range(len(matrix)):
            break
        new_position = matrix[r][c]
        result = is_new_position_valid(matrix, r, c)
        if not result:  # game over
            break
        if new_position == 'X':  # game over
            break
        new_position = int(new_position)
        coins += new_position
        current_place = r, c
        player_moves.append(current_place)
    elif command == 'down':
        r += 1
        if r not in range(len(matrix)):
            break
        new_position = matrix[r][c]
        result = is_new_position_valid(matrix, r, c)
        if not result:  # game over
            break
        if new_position == 'X':  # game over
            break
        new_position = int(new_position)
        coins += new_position
        current_place = r, c
        player_moves.append(current_place)
    elif command == 'left':
        c -= 1
        if c not in range(len(matrix)):
            break
        new_position = matrix[r][c]
        result = is_new_position_valid(matrix, r, c)
        if not result:  # game over
            break
        if new_position == 'X':  # game over
            break
        new_position = int(new_position)
        coins += new_position
        current_place = r, c
        player_moves.append(current_place)
    elif command == 'right':
        c += 1
        if c not in range(len(matrix)):
            break
        new_position = matrix[r][c]
        result = is_new_position_valid(matrix, r, c)
        if not result:  # game over
            break
        if new_position == 'X':  # game over
            break
        new_position = int(new_position)
        coins += new_position
        current_place = r, c
        player_moves.append(current_place)
if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    coins *= 0.5
    print(f"Game over! You've collected {floor(coins)} coins.")
print("Your path:")
for el in player_moves:
    x, y = el
    print(f"[{x}, {y}]")