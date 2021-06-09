def operate(operator, *numbers):
    def get_initial_value(operator):
        if operator == "+":
            return 0
        elif operator == "/":
            return numbers[0]
        elif operator == "-":
            return numbers[0]
        else:
            return 1

    result = get_initial_value(operator)


    if operator == "+":
        for i in numbers:
            result += i
    elif operator == "-":
        for i in range(1, len(numbers)):
            result -= numbers[i]
    elif operator == "*":
        for i in numbers:
            result *= i
    else:
        for i in range(1, len(numbers)):
            result /= numbers[i]
    return result


print(operate("+", 100, 50))
print(operate("*", 100, 10))
print(operate("/", 100, 5))
print(operate("-", 100, 5))
