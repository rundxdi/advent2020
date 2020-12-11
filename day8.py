# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 08:55:48 2020

@author: rundx
"""
import sys

f = open('day8.txt','r')

instructions = []

for line in f:
    tempLine = line.rstrip().split()
    instructions.append((tempLine[0],int(tempLine[1])))
    
stepTrace = []

def nop(step):
    return step + 1

def acc(step):
    return instructions[step][1]

def jmp(step):
    return instructions[step][1]


changes = []


accum = 0
step = 0
while step< len(instructions):
    #print('step',step)
    stepTrace.append(step)
    whatDo = instructions[step][0]
    if whatDo == 'nop':
        lastChange = step
        step = nop(step)
    elif whatDo == 'acc':
        accum += acc(step)
        step += 1
    else:
        lastChange = step
        step += jmp(step)
    if step in stepTrace:
        break

        
    
print(accum)

for i in range(len(instructions)):
    newInstructions = instructions.copy()
    if instructions[i][0] == 'jmp':
        newInstructions[i] = ('nop', instructions[i][1])
    elif instructions[i][0] == 'nop':
        newInstructions[i] = ('jmp', instructions[i][1])
    accum = 0
    step = 0
    stepTrace = []
    while step< len(instructions):
        #print('step',step)
        stepTrace.append(step)
        whatDo = newInstructions[step][0]
        if whatDo == 'nop':
            step = nop(step)
        elif whatDo == 'acc':
            accum += acc(step)
            step += 1
        else:
            step += jmp(step)
        if step in stepTrace:
            break
        if step == len(instructions):
            print(accum)
            sys.exit()
