from Classi import *
from dijkstra import dijkstra
from costo import costo

def yen(start: Node, finish: Node, k: int, grafo):
    #if map_names_to_node[start] in grafo.nodes and map_names_to_node[finish] in grafo.nodes:
    #    start, finish = map_names_to_node[start], map_names_to_node[finish]
    A = [] #lista di liste (le liste sono i cammini minimi) 
    D = dijkstra(start, finish, grafo)
    if D == None:
        return None
    A.append(D)
    indice = 0
    for nodo in D:
        indice += 1
        if indice >= len(D):
            break
        E = grafo.edges[:] #contiene tutti gli archi del grafo
        nodo_succ = D[indice]
        for edge in nodo.edges:
            if nodo_succ == edge.destination and edge in E:
                E.remove(edge)
        #il grafo nuovo deve avere stessi nodi e gli archi di E
        grafo_nuovo = Graph()
        for nodo in grafo.nodes:
            Node(grafo_nuovo, name = nodo.name)
            #print(nodo.name)
        for edge in E:
            Edge(grafo_nuovo, edge.weight, edge.source, edge.destination)
            #print(edge)
        #print(f"dijkstra {indice}")
        perc = dijkstra(start, finish, grafo_nuovo)
        if perc != None and perc not in A:
            A.append(perc)
    #creo un insieme KS_paths con i k percorsi minimi
    paths_and_costs = []
    for path in A:
        c = costo(grafo, path)
        paths_and_costs.append((path, c))
    paths_and_costs = sorted(paths_and_costs, key = lambda t: t[1])
    KS_paths = paths_and_costs[:k]
    #print(A)

    return KS_paths
        

    

        
        
        
        