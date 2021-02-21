#! python3
import random

def guessing_game():
    x = random.randint(0,100)
    while 1:
        guess = int(input('Please guess a random integer between 0 and 100, inclusive:\n')) 
        if guess < x:
            print('Too low')
        elif guess > x:
            print('Too high')
        else:
            print('Just right')
            break

guessing_game()
