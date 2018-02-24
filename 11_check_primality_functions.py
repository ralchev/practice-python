#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ask the user for a number and determine whether the number is prime or not.
"""

def is_prime():
    number = int(input("Please give me a number! Press Ctrl + C if you want to stop."))

    list_of_divisors = [divisor for divisor in range(2, number) if number % divisor == 0]

    if number > 1 and len(list_of_divisors) == 0:
        print(number, "is prime")
    elif number > 1 and len(list_of_divisors) != 0:
        print(number, "is not prime")
    else:
        print("Something is wrong here")
        
while True:
    is_prime()