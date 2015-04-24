from base.iterator import iterator
from disjoint_set import disjoint_set

class MST:

    """ 
    Abstraction for generic spanning tree algorithm
    """
    def __init__(self, weighted_graph):
        self.mst = []
        self.weight = 0.0
        self.__kruskal_mst(weighted_graph)

    def edges(self):
        return self.mst

    def weight(self):
        return self.weight

    def __kruskal_mst(self, G):
        """
        Kruskal algorithm:
        - Consider edges in ascending order of weight
        - Add next edge to T mst unless this creates a cycle
        Total complexity E*Lg(V)
        """
        l = []      
        for v in range(G.V()):
            l.append(v)
        
        djs = disjoint_set(l)
        edges = G.edges()
        edges.sort() # a priority queue would do the same job of sorting
        
        for e in edges:
            v,w,weight = e
            if djs.find(v) != djs.find(w):
                djs.union(v,w)
                self.mst.append(e)
                self.weight += e.weight
        



