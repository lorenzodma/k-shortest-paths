from Classi import *
from dijkstra import dijkstra
from yen import yen

grafo = Graph()

A = Node(grafo, 'A')
B = Node(grafo, 'B')
C = Node(grafo, 'C')
D = Node(grafo, 'D')
E = Node(grafo, 'E')
F = Node(grafo, 'F')
G = Node(grafo, 'G')

Edge(grafo, 2, A, C)
Edge(grafo, 4, B, E)
Edge(grafo, 9, C, D)
Edge(grafo, 3, E, G)
Edge(grafo, 4, D, F)

print(dijkstra(A, G, grafo))
#print(yen(A, G, 2, grafo))