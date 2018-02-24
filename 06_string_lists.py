#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

word = str(input("Please give me a word!"))
reversed_word = word[::-1] # Going the pythonic way!

if reversed_word == word:
    print("It is a palindrome!")
else:
    print("It is not a palindrome!")