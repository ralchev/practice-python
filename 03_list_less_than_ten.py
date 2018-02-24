#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

user_number = int(input("Give me a number please!"))

new_list = []
new_list_for_user = []

for number in a:
    if number < 5:
        new_list.append(number)
        
print(new_list)

for number in a:
    if number < user_number:
        new_list_for_user.append(number)

print("And this is a list for you \n" + str(new_list_for_user))