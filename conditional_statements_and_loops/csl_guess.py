#Write a Python program to guess a number between 1 to 9.

import random
target = 0
guess = random.randint(1,10)

while target != guess:
    guess = int(input('Guess a number between 1 and 10 until you get it right : '))
print("Well guessed!")
