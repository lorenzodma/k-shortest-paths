from Classi import Edge, Graph, Node 
import pandas as pd
import math
import json

mydata = pd.read_csv(".\\mydata.csv")

grafo = Graph()
#todo per ogni fermata creare un nodo
solo_fermate = mydata.loc[:, "stop_name"]
stop_name_to_node = {}
for fermata in solo_fermate:
    if stop_name_to_node.get(fermata) is None:
        stop_name_to_node[fermata] = Node(grafo, fermata)
    
#todo per ogni volta che lo stop sequence è > 1 creare un arco con la fermata precedente, con peso = time delta
for index,row in mydata.iterrows():
    print(index)
    if row['stop_sequence'] > 1:
        prev = mydata.iloc[index - 1]
        Edge(grafo, int(row['time_delta']), stop_name_to_node[prev['stop_name']], stop_name_to_node[row['stop_name']])

with open("grafo.json", "w+") as file:
    json.dump(grafo, file, default=lambda x: x.toJSON())
