from random import randint, choice

RULES = 'What is the result of the expression?'


def math_operation(a, b, operation):
    if operation == "+":
        result = f'{a + b}'
    elif operation == "-":
        result = f'{a - b}'
    else:
        result = f'{a * b}'
    return str(result)


def game_generator():
    a = randint(1, 10)
    b = randint(1, 10)
    operation = choice(['+', '-', '*'])
    task = f'{a} {operation} {b}'
    result = math_operation(a, b, operation)
    return task, result
