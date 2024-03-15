import prompt

SCORE_FOR_WIN = 3


def launch(games):
    print('Welcome to the brain games!')
    name = prompt.string('May i have your name ? ')
    print(f'Hello, {name}!\n{games.RULES}')

    score = 0

    while score < SCORE_FOR_WIN:
        task, result, = games.game_generator()
        print(f'Question: {task}')
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
        score += 1
        if answer != result:
            print(f'\'{answer}\' is wrong answer ;(.\
Correct answer was \'{result}\'')
            print(f'Let\'s try again, {name}!')
            break
        if score == 3:
            print(f'Congratulations, {name}!')
