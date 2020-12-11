# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 15:43:14 2020

@author: rundx
"""

f = open('day2.txt', 'r')

lines = []

for line in f:
    lines.append(line.rstrip())
    

passwordTuples = []
for password in lines:
    new = password.split(' ')
    counts = new[0].split('-')
    passTuple = (int(counts[0]), int(counts[1]), new[1][0], new[2])
    passwordTuples.append(passTuple)
    
valid = 0  
for combo in passwordTuples:
    if combo[-1].count(combo[-2]) <= combo[1] and combo[-1].count(combo[-2]) >= combo[0]:
        valid+=1
        
print(valid)

valid2 = 0

for combo in passwordTuples:
    if combo[1] > len(combo[-1]):
        continue
    if combo[-1][combo[0]-1] == combo[-2] or combo[-1][combo[1]-1] == combo[-2]:
        valid2+=1
    if combo[-1][combo[0]-1] == combo[-2] and combo[-1][combo[1]-1] == combo[-2]:
        valid2-=1
        
print(valid2)