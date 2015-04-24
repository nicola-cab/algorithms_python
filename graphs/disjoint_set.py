class disjoint_set:
    """
        Disjoint set is a data structure used to keep track of elements 
        partitionated into a number of disjoint subsets.
        This data structure is real useful because it supports 2 operations:
        - find  -> determine which subset a particular element is in
        - union -> join to subset in a single one
        
        The focal point on this kind of data structure is how to obtain good performances. 
        Essentially this implementation adopts a underlying tree data structure that has to be 
        balanced in order to avoid bad worst case scenarios.
        To balanced the tree I use this simple method. I always attach the root of a smaller tree
        to a larger tree.
    """
    
    def __init__(self, V):
        self.id = {}
        self.rank   = {}
        for v in V:
            self.id[v] = v
            self.rank[v] = 1

    def union(self, v1, v2):
        id1 = self.find(v1)
        id2 = self.find(v2)
        if id1 == id2:
            return
        if self.rank[id1] < self.rank[id2]:
            self.id[id1] = self.id[id2]
            self.rank[id2] += self.rank[id1]
        else:
            self.id[id2] = self.id[id1]
            self.rank[id1] += self.rank[id2]
    
    def find(self, v):
        while self.id[v] != v:
            v = self.id[v]
        return v
        
    def connect(self, v, w):
        return self.find(v) == self.find(w)