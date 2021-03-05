#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 14:39:35 2021

@author: EduardoWork
"""

while True:
    try:
        gross = int(input('Gross income: '))
        kids = int(input('Number of kids: '))
        break
    except ValueError:
        print('Enter numbers only')

if kids > 10:
    kids = 10

tax = 0

if gross < 1000:
    tax = 10
elif gross < 2000:
    tax = 12
elif gross < 4000:
    tax = 14
else:
    tax = 18

if gross < 2000:
    tax = tax - (kids*1)
else:
    tax = tax - (kids*0.5)

print(f'Gross: {gross}; Kids: {kids}; Net: {gross*(100-tax)/100}')
