# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 16:04:12 2020

@author: rundx
"""

import numpy as np

f = open('day12.txt','r')

dirs = ['E','S','W','N']
facing = 'E'
position = [0,0]

orders = [line.rstrip() for line in f]
'''
for order in orders:
    if order[0] == 'R':
        print(facing, order[1:])
        facing = dirs[(dirs.index(facing) + int(order[1:])//90) % 4]
        print(facing)
    elif order[0] == 'L':
        facing = dirs[(dirs.index(facing) - int(order[1:])//90) % 4]
    elif order[0] == 'F':
        direction = facing
        if direction == 'N':
            position[1] += int(order[1:])
        elif direction == 'E':
            position[0] += int(order[1:])
        elif direction == 'S':
            position[1] -= int(order[1:])
        elif direction == 'W':
            position[0] -= int(order[1:])
    else:
        direction = order[0]
        if direction == 'N':
            position[1] += int(order[1:])
        elif direction == 'E':
            position[0] += int(order[1:])
        elif direction == 'S':
            position[1] -= int(order[1:])
        elif direction == 'W':
            position[0] -= int(order[1:])

print(position)
'''
waypoint = [10,1]

for order in orders:
    if order[0] == 'R':
        theta = np.radians(360-int(order[1:]))
        cos = np.cos(theta)
        sin = np.sin(theta)
        M = np.round(np.array(((cos,-sin),(sin,cos))))
        waypoint = list(np.round(np.matmul(M,waypoint)))
    elif order[0] == 'L':
        theta = np.radians(int(order[1:]))
        cos = np.cos(theta)
        sin = np.sin(theta)
        M = np.round(np.array(((cos,-sin),(sin,cos))))
        waypoint = list(np.round(np.matmul(M,waypoint)))
    elif order[0] == 'F':
        position[0],position[1] = position[0]+int(order[1:])*waypoint[0], position[1]+int(order[1:])*waypoint[1]
    else:
        direction = order[0]
        if direction == 'N':
            waypoint[1] += int(order[1:])
        elif direction == 'E':
            waypoint[0] += int(order[1:])
        elif direction == 'S':
            waypoint[1] -= int(order[1:])
        elif direction == 'W':
            waypoint[0] -= int(order[1:])
            

print(position)