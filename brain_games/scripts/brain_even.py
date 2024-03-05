#!/usr/bin/env python3
from random import randint
import prompt

print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!')
print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    count = 0
    while count < 3:
        x = randint(1, 100)
        print(f'Question:{x}')
        answer = input('Your answer:')
        if answer != 'no' and answer != 'yes':
            print('incorrect input')
            break
        if x % 2 == 0 and answer == 'yes' or x % 2 != 0 and answer == 'no':
            print('Correct!')
            count += 1
        if x % 2 == 0 and answer == 'no':
            print("'no' is wrong answer ;(. Correct answer was 'yes'")
            print(f'Let\'s try again {name}')
        elif x % 2 != 0 and answer == 'yes':
            print("'yes' is wrong answer ;(. Correct answer was 'no'")
            print(f'Let\'s try again {name}')
            break
        if count == 3:
            print(f'Congratulations, {name}!')


