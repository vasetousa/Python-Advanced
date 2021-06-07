def read_matrix(is_test=False):
    if is_test:
        return [
            [1, 2, 3],
            [4, 5, 6],
        ]
    else:
        rows, columns = [int(el) for el in (input().split())]
        matrix = []
        for r in range(rows):
            x = input().split()
            matrix.append(x)
        return matrix

matrix = read_matrix()  # for local testing use matrix = read_matrix(is_test=True)
# pprint(matrix)

command = input()

while not command == "END":
    if command.startswith("swap"):
        try:
            command_string, row_1, col_1, row_2, col_2 = command.split()
            row_1 = int(row_1)
            row_2 = int(row_2)
            col_1 = int(col_1)
            col_2 = int(col_2)
            x = matrix[row_1][col_1]
            matrix[row_1][col_1] = matrix[row_2][col_2]
            matrix[row_2][col_2] = x
            for el in matrix:
                print(*el)

        except:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()
