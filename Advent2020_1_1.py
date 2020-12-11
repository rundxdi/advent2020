# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:23:34 2020

@author: rundx
"""
import sys

f = open('advent_2020_1_1.txt', 'r')
expenses = []
for line in f:
    expenses.append(int(line.rstrip()))
    
for i in expenses:
    for j in expenses:
        for k in expenses:
            if i+j+k == 2020:
                print(i,j,k,i*j*k)
                sys.exit()