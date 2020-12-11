# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 07:16:59 2020

@author: rundx
"""

import networkx as nx
import matplotlib.pyplot as plt; plt.ion()


g = nx.DiGraph()

f = open('day7.txt','r')

for line in f:
    tempLine = line.rstrip().split(' contain ')
    container = tempLine[0].split('bag')[0]
    contained = [x.split(' bag')[0] for x in tempLine[1].split(', ')]
    g.add_node(container.rstrip(' '))
    if contained != ['no other']:
        for bagType in contained:
            g.add_edge(container.rstrip(' '), bagType[2:].rstrip(' '), holds = int(bagType[0]))

holders = nx.ancestors(g,'shiny gold')

print(len(holders))

## Part 2

stuff = nx.descendants(g,'shiny gold')
stuff.add('shiny gold')

gold = g.subgraph(stuff)

paths = []
for node in gold.nodes:
    if gold.out_degree(node) == 0:
        print(len(list(nx.all_simple_edge_paths(gold, 'shiny gold', node))))
        for path in nx.all_simple_edge_paths(gold, 'shiny gold', node):
            paths.append(path)
        
totalBags = 0
gold.nodes['shiny gold']['bags'] = 1

def add_bags(node):
    for cNode in gold.successors(node):
        if gold.nodes[cNode].get('bags'):
            gold.nodes[cNode]['bags'] += gold.nodes[node]['bags']*gold.edges[(node,cNode)]['holds']
        else:
            gold.nodes[cNode]['bags'] = gold.nodes[node]['bags']*gold.edges[(node,cNode)]['holds']

order = list(nx.topological_sort(gold))

for node in order:
    add_bags(node)
    
totalBags = -1
for node in gold.nodes:
    totalBags += gold.nodes[node]['bags']
      
print(totalBags)