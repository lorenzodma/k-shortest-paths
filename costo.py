from Classi import *

def costo(grafo, percorso: list):
    costo_att = 0
    indice = 0
    archi_cons = set()
    
    for nodo in percorso:
        indice += 1
        if indice >= len(percorso):
            break
        nodo_succ = percorso[indice]
        for edge in nodo.edges:
            if nodo_succ == edge.destination and edge not in archi_cons:
                archi_cons.add(edge)
                costo_att = costo_att + edge.weight
    return costo_att
                
# def costo(graph, path:list):
#   cost = 0
#   for source, dest in zip(path, path[1:]):
#     for edge in source.edges:
#       if edge.destination == dest:
#         cost += edge.weight
#         break
#   return cost        
        
    
    
    