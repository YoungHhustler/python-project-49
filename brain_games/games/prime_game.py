import random
RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_generator():
    rndm_num = random.randint(1, 3572)
    task = rndm_num
    count = 0
    for i in range(1, rndm_num + 1):
        if rndm_num % i == 0:
            count += 1
    if count == 2:
        result = 'yes'
    else:
        result = 'no'
    return task, result
