from Classi import *
from dijkstra import dijkstra
from yen import yen
import time
import random

grafo = Graph()

C = Node(grafo, 'C')
D = Node(grafo, 'D')
E = Node(grafo, 'E')
F = Node(grafo, 'F')
G = Node(grafo, 'G')
H = Node(grafo, 'H')

Edge(grafo, 3, C, D)
Edge(grafo, 2, C, E)
Edge(grafo, 1, E, D)
Edge(grafo, 2, E, F)
Edge(grafo, 4, D, F)
Edge(grafo, 3, E, G)
Edge(grafo, 2, F, G)
Edge(grafo, 1, F, H)
Edge(grafo, 2, G, H)

#print(dijkstra(C, H, grafo))
#print(yen(C, H, 3, grafo))

execution_time = 0
for i in range(100):
    print(i)
    start = random.choice(grafo.nodes)
    finish = random.choice(grafo.nodes)
    print(start,",",finish)
    start_time = time.time()
    yen(start, finish, 2, grafo)
    end_time = time.time()
    execution_time += end_time - start_time
    print(execution_time/(i+1))