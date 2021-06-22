def math_ops(x, y, operation):
    result = 0
    if operation == "*":
        return multiply(x, y)
    elif operation == "/":
        return division(x, y)
    elif operation == "+":
        return summarize(x, y)
    elif operation == "-":
        return subtract(x, y)
    elif operation == "^":
        return exponentiation(x, y)


def summarize(x, y):
    return x + y


def division(x, y):
    return x / y


def multiply(x, y):
    return x * y


def subtract(x, y):
    return x - y


def exponentiation(x, y):
    return x ** y
