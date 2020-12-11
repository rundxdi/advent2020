# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:24:23 2020

@author: rundx
"""

import itertools

f = open('day9.txt','r')

entries = []

for line in f:
    entries.append(int(line.rstrip()))
    
def sums(index):
    return [x+y for (x,y) in itertools.combinations(entries[index-25:index],2)]

def contiguousSums(length):
    return [sum(entries[x:x+length]) for x in range(len(entries)-length)]


for i in range(25,len(entries)):
    validSums = sums(i)
    if entries[i] not in validSums:
        print(entries[i])
        
target = 57195069

i = 2

while i < len(entries):
    validSums = contiguousSums(i)
    if target in validSums:
        x = validSums.index(target)
        y = x+i
        minVal = min(entries[x:y])
        maxVal = max(entries[x:y])
        weak = minVal + maxVal 
        print(weak)
        break
    i += 1