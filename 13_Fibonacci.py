#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

@author: ralchev
"""

def generate_fibonacci(count):
    numbers = [0, 1]
    while len(numbers) < count:
        next_number = numbers[-1] + numbers[-2]
        numbers.append(next_number)
    print(numbers)

def get_count():
    count = int(input('\nHow many Fibonnaci numbers would you like me to generate for you?'))
    if count < 2:
        print('Come on... We need a bigger number!')
        get_count()
    return generate_fibonacci(count)

get_count()
