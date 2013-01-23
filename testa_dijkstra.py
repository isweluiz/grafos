#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Dijkstra as d
import networkx as nx
import numpy as n
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_node('t')
G.add_node('x')
G.add_node('s')
G.add_node('y')
G.add_node('z')

G.add_edge('s', 't', weight=10)
G.add_edge('t', 'x', weight=1)
G.add_edge('s', 'y', weight=5)
G.add_edge('t', 'y', weight=2)
G.add_edge('y', 'z', weight=2)
G.add_edge('y', 't', weight=3)
G.add_edge('y', 'x', weight=9)
G.add_edge('x', 'z', weight=4)
G.add_edge('z', 'x', weight=6)
G.add_edge('z', 's', weight=7)

H = d.Dijkstra(G, 's')

nx.draw(H)
plt.show()
