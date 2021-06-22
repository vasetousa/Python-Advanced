from Mathematical_operations.operations import math_ops


number1, sign, number2 = input().split()
number1 = float(number1)
number2 = float(number2)
value = (math_ops(number1, number2, sign))
print(f"{value:.2f}")


