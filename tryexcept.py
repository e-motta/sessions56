#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:22:37 2021

@author: EduardoWork
"""

age = input('How old are you? ')

try:
    age = int(age)
except ValueError:
    print('Sorry, but that was not a number.')
else:
    print('You were born around', 2021-age)
finally:
    print('Finished')
