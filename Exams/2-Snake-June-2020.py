def read_matrix(side, is_test=False):
    if is_test:
        return [
            ['-', '-', '-', '-', '-', 'S'],
            ['-', '-', '-', '-', 'B', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-'],
            ['-', '-', 'B', '-', '-', '-'],
            ['-', '-', '*', '-', '-', '-'],

        ]
    else:
        """ read the matrix from input """
        matrix = []
        for r in range(side):
            x = [ch for ch in input()]
            matrix.append(x)
        return matrix


def find_snake_burrows_food(matrix):
    burrow_spots = []
    food_spots = []
    snake_coordinates = (0, 0)
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            current_position = matrix[row][col]
            if current_position == SNAKE:
                snake_coordinates = row, col
            elif current_position == BURROW:
                burrow_spots.append((row, col))
            elif current_position == FOOD:
                food_spots.append((row, col))
    return snake_coordinates, burrow_spots, food_spots


def is_move_valid(row1, col1, size):
    if not row1 in range(0, size) or not col1 in range(0, size):
        return False
    return True


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



SNAKE = "S"
BURROW = "B"
FOOD = "*"
EMPTY = "."
food_quantity = 0

side = int(input())
matrix = read_matrix(side, is_test=False)  # for local testing use matrix = read_matrix(is_test=True)
snake, burrows, food = find_snake_burrows_food(matrix)
current_r, current_c = snake # 1
current_spot = snake

while True:
    snake_direction = input()
    next_row, next_col = directions(snake_direction)
    snake_next_move_r,  snake_next_move_c = current_r + next_row, current_c + next_col   # next spot to move "S"
    # matrix[current_r][current_c] = EMPTY    # starting point for "S"  1
    if not is_move_valid(snake_next_move_r, snake_next_move_c, side):
        matrix[current_r][current_c] = EMPTY
        print("Game over!")
        break
    elif matrix[snake_next_move_r][snake_next_move_c] == BURROW:
        matrix[current_r][current_c] = EMPTY
        spot = (snake_next_move_r, snake_next_move_c)
        matrix[snake_next_move_r][snake_next_move_c] = EMPTY
        new_burrow = [burr for burr in burrows if burr != spot][0]
        snake_next_move_r, snake_next_move_c = new_burrow
        matrix[snake_next_move_r][snake_next_move_c] = SNAKE
        current_r, current_c = snake_next_move_r, snake_next_move_c

    elif matrix[snake_next_move_r][snake_next_move_c] == FOOD:
        matrix[current_r][current_c] = EMPTY
        matrix[snake_next_move_r][snake_next_move_c] = SNAKE    # new spot == "S"
        current_r, current_c = snake_next_move_r, snake_next_move_c
        food_quantity += 1

    elif matrix[snake_next_move_r][snake_next_move_c] == "-":
        matrix[current_r][current_c] = EMPTY
        matrix[snake_next_move_r][snake_next_move_c] = SNAKE
        current_r, current_c = snake_next_move_r, snake_next_move_c

    if food_quantity == 10:
        print("You won! You fed the snake.")
        break

print(f"Food eaten: {food_quantity}")

for el in matrix:
    count = 1
    for char in el:
        print(char, end="")
        if count == side:
            print()
        count += 1