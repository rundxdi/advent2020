# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:19:21 2020

@author: rundx
"""

import numpy as np

f = open('day3.txt', 'r')

path = np.zeros((323,31))


row = 0
for line in f:
    temp = line.rstrip()
    col = 0
    for char in temp:
        if char == '.':
            char = 0
        elif char == '#':
            char = 1
        path[row][col] = char
        col+=1
    row+=1
    
pos = [0,0]

treesHit = 0
while pos[0] < 322:
    pos[0]+=1
    pos[1]+=3
    pos[1] = pos[1] % 31
    print(pos)
    if path[pos[0]][pos[1]] == 1:
        treesHit += 1

prdTrees = treesHit

pos = [0,0]
treesHit = 0
while pos[0] < 322:
    pos[0]+=1
    pos[1]+=1
    pos[1] = pos[1] % 31
    print(pos)
    if path[pos[0]][pos[1]] == 1:
        treesHit += 1
        
prdTrees *= treesHit

pos = [0,0]
treesHit = 0
while pos[0] < 322:
    pos[0]+=1
    pos[1]+=5
    pos[1] = pos[1] % 31
    print(pos)
    if path[pos[0]][pos[1]] == 1:
        treesHit += 1
        
prdTrees *= treesHit

pos = [0,0]
treesHit = 0
while pos[0] < 322:
    pos[0]+=1
    pos[1]+=7
    pos[1] = pos[1] % 31
    print(pos)
    if path[pos[0]][pos[1]] == 1:
        treesHit += 1
        
prdTrees *= treesHit

pos = [0,0]
treesHit = 0
while pos[0] < 322:
    pos[0]+=2
    pos[1]+=1
    pos[1] = pos[1] % 31
    print(pos)
    if path[pos[0]][pos[1]] == 1:
        treesHit += 1
        
prdTrees *= treesHit

print(prdTrees)