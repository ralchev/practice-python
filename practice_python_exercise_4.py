#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Create a program that asks the user for a number and then prints out a list
of all the divisors of that number. (If you don’t know what a divisor is,
it is a number that divides evenly into another number. For example,
13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

number = int(input("Please give me a number!"))

# Since we want to see all of the divisors, we want to check for all numbers from 1 to the number we are dividing.
div_numbers = range(1, number+1)

divisor_list = []

for div_number in div_numbers:
    if number % div_number == 0:
        divisor_list.append(div_number)

print(divisor_list)