import math
import json
from Classi import *
from dijkstra import dijkstra
from costo import costo
from yen import yen
import time
import random


with open('grafo.json') as data_file:
    x = json.load(data_file)
    

grafo = Graph()
map_names_to_node = {}

for node in x['nodes']:
    map_names_to_node[node['name']] = Node(grafo, name = node['name'])

for edge in x['edges']:
    Edge(grafo, edge['weight'], map_names_to_node[edge['source']['name']], map_names_to_node[edge['destination']['name']])

#print(json.dumps(grafo, default=lambda x: x.toJSON()))

grafo.edges = list(set(grafo.edges))
grafo.nodes = list(set(grafo.nodes))

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
# 
# partenza = map_names_to_node["Is Mirrionis (ang. via Montesanto)"]
# arrivo = map_names_to_node["Lungosaline (ang. via d'Elba)"]
# print(dijkstra(partenza,arrivo,grafo))
# print(yen(partenza, arrivo, 2, grafo))
# #print(yen(partenza, arrivo, 2, grafo))
