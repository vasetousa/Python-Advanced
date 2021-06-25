def is_hit_valid(matrix, row, col):
    if row not in range(0, len(matrix)-1):
        return False
    elif col not in range(0, len(matrix)-1):
        return False
    return True


def get_current_result_from_four_numbers(matrix, letter):
    global current_score
    el1_row = row
    el1_col = 0
    num1 = matrix[el1_row][el1_col]
    el2_row = 0
    el2_col = col
    num2 = matrix[el2_row][el2_col]
    el3_row = len(matrix) - 1
    el3_col = col
    num3 = matrix[el3_row][el3_col]
    el4_row = row
    el4_col = len(matrix) - 1
    num4 = matrix[el4_row][el4_col]
    if letter == "D":
        current_score = (int(num1) + int(num2) + int(num3) + int(num4)) * 2
    elif letter == "T":
        current_score = (int(num1) + int(num2) + int(num3) + int(num4)) * 3
    elif str(letter).isdigit():
        current_score = letter
        return int(current_score)
    return int(current_score)


def read_matrix(is_test=False):
    if is_test:
        return [
            [17,  8,  21,   6,  13,   3,  24],
            [16, 'D', 'D', 'D', 'D', 'D', 14],
            [ 7, 'D', 'T', 'T', 'T', 'D', 15],
            [23, 'D', 'T', 'B', 'T', 'D',  2],
            [ 9, 'D', 'T', 'T', 'T', 'D', 22],
            [19, 'D', 'D', 'D', 'D', 'D', 10],
            [12, 18,   4,  20,   5,   11,  1]
        ]

    else:
        side = 7
        matrix = []
        for r in range(side):
            x = [el for el in (input().split())]
            matrix.append(x)
        return matrix


player_list = input().split(', ')
matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
""" D - sum(corresponding 4 numbers) * 2, T - sum(corresponding 4 numbers) * 3, B i wins the game """
""" any number hit is deducted from the score """

from collections import deque

players_scores_list = (501, 501)
players = deque(player_list)                                            # !!!
players_score = deque(players_scores_list)                              # !!!
throw_counter_list = (0, 0)
throw_counter = deque(throw_counter_list)                               # !!!

while True:
    coordinates = input().split(", ")
    row = coordinates[0][1:]
    col = coordinates[1][:-1]
    row = int(row)
    col = int(col)
    current_player = players.popleft()
    current_total_score = players_score.popleft()
    current_throw_counter = throw_counter.popleft()
    current_throw_counter += 1
    if not is_hit_valid(matrix, row, col):  # player missed the board, next player turn
        players.append(current_player)  # adding player back to the end of the queue
        players_score.append(current_total_score)  # adding player score back to the end of the queue
        throw_counter.append(current_throw_counter)
        continue
    current_hit = matrix[row][col]
    if current_hit == 'B':
        """Game over"""
        break

    current_result = get_current_result_from_four_numbers(matrix, current_hit)
    result = current_total_score - current_result  # player score minus the number in current cell
    if result <= 0:  # result dropped under 0, current player wins
        break
    players.append(current_player)  # adding player back to the end of the queue
    players_score.append(result)   # adding player score back to the end of the queue
    throw_counter.append(current_throw_counter)

print(f"{current_player} won the game with {current_throw_counter} throws!")
