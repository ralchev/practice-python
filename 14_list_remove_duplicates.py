#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

@author: ralchev
"""

def resolve_dupl(list):
    resolved = []
    for item in list:
        if item not in resolved:
            resolved.append(item)
    return resolved
