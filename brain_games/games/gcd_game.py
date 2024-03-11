import math
from random import randint


RULES = "Find the greatest common divisor of given numbers."


def game_generator():
    x = randint(1, 10)
    y = randint(1, 10)
    task = f'{x} {y}'
    result = math.gcd(x, y)
    return task, str(result)
