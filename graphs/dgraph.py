import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from base.iterator import iterator

class directed_graph:
    """
        direct graph representation.
        This class provides a set of APIs that provide a common interface
        for a generic undirect graph.
        The data sturcture used to represent the graph is a list of adjacency.
        """
    
    def __init__(self, v):
        if v <= 0:
            raise Exception("number of vertices cannot be <= 0")
        self.v = v
        self.e = 0
        self.adj_list = [None]*v
        for i in range(v):
            self.adj_list[i] = []

def get_number_vertices(self):
    return self.v
    
    def get_number_edges(self):
        return self.e
    
    def add_edge(self,v,w):
        self.validate_vertex(v)
        self.validate_vertex(w)
        self.e += 1
        self.adj_list[v].append(w)
    
    def get_adj_list(self,v):
        self.validate_vertex(v)
        return iterator(self.adj_list[v])
    
    def get_degree(self, v):
        self.validate_vertex(v)
        return len(self.adj_list[v])
    
    def validate_vertex(self,v):
        if v < 0 or v>=self.v:
            raise Exception("Index out of bound")
