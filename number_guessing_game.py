#number guessing game

import random
print('Welcome to Number Guessing Game!\nYou will be guessing between 1-10')

play = 'yes'

while play[0] != 'n':
    number = random.randint(1, 10)
    guess = -1
    while number != guess:
        guess = int(input('Enter your guess: '))
        if guess < number:
            print('Try something bigger!')
        elif guess > number:
            print('try something lesser!')
        
    print('YOU DID IT!')
    play = input('Wanna play again? [yes/no]: ')
