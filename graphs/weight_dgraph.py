from base.iterator import iterator
class weight_direct_graph:
    """ Abstraction for a direct graph with weighted edges """    
    
    def __init__(self, v):
        self.v = v                                    
        self.e = 0
        self.adj_list = [None] * v                    
        for i in range(v):
            self.adj_list[i] = []                     

    def V(self):
        return self.v
    
    def E(self):
        return self.e
    
    def degree(self, v):
        return len(self.adj_list[v])
                                                      
    def add_edge(self, e):
        v = e.v
        w = e.w
        self.adj_list[v].append(e)
        self.e += 1
        
    def edges_vertex(self, v):
        return iterator(self.adj_list[v])
    
    def edges(self):
        l = []
        for v in range(self.V()):
            for e in self.adj_list[v]:
                l.append(e)
        return l
