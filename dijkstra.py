import math
from Classi import *


def dijkstra(start: Node, finish: Node, grafo: Graph):        
    #N = grafo.nodes[:] #Nodi del grafo
    V = []  #Nodi visitati
    S = []
    S.append(start)
        
    d_z = {}
    perc_migliori : dict[Node, list[Node]] = {}
    
    perc_migliori[start] = [start]

    #Inizializzazione 
    for nodo in grafo.nodes:
        if nodo == start:
            d_z[nodo] = 0
        else:
            d_z[nodo] = math.inf
    #Elaborazione
    while S:
        #print(S)
        #devo rimuovere il nodo con d_z minore da S e metterlo in V
        valore_minimo = math.inf
        nodo_da_rimuovere = None
        for nodo in S:
            #print(S)
            #print(d_z)
            if d_z[nodo] < valore_minimo:
                nodo_da_rimuovere = nodo
                valore_minimo = d_z[nodo]
        S.remove(nodo_da_rimuovere)
        V.append(nodo_da_rimuovere)
        for edge in nodo_da_rimuovere.edges:
            if edge not in grafo.edges:
                continue
            dest_node = edge.destination
            if d_z[nodo_da_rimuovere] + edge.weight < d_z[dest_node]:
                d_z[dest_node] = d_z[nodo_da_rimuovere] + edge.weight
                if edge.source in perc_migliori:
                    perc_migliore_pred = perc_migliori[edge.source].copy() 
                    perc_migliore_pred.append(dest_node)
                    perc_migliori[dest_node] = perc_migliore_pred
                else:
                    return None
                if dest_node not in S and dest_node not in V:
                    S.append(dest_node)
        if finish in V:
            break
    return perc_migliori[finish] if finish in perc_migliori else None
                
                
               
            
