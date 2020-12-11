# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 12:11:29 2020

@author: rundx
"""

import networkx as nx
import itertools
import datetime


timestart = datetime.datetime.now()

f = open('day10.txt','r')

ratings = [int(line.rstrip()) for line in f]
f.close()

g = nx.DiGraph()

for rating in ratings:
    g.add_node(rating)
    
ratings.append(0)
ratings.append(max(ratings) + 3)
g.add_node(0, demand = -1)
g.add_node(max(ratings), demand = 1)
ratings = sorted(ratings)
    
for (n1,n2) in itertools.combinations(g.nodes,2):
    if n2 - n1 <=3 and n2-n1 >=0:
        g.add_edge(n1,n2, cost = -1)
    elif n1 - n2 <=3 and n1 - n2 >=0:
        g.add_edge(n2,n1, cost = -1)

flowDict = nx.min_cost_flow(g, demand = 'demand', weight = 'cost')

seq = sorted([i for (i,j) in g.edges if flowDict[i][j]])
seq.append(max(ratings))

jump1 = 0
jump3 = 0


for (i,j) in nx.utils.pairwise(seq):
    if j == i + 1:
        jump1 += 1
    if j == i + 3:
        jump3 += 1
             
print(jump1*jump3)

visitList = list(reversed(list(nx.topological_sort(g))))

paths = [0]*len(ratings)


def numPaths(node):
    if node == 0:
        paths[-1] = 1
    else:
        paths[-node-1] = sum([paths[ratings.index(child)] for child in g.successors(visitList[node])])
    

for node in visitList:
    numPaths(visitList.index(node))
    
print(paths[0])
timeend = datetime.datetime.now()
print(f'Time to complete: {timeend - timestart}')