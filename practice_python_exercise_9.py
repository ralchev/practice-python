#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
too high, or exactly right. (Hint: remember to use the user input lessons 
from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends,
print this out.
"""

import random

number = random.randint(1, 10)
guess = 0
trials = 0

while guess != number and guess != "exit":
    guess = input("Please guess the number between 1 and 9. If you want to stop the game, just enter 'exit': ")

    if guess == "exit":
        print("GAME OVER!")
        break
    
    guess = int(guess)
    trials += 1
    if guess not in range(1, 10):
        print("Your guess has to be a number between 1 and 9!")
    elif guess < number:
        print("Your guess is low!")
    elif guess > number:
        print("your guess is high!")
    else:
        if trials == 1:
            print("You guessed it right away!")
        else:
            print("You guessed it in " + str(trials) + " trials")