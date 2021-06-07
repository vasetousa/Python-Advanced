# WHEN YOU PRINT FLOATS OR INTEGERS, BUT YOU NEED TO FORMAT WITH :.2f,
# USE THE LAMBDA, row 6
# data = {Peter: (4.50, 3.60)}      # list as a value in dictionary
# for key, value in data.items():
#     avg = sum(value)/len(value)
#     grades = ' '.join(map(lambda grade: f'{grade:.2f}', value))
#     print(f"{key} -> {grades} (avg: {avg:.2f})")

# PPRINT
# from pprint import pprint
# pprint(matrix) prints the matrix properly


print(" ".join(str(x) for x in row))   # reverse the ints to strings to be able to .join()