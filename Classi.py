#Creo classi grafo, archi, nodi
class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node:'Node'):
        self.nodes.append(node)

    def add_edge(self, edge:'Edge'):
        self.edges.append(edge)
    
    def remove_edge(self, edge:'Edge'):
        self.edges.remove(edge)
    
    
    def toJSON(self):
        d = {}
        for key, val in self.__dict__.items():
            if isinstance(val, list):
                d[key] = [v.toJSON() for v in val]
        return d
    

class Edge:
    def __init__(self, graph:'Graph', weight:int, source:'Node', destination:'Node'):
        graph.add_edge(self)
        self.weight = weight
        self.source = source
        source.add_edge(self)
        self.destination = destination
        destination.add_edge(self)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return (self.weight == other.weight and self.source == other.source and self.destination == other.destination) 
          
    def __hash__(self):
        return hash((self.weight, self.source, self.destination))
    
    def __str__(self):
        return 'ARCO: ' + str(self.weight) + ' ' + str(self.source) + '->' + str(self.destination)
    
    def __repr__(self):
        return 'ARCO: ' + str(self.weight) + ' ' + str(self.source) + '->' + str(self.destination)
    
    def toJSON(self):
        d = {}
        for key, val in self.__dict__.items():
            if type(val) == Node:
                d[key] = val.toJSON()
            else:
                d[key] = val
        return d


class Node:
    def __init__(self, graph:'Graph', name):
        graph.add_node(self)
        self.name = name
        self.edges = []
        
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.name == other.name
          
    def __hash__(self):
        return hash(self.name)
        
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def add_edge(self, edge:'Edge'):
        self.edges.append(edge)
    def toJSON(self):
        d = {}
        for key, val in self.__dict__.items():
            if not isinstance(val, list):
                d[key] = val
        return d
