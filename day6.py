# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 00:44:15 2020

@author: rundx
"""

f = open('day6.txt','r')




def part1():
    count = 0
    groupYes = set()
    for line in f:
        tempLine = line.rstrip()
        if len(tempLine) > 0:
            for char in tempLine:
                groupYes.add(char)
        else:
            count += len(groupYes)
            groupYes =set()

    print(count)


def part2():
    count = 0
    dictYes = dict()
    groupMembers = 0
    for line in f:
        tempLine = line.rstrip()
        if len(tempLine) > 0:
            groupMembers += 1
            for char in tempLine:
                if char in dictYes:
                    dictYes[char] += 1
                else:
                    dictYes[char] = 1
        else:
            count += sum([1 for x in dictYes.values() if x == groupMembers])
            dictYes = dict()
            groupMembers = 0
    
    print(count)
    
part2()