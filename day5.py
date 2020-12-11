# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 14:13:49 2020

@author: rundx
"""

import sys

tickets = []

f = open('day5.txt', 'r')

for line in f:
    tickets.append(line.rstrip())
    
def binaryRow(rowID):
    minRow = 0
    maxRow = 127
    for char in rowID:
        if char == 'F':
            maxRow = (minRow + maxRow)//2 
        if char == 'B':
            minRow = (minRow + maxRow)//2 + 1 

    return minRow

def binaryCol(rowID):
    minRow = 0
    maxRow = 7
    for char in rowID:
        if char == 'L':
            maxRow = (minRow + maxRow)//2
        if char == 'R':
            minRow = (minRow + maxRow)//2 + 1

    return minRow
    
def convertTicket(seatString):
    rowID = seatString[:7]
    colID = seatString[7:]
    
    
    row = binaryRow(rowID)
    col = binaryCol(colID)
    
    
    seatID = 8*row + col
    return seatID





ticketIDs = []

for ticket in tickets:
    ticketIDs.append(convertTicket(ticket))

print(max(ticketIDs))

maxID = max(ticketIDs)
minID = min(ticketIDs)

for i in range(minID,maxID+1):
    if i not in ticketIDs:
        print(i)