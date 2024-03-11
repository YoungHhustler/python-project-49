import random


RULES = "What number is missing in the progression?"


def game_generator():
    length_progresson = random.randint(5, 10)  # длинна прогрессии
    step_progression = random.randint(2, 5)  # шаг прогрессии
    start_prog = random.randint(1, 15)  # число начала прогрессии
    current = start_prog
    po = []
    for i in range(length_progresson):
        current += step_progression  # прибавляем шаг прогрессии
        po.append(current)
    index = random.randint(0, len(po) - 1)
    result = po[index]
    po[index] = '..'
    task = ' '.join([str(x) for x in po])
    return task, str(result)
