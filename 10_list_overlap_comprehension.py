#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.
Write this using at least one list comprehension.
"""

import random

a = random.sample(range(1, 3000), 50)
b = random.sample(range(1, 3000), 100)

common_numbers = [number for number in set(a) if number in b] # sets cannot have duplicates
        
print(common_numbers)