# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 13:16:29 2020

@author: rundx
"""

import networkx as nx
import itertools

f = open('day11.txt','r')

seats = []

for line in f:
    seats.append([char for char in line.rstrip()])
    
g1 = nx.Graph()
g2 = nx.Graph()


for i in range(len(seats)):
    for j in range(len(seats[i])):
        g1.add_node((i,j), seat = seats[i][j])
            
adjacencyPairs = list(itertools.product([-1,0,1],[-1,0,1]))
adjacencyPairs.remove((0,0))

for node in g1.nodes:
    for pair in adjacencyPairs:
        if (node[0]+pair[0], node[1]+pair[1]) in g1.nodes:
            g1.add_edge((node[0],node[1]),(node[0] + pair[0],node[1] + pair[1]))

        
#part 1
'''
while nx.get_node_attributes(g1,'seat') != nx.get_node_attributes(g2,'seat'):
    g2 = g1.copy()
    for node in g2.nodes:
        if g2.nodes[node]['seat'] == 'L' and '#' not in [g2.nodes[x]['seat'] for x in g2.neighbors(node)]:
            g1.nodes[node]['seat'] = '#'
        elif g2.nodes[node]['seat'] == '#' and [g2.nodes[x]['seat'] for x in g2.neighbors(node)].count('#') >=4:
            g1.nodes[node]['seat'] = 'L'
            
print(list(nx.get_node_attributes(g1,'seat').values()).count('#'))
'''
def lineOfSight(node):
    directions = dict()
    firstNode = node
    for pair in adjacencyPairs:
        node = firstNode
        while (node[0]+pair[0], node[1]+pair[1]) in g1.nodes:
            node = (node[0]+pair[0], node[1]+pair[1])
            if g2.nodes[node]['seat'] == 'L':
                break
            if g2.nodes[node]['seat'] == '#':
                directions[node] = '#'
                break
    if list(directions.values()).count('#') >= 5:
        return '#'
    elif list(directions.values()).count('#') == 0:
        return 'L'
   
    
while nx.get_node_attributes(g1,'seat') != nx.get_node_attributes(g2,'seat'):
    g2 = g1.copy()
    for node in g2.nodes:
        if g2.nodes[node]['seat'] == 'L' and lineOfSight(node) == 'L':
            g1.nodes[node]['seat'] = '#'
        elif g2.nodes[node]['seat'] == '#' and lineOfSight(node) == '#':
            g1.nodes[node]['seat'] = 'L'
            
print(list(nx.get_node_attributes(g1,'seat').values()).count('#'))