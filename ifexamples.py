#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:59:08 2021

@author: EduardoWork
"""
number = input('Give me a number please: ')

try:
    number = int(number)
except ValueError:
    print('That was not a number')
else:
    if number % 2 == 0:
        print('Your number is even')
    else:
        print('Your number iss odd')
