from random import randint

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_generator():
    task = randint(1, 100)
    result = 'yes' if task % 2 == 0 else 'no'
    return task, result
