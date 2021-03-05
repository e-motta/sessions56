#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:58:26 2021

@author: EduardoWork
"""

n = 1
result = 0

while n < 10:
    if n % 2 != 0:
        result = result + n
    n = n + 1

print('sum of first 9 odd numbers is', result)
