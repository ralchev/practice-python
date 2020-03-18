#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.

@author: ralchev
"""

def reverse_order():
    string = input('\nPlease write a sentence here!\n')
    return ' '.join(string.split()[::1])

reverse_order()