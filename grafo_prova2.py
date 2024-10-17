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
H = Node(grafo, 'H')

Edge(grafo, 1, A, B)
Edge(grafo, 3, A, C)
Edge(grafo, 5, A, D)
Edge(grafo, 6, B, E)
Edge(grafo, 6, C, D)
Edge(grafo, 2, C, E)
Edge(grafo, 4, D, F)
Edge(grafo, 9, E, F)
Edge(grafo, 2, F, G)
Edge(grafo, 1, G, H)

print(dijkstra(A, H, grafo))
print(yen(A, H, 2, grafo))

