import prompt


def launch(games):
    print('Welcome to the brain games!')
    name = prompt.string('May i have your name ? ')
    print(f'Hello, {name}!')
    score = 0
    print(games.RULES)

    while score < 3:
        task, result, = games.game_generator()
        print(f'Question: {task}')
        answer = input('Your answer: ')
        if answer == result:
            print('Correct!')
        score += 1
        if answer != result:
            print(f'\'{answer}\' is wrong answer ;(.\
Correct answer was \'{result}\'')
            print(f'Let\'s try again {name}')
            break
        if score == 3:
            print(f'Congratulations, {name}!')
